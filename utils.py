#! /bin/python3


# prints list in a more readable way
nesting = 0;

def list_pretty_view(arg):

	global nesting

	nesting = nesting + 1
	padding = '-' * nesting;
	
	
	
	if type(arg) is list:	# list go recursively
		
		print (padding, "[")
		
		for ll in arg:
			list_pretty_view(ll)
			
		print (padding, "]")
	else:	# leaf not list
		padding = "-" * (nesting + 1)
		print("%s%s" %(padding, arg))

	
	nesting = nesting - 1
	
# /def list_pretty_view

# check whether char is in string
def isin(char, string):
	return string.find(char) != -1	
	
	
