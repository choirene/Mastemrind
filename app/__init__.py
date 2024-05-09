from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import index_bp, home_bp
    app.register_blueprint(index_bp)
    app.register_blueprint(home_bp)

    return app
    
create_app()