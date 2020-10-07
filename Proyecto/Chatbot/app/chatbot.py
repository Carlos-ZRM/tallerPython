from flask import Flask, request, json, Response

import os

if "FLASK_HOST"   in os.environ:
    FLASK_HOST = os.environ["FLASK_HOST"]
else :
    FLASK_HOST =  '0.0.0.0'


if "FLASK_PORT"   in os.environ:
    FLASK_PORT = os.environ["FLASK_PORT"]
else :
    FLASK_PORT = 5000
    
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_ips():
    #print(request.environ)
    return Response(response=json.dumps({'IP Remota ': request.remote_addr, 'IP Host':request.environ['SERVER_NAME'],'Informacion ':os.uname()[1]}),
                    status=200,
                    mimetype='application/json')


if __name__ == '__main__':
        app.run(debug=True, port=FLASK_PORT, host=FLASK_HOST)