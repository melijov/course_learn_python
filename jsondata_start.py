# Print only the events wher at least one person reported feeling something
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import json

def printResults(data):
  #Use json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  #now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
    print(theJSON["metadata"]["title"])
  
  #output number of events
  count =theJSON["metadata"]["count"]
  print(str(count) +  " events recorded")
  
  #for each event, print the place where it occurred
  for i in theJSON["features"]:
    print(i["properties"]["place"])
  print("------------------\n")
  
  #print the events that only have a magnitude greather than f4
  for i in theJSON["features"]:
    if i["properties"]["mag"]>=4.0:
	  print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
  print("------------------\n")
   
  #print only the events where at least 1 person reported feeling something
  print("Events that were felt:")
  for i in theJSON["features"]:
    feltReports= i["properties"]["felt"]
    if feltReports !=None:
	  if feltReports >0:
	    print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times")
  print("------------------\n")
	
def main():
  print("jsondata_start.py.main")
  #This feed lists all earthquakes for the last day larger that Mag 2.5
  urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
 
  #Open the URL and read the data
  webUrl = urlopen(urlData)
  print("result code: " + str(webUrl.getcode()))
  if (webUrl.getcode()==200):
    data = webUrl.read()
    printResults(data)
  else:
    print("Received error, cannot parse results")

if __name__ == '__main__':
  main()