import os
from flask import Flask, render_template, request, url_for, flash, redirect
from models import Post, db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect app and database
db.init_app(app)

# Initialize the database (Run this once)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # SQLAlchemy query to get all posts ordered by creation date
    # .desc() --> sort in descending order
    posts = Post.query.order_by(Post.created.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            # Create a new Post object and add it to the session
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    # Fetch the post or return a 404 error if it doesn't exist
    post = Post.query.get_or_404(id)
    
    db.session.delete(post)
    db.session.commit()
    
    flash(f'"{post.title}" was successfully deleted!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)