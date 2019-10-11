from flask import Flask, request, redirect, render_template, url_for, make_response
from RESEARCHER import app, db, bcrypt
from RESEARCHER.forms import LoginForm, PostResearch, UserForm, SimpleForm
# from RESEARCHER import errors
from RESEARCHER.models import Researche, User
from RESEARCHER.utils import save_image
from flask_login import current_user, login_user, login_required, logout_user


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/products/upload', methods=['GET', 'POST'])
@login_required
def upload():
    research_form = PostResearch()
    
    if research_form.validate_on_submit():
        research = Research()
        db.session.add(research)
        db.session.commit()

        return redirect(url_for('researchs'))
    return render_template('post_researche.html', form=research_form)


@app.route('/researchs', methods=['GET'])
@login_required
def products():

    products = Product.query.all()


    image_path = url_for("static", filename="posts/images")

    return render_template('products.html', image_path=image_path, products=products)


@app.route("/products/product/<id>", methods=["GET", "POST"])
@login_required
def product(id):
    product = Product.query.get(id)

    form = SimpleForm()

    if form.validate_on_submit():
        product.user_id = current_user.id
        db.session.commit()

    return render_template("product.html", product=product, form=form)



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

        return redirect(url_for("profile"))
    return render_template('register.html', form=user_form)  

@app.route('/packages', methods=['GET', 'POST'])
def packages():
    return render_template('packages.html')

@app.route("/profile", methods=["GET"])
@login_required
def profile():
    products = Product.query.filter_by(owner_id=current_user.id)
    return render_template("profile.html", user=current_user, products=products)



