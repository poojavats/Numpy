#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


a=[1,2,3,4,5]


# In[3]:


ar=np.array(a)


# In[4]:


type(ar)


# In[5]:


np.array(ar)


# In[6]:


np.array([[1,2],[4,5]])


# In[9]:


np.asarray(3)


# In[14]:


a=[2,3,4]


# In[15]:


np.asanyarray(a)


# In[18]:


b=np.matrix(a)


# In[19]:


b


# In[20]:


np.asanyarray(b)


# In[21]:


c=a


# In[22]:


c[0]=100


# In[23]:


c


# In[25]:


c[1]=200


# In[26]:


c


# In[27]:


d=np.copy(a)


# In[28]:


d


# In[29]:


a


# In[30]:


a[1]=400


# In[31]:


a


# In[32]:


d


# # From function is a Function which help to generate array

# In[33]:


np.fromfunction(lambda i,j:i==j,(3,3))


# In[34]:


np.fromfunction(lambda i,j:i*j,(3,3))


# In[35]:


iterable= (i*i for i in range(5))


# In[38]:


np.fromiter(iterable,float)


# In[40]:


np.fromstring('Hello I am Pooja',sep='')


# In[41]:


np.fromstring('4,5',sep=',')


# In[43]:


#Numpy Data points
l=[2,3,4,5]


# In[44]:


ar=np.array(l)


# In[45]:


ar


# In[46]:


ar.ndim


# In[48]:


ar2=np.array([[1,2,3,4],[3,4,5,6]])


# In[49]:


ar2


# In[50]:


ar2.ndim


# In[51]:


ar.size


# In[52]:


ar2.size


# In[53]:


ar.shape


# In[54]:


ar2.shape


# In[55]:


ar.dtype


# In[56]:


ar2.dtype


# In[57]:


ar22=np.array([[1.4,22,23],[23,24,25]])


# In[58]:


ar22


# In[59]:


ar22.dtype


# In[60]:


range(5)


# In[61]:


list(range(5))


# In[62]:


np.arange(2.3,5.8)


# In[63]:


np.arange(2.3,5.6,3)


# In[64]:


list(np.arange(2.3,5.6,3))


# In[66]:


np.linspace(1,5,10)


# In[67]:


np.zeros(5)


# In[68]:


np.zeros((3,4))


# In[70]:


np.zeros((3,4,2))


# In[71]:


np.ones(4)


# In[72]:


np.ones((2,3))


# In[74]:


on=np.ones((2,3,2))


# In[75]:


on+5


# In[76]:


on*6


# In[79]:


np.empty((3,4))


# In[81]:


#Identity Matrix
np.eye(4)


# In[87]:


np.linspace(2,4,20)


# In[89]:


np.logspace(2,5,10,base=2)


# # randn data Generate data where mean=0,STD=1 - Standard Normal Distribution

# In[91]:


arr=np.random.randn(3,4)


# In[92]:


import pandas as pd


# In[93]:


pd.DataFrame(arr)


# # Rand Fuction Genearte the data Randomaly

# In[94]:


np.random.rand(3,4)


# In[96]:


np.random.randint(1,110,(3,4))


# In[108]:


pd.DataFrame(np.random.randint(1,100,(30,40))).to_csv("test.csv")


# In[110]:


arr=np.random.rand(3,4)


# In[111]:


arr


# In[118]:


arr1=arr.reshape(6,-1)


# In[119]:


arr1


# In[120]:


arr1[0]


# In[121]:


arr[0][1]


# In[124]:


arr1[2:5,1]


# In[127]:


al=np.random.randint(1,100,(5,5))


# In[128]:


al


# In[133]:


al[al>50]


# In[140]:


al[2:5,[2,3,4]]


# In[141]:


array1=np.random.randint(1,3,(3,3))


# In[142]:


array1


# In[143]:


array2=np.random.randint(1,3,(3,3))


# In[144]:


array1+array2


# In[145]:


array1-array2


# In[146]:


array1/array2


# In[147]:


array1*array2


# In[148]:


array1@array2


# In[149]:


array1/0


# In[151]:


array1+100


# In[152]:


array1**2


# # Broadcasting

# In[156]:


arr=np.zeros((4,4))


# In[157]:


arr


# In[159]:


row=np.array([1,2,3,4])


# In[160]:


row


# In[161]:


arr+row


# In[164]:


row.T


# In[166]:


column=np.array([[1,2,3,4]])


# In[170]:


column.T+arr


# In[174]:


al=np.random.randint(1,4,(3,5))


# In[175]:


al


# In[176]:


np.sqrt(al)


# In[177]:


np.exp(al)


# In[180]:


np.log10(al)


# In[ ]:




