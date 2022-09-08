
def age_status(age_people):
  if 3 <= age_people < 7:
    print('Учиться в детском саду')
  elif 7 <= age_people <= 16:
    print('Учиться в школе')
  elif 17 <= age_people <= 23:
    print('Учится в универе')
  else:
    print('Работает')

age = int(input('Введите возраст'))
age_status(age)
