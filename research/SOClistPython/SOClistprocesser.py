## Kaitlyn Son
## June 8 2016
## processing SOClist into smaller lists

def main():


    with open('SOClist.txt', 'r') as infile:
        soc_dict = {}
        contents = infile.readlines() #readlines returns all lines as a python list
        
        for line in contents: # iterates thru every element in list
            code = line[:8]
            occupation = line.strip()[8:]
            first_key = code[:2] # gets first two nums of line
            second_key = code[3]
            
            if not first_key in soc_dict:
                soc_dict[first_key] = {}
                
            if not second_key in soc_dict[first_key]:
                soc_dict[first_key][second_key] = []
            soc_dict[first_key][second_key].append((code, occupation))

            
main()


