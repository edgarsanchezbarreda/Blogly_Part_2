"""Blogly application."""

from email.policy import default
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'helloworld123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

default_image_url = 'https://merriam-webster.com/assets/mw/images/article/art-wap-article-main/egg-3442-e1f6463624338504cd021bf23aef8441@1x.jpg'

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """This route displays the home page"""
    users = User.query.all()
    return render_template('user_list.html', users = users)


@app.route('/', methods=["POST"])
def add_user():
    """This route allows us to add a user to the database using the form"""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url'] or default_image_url

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect(f"/{new_user.id}")


@app.route('/<int:user_id>')
def user_details(user_id):
    """This route displays the user's details if clicked on the user home page"""
    user = User.query.get(user_id)
    posts = Post.query.filter(Post.user_id == User.id)
    return render_template('details.html', user = user, posts = posts)


@app.route('/<int:user_id>/edit')
def edit_user(user_id):
    """This route takes us to the edit page where we can edit the name and image of the selected user."""
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user= user)


@app.route('/<int:user_id>/edit', methods = ['POST'])
def save_edit_user(user_id):
    """This route allows us to save whatever changes were made in the edit page to our database, and returns us to the homepage"""
    user = User.query.get_or_404(user_id)
    
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url'] or default_image_url

    db.session.add(user)
    db.session.commit()

    return redirect('/')


@app.route('/<int:user_id>/delete', methods = ['POST'])
def delete_user(user_id):
    """This route allows us to delete a user completely from our database."""
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect('/')