import glob
from pathlib import Path
from utils import load_plugins
import logging
import asyncio
from config import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, MK11, MK12, MK13, MK14, MK15, MK16, MK17, MK18, MK19, MK20, MK21, MK22, MK23, MK24, MK25, MK26, MK27, MK28, MK29, MK30, MK31, MK32, MK33, MK34, MK35, MK36, MK37, MK38, MK39, MK40, MK41, MK42, MK43, MK44, MK45, MK46, MK47, MK48, MK49, MK50 

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "AltronX/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\𝗟𝗘𝗚𝗘𝗡𝗗 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧 𝗗𝗘𝗣𝗟𝗢𝗬𝗘𝗗  𝗦𝗨𝗖𝗖𝗘𝗦𝗙𝗨𝗟𝗟𝗬😎🤘🏻\n𝗠𝗬 𝗗𝗔𝗗 ---> @II_BAD_BBY_II")


async def main():
    await MK1.run_until_disconnected()
    await MK2.run_until_disconnected()
    await MK3.run_until_disconnected()
    await MK4.run_until_disconnected()
    await MK5.run_until_disconnected()
    await MK6.run_until_disconnected()
    await MK7.run_until_disconnected()
    await MK8.run_until_disconnected()
    await MK9.run_until_disconnected()
    await MK10.run_until_disconnected()
    await MK11.run_until_disconnected()
    await MK12.run_until_disconnected()
    await MK13.run_until_disconnected()
    await MK14.run_until_disconnected()
    await MK15.run_until_disconnected()
    await MK16.run_until_disconnected()
    await MK17.run_until_disconnected()
    await MK18.run_until_disconnected()
    await MK19.run_until_disconnected()
    await MK20.run_until_disconnected()
    await MK21.run_until_disconnected()
    await MK22.run_until_disconnected()
    await MK23.run_until_disconnected()
    await MK24.run_until_disconnected()
    await MK25.run_until_disconnected()
    await MK26.run_until_disconnected()
    await MK27.run_until_disconnected()
    await MK28.run_until_disconnected()
    await MK29.run_until_disconnected()
    await MK30.run_until_disconnected()
    await MK31.run_until_disconnected()
    await MK32.run_until_disconnected()
    await MK33.run_until_disconnected()
    await MK34.run_until_disconnected()
    await MK35.run_until_disconnected()
    await MK36.run_until_disconnected()
    await MK37.run_until_disconnected()
    await MK38.run_until_disconnected()
    await MK39.run_until_disconnected()
    await MK40.run_until_disconnected()
    await MK41.run_until_disconnected()
    await MK42.run_until_disconnected()
    await MK43.run_until_disconnected()
    await MK44.run_until_disconnected()
    await MK45.run_until_disconnected()
    await MK46.run_until_disconnected()
    await MK47.run_until_disconnected()
    await MK48.run_until_disconnected()
    await MK49.run_until_disconnected()
    await MK50.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
  
