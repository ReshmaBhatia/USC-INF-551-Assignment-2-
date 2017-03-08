import json
import math
import sys

def checkYear(ip):
    if (ip[0]=="2"):
      return True

def checkTerminal(ip):
    if (ip[0]=="t" or ip[0]=="T"):
        return True

def checkDA(ip):
    if (ip[0]=="a" or ip[0]=="A" or ip[0]=="D" or ip[0]=="d"):
        return True

def OrgTer(ip):
    if ip.capitalize()=="T1":
        return "Terminal 1"
    elif ip.capitalize()=="T2":
        return "Terminal 2"
    elif ip.capitalize()=="T3":
        return "Terminal 3"
    elif ip.capitalize()=="T4":
        return "Terminal 4"
    elif ip.capitalize()=="T5":
        return "Terminal 5"
    elif ip.capitalize()=="T6":
        return "Terminal 6"
    else:
        return "Tom Bradley International Terminal"

def OrgDA(ip):
    if ip.capitalize()=="Arrival":
        return "Arrival"
    else:
        return "Departure"


def working(l):
    minimum= min(l)
    maximum= max(l)
    l.sort()
    sortlength = len(l)
    check = (sortlength-1)//2
    med=0
    if (sortlength % 2):
        med= round(l[check],1)
    else:
        med= round((l[check]+l[check+1])/2.0,2)
    sum1 = sum(l)
    length=len(l)
    avg= float(sum1)/length
    diff=[i - avg for i in l]
    square_diff=[j**2 for j in diff]
    sum2=sum(square_diff)
    variance=float(sum2)/length
    stand_dev=math.sqrt(variance)
    print minimum,",",maximum,",",round(med,1),",",round(avg,2),",",round(stand_dev,2)


input = json.loads(open(sys.argv[1]).read())


data=input['data']

a=sys.argv[2]
b=a.split(" ")
#print a
YearList = set([])
TerminalList = set([])
DAList = set([])
for element in b:
    if checkYear(element):
        YearList.add(element)
    elif checkTerminal(element):
        TerminalList.add(OrgTer(element))
    else:
        DAList.add(OrgDA(element))

if not YearList:
    YearList.add("2006")
    YearList.add("2007")
    YearList.add("2008")
    YearList.add("2009")
    YearList.add("2010")
    YearList.add("2011")
    YearList.add("2012")
    YearList.add("2013")
    YearList.add("2014")
    YearList.add("2015")
    YearList.add("2016")

if not TerminalList:
    TerminalList.add("Terminal 1")
    TerminalList.add("Terminal 2")
    TerminalList.add("Terminal 3")
    TerminalList.add("Terminal 4")
    TerminalList.add("Terminal 5")
    TerminalList.add("Terminal 6")
    TerminalList.add("Tom Bradley International Terminal")

if not DAList:
    DAList.add("Departure")
    DAList.add("Arrival")


FinalNumList=[]
for row in data:
    if (row[9][0:4] in YearList and row[10] in TerminalList and row[11] in DAList):
        FinalNumList.append(int(row[13]))
        #print FinalNumList

working(FinalNumList)

