from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")


@app.route('/sidebar_left', methods=['GET'])
def sidebar_left():
    return render_template("sidebar-left.html")


@app.route('/sidebar_right', methods=['GET'])
def sidebar_right():
    return render_template("sidebar-right.html")


@app.route('/single', methods=['GET'])
def single():
    return render_template("single.html")


@app.route('/blog', methods=['GET'])
def blog():
    return render_template("blog.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)