# #!/bin/python3

"""
a tuples is an immutable list (cannot be changed, only created and destroyed)
"""

myTuple = (1111, 2000, 3333)
print(myTuple)
print(myTuple[1])                               # select element inside tuple
#myTuple[1] = 2222                              # TypeError: 'tuple' object does not support item assignment

myTupleNew = (myTuple[0], 2222, myTuple[2])     # create new tuple 
print(myTupleNew)                               # 1111, 2222, 3333
del myTuple                                     # remove myTuple


"""
a dictionary is a key-value store
also known as 'dict' for short 
"""

dict = {'Name': 'Josh', 'Height': 6.0}
print(dict)                                     # {'Name': 'Josh', 'Height': 6.0}
print(dict['Height'])                           # 6.0
dict['Height'] = 5.11                           # update value 
print(dict['Height'])                           # {'Name': 'Josh', 'Height': 5.11}

del dict['Name']                                # delete a particular entry in the dictionary
print(dict)                                     # {'Height': 5.11}
dict.clear()                                    # clear the dictionary object
print(dict)                                     # {}
del dict                                        # delete dict
print(dict)                                     # <class 'dict'>

#dict['Height'] = 5.11                          # TypeError: 'type' object does not support item assignment
