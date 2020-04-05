# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:21:54 2020

@author: SauravRawat
"""

from logpy import Relation,facts,run,fact
parent=Relation()
father=Relation()
mother=Relation()

#facts(parent,('Father','Child'),('Mother','Child'),('Vineeta','Amit'),('Vineeta','Krishna'))
facts(father,('Father','Child'),('Rohit','Gaurav'),('Abhishek','Vikram'),('Grandfather','Father'))
facts(mother,('Mother','Child'),('Vineeta','Amit'),('Vineeta','Krishna'))

def parent(x, y):
    return conde([father(x, y)], [mother(x, y)])

def grandfather(x, z):
    y = var()
    return conde((father(x, y), father(y, z)))

def sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

def uncle(x, y):
    temp = var()
    return conde(sibling(x,y),father(temp, x) ,grandfather(temp, y))

#facts(parent,('Father','Child'),('Mother','Child'),('Grandfather','Father'))
#print("Parent of Child are :",run(2, x, parent(x, 'Child')))  # two x such that x is a parent of Child
#print("Child of Father is :",run(1,x,parent('Father',x)))# one x such that Father is a parent of x

print("\n======================================================")
print("\n\t==========Menu==========\n")
print(" Enter the no of the relation you want to find")
print("""
      1.Child
      2.Father 
      3.Mother  
      4.Parent 
      5.Grandfather 
      6.Sibling 
      7.Uncle""")
n=int(input(" Enter the no of the relation you want to find :"))
if (n==1):
    s=input("You want to find the child .Enter the name of parent :\t")
    print("Child of "+s+" is : ",run(1,x,parent(s,x)))
if(n==2):
    s=input("You want to find the Father .Enter the name of Child:\t")
    print("Father of "+s+" is : ",run(1,x,father(x,s)))
if(n==3):
    s=input("You want to find the Mother .Enter the name of Child:\t")
    print("Mother of "+s+" is : ",run(1,x,mother(x,s)))
if(n==4):
    s=input("You want to find the Parent of the Child .Enter the name of Child:\t")
    print("Parents of "+s+" are : ",run(2,x,parent(x,s)))
    #print(run(2,x,parent(x,'Child')))
if (n==5):
    s=input("You want to find the grandparent .Enter the name of grandson to find his grandfather's name :  ")
    print("Grandfather of "+s+" is :",run(1, x, grandfather(x,s)))
if (n==6):
    s=input("You want to find the sibling .Enter the name of one of the sibling :  ")
    print("Sibling of "+s+" is :",run(0,x,sibling(x,s)))
    #print("",run(0,x,sibling(x,'Krishna')))
if(n==7):
    s=input("You want to find the uncle.Enter the name of child whose uncle's name you wanna find :")
    print("Uncle of "+s+" is : ",run(1,x,uncle(x,s)))
else:
    print("\n======================================================")
    print("\n  Enter the valid no of the relation from the above list")
    print("  Try again Later")
    print("\n======================================================")
    
