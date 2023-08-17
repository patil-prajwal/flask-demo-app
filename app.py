from flask import Flask, render_template, request

app = Flask(__name__, static_url_path="/static")

app.secret_key = b"5ce934008d5a"


@app.route("/index")
@app.route("/")
def home():

    title = "App Home Page"
    text = "Hi There , You're At Home Page of App !!"
    return render_template("page.html", title=title, text=text)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):

    title = "App Home Page"
    if not name:
        text = "Hello, World!  It Is Home Page"
    else:
        text = f"Hello {name} !!"
    return render_template("page.html", name=name, title=title, text=text)


@app.route('/myIP')
def myIP():

    ip = request.remote_addr
    title = "User / Client IP Address Finder"
    if not ip:
        text = "Coudnt Get Your IP"
    else:
        text = f"Hello Your IP Address is {ip}"
    return render_template("page.html", ip=ip, title=title, text=text)


@app.route('/test')
def test():
    return app.send_static_file("test.html")


@app.errorhandler(404)
def page_not_found(error):

    title = "Page Not Found Error"
    text = "Your Requested Page Not Found !!!"
    return render_template('page.html', title=title, text=text), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
