import os
import json
from random import choice, randint

import crud
import model
import server

os.system("dropdb foams")
os.system("createdb foams")

model.connect_to_db(server.app)
model.db.create_all()

with open("data/foam-seed.json") as f:
    image_data = json.loads(f.read())

images_in_db=[]
for image in image_data:
    url,lastModified=(
        image["url"],
        image["lastModified"]
    )
    db_image=crud.create_image(url,lastModified)
    images_in_db.append(db_image)
model.db.session.add_all(images_in_db)
model.db.session.commit()