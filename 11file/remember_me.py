import json
# 如果以前存储了用户名，就加载他
# 否则就提示用户输入用户名并存储他
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print(f"We will remember you,{username}!")
else:
    print(f"Welcome back,{username}!")

# 重构：代码能够正确运行，但能够做进一步的改进，将代码划分为一系列完成具体工作的函数，该过程称为重构
# 重构使得代码更加清洗，更加易于理解、更容易进行拓展
# 上述代码的重点是问候用户，可以将所有代码都放到一个函数中


def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What's your name?")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print(f"We will remember you,{username}!")
    else:
        print(f"Welcome back,{username}!")


greet_user()

# 重构greet_user()使其不执行这么多的任务


def get_stored_username():
    """如果存储了用户名，就获取他"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None  # 返回空，即为False
    else:
        return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print(f"Welcome back,{username}!")
    else:
        username = input("What's your name?")
        filename = 'username.json'
        with open(filename, 'w') as f_object:
            json.dump(username, f_object)
            print(f"We will remember you,{username}")


greet_user()
