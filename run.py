from flask import Flask
from API.views import Routes
from API.config.config import DevelopmentConfig          


class Server:

    """creating flask to start the server"""
    def create_app(self, config=None):
        app = Flask(__name__)
        app.config.from_object(DevelopmentConfig)
        Routes.generate(app)
        return app

app = Server().create_app()

if __name__=='__main__':
    app.run(debug=False)