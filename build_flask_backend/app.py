from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Our "Database" (a simple Python list for now)
tasks = ["Learn Flask", "Build a web app", "Take over the world"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the task from the form input
        new_task = request.form.get('task_content')
        if new_task:
            tasks.append(new_task)
        # Redirect back to the home page to see the updated list
        return redirect(url_for('index'))
    
    # Send the tasks list to the Jinja template
    return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)