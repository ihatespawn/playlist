from flask import Flask, render_template, request, send_from_directory
from time import sleep as wait
import requests
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/getvideos")
def getvideos():
    vidlinks = []
    playlist = request.args.get('playlist')
    domain = playlist.split("://")[1].split("/")[0]
    if "youtube" in domain:
        playlistid = playlist.split("playlist?list=")[1]
        rq = requests.get(f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlistid}&maxResults=1000&key=" + os.environ.get('YOUTUBE_API_KEY', ''))
        req = rq.json()
        if req.get('error'):
            return req["error"]["message"]
        else:
            for vid in req["items"]:
                vidlinks.append("https://youtube.com/watch?v=" + vid["snippet"]["resourceId"]["videoId"])
    else:
        return "invalid service, for now it only supports normal youtube playlists", 406
    return ';'.join(vidlinks)

@app.route("/files/<path:path>")
def files(path):
    return send_from_directory("static", path)
