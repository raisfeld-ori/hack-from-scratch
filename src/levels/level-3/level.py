from src.levels.levels import Level
from flask import request, redirect, make_response, render_template


level_password = "FLAG(ThefakeAdmin)"

def create_level(level: Level):
    bp = level.blueprint

    @bp.route('/admin', methods=['GET', 'POST'])
    def submit_secret_flag():
        role = request.args.get("role")
        if role == "admin":
            return "Hi admin! the flag is FLAG(ParameterTemperingIsCool)"
        else:
            return  "Error! Only admins can access this page!", 403
    
    @bp.post('/submit_final')
    def submit_final_flag():
        submitted_flag = request.form.get("flag")
        if submitted_flag == "FLAG(ParameterTemperingIsCool)":
            response = make_response(redirect('/level-4/'))
            response.set_cookie("current_flag", "FLAG(ParameterTemperingIsCool)")
            return response
        else:
            return render_template('levels/level-3.html', error=True), 403
    
    return level