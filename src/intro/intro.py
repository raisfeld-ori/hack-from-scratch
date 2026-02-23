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