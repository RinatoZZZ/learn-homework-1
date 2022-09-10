"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')




def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет пользователь!')



def talk_to_me(update, context):
    planets=['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    user_planet = update.message.text
    if user_planet in planets:
      planet = ephem.Sun('2022/10/09')
      constellation = ephem.constellation(planet)
      update.message.reply_text(constellation)
    elif user_planet in planets:
      planet = ephem.Moon('2022/10/09')
      constellation = ephem.constellation(planet)
      update.message.reply_text(constellation)
    elif user_planet in planets:
      planet = ephem.Mercury('2022/10/09')
      constellation = ephem.constellation(planet)
      update.message.reply_text(constellation)
    elif user_planet in planets:
      planet = ephem.Venus('2022/10/09')
      constellation = ephem.constellation(planet)
      update.message.reply_text(constellation)
    elif user_planet in planets:
      planet = ephem.Mars('2022/10/09')
      constellation = ephem.constellation(planet)
      update.message.reply_text(constellation)
    elif user_planet in planets:
      planet = ephem.Jupiter('2022/10/09')
      constellation = ephem.constellation(planet)
      update.message.reply_text(constellation)   
    elif user_planet in planets:
      planet = ephem.Uranus('2022/10/09')
      constellation = ephem.constellation(planet)
      update.message.reply_text(constellation)
    elif user_planet in planets:
      planet = ephem.Neptune('2022/10/09')
      constellation = ephem.constellation(planet)
      update.message.reply_text(constellation)
    elif user_planet in planets:
      planet = ephem.Pluto('2022/10/09')
      constellation = ephem.constellation(planet)
      update.message.reply_text(constellation)
    else:
      update.message.reply_text('Такой планеты в солнечной системы нет')



def main():
    mybot = Updater("5497179145:AAFq69pql94ISf02FOG3lRStZS1e4ffGIBA",  use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
