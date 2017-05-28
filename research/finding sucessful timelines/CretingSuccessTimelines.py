# read in list of sorted user ids
# store them into a set - a python regular set
# > if x in set ret t/f 
# get user id of all english speakers and see if user is in set. if in set read whole line into new file .json file
# read up on json file

# glob.glob give u a list of all files


import glob
import bz2
import os

success_set = set()
with open("/Volumes/Starbuck/class/tweet_text_processing/home_value_success_users.txt") as uidfile:
	for line in uidfile:
		success_set.add(line.strip())

#  this does one file 
# in_file_name = "/Volumes/Starbuck/class/twitter_data/modified_essential/US_GB_CA_AU_NZ_SG/part-00000.bz2"
# out_file_name = "/Volumes/Starbuck/class/twitter_data/success_timelines.json"
# 
# j=0 
# 
# with bz2.BZ2File(in_file_name) as infile, bz2.BZ2File(out_file_name,'w') as outfile:
# 	for i,line in enumerate(infile):
# 		if i%1000 == 0:
# 			print ("finished {} lines".format(i))
# 		id_num = line.split("\t")[0][1:-1]
# 		if id_num in success_set:
# 			j=j+1
# 			outfile.write(line)
# 			print("found {} successful ids".format(j))
# 


#in_file_pat = "/Volumes/Starbuck/class/twitter_data/modified_essential/US_GB_CA_AU_NZ_SG/part-*.bz2"
in_file_pat = "/Volumes/Starbuck/class/twitter_data/modified_essential/US_GB_CA_AU_NZ_SG/part-0000*.bz2"
j=0

out_file_path = "/Volumes/Starbuck/class/twitter_data/filtered_timelines"


for in_file_name in glob.glob(in_file_pat):
    file_name = os.path.basename(in_file_name)
    out_file_name = os.path.join(out_file_path,"success_"+file_name)
    
    with bz2.open(in_file_name, mode="rt", encoding="UTF-8") as infile, bz2.open(out_file_name,mode='wt',  encoding="UTF-8") as outfile:
        for i,line in enumerate(infile):
            if i%1000 == 0:
                print ("finished {} lines in {} file ".format(i,file_name))
            id_num = line.split("\t")[0][1:-1]
            if id_num in success_set:
                j=j+1
                outfile.write(line)
                print("found {} successful ids".format(j))

        

