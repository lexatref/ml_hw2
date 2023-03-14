from flask import Flask
from flask import request
import requests
from io import BytesIO
import logging

from plate_client import PlateClient

app = Flask(__name__)

@app.route('/readPlateNumber', methods=['GET'])
def read_plate_number():
    if 'imageid' not in request.args:
        return {'error': 'field "imageid" not found'}, 400
    imageid = request.args['imageid']
    reader = PlateClient('http://51.250.83.169:7878/images')
    status, res = reader.readNumber(imageid)

    if status==200:
        return {
        'plate_number': res,
        }
    else:
        return {'error': res}, status

@app.route('/readPlateNumbers', methods=['GET'])
def read_plate_numbers():
    if 'imageids' not in request.args:
        return {'error': 'field "imageids" not found'}, 400
    imageids = request.args['imageids']

    reader = PlateClient('http://51.250.83.169:7878/images')
    status, res = reader.readNumbers(imageids)

    if status==200:
        return {'plate_numbers': res}
    else:
        return {'error': res}, status

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(levelname)s] [%(asctime)s] %(message)s',
        level=logging.INFO,
    )

    app.run(host='0.0.0.0', port=8080, debug=True)
