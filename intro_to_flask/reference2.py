from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Welcome back, Boss. You have full access.'

@app.route('/guest/<guest_name>')
def hello_guest(guest_name):
    return f'Hello {guest_name}, you are logged in as a Guest.'

@app.route('/user/<name>')
def user_logic(name):
    """
    This route acts as a traffic controller.
    It decides where to send the user based on their name.
    """
    if name.lower() == 'admin':
        # We use the function name 'hello_admin'
        return redirect(url_for('hello_admin'))
    else:
        # We pass the 'name' variable into 'hello_guest'
        return redirect(url_for('hello_guest', guest_name=name))

if __name__ == '__main__':
    app.run(debug=True)