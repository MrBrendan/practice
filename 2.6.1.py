#Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

#Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

#В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

#Вращение можно было завернуть в функцию (хочу оставить так, как свой первый код)
a=[]
w1=[]
w2=[]
# условие для end:
while ['end'] not in a:
    a.append(input().split())
if ['end'] in a:
    a.remove(['end'])
# узнаем размеры будущей матрицы:
x=int(len(a[0]))
ind=[]
for i in a:
    ind+=[a.index(i)]
y=int(len(ind))
# создаем матрицу подсчёта только по строкам )лево-право)
A=[]
for i in range(y):
    B=[]
    for j in range(x):
        B.append(a[i][j])
    for j in range(x):
        try:
            v=int(a[i][j+1])+int(a[i][j-1])
            w1.append(v)
        except IndexError:
            try:
                v=int(a[i][j+1])+int(a[i][x-1])
                w1.append(v)
            except IndexError:
                v=int(a[i][j-1])+int(a[i][0])
                w1.append(v)
    A.append(B)
# переворачиваем исходнкю матрицу (отображаем(
C=[]
for j in range(x):
    D=[]
    for i in range(y):
        D.append(a[i][j])
    C.append(D)
# создаем по перевернутой матрице подсчётную по строкам
E=[]
for j in range(y):
    F=[]
    for i in range(x):
        F.append(C[i][j])
    for i in range(x):
        try:
            v=int(C[i][j+1])+int(C[i][j-1])
            w2.append(v)
        except IndexError:
            try:
                v=int(C[i][j+1])+int(C[i][x-1])
                w2.append(v)
            except IndexError:
                v=int(C[i][j-1])+int(C[i][0])
                w2.append(v)
    E.append(F)
# складываем 2 матрицы подсчётов
wmara=list(map(lambda x,y: x+y,w1,w2))
# выводим результат
J=[]
for i in wmara:
    if len(J)!=x:
        J.append(i)
    else:
        print(*J)
        J=[i]
print(*J)