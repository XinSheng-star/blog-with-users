from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, URL, Email
from flask_ckeditor import CKEditorField
import email_validator



class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    name = StringField("Name", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Register")
##WTForm

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")

class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[InputRequired()])
    subtitle = StringField("Subtitle", validators=[InputRequired()])
    img_url = StringField("Blog Image URL", validators=[InputRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[InputRequired()])
    submit = SubmitField("Submit Post")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[InputRequired()])
    submit = SubmitField("Submit Comment")
