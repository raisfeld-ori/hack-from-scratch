from src.levels.levels import Level
from flask import request, redirect, make_response


level_password = "CTF(ThefakeAdmin)"

def create_level(level: Level):
    bp = level.blueprint

    @bp.route('/admin', methods=['GET', 'POST'])
    def submit_secret_flag():
        role = request.args.get("role")
        if role == "admin":
            return "Hi admin! the flag is CTF(ParameterTemperingIsCool)"
        else:
            return  "Error! Only admins can access this page!", 403
    
    @bp.post('/submit_final')
    def submit_final_flag():
        submitted_flag = request.form.get("flag")
        if submitted_flag == "CTF(ParameterTemperingIsCool)":
            response = make_response(redirect('/level-4/'))
            response.set_cookie("current_flag", "CTF(ParameterTemperingIsCool)")
            return response
        else:
            return "Incorrect final flag!", 403
    
    return level