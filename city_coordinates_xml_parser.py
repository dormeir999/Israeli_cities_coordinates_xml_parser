# 
# Example file for parsing and processing XML
#
import xml.dom.minidom
import pandas as pd
from openpyxl import Workbook
import urllib.request
import os

def main():

  dir_path = os.path.dirname(os.path.realpath(__file__))

  url = 'https://www.mapi.gov.il/ProfessionalInfo/Documents/dataGov/CITY.xml'
  urllib.request.urlretrieve(url, "CITY.xml")

  # use the parse() function to load and parse an XML file
  doc = xml.dom.minidom.parse("CITY.xml")


  # create the cities dataframe
  df = pd.DataFrame(columns=['City', 'X coordinate', 'Y coordinate'])

  # get a list of city records
  Records = doc.getElementsByTagName("Records")[0].childNodes
  #print("There are %d records: " % Records.length)
  #i = 0
  for record in Records:
    city_name = record.childNodes[0].childNodes[4].childNodes[0].nodeValue
    # print(record.childNodes[0].childNodes[1].childNodes[0].nodeName)
    city_x_coordinate = record.childNodes[0].childNodes[1].childNodes[0].childNodes[0].nodeValue
    # print(record.childNodes[0].childNodes[1].childNodes[1].nodeName)
    city_y_coordinate = record.childNodes[0].childNodes[1].childNodes[1].childNodes[0].nodeValue
    df = df.append({'City':city_name, 'X coordinate':city_x_coordinate, 'Y coordinate':city_y_coordinate},ignore_index=True)
    #df.loc[i] = city_name,city_x_coordinate,city_y_coordinate
    #df.iloc[i,1] = city_x_coordinate
    #df.iloc[i,2] = city_y_coordinate
    #i+=1

  print(df)
  df.to_excel("Israel_cities_coordinates.xlsx",index=False)

if __name__ == "__main__":
  main();

