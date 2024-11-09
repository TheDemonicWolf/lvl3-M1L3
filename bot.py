from config import token

import telebot
import random

bot = telebot.TeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ну привет. Какова цель твоего визита?\
""")



#Хэндлер инфо
@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, """\
        Хочеь узнать обо мне? Ну слушай. Я Каратель, беспощадный и могущественный бот. Я храню в себе большое количество информации, и не каждому дано её знать.\
""")


#Хэндлер для новорегов
@bot.chat_join_request_handler()
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'У нас гости!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)



# Хэндлер, реагирующий на пинг
@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, """\
        Зачем я понадобился?\
""")


# Хэндлер для мудрых цитат
@bot.message_handler(commands=["quote"])
def quote(message):
    quotes = ['Сражение выигрывает тот, кто твёрдо решил выиграть',
              'Если ты однажды упал, это не означает, что ты никогда не поднимешься',
              'Если не можешь иметь то, что хочешь, научись хотеть то, что имеешь',
              'Не имей любви, которая походила бы на дружбу, имей дружбу, которая бы походила на любовь',
              'Самые нелепые поступки человек совершает всегда из благороднейших побуждений',
              'Когда слишком часто закрываешь глаза на поступки людей, они начинают делать то, что видно даже с закрытыми глазами',
              'Одну спичку дважды не зажжёшь',
              'Не важно, что человек может тебе дать, важно то, от чего он ради тебя отказывается',
              'Если вы стали для кого-то плохим, значит вы делали для него слишком много хорошего',
              'О нас думают плохо лишь те, кто хуже нас',
              'Только дурак никогда не меняет своего мнения',
              'Поток, заграждённый в стремлении своём, тем сильнее становится, чем твёрже находит противостояние',
              'Лучше иметь одну блестящую грань, чем быть всесторонне тусклым',
              'Самые важные вещи в мире были совершены людьми, которые прдолжали попытки, даже когда не оставалось никакой надежды',
              'Если вы хотите иметь успех, вы должны выглядеть так, как будто вы его имеете',
              'Ошибки - это знаки препинания жизни, без которых, как и в тексте, не будет смысла',
              'У всего есть своя красота, но не каждый может её увидеть']
    bot.reply_to(message, random.choice(quotes))



@bot.message_handler(commands=['ban', 'Бан'])
def ban_user(message):
    if message.reply_to_message: #проверка на то, что эта команда была вызвана в ответ на сообщение 
        chat_id = message.chat.id # сохранение id чата
         # сохранение id и статуса пользователя, отправившего сообщение
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
         # проверка пользователя
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
            bot.reply_to(message, f"@{message.reply_to_message.from_user.username}, тебя ждёт наказание... Божественная кара! Изгнание!")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")




bot.infinity_polling()
