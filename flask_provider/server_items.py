# flask_videos.py
from flask import Flask, jsonify, send_from_directory, request
import os

vid_server = Flask(__name__)
VIDEO_FOLDER = os.path.join(os.getcwd(), "vids_flask") # Folder with your .mp4, .mkv, etc.

@vid_server.route('/video/<filename>')
def serve_video(filename):
    return send_from_directory(VIDEO_FOLDER, filename)

@vid_server.route('/video_list')
def video_list():
    files = os.listdir(VIDEO_FOLDER)
    videos = {

        file: f"http://{request.host}/video/{file}"
        for file in files if file.lower().endswith(('.mp4', '.mkv', '.webm'))
    }
    return jsonify(videos)

if __name__ == '__main__':
    vid_server.run(debug=True, host="0.0.0.0", port=7000)  # Accessible on localhost and LAN IP

