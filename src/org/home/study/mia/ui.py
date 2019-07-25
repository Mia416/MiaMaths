from docx import *
from docx.shared import Pt,Mm
from CommonClass import M_Doc
from CommonClass import Gen_Data
import operator
from docxtpl import DocxTemplate, InlineImage
import jinja2
from PIL import Image
from resizeimage import resizeimage
import os





pic_original = 'pic_draft'
pic_ready = 'pic'
pic_set = []




for filename in os.listdir('pic_draft'):
    if filename.endswith('.jpg'):
        with open('pic_draft\%s'%(filename), 'r+b') as f:
            with Image.open(f) as image:
                x,y = image.size
                x_s=  int(250)
                y_s = int(y * x_s / x)
                out = image.resize((80,80),Image.ANTIALIAS)
                newpath = 'pic\%s'%(filename)
                out.save(newpath)                
                #pic_set.append(newpath)
                pic_set.append('pic_draft\%s'%(filename))


def getImageSize(path):
    with open(path, 'r+b') as f:
        with Image.open(f) as image:
            return image.size


#doc = DocxTemplate("template.docx")
tpl=DocxTemplate('templates/dynamic_table_111.docx')
b=[]
for i in pic_set:
    width,height = getImageSize(pic_set[pic_set.index(i)])
    b.append(InlineImage(tpl,pic_set[pic_set.index(i)] ,width=Mm(100), height=Mm(100)))


#context = {
#    'chen_test' :[InlineImage(tpl,pic_set[0] ,width=Mm(100), height=Mm(50)),InlineImage(tpl,pic_set[1],width=Mm(100), height=Mm(50)),InlineImage(tpl,pic_set[2],width=Mm(100), height=Mm(50))],
#}

context = {
    'chen_test' :b,
}






jinja_env = jinja2.Environment(autoescape=True)
tpl.render(context,jinja_env)

tpl.save("generated_doc.docx")
