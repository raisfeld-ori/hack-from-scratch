from src.levels.levels import Level
from flask import request, redirect, make_response


level_password = "FLAG(YourNowAnAmatuerHacker)"

def create_level(level: Level):
    bp = level.blueprint
    
    @bp.post('/submit_final')
    def submit_final_flag():
        submitted_flag = request.form.get("flag")
        if submitted_flag == "FLAG(DontStealMySecret)":
            response = make_response(redirect('/level-6/'))
            response.set_cookie("current_flag", "FLAG(DontStealMySecret)")
            return response
        else:
            return "Incorrect final flag!", 403

    
    return level