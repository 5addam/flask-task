from concurrent.futures import thread
from flask_task import app

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
