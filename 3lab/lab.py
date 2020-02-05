from datetime import datetime
import json
import vk
import vk_api

access_token = '374b7acf374b7acf374b7acfdb372677633374b374b7acf6ac4779e3fcf5cff972640c2'
api_v = 5.101


class Parse:
    def __init__(self, user_id, deep, root):
        self.user_id = user_id
        self.deep = deep
        self.root = root


class User:

    def __init__(self, user_id, age, countPhoto, countVideo, countNotes, countGroups, city):
        self.user_id = user_id
        self.age = age
        self.photo = countPhoto
        self.countVideo = countVideo
        self.countNotes = countNotes
        self.countGroups = countGroups
        self.city = city

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def userFriends(user_id, deep):
    if deep < max_deep:
        try:
            deep += 1
            friends = vk_api.friends.get(user_id=user_id, order='hints', v=api_v)
            items = map(lambda friend: Parse(friend, deep, user_id), friends['items'])
            parsing = list(items)
        except:
            return

        parsedUsers.extend(parsing)
        for item in parsing:
            userFriends(item.user_id, item.deep)
    else:
        return


def getinfo(user_id):
    try:
        user_info = vk_api.users.get(user_id=user_id, fields='bdate, counters, city', v=api_v)

        try:
            birtdate = user_info[0]['bdate']
            now = datetime.now()
            birthday = datetime.strptime(birtdate, '%d.%m.%Y')
            age = now.year - birthday.year
        except:
            age = 0

        try:
            photos = user_info[0]['counters']['photos']
        except:
            photos = 0

        try:
            videos = user_info[0]['counters']['videos']
        except:
            videos = 0

        try:
            notes = user_info[0]['counters']['notes']
        except:
            notes = 0
        try:
            groups = user_info[0]['counters']['groups']
        except:
            groups = 0
        try:
            city = user_info[0]['city']
        except:
            city = 0

        return User(user_id, age, photos, videos, notes, groups, city)

    except Exception as er:
        print(er)
        return


if __name__ == '__main__':

    session = vk.Session(access_token=access_token)
    vk_api = vk.API(session)
    max_deep = 2
    root_id = 291484564

    parsedUsers = []
    usersInfo = []

    userFriends(root_id, 0)

    for user in parsedUsers:
        us = getinfo(user.user_id)
        if us is not None:
            usersInfo.append(us)

    with open('data.json', 'w') as outfile:
        json.dump(usersInfo, outfile, default=lambda x: x.__dict__)
