import random
import operator
from decimal import Decimal


def generatenum(n):
    result_group = {}
    for i in range(n):
        result_ = modelA()
        result_group[str(i)] = result_
        result_ = modelB()
        result_group[str(i)] = result_


    for key,value in result_group.items():
        print (key, '=>', result_group[key])
        #modelB()
        #modelC()
        #modelD()
        #modelE()
        #modelF()
        #modelG()
        #modelA()
        #modelB()



def generateIntSub(n,m):
    return random.randint(int(n),int(m))

#x+1=2
def modelA():
     op = "+"
     s1 = generateIntSub(1,50)
     s2 = generateIntSub(1,50)
     result_ = operator.add(s2, s1)
     print("%s %s %d = " %(s1,op,s2))


#1+x=2
def modelB():
     op = "-"
     s1 = generateIntSub(51,100)
     s2 = generateIntSub(0,50)
     result_ = operator.sub(s1, s2)
     print("%d %s %s =" %(s1,op,s2))






list = ['A', 'B']

def weight_choice(weight):
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i

def generate(n):
    result_group = {}
    for i in range(n):
        model = list[weight_choice([5,5])]
        if model=="A":
            result_ = modelA()
        if model=="B":
            result_ = modelB()

        result_group[str(i)] = result_

    for key,value in result_group.items():
            print (key, '=>', result_group[key])

generate(5000)
