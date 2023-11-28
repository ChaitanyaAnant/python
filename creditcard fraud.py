import datetime as dt
def separate(word1):
    s1=word1
    len1=len(s1)
    f1=open("city1.txt","a")
    f2=open("city2.txt","a")
    odd=""
    even=""
    for i in range(0,len1//2,1):
        odd=odd+s1[2*i]
    for i in range(0,len1//2,1):
        even=even+s1[1+2*i]
    f1.write(odd)
    f2.write(even)
    f1.close()
    f2.close()
    print(odd)
    print(even)
f3=open("in4.txt","r")
temp1=f3.readline()
print(temp1)
separate(temp1)

today = dt.datetime.now()
y1 = today.year
m1=today.month
d1=today.day
print(y1)
print(m1)
print(d1)


