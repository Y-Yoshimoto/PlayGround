# coding:utf-8
import math

def my_abs(x):
    if (x < 0):
        x = x * -1
    return x

def my_fibo(n):
    var = [1,1,0]
    fibo = [0] #fibo.append([0]) #要素0をリストcに追加
    if(n < 0):
        return "Error(N<0)!"
    i = 1
    while(i <= n):
        fibo.append(var[0])
        #print(var[0])
        var[0] = var[1] + var[2]        #フィボナッチ数の計算
        var[1] = var[2];var[2] = var[0] #移動
        i+=1
    return fibo
#演習1　絶対値
#x = 8
#print(my_abs(x))
#演習2 フィボナッチ数
c = my_fibo(8)
for i in c:
    print(i)
