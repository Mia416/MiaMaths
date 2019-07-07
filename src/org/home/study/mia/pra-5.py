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


def modelSub(flag):
    s0 = generateIntSub(50,99)
    s1 = generateDecimalMiuns(2)
    m = "-"
    re = operator.sub(s0, s1)
    print("%d %s %.2f = " %(s0,m,s1))
    if (flag): 
         print("%d %s %.2f = %.2f" %(s0,m,s1,re)) 
    

def modelPlus(flag):
    s0 = generateDecimalMiuns(2)
    s1 = generateDecimalA(3)
    m = "+"
    re = operator.add(s0, s1)
    print("%.2f %s %.3f = " %(s0,m,s1)) 
    if (flag):
         print("%.2f %s %.3f = %.3f" %(s0,m,s1,re)) 

def modelC(flag):
    s0 = generateDecimalA(2)
    s1 = generateInt(30)
    m = "*"
    re = operator.mul(s0, s1)
    print("%.2f %s %d = " %(s0,m,s1)) 
    if (flag):
         print("%.2f %s %d = %.2f" %(s0,m,s1,re)) 
    
def modelD(flag):
    s0 = generateDecimalA(2)
    s1 = generateInt(30)
    m = "/"
    re = operator.mul(s0, s1)
    print("%.2f %s %.2f = " %(re,m,s0))  
    if (flag):
         print("%.2f %s %.2f = %.2f" %(re,m,s0,s1))  

def modelA(flag):
    s0 = generateDecimal(1)  
    s1 = generateDecimal(3)
    m = "*"
    re = operator.mul(s0, s1)
    print("%.1f %s %.1f = " %(s0,m,s1))
    if (flag):
        print("%.1f %s %.1f = %.1f" %(s0,m,s1,re))  
    
    
def modelB(flag):
    s0 = generateDecimal(1)  
    s1 = generateInt(20)
    m = "/"
    re = operator.mul(s0, s1)
    print("%.1f %s %d = " %(re,m,s1))
    if (flag):
         print("%.1f %s %d = %.1f" %(re,m,s1,s0))


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
    
generate(100,True) 