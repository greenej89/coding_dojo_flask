from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User

# Root route redirects to page rendering a list of users
@app.route('/')
def index():
    return redirect('/users')

# Returns a page that renders a table containing the id, full name, email, creation time, and actions for all user objects in the users table of the database
@app.route('/users')
def get_all_users():
    users = User.get_all()
    return render_template('read(all).html', users = users)

# Returns a page that renders a form to input a new user
@app.route('/users/new')
def add_user():
    return render_template('create.html')

# Creates a data dictionary for a new user. Calls a User class method to save the data dictionary as a row in the users table.
# Returns a page containing information for the new user
@app.route('/users/create', methods=['POST'])
def create_user():
    data = { 
        'first_name': request.form['first_name'], 
        'last_name': request.form['last_name'],
        'email':  request.form['email']
    }
    user_id = User.save(data)
    return render_template('read(one).html', user=search_users_by_id( User.get_all() , user_id ))

# Takes a parameter for user_id.  
# Returns a page containing information for the given user_id and the respective User instance.
@app.route('/users/<int:user_id>')
def get_user_info(user_id):
    return render_template('read(one).html', user=search_users_by_id( User.get_all() , user_id ))

# Takes a parameter for user_id.  
# Returns a page containing a form to edit the information for the given user_id and the respective User instance.
@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    return render_template('edit.html', user=search_users_by_id( User.get_all() , user_id ))

# Takes a parameter for user_id.
# Creates a data dictionary for using form information submitted on edit page. 
# Calls User class method to update the columns for the given row in the database.
# Redirects user to users page.
@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    data = { 
        'id' : user_id,
        'first_name': request.form['first_name'], 
        'last_name': request.form['last_name'],
        'email':  request.form['email']
        }
    User.update(data)
    return redirect(f'/users/{user_id}')

# Takes a parameter for user_id.
# Calls User class method to delete the user row from the users table for the given user_id.
# Redirects to users page
@app.route('/users/<int:user_id>/destroy')
def delete_user(user_id):
    data = {'id' : user_id}
    User.delete_user(data)
    return redirect('/users')

#Helper function uses the user_id to find the correct user in a list of all users and return it to the template
def search_users_by_id(users, user_id):
    print("Search for user by id....")
    for each_user in users:
        if each_user.id == user_id:
            user = each_user
    return user
