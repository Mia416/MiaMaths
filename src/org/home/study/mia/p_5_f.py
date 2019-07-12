from docx import *
from docx.shared import Pt
from CommonClass import M_Doc
from CommonClass import Gen_Data
import random
import operator
import math



#2x+5=10
def modelA():
    G_data= Gen_Data()
    flag = True
    s0 =  G_data.Generate_Int(1,20)
    x = "X"
    op = "+"
    s1 = G_data.Generate_Int(1,50)
    s2 = G_data.Generate_Int(100,500)
    s_temp = operator.sub(s2, s1)
    while (flag):
        #print(s_temp)
        #print(s0)
        if(s_temp % s0==0):
            result = "%d %s %s %d = %d" %(s0,x,op,s1,s2)
            flag = False
        else:
            mid = int(math.sqrt(s_temp))
            if (s0>=mid):
                s0 =  operator.add(s0, 1)
            elif(s0<=mid):
                s0 =  operator.sub(s0, 1)

    s_result = operator.truediv(s_temp,s0)
    if ((s_result==1)|(s_result==s_temp)):
        return '',''
    else:
        return result,int(s_result)


#2+5x=10
def modelB():
    G_data= Gen_Data()
    flag = True
    s0 =  G_data.Generate_Int(2,10)
    x = "X"
    op = "+"
    s1 = G_data.Generate_Int(2,10)
    s2 = G_data.Generate_Int(100,200)
    s_temp = operator.sub(s2, s0)
    while (flag):
        if(s_temp % s1==0):
            result = "%d %s %d %s = %d" %(s0,op,s1,x,s2)
            flag = False
        else:
            mid = int(math.sqrt(s_temp))
            if (s1>=mid):
                s1 =  operator.add(s1, 1)
            elif(s1<=mid):
                s1 =  operator.sub(s1, 1)

    s_result = operator.truediv(s_temp,s1)
    if ((s_result==1)|(s_result==s_temp)):
        return '',''
    else:
        return result,int(s_result)


#2x-5=10
def modelC():
    G_data= Gen_Data()
    flag = True
    s0 =  G_data.Generate_Int(2,10)
    x = "X"
    op = "-"
    s1 = G_data.Generate_Int(2,50)
    s2 = G_data.Generate_Int(100,2000)
    s_temp = operator.add(s2, s0)
    while (flag):
        if(s_temp % s0==0):
            result = "%d %s %s %d = %d" %(s0,x,op,s1,s2)
            flag = False
        else:
            mid = int(math.sqrt(s_temp))
            if (s0>=mid):
                s0 =  operator.add(s0, 1)
            elif(s0<=mid):
                s0 =  operator.sub(s0, 1)

    s_result = operator.truediv(s_temp,s0)
    if ((s_result==1)|(s_result==s_temp)):
        return '',''
    else:
        return result,int(s_result)


#20-5x=10
def modelD():
    G_data= Gen_Data()
    flag = True
    s0 =  G_data.Generate_Int(200,1000)
    x = "X"
    op = "-"
    s1 = G_data.Generate_Int(2,10)
    s2 = G_data.Generate_Int(1,199)
    s_temp = operator.sub(s0, s2)
    while (flag):

        if(s_temp % s1==0):
            result = "%d %s %d %s = %d" %(s0,op,s1,x,s2)
            flag = False
        else:
            mid = int(math.sqrt(s_temp))
            if (s1>=mid):
                s1 =  operator.add(s1, 1)
            elif(s1<=mid):
                s1 =  operator.sub(s1, 1)
    s_result = operator.truediv(s_temp,s1)
    if ((s_result==1)|(s_result==s_temp)):
        return '',''
    else:
        return result,int(s_result)


#2x÷2=10
def modelE():
    G_data= Gen_Data()
    flag = True
    s0 =  G_data.Generate_IntRange(2,20,2)
    x = "X"
    op = "÷"
    s1 = G_data.Generate_Int(5,20)
    s2 = G_data.Generate_IntRange(50,500,2)
    s_temp = operator.mul(s1, s2)
    while (flag):
        if(s_temp % s0==0):
            result = "%d %s %s %d = %d" %(s0,x,op,s1,s2)
            flag = False
        else:
            mid = int(math.sqrt(s_temp))
            if (s0>=mid):
                s0 =  operator.add(s0, 1)
            elif(s1<=mid):
                s0 =  operator.sub(s0, 1)
    s_result = operator.truediv(s_temp,s0)
    if ((s_result==1)|(s_result==s_temp)):
        return '',''
    else:
        return result,int(s_result)



list = ['A','B','C','D','E']

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
        model = list[weight_choice([2,2,2,2,2])]
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

        if(result.strip()!=''):
            print(result)
            print(result_)
            d.Add_Process(document,result)


        result_group[str(i)] = result_

    for key,value in result_group.items():
            number = str(key)
            val = result_group[key]
            s_temp = "%s => %s " %(number,val)
            #print (key, '=>', result_group[key])
            d.Add_Process(document,s_temp)

    d.Save_Doc(document,"t5.docx")

generate(500)
