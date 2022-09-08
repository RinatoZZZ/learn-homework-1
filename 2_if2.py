
def length_line(line1, line2):
  if not isinstance(line1, str) and isinstance(line2, str): #задать вопрос!
    return '0'
  elif len(line1) == len(line2):
    return '1'
  elif len(line1) > len(line2):
    return '2'
  elif len(line1) != len(line2) and 'learn' in line2:
    return '3'



print(length_line('asf', 'asf'))
print(length_line('asf', 'le'))
print(length_line('asf', 'learn'))
    
