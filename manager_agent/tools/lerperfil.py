from instagrapi import Client

cl = Client()
cl.login_by_sessionid("ASAMMRekqksxZyCTpgrs2Ma2Vsxx-IQ-uHTS1ZVwS9Hv5a9EEZ-nnw0DWDzrNjtwzWASOGbcxrLEO-NAVdRjzvfXZv9tyucfwtcF7rqoduxHhXKha7BVVxvk_Z7wTGfo1euXAjQ")

target_id = cl.user_id_from_username("sandeco")
posts = cl.user_medias(target_id, amount=3)
for media in posts:
    # download photos to the current folder
    cl.photo_download(media.pk)