"""
Final Project for Algorithms class, Supervide by Dr. Jonathan Lee.
The project is sorting data sets of companies to get the highest
volume in stock market each day of the selected month by the user.
"""
from SortingFunctions import *
import matplotlib.pyplot as plt

#number of companies input with type check
def number_of_companies_():
    while True:
        try:
            number_of_companies = int(input('Please type the number of companies'))
            break
        except:
            print("--wrong input type--")
    return str(number_of_companies)
#end def number_of_companies_

#month choise, type check
def month_():
    while True:
        try:
            month = int(input('Please choose a month from 1 to 8'))
            break
        except:
            print("--wrong input type--")
    return str(month)
#end def month


#menu of companies
def menu():
    print(' Amazon \n Apple \n Tesla \n Google')
#end def menu

#take input from user and make a list of inputs
def inputt(tt):
    t=int(tt)
    listOfInput=[]
    for i in range(t):
        while True:
         try:
          i=input('Enter company name')+'.txt'
          open(i)
          listOfInput.append(i)
          break
         except FileNotFoundError:
             print('Wrong choice, please choose from the list')
    return listOfInput

#read each file data, with name, and the chosen month by user
def ReadFile(name,month):

  with open(name) as f:
    lines = f.readlines()
  label=name.split('.')[0]
  Data_of_selected_month=[]
  for line in lines:
    if (line[0]==month):
      Data_of_selected_month.append(line.split())

    dates = []
    for i in range(len(Data_of_selected_month)):
        dates.append(Data_of_selected_month[i][0])

    FinalData=[]
    for i in range(len(Data_of_selected_month)):
        FinalData.append([int(Data_of_selected_month[i][1]),label])
 #get the data to be sroted and the dates column
  return FinalData,dates
#end def ReadFile

#use the output of ReadFile to get the total list
def Data(aaa,month,v):
    all = []
    try:
        a = ReadFile(aaa[0], month)
        b = ReadFile(aaa[1], month)
        c = ReadFile(aaa[2], month)
        d = ReadFile(aaa[3], month)
    except IndexError:
        pass
    gg = int(v)
    for i in range(len(a[0])):
        all.append(a[0][i])
        if (gg > 1):
            all.append(b[0][i])
        if (gg > 2):
            all.append(c[0][i])
        if (gg > 3):
            all.append(d[0][i])
    return all,a[1]
#end def data

#the function to take the list and sort it
def sorting(sort,l,n):
    #list needed after read, number of comapnies, len of the list
    Sortedlist=[]
    p=0
    for k in range(n):
     try:
      dd=sort[p:p+l]
      yy=dd[:][:]
      quickSort(yy,0,l-1)
      dd.clear()
      Sortedlist.append(yy[l-1])
      yy.clear()
      p=p+l
     except IndexError:
         pass
    #return the sorted list
    return Sortedlist
#end def sorting

#arrange the list befor plot
def arrange(sort):
    v = []
    for i in range(len(sort)):
        v.append(str(sort[i]))
    return v
#end def arrange

#graph function depends on user choise
def graph(input_,x,y):
    if input_=="bar":
     plt.bar(x, y, align='edge', width=.1)
     plt.tick_params(labelsize=7)
     return plt.show()
    if input_=="scatter":
     plt.scatter(x, y, 50)
     plt.tick_params(labelsize=7)
     return plt.show()
#end def graph



#def main
def main():

  number_of_companies=number_of_companies_()
  month=month_()
  menu()
  list_inputs = inputt(number_of_companies)
  Final_list=Data(list_inputs,month,number_of_companies)
  Lengh=len(Final_list[1])
  sort=sorting(Final_list[0],int(number_of_companies),Lengh)
  result=arrange(sort)
  graph_type=input('Please choose the graph type: \n bar \n scatter')
  graph(graph_type,Final_list[1],result)
 #end def main

if __name__ == '__main__':
   while True:
    main()
    quit = input('Type Q to quit or press enter to continue')
    if quit == "Q":
        break



