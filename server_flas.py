from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recipe/')
def recipe():
    return render_template('recipe.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run()