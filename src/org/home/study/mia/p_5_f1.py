from docx import *
from docx.shared import Pt
from CommonClass import M_Doc
from CommonClass import Gen_Data
import random
import operator
import math



#2x+5=10.00
def modelA():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Decimal(1.00,20.00,2)
    s1 = G_data.Generate_Int(2,10)
    s2 = G_data.Generate_Int(2,20)
    x = "X"
    op = "+"
    s3 = operator.mul(s0, s1)
    s3 = operator.add(s3, s2)
    result = "%d %s %s %d = %.2f" %(s1,x,op,s2,s3)
    return result,float(s0)

#2.00+5x=10.00
def modelB():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Decimal(1.00,20.00,2)
    x = "X"
    op = "+"
    s1 = G_data.Generate_Decimal(3.00,50.00,2)
    s2 = G_data.Generate_Int(2,10)
    s3 = operator.mul(s0, s2)
    s3 = operator.add(s3, s1)
    result = "%.2f %s %d %s = %.2f" %(s1,op,s2,x,s3)
    return result,float(s0)


#2x-5.00=10.00
def modelC():
    G_data= Gen_Data()
    flag = True
    s0 =  G_data.Generate_Decimal(10.00,20.00,2)
    x = "X"
    op = "-"
    s1 = G_data.Generate_Int(2,20)
    s2 = G_data.Generate_Decimal(1.00,20.00,2)
    s3 = operator.mul(s1, s0)
    s3 = operator.sub(s3, s2)
    result = "%d %s %s %.2f = %.2f" %(s1,x,op,s2,s3)
    return result,float(s0)



#20.00-5x=10.00
def modelD():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Decimal(200.00,500.00,2)
    x = "X"
    op = "-"
    s1 = G_data.Generate_Decimal(2.00,10.00,2)
    s2 = G_data.Generate_Int(1,9)
    s3 = operator.mul(s1, s2)
    s3 = operator.sub(s0, s3)
    result = "%.2f %s %d %s = %.2f" %(s0,op,s2,x,s3)
    return result,float(s1)





list = ['A','B','C','D']

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
        model = list[weight_choice([2,3,2,3])]
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

    d.Save_Doc(document,"t7.docx")

generate(100)
