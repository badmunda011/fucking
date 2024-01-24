import asyncio
import random
from telethon import events
from config import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, MK11, MK12, MK13, MK14, MK15, MK16, MK17, MK18, MK19, MK20, MK21, MK22, MK23, MK24, MK25, MK26, MK27, MK28, MK29, MK30, MK31, MK32, MK33, MK34, MK35, MK36, MK37, MK38, MK39, MK40, MK41, MK42, MK43, MK44, MK45, MK46, MK47, MK48, MK49, MK50, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltronX.data import RAID, REPLYRAID, ALTRON, MRAID, SRAID, CRAID, ALTRON, PBIRAID, PBISPAMRAID

que = {}
@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK12.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗥𝗮𝗶𝗱\n  » {hl}raid <count> <Username of User>\n  » {hl}raid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        mkraid = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(mkraid) == 2:
            message = str(mkraid[1])
            a = await e.client.get_entity(message)
            g = a.id
            if int(g) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(g) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(mkraid[0])
                for _ in range(counter):
                    reply = random.choice(PBISPAMRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(g) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                c = b.first_name
                counter = int(mkraid[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(PBISPAMRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK12.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗥𝗮𝗶𝗱\n  » {hl}raid <count> <Username of User>\n  » {hl}raid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        mkraid = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(mkraid) == 2:
            message = str(mkraid[1])
            a = await e.client.get_entity(message)
            g = a.id
            if int(g) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(g) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(mkraid[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(g) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                c = b.first_name
                counter = int(mkraid[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@MK1.on(events.NewMessage(incoming=True))
@MK2.on(events.NewMessage(incoming=True))
@MK3.on(events.NewMessage(incoming=True))
@MK4.on(events.NewMessage(incoming=True))
@MK5.on(events.NewMessage(incoming=True))
@MK6.on(events.NewMessage(incoming=True))
@MK7.on(events.NewMessage(incoming=True))
@MK8.on(events.NewMessage(incoming=True))
@MK9.on(events.NewMessage(incoming=True))
@MK10.on(events.NewMessage(incoming=True))
@MK11.on(events.NewMessage(incoming=True))
@MK12.on(events.NewMessage(incoming=True))
@MK13.on(events.NewMessage(incoming=True))
@MK14.on(events.NewMessage(incoming=True))
@MK15.on(events.NewMessage(incoming=True))
@MK16.on(events.NewMessage(incoming=True))
@MK17.on(events.NewMessage(incoming=True))
@MK18.on(events.NewMessage(incoming=True))
@MK19.on(events.NewMessage(incoming=True))
@MK20.on(events.NewMessage(incoming=True))
@MK20.on(events.NewMessage(incoming=True))
@MK21.on(events.NewMessage(incoming=True))
@MK22.on(events.NewMessage(incoming=True))
@MK23.on(events.NewMessage(incoming=True))
@MK24.on(events.NewMessage(incoming=True))
@MK25.on(events.NewMessage(incoming=True))
@MK26.on(events.NewMessage(incoming=True))
@MK27.on(events.NewMessage(incoming=True))
@MK28.on(events.NewMessage(incoming=True))
@MK29.on(events.NewMessage(incoming=True))
@MK30.on(events.NewMessage(incoming=True))
@MK32.on(events.NewMessage(incoming=True))
@MK33.on(events.NewMessage(incoming=True))
@MK34.on(events.NewMessage(incoming=True))
@MK35.on(events.NewMessage(incoming=True))
@MK36.on(events.NewMessage(incoming=True))
@MK37.on(events.NewMessage(incoming=True))
@MK38.on(events.NewMessage(incoming=True))
@MK39.on(events.NewMessage(incoming=True))
@MK40.on(events.NewMessage(incoming=True))
@MK41.on(events.NewMessage(incoming=True))
@MK42.on(events.NewMessage(incoming,=True))
@MK43.on(events.NewMessage(incoming=True))
@MK44.on(events.NewMessage(incoming=True))
@MK45.on(events.NewMessage(incoming=True))
@MK46.on(events.NewMessage(incoming=True))
@MK47.on(events.NewMessage(incoming=True))
@MK48.on(events.NewMessage(incoming=True))
@MK49.on(events.NewMessage(incoming=True))
@MK50.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    await asyncio.sleep(0.1)
    await event.client.send_message(
        entity=event.chat_id,
        message="""{}""".format(random.choice(PBIRAID)),
        reply_to=event.message.id,
    )


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK12.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))

async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐏𝐁𝐈𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}sraid <Username of User>\n  » {hl}sraid <reply to a User>"
    if e.sender_id in SUDO_USERS:
        mkrr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 11:
            message = str(mkrr[0])
            a = await e.client.get_entity(message)
            user_id = int(a.id)
            if int(user_id) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) == OWNER_ID:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                await e.reply("» ਹੁਣ ਇਸ ਦੀ ਭੈਣ ਦੀ ਲਨ ਦੇਣਾ ਬੈਡ ਨੇ😈", parse_mode=None, link_preview=None)

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            user_id = int(b.id)
            if int(user_id) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) == OWNER_ID:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                await e.reply("» ਹੁਣ ਇਸ ਦੀ ਭੈਣ ਦੀ ਲਨ ਦੇਣਾ ਬੈਡ ਨੇ😈", parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK12.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%sdsraid(?: |$)(.*)" % hl))
async def _(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐏𝐁𝐈𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}dsraid <Username of User>\n  » {hl}dsraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        AltX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(e.text) > 12:
            message = str(AltX[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            await e.reply("» ਮਾਰਲਈ ਇਸ ਦੀ ਭੈਣ ਦੀ ਸ਼ੋਲੀ ਬੈਡ ਨੇ!! 😂", parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            await e.reply("» ਮਾਰਲਈ ਇਸ ਦੀ ਭੈਣ ਦੀ ਸ਼ੋਲੀ ਬੈਡ ਨੇ!! 😂", parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@MK1.on(events.NewMessage(incoming=True))
@MK2.on(events.NewMessage(incoming=True))
@MK3.on(events.NewMessage(incoming=True))
@MK4.on(events.NewMessage(incoming=True))
@MK5.on(events.NewMessage(incoming=True))
@MK6.on(events.NewMessage(incoming=True))
@MK7.on(events.NewMessage(incoming=True))
@MK8.on(events.NewMessage(incoming=True))
@MK9.on(events.NewMessage(incoming=True))
@MK10.on(events.NewMessage(incoming=True))
@MK11.on(events.NewMessage(incoming=True))
@MK12.on(events.NewMessage(incoming=True))
@MK13.on(events.NewMessage(incoming=True))
@MK14.on(events.NewMessage(incoming=True))
@MK15.on(events.NewMessage(incoming=True))
@MK16.on(events.NewMessage(incoming=True))
@MK17.on(events.NewMessage(incoming=True))
@MK18.on(events.NewMessage(incoming=True))
@MK19.on(events.NewMessage(incoming=True))
@MK20.on(events.NewMessage(incoming=True))
@MK21.on(events.NewMessage(incoming=True))
@MK22.on(events.NewMessage(incoming=True))
@MK23.on(events.NewMessage(incoming=True))
@MK24.on(events.NewMessage(incoming=True))
@MK25.on(events.NewMessage(incoming=True))
@MK26.on(events.NewMessage(incoming=True))
@MK27.on(events.NewMessage(incoming=True))
@MK28.on(events.NewMessage(incoming=True))
@MK29.on(events.NewMessage(incoming=True))
@MK30.on(events.NewMessage(incoming=True))
@MK31.on(events.NewMessage(incoming=True))
@MK32.on(events.NewMessage(incoming=True))
@MK33.on(events.NewMessage(incoming=True))
@MK34.on(events.NewMessage(incoming=True))
@MK35.on(events.NewMessage(incoming=True))
@MK36.on(events.NewMessage(incoming=True))
@MK37.on(events.NewMessage(incoming=True))
@MK38.on(events.NewMessage(incoming=True))
@MK39.on(events.NewMessage(incoming=True))
@MK40.on(events.NewMessage(incoming=True))
@MK41.on(events.NewMessage(incoming=True))
@MK42.on(events.NewMessage(incoming=True))
@MK43.on(events.NewMessage(incoming=True))
@MK44.on(events.NewMessage(incoming=True))
@MK45.on(events.NewMessage(incoming=True))
@MK46.on(events.NewMessage(incoming=True))
@MK47.on(events.NewMessage(incoming=True))
@MK48.on(events.NewMessage(incoming=True))
@MK49.on(events.NewMessage(incoming=True))
@MK50.on(events.NewMessage(incoming=True))


async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    await asyncio.sleep(0.1)
    await event.client.send_message(
        entity=event.chat_id,
        message="""{}""".format(random.choice(REPLYRAID)),
        reply_to=event.message.id,
    )


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK12.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}rraid <Username of User>\n  » {hl}rraid <reply to a User>"
    if e.sender_id in SUDO_USERS:
        mkrr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 11:
            message = str(mkrr[0])
            a = await e.client.get_entity(message)
            user_id = int(a.id)
            if int(user_id) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) == OWNER_ID:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                await e.reply("» ਹੁਣ ਇਸ ਦੀ ਭੈਣ ਦੀ ਲਨ ਦੇਣਾ ਬੈਡ ਨੇ😈", parse_mode=None, link_preview=None)

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            user_id = int(b.id)
            if int(user_id) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) == OWNER_ID:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                await e.reply("» ਹੁਣ ਇਸ ਦੀ ਭੈਣ ਦੀ ਲਨ ਦੇਣਾ ਬੈਡ ਨੇ😈", parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK12.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def _(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}drraid <Username of User>\n  » {hl}drraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        AltX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(e.text) > 12:
            message = str(AltX[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            await e.reply("» ਮਾਰਲਈ ਇਸ ਦੀ ਭੈਣ ਦੀ ਸ਼ੋਲੀ ਬੈਡ ਨੇ!! 😂", parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            await e.reply("» ਮਾਰਲਈ ਇਸ ਦੀ ਭੈਣ ਦੀ ਸ਼ੋਲੀ ਬੈਡ ਨੇ!! 😂", parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK12.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗠𝗥𝗮𝗶𝗱\n  » {hl}mraid <count> <Username of User>\n  » {hl}mraid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        mkmr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(mkmr) == 2:
            message = str(mkmr[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(mkmr[0])
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(mkmr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK12.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗦𝗥𝗮𝗶𝗱\n  » {hl}sraid <count> <Username of User>\n  » {hl}sraid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        MKsr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(MKsr) == 2:
            message = str(MKsr[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(MKsr[0])
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(MKsr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK12.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: C𝗥𝗮𝗶𝗱\n  » {hl}craid <count> <Username of User>\n  » {hl}craid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        MKsr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(MKsr) == 2:
            message = str(MKsr[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(MKsr[0])
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(MKsr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

                           
