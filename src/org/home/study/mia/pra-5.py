'''


@author: Paul
'''
import random
import operator
from decimal import Decimal

#debug use
def generatenum(n):
    for i in range(n):
        modelD()
        #modelA()
        #modelB()

def generateDecimalA(n):
    return (round(random.uniform(0.01,0.59),n))

def generateDecimal(n):
    return (round(random.uniform(0.01,9.99),n))

def generateDecimalMiuns(n):
    return (round(random.uniform(0.01,50.00),n))

def generateInt(n):
    return random.randint(1,int(n))

def generateIntSub(n,m):
    return random.randint(int(n),int(m))

#51-5.55
def modelSub():
    s0 = generateIntSub(50,99)
    s1 = generateDecimalMiuns(2)
    m = "-"
    re = operator.sub(s0, s1)
    print("%d %s %.2f = " %(s0,m,s1))
    return re


#5.55+1.44
def modelPlus():
    s0 = generateDecimalMiuns(2)
    s1 = generateDecimalA(3)
    m = "+"
    re = operator.add(s0, s1)
    print("%.2f %s %.3f = " %(s0,m,s1))
    return re

#0.44*28
def modelC():
    s0 = generateDecimalA(2)
    s1 = generateInt(30)
    m = "×"
    re = operator.mul(s0, s1)
    print("%.2f %s %d = " %(s0,m,s1))
    return re


#0.44÷15
def modelD():
    s0 = generateDecimalA(2)
    s1 = generateInt(30)
    m = "÷"
    re = operator.mul(s0, s1)
    print("%.2f %s %.2f = " %(re,m,s0))
    return re


#0.5×0.555
def modelA():
    s0 = generateDecimal(1)
    s1 = generateDecimal(3)
    m = "×"
    re = round(operator.mul(s0, s1),4)
    print("%.1f %s %.1f = " %(s0,m,s1))
    return re


#9.9÷15
def modelB():
    s0 = generateDecimal(1)
    s1 = generateInt(20)
    m = "÷"
    re = operator.mul(s0, s1)
    print("%.1f %s %d = " %(re,m,s1))
    return re



list = ['A', 'B', 'C', 'D','E','F']

def weight_choice(weight):
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i

def generate(n):
    result_group = {}
    for i in range(n):
        model = list[weight_choice([10,0,0,0,0,0])]
        print(i,':')
        if model=="A":
             result_ = modelA()
        if model=="B":
             result_ = modelB()
        if model=="C":
            result_ = modelC()
        if model=="D":
            result_ = modelD()
        if model=="E":
            result_ = modelPlus()
        if model=="F":
            result_ = modelSub()
        result_group[str(i)] = result_
        
    for key,value in result_group.items():
            print (key, '=>', result_group[key])

generate(100)
