# coding:utf-8
#if文
x = 5
if(x > 0):
    print("+")
elif(x == 0):
    print("0")
    print("Zero")
else:
    print("-")

#for文 イテレーター
a = [1,2,3,4,5]
for i in a:
    print(i)
print("\n")

c = []
for i in range(1,100):
    if(i%3 != 0):
        continue
    if(i%5 != 0):
        continue
    print(i)

#While文
b = 123456789
i = 1
while(2**i < b):
    i+=1
print("\n")
print(i)
print("\n")


#演習1
d = [[1,5,3],[2,6,4]]
for i in d:
    print(max(i))
#演習2
for i in range(1,100):
    s = ""
    if(i%3 == 0):
        s += "Fizz"
    if(i%5 == 0):
        s += "Buzz"
    if (s != ""):
        print "%d %s" % (i,s)
