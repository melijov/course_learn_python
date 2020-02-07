#Example file for retrieving data from the internet
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def main():
  print("inetdata_start.py.main")
  webUrl = urlopen("http://www.google.com")
  print("result code: " + str(webUrl.getcode()))
  data = webUrl.read()
  print(data)
  
if __name__=='__main__':
  main()