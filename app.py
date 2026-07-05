# Import Flask and render_template (used to load HTML files from the 'templates' folder)
from flask import Flask, render_template

# Create the Flask application instance
app = Flask(__name__)

# Route for the Home page (when someone visits '/')
@app.route('/')
def home():
    return render_template('home.html')

# Route for the Projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Route for the Skills page
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Route for the Education page
@app.route('/education')
def education():
    return render_template('education.html')

# Route for the Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Only run the app if this file is executed directly (not imported)
if __name__ == '__main__':
    app.run(debug=True)  # debug=True auto-reloads on code changes and shows errors in browser