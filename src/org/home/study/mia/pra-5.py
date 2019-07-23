'''


@author: Paul
'''
import random
import operator
from decimal import Decimal
from docx import *
from docx.shared import Pt
from CommonClass import M_Doc
from CommonClass import Gen_Data

#debug use
def generatenum(n):
    for i in range(n):
        result,result_ = modelA()
        print (result)
        print (result_)



#51-5.555
def modelSub():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Int(50,99)
    s1 =  G_data.Generate_Decimal(1.001,30.001,3)
    op =  G_data.opSub
    re = operator.sub(s0, s1)
    result = "%d %s %.3f = " %(s0,op,s1)
    result_ = float(re)
    return result,result_


#5.55+1.444
def modelPlus():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Decimal(1.01,50.00,2)
    s1 =  G_data.Generate_Decimal(1.001,30.001,3)
    op =  G_data.opAdd
    re = operator.add(s0, s1)
    result = "%.2f %s %.3f = " %(s0,op,s1)
    result_ = float(re)
    return result,result_

#0.44*28
def modelC():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Int(1,99)
    s1 =  G_data.Generate_Int(1,20)
    op =  G_data.opDiv
    re =  operator.truediv(operator.mul(s0, s1),10000)
    s0 =  operator.truediv(s0,100)
    result = "%.4f %s %.2f = " %(re,op,s0)
    result_ = float(operator.truediv(s1,100))
    return result,result_


#37.820÷4
def modelD():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Decimal(1.001,10.001,3)
    s1 =  G_data.Generate_Int(1,20)
    op =  G_data.opDiv
    re = operator.mul(s0, s1)
    result = "%.3f %s %d = " %(re,op,s1)
    result_ = float(s0)
    return result,result_


#0.5×0.55
def modelA():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Decimal(1.00,20.00,1)
    s1 =  G_data.Generate_Decimal(1.00,10.00,2)
    op =  G_data.opMul
    re = operator.mul(s0, s1)
    result = "%.1f %s %.2f = " %(s0,op,s1)
    result_ = float(re)
    return result,result_


#4.42÷2.6
def modelB():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Decimal(1.00,20.00,1)
    s1 =  G_data.Generate_Decimal(1.00,10.00,1)
    op =  G_data.opDiv
    re = operator.mul(s0, s1)
    result = "%.3f %s %.1f = " %(re,op,s0)
    result_ = float(s1)
    return result,result_



list = ['A', 'B', 'C', 'D','E','F']

def weight_choice(weight):
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i

def generate(n):
    result_group = {}
    document = Document()
    d = M_Doc()
    for i in range(n):
        model = list[weight_choice([2, 2, 2, 2,1,1])]
        #print(n)
        if model=="A":
             result,result_ = modelA()
        if model=="B":
             result,result_ = modelB()
        if model=="C":
            result,result_  = modelC()
        if model=="D":
             result,result_ = modelD()
        if model=="E":
            result,result_ = modelPlus()
        if model=="F":
            result,result_ = modelSub()

        d.Add_Process(document,result)
        result_group[str(i)] = result_

    for key,value in result_group.items():
            number = str(key)
            val = result_group[key]
            s_temp = "%s => %s " %(number,val)
            d.Add_Process(document,s_temp)

    d.Save_Doc(document,"t7.docx")




generate(1000)
