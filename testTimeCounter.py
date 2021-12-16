import time

print("press any key to start")
x1 = input("")
t1 = time.time()
x1 = input("press any key to end")
t2 = time.time()

t3 = t2-t1
milisec = ((t3%1)*100)//1
sec = (t3%60)//1
mint = (t3//60)%60 
hour = (mint//60)

print("ur time is ==>",int(hour),"h:",int(mint),"m:",int(sec),"s:",int(milisec),"ms")





