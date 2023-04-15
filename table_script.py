import pandas as pd
import csv

#this is the empty list
city_name = [] 
county_name = [] 

#Uploading CSV file 
data = pd.read_csv('training_data.csv')

#extracting list of city and county from CSV file
city_name = data[data.columns[1]].tolist() #This returns the name of the column
county_name = data[data.columns[2]].tolist()

#creating disctionary list of city and county
dict = {'city': city_name, 'county': county_name}

df = pd.DataFrame(dict) 
#use groupby with function size. Then reset index with rename column 0 to count.
df = df.groupby(['county', 'city']).size().reset_index(name='count')

#df.drop_duplicates() - not needed

print (df)

#saving the dataframe 
df.to_csv('result_data.csv') 