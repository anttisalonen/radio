# coding=utf8

import subprocess
import os

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/radio", methods=['POST', 'GET'])
def radio(name=None):
    s = u'Radio P1 Trøndelag'
    if request.method == 'POST':
        try:
            os.unlink('foo')
        except OSError:
            pass
        subprocess.call('killall mplayer >/dev/null', shell=True)
        if request.form['submit'] == s:
            subprocess.call('mplayer http://lyd.nrk.no/nrk_radio_p1_trondelag_mp3_h &', shell=True)
            with open('foo', 'w') as f:
                f.write(s.encode('utf8'))
        elif request.form['submit'] == 'Stop':
            pass
        else:
            pass
    try:
        with open('foo', 'r') as f:
            name = f.read().decode('utf8').strip()
    except IOError:
        name = 'nothing'
    return render_template('radio.html', name=name)

if __name__ == "__main__":
    try:
        os.unlink('foo')
    except OSError:
        pass
    app.run()

