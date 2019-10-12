from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, length, Email
from wtforms_components import SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.widgets import TextArea

grade_select = [("elementarySchool", "الابتدائية"), ("middleSchool", "المتوسطة"),
           ("highSchool", "الثانوية"), ("all","الكل")]
province_select = [("Makkah", "منطقة مكة المكرمة"), ("Riyadh", "منطقة الرياض"), ("all", "الكل")]
level_select =[("excellent", "ممتاز"), ("medium", "متوسط"), ("low", "منخفظ"), ("all", "الكل")]



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
    research_subject = wtforms.StringField("وصف البحث", validators=[
        DataRequired(), length(min=3, max=255)], widget=TextArea())
    survey_link = wtforms.StringField("رابط الاستبيان", validators=[DataRequired(), length(max=255)])
    grade = wtforms.SelectField(
        "السنة", choices=grade_select, validators=[DataRequired()])
    province = wtforms.SelectField(
        "منطقة البحث", choices=province_select, validators=[DataRequired()])
    level = wtforms.SelectField(
        "مستوى الطلاب", choices=level_select, validators=[DataRequired()])
    submit = wtforms.SubmitField("اعرض")


class UserForm(FlaskForm):
    full_name = wtforms.StringField(
        "name", validators=[length(max=255), DataRequired()])
    password = wtforms.StringField("password", validators=[length(min=3)])
    submit = wtforms.SubmitField("سجل")

class SchoolLoginForm(FlaskForm):
    name = wtforms.StringField("اسم المدرسة")
    password = wtforms.StringField("الرقم السري")

class schoolForm(FlaskForm):
    name = wtforms.StringField("اسم المدرسة")
    password = wtforms.StringField("الرقم السري")


class SimpleForm(FlaskForm):
    button1 = wtforms.SubmitField("button1")
    button2 = wtforms.SubmitField("button2")

