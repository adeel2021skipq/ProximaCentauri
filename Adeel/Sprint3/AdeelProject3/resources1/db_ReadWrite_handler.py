import boto3 , json

def ReadFromTable(tableName):
    client = boto3.client('dynamodb')
    
    ########################## Scaning values from DB table ###########
    Urls = client.scan(
            TableName=tableName,
            AttributesToGet=[
            'Links'])
    links = Urls['Items'] # list of items
    
    ############## changing list into dictionery ###########
    
    URL_names = {}
    for i in range(len(links)):
        URL_names[i] = links[i]
        
    ################ getting the url names ############
        
    names = []
    for j in range(len(URL_names)):
       names.append(URL_names[j]['Links']['S'])
    
    print(names)
    return names
