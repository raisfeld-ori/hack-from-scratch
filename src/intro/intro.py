from flask import Blueprint, redirect, render_template, url_for, request
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