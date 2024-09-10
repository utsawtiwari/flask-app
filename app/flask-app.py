from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ip')
def get_ip():
    pod_ip = request.remote_addr
    return f"Pod IP address: {pod_ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

