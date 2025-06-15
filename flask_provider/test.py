from flask import Flask, send_file, abort
import os
from urllib.parse import unquote

server = Flask(__name__)

VIDEO_FOLDER = os.path.join(os.getcwd(), "vids_flask")

@server.route("/video/<path:filename>")
def get_video(filename):
    decoded_filename = unquote(filename)  # Decodifica espaços e caracteres especiais
    filepath = os.path.join(VIDEO_FOLDER, decoded_filename)
    if not os.path.isfile(filepath):
        return abort(404, description="Arquivo não encontrado")
    return send_file(filepath, mimetype="video/mp4")

if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=6000)
