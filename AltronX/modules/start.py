from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, MK11, MK12, MK13, MK14, MK15, MK16, MK17, MK18, MK19, MK20, MK21, MK22, MK23, MK24, MK25, MK26, MK27, MK28, MK29, MK30, MK31, MK32, MK33, MK34, MK35, MK36, MK37, MK38, MK39, MK40, MK41, MK42, MK43, MK44, MK45, MK46, MK47, MK48, MK49, MK50 
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("☆ 𝐂ᴏᴍᴍᴀɴᴅs ☆", data="help_back")
        ],
        [
        Button.url("☆ 𝐂ʜᴀɴɴᴇʟ ☆", "https://t.me/ll_BAD_MUNDA_WORLD_ll"),
        Button.url("☆ 𝐒ᴜᴘᴘᴏʀᴛ", "https://t.me/ll_THE_BAD_BOT_ll")
        ],
        [
        Button.url("☆ 𝐁ᴀᴅ 𝐎ᴘ ☆", "https://t.me/II_BAD_MUNDA_II")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
@MK11.on(events.NewMessage(pattern="/start"))
@MK12.on(events.NewMessage(pattern="/start"))
@MK13.on(events.NewMessage(pattern="/start"))
@MK14.on(events.NewMessage(pattern="/start"))
@MK15.on(events.NewMessage(pattern="/start"))
@MK16.on(events.NewMessage(pattern="/start"))
@MK16.on(events.NewMessage(pattern="/start"))
@MK17.on(events.NewMessage(pattern="/start"))
@MK18.on(events.NewMessage(pattern="/start"))
@MK19.on(events.NewMessage(pattern="/start"))
@MK20.on(events.NewMessage(pattern="/start"))
@MK21.on(events.NewMessage(pattern="/start"))
@MK22.on(events.NewMessage(pattern="/start"))
@MK23.on(events.NewMessage(pattern="/start"))
@MK24.on(events.NewMessage(pattern="/start"))
@MK25.on(events.NewMessage(pattern="/start"))
@MK26.on(events.NewMessage(pattern="/start"))
@MK27.on(events.NewMessage(pattern="/start"))
@MK28.on(events.NewMessage(pattern="/start"))
@MK29.on(events.NewMessage(pattern="/start"))
@MK30.on(events.NewMessage(pattern="/start"))
@MK31.on(events.NewMessage(pattern="/start"))
@MK32.on(events.NewMessage(pattern="/start"))
@MK33.on(events.NewMessage(pattern="/start"))
@MK34.on(events.NewMessage(pattern="/start"))
@MK35.on(events.NewMessage(pattern="/start"))
@MK36.on(events.NewMessage(pattern="/start"))
@MK37.on(events.NewMessage(pattern="/start"))
@MK38.on(events.NewMessage(pattern="/start"))
@MK39.on(events.NewMessage(pattern="/start"))
@MK40.on(events.NewMessage(pattern="/start"))
@MK41.on(events.NewMessage(pattern="/start"))
@MK42.on(events.NewMessage(pattern="/start"))
@MK43.on(events.NewMessage(pattern="/start"))
@MK44.on(events.NewMessage(pattern="/start"))
@MK45.on(events.NewMessage(pattern="/start"))
@MK46.on(events.NewMessage(pattern="/start"))
@MK47.on(events.NewMessage(pattern="/start"))
@MK48.on(events.NewMessage(pattern="/start"))
@MK49.on(events.NewMessage(pattern="/start"))
@MK50.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝐇ᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝐈 𝐀𝐦 [{BotName}](tg://user?id={BotId})**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ 𝐃ᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ :~ [⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α_꯭آآ⎯꯭ ꯭̽🌸](https://t.me/II_BAD_MUNDA_II)**\n\n"
        TEXT += f"» ** 𝐋ᴇɢᴇɴᴅ sᴘᴀᴍ x ᴠᴇʀsɪᴏɴ :** `3.2`\n"
        TEXT += f"» **𝐓ᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph/file/911bc5ee7330f9dc72ee8.jpg",
                caption=TEXT, 
                buttons=PythonButton)

