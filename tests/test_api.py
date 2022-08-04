import requests

"""
Test Spotify's data url first to make sure that's still running the same
"""
def test_spotify_url():
    r = requests.get("https://open.spotify.com/oembed?url=https://open.spotify.com/track/3gdewACMIVMEWVbyb8O9sY?si=4aa5ccd2e28c4eae")
    data = r.json()
    print(data)
    assert data['title'] == "Rocket Man (I Think It's Going To Be A Long, Long Time)"
    assert data['thumbnail_url'] == "https://i.scdn.co/image/ab67616d00001e023009007708ab5134936a58b3"


def test_api_url():
    r = requests.get("https://spotify-cover-art-serverless-function.vercel.app/api/spotify-data?spotifyurl=https://open.spotify.com/track/3gdewACMIVMEWVbyb8O9sY?si=54f5722a4c5f482e")
    data = r.json()
    print(data)
    assert data == "https://i.scdn.co/image/ab67616d00001e023009007708ab5134936a58b3"


def test_api_url_error():
    r = requests.get("https://spotify-cover-art-serverless-function.vercel.app/api/spotify-data?spotifyurllll=https://open.spotify.com/track/3gdewACMIVMEWVbyb8O9sY?si=54f5722a4c5f482e")
    data = r.json()
    print(data)
    message = {
        "error": "error with query. make sure to query https://spotify-cover-art-serverless-function.vercel.app/api/spotify-data?spotifyurl= < Spotify Song Link Here > "}

    assert data == message
