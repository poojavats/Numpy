#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


arr=np.array([5,3,4,9,55,77,88])


# In[4]:


arr


# In[7]:


np.sort(arr)


# In[8]:


np.searchsorted(arr, 34)


# In[9]:


arr1=np.array([0,345,454,0,0,0,0,0,0,0])


# In[11]:


np.count_nonzero(arr1)


# In[12]:


arr


# In[13]:


arr>6


# In[14]:


np.where(arr>6)


# In[15]:


np.extract(arr>6,arr)


# In[16]:


#Numpy-Byte Swapping


# In[17]:


arr


# In[18]:


arr.byteswap()


# # Copies and Views

# In[19]:


a=np.copy(arr)


# In[20]:


a


# In[21]:


b=arr.view()


# In[22]:


b


# In[23]:


b[0]=94


# In[24]:


b


# In[25]:


arr


# In[26]:


a


# # Matrix Library

# In[27]:


import numpy.matlib as nm


# In[29]:


nm.zeros(5)


# In[30]:


np.zeros(5)


# In[31]:


nm.ones((3,4))


# In[32]:


np.eye(5)


# # Numpy-Linear Algebra

# In[37]:


arr1=np.random.randint([1,2],[3,4])


# In[38]:


arr2=np.random.randint([1,2],[3,4])


# In[39]:


np.dot(arr1,arr2)


# In[40]:


arr1@arr2


# In[ ]:




