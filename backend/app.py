from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "🚀 Backend Running Successfully!",
        "project": "DevOps CI/CD Portfolio",
        "technologies": [
            "Flask",
            "Docker",
            "Jenkins",
            "GitHub",
            "AWS EC2"
        ],
        "status": "success"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "server": "running",
        "deployment": "successful",
        "port": 5000
    })


@app.route("/api/devops")
def devops():
    return jsonify({
        "pipeline": [
            "GitHub Push",
            "Jenkins Pipeline",
            "Docker Build",
            "Docker Compose",
            "AWS Deployment"
        ],
        "frontend": "React + Vite",
        "backend": "Flask API",
        "containerization": "Docker",
        "orchestration": "Docker Compose"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)