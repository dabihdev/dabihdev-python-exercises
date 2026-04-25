from flask import Flask, render_template, request
from markupsafe import escape

# 1. initialize WSGI application
# WSGI application: https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface#:~:text=The%20Web%20Server%20Gateway%20Interface,in%20the%20Python%20programming%20language.
app = Flask(__name__)

# 2. map methods to routes (what should happen when a certain page is opened?)
@app.route('/')
def home():
    return "Hello! This is the home page."

@app.route('/about')
def about():
    return "<h1>About Us</h1><p>We are building things with Flask!</p>" # HTML

# 3. dynamic routes
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User name: {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

# 4. Use template pages
@app.route('/dashboard')
def dashboard():
    user_name = "Alex"
    hobby_list = ["Coding", "Hiking", "Reading"]
    # Meet our next actor: render_template
    return render_template('index.html', name=user_name, items=hobby_list)



# 5. handle requests (LOGIN form)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # The 'request' actor snoops on the incoming data
        username = request.form.get('username')
        return f"Logging in {username}..."
    
    # create the form in the page (input+button)
    return '''
        <form method="post">
            <input type="text" name="username">
            <input type="submit">
        </form>
    '''

# 6. run the back end app
if __name__=="__main__":
      app.run(debug=True)