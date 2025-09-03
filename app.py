import redis
from flask import Flask, render_template

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)

@app.route("/")
def home():
    count = cache.incr("hits")
    return render_template("home.html", visits=count)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
