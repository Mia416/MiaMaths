from docx import *
from docx.shared import Pt
from CommonClass import M_Doc




document = Document()
d = M_Doc()
d.Add_Picture(document,"D:\\pic\\1.jpg")
d.Add_Picture(document,"D:\\pic\\2.jpg")
d.Save_Doc(document,"t100.docx")
