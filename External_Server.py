from flask import Flask, redirect, url_for, render_template, request, session, flash
import os
import requests

app = Flask(__name__)                                           # Create an instance of the Flask app

app.secret_key = 'testKeyDontWorryAboutIt'                      # Used to hash session data

if os.environ.get('PORT'):
    PORT = os.environ.get('PORT')
else:
    PORT = 5000

SERVER = os.environ.get('SERVER')
if SERVER is None:
    print('\nERROR: SERVER environment variable not found\n')
    exit()

print('\nPort: ', PORT)
print('Backend: ', SERVER, '\n')


# Home page
@app.route("/")                 # Slash means come here when the base domain is visited
def home():
    return render_template("index.html", isLoggedIn='user' in session)

@app.route("/user_page")
def user_page():
    return render_template("index.html", isLoggedIn='user' in session)

@app.route("/settings")
def settings():
    return render_template("index.html", isLoggedIn='user' in session)

@app.route("/email_portal")
def email_portal():
    return render_template("index.html", isLoggedIn='user' in session)

@app.route("/password_reset_portal")
def password_reset_portal():
    return render_template("index.html", isLoggedIn='user' in session)

@app.route("/logout")
def logout():
    user = session.pop('user', None)                    # Pop the user from session
    for key in list(session.keys()):                    # Clear the rest of the session (if anything)
        session.pop(key, None)
    flash(f'{user} has been logged out!')               # Flash message on next page that the user signed out
    return redirect(url_for("login"))

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":                                # If data submitted with post method
        username = request.form['Username']                     # Take the value from the form from the input named nm
        password_plain = request.form['Password']
        userData = [username, password_plain]                   # List of new user data to send to DB
        
        #isLoginSuccess = authenticate_user(userData, db_info)    # Pass in [username, password_entered] and db connection info
        response = requests.post(
            SERVER + '/login_internal',
            json={
                'username': username,
                'password_plain': password_plain
            },
        )
        print(response.get_json())
        if response.status_code == 200:
            session['user'] = username                          # Create a session
            flash(f'{userData[0]} logged in!')                  # Flash message on next page that the user signed in
            return redirect(url_for("user_page"))               # Redirect to the user page
        #elif isLoginSuccess is None:
        #    flash('Incorrect username')
        else:
            #flash('Incorrect password')
            flash('Login failed')

    elif request.method == 'GET' and 'user' in session:         # If a session exists
        return redirect(url_for("user_page"))                    # Redirect to user page
    
    # Only makes it here if
        # GET while not signed in (no session)
        # POST but login failed
    return render_template("login.html", isLoggedIn=False)
    
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['Username']                 # Take username from the form (input named Username)
        password_plain = request.form['Password']           # Take password from the form (input name Password)
        newUserData = [username, password_plain]            # List of new user data to send to DB

        # Frontend should validate username (and password) is not blank, but send back to sign in if not
        if username == '':
            flash('Blank username caught in backend, fix JS form validation')
            return render_template("signup.html", isLoggedIn=False)
        
        #isSignupSuccess = db_add_user(newUserData, db_info)                 # Try to add the new user to the DB
        response = requests.post(
            SERVER + '/signup_internal',
            json={
                'username': username,
                'password_plain': password_plain
            },
        )
        print(response.get_json())
        if response.status_code == 200:                                     # If successful
            session['user'] = username                                      # Create a session
            flash(f'Thanks for signing up '+ str(username) + '!')           # Flash success message on next page
            return redirect(url_for("user_page"))                           # Send to userPage
        else:
            flash(f' Username"' + str(username) + '" is already taken')     # Flash failure message on next page
            return redirect(url_for('signup'))

    return render_template("signup.html", isLoggedIn='user' in session)



if __name__ == "__main__":      # If we run this file directly
    app.run(debug=True, port=PORT)         # Start the app (debug mode means code updates here take effect on page reload)
