
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import pylab as plot

get_ipython().magic('pylab inline')


# In[76]:


df = pd.read_csv('Municipal_income.csv')
df.Income=pd.to_numeric(df.Income, )
df.drop('State_code',axis=1,inplace=True)
df.head(2)


# In[88]:


print("There are {} municipalities. \n".format(df.shape[0]))
      
print("Lowest income is {} with ${}/month. \n".format(
    df.Municipality.loc[df.Income.idxmin()], df.Income.min()))

print("Highest income is {} with ${}/month. \n".format(
    df.Municipality.loc[df.Income.idxmax()], df.Income.max()))

print("Mean monthly household income is ${:.2f} with standard deviation ${:.2f}. \n".format(
    df.Income.mean(),df.Income.std()))


# In[53]:


plt.figure(figsize = [6,6])
plt.hist(df.Income,bins=100)
plt.xlabel()
plt.title("Histogram of income in Mexico's municipalities");

