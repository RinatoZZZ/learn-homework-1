
sales_list = [ 
  {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
  {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
  {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

def sales_amount(phone_sold):
  sum_sold = 0
  for sold in phone_sold:
    sum_sold += sold
  return sum_sold


sum_all_phone = 0
numbers_of_models = 0

for name_phone in sales_list:
  all_sold = sales_amount(name_phone['items_sold'])
  avr_sold =(sales_amount(name_phone['items_sold'])) / len('items_sold')
  sum_all_phone += all_sold
  numbers_of_models += 1
  print(f'Суммарное количество продаж {name_phone["product"]} : {all_sold}')
  print(f'Cреднее количество продаж {name_phone["product"]} : {avr_sold}')
  print(f'Cуммарное количество продаж всех товаров: {sum_all_phone}')
  print(f'Cреднее количество продаж всех товаров: {sum_all_phone/numbers_of_models}')

 