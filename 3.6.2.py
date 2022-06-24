#Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
#Первое слово в тексте последнего файла: "We".

#Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

#Все файлы располагаются в каталоге по адресу:
#https://stepic.org/media/attachments/course67/3.6.3/

#Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests
import os

r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
s=r.text
while 'We' not in s:
    par=os.path.splitext(s)[0]
    r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + par + '.txt')
    s=r.text