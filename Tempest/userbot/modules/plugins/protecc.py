""" This file is a part of @TempestSupports team """

import requests

from bs4 import BeautifulSoup
from pyrogram.types import Message

from Tempest import app, gen




app.CMD_HELP.update(
    {"protecc" : (
        "protecc",
        {
        "protecc [reply]" : "automatically protect waifus in your channels.",
        }
        )
    }
)




headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
}



@app.on_message(gen("pp", exclude =["sudo"]))
async def imagesauce_handler(_, m: Message):
    try:
        reply = m.reply_to_message
        if not reply:
            return await app.send_edit("Reply to some media.", text_type=["mono"], delme=4)

        if reply.photo:
            await app.send_edit("searching ...")
            savename = "photo_{}_{}.png".format(
                reply.photo.file_id, 
                reply.photo.date
                )
            await app.download_media(
                reply,
                file_name="./downloads/" + savename
                )
        elif reply.animation:
            await app.send_edit("⏳ • Hold on ...")
            savename = "giphy_{}-{}.gif".format(
                reply.animation.date,
                reply.animation.file_size
                )
            await app.download_media(
                reply,
                file_name="./downloads/" + savename
                )
        else:
            return await app.send_edit("Only photo & animation media's are supported.", text_type=["mono"], delme=4)

        # get url
        searchUrl = 'http://www.google.co.id/searchbyimage/upload'
        filePath = './downloads/{}'.format(savename)
        multiPart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
        response = requests.post(searchUrl, files=multiPart, headers=headers)
        getUrl = response.url

        # get results in text
        text = requests.get(getUrl, headers=headers).text
        soup = BeautifulSoup(text, "html.parser")
        try:
            find = soup.find_all("div", {"class":"r5a77d"})[0]
        except IndexError:
            return await app.send_edit("`No Results found !`", delme=3)
        textResults = find.text.split(":")[-1]

        await app.send_edit("/protecc {}".format(textResults), disable_web_page_preview = True)
    except Exception as e:
        await app.error(e)
