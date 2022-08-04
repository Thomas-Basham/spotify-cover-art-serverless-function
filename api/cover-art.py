from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import json

class handler(BaseHTTPRequestHandler):
    # track_url = "/api/cover-art?spotifyurl=http://open.spotify.com/track/0UJTi2a46HRnFD8wGFYjil?si=db7b62083e8c4253"

    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "spotifyurl" in dic:
            url = f"https://open.spotify.com/oembed?url="
            r = requests.get(url + dic["spotifyurl"])
            data = r.json()
            # for item in data:
            #     picture = item["thumbnail_ur"]
            # message = data
        #
        # # elif "capital" in dic:
        # #     url = "https://restcountries.com/v3.1/capital/"
        # #     r = requests.get(url + dic["capital"])
        # #     data = r.json()
        # #     for item in data:
        # #         country = item["name"]["common"]
        # #     message = f'{dic["capital"]} is the capital of {country}.'
        # #
        # else:
        #     message = 'URL Undefined '

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        self.wfile.write(bytes(json.dumps(data, ensure_ascii=False), 'utf-8'))

        # self.wfile.write(message.encode())
        return


def test_spotify_url():
    r = requests.get("https://open.spotify.com/oembed?url=http://open.spotify.com/track/0UJTi2a46HRnFD8wGFYjil?si=db7b62083e8c4253")
    data = r.json()
    print(data)
