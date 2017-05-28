
# coding: utf-8

# 1. use reg expressions to just get the nums - capture groups. specificying character ranges. char class for white space. sometimes no num just a period
# 2. find a way to parse thru nums. find new and old vals.
# 3. find way deal w multi old vals
# 4. print things that dont match to inspect

# In[19]:

infile = [
'replace rocc60 = 41 if rocc70 == 103',
'hello ',
'replace rocc60 = 42 if rocc70 == 112',
'',
'replace rocc60 = 43 if rocc70 == 113',
'',
'replace rocc60 = 45 if rocc70 == 110',
'',
'replace rocc60 = 50 if rocc70 == 114',
'',
'replace rocc60 = 52 if rocc70 == 134',
'',
'replace rocc60 = 53 if rocc70 == 120 | rocc70 ==  121 | rocc70 == 122 | rocc70 ==  125 | rocc70 ==  126 ',
'',
'replace rocc60 = 54 if rocc70 == 115 | rocc70 ==  130 | rocc70 ==  131 | rocc70 ==  132 | rocc70 ==  133',
'',
'replace rocc60 = 60 if rocc70 == 135 | rocc70 ==  140',
'',
'replace rocc60 = 70 if rocc70 == 182',

]


# In[51]:

import re
import pandas as pd

pat = re.compile(r"\s([0-9.]+)")

mappings = [] #list of tuples of whole content in file
#mappings.append((new_val,(old_vals), (firstnum, secondnums), (fistnum, secondnums))

#with open("name.txt") as infile:
for line in infile:
    
    if line.startswith("replace rocc"):
        list_of_all_nums = pat.findall(line) # gets all numbers
        new_val = list_of_all_nums[0] # new number
        #old_vals = [] # list of all or the one old values 
        
        for num in list_of_all_nums[1:]:
            key_val_pair = (num, new_val) ## 
            mappings.append(key_val_pair)
            
    else:
        if line:
            print(line)
        
# make a pandas data frame
df = pd.DataFrame(data = mappings, columns=['old val', 'new val' ])
df


# In[ ]:
#%%
print('hello')

#%%



# In[ ]:



