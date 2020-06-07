import json
from pathlib import Path
#THIS IS TO CREATE A JSON FILE AND STORE
# movies = [
#     {"id":1,"titile":"onepiece","year": 1998 },
#     {"id":2,"titile":"blood_dimond","year": 2002 }
# ]
# data=json.dumps(movies)
# # print(data)
# Path("movies.json").write_text(data)


#TO READ FORM JSON FILE PROVIDED
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0]["titile"])  