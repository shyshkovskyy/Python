
likelist1 = input('Введите список тех, кто поставил лайки: ')#Андрей Жанна Катя Макс
likelist2 = str(likelist1).split()


likelist0 = likelist2  #список имен, тех кто поставил лайки
if (("".join(likelist0)).isalpha()) == False:   #Проверяем, чтобы были только буквы. Если есть цифры или символы - выводим сообщение об ошибке.
  print('Во введенном имени есть число или символ. Исправьте.')
  exit()
else:
  for element in likelist0:
    if len(element) > 10:   #Проверяем, чтобы имя было не более 10 букв. Если больше 10 - выводим сообщение об ошибке.
      print('Есть имя с длиной более 10 букв. Уменьшите имя.')
      exit()
  likelist = likelist0      #Создаем копию списка.
  if len(likelist) == 0:    #Проверяем сколько человек поставили лайки. Выводим соответствующее сообщение.
         print('Это никому не нравится')
  elif len(likelist) == 1:
         print (likelist[0] + ' лайкнул это.')
  elif len(likelist) == 2:
         print (likelist[0] + ' и ' + likelist[1] + ' лайкнули это.')
  elif len(likelist) == 3:
         print (likelist[0] + ', ' + likelist[1] + ' и ' + likelist[2] +' лайкнули это.')
  else:
         print(likelist[0] + ', ' + likelist[1] + ' и ещё ' + str(len(likelist)-2) + ' человек(а) лайкнули это.')
exit()

