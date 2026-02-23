from flask import Flask
from src.levels.levels import build_levels
from src.intro.intro import main_blueprint
from src.ssh.ssh_server import start_ssh_server_background
from pathlib import Path


def build_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    levels = build_levels()
    for level in levels:
        app.register_blueprint(level.blueprint)
    
    #start_ssh_server_background('localhost', 2222, Path("./.ssh/keys") )
    return app