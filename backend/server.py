from app import createApp

app = createApp()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    # from gevent import pywsgi
    # server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    # server.serve_forever()