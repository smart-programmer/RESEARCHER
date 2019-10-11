from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, length, Email
from wtforms_components import SelectField
from flask_wtf.file import FileField, FileAllowed 
from wtforms.widgets import TextArea


options = [("للساعة", "للساعة"), ("لليوم", "يوميا"),("للاسبوع", "اسبوعيا"), ("للشهر", "للشهر")]




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


class UploadProduct(FlaskForm):
    image = FileField("ارفع صورة", validators=[FileAllowed(["jpg", "png", "GIF", "jpeg", "gif"]), DataRequired()])
    name = wtforms.StringField("اسم المنتج", validators=[
                                DataRequired(), length(min=3, max=255)])
    description = wtforms.StringField("وصف المنتج", validators=[
        DataRequired(), length(min=3, max=255)], widget=TextArea())
    price = wtforms.StringField("سعر المنتج")
    period = wtforms.SelectField("المدة", choices=options, validators=[DataRequired()])
    submit = wtforms.SubmitField("اعرض")


class UploadTestimonial(FlaskForm):
    name = wtforms.StringField(" اسم العميل ", validators=[
        DataRequired(), length(min=3, max=255)])
    work = wtforms.StringField("  طبيعة عمله ", validators=[
        DataRequired(), length(min=3, max=255)])
    description = wtforms.StringField("   ماقله العميل ", validators=[
        length(min=3, max=500)], widget=TextArea())

    submit = wtforms.SubmitField("أرفع")


class ReplyForm(FlaskForm):
    subject = wtforms.StringField("عنون الرسالة", validators=[
        length(max=255)])
    message = wtforms.TextAreaField("نص الرسالة ", validators=[
                                    DataRequired(), length(max=1000)])
    submit = wtforms.SubmitField("أرسل")


class UserForm(FlaskForm):
    full_name = wtforms.StringField("name", validators=[length(max=255), DataRequired()])
    password = wtforms.StringField("password", validators=[length(min=3)])
    submit = wtforms.SubmitField("سجل")




class SimpleForm(FlaskForm):
    button1 = wtforms.SubmitField("button1")
    button2 = wtforms.SubmitField("button2")