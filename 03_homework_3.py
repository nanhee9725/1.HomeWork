from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target_music = db.music.find_one({'title': '안녕'})
print(target_music['artist'])