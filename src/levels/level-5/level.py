from src.levels.levels import Level
from flask import request, redirect, make_response
from random import randint

level_password = None

users = [
    {
        "id": 22,
        "username": "Alice",
        "name": "Alice",
        "bio": "I'm Alice!, I love hiking and cooking.",
        "image": f"https://picsum.photos/id/{randint(1, 800)}/200/300",
        "isAdmin": False,
    },
    {
        "id": 23,
        "username": "Bob",
        "name": "Bob",
        "bio": "Bob here, I'm a Nerd",
        "image": f"https://picsum.photos/id/{randint(1, 800)}/200/300",
        "isAdmin": False,
    },
    {
        "id": 24,
        "username": "Charlie",
        "name": "Charlie",
        "bio": "Charlie is my name, and I enjoy photography and traveling.",
        "image": f"https://picsum.photos/id/{randint(1, 800)}/200/300",
        "isAdmin": False,
    },
    {
        "id": 25,
        "username": "Dana",
        "name": "Dana",
        "bio": "Hi, I'm Dana! I love painting and music.",
        "image": f"https://picsum.photos/id/{randint(1, 800)}/200/300",
        "isAdmin": True,
    }
]

def create_level(level: Level):
    bp = level.blueprint
    
    @bp.post('/submit_final')
    def submit_final_flag():
        submitted_flag = request.form.get("flag")
        if submitted_flag == "CTF(YourNowAnAmatuerHacker)":
            response = make_response(redirect('/level-6/'))
            response.set_cookie("current_flag", "CTF(YourNowAnAmatuerHacker)")
            return response
        else:
            return "Incorrect final flag!", 403
    
    @bp.get("/myinfo")
    def get_my_info():
        id = request.args.get("id")
        if id == "25":
            return "Hi Admin! Your ID is 25. Your secret flag is CTF(YourNowAnAmatuerHacker)"
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