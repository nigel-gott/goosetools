from rest_framework import serializers

from goosetools.industry.models import ShipOrder


class ShipOrderSerializer(serializers.ModelSerializer):
    recipient_character_name = serializers.CharField(
        source="recipient_character.ingame_name", read_only=True
    )
    assignee_name = serializers.CharField(
        source="assignee.discord_user.username", read_only=True
    )

    availible_transition_names = serializers.ReadOnlyField()

    class Meta:
        model = ShipOrder
        fields = [
            "id",
            "uid",
            "created_at",
            "ship",
            "quantity",
            "assignee",
            "recipient_character",
            "payment_method",
            "state",
            "notes",
            "recipient_character_name",
            "assignee_name",
            "availible_transition_names",
        ]