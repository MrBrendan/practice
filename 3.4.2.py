#Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

#Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

#В качестве ответа укажите вывод программы, а не саму программу.

#Слова, написанные в разных регистрах, считаются одинаковыми.

with open('c:/input/dataset_3363_3 (1).txt') as gg:
    lines = gg.readlines()
    line1=[]
    dc={}
    def up(dc, x, v=1):
        if x in dc:
            dc[x]+=1
        elif x not in dc:
            dc[x]=v
    for line in lines:
        line1+=line.lower().split()
    for i in line1:
        up(dc,i)
    max_val=max(dc.values())
    for key, value in dc.copy().items():
        if value<max_val:
            del dc[key]
        else:
            pass
    min_key=min(dc.keys())
    for key, value in dc.copy().items():
        if key>min_key:
            del dc[key]
        else:
            pass
with open ('c:/input/out.txt','w') as ouf:
    for key, value in dc.items():
        ouf.write("{0} {1}".format(key,value))