# coding:utf-8
#タプル
a = ("taro", "1986", "Tokyo")
print(a)
print(type(a))
#辞書型
c = {"apple":"red", "lcemon":"yellow"}
print(c["apple"])

#クロージャー
def adder(x):
    def fun(y):
        return x + y
    return fun
adder5 = adder(5)
print(adder5(5))
print(adder5(12))

#演習１
def NoOverlap(vlist):
    var = set()
    for i in vlist:
        var.add(i)
    return list(var)

blist = [2,3,5,6,6,7,8,2,1,2]
print(NoOverlap(blist))

#演習２
