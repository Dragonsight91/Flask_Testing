from flask import Flask, redirect, render_template
from .api import api_v1, api_v2

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(api_v1.bp)
    app.register_blueprint(api_v2.bp)

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
    
    return app