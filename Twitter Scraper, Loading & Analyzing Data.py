
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import json      # library for working with JSON-formatted text strings
import pprint as pp    # library for cleanly printing Python data structures


# This is a basic test for https://github.com/taspinar/twitterscraper. Using the demo data looking at all tweets re. Trump.

# In[11]:


#this loads the data into json in the notebook

with open('cc_test.JSON') as f:
  data = json.load(f)

print(type(data))


# In[10]:


print(data[:500])


# In[15]:


pp.pprint(data)
