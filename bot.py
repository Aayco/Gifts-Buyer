""" Coder: Amiru Mohammed """
""" Telegram: t.me/Aayco """
""" Github: github.com/Aayco """
""" File: bot.py """
""" Date: 2025-07-02 20:08:12 """

# 🍭 Imports
from telethon import (
    TelegramClient,
    events,
    types,
    functions,
    sessions
)

from telethon.tl.types import (
    InputInvoiceStarGift
)
from json import (
    load,
    dump
)

from os import (
    path,
    system,
    listdir
)

from rich import (
    console,
    prompt,
    panel,
    align
)

from asyncio import (
    sleep,
    run
)

# 🎨 Setup Rich console and prompt
con = console.Console()
pr = prompt.Prompt()
pn = panel.Panel
al = align.Align

# 🍰 Variables
conf_file = 'config.json'

# 🎥 Banner
def banner():
    text = f"[cyan]͡(Auto Gifts Buyer)͡\n[yellow]“Powered by Aayco”"
    panel = pn(al.center(text, vertical="middle"), padding=(0, 1), border_style="bright_magenta")
    con.print(panel)
banner()

# ⚙️Config Setup
def config(conf_file):
    try:
        # If config file exists
        if path.exists(path=conf_file):
            # Open it
            with open(file=conf_file, mode='r', encoding='utf-8') as fp:
                # Load data inside
                return load(fp=fp)
        # If not found
        else:
            conf_data = {
                # Your account api id
                "api_id": 6,
                # Your account api hash
                "api_hash": "",
                # Your bot token (let it null or empty string to use string session)
                "token": "123456759:AAjehfdhhrhd",
                # Your account string session (let it null or empty string to use bot token)
                "session" : "",
                # The reciver username or id (user|channel)
                "reciver": "aayco",
                # Set to true if you only want upgradeable gifts
                "upgradeable": False,
                # Set to true if you only want limited gifts
                "limited": False,
                # Set to true if you only want normal gifts from stock (useless but why not)
                "normal": False,
                # Put id of gifts you need to skip
                "blacklist": [],
                # Set to true if you want gifts to be sending with hiding user
                "hide": False,
                # Set to true if you want client to update gift
                "upgrade": False,
                # Number of gifts you want to buy
                "quantity": 5,
                # Start price
                "start": 100,
                # End price
                "end": 500
            }
            # Open config file
            with open(file=conf_file, mode='w', encoding='utf-8') as fp:
                # Put data inside
                dump(obj=conf_data,fp=fp,indent=4)
                # Return the data
                return conf_data
    # If program couldn't write or open the file
    except PermissionError:
        exit("Couldn't open config file give code reading files permission or change config file to place to another one it can be read from")

# 🤖 Bot
setup = config(conf_file=conf_file)
api_id = setup["api_id"]
api_hash = setup["api_hash"]
bot_token = setup["token"]
session = setup["session"]
if bot_token:
    bot = TelegramClient(session="AutoBuyer", api_id=api_id, api_hash=api_hash)
elif session:
    bot = TelegramClient(session=sessions.StringSession(string=session), api_id=api_id, api_hash=api_hash)
else:
    con.print("[red]You should provide auth method")
    exit()

# 👑 Buyer class
class Buyer:
    # 🌟 Buying def
    @staticmethod
    async def buy():
        # ⚙️ Settings
        settings = config(conf_file=conf_file)
        reciver = await bot.get_input_entity(settings["reciver"])
        upgradeable = settings["upgradeable"]
        limited = settings["limited"]
        normal = settings["normal"]
        blacklist = settings["blacklist"]
        hide = settings["hide"]
        upgrade = settings["upgrade"]
        quantity = settings["quantity"]
        start = settings["start"]
        end = settings["end"]
        bought = 0
        # 🌀 Buying loop
        while bought < quantity:
            gifts = await bot(functions.payments.GetStarGiftsRequest(hash=0))
            for gift in gifts.gifts:
                if gift.id in blacklist:
                    continue
                if gift.sold_out:
                    continue
                if (gift.availability_remains is not None):
                    continue
                if upgradeable and not gift.can_upgrade:
                    continue
                if limited and not gift.limited:
                    continue
                if normal and gift.limited:
                    continue
                if not (start <= gift.stars <= end):
                    continue
                try:
                    invoice = InputInvoiceStarGift(
                        peer=reciver,
                        gift_id=gift.id,
                        include_upgrade=upgrade,
                        hide_name=hide
                    )
                    payment_form = await bot(functions.payments.GetPaymentFormRequest(invoice=invoice))
                    await bot(functions.payments.SendStarsFormRequest(form_id=payment_form.form_id, invoice=invoice))
                    bought += 1
                    con.print(f"[green]Bought {bought}/{quantity} gifts...")
                    await sleep(2)
                except Exception as e:
                    # If User don't have enough stars
                    if "RPCError 406: PRECHECKOUT_FAILED" in str(e) or "RPCError 400: BALANCE_TOO_LOW" in str(e):
                        con.print("[red]You don't have enough stars. Set a lower range or recharge.")
                        exit()
                    con.print(f"[red]Error: {str(e)}")

    # ▶️ Run the bott
    @staticmethod
    async def run():
        if setup["token"]:
            await bot.start(bot_token=bot_token)
        elif setup["session"]:
            await bot.start()
        else:
            con.print("[red]You should provide client")
            exit()
        await Buyer.buy()
        await bot.run_until_disconnected()

if __name__ == "__main__":
    try:
        run(main=Buyer.run())
    except KeyboardInterrupt:
        con.print("[red]Stopped by user")
    except Exception as e:
        con.print(f"[red]Error: {str(e)}")
