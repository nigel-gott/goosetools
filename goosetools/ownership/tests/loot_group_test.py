from django.urls.base import reverse
from freezegun import freeze_time

from goosetools.ownership.models import LootGroup
from goosetools.tests.goosetools_test_case import GooseToolsTestCase


@freeze_time("2012-01-14 12:00:00")
class LootGroupTest(GooseToolsTestCase):
    def an_open_fleet(self, gives_shares_to_alts=False):
        return self.a_fleet(
            start_date="Jan. 14, 2012",
            start_time="11:02 AM",
            gives_shares_to_alts=gives_shares_to_alts,
        )

    def a_loot_group(self, fleet):
        self.post(
            reverse("loot_group_create", args=[fleet.pk]),
            {
                "loot_source": "Anom",
                "name": "MyLootGroupName",
                "anom_level": 6,
                "anom_type": "Scout",
                "anom_faction": "Serpentis",
                "anom_system": self.system.pk,
            },
        )
        return LootGroup.objects.last()

    def test_can_make_a_loot_group(self):
        fleet = self.an_open_fleet()
        self.post(
            reverse("loot_group_create", args=[fleet.pk]),
            {
                "loot_source": "Anom",
                "name": "MyLootGroupName",
                "anom_level": 6,
                "anom_type": "Scout",
                "anom_faction": "Serpentis",
                "anom_system": self.system.pk,
            },
        )

        response = self.get(
            reverse("loot_group_view", args=[LootGroup.objects.last().pk])  # type: ignore
        )
        self.assertEqual(response.context["loot_group"].name, "MyLootGroupName")

    def test_can_join_a_loot_group_as_a_non_admin(self):
        fleet = self.an_open_fleet()
        loot_group = self.a_loot_group(fleet)
        self.client.force_login(self.other_user)
        response = self.get(reverse("loot_group_view", args=[loot_group.pk]))
        self.assertNotIn(
            self.other_char.ingame_name, str(response.content, encoding="utf-8")
        )
        self.post(
            reverse("loot_share_join", args=[loot_group.pk]),
            {"character": self.other_char.pk},
        )
        response = self.get(reverse("loot_group_view", args=[loot_group.pk]))
        self.assertIn(
            self.other_char.ingame_name, str(response.content, encoding="utf-8")
        )

    def test_can_close_a_loot_group_then_non_admins_cant_join(self):
        fleet = self.an_open_fleet()
        loot_group = self.a_loot_group(fleet)
        r = self.post(reverse("loot_group_close", args=[loot_group.pk]))
        self.assert_messages(
            r,
            [
                (
                    "success",
                    "Closed loot group: Serpentis Scout Level 6 @ 2012-01-14 12:00:00+00:00 in Test System (Test Region)",
                )
            ],
        )

        self.client.force_login(self.other_user)
        errors = self.post_expecting_error(
            reverse("loot_share_join", args=[loot_group.pk]),
            {"character": self.other_char.pk},
        )
        self.assertEqual(
            errors, ["[Test Corp] Test Char 2 is not allowed to join this group."]
        )
        self.assertEqual(loot_group.lootshare_set.count(), 0)

    def test_fc_can_still_add_members_to_closed_loot_group(self):
        fleet = self.an_open_fleet()
        loot_group = self.a_loot_group(fleet)

        self.post(reverse("loot_group_close", args=[loot_group.pk]))

        loot_share_info = {
            "character": self.other_char.pk,
            "share_quantity": 1,
            "flat_percent_cut": 0,
        }
        self.post(reverse("loot_share_add", args=[loot_group.pk]), loot_share_info)
        self.assertEqual(
            list(
                loot_group.lootshare_set.values(
                    "character", "share_quantity", "flat_percent_cut"
                ).all()
            ),
            [loot_share_info],
        )

    def test_can_reopen_a_closed_loot_group(self):
        fleet = self.an_open_fleet()
        loot_group = self.a_loot_group(fleet)

        self.post(reverse("loot_group_close", args=[loot_group.pk]))
        self.post(reverse("loot_group_open", args=[loot_group.pk]))

        self.client.force_login(self.other_user)
        self.post(
            reverse("loot_share_join", args=[loot_group.pk]),
            {"character": self.other_char.pk},
        )
        self.assertEqual(
            list(
                loot_group.lootshare_set.values(
                    "character", "share_quantity", "flat_percent_cut"
                ).all()
            ),
            [
                {
                    "character": self.other_char.pk,
                    "share_quantity": 1,
                    "flat_percent_cut": 0,
                }
            ],
        )
