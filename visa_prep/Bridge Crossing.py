x,y,z=map(int,input().split())
if z>=y:
    mangoes=(z-y)//x
else:
    mangoes=0
print(mangoes)
