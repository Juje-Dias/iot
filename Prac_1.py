import telepot
token = '997110905:AAGb_SJrXQFvN8lJ-3nn1KBJqPcxTPE6WI4'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == "text":
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

TelegramBot.message_loop(handle)



