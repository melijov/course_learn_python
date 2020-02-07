#declare a variable
f=0
#print(f)

#re-declaring the variable
#f="abc"
#print(f)

#Error: variables of diff types cannot be combined. Python is a strongly typed language. This works in Javascript!!!
#print("this is a string "+str(123))

#Global vs Local Variables (inside a function) a local variable can be casted by using global
def someFunction():
  global f
  f="def"
  print(f)
  
someFunction()
print(f)

del f # undefine variables in real time
print(f)