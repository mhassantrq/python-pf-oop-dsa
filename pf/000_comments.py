"""
Comments are lines of codes that are not executed by the language translator, compiler, interpreter etc.

These comments are used to explain codes, provide documentations or useful explanations.

We'll use comments to explain different concepts in going forward.

There are two types of comments in python. Basically theres just one type, the single line comment. But a way out using string
declaration, we can write multi line comments as well.
"""


#   single line comments start with a hash symbol as at the start of this line
#   you can have multi line comments
#   via using the single line comment method
#   however, its repetitive writing the same hash symbol again and again
#   hence, below is the method for multi line comment.


"""
Multi line comments are enclosed with three quotation marks as around this comment.

As stated above that python typically has single line comment, this multi line comment is basically a string value without
assigning it to a variable.

However, this multiline comment can be assigned to a variable and used as well unlike single line comments.
lets see below.
"""



var = """ this is multiline comment """

print(var)


#   look at the type of this multi line comment
#   this will print that the multi line comment is of class <str>, a string.
print(type(var))
