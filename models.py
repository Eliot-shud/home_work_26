from marshmallow import Schema, ValidationError, fields, validates_schema

VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'limit', 'sort')


class RequestSchema(Schema):
    cmd_1 = fields.Str(required=True)
    value_1 = fields.Str(required=True)
    cmd_2 = fields.Str(required=True)
    value_2 = fields.Str(required=True)
    file_name = fields.Str(required=True)

    @validates_schema
    def check_all_cmd_valid(self, values: dict[str, str], *args, **kwargs):
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contains invalid value')


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)