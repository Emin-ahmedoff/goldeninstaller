from telethon.tl.functions.channels import EditPhotoRequest, CreateChannelRequest
from .language import LANG, COUNTRY, LANGUAGE, TZ
from telethon import TelegramClient, functions
from telethon.sessions import StringSession
from rich.prompt import Prompt, Confirm
from asyncio import get_event_loop
from qalaktika_installer import *
from .astring import main
from time import time
from . import console
from git import Repo
import requests
import heroku3
import base64
import random
import os

LANG = LANG['MAIN']
Client = None

def connect (api):
    heroku_conn = heroku3.from_key(api)
    try:
        heroku_conn.apps()
    except:
        hata(LANG['INVALID_KEY'])
        exit(1)
    return heroku_conn

def createApp (connect):
    appname = "owenuserbot" + str(time() * 1000)[-4:].replace(".", "") + str(random.randint(0,500))
    try:
        connect.create_app(name=appname, stack_id_or_name='container', region_id_or_name="eu")
    except requests.exceptions.HTTPError:
        hata(LANG['MOST_APP'])
        exit(1)
    return appname

def hgit (connect, repo, appname):
    global api
    app = connect.apps()[appname]
    giturl = app.git_url.replace(
            "https://", "https://api:" + api + "@")

    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(giturl)
    else:
        remote = repo.create_remote("heroku", giturl)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as e:
        hata(LANG['ERROR'] + str(e))

    bilgi(LANG['POSTGRE'])
    app.install_addon(plan_id_or_name='062a1cc7-f79f-404c-9f91-135f70175577', config={})
    basarili(LANG['SUCCESS_POSTGRE'])
    return app

async def oturumacvebotlogolustur (stri, aid, ahash):
    try:
        Client = TelegramClient(StringSession(stri), aid, ahash)
        await Client.start()
        ms = await Client.send_message('me',LANG['QALAKTİKAUSERBOT'])
        KanalId = await Client(CreateChannelRequest(
            title='QalaktikaUserBot BotLog',
            about=LANG['AUTO_BOTLOG'],
            megagroup=True
        ))

        KanalId = KanalId.chats[0].id

        Photo = await Client.upload_file(file='owen.jpg')
        await Client(EditPhotoRequest(channel=KanalId, 
            photo=Photo))
        msg = await Client.send_message(KanalId, LANG['DONT_LEAVE'])
        await msg.pin()

        KanalId = str(KanalId)
        if "-100" in KanalId:
            return KanalId
        else:
            return "-100" + KanalId
    except:
        KanalId = 'err'
        return KanalId

if __name__ == "__main__":
    logo(LANGUAGE)
    loop = get_event_loop()
    api = soru(LANG['HEROKU_KEY'])
    bilgi(LANG['HEROKU_KEY_LOGIN'])
    heroku = connect(api)
    basarili(LANG['LOGGED'])

    # Telegram #
    onemli(LANG['GETTING_STRING_SESSION'])
    stri, aid, ahash = main()
    basarili(LANG['SUCCESS_STRING'])
    
    baslangic = time()


  
