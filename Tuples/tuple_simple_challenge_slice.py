# Write the function to slice the tuple between the given start (inclusive)
# and end (exclusive) indexes, and join the resulting range of values as a comma delimited string.
#
# For example,
# tuple_slice(1, 4, (76, 34, 13, 64, 12)) should return "34,13,64".

def slice_tuple(start, stop, values):
    string_tuple = values[start:stop]
    string_comma_separated = '"'
    for value in string_tuple:
        string_comma_separated += str(value) + ','
    string_comma_separated = string_comma_separated[:-1]
    string_comma_separated += '"'
    print(string_comma_separated)



slice_tuple(1,4, (76, 34, 13, 64, 12))
slice_tuple(4,11, (1, 3, 13, 64, 12,67,89,89,34,'mystring1','abc','zzz', 999))

