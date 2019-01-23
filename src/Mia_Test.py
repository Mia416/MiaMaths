'''
Created on Jan 23, 2019

@author: paul
'''
import random
import operator

def generatenum(n):
    return random.randint(1,int(n))

# model A 101 - ( 65 + 50 ) + 13 = 
def model1():
     L = []
     for i in range(4):
         num = random.randint(1,200)
         L.append(num)
     L.sort(reverse=True)
     op1 = random.choice("+*")
     op2 = random.choice("%")
     op3 = random.choice("+-*")
     op4 ="("
     op5 = ")"
     
     if op2=="-":
         while(L[1]<L[2]):
             L[2] = generatenum(100)
     if op2=="%":
         while(L[1]%L[2]!=0):
             L[2] = generatenum(100)
             L[1] = operator.mul(L[2], generatenum(10))   
     print("%d %s %s %d %s %d %s %s %d = " % (L[0],op1,op4,L[1],op2,L[2],op5,op3,L[3]))
     

# Model B: 4*6+(8*3)
def model2():
     L = []
     for i in range(4):
         num = random.randint(1,200)
         L.append(num)
     L.sort(reverse=True)
     op1 = random.choice("+*%")
     op2 = random.choice("+-*")
     op3 = random.choice("+-*")
     op4 ="("
     op5 = ")"     
     if op3=="-":
         while(L[2]<L[3]):
             L[3] = generatenum(100)
     if op1=="%":
         while(L[0]%L[1]!=0):
             L[1] = generatenum(100)
             L[0] = operator.mul(L[1], generatenum(10)) 
     if op3=="%":
         while(L[2]%L[3]!=0):
             L[3] = generatenum(100)
             L[2] = operator.mul(L[3], generatenum(10))     
     print("%d %s %d %s %s %d %s %d %s = " % (L[0],op1,L[1],op2,op4,L[2],op3,L[3],op5))

#model C :(a+b)*c-d
def model3():
     L = []
     for i in range(4):
         num = random.randint(1,200)
         L.append(num)
     L.sort(reverse=True)
     op1 = random.choice("+-*%")
     op2 = random.choice("+-*")
     op3 = random.choice("+-*%")
     op4 ="("
     op5 = ")"     
     if op1=="-":
         while(L[0]<L[1]):
             L[1] = generatenum(100)
     if op1=="%":
         while(L[0]%L[1]!=0):
             L[1] = generatenum(100)
             L[0] = operator.mul(L[1], generatenum(10)) 
     if op3=="%":
         while(L[2]%L[3]!=0):
             L[3] = generatenum(100)
             L[2] = operator.mul(L[3], generatenum(10))     
     print("%s %d %s %d %s %s %d %s %d  = " % (op4,L[0],op1,L[1],op5,op2,L[2],op3,L[3]))

#Model D: a+b-c+d
def model4():
     L = []
     for i in range(4):
         num = random.randint(1,200)
         L.append(num)
     L.sort(reverse=True)
     op1 = random.choice("+-*%")
     op2 = random.choice("+*")
     op3 = random.choice("+-*%")
    
     if op1=="-":
         while(L[0]<L[1]):
             L[1] = generatenum(100)
     if op1=="%":
         while(L[0]%L[1]!=0):
             L[1] = generatenum(100)
             L[0] = operator.mul(L[1], generatenum(10)) 
     if op3=="%":
         while(L[2]%L[3]!=0):
             L[3] = generatenum(100)
             L[2] = operator.mul(L[3], generatenum(10))    
 
     print(" %d %s %d %s %d %s %d  = " % (L[0],op1,L[1],op2,L[2],op3,L[3]))
     
list = ['A', 'B', 'C', 'D']

def weight_choice(weight):
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i

def generate(n):
    for i in range(n):
        model = list[weight_choice([5, 2, 2, 1])]
        if model=="A":
             model1()
        if model=="B":
             model2()
        if model=="C":    
            model3()
        if model=="D":
             model4()

generate(30)   
