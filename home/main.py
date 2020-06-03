import requests, json
import pandas as pd

def main():
    rawJSON = getData("https://c19downloads.azureedge.net/downloads/json/coronavirus-cases_latest.json")

    jsonToDataframe(rawJSON)

def getData(loc):
    response = requests.get(loc)
    data = response.json()

    return data

def jsonToDataframe(json):

    return 0    

if __name__ == "__main__":
    main()