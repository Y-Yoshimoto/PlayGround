# coding:utf-8
class Score:
    def __init__(self, name, math, english,japanese):
        self.name = name
        self.math = math
        self.english = english
        self.japanese = japanese
        self.average = (self.math+self.english+self.japanese)/3.0

    def scorePrint(self):
        print "{0}の成績は M={1},E={2},J={3}".format(self.name,self.math,self.english,self.japanese)

    def get_average(self):
        return (self.math+self.english+self.japanese)/3.0

taro = Score("太郎",60,70,80)
jiro = Score("二郎",80,70,90)
saburo = Score("三郎",50,30,60)

list=[taro,jiro,saburo]
print(max([x.math for x in list]))
print(taro.average)
