from flask import Flask, redirect, render_template

from Flask_Testing.api import v1,v2

app = Flask(__name__)

@app.route("/")
def index():
    title="Landing Page"
    return render_template('base.html', title=title)

@app.route("/login")
def login():
    title="Login Page"
    return render_template('base.html', title=title)

@app.route("/api/doc")
@app.route("/api/")
def api_doc():
    title="API Documentation"
    return render_template('base.html', title=title)

@app.route("/api/<string:version>/<string:api_group>/<string:api_endpoint>")
def api(version: str, api_endpoint: str, api_group: str):
    if version == "v1":
        return v1.api_call(api_endpoint, api_group)
    elif version == "v2":
        return v2.api_call(api_endpoint, api_group)

