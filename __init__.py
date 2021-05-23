from flask import (Flask, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)
from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache
from peewee import *
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *
from assetshandler import AssetFile, Assets
from assetsDB import posts_update
import os, sqlite3, yaml



stream = open("config.yaml", 'r')
config = yaml.load(stream, Loader=yaml.FullLoader)


conn = sqlite3.connect(config["init"]["DB"], check_same_thread=False)

ADMIN_PASSWORD = 'secret'
app = Flask(__name__)
APP_DIR = os.path.dirname(os.path.realpath(__file__))
db = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
DEBUG = False
SECRET_KEY = 'shhh, secret!'  # Used by Flask to encrypt session cookie.
SITE_WIDTH = 800


app.config.from_object(__name__)



