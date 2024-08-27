import telebot
from telebot import types

token = '7523792865:AAEiDOJHA3HeVvmo_zAj11jQ4RC9GENsols'

bot = telebot.TeleBot(token)

menu_items = {
    "Рафф Разный": {
        "ingredients": ["Эспрессо", "Взбитые сливки", "Сироп"],
        "size": {"STD": 200, "MDL": 260, "BIG": 280}
    },
    "Рафф Арахисовый": {
        "ingredients": ["Эспрессо", "Взбитые сливки", "Сироп", "Арахисовая паста"],
        "size": {"STD": 210, "MDL": 270, "BIG": 300}
    },
    "Моккачино": {
        "ingredients": ["Эспрессо", "Взбитое молоко", "Какао"],
        "size": {"MDL": 240, "BIG": 270}
    },
    "Горячий Шоколад": {
        "ingredients": ["Взбитое молоко", "Какао"],
        "size": {"MDL": 140, "BIG": 240}

    },
    "Какао": {
        "ingredients": ["Взбитое молоко", "Какао"],
        "size": {"STD": 170, "MDL": 200, "BIG": 250}
    },

    "Латте Матча": {
        "ingredients": ["молоко", "Матча", "Сироп"],
        "size": {"STD": 170, "MDL": 210, "BIG": 240}
    },
    "Чай Ягодный": {
        "ingredients": ["Мята", "Брусника", "Чёрный чай", ],
        "size": {"BIG": 220}
    },
    "Бэбичино": {
        "ingredients": ["Вспененое молоко", "Сироп"],
        "size": {"STD": 110, "MDL": 160, "BIG": 190}
    },
    "Чай Апельсиновый": {
        "ingredients": ["Апельсины + Лемон", "Чёрный чай", "Апельсиновый сок"],
        "size": {"BIG": 220}
    },
    "Чай Облепиховый": {
        "ingredients": ["Чёрный чай", "Облепиха", "Лемон"],
        "size": {"BIG": 220}
    },
    "Чайник": {
        "ingredients": ["Чай", "Вода"],
        "size": {"BIG": 130, "600 мл": 190}
    }

    # Add the rest of the menu items in a similar format
}

menu_items2 = {
    "Бамбл": {
        "ingredients": ["Эспрессо", "Сок", "Сироп"],
        "size": {"MDL": 240, "BIG": 290}
    },
    "Эспрессо-тоник/Кола": {
        "ingredients": ["Эспрессо", "Тоник/Кола"],
        "size": {"MDL": 230, "BIG": 260}
    },
    "Фраппучино": {
        "ingredients": ["Эспрессо", "Взбитые сливки", "Взбитые Молоко", "Сироп"],
        "size": {"MDL": 230, "BIG": 270}
    },
    "Ice Latte": {
        "ingredients": ["Эспрессо", "Молоко"],
        "size": {"STD": 150, "MDL": 190, "BIG": 230}
    },
    "Смузи мятно-банановый": {
        "ingredients": ["Сок", "Банан", "Сироп"],
        "size": {"BIG": 260}
    },
    "Смузи облеченковый": {
        "ingredients": ["Мороженое", "Облепиха", "Банан", "Сок"],
        "size": {"BIG": 260}
    },
    "Смузи смородиновый": {
        "ingredients": ["Мороженое", "Сок", "Банан", "Облепиха"],
        "size": {"BIG": 260}
    },
    "Пьяный Aнгел": {
        "ingredients": ["Мороженое", "Сироп", "Молоко", "Эспрессо"],
        "size": {"MDL": 250, "BIG": 310}
    },
    "Молочный коктейль классический": {
        "ingredients": ["ًШарик Мороженое", "Молоко"],
        "size": {"BIG": 260}
    },
    "Молочный коктейль Нэсквик": {
        "ingredients": ["Сливки", "Мороженое", "Какао", "Молоко"],
        "size": {"BIG": 260}
    },
    "Молочный коктейль Bubble Gum": {
        "ingredients": ["Сливки", "Мороженое", "Молоко", "Сироп"],
        "size": {"BIG": 260}
    },
    "Казанова": {
        "ingredients": ["Мороженое", "Банан", "Молоко", "Эспрессо", ],
        "size": {"BIG": 320}
    }  # ,
    # "Дополнительно": {
    #     "Любой напиток на растительном молоке": 60,
    #     "Молоко": 30,
    #     "Взбитые сливки": 40,
    #     "Сироп": 35,
    #     "Маршмеллоу": 30,
    #     "Мёд": 30
    # }
}

menu_items3 = {
    "Американо": {
        "ingredients": ["Вода", "Эспрессо"],
        "size": {"STD": 130, "MDL": 170, "BIG": 200}
    },
    "Япончик": {
        "ingredients": ["Вода", "Эспрессо"],
        "size": {"MDL": 140}
    },
    "Флэт Уайт": {
        "ingredients": ["Молочная пена", "Вспененое молоко", "Эспрессо"],
        "size": {"STD": 170, "MDL": 220, "BIG": 250}
    },
    "Латте": {
        "ingredients": ["Молочная пена", "Вспененое молоко", "Эспрессо"],
        "size": {"STD": 150, "MDL": 190, "BIG": 230}
    },
    "Капучино": {
        "ingredients": ["Молочная пена", "Вспененое молоко", "Эспрессо"],
        "size": {"STD": 150, "MDL": 190, "BIG": 230}
    },
    "Рад Каша": {
        "ingredients": ["Вспененое молоко", "Хлопья"],
        "size": {"STD": 120}
    },
    "Рад Каша, Ягодная": {
        "ingredients": ["Вспененое молоко", "Смородина/Брусника", "Хлопья"],
        "size": {"STD": 150}
    },
    "Гранола": {
        "ingredients": ["Молоко", "Орехи + Цукаты", "Мёд"],
        "size": {"MDL": 120}
    }
}


@bot.message_handler(commands=['start'])
def start_message(message):
    buttons = types.InlineKeyboardMarkup(row_width=1)

    button_hello = types.InlineKeyboardButton("Главное меню", callback_data="hello")
    # button_bye = types.InlineKeyboardButton("Меню напитков, еды, десертов", callback_data="bye")
    button_cat = types.InlineKeyboardButton("Оформление заказа", callback_data="cat")
    button_stats = types.InlineKeyboardButton("Статус заказа", callback_data="stats")
    button_stats2 = types.InlineKeyboardButton("Акции и предложения", callback_data="offers")
    button_stats3 = types.InlineKeyboardButton("Контакты и локация", callback_data="contacts")
    button_stats4 = types.InlineKeyboardButton("Обратная связь", callback_data="link")

    buttons.add(button_hello, button_cat, button_stats, button_stats2, button_stats3, button_stats4)

    bot.send_message(message.chat.id, "Привет ✌️ Выберите нужную команду:", reply_markup=buttons)


def display_payment_options(message, item_name):
    item = menu_items.get(item_name)
    if item:
        prices = item["size"]
        markup = types.InlineKeyboardMarkup()
        for size, price in prices.items():
            button_text = f"Pay {size} - {price}"      
            callback_data = f"pay_{item_name}_{size}"
            markup.add(types.InlineKeyboardButton(button_text, callback_data=callback_data))
        bot.send_message(message.chat.id, "Select a size to pay:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Item not found.")

    item2 = menu_items2.get(item_name)
    if item2:
        prices = item2["size"]
        markup = types.InlineKeyboardMarkup()
        for size, price in prices.items():
            button_text = f"Pay {size} - {price}"
            callback_data = f"pay_{item_name}_{size}"
            markup.add(types.InlineKeyboardButton(button_text, callback_data=callback_data))
        bot.send_message(message.chat.id, "Select a size to pay:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Item not found.")

    item = menu_items3.get(item_name)
    if item3:
        prices = item3["size"]
        markup = types.InlineKeyboardMarkup()
        for size, price in prices.items():
            button_text = f"Pay {size} - {price}"
            callback_data = f"pay_{item_name}_{size}"
            markup.add(types.InlineKeyboardButton(button_text, callback_data=callback_data))
        bot.send_message(message.chat.id, "Select a size to pay:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Item not found.")


@bot.callback_query_handler(func=lambda call: True)
def button_click(call):
    if call.data.startswith("pay_"):
        data_parts = call.data.split("_")
        item_name = data_parts[1]
        size = data_parts[2]
        amount = menu_items.get(item_name, {}).get("size", {}).get(size)

        # Implement payment logic here
        bot.reply_to(call.message, f"Payment processed for {item_name} - {size}. Amount: {amount}")
    else:
        display_payment_options(call.message, call.data)





@bot.callback_query_handler(func=lambda call: True)
def button_click(call):
    if call.data.startswith("pay_"):
        data_parts = call.data.split("_")
        item_name = data_parts[1]
        size = data_parts[2]
        amount = menu_items2.get(item_name, {}).get("size", {}).get(size)

        # Implement payment logic here
        bot.reply_to(call.message, f"Payment processed for {item_name} - {size}. Amount: {amount}")
    else:
        display_payment_options(call.message, call.data)






@bot.callback_query_handler(func=lambda call: True)
def button_click(call):
    if call.data.startswith("pay_"):
        data_parts = call.data.split("_")
        item_name = data_parts[1]
        size = data_parts[2]
        amount = menu_items3.get(item_name, {}).get("size", {}).get(size)

        # Implement payment logic here
        bot.reply_to(call.message, f"Payment processed for {item_name} - {size}. Amount: {amount}")
    else:
        display_payment_options(call.message, call.data)


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == "hello":
        bot.send_message(call.message.chat.id, "Вот наше меню 😋")
        bot.send_photo(call.message.chat.id, "https://freeimage.host/i/dV8A0Pt")
        bot.send_photo(call.message.chat.id, "https://freeimage.host/i/dVSJ8GV")
        bot.send_photo(call.message.chat.id, "https://freeimage.host/i/dVSJGG2")
        bot.send_photo(call.message.chat.id, "https://freeimage.host/i/dVSJNTb")


    elif call.data == "bye":
        bot.send_message(call.message.chat.id, "¡drinks minu!!!!!!!!!!!!")
    elif call.data == "cat":
        bot.send_message(call.message.chat.id, "Выберите тип заказа:")
        buttons = types.InlineKeyboardMarkup(row_width=1)

        button_cold = types.InlineKeyboardButton("Холодный", callback_data="cold")
        button_piece = types.InlineKeyboardButton("Штучный", callback_data="piece")
        button_sweet = types.InlineKeyboardButton("Сладкий", callback_data="sweet")
        buttons.add(button_cold, button_piece, button_sweet)

        bot.send_message(call.message.chat.id, "Что вы хотите заказать", reply_markup=buttons)
    elif call.data == "cold":
        bot.send_message(call.message.chat.id, "Вы выбрали Холодный напиток.")
        buttons = types.InlineKeyboardMarkup(row_width=1)

        for item_name in menu_items2:
            button = types.InlineKeyboardButton(item_name, callback_data=item_name)

            buttons.add(button)

        bot.send_message(call.message.chat.id, "Холодный напитки:", reply_markup=buttons)


    elif call.data == "sweet":
        bot.send_message(call.message.chat.id, "Выберите напиток:")
        buttons = types.InlineKeyboardMarkup(row_width=1)

        for item_name in menu_items:
            button = types.InlineKeyboardButton(item_name, callback_data=item_name)

            buttons.add(button)

        bot.send_message(call.message.chat.id, "Сладкие напитки:", reply_markup=buttons)

    elif call.data == "piece":
        bot.send_message(call.message.chat.id, "Вы выбрали Штучный напиток.")
        buttons = types.InlineKeyboardMarkup(row_width=1)

        for item_name in menu_items3:
            button = types.InlineKeyboardButton(item_name, callback_data=item_name)

            buttons.add(button)

        bot.send_message(call.message.chat.id, "Штучный напитки:", reply_markup=buttons)

    elif call.data in menu_items:
        item = menu_items[call.data]
        ingredients = "\n".join(item["ingredients"])
        prices = "  ".join([f"{size} - {price}" for size, price in item["size"].items()])
        message = f"{call.data}\nИнгредиенты:\n{ingredients}\nцена:\n{prices}"
        bot.send_message(call.message.chat.id, message)
    elif call.data in menu_items2:
        item = menu_items2[call.data]
        ingredients = "\n".join(item["ingredients"])
        prices = "  ".join([f"{size} - {price}" for size, price in item["size"].items()])
        message = f"{call.data}\nИнгредиенты:\n{ingredients}\nцена:\n{prices}"
        bot.send_message(call.message.chat.id, message)

    elif call.data in menu_items3:
        item = menu_items3[call.data]
        ingredients = "\n".join(item["ingredients"])
        prices = " , ".join([f"{size} - {price}" for size, price in item["size"].items()])
        message = f"{call.data}\nИнгредиенты:\n{ingredients}\nцена:\n{prices}"
        bot.send_message(call.message.chat.id, message)

    elif call.data == "stats":
        bot.send_message(call.message.chat.id, "Сейчас мы проверим статистику вашего заказа")

    elif call.data == "offers":
        bot.send_message(call.message.chat.id, "сегодня у нас скидка 20% 🤑")
    elif call.data == "contacts":
        bot.send_message(call.message.chat.id,
                         "Вот наш номер: +7 (904) 054-37-57,\n our vk:https://vk.com/coffeestar_gagarin \n our insta: ")
    elif call.data == "link":
        bot.send_message(call.message.chat.id, "comments")



@bot.message_handler(commands=['menu'])
def start_message(message):
    # List of image URLs
    image_urls = [
        "https://freeimage.host/i/dV8A0Pt",
        "https://freeimage.host/i/dVSJ8GV",
        "https://freeimage.host/i/dVSJGG2",
        "https://freeimage.host/i/dVSJNTb"
    ]

    # Iterate through the list of image URLs and send them one by one
    for url in image_urls:
        bot.send_photo(message.chat.id, url)


# bot.send_photo(message.chat.id,"https://freeimage.host/i/dV8A0Pt" + "https://freeimage.host/i/dVSJ8GV" +"https://freeimage.host/i/dVSJGG2" +"https://freeimage.host/i/dVSJNTb")
# bot.send_photo(message.chat.id,"https://freeimage.host/i/dVSJ8GV")
# bot.send_photo(message.chat.id,"https://freeimage.host/i/dVSJGG2" )
# bot.send_photo(message.chat.id, "https://freeimage.host/i/dVSJNTb")


# @bot.message_handler(commands=['start'])
# def start_message(message):
#  buttons = types.InlineKeyboardMarkup(row_width=7)

# task1 = types.InlineKeyboardButton("first button", callback_data="button1")
# task2 = types.InlineKeyboardButton("2nd button", callback_data="button2")
# task3 = types.InlineKeyboardButton("3rd button", callback_data="button3")
# task4 = types.InlineKeyboardButton("4th button", callback_data="button4")
# markup.add(task1, task2, task3, task4)
# bot.send_message(message.chat.id, "Привет ✌️ выберите нужную команду", reply_markup=buttons)


# @bot.callback_query_handler(func=lambda call:True)
# if answear(callback):
#  pass
#
# @bot.message_handler(content_types=['text'])
# def new_message(message):
#     if message.text in ("hello", "Hi", "Hello"):
#         bot.send_message(message.chat.id, "Hi ✌️ ")
#     elif message.text in ("bye", "Bye"):
#         bot.send_message(message.chat.id, "bye ✌️ ")
#     elif message.text == "cat":
#         bot.send_message(message.chat.id,
#                          "https://th-thumbnailer.cdn-si-edu.com/ii_ZQzqzZgBKT6z9DVNhfPhZe5g=/fit-in/1600x0/filters:focal(1061x707:1062x708)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer_public/55/95/55958815-3a8a-4032-ac7a-ff8c8ec8898a/gettyimages-1067956982.jpg ")
#     else:
#         bot.send_message(message.chat.id, "I don't understand ✌️ ")
bot.polling()