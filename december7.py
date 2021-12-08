#!/usr/bin/env python
# coding: utf-8

# In[2]:


# program to print sum of all numbers using map function

l=[2,5,8,6,9]
def square(n):
    return n**2
    


# In[3]:


list(map(square,l))


# In[7]:


# program to find the largest element in a list.
def larger(l,n):
    max=l[0]
    for i in range(0,n):
        if l[i]>max:
            max=l[i]
    return max
    


# In[8]:


l=[25,84,76,8,5,7,97]
n=len(l)
larger(l,n)


# In[28]:


# swaping of two numbers.
x=6
y=8
print('before swaping:')
print('x is {} and y is {}'.format(x,y))
temp=x
x=y
y=temp
print('after swaping')
print('x is {} and y is {}'.format(x,y))


# In[29]:


# swaping withou using third variable.
x=6
y=8
print('before swaping:')
print('x is {} and y is {}'.format(x,y))
x,y=y,x
print('after swaping')
print('x is {} and y is {}'.format(x,y))


# In[14]:


# program to swaping position of numbers in a list.
def swapposition(l,pos1,pos2):
    l[pos1],l[pos2]=l[pos2],l[pos1]
    return l


# In[15]:


swapposition([2,3,4,5,6],2,4)


# In[25]:


# inserting elements at a perticuler position.
def insertlist(l,p1,p2):
    first=l.pop(p1)
    second=l.pop(p2)
    l.insert(p1,4)
    l.insert(p2,8)
    return l


# In[26]:


insertlist([23,4,78,99,45,7,22,],2,4)


# In[ ]:




