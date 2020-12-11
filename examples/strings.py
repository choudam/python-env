# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:44:01 2020

@author: srinic
"""

def substring(s,f):
    for i in range(len(s)):
        if s[i] == f[0]:
            find=True
            for j in range(1,len(f)):
                if i+j > len(s) or s[i+j] != f[j]:
                    find=False
                    break
            if find == True:
                return i
    return -1


def substringlast(s,f):
    sl=len(s)
    fl=len(f)
    i=sl-1
    while (i>=fl):
        if s[i] == f[fl-1]:
        
            find=True
            for j in range(1,fl):
                if s[i-j] != f[fl-j-1]:
                    find=False
                    break
            if find == True:
                return i
        i-=1            
    return -1

x = substring("The rain in Spain", "in")

print(x)

x = substringlast("The rain in Spain", "int")

print(x)


x=input("Enter number")
xi= float(x)

print(xi*xi)


age=26

name =input("Enter your name: ")
try:
    age=int(input("Enter age: "))
except:
    print("Invalid age. assuming you are in 20's")
else:
    print("Thank you for letting me know your age")
        

txt="His name is {1}. {1} is {0} years old."
print(txt.format(age,name))