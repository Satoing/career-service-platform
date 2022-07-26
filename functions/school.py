from flask import Blueprint, render_template, request,redirect
from .config import *

school = Blueprint('school', __name__)


@school.route("/school")
def school_view():
    db = SQLManager()
    infos = db.get_list("select * from school")
    return render_template('school.html',infos=infos)