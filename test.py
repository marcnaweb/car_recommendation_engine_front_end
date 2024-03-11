import requests

def searche_img(img_name:str):
    # Your Google Custom Search Engine ID
    cse_id = 'b7ff0286733a14d63'
    # Your API key
    api_key = 'AIzaSyCgPetKA5xfpAek8r0pGw5ie8NuYo4D_is'
    # The search query
    query = "site:auto-data.net " + img_name
    # The search URL
    search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cse_id}&key={api_key}&searchType=image"
    # Make the request
    response = requests.get(search_url)
    results = response.json()
    print(results)
    # Extracting image URLs
    try:
        image_urls = [item['link'] for item in results['items']]
        print(image_urls)
        output = image_urls[0]
        return output
    except:
        return("img not working")

print(searche_img("audi a3"))
