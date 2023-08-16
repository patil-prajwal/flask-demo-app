from flask import Flask, render_template, request

app = Flask(__name__, static_url_path="/static")

app.secret_key = b"5ce934008d5a"


@app.route("/index")
@app.route("/")
def home():
    return render_template("home.html")


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template("hello.html", name=name)


@app.route('/test')
def test():
    return app.send_static_file("test.html")


@app.route('/myIP')
def myIP():
    ip = request.remote_addr
    return render_template("myIP.html", ip=ip)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
