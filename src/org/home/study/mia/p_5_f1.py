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
    op = G_data.opAdd
    s3 = operator.mul(s0, s1)
    s3 = operator.add(s3, s2)
    result = "%d %s %s %d = %.2f" %(s1,x,op,s2,s3)
    return result,float(s0)

#2.00+5x=10.00
def modelB():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Decimal(1.00,20.00,2)
    x = "X"
    op = G_data.opAdd
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
    op = G_data.opSub
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
    op = G_data.opSub
    s1 = G_data.Generate_Decimal(2.00,10.00,2)
    s2 = G_data.Generate_Int(1,9)
    s3 = operator.mul(s1, s2)
    s3 = operator.sub(s0, s3)
    result = "%.2f %s %d %s = %.2f" %(s0,op,s2,x,s3)
    return result,float(s1)


#18(x-2)=270
def modelE():
    G_data= Gen_Data()
    s0 =  G_data.Generate_Int(2,20)
    x = "X"
    op = G_data.opSub
    s1 = G_data.Generate_Int(2,20)
    s2 = operator.mul(s0, s1)
    s3 = G_data.Generate_Int(2,s1)
    result_ =  operator.add(s1, s3)
    result = "%d(%s %s %d) = %d" %(s0,x,op,s3,s2)
    return result,result_

#(200-x)÷4=20
def modelF():
    G_data= Gen_Data()
    s0 = G_data.Generate_Int(2,20)
    s1 = G_data.Generate_Int(2,20)
    s2 = operator.mul(s0, s1)
    x = "X"
    op1 = G_data.opSub
    op2 = G_data.opDiv
    s3 = G_data.Generate_Int(s2,1000)
    result_ = operator.sub(s3, s2)
    result = "( %d %s %s ) %s %d = %d" %(s3,op1,x,op2,s1,s0)
    return result,result_

#100÷（x+5）=10
def modelG():
    G_data= Gen_Data()
    s0 = G_data.Generate_Int(2,30)
    s1 = G_data.Generate_Int(2,30)
    s2 = operator.mul(s0, s1)
    x = "X"
    op1 = G_data.opAdd
    op2 = G_data.opDiv
    s3 = G_data.Generate_Int(2,s1)
    result_ = operator.sub(s1, s3)
    result = "%d %s ( %s %s %d ) = %d" %(s2,op2,x,op1,s3,s0)
    return result,result_


#(8+x)÷5=10
def modelH():
    G_data= Gen_Data()
    s0 = G_data.Generate_Int(2,30)
    s1 = G_data.Generate_Int(2,30)
    s2 = operator.mul(s0, s1)
    x = "X"
    op1 = G_data.opAdd
    op2 = G_data.opDiv
    s3 = G_data.Generate_Int(2,s2)
    result_ = operator.sub(s2, s3)
    result = "( %d %s %s ) %s %d = %d" %(s3,op1,x,op2,s1,s0)
    return result,result_

#x÷5-8=10
def modelI():
    G_data= Gen_Data()
    s0 = G_data.Generate_Int(2,30)
    s1 = G_data.Generate_Int(50,100)
    s2 = G_data.Generate_Int(2,s1)
    s3 = operator.sub(s1, s2)
    x = "X"
    op1 = G_data.opDiv
    op2 = G_data.opSub
    result_ =  operator.mul(s0, s1)
    result = "%s %s %d %s %d = %d" %(x,op1,s0,op2,s2,s3)
    return result,result_


#100÷5x=2
def modelJ():
    G_data= Gen_Data()
    s0 = G_data.Generate_Int(2,9)
    s1 = G_data.Generate_Int(2,19)
    s2 = G_data.Generate_Int(2,9)
    s3 = operator.mul(operator.mul(s0, s1),s2)
    x = "X"
    op1 = G_data.opDiv
    op2 = G_data.opMul
    result_ =  s0
    result = "%d %s %d %s = %d" %(s3,op1,s1,x,s0)
    return result,result_

list = ['A','B','C','D','E','F','G','H','I','J']

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
        model = list[weight_choice([1,1,1,1,1,1,1,1,1,1])]
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
        if model=="H":
             result,result_ = modelH()
        if model=="I":
            result,result_ = modelI()
        if model=="J":
            result,result_ = modelJ()

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

generate(1000)
