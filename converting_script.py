import csv
import os

#asks user the name of file
userFile = input('Enter the name of the csv file: ')

#reads in the data of file
f = open(userFile)
csv_f = csv.reader(f)
next(csv_f, None)  # skip the headers

#reads it in again this time to count the rows in the file
with open(userFile,"r") as l:
    reader = csv.reader(l,delimiter = ",")
    data = list(reader)
    tot_row_count = len(data)

#opening text of the geojson
test = "{ \n\t\"type\": \"FeatureCollection\",\n\t\"features\": [\n\t"
cords_list = []

row_count = 0

#iterates through all the rows of the file
for row in csv_f:
    #increments what row currently on 
    row_count = row_count + 1
    #coordinates data is stored on column 11 (11-1 = 10, etc)
    number = row[0]
    city = row[1]
    county = row[2]
    fid = row[3]  
    geoid = row[4]
    ogc_fid = row [5]
    owner = row[6]
    parcelnumb = row[7]
    state = row[8]
    geo_type = row[9]
    coordinates = row[10]

    #if the row is not the last rown continue as normal
    if (row_count < tot_row_count - 1 ):
        cords_list.append("\t\t{\n\t\t\"type\": \"Feature\",\n\t\t\"geometry\": {\n\t\t\t\"type\": \""+str(geo_type)+"\",\n\t\t\t\"coordinates\": \n\t\t\t"+str(coordinates)+"\n\t\t\t\n\t\t},\n\t\t\"properties\": {\n\t\t\t\"city\": \""+str(city)+"\",\n\t\t\t"+"\"county\": \""+str(county)+"\",\n\t\t\t\"number\": \""+str(number)+"\",\n\t\t\t\"parcelnumb\": \""+ str(parcelnumb)+"\",\n\t\t\t\"geoid\": \""+ str(geoid)+"\",\n\t\t\t\"ogc fid\": \""+ str(ogc_fid)+"\",\n\t\t\t\"owner\": \""+ str(owner)+"\",\n\t\t\t\"state\": \""+ str(state)+"\",\n\t\t\t\"fid\": \""+str(fid)+"\"\n\t\t}\n\t\t},\n")
    #if the row is the last row dont put a comma at the end
    else:
        cords_list.append("\t\t{\n\t\t\"type\": \"Feature\",\n\t\t\"geometry\": {\n\t\t\t\"type\": \""+str(geo_type)+"\",\n\t\t\t\"coordinates\": \n\t\t\t"+str(coordinates)+"\n\t\t\t\n\t\t},\n\t\t\"properties\": {\n\t\t\t\"city\": \""+str(city)+"\",\n\t\t\t"+"\"county\": \""+str(county)+"\",\n\t\t\t\"number\": \""+str(number)+"\",\n\t\t\t\"parcelnumb\": \""+ str(parcelnumb)+"\",\n\t\t\t\"geoid\": \""+ str(geoid)+"\",\n\t\t\t\"ogc fid\": \""+ str(ogc_fid)+"\",\n\t\t\t\"owner\": \""+ str(owner)+"\",\n\t\t\t\"state\": \""+ str(state)+"\",\n\t\t\t\"fid\": \""+str(fid)+"\"\n\t\t}\n\t\t}\n")

#output geojson
#deletes any geojson file first before recreating

try:
    os.remove("result_task2.geojson")
except OSError:
    pass
with open("result_geojson.geojson", "a") as outputFile:
    outputFile.write(test) 
    for line in cords_list:       
        outputFile.write(line)
    outputFile.write("\t]\n}")