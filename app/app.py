# app/app.py
import os
from dotenv import load_dotenv
from app import create_app
from app.config import DevelopmentConfig, ProductionConfig

load_dotenv()

env = os.environ.get('ENV', 'development')
config_class = DevelopmentConfig if env == 'development' else ProductionConfig
app = create_app(config_class)

if __name__ == '__main__':
    app.run()
