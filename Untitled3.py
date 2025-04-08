#!/usr/bin/env python
# coding: utf-8

# In[3]:


from scipy.stats import mannwhitneyu
group1 = [1,2,4,18,45,56,78,90]
group2 = [1,30,80,93,95,99,100]
statistic, p_value = mannwhitneyu(group1,group2)
print("mann-whitney u istatistiği:", statistic)
print("p değeri:" ,p_value)


# In[ ]:




