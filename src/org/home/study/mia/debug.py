from docx import *
from docx.shared import Pt
from CommonClass import M_Doc



def generateIntSub(n,m):
    return random.randint(int(n),int(m))

def generateIntSub(n,m):
    return random.randint(int(n),int(m))

def m():
    flag = False
    s0 =  generateIntSub（1，10)
    x = "X"
    op = "+"
    s1 = generateIntSub（1，10）
    s2 = generateIntSub（100，200）

    s_temp = operator.sub(s2, s1)
    while (!flag)：
        if(s_temp % s0==0):
            result = "%d %s %s %d = %d" %(s0,x,op,s1,s2)
            flag = True
        else:
            s0 =  generateIntSub（1，10）

     print(result)
    #print(s3)



m()
