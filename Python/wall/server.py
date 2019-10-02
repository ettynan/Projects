from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

from flask_bcrypt import Bcrypt
import re #for regex

app = Flask(__name__)
mysql = MySQLConnector(app,'wall')
app.secret_key = 'jnsdflkas'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt=Bcrypt(app) 

name = re.compile(r'^[a-zA-Z]')

@app.route('/')
def index():
    if not 'user_id' in session:
        session['user_id'] = None
    return render_template('index.html')

# login and registration
@app.route('/register', methods = ['POST'])
def register():
    print 'b'
    #error checking
    error = 0
    #check first name length
    if len(request.form['first_name']) <2:
        error += 1
        flash("First name needs more characters")
    #check for numbers in the first name
    elif not name.match(request.form['first_name']):
        error += 1
        flash("no numbers allowed in the name")
    #check first name length
    if len(request.form['last_name']) <2:
        error += 1
        flash("Last name need more characters")
    #check for numbers in the last name
    elif not name.match(request.form['last_name']):
        error += 1
        flash("no numbers allowed in the name")
    #check email validity and field entry
    if not EMAIL_REGEX.match(request.form['email']):
        error += 1
        flash('email is not valid!')
    if len(request.form['password']) <9:
        error+= 1
        flash("password needs to be 9 characters!")
    #check passwords both match
    if request.form['password'] != request.form['confirm']:
        error+= 1
        flash("passwords do not match!")
        #If not errors then generate hash password and send info to database
    query = 'SELECT * FROM users WHERE email = :email'
    data = {'email': request.form['email']}
    user = mysql.query_db(query, data)

    if user:
        error += 1
        flash('Email already exists')
        return redirect('/')
    if error == 0:
        hashed = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :confirm, NOW(), NOW())"
        #get form data
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'confirm': hashed 
        }
        mysql.query_db(query, data)
        
        return redirect('/login')
    
    return redirect('/')


@app.route('/login', methods = ['POST'])
def login():
    print 'c'
    error = 0
    query = 'SELECT id, first_name, password FROM users WHERE email = "{}"'.format(request.form['email'])
    user = mysql.query_db(query)
    print user
    if len(user) < 1:
        flash("Email doesn't exist")
        error += 1
    elif not bcrypt.check_password_hash(user[0]['password'], request.form['password']):
        flash('Wrong password')
        error += 1
    elif error == 0:
        session['user_id'] = user[0]['id']
        session ['name'] = user[0]['first_name']
        return redirect('/login')

    return redirect('/')

@app.route('/login')
def login_info():
    print 'd'
    return render_template('success.html')

@app.route('/success')
def success():
    print 'e'
    query = "SELECT messages.id, messages.message, messages.created_at, users.first_name, users.last_name FROM messages JOIN users on users.id = messages.user_id"
    all_messages = mysql.query_db(query) #list of objects returned
    
    query = "SELECT comments.message_id, comments.comment, comments.created_at, users.first_name, users.last_name FROM comments JOIN users on users.id = comments.user_id"
    all_comments = mysql.query_db(query) #list of objects returned
    return render_template('success.html', messages = all_messages, comments = all_comments)

@app.route('/delete', methods = ['POST'])
def delete():
    print 'f'
    session.clear()
    return redirect('/')

#code for messages - the first function actually will be the wall with all the messages and comments, and then the posting of messages later
@app.route('/message', methods=['POST'])
def message():
    print 'g'
    print request.form
    print session
    query = "INSERT into messages (message, user_id, created_at, updated_at) VALUES (:content, :user_id, NOW(), NOW())"
    values = {
         "content": request.form["content"], 
         "user_id": session["user_id"]
    }
    print session['user_id']
    # #  ('/wall) return render_template("wall.html, first_name = fname[0]['first_name']")
    mysql.query_db(query, values)
    return redirect('/success')

@app.route('/comment/<message_id>', methods = ['POST'])
def comment(message_id):
    print 'h'
    query = "INSERT into comments (comment, user_id, message_id, created_at, updated_at) VALUES (:content, :user_id, :message_id, NOW(), NOW())"
    values = {
        "content": request.form["content"], 
        "user_id": session["user_id"],
        "message_id": message_id
    }
    mysql.query_db(query, values)
    return redirect('/success')

app.run(debug=True)
