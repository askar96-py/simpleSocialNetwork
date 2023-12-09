import json

with open('app/data.json') as f:
    data = json.load(f)

class DataManager:

    def __init__(self, data) -> None:
        self._users = data['users']
        self._current_user = data['current_user']

    def check_user_data(self, username, password):
        for i in self._users:
            if i['username'] == username and i['password'] == password:
                self._current_user = i
                return True
        return False
    
    def delete_current_user(self):
        self._users.remove(self._current_user)

    def get_current_user(self):
        if self._current_user is None:
            return False
        return self._current_user

    def set_current_user(self, current_user):
        self._current_user = current_user

    def add_new_user(self, new_user):
        self._users.append(new_user)

    def get_user_list(self):
        return self._users
    

db = DataManager(data=data)

# def get_current_user():
#     print(data['current_user'])
#     return data['current_user']

# def get_user_list():
#     return data['users']

# def add_new_user(new_user):
#     data['users'].append(new_user)