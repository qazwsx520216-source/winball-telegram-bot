from telegram.ext import Updater, CommandHandler
from datetime import datetime

TOKEN = "7231855121:AAHkk6EUC-F3ZThbaOkxt377wH0DPmqv54o"

def start(update, context):
    update.message.reply_text("👋 歡迎使用 Jiewei AI 體育預測機器人！\n輸入 /今天預測 查看今日 AI 推薦盤口")

def today_prediction(update, context):
    today = datetime.now().strftime("%Y-%m-%d")
    msg = f"📊 今日 AI 體育預測（{today})\n\n"

    games = [
        {
            "sport": "NBA",
            "teams": "湖人 vs 勇士",
            "time": "2025-07-19 08:30",
            "pick": "湖人 -4.5",
            "confidence": "76%"
        },
        {
            "sport": "MLB",
            "teams": "洋基 vs 紅襪",
            "time": "2025-07-19 07:10",
            "pick": "小分 8.5",
            "confidence": "81%"
        },
        {
            "sport": "英超",
            "teams": "利物浦 vs 曼城",
            "time": "2025-07-19 22:00",
            "pick": "大 2.5",
            "confidence": "79%"
        },
        {
            "sport": "NHL",
            "teams": "金騎士 vs 雪鳥",
            "time": "2025-07-19 10:15",
            "pick": "讓分 -1.5",
            "confidence": "74%"
        }
    ]

    for game in games:
        msg += f"🏟 {game['sport']}｜{game['teams']}\n"
        msg += f"🕒 開賽時間：{game['time']}\n"
        msg += f"推薦：{game['pick']}（信心：{game['confidence']}）\n\n"

    update.message.reply_text(msg.strip())

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("今天預測", today_prediction))
    updater.start_polling()
    print("🤖 Jiewei AI Bot 正在雲端運行中...")
    updater.idle()

if __name__ == "__main__":
    main()
