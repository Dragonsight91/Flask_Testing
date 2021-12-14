from flask import Flask, redirect, render_template
from .api import v1, v2

def create_app():
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
    def api_doc():
        title="API Documentation"
        return render_template('base.html', title=title)

    @app.route("/api/<string:version>/<string:api_endpoint>")
    def api(version: str, api_endpoint: str, api_group: str):
        if version == "v1":
            return v1.api_call(api_endpoint, api_group)
        elif version == "v2":
            return v2.api_call(api_endpoint, api_group)
    
    return app