from models import User, Post, db
from app import app

db.drop_all()
db.create_all()

Quentin = User(first_name= 'Quentin', last_name = 'Tarantino', image_url = 'https://www.indiewire.com/wp-content/uploads/2021/06/tarantino.png?resize=800,545')

Barack = User(first_name = 'Barack', last_name = 'Obama', image_url = 'https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTE4MDAzNDEwNzg5ODI4MTEw/barack-obama-12782369-1-402.jpg')

Rock = User(first_name = 'Dwayne', last_name = 'Johnson')

post_1 = Post(title = 'New movie!', content = 'I have a new movie coming, please be on the look out!', user_id = 1)

post_2 = Post(title = 'Hello everyone!', content = 'Hello everyone, I am new to this app please follow!', user_id = 2)

post_3 = Post(title = 'Any good restaurants?', content = 'I am new to this city does anyone know a good taco spot?', user_id = 3)

post_4 = Post(title = 'What a game!', content = 'Last nights basketball game was incredible, it came down to the wire!', user_id = 1)

post_5 = Post(title = 'Books to read.', content = 'I am looking for a good book to read, any suggestions?', user_id = 2)

post_6 = Post(title = 'New role!', content = 'I am filming ANOTHER movie with Kevin Hart!', user_id = 3)

db.session.add(Quentin)
db.session.add(Barack)
db.session.add(Rock)
db.session.add(post_1)
db.session.add(post_2)
db.session.add(post_3)
db.session.add(post_4)
db.session.add(post_5)
db.session.add(post_6)

db.session.commit()