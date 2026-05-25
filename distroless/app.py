from flask import Flask
import os

app = Flask(__name__)

LOG_DIR = "/app/logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.route("/")
def home():

    with open(f"{LOG_DIR}/access.log", "a") as f:
        f.write("Backend accessed\n")

    return "Backend Running with Volume 🚀"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)