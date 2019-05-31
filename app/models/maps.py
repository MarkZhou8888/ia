import json, requests

def api_call(search_term):
    # get api key
    api_key = 'gCj7A0rm72aaZi0LZyx3iKX8M6EWTYEe'
    # create url by looking at doc
    url = 'https://api.giphy.com/v1/gifs/search?api_key='+api_key+'&q='+search_term+'&limit=25&offset=2&rating=PG-13&lang=es'
    url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/output?parameters'
    # print url for parsing
    print(url)
    # make call
    data = requests.get(url).json()

    all_pics = data['data']

    return all_pics
