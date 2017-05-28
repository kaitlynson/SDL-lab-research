
class Recoder(object):
    
    def __init__(self, dictionary):
        self.d = dictionary


    def recode (self, old_value, strict=False):
        
        if strict==True:
            return self.d[old_value]
        else:
            return self.d.get(old_value, old_value) # if val not there and on strict ret error
                                                    # if there on or off strict ret val.




# int_to_letter = Recoder({'a':1, 'b':2, 'c':3})
# print(int_to_letter.recode('d'))
# int_to_letter.recode('d', strict=True)


#csv file two cols old new val
# first code white space next code 
