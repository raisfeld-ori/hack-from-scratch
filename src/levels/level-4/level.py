from src.levels.levels import Level
from flask import request, redirect, make_response, render_template


level_password = "CTF(ParameterTemperingIsCool)"

def create_level(level: Level):
    bp = level.blueprint
    users = [21, 5]
    admins = [1, 105]
    
    # In these routes I use force=True because I want the request to be as simple as possible
    # Even though this also means the mime type is different
    
    @bp.route('/admin', methods=['POST'])
    def submit_secret_flag():
        try:
            id = request.get_json(force=True).get("id")
            if id in admins:
                return "Hi admin! the flag is CTF(RLSisIMPORTANT)"
            else:
                return  "Error! Only admins can access this page!", 403
        except:
            return "Invalid request!", 400
    
    @bp.post('/users')
    def check_user():
        try:
            id = request.get_json(force=True).get("id")
            if id in admins:
                return "Hi admin!"
            else:
                return  "Hi user! Your ID is {}".format(id)
        except:
            return "Invalid request!", 400
    
    @bp.get('/users')
    def get_users():
        return "Users: {}".format(", ".join(map(str, users))) + " Admins: {}".format(", ".join(map(str, admins)))
    
    @bp.post('/submit_final')
    def submit_final_flag():
        submitted_flag = request.form.get("flag")
        if submitted_flag == "CTF(RLSisIMPORTANT)":
            response = make_response(redirect('/level-5/'))
            response.set_cookie("current_flag", "CTF(RLSisIMPORTANT)")
            return response
        else:
            return render_template('levels/level-4.html', error=True), 403
    
    return level