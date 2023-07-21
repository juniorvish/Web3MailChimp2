```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class WalletAddressForm(FlaskForm):
    wallet_address = StringField('Wallet Address', validators=[DataRequired(), Length(min=42, max=42)])
    submit = SubmitField('Submit')

    def validate_wallet_address(self, wallet_address):
        if not wallet_address.data.startswith('0x'):
            raise ValidationError('Invalid wallet address. Must start with 0x.')
```