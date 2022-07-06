#! /bin/python3

# global nametable
names = {
	"true": True,
	"false": False
}

# set (or create new) name
def setname(name, value):
	names[name] = value
	
# get value or None
def getname(name):
	if name in names:
		return names[name]
	else:
		return None
		

