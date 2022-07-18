import time
import logging 
import platform

import pyrogram
from config import Config
from telegraph import Telegraph
from pyrogram import __version__ as pyrogram_version
from Tempest.core.database import Database
from Tempest.core.helpers import Helpers
from Tempest.core.newpyrogram import Methods






class ClassManager(Config, Helpers, Database, Methods):
    # versions /
    python_version = str(platform.python_version())
    pyrogram_version = str(pyrogram_version)

    # assistant /
    assistant_name = "Shion"
    assistant_version = "v.0.0.1"

    # userbot /
    userbot_name = "Tempest UB"
    userbot_version = "v.0.0.1"

    # containers /
    CMD_HELP = {}

    # owner details /
    owner_name = "Zephys"
    owner_id = 5231333039
    owner_username = "@X_Zephys"

    # other /
    message_ids = {}
    PIC = "https://telegra.ph/file/38eec8a079706b8c19eae.mp4"
    Repo = "https://github.com/TempestNetwork/TempestUB.git"
    StartTime = time.time()
    utube_object = object
    callback_user = None

    # debugging /
    
   
    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    logging.getLogger("pyrogram.session.session").setLevel(logging.WARNING) 
    logging.getLogger("pyrogram.session.internals.msg_id").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.dispatcher").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.connection.connection").setLevel(logging.WARNING)
    log = logging.getLogger()

    # telegraph /
    telegraph = Telegraph()
    telegraph.create_account(short_name=Config.TL_NAME if Config.TL_NAME else "Tempest Userbot")
