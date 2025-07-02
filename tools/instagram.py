from instagrapi import Client
import os
from dotenv import load_dotenv

load_dotenv()
login = os.getenv("LOGININSTAGRAM")
senha = os.getenv("SENHAINSTAGRAM")

cl = Client()
cl.login(login, senha)

target_id = cl.user_id_from_username("sandeco")
posts = cl.user_medias(target_id, amount=10)
for media in posts:
    # download photos to the current folder
    print(media.caption_text)
    print(media.thumbnail_url)
