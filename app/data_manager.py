from app import db, app

class DataManager:
    def save_user(self, user):
        if app.config['USE_DATABASE']:
            db.session.add(user)
            db.session.commit()
        else:
            pass