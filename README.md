# 🎁 Auto Gifts Buyer Bot

> ⚡ Powered by [Aayco](https://t.me/Aayco) — A smart Telegram bot for auto-buying Telegram star gifts 🎉

---

## 📌 Description

This bot automatically purchases Telegram **Star Gifts** based on customizable filters such as:

- ✅ Price range
- 🔒 Limited / upgradeable filters
- 🚫 Blacklist specific gift IDs
- 👻 Send gifts anonymously
- 🔁 Upgrade gifts if possible

Great for auto-collectors, gift senders, or bots that need to handle Telegram star-based purchases.

---

## 🧰 Features

| Feature                | Description                                                 |
|------------------------|-------------------------------------------------------------|
| 🎯 Targeting           | Send gifts to any user/channel (username or ID)             |
| 🛒 Auto-buy            | Purchases a number of gifts within a price range            |
| ⚙️ Configurable        | Edit all settings via a simple `config.json` file           |
| 🧩 Gift Filters        | Buy only `upgradeable`, `limited`, or `normal` gifts        |
| 👤 Anonymity           | Option to hide sender identity when sending gifts           |
| 🧱 Blacklist Support   | Skip specific gift IDs                                       |
| 🚨 Error Handling      | Graceful exits on low balance or permission issues          |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aayco/AutoGiftBuyer.git
cd AutoGiftBuyer

2. Install dependencies

pip install -r requirements.txt

> Requirements file should include:

telethon
rich



3. Configure the bot

The first run will auto-generate a config.json. Edit it with your details:

{
  "api_id": 123456,
  "api_hash": "api hash",
  "token": "bot token",
  "session": "string session",
  "reciver": "username_or_id",
  "upgradeable": false,
  "limited": false,
  "normal": false,
  "blacklist": [],
  "hide": false,
  "upgrade": false,
  "quantity": 5,
  "start": 100,
  "end": 500
}

> 🔐 You must provide either a token or session.




---

🚀 Run the Bot

python bot.py

You’ll see this banner on start:

͡(Auto Gifts Buyer)͡
“Powered by Aayco”

The bot will then attempt to buy gifts based on your config.


---

🛠 Example Use Cases

🛍 Buying specific limited edition gifts automatically

🎉 Sending anonymous gifts to a group or user

🧪 Running star-gift load tests

🤖 Integrating with other bots that automate Telegram features



---

🧑‍💻 Author

👨‍💻 Amiru Mohammed

💬 Telegram: @Aayco

🧠 Github: github.com/Aayco



---

📄 License

This project is open source under the MIT License.


---

> ✨ If you like this project, consider starring it and following the author!



---
