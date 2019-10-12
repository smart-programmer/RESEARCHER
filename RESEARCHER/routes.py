from flask import Flask, request, redirect, render_template, url_for, make_response
from RESEARCHER import app, db, bcrypt
from RESEARCHER.forms import LoginForm, PostResearch, UserForm, SimpleForm, SchoolLoginForm, schoolForm
# from RESEARCHER import errors
from RESEARCHER.models import Research, User, School
# from RESEARCHER.utils import save_image
from flask_login import current_user, login_user, login_required, logout_user

# done
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

# Working 
@app.route('/research/upload', methods=['GET', 'POST'])
@login_required
def upload():
    research_form = PostResearch()
    
    if research_form.validate_on_submit():
        name = research_form.name.data
        survey_link = research_form.survey_link.data
        research_subject = research_form.research_subject.data
        grade = research_form.grade.data
        province = research_form.province.data
        level = research_form.level.data

        school = School.query.all()
        if len(school) > 0:
            if not (research.province == "all"):
                school = School.query.filter_by(province=research.province).first()
        else:
            return redirect(url_for("home"))
        
        


        
        research = Research(owner=current_user.id, research_subject=research_subject, survey_link=survey_link,
        grade=grade, province=province, level=level, name=name, school=school.id)
        db.session.add(research)
        db.session.commit()


        


        return redirect(url_for('home'))
    return render_template('post_research.html', form=research_form)


# @app.route('/researchs', methods=['GET'])
# @login_required
# def products():

#     products = Product.query.all()


#     image_path = url_for("static", filename="posts/images")

#     return render_template('products.html', image_path=image_path, products=products)


# @app.route("/products/product/<id>", methods=["GET", "POST"])
# @login_required
# def product(id):
#     product = Product.query.get(id)

#     form = SimpleForm()

#     if form.validate_on_submit():
#         product.user_id = current_user.id
#         db.session.commit()

#     return render_template("product.html", product=product, form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = LoginForm()

    if form.validate_on_submit():
        full_name = form.full_name.data
        user = User.query.filter_by(full_name=full_name).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                next_page = request.args.get("next")
                return redirect(next_page) if next_page else redirect(url_for("profile"))
            else:
                return redirect(url_for("login"))
        else:
            return redirect(url_for("login"))
    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))



@app.route('/register', methods=["GET", "POST"])
def register():
    user_form = UserForm()

    if user_form.validate_on_submit():
        full_name = user_form.full_name.data
        password = bcrypt.generate_password_hash(user_form.password.data).decode("utf-8")
        
        user = User(full_name=full_name, password=password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template('register.html', form=user_form)  



@app.route("/profile", methods=["GET"])
@login_required
def profile():
    researches = Research.query.filter_by(owner=current_user.id)
    return render_template("profile.html", user=current_user, researches=researches)


@app.route("/school_register")
def school_register():
    school_form = schoolForm()
    if school_form.validate_on_submit():
        name = school_form.name.data
        password = school_form.password.data

        school = School(name=name, password=password)
        db.session.add(school)
        db.sessio.commit()
    return render_template("school_register.html", form=school_form)

@app.route("/school_login")
def school_login():
    school_login_form = SchoolLoginForm()
    if school_login_form.validate_on_submit():
        name = school_login_form.name.data
        password = school_login_form.password.data
        school = School.query.filter_by(name=name).first()

        if school:
            if school.password == password:
                return redirect(url_for("school_profile", name=name))
            else:
                return redirect(url_for("school_login"))
        else:
            return redirect(url_for("home"))
                
    return render_template("school_login.html", form=school_login_form)

@app.route("/school_profile/<name>")
def school_profile(name):
    # اعرض الابحاث الموجهة لهذي المدارس وحط زر قبول بحث وهمي واشياء اضافية زي رابط يودي لصفحة البحث ومعلوماته كلها
    school = School.query.filter_by(name=name).first()
    return render_template("school_profile.html", school=school)


@app.route("/research/<id>")
def research(id):
    # الصفحة اللي حتروه لها المدرية اذا ضغطت على رابط بحث
    research = Research.query.get(id)
    return render_template("research.html", research=research)
