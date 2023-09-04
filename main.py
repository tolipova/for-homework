juft_sonlar=list(range(0,102,2))
print(juft_sonlar)

son=int(input("Xoxlagan sonni kiriting: "))
factorial=1
for i in range(1, son+1):
    factorial*=i
    print(f"{son}ning faktoriali {factorial}ga teng")


sonlar=list(range(100))
total=0
for num in sonlar:
    total+=num
    print("Ruyxatdagi sonlar yig'indisi: ",total)


number=list(range(101))
total=0
for son in number:
     total*=son
     print("Listdagi sonlar kupaytmasi:",total)

list=[1,2,3,4,5,6,7,8,9,10]
kv=[]
for c in list:
    kv.append(c**2)
    print("Sonlarning kvadrati:",kv)

for raqam in range(1,101):
    if raqam%3==0:
        print("3ga bulinadigan sonlar:",raqam)
    elif raqam%5==0:
        print("5ga bulinadigan sonlar:",raqam)
    else:
        print("Xatolik bor")       