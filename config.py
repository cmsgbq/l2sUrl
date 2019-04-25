
import dbalchemy

def create_or_check_db(app):
    @app.before_first_request
    def db_check_and_create():
        dbalchemy.db.create_all()
        