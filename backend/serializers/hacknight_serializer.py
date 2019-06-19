from marshmallow import Schema, fields, validate


 class HacknightSchema(Schema):
    class Meta:
        fields = ('date',)

    date = fields.Str(required=True)


hacknight_schema = HacknightSchema()
hacknights_schema = HacknightSchema(many=True)