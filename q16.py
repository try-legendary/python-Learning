#Write type_name(x) that returns type as string (e.g., "int")

def type_name(x):
	return type(x)
print(type_name(10))        # "int"
print(type_name(3.14))      # "float"
print(type_name("hello"))   # "str"
print(type_name([1, 2, 3])) # "list"