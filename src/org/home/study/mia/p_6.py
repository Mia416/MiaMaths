import random
import operator
from decimal import Decimal
from docx import *
from docx.shared import Pt
from CommonClass import M_Doc


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
     s0 = "X"
     op = "+"
     s1 = generateIntSub(1,50)
     s2 = generateIntSub(51,150)
     result_ = operator.sub(s2, s1)
     result = "%s %s %d = %d" %(s0,op,s1,s2)
     #print("%s %s %d = %d" %(s0,op,s1,s2))
     return result,result_

#1+x=2
def modelB():
     s0 = "X"
     op = "+"
     s1 = generateIntSub(1,50)
     s2 = generateIntSub(51,150)
     result_ = operator.sub(s2, s1)
     result = "%d %s %s = %d" %(s1,op,s0,s2)
     #print("%d %s %s = %d" %(s1,op,s0,s2))
     return result,result_

#x-1=2
def modelC():
     s0 = "X"
     op = "-"
     s1 = generateIntSub(51,150)
     s2 = generateIntSub(1,50)
     result_ = operator.add(s2, s1)
     result = "%s %s %d = %d" %(s0,op,s1,s2)
     #print("%s %s %d = %d" %(s0,op,s1,s2))
     return result,result_

#1-x=2
def modelD():
     s0 = "X"
     op = "-"
     s1 = generateIntSub(51,150)
     s2 = generateIntSub(1,50)
     result_ = operator.sub(s1, s2)
     result = "%d %s %s = %d" %(s1,op,s0,s2)
     #print("%d %s %s = %d" %(s1,op,s0,s2))
     return result,result_

#2X=10
def modelE():
     s0 = "X"
     s1 = generateIntSub(1,20)
     s2 = generateIntSub(1,20)
     s3 = operator.mul(s1, s2)
     result = "%d %s = %d" %(s1,s0,s3)
     #print("%d %s = %d" %(s1,s0,s3))
     return result,s2

#2÷x=1
def modelF():
     s0 = "X"
     op = "÷"
     s1 = generateIntSub(1,20)
     s2 = generateIntSub(1,20)
     s3 = operator.mul(s1, s2)
     result = "%d %s %s  = %d" %(s3,op,s0,s1)
     #print("%d %s %s  = %d" %(s3,op,s0,s1))
     return result,s2

# x÷1=2
def modelG():
     s0 = "X"
     op = "÷"
     s1 = generateIntSub(1,20)
     s2 = generateIntSub(1,20)
     result_ = operator.mul(s1, s2)
     result = "%s %s %d  = %d" %(s0,op,s1,s2)
     #print("%s %s %d  = %d" %(s0,op,s1,s2))
     return result,result_




list = ['A', 'B', 'C', 'D','E','F','G']

def weight_choice(weight):
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i

def generate(n):
    document = Document()
    d = M_Doc()
    result_group = {}
    for i in range(n):
        model = list[weight_choice([2,2, 2, 1,1,1,1])]
        if model=="A":
            result,result_ = modelA()
        if model=="B":
            result,result_ = modelB()
        if model=="C":
            result,result_ = modelC()
        if model=="D":
            result,result_ = modelD()
        if model=="E":
            result,result_ = modelE()
        if model=="F":
             result,result_ = modelF()
        if model=="G":
             result,result_ = modelG()

        d.Add_Process(document,result)
        #d.Add_Process(document,"")
               
        result_group[str(i)] = result_

    for key,value in result_group.items():
            number = str(key)
            val = result_group[key]
            s_temp = "%s => %s " %(number,val)
            #print (key, '=>', result_group[key])
            #d.Add_Process(document,s_temp)
            
    d.Save_Doc(document,"t3.docx")

generate(500)
