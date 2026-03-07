import urllib.request, json
try:
    response = urllib.request.urlopen('http://127.0.0.1:9222/json')
    data = json.loads(response.read())
    for p in data:
        if p['type'] == 'page':
            print(f"URL: {p['url']}")
            print(f"Title: {p['title']}")
except Exception as e:
    print(f"Error: {e}")
