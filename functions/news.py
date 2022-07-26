from flask import Blueprint

new_list = Blueprint('news', __name__)

@new_list.route("/news")
def news():
    return "这是新闻版块！"