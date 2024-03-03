from flask import Flask
from app.regist_views import regist
from app.signin import auth
from app.today_views import today_bp
from app.models import db


def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.db'
    db.init_app(app)
    

    app.register_blueprint(regist)
    app.register_blueprint(auth)
    app.register_blueprint(today_bp)

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)