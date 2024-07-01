from wtforms import Form, IntegerField, StringField
from wtforms.validators import DataRequired, Length

from app.libs.enums import ClientTypeEnums


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), Length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnums(value.data)
        except ValueError as e:
            raise e
        