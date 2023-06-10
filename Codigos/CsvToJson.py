import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='latin-1') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        cont = 0
        for row in csvReader:
            cont +=1 
            row['_id'] = str(cont)
            #add this python dict to json array
            jsonArray.append(row)
            
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='latin-1') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'C:\\Users\\admin\\Desktop\\Peliculas.csv'
jsonFilePath = r'C:\\Users\\admin\\Desktop\\Peliculas.json'
csv_to_json(csvFilePath, jsonFilePath)

