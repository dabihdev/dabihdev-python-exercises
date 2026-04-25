from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__) # you're creating WSGI software!

# map routes to python methods
@app.route("/")
def index():
    return "Hello to Home!"

@app.route("/about")
def get_company_info():
    return "<h1>About</h1> <p>Company info</p>" # HTML code

@app.route("/contacts")
def show_contacts():
    return "Here my contacts"

# variables
@app.route("/user/<user_name>")
def get_user(user_name):
    return f"Username: {escape(user_name)}"

# templates
@app.route("/welcome")
def render_welcome_page():
    user = "Alex"
    items = ["reading", "writing", "trekking"]
    return render_template("index.html", name=user, items=items)

@app.route("/login", methods=["GET", "POST"])
def login():
     # special case
     if request.method == "POST":
         name = request.form.get("username")
         return f"Logging user {name}"
     # normal case ("GET")
     return '''
        <form method="post">
            <input type="text" name="username">
            <input type="submit">
        </form>
    '''

if __name__=="__main__":
    app.run(debug=True)