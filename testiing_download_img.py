import os
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote
from selenium import webdriver

from serpapi import GoogleSearch
import requests, lxml, re, json, urllib.request

def serpapi_get_google_images(query):
    image_results = []

    # search query parameters
    params = {
        "engine": "google",               # search engine. Google, Bing, Yahoo, Naver, Baidu...
        "q": query,                       # search query
        "tbm": "isch",                    # image results
        "num": "10",                     # number of images per page
        "ijn": 0,                         # page number: 0 -> first page, 1 -> second...
        "api_key": "c29d3cb47572955cb027dded55650f88a4520db103243003fa5d897870e405f8",                 # https://serpapi.com/manage-api-key
        # other query parameters: hl (lang), gl (country), etc
    }

    search = GoogleSearch(params)         # where data extraction happens

    images_is_present = True
    #while images_is_present:
    results = search.get_dict()       # JSON -> Python dictionary

    # checks for "Google hasn't returned any results for this query."
    if "error" not in results:
        for index, image in enumerate(results["images_results"], start=1):
            if image["original"] not in image_results:
                image_results.append(image["original"])
                if index>2:
                    break

        # update to the next page
        #params["ijn"] += 1
    else:
        print(results["error"])
        images_is_present = False

    # -----------------------
    # Downloading images
    # for index, image in enumerate(image_results, start=1):
    #     print(f"Downloading {index} image...")

    #     opener=urllib.request.build_opener()
    #     opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36")]
    #     urllib.request.install_opener(opener)

    #     urllib.request.urlretrieve(image, f"{query}_{index}.jpg")

    #     if index>2:
    #         break

    #print(type(json.dumps(image_results, indent=2)))
    # print(image_results[0])
    # print(type(image_results))
    # print(len(image_results))


    output = image_results[0]

    return output
    #return json.dumps(image_results, indent=2)


test = serpapi_get_google_images("Audi a3") # test
print(test)
