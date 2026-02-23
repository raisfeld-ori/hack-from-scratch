from flask import Blueprint, make_response, redirect, render_template, request
from src.levels.levels import Level

main_blueprint = Blueprint("main", __name__)

levels: list[Level] = []
def set_levels(lvls: list[Level]):
    global levels
    levels = lvls


@main_blueprint.route("/")
def index():
    return render_template("index.html")

    
@main_blueprint.route("/info")
def info():
    return render_template("info.html")

@main_blueprint.route("/return_to_level", methods=["POST"])
def return_to_level():
    flag = request.form.get("flag")
    for level in levels:
        if level.match_password(flag):
            response = make_response(redirect(f"/level-{level._level_num}/"))
            response.set_cookie("current_flag", flag)
            return response
    return "Invalid flag!", 400