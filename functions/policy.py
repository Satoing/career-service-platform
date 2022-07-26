from flask import Blueprint, render_template, request,redirect
from .config import *

policy = Blueprint('policy', __name__)


@policy.route("/school/policy")
def policy_view():
    db = SQLManager()
    news = db.get_list("select * from news")
    return render_template('policy.html',news=news)