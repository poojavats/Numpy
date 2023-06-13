#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[38]:


arr=np.random.randint(1,10,(3,4))


# In[39]:


arr


# In[40]:


arr.T


# In[42]:


arr.reshape(6,2)


# In[47]:


arr.reshape(4,3)


# In[48]:


arr


# In[49]:


arr.flatten()


# In[50]:


arr1=np.array([1,2,3,3,4])


# In[51]:


arr1


# In[52]:


arr1.ndim


# In[54]:


np.expand_dims(arr1,axis=1)


# In[83]:


np.expand_dims(arr1,axis=0)


# In[84]:


arr


# In[85]:


np.squeeze(arr)


# In[87]:


data=np.array([[1],[2],[3]])


# In[88]:


np.squeeze(data)


# In[89]:


arr1


# In[90]:


np.repeat(arr1,3)


# In[92]:


np.roll(arr1,2)


# In[93]:


np.diag(arr1)


# # Binary operation

# In[95]:


arr1=np.random.randint(1,10,[3,4])


# In[96]:


arr2=np.random.randint(1,10,[3,4])


# In[97]:


arr1


# In[98]:


arr2


# In[99]:


arr1+arr2


# In[100]:


arr1*arr2


# In[101]:


arr1/arr2


# In[103]:


arr1-arr2


# In[104]:


arr1%arr2


# In[105]:


arr1**arr2


# In[106]:


arr1&arr2


# In[107]:


~arr1


# In[108]:


arr1


# In[109]:


arr1 |arr2


# In[110]:


arr1>arr2


# # String Function

# In[112]:


arr=np.array(["pooja","sharma"])


# In[113]:


arr


# In[115]:


np.char.upper(arr)


# In[116]:


np.char.title(arr)


# In[117]:


np.char.capitalize(arr)


# In[118]:


arr1


# In[120]:


np.sin(arr1)


# In[121]:


np.cos(arr1)


# In[122]:


np.tan(arr1)


# In[123]:


np.tanh(arr1)


# In[124]:


np.log10(arr1)


# In[125]:


np.exp(arr1)


# In[126]:


np.sqrt(arr1)


# In[128]:


np.power(arr1,2)


# In[129]:


np.mean(arr1)


# In[130]:


np.max(arr1)


# In[131]:


np.std(arr1)


# In[133]:


np.median(arr1)


# In[134]:


np.var(arr1)


# In[135]:


np.min(arr1)


# In[ ]:




