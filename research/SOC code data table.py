
# coding: utf-8

# In[51]:

import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt


with open('/Users/sports195admin/Desktop/rxch/SOClistPython/SOClist.txt', 'r') as infile:
    soc_dict = {}
    contents = infile.readlines() #readlines returns all lines as a python list

    for line in contents: # iterates thru every element in list
        code = line[:7]
        #print('"{}"'.format(code))
        occupation = line.strip()[8:]
        first_key = code[:2] # gets first two nums of line
        second_key = code[3]

        if not first_key in soc_dict:
            soc_dict[first_key] = {}

        if not second_key in soc_dict[first_key]:
            soc_dict[first_key][second_key] = {"label":None, "SOC":[]}
            
        if code[-3:] == "000":
           # print(occupation)
            soc_dict[first_key][second_key]["label"] = occupation
            
        else:
            soc_dict[first_key][second_key]["SOC"].append((code, occupation))
       # break
        
        
        
        


# In[52]:

"11-1000"[-3:]=="000"


# In[ ]:




# In[53]:

soc_dict["13"]


# In[62]:

results = []
for first_key in sorted(soc_dict.keys()):
    for second_key in sorted(soc_dict[first_key]):
        if second_key == "0":
            continue
        for occupation in sorted(soc_dict[first_key][second_key]["SOC"]):
            results.append((soc_dict[first_key]["0"]["label"], soc_dict[first_key][second_key]["label"], occupation[1]))
           # print (soc_dict[first_key]["0"]["label"], soc_dict[first_key][second_key]["label"], occupation[1])


# In[ ]:




# In[65]:

df = pd.DataFrame(data = results, columns=['Kind', 'Type of Job', 'Occupation']) ##change names
df


# In[ ]:



