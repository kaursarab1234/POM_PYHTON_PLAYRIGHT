import csv


def csvdate(filepath):
    print("handling csv file")
    values=[]
   # filepath="testData/credentials.csv"
    with open(filepath) as f:
        formatteddata=csv.DictReader(f)
        for i in formatteddata:
            values.append(i)
    return values
