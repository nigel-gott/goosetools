from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from timezone_field import TimeZoneField
from dateutil.relativedelta import relativedelta


class GooseUser(AbstractUser):
    timezone = TimeZoneField(default='Europe/London')

    def discord_avatar_url(self):
        """
        :return: Returns the users discord avatar image link or false if they do not have one or an error occurs.
        """
        try:
            social_infos = SocialAccount.objects.filter(user=self)
            if len(social_infos) == 1:
                social_info = social_infos[0]
                avatar_hash = social_info.extra_data['avatar']
                discord_id = social_info.uid
                return f"https://cdn.discordapp.com/avatars/{discord_id}/{avatar_hash}.png"
        except Exception:
            pass
        return False


class Region(models.Model):
    name = models.TextField(primary_key=True)

    def __str__(self):
        return str(self.name)


class System(models.Model):
    name = models.TextField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Corp(models.Model):
    name = models.TextField(primary_key=True)

    def __str__(self):
        return str(self.name)


class Character(models.Model):
    discord_id = models.TextField()
    ingame_name = models.TextField()
    corp = models.ForeignKey(Corp, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.corp}] {self.ingame_name}"


class FleetType(models.Model):
    type = models.TextField()
    material_icon = models.TextField()
    material_colour = models.TextField()

    def __str__(self):
        return str(self.type)


def human_readable_relativedelta(delta):
    attrs = ['years', 'months', 'days', 'hours', 'minutes']
    return ', '.join(
        ['%d %s' % (getattr(delta, attr), attr if getattr(delta, attr) > 1 else attr[:-1]) for attr in attrs if
         getattr(delta, attr)])


class Fleet(models.Model):
    fc = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.TextField()
    fleet_type = models.ForeignKey(FleetType, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    expected_duration = models.TextField(blank=True, null=True)

    def human_readable_started(self):
        now = timezone.now()
        difference = self.start - now
        seconds = difference.total_seconds()
        pos_delta = relativedelta(seconds=abs(seconds))
        human_delta = human_readable_relativedelta(pos_delta)
        if abs(seconds) <= 60:
            return "Starts Now"
        elif seconds > 0:
            return f"Starts in {human_delta}"
        else:
            return f"Started {human_delta} ago"

    def human_readable_ended(self):
        now = timezone.now()
        if not self.end:
            return False
        difference = self.end - now
        seconds = difference.total_seconds()
        pos_delta = relativedelta(seconds=abs(seconds))
        human_delta = human_readable_relativedelta(pos_delta)
        if abs(seconds) <= 60:
            return "Ends Now"
        elif seconds <= 0:
            return f"Ended {human_delta} ago"
        else:
            return f"Ends in {human_delta}"

    def __str__(self):
        return str(self.name)


class FleetMember(models.Model):
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(blank=True, null=True)
    left_at = models.DateTimeField(blank=True, null=True)