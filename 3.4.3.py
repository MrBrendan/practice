with open('c:/input/dataset_3363_4 (4).txt') as gg:
    lines = gg.readlines()
    line1=[]
    line2=[]
    for line in lines:
        line1+=line.split()
    for line in line1:
        line2+=line.split(';')
with open ('c:/input/out.txt','w') as ouf:
    n=0
    for line in line2.copy():
        try:
            name=line2[n]
            math=int(line2[n+1])
            fiz=int(line2[n+2])
            rus=int(line2[n+3])
            n+=4
            line=((math+fiz+rus)/3)
            ouf.write(f"{line}\n")
        except IndexError:
            pass
    n,math1,fiz1,rus1=0,0,0,0
    for i in range(1,len(line2)+1):
        try:
            while n<=len(line2):
                math1+=int(line2[n+1])
                fiz1+=int(line2[n+2])
                rus1+=int(line2[n+3])
                n+=4
        except IndexError:
            pass
    ouf.write(f"{(math1*4/len(line2))} {(fiz1*4/len(line2))} {(rus1*4/len(line2))}")