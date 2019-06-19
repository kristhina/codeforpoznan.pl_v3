from marshmallow import Schema, fields, validate
from participant_serializer import participant_schema


class HacknightSchema(Schema):
    class Meta:
        fields = ('date', 'participants')

    date = fields.Str(required=True)
    participants = fields.List(fields.Nested(participant_schema))


hacknight_schema = HacknightSchema()
hacknights_schema = HacknightSchema(many=True)