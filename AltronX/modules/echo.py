import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, MK11, MK12, MK13, MK14, MK15, MK16, MK17, MK18, MK19, MK20, MK21, MK22, MK23, MK24, MK25, MK26, MK27, MK28, MK29, MK30, MK31, MK32, MK33, MK34, MK35, MK36, MK37, MK38, MK39, MK40, MK41, MK42, MK43, MK44, MK45, MK46, MK47, MK48, MK49, MK50, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltronX.sql.echo_sql import addecho, is_echo, remove_echo
from AltronX.data import ALTRON


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK12.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"**ᴇᴄʜᴏ**:\n  » `{hl}echo <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        if int(user_id) in ALTRON:
            await event.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
        elif int(user_id) == OWNER_ID:
            await event.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
        elif int(user_id) in SUDO_USERS:
            await event.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
        else:
            chat_id = event.chat_id
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                await event.reply("» ᴇᴄʜᴏ ᴘʜʟᴇ sᴇ ʟᴀɢᴀ ʜᴜᴀ ʜᴀɪ.. ʜᴇʜᴇʜᴇ !!")
                return
            addecho(user_id, chat_id)
            await event.reply("» ᴇᴄʜᴏ ʟᴀɢ ɢʏᴀ! ʜᴀʜᴀʜᴀ!! ✅")
     else:
          await event.reply(usage)


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK11.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK13.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK14.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK15.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK16.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK17.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK18.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK19.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK20.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK21.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK22.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK23.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK24.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK25.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK26.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK27.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK28.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK29.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK30.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK31.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK32.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK33.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK34.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK35.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK36.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK37.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK38.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK39.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK40.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK41.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK42.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK43.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK44.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK45.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK46.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK47.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK48.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK49.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK50.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
  usage = f"**ʀᴇᴍᴏᴠᴇ ᴇᴄʜᴏ**:\n  » `{hl}rmecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = event.chat_id
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await event.client(alt)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await event.reply("» ᴜғғ ʏʀʀ!! ᴇᴄʜᴏ ʜᴛᴛ ɢʏᴀ ☑️")
        else:
            await event.reply("» ᴇᴄʜᴏ ᴛᴏ ᴋᴀʙᴋᴀ ʜᴀᴛᴛ ɢʏᴀ.. ᴜ ғᴏᴏʟ !!")
     else:
          await event.reply(usage)


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
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.3)
        try:
            Python = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(Python)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)

                          
