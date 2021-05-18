from flask import Flask, render_template, redirect, url_for, request
from assetshandler import AssetFile, Assets
from assetsDB import posts_update
import os, sqlite3, yaml

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
stream = open("config.yaml", 'r')
config = yaml.load(stream, Loader=yaml.FullLoader)
conn = sqlite3.connect(config["init"]["DB"], check_same_thread=False)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        userEmail = request.form['userEmail']
        return userEmail
    return render_template("index.html",
                           Title="Home",
                           Header=config["author"]["name"],
                           Body=config["author"]["bio"],
                           Blog=url_for("blog"),
                           Resume=url_for("resume")
                           )


@app.route('/quote')
def quote():
    return "not yet"


@app.route('/blog')
def blog():
    asset = Assets()
    return render_template("blog.html",
                           Title="Blog",
                           Header="Blog",
                           Body="Landing Page for Blog Posts",
                           List=asset.posts_list
                           )


@app.route('/resume')
def resume():
    return render_template("resume.html",
                           Title="Blog",
                           Header="Blog",
                           Resume=os.getcwd().replace('\\', '/') + '/resume/' + "Cem_Sakarya_Resume.pdf"
                           )


@app.route('/blog/<blogpost>')
def posts(blogpost):
    asset = AssetFile(blogpost)
    posts_update(conn, blogpost)
    return render_template("blog-test.html",
                           Title=asset.title,
                           Header=asset.header,
                           Image1="/static/images/IMG_0299.jpg",
                           Image2="/static/images/IMG_0299@2x.jpg",
                           Body=asset.body
                           )


if __name__ == '__main__':
    app.run(debug=True)
