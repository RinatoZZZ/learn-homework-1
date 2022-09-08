def ask_user(ask):
  while True:
    if ask == 'Хорошо':
      break
    else:
      ask = input('Как дела?')


user_answer = input('Как дела?')
ask_user(user_answer)

