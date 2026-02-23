from src.levels.levels import Level
from flask import request, redirect, make_response


level_password = "FLAG(IamAHacker)"

def create_level(level: Level):
    bp = level.blueprint

    @bp.post('/admin')
    def submit_secret_flag():
        return "The flag is for admins only! please go to /admin to get it"
    
    @bp.get('/admin')
    def get_admin_flag():
        return "Welcome, totally real admin that I totally trust. The flag is: FLAG(ThefakeAdmin)"
    
    @bp.post('/submit_final')
    def submit_final_flag():
        submitted_flag = request.form.get("flag")
        if submitted_flag == "FLAG(ThefakeAdmin)":
            response = make_response(redirect('/level-3/'))
            response.set_cookie("current_flag", "FLAG(ThefakeAdmin)")
            return response
        else:
            return "Incorrect final flag!", 403
    
    return level