from flask import Flask
from flask import render_template, send_from_directory
import config, dbalchemy, settings, os
import sUrl

app = Flask(__name__)
app.config.from_pyfile('settings.py')

dbalchemy.db.init_app(app)
app.register_blueprint(sUrl.bp)
config.create_or_check_db(app)

@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(
        host = settings.DEBUG_HOST, port = settings.DEBUG_PORT
    )
