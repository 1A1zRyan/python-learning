import json

#如果存储过就加载，否则就输入并存储
def greet_user():
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except :
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
    else:
        print("Welcome back, " + username + "!")

greet_user()