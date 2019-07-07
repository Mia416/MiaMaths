'''
Created on Jan 23, 2019

@author: paul
'''
import random
import operator

def generatenum(n):
    return random.randint(1,int(n))

def cal(num1,num2,op):
    temp = 0;
    if op==("+"):
        temp = operator.add(num1, num2)
    if op==("-"):
        temp = operator.sub(num1, num2)
    if op==("*"):
        temp = operator.mul(num1, num2)
    if op==("/"):
        temp = operator.truediv(num1, num2)
        
    return int(temp)
    
# model A 101 - ( 65 + 50 ) + 13 = 
def model1():
     L = []
     for i in range(4):
         num = random.randint(1,200)
         L.append(num)
     L.sort(reverse=True)
     op1 = random.choice("+*")
     op2 = random.choice("/")
     op3 = random.choice("+-*")
     op4 ="("
     op5 = ")"
     
     if op2=="-":
         while(L[1]<L[2]):
             L[2] = generatenum(99)
     if op2=="/":
         while(L[1]%L[2]!=0):
             L[2] = generatenum(99)
             L[1] = operator.mul(L[2], generatenum(10))   
     print("%d %s %s %d %s %d %s %s %d = " % (L[0],op1,op4,L[1],op2,L[2],op5,op3,L[3]))
     
     temp1 = cal(L[1],L[2],op2)
     if op3=="*":
         temp2 = cal(temp1,L[3],op3)
         result_temp = cal(L[0],temp2,op1)
     else:
         temp2 = cal(temp1,L[0],op1)
         result_temp = cal(temp2,L[3],op3)    
     
     print (result_temp)

# Model B: 4*6+(8*3)
def model2():
     L = []
     for i in range(4):
         num = random.randint(1,200)
         L.append(num)
     L.sort(reverse=True)
     op1 = random.choice("+*/")
     op2 = random.choice("+-*")
     op3 = random.choice("+-*")
     op4 ="("
     op5 = ")"     
     if op3=="-":
         while(L[2]<L[3]):
             L[3] = generatenum(99)
     if op1=="/":
         while(L[0]%L[1]!=0):
             L[1] = generatenum(99)
             L[0] = operator.mul(L[1], generatenum(10)) 
     if op3=="/":
         while(L[2]%L[3]!=0):
             L[3] = generatenum(99)
             L[2] = operator.mul(L[3], generatenum(10))     
     print("%d %s %d %s %s %d %s %d %s = " % (L[0],op1,L[1],op2,op4,L[2],op3,L[3],op5))


     temp1 = cal(L[2],L[3],op3)
     if op2=="*":
         temp2 = cal(L[1],temp1,op2)
         result_temp = cal(L[0],temp2,op1)
     else:    
        temp2 = cal(L[0],L[1],op1)
        result_temp = cal(temp2,temp1,op3)
        
     print (result_temp)   
#model C :(a+b)*c-d
def model3():
     L = []
     for i in range(4):
         num = random.randint(1,200)
         L.append(num)
     L.sort(reverse=True)
     op1 = random.choice("+-*/")
     op2 = random.choice("+-*")
     op3 = random.choice("+-*/")
     op4 ="("
     op5 = ")"     
     if op1=="-":
         while(L[0]<L[1]):
             L[1] = generatenum(99)
     if op1=="/":
         while(L[0]%L[1]!=0):
             L[1] = generatenum(99)
             L[0] = operator.mul(L[1], generatenum(10)) 
     if op3=="/":
         while(L[2]%L[3]!=0):
             L[3] = generatenum(99)
             L[2] = operator.mul(L[3], generatenum(10))     
     print("%s %d %s %d %s %s %d %s %d  = " % (op4,L[0],op1,L[1],op5,op2,L[2],op3,L[3]))


     temp1 = cal(L[0],L[1],op1)
     if (op3=="*") or (op3=="/"):
         temp2 = cal(L[2],L[3],op3)
         result_temp = cal(temp1,temp2,op2)
     else:
         temp2 = cal(temp1,L[2],op2)
         result_temp = cal(temp2,L[3],op3)
    
     print(result_temp)

#Model D: a+b-c+d
def model4():
     L = []
     for i in range(4):
         num = random.randint(1,200)
         L.append(num)
     L.sort(reverse=True)
     op1 = random.choice("+-*/")
     op2 = random.choice("+*")
     op3 = random.choice("+-*/")
    
     if op1=="-":
         while(L[0]<L[1]):
             L[1] = generatenum(99)
     if op1=="/":
         while(L[0]%L[1]!=0):
             L[1] = generatenum(99)
             L[0] = operator.mul(L[1], generatenum(10)) 
     if op3=="/":
         while(L[2]%L[3]!=0):
             L[3] = generatenum(99)
             L[2] = operator.mul(L[3], generatenum(10))    
 
     print(" %d %s %d %s %d %s %d  = " % (L[0],op1,L[1],op2,L[2],op3,L[3]))
     
     if op1=="*" or op1=="/" :
         temp1 = cal(L[0],L[1],op1)
         if op2=="*":
             temp2 = cal(temp1,L[2],op2)
             result_temp = cal(temp2,L[3],op3)
         else :
             if op3=="*" or op3=="/" :
                 temp2 = cal(L[2],L[3],op3)
                 result_temp = cal(temp1,temp2,op2)
             else:
                 temp2 = cal(temp1,L[2],op2)
                 result_temp = cal(temp2,L[3],op3)   
     else:
         if op2=="*":
             temp1=cal(L[1],L[2],op2)
             if op3=="*" or op3=="/" :
                 temp2 =cal(temp1,L[3],op3)
                 result_temp = cal(L[0],temp2,op1)
             else:
                 temp2 = cal(L[0],temp1,op2)
                 result_temp = cal(temp2,L[3],op3)
        
         else:
             if op3=="*" or op3=="/" :
                 temp1 =cal(L[2],L[3],op3)
                 temp2 =cal(L[0],L[1],op1)
                 result_temp=cal(temp2,temp1,op2)
                 
             else:
                 temp1 =cal(L[0],L[1],op1)
                 temp2 =cal(temp1,L[2],op2)
                 result_temp =cal(temp2,L[3],op3)
                 
     print (result_temp)
                 
                 
                     
list = ['A', 'B', 'C', 'D']

def weight_choice(weight):
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i

def generate(n):
    for i in range(n):
        model = list[weight_choice([3, 3, 3, 1])]
        if model=="A":
             model1()
        if model=="B":
             model2()
        if model=="C":    
            model3()
        if model=="D":
             model4()

generate(10)   

 
