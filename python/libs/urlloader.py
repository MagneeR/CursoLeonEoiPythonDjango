from urllib import request #Necesitamos la libreria de python urllib para hacer llamadas http

def load_url(url):
    req = request.Request(url, headers = {'User-Agent' : 'Mozilla/5.0'})
    with request.urlopen(req) as response:
        return response.read()