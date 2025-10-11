"""
built in data structure dict

these include key value pairs
these are unordered
their values can be easily changed 
"""

var_dict = {
    'chemistry': 55,
    'physics': 65,
    'maths': 75,
}

print(var_dict)


#   for above, key is subject and value is their respective marks

#   access using key 
print(var_dict['maths'])


#   add new key and value
var_dict['biology'] = 71
print(var_dict)