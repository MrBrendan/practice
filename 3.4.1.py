with open('c:/input/dataset_3363_2 .txt') as gg:
    j=[]#создаем список с учетом многозначности числа
    n=0#счетчик для j
    k=[]#создаем список конечный, без "" значений
    m=0#счетчик для k
    s=str()
    for line in gg:
        line=line.strip()
    for a in line:
        try:
            if 'A'<=a<='z':
                j+=line[n]
                n+=1
            else:
                try:
                    while '0'<=line[n]<='9':
                        s+=line[n]
                        n+=1
                    j+=[s]
                    s=str()
                except IndexError:
                    if n>len(j):
                        j+=[s]
                        s=str()
                    pass
        except IndexError:
            pass
    for i in j:
        if i!='':
            k.append(i)
    if 'A'<=j[-1]<='z':
        k.append('1')
with open ('c:/input/out.txt','w') as ouf:
    for i in k:
        if 'A'<=i<='z':
            ouf.write(str(i*int(k[m+1])))
            m+=1
        else:
            m+=1
            continue