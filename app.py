import functools
import urllib

from flask import (Flask, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)
from assetshandler import AssetFile, Assets
from assetsDB import posts_update
import os, sqlite3, yaml
from __init__ import conn, app, config


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        userEmail = request.form['userEmail']
        return userEmail
    return render_template("index-test.html",
                           Title="Home",
                           Header=config["author"]["name"],
                           LinkedIn=config["author"]["linkedin"],
                           github=config["author"]["github"],
                           Body=config["author"]["bio"],
                           Blog=url_for("blog"),

                           )


@app.route('/timeline')
def timeline():
    return render_template("timeline.html",
                            Image1 = "/static/images/IMG_0299.jpg",
                            Image2 = "/static/images/IMG_0299@2x.jpg",
                            cisa="/static/images/CISA.jpg",
                            cisa2="/static/images/CISA@2x.jpg",
                            cissp="/static/images/CISSP_-_Square.jpg",
                            cissp2="/static/images/CISSP_-_Square@2x.jpg"
                           )


@app.route('/blog')
def blog():
    asset = Assets()
    return render_template("blog.html",
                           Title="Blog",
                           Header="Blog",
                           Body="Landing Page for Blog Posts",
                           List=asset.posts_list
                           )


@app.route('/blog/<blogpost>')
def posts(blogpost):
    asset = AssetFile(blogpost)
    posts_update(conn, blogpost)
    return render_template("blogpost-test.html",
                           Title=asset.title,
                           Header=asset.header,
                           Image1="/static/images/IMG_0299.jpg",
                           Image2="/static/images/IMG_0299@2x.jpg",
                           Body=asset.body
                           )


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()

