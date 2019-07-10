import random
import operator
from decimal import Decimal


def generatenum(n):
    for i in range(n):
        modelA()
        modelB()
        modelC()
        modelD()
        modelE()
        modelF()
        modelG()
        #modelA()
        #modelB()



def generateIntSub(n,m):
    return random.randint(int(n),int(m))


def modelA():
     s0 = "X"
     op = "+"
     s1 = generateIntSub(1,50)
     s2 = generateIntSub(51,150)
     print("%s %s %d = %d" %(s0,op,s1,s2))

def modelB():
     s0 = "X"
     op = "+"
     s1 = generateIntSub(1,50)
     s2 = generateIntSub(51,150)
     print("%d %s %s = %d" %(s1,op,s0,s2))

def modelC():
     s0 = "X"
     op = "-"
     s1 = generateIntSub(51,150)
     s2 = generateIntSub(1,50)
     print("%s %s %d = %d" %(s0,op,s1,s2))

def modelD():
     s0 = "X"
     op = "-"
     s1 = generateIntSub(51,150)
     s2 = generateIntSub(1,50)
     print("%d %s %s = %d" %(s1,op,s0,s2))

def modelE():
     s0 = "X"
     s1 = generateIntSub(1,20)
     s2 = generateIntSub(1,20)
     s3 = operator.mul(s1, s2)
     print("%d %s = %d" %(s1,s0,s3))

def modelF():
     s0 = "X"
     op = "÷"
     s1 = generateIntSub(1,20)
     s2 = generateIntSub(1,20)
     s3 = operator.mul(s1, s2)
     print("%d %s %s  = %d" %(s3,op,s0,s1))
def modelG():
     s0 = "X"
     op = "÷"
     s1 = generateIntSub(1,20)
     s2 = generateIntSub(1,20)

     print("%s %s %d  = %d" %(s0,op,s1,s2))




list = ['A', 'B', 'C', 'D','E','F']

def weight_choice(weight):
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i

def generate(n,flag):
    for i in range(n):
        model = list[weight_choice([2, 2, 2, 2,1,1])]
        if model=="A":
             modelA(flag)
        if model=="B":
             modelB(flag)
        if model=="C":
            modelC(flag)
        if model=="D":
             modelD(flag)
        if model=="E":
             modelPlus(flag)
        if model=="F":
             modelSub(flag)

generatenum(10)
