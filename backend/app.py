from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps Backend</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }

            body {
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #0f172a, #1e293b, #111827);
                color: white;
                padding: 20px;
            }

            .container {
                width: 100%;
                max-width: 750px;
                background: rgba(255,255,255,0.08);
                padding: 50px;
                border-radius: 20px;
                text-align: center;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 30px rgba(0,0,0,0.4);
            }

            h1 {
                font-size: 3rem;
                margin-bottom: 20px;
                color: #38bdf8;
            }

            p {
                font-size: 1.2rem;
                line-height: 1.8;
                color: #cbd5e1;
            }

            .tech-stack {
                margin-top: 35px;
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 15px;
            }

            .tech {
                background: #1e293b;
                padding: 12px 20px;
                border-radius: 999px;
                border: 1px solid #334155;
                font-size: 0.95rem;
            }

            .btn {
                margin-top: 40px;
                padding: 14px 30px;
                border: none;
                border-radius: 10px;
                background: #22c55e;
                color: #0f172a;
                font-size: 1rem;
                font-weight: bold;
                cursor: pointer;
                box-shadow: 0 4px 15px rgba(34,197,94,0.4);
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🚀 Backend API Running</h1>

            <p>
                Successfully deployed using
                <b style="color:#22c55e;">Flask</b>,
                <b style="color:#f97316;">Docker</b>,
                <b style="color:#eab308;">Jenkins</b>,
                <b style="color:#38bdf8;">GitHub</b>
                and
                <b style="color:#a855f7;">AWS EC2</b>.
            </p>

            <div class="tech-stack">
                <div class="tech">Flask</div>
                <div class="tech">Docker</div>
                <div class="tech">Jenkins</div>
                <div class="tech">CI/CD</div>
                <div class="tech">AWS EC2</div>
            </div>

            <button class="btn">
                Backend Deployment Successful ✅
            </button>

        </div>

    </body>
    </html>
    """


@app.route("/api/health")
def health():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)