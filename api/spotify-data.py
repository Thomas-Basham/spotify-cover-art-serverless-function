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
            cover_art_data = data["thumbnail_url"]
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            self.wfile.write(bytes(json.dumps(cover_art_data, ensure_ascii=False), 'utf-8'))

        else:

            message = {"error": "error with query. make sure to query https://spotify-cover-art-serverless-function.vercel.app/api/spotify-data?spotifyurl= < Spotify Song Link Here > "}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            self.wfile.write(bytes(json.dumps(message, ensure_ascii=False), 'utf-8'))
        return
