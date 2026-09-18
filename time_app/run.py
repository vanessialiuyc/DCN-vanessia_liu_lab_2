from flask import Flask
from datetime import datetime, timezone, timedelta

app = Flask(__name__)


@app.route('/time')
def return_time():
    eastern = timezone(timedelta(hours=-4))
    now = datetime.now(eastern)
    return now.strftime('%m-%d-%Y %H:%M:%S')


if __name__=='__main__':
    app.run(host='0.0.0.0',
        port=8080,
        debug=True)
