#Conditional statements

def main():
  x,y = 10,100
  #Python does not have a switch case block
  #conditional flows if, elif, else
  if (x<y):
    st ="x is less than y"
  elif( x == y ):
    st ="x is equal to y"
  else:
    st ="x is greater than y"
  print st
  
  #conditional statements let you use "a if c else b": concise statement
  st = "x is less than y" if (x<y) else "x is greater than or the sames as y"
  print st
if __name__=="__main__":
  main()