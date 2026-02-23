from flask import render_template, Blueprint, request, redirect, url_for, make_response
from pathlib import Path
import importlib.util
import sys


class Level(object):
    def __init__(self, level_num, password: str | None = None):
        self._level_num = level_num
        self._password = password
        self._blueprint = Blueprint(f"level-{level_num}", __name__, url_prefix=f"/level-{level_num}")
        self._blueprint.add_url_rule("/", view_func=self.get_default_page, endpoint="default")
        self._blueprint.add_url_rule("/level-lock", view_func=self.get_level_lock_page, endpoint="lock")
        self._blueprint.add_url_rule("/submit_flag", methods=["POST"], view_func=self.submit_flag, endpoint="submit")
    
    @property
    def blueprint(self):
        return self._blueprint

    def set_password(self, password: str):
        self._password = password
    
    def match_password(self, password: str) -> bool:
        return self._password == password
    
    def get_default_page(self):
        if self._password is not None:
            current_flag = request.cookies.get("current_flag")
            if current_flag != self._password:
                return redirect(url_for(f"level-{self._level_num}.lock"))
        return render_template(f"levels/level-{self._level_num}.html")
    
    def get_level_lock_page(self):
        return render_template("level-lock.html", level_num=self._level_num)
    
    def submit_flag(self):
        if self._password is None:
            return "No password for this level", 400
        
        submitted_flag = request.form.get("flag")
        if submitted_flag == self._password:
            response = make_response(redirect(url_for(f"level-{self._level_num}.default")))
            response.set_cookie("current_flag", self._password)
            return response
        else:
            return render_template("level-lock.html", level_num=self._level_num, error="Incorrect flag!")



def build_levels():
    levels = []
    levels_dir = Path(__file__).parent
    
    level_dirs = []
    for item in levels_dir.iterdir():
        if item.is_dir() and item.name.startswith('level-'):
            try:
                level_num = int(item.name.split('-')[1])
                level_dirs.append((level_num, item))
            except (IndexError, ValueError):
                continue
    
    level_dirs.sort(key=lambda x: x[0])
    
    for level_num, level_dir in level_dirs:
        level = Level(level_num)
        level_file = level_dir / 'level.py'
        if level_file.exists():
            spec = importlib.util.spec_from_file_location(f"level_{level_num}", level_file)
            module = importlib.util.module_from_spec(spec)
            sys.modules[f"level_{level_num}"] = module
            spec.loader.exec_module(module)
            if hasattr(module, 'level_password'):
                level.set_password(module.level_password)
            
            if hasattr(module, 'create_level'):
                level = module.create_level(level)
                levels.append(level)
    
    return levels