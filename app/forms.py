from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
# from wtforms import StringField


class UploadForm(FlaskForm):
    photo_test = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'Images Only!'])
    ])
