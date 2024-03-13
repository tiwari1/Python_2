#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Membership operator
1. in 
2. not in


# In[1]:


# in
l=[1,2,3,4,5]
print(2 in l)


# In[2]:


l=[1,3,4,5]
print(2 in l)


# In[3]:


# not in
l=[1,2,3,4,5]
print(2 not in l)


# In[4]:


# not in
l=[1,3,4,5]
print(2 not in l)


# In[ ]:


# Identity operator
1. is
2. is not


# In[5]:


print(7 is 7) #Did you mean '=='?


# In[6]:


print( 7 is not 7 )


# In[ ]:


#bitwise operator


# In[ ]:


# String
# 'ejbfd453.345',"345.345","""4354.4545"""
# immutable
1. len()    # 1 onwards
2. Indexing # 0 onwards [] -1
3. Slicing  [start:stop:step] # 1--> 0,2-->1,3-->2,5-->4,9-->8


# In[7]:


x='python'
print(len(x))


# In[8]:


x='python .?'
print(len(x))


# In[9]:


x='python'
# expected output: t
print(x[2])


# In[10]:


x='python'
# expected output: o
print(x[4])


# In[11]:


x='python'
# expected output: p
print(x[0])


# In[12]:


x='python'
# expected output: n
print(x[5])


# In[13]:


x='python'
# expected output: o
print(x[-2])


# In[14]:


x='python'
# expected output: p
print(x[-6])


# In[15]:


x='python'
# expected output: py
print(x[0]+x[1])


# In[16]:


x='python'
# expected output: thon
print(x[2:])


# In[17]:


x='python'
# expected output: thon
print(x[:])


# In[18]:


x='python'
# expected output: ytho
print(x[1:5]) 


# In[19]:


x='python'
# expected output: pyt
print(x[0:3])


# In[20]:


x='python'
# expected output: yth
print(x[1:4])


# In[21]:


# Step
x='python'
# expected output: thon
print(x[::1])


# In[22]:


x='python'
# expected output: pto
print(x[::2])


# In[23]:


x='python'
# expected output: ph
print(x[::3])


# In[24]:


x='python'
# expected output: po
print(x[::4])


# In[25]:


# Negative indexing
x='python'
# expected output: th
print(x[-4:-2])


# In[26]:


x='python'
# expected output: pyt
print(x[-6:-3])


# In[27]:


# step negative reverse
x='python'
# expected output: 
print(x[::-1])


# In[28]:


# step negative reverse
x='python'
# expected output: 
print(x[::-2])


# In[29]:


# step negative reverse
x='python'
# expected output:nt 
print(x[::-3])


# In[ ]:


# String function
1. len()
2. upper()
3. lower()
4. capitalize()
5. title()
6. replace()
7. isalpha()
8. isdigit()
9. isnumeric()
10. isalnum()
11. count()
12. find()
13. rfind()
14. index()
15. rindex()
16. startswith()
17. endswith()
18. center()
19. split()
20. join()
21. del()
22. abs()
23. strip()
24. swapcase()
25. isupper()
26. islower()


# In[30]:


# upper() #it takes no arguments
x='python'
print(x.upper()) #str.upper() takes no arguments (1 given)


# In[31]:


# upper() #it takes no arguments
x='PYTHON'
print(x.upper())


# In[32]:


# lower() # it takes no arguments
x='PYTHON'
print(x.lower())


# In[33]:


# replace() # it takes 3 arguments
x='Initial interest'
print(x.replace('i','-'))


# In[34]:


# replace() # it takes 3 arguments
x='Initial interest'
print(x.replace('i','-',2))


# In[ ]:





# In[ ]:




