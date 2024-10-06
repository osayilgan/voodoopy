import os
from flask import Flask, render_template_string

class Gui:
    def __init__(self, page):
        self.page = page

    def run(self, debug=False):
        # Create the Flask app and specify the static folder location
        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template_string(self.page.render())

        # Run the app
        app.run(host="0.0.0.0", port=3000, debug=debug)
