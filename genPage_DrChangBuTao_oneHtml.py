# -*- coding:utf-8 -*-   

import sys
import os
import pickle
import re

#===  class define ...

class argListOut:
 
   def __init__(self,argList):
     self.argList = argList
     self.argStr = ""


   def ListOut(self):
     for value in self.argList:
         self.argStr = self.argStr+" "+value
     print(self.argStr) 

#===  main program start ...

if len(sys.argv) != 2:
   print "The line option is not assigned correctly : ",
   argList = (sys.argv) 
   argListOutInst = argListOut(argList)
   argListOutInst.ListOut()
   print "EXIT "
   exit()
else :
   argList = (sys.argv) 
   argListOutInst = argListOut(argList)
   argListOutInst.ListOut()

#=== Input File handling area ...

fileNow = open(argList[1], 'r')
#print fileNow.read()
listNow = fileNow.readlines()
fileNow.close()

#=== Output File handling area ...

#new0_file = open("page_DrWangWenYuan_balance.html.pre", "w")
inputFn = argList[1].replace("txt", "html")
new_file = open(inputFn, "w")

htmlHeadTxt = "<!DOCTYPE html>\n"
htmlHeadTxt += "<html>\n"
htmlHeadTxt += "<head>\n"
htmlHeadTxt += "<meta name=\"robots\" content=\"noindex\">\n"
htmlHeadTxt += "<meta name=\"googlebot\" content=\"noindex\">\n"
htmlHeadTxt += "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
htmlHeadTxt += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
#htmlHeadTxt += "<link rel=\"stylesheet\" href=\"https://www.w3schools.com/lib/w3.css\">"
htmlHeadTxt += "<style>p.myWrap {width: 30em;    word-wrap: break-word;}</style>\n"
htmlHeadTxt += "</head>\n"
htmlHeadTxt += "<body>\n"
#htmlHeadTxt += "<pre style=\"color: rgb(0, 0, 0); word-wrap: break-word; white-space: pre-wrap;\">\n"
htmlHeadTxt += "<p style=\"margin: 0px; font-size: 11px; font-family: Menlo; text-align: center;\">\n"
#htmlHeadTxt += "  <span style=\"font-size:24px;\"><strong>Balance Acupuncture of Dr Wang Wen-Yuan</strong></span></p>\n"
htmlHeadTxt += "<a name=\"fn_home\"></a>"
#htmlHeadTxt += "<img src=\"DrWangWenYan_balance_title.gif\">"
htmlHeadTxt += "<div class=\"w3-row-padding\">"
htmlHeadTxt += "<div class=\"w3-third\">"
htmlHeadTxt += "<p class=\"myWrap\"> "
#htmlHeadTxt += "<p style=\"color: rgb(0, 0, 0); width: 21em; word-wrap: break-word;  white-space: pre-wrap;\">\n"
#htmlHeadTxt += "<pre style=\"noWrap\">\n"



htmlTailTxt = "\n\n</p>\n</body>\n</html>\n"
#htmlTailTxt = "\n\n</body>\n</html>\n"

new_file.write(htmlHeadTxt)

cateQ = []
cateLinkQ = []
descQ = []

pn = 0
catNum = 0
l2_start = 0
l3_start = 0
l4_start = 0
l5_start = 0


for item in listNow:
    regex1 = r"^(\d+)\s+(.*)"
    regex2 = r"^(\d+\.\d+)\s+(.*)"
    regex3 = r"^(\d+\.\d+\.\d+)\s+(.*)"
    regex4 = r"^(\d+\.\d+\.\d+\.\d+)\s+(.*)"
    regex5 = r"^(\d+\.\d+\.\d+\.\d+\.\d+)\s+(.*)"
    if (re.findall(regex1, item.strip())):
        match1 = re.search(regex1, item)
        #print match.group(2)
        #print match.group(3)
        #new0_file.write(u"<a name=\""+str(pn)+"\">")
        descQ.append("<br><br><a href=\"#fn_home\"><img src=\"icon_home2_s.gif\" /></a>")
        descQ.append("<a name=\""+match1.group(1)+"\"></a>")
        descQ.append("<div style=\"color:red; font-size:45px;\">"+match1.group(2)+"</div>")
        pn += 1
        cateQ.append("<p style=\"color:#ff5555;\"><h3>"+item+"</h3></p>")
        cateLinkQ.append(match1.group(1))
        l2_start = 0
        l3_start = 0
        l4_start = 0
        l5_start = 0
    elif (re.findall(regex2, item.strip())):
        match2 = re.search(regex2, item)
        descQ.append("<a name=\""+match2.group(1)+"\"></a>")
        descQ.append("<div style=\"font-size:24px; color:#0000FF; margin-left: 40px;\"><li>"+match2.group(2)+"</li></div>")
        #cateQ.append(item)
        #cateLinkQ.append(match2.group(1))
        l2_start = 1
        l3_start = 0
        l4_start = 0
        l5_start = 0
    elif (re.findall(regex3, item.strip())):
        match3 = re.search(regex3, item)
        descQ.append("<div style=\"font-size:18px;margin-left: 60px;\"><li>"+match3.group(2)+"</li></div>")
        #cateQ.append(item)
        l3_start = 1
        l4_start = 0
        l5_start = 0
    elif (re.findall(regex4, item.strip())):
        match4 = re.search(regex4, item)
        descQ.append("<div style=\"font-size:16px; margin-left: 80px;\"><li>"+match4.group(2)+"</li></div>")
        #cateQ.append(item)
        l4_start = 1
        l5_start = 0
    elif (re.findall(regex5, item.strip())):
        match5 = re.search(regex5, item)
        descQ.append("<div style=\"font-size:14px; margin-left: 90px;\"><li>"+match5.group(2)+"</li></div>")
        #cateQ.append(item)
        l5_start = 1

#new_file.write(" <table width=\"100%\" border=\"1\" cellspacing=\"4\" cellpadding=\"1\">\n")
new_file.write(" <table width\"80\" border=\"1\" cellspacing=\"4\" cellpadding=\"1\" >\n")
for i, item in enumerate(cateQ):
    new_file.write("<tr><td><a href=\"#"+cateLinkQ[i]+"\">"+item+"</a></td></tr>")
new_file.write(" </table>\n")    

for item in descQ:
    new_file.write(item+"\n")



new_file.write(htmlTailTxt)

new_file.close

exit()

fileFinal = open("page_DrWangWenYuan_balance.html.pre", 'r')
listFinal = fileFinal.readlines()
fileFinal.close()

#<a href="#fn_home">

kon = 0

new_file.write("<h1><b>平衡針灸</b></h1>\n")
new_file.write("<table align=\"left\" border=\"1\" width=\"800\" height = \"40\"cellpadding=\"1\" cellspacing=\"1\">\n")
new_file.write("<tr><td bgcolor=\"#ccffcc\">各種病痛分類</td></tr>")
for i, itemC in enumerate(cateQ):
    print i, itemC
    new_file.write("<tr><td><a href=\"#cate_"+str(i)+"\">"+itemC+"</a></td></tr>")
new_file.write("</table>")
new_file.write("<p>&nbsp;</p>")
new_file.write("<p>&nbsp;</p>  </p>")

for itemF in listFinal:
    for strNow in acpuQ:
        if "a name" in itemF:
           kon += 1
        elif strNow in itemF:
           if "<br>" in itemF:
               kon += 1
           else:
               newStr =  "<a href=\"#"+strNow+"\">"+strNow+"</a>"
               itemF = itemF.replace(strNow, newStr)
    new_file.write(itemF)








#<tr><td bgcolor="yellow" colspan="2">﻿(1XXX)：                       </td> </tr>
