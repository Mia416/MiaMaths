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

G_data= Gen_Data()
s0 =  G_data.Generate_Decimal(1.00,20.00,2)
s1 = G_data.Generate_Int(2,10)
s2 = G_data.Generate_Int(2,20)
s3 = operator.mul(s0, s1)
s3 = operator.add(s3, s2)
x = "X"
op = "+"
result = "%d %s %s %d = %s" %(s1,x,op,s2,s_temp)
s_temp = "%.2f" %(s_temp)
print (result)
print (s0)



pic_original = 'D:\\pic\\pic\\'
pic_ready = 'D:\\pic\\ready\\'
pic_set = []

for filename in os.listdir(pic_original):
    if filename.endswith('.jpg'):
        with open("%s%s" %(pic_original,filename), 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_thumbnail(image, [500, 300])
                newpath = "%s%s" %(pic_ready,filename)
                cover.save(newpath, image.format)
                pic_set.append(newpath)



doc = DocxTemplate("template.docx")
context = {
   'myimage' : InlineImage(doc,pic_set[0] ,width=Mm(100), height=Mm(50)),
   'myimage1' : InlineImage(doc,pic_set[1],width=Mm(100), height=Mm(50)),
   'myimage2' : InlineImage(doc,pic_set[2],width=Mm(100), height=Mm(50)),
   'myimage3' : InlineImage(doc,pic_set[3],width=Mm(200), height=Mm(150)),
   'myimage4' : InlineImage(doc,pic_set[4],width=Mm(200), height=Mm(150)),
   'myimage5' : InlineImage(doc,pic_set[5],width=Mm(200), height=Mm(150)),
   'myimage6' : InlineImage(doc,pic_set[6],width=Mm(200), height=Mm(150)),
   'myimage7' : InlineImage(doc,pic_set[7],width=Mm(200), height=Mm(150)),
   'myimage8' : InlineImage(doc,pic_set[8],width=Mm(200), height=Mm(150)),
   'myimage9' : InlineImage(doc,pic_set[8],width=Mm(200), height=Mm(150)),

    }



jinja_env = jinja2.Environment(autoescape=True)
doc.render(context,jinja_env)

doc.save("generated_doc.docx")

#document = Document()
#d.Add_Picture(document,"D:\\pic\\1.jpg")
#d.Add_Picture(document,"D:\\pic\\2.jpg")
#d.Save_Doc(document,"t100.docx")

#with open('D:\\pic\\3.jpg', 'r+b') as f:
#    with Image.open(f) as image:
#        cover = resizeimage.resize_thumbnail(image, [200, 150])
#        cover.save('test1.jpg', image.format)


#img = Image.open('D:\\pic\\3.jpg')
#new_img = img.resize((200,150),Image.LANCZOS)
#new_img.save('test_f.jpg')
