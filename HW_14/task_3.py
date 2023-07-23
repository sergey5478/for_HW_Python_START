import json

from task_1 import User
from task_2 import LevelException, AccessException


class Project:
    def __init__(self, users):
        self.users = users
        self.admin = None

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                users_dict = json.load(f)
        except Exception as e:
            print(f'При открытии файла {filename} возникла ошибка {e}. ')
        else:
            users = []
            for level, user in users_dict.items():
                for user_id, name in user.items():
                    users.append(User(user_id, name, level))
            return Project(users)

    def __str__(self):
        return str(self.users)

    # вход в систему
    def login(self, user_id, name):
        user_new = User(user_id, name)
        if user_new not in self.users:
            raise AccessException(user_id)
        for user in self.users:
            if user_new == user:
                self.admin = user

    def add_user(self, user_id, name, level):
        if int(self.admin.level) >= int(level):
            raise LevelException(level, name)
        self.users.append(User(user_id, name, level))


if __name__ == '__main__':
    filename = 'users.json'
    project = Project.load(filename)
    print(project)

    project.login('006', 'Люся')
    print(project.admin)

    project.add_user('010', 'Мустафа', 6)

    print(*project.users)
