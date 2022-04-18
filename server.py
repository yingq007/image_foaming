"""Server for images foaming."""

from flask import Flask
from model import connect_to_db
from flask import Flask, render_template, request, flash, session, redirect, jsonify
import crud
from jinja2 import StrictUndefined
app = Flask(__name__)


@app.route('/')
def homepage():
    """View homepage."""

    return render_template("homepage.html")

@app.route('/users')
def create_user():
    """View create account page"""

    return render_template("users.html") 


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.create_user(email, password)
    flash("Account created! Please log in.")
    return redirect("/")

@app.route('/login')
def login_user():
    """View create account page"""

    return render_template("login.html") 


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.email}!")

    return redirect("/")

@app.route('/images')
def view_all_images():
    """View all images."""

    images=crud.get_images()    
    return render_template("images.html", images=images)

@app.route('/images', methods=["POST"])
def add_an_image_to_foaming():
    """tag an image is foaming or not """

    image_id = request.form.get('image_id')
    url = request.form.get('url')
    lastModified= request.form.get('lastModified')
    result = request.form.get('result')
    image = crud.get_image_by_image_id(image_id)
    if (result == "foaming"):
        crud.create_foaming(image.image_id, session['user_id'],'True')
        flash(f" You've added to your foaming")
    elif (result == "not_foaming"):
        crud.create_foaming(image.image_id, session['user_id'],'False')
        flash(f" You've added to your non-foaming")
    return redirect("/images")



@app.route('/images_foaming')
def show_foaming_images():
    """show tagged image(foaming) in user's profile """
    
    user = crud.get_user_by_id(session['user_id'])
    res1={'foam':[]}
    for image in user.images:
        foaming_res={}
        if(image.foam=='True'):
            foaming_res['image_id']=image.image_id
            foaming_res['url']=image.url
            foaming_res['lastModified']=image.lastModified
            res1['foam'].append(foaming_res) 
    return jsonify(res1)

@app.route('/images_not_foaming')
def show_not_foaming_images():
    """show tagged image(non-foaming) in user's profile """
    
    user = crud.get_user_by_id(session['user_id'])
    res2={'not_foam':[]}
    for image in user.images:
        foaming_res={}
        if(image.foam=='False'):
            foaming_res['image_id']=image.image_id
            foaming_res['url']=image.url
            foaming_res['lastModified']=image.lastModified
            res2['not_foam'].append(foaming_res)
    return jsonify(res2)



@app.route('/user_profile')
def view_user_profile():
    """View create account page"""

    return render_template("user_profile.html") 

if __name__ == "__main__":
    connect_to_db(app)
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.jinja_env.undefined = StrictUndefined
    app.run(host="0.0.0.0", debug=True)