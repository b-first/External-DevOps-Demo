from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)                                           # Create an instance of the Flask app

app.secret_key = 'testKeyDontWorryAboutIt'                      # Used to hash session data

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
    return render_template("index.html", isLoggedIn='user' in session)

@app.route("/login")
def login():
    return render_template("index.html", isLoggedIn='user' in session)

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':

        # Create the user here
        
        return redirect(url_for('user_page'))

    return render_template("signup.html", isLoggedIn='user' in session)



if __name__ == "__main__":      # If we run this file directly
    app.run(debug=True)         # Start the app (debug mode means code updates here take effect on page reload)
