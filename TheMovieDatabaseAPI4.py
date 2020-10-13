#importeren van modules
import urllib.parse
import requests

#variabelen benoemen + input geven
main_api = "https://api.themoviedb.org/4/search/movie?"
#vul je authenticatie credentials hier in
key = "1e57fffd40e60bde3747fd40109749e3"
while True:
    title = input("Movie to search for: ")
    #om het scriptje te kunenn stoppen
    if title == "quit" or title == "q":
        break


    #url samenstellen
    url = main_api + urllib.parse.urlencode({"api_key":key, "query":title})

    #informatie ophalen via url
    json_data = requests.get(url).json()

    if json_data != "":
        #resultaat printen
        for item in json_data["results"]:
            print("=================================================================")
            print("Title: " + str(item["title"]) + "\n")
            print("Popularity:", item["popularity"], "\n")
            print("Overview:", item["overview"], "\n")
            print("=================================================================")
    #als er geen resultaat is gevonden
    else:
        print("This movie is not found")