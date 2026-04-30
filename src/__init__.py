from flask import Flask
from .extensions import db, login_manager
from .routes import auth_bp, stats_bp
import os
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)


    ### Application Configuration
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-me-in-production")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI") or (
        f"mysql+pymysql://{os.getenv('DB_USER', 'root')}:{os.getenv('DB_PASSWORD', 'password')}@"
        f"{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '3306')}/{os.getenv('DB_NAME', 'gympal')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



    ### Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"  # type: ignore[assignment]


    ### User Session Management
    # Tell Flask-Login how to reload user objects from session cookies
    from .models import User



    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))



    ### Register Route Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(stats_bp)

    ### Database Initialization
    # Auto-create tables in development mode - use Flask-Migrate for production
    with app.app_context():
        db.create_all()

    return app