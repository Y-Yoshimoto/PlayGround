# coding:utf-8
adder = lambda x,y : x + y
print(adder(5,10))

num_list = range(10)

even_list = filter(lambda x:x%2 == 0, num_list)
print(even_list)

print(filter(lambda x:x%2 == 0, num_list))
print(map(lambda x:x*10, num_list))

list1 = [x*2 for x in range(10)]
print(list1)
list2 = [x*3 for x in range(10) if x%2 == 0]
print(list2)

#a = range(5)
a = [1,2,3,4,5]
print(a[1:])
