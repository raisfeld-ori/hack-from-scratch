from src.levels.levels import Level
from flask import request, redirect, make_response, render_template


level_password = None

def create_level(level: Level):
    bp = level.blueprint
    
    @bp.post('/submit_final')
    def submit_final_flag():
        submitted_flag = request.form.get("flag")
        if submitted_flag == "CTF(ilovehtml)":
            response = make_response(redirect('/level-1/'))
            response.set_cookie("current_flag", "CTF(ilovehtml)")
            return response
        else:
            return render_template("levels/level-0.html", error="Incorrect flag. Try again."), 403

    
    return level