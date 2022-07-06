#! /bin/python3

# imports
import os
import sys

import utils
import parser
import engine
import names


version = "0.1";
date = "6/23/2022";



# globals
expressions = []	# expressions to evaluate

# interprete command line
if len(sys.argv) < 2:
	print ("usage: pl [quoted expression(s) or file name(s)]")
	exit(0)

for arg in sys.argv[1:]:
	if os.path.isfile(arg):	# filename passed
		try:
			code_file = open(arg, "r")
			code_text = code_file.read()
			code_file.close()
			expressions.append(code_text)
		except:
			print("cannot load file {0}".format(arg))
	else:
		expressions.append(arg)
		

for expr in expressions:
	
	ats = parser.parse(expr)
	
	for at in ats:
		(typ, at, row, col) = at
		print("[{0}:{1}] -> {2} ({3})".format(row, col, at, parser.atom_type_trans(typ)))

# normal exit
exit(0)
