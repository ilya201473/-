import telebot
bot = telebot.TeleBot("6695991653:AAHmp1md7MOzEdwCBs01vz-0t_k4qOyJaYk")


@bot.message_handler(commands = ["casino"])
def test(m):
    bot.send_message(m.chat.id,"🎰")
bot.infinity_polling

()@bot.message_handler(coma)
def test(m):
    bot.send_message(m.chat.id,"Привет это военкомат")

bot.infinity_polling()
