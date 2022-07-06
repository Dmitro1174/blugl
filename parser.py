#! /bin/python3

import utils

# constants
OPERATORS = "+-*/(),"

ATOM_NAME = 1
ATOM_CONST = 2
ATOM_OPER = 3

# parse text into atoms' array
def parse(text):
	res = []	# resulting array
	txtlen = len(text)
	pos = 0
	char = ''
	tmp = ''
	row = 0
	col = 1; # relative text position
	start_rol = 1; # token starting column
	
	while pos < txtlen:

		tmp = ''

		# get next char
		char = text[pos]
	
		# analize !!!
		if char in OPERATORS:
					
			res.append((ATOM_OPER, char, row, col))
				
			pos = pos + 1
			col = col + 1
			
		elif char == ';':	# comment to end of line - pass it
		
			#pos = pos + 1
			#col = col + 1
			
			while pos < txtlen:
			
				pos = pos + 1
				if pos >= txtlen: break
				
				char = text[pos]
				
				if char == "\n":
					col = 1
					row = row + 1
					break
				else:
					col = col + 1
				
		elif char == '"':	# quoted string
		
			tmp = char
			start_col = col
			
			while(pos < txtlen):
				
				pos = pos + 1
				
				if pos >= txtlen: break
				
				char = text[pos]
				
				if char == "\n":
					col = 1
					row = row + 1
				else: col = col + 1
				
				if char != '"':
					tmp = tmp + char
				else:
					tmp = tmp + '"'
					pos = pos + 1
					break
					
			if char != '"' or pos >= txtlen: 
				print ("unquoted string literal")
				break
			
			res.append((ATOM_CONST, tmp, row, start_col))
			
		elif char.isdigit():	# digit
		
			start_col = col
		
			while char.isdigit() or char == '.':
				
				tmp = tmp + char
				
				pos = pos + 1
				if pos >= txtlen: break
				
				col = col + 1
				
				char = text[pos]
			
			res.append((ATOM_CONST, tmp, row, start_col))
			
		elif char.isspace():	# whitespaces - pass 'em
			
			while char.isspace():
			
				if char == "\n":
					col = 1
					row = row + 1
				else:
					col = col + 1
				
				
				pos = pos + 1
				if pos >= txtlen: break
				
				char = text[pos]
				
		elif char.isalpha():	# identifier
		
			start_col = col
		
			while char.isalpha() or char.isdigit():
				tmp = tmp + char
				
				pos = pos + 1
				col = col + 1
				if pos >= txtlen: break
				
				char = text[pos]
				
			
			res.append((ATOM_NAME, tmp, row, start_col))
			
		else:
			print ("unexpected token `{}`".format(char))
			pos = pos + 1
	
	# return
	return res
# /parse()

# for debug: translate atom type to string repr
def atom_type_trans(atom_type):
	if atom_type == ATOM_CONST: return 'literal'
	elif atom_type == ATOM_OPER: return 'operator'
	else: return 'name/keyword'
	
