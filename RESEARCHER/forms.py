from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, length, Email
from wtforms_components import SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.widgets import TextArea

options = [("للساعة", "للساعة"), ("لليوم", "يوميا"),
           ("للاسبوع", "اسبوعيا"), ("للشهر", "للشهر")]
user_type_list = [("باحث", "باحث"), ("طالب", "طالب")]


class MessageForm(FlaskForm):
    full_name = wtforms.StringField(
        "الاسم ", validators=[length(min=3, max=255)])
    email = wtforms.StringField("البريد الإلكتروني", validators=[
                                Email(), DataRequired(), length(max=255)])
    subject = wtforms.StringField("عنوان الرسالة", validators=[
                                  length(min=3, max=255)])
    content = wtforms.TextAreaField("نص الرسالة ", validators=[
                                    DataRequired(), length(max=1000)])
    submit = wtforms.SubmitField("أرسل")


class LoginForm(FlaskForm):
    full_name = wtforms.StringField("اسم المستخدم")
    password = wtforms.StringField("الرقم السري")
    submit = wtforms.SubmitField("تسجيل الدخول")


class PostResearch(FlaskForm):
    name = wtforms.StringField("اسم البحث", validators=[
        DataRequired(), length(min=3, max=255)])
    description = wtforms.StringField("وصف البحث", validators=[
        DataRequired(), length(min=3, max=255)], widget=TextArea())
    submit = wtforms.SubmitField("اعرض")


class UserForm(FlaskForm):
    full_name = wtforms.StringField(
        "name", validators=[length(max=255), DataRequired()])
    password = wtforms.StringField("password", validators=[length(min=3)])
    submit = wtforms.SubmitField("سجل")
    user_type = wtforms.SelectField(
        "النوع", choices=user_type_list, validators=[DataRequired()])


class SimpleForm(FlaskForm):
    button1 = wtforms.SubmitField("button1")
    button2 = wtforms.SubmitField("button2")

