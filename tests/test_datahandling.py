def jsonhandling():
    import json
    with open("testData/credentials.json") as f:
        data=json.load(f)
        print(data)
        #print(data["positivecrdentials"]["username"])
        #print(data["positivecrdentials"]["password"])

def test_csvhandling():
    import csv  
    with open ("testData/credentials.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            print(i)