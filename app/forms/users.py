from wtforms import Form, TextField, PasswordField, validators


class LoginForm(Form):
    email = TextField('Email', [validators.Required(), validators.Email()])
    password = PasswordField('Password', [validators.Required()])
