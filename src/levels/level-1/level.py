from src.levels.levels import Level
from flask import make_response, request, redirect


level_password = "FLAG(ilovehtml)"

def create_level(level: Level):
    bp = level.blueprint
    
    @bp.post('/secret_flag')
    def submit_secret_flag():
        return "Shhh, don't tell anyone. The flag is FLAG(IamAHacker)"
    
    @bp.post('/submit_final')
    def submit_final_flag():
        submitted_flag = request.form.get("flag")
        if submitted_flag == "FLAG(IamAHacker)":
            response = make_response(redirect('/level-2/'))
            response.set_cookie("current_flag", "FLAG(IamAHacker)")
            return response
        else:
            return "Incorrect final flag!", 403
    
    return level