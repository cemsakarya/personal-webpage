from flask import render_template, redirect, url_for, request
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome!'


@app.route('/index')
def index():
    return render_template('/Templates/index.html', title='Welcome')


@app.route('/resume')
def resume():
    return render_template('resume.html', title='Resume')


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/email', methods=['POST', 'GET'])
def email():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))



@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


if __name__ == '__main__':
    app.run(debug=True)
