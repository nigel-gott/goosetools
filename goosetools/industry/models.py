from django.conf import settings
from django.db import models
from django_fsm import FSMField, transition

from goosetools.users.models import Character


class Ship(models.Model):
    name = models.TextField(primary_key=True)
    tech_level = models.PositiveIntegerField()
    free = models.BooleanField(default=False)

    def __str__(self):
        if self.free:
            return f"{self.name} - FREE"
        else:
            return str(self.name)


class ShipOrder(models.Model):
    PAYMENT_METHODS = [("eggs", "eggs"), ("isk", "isk"), ("free", "free")]
    recipient_character = models.ForeignKey(Character, on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    contract_made = models.BooleanField(default=False)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    uid = models.TextField(unique=True)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    state = FSMField(default="not_started")
    notes = models.TextField(blank=True)
    payment_method = models.TextField(choices=PAYMENT_METHODS)

    def __str__(self):
        return f"ShipOrder({self.id}) - {self.ship}*{self.quantity}->{self.recipient_character}:{self.uid}"

    def availible_transitions(self):
        # pylint: disable=no-member
        return {t.name: t for t in self.get_available_state_transitions()}  # type: ignore

    def availible_transition_names(self):
        # pylint: disable=no-member
        return [t.name for t in self.get_available_state_transitions()]  # type: ignore

    @transition(field=state, source="not_started", target="inventing")
    def inventing(self):
        pass

    @transition(field=state, source="inventing", target="awaiting_production_slot")
    def awaiting_production_slot(self):
        pass

    @transition(
        field=state,
        source=["inventing", "awaiting_production_slot", "not_started"],
        target="building",
    )
    def building(self):
        pass

    @transition(field=state, source=["building", "not_started"], target="built")
    def built(self):
        pass

    @transition(field=state, source="built", target="audit")
    def audit(self):
        pass

    @transition(field=state, source=["audit", "missing_contract"], target="sent")
    def sent(self):
        pass

    @transition(field=state, source="audit", target="missing_contract")
    def missing_contract(self):
        pass

    @transition(field=state, source="*", target="not_started")
    def reset(self):
        pass
