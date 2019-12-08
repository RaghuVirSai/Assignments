#!/usr/bin/env python
# coding: utf-8

# # Assignment1
# 

# Task1

# T1.2. Install Jupyter notebook and run the first program and share the screenshot of the output.

# In[1]:


584*54


# T.1.2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[2]:


nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))


# T 1.3. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[3]:


fname = input("firstname :  ")
lname = input("lastname  :  ")
print  (lname + " " + fname)


# T 1.4 Write a Python program to find the volume of a sphere with diameter 12 cm. 
# Formula: V=4/3 * π * r 3

# In[4]:


import math 
pi =math.pi


# In[5]:


pi = 3.1415926535897931
r= 12.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# # Task 2

# T 2.1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

# In[6]:


n = input('Enter numbers with separated comma:')
num=[]
for i in n.split():
    num.append(i)
    print(num)


# T.2.2 Create the below pattern using nested for loop in Python. 
# ** * * * * * * * * * * * * * * * * * * * * * * *
# 

# In[23]:



n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
    
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# T 2.3. Write a Python program to reverse a word after accepting the input from the user. 
# Sample Output: Input word:
# AcadGild Output: dilGdacA

# In[24]:


word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


# T 2.4 Write a Python Program to print the given string in the format specified in the sample output.
# 

# In[30]:


print("WE, THE PEOPLE OF INDIA, \n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC, \n\t\tand to secure to all its citizens.") 


# In[ ]:




