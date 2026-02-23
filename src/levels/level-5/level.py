from src.levels.levels import Level
from flask import request, redirect, make_response

level_password = "FLAG(RLSisIMPORTANT)"

users = [
    {
        "id": 22,
        "username": "Alice",
        "name": "Alice",
        "bio": "I'm Alice!, I love hiking and cooking.",
        "image": "https://i.pravatar.cc/150?img=1",
        "isAdmin": False,
    },
    {
        "id": 23,
        "username": "Bob",
        "name": "Bob",
        "bio": "Bob here, I'm a a baby",
        "image": "https://i.pravatar.cc/150?img=2",
        "isAdmin": False,
    },
    {
        "id": 24,
        "username": "Ariel",
        "name": "Ariel",
        "bio": "Hi, I'm the goat! I love bullying and coding.",
        "image": "/static/images/ariel.png",
        "isAdmin": False,
    },
    {
        "id": 25,
        "username": "Yogev",
        "name": "Yogev",
        "bio": "Hi, I'm Yogev! I love painting and vibe coding.",
        "image": "https://i.pravatar.cc/150?img=4",
        "isAdmin": True,
    }
]

def create_level(level: Level):
    bp = level.blueprint
    
    @bp.post('/submit_final')
    def submit_final_flag():
        submitted_flag = request.form.get("flag")
        if submitted_flag == "FLAG(YourNowAnAmatuerHacker)":
            response = make_response(redirect('/level-6/'))
            response.set_cookie("current_flag", "FLAG(YourNowAnAmatuerHacker)")
            return response
        else:
            return "Incorrect final flag!", 403
    
    @bp.get("/myinfo")
    def get_my_info():
        id = request.args.get("id")
        if id == "25":
            return "Hi Admin! Your ID is 25. Your secret flag is FLAG(YourNowAnAmatuerHacker)"
        elif id == "21":
            return "Hi User! Your ID is 21. You have no extra permissions"
        res = list(filter(lambda user: user["id"] == int(id), users))
        if res:
            return res[0]
        else:
            return "User not found", 404

    @bp.get("/users")
    def get_friends():
        id = request.args.get("id")
        return users
    
    return level