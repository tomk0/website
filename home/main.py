import requests

def main():
    json = getData("https://c19downloads.azureedge.net/downloads/json/coronavirus-cases_latest.json")


def getData(loc):
    response = requests.get(loc)
    data = response.json()

    return data

if __name__ == "__main__":
    main()