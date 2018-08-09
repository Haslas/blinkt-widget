import requests
import status_file_handling_funcs as sfhf

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('dashboard.html', statuses=sfhf.load_statuses())


@app.route('/', methods=['POST'])
def change():
    errorTuple = (
                 requests.exceptions.Timeout,
                 requests.exceptions.ConnectTimeout,
                 requests.exceptions.ConnectionError)
    the_new_status = request.form['new_status']
    endpoint = request.form['endpoint']
        # changes the status of the relevant device by calling api.refresh()
    try:
        requests.post(endpoint, data={'new_status': the_new_status}, timeout=1)
        # status.change_status(the_new_status)
    except:
        pass
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001, threaded=True)
