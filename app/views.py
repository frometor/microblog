from app import app
from flask import url_for, request, render_template


@app.route('/login_user', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return "Welcome back, %s" % request.form['username']
        else:
            error = 'Incorrect username and password'
    return render_template('login.html', error=error)


def valid_login(username, password):
    if username == password:
        return True
    else:
        return False

#@app.route('/hello')
#@app.route('/hello/<name>')
# def hello(name=None):
#    return render_template('hello.html',name=name)

#@app.route('/login', methods=['GET', 'POST'])
# def login():
#    if request.method== 'POST':
#        return 'username is '+str(request.values["username"])
#    else:
#        return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

#@app.route('/login', methods=['GET'])
# def login():
#    if request.values:
#        return 'username is '+str(request.values["username"])
#    else:
#        return '<form method="get" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

#@app.route('/')
# def index():
#   return url_for('show_user_profile', username='richard')

# @app.route('/username/<username>')
# def show_user_profile(username):
 #   #show username
 #   return "User %s " % username
