from argparse import ArgumentParser
import datetime
import hashlib
import time

from flask import Flask
from flask import request
from flask import jsonify
import numpy as np


app = Flask(__name__)

####### PUT YOUR INFORMATION HERE #######
CAPTAIN_EMAIL = 'my@gmail.com'          #
SALT = 'my_salt'                        #
#########################################


def generate_server_uuid(input_string):
    """ Create your own server_uuid.
    @param:
        input_string (str): information to be encoded as server_uuid
    @returns:
        server_uuid (str): your unique server_uuid
    """
    s = hashlib.sha256()
    data = (input_string + SALT).encode("utf-8")
    s.update(data)
    server_uuid = s.hexdigest()
    return server_uuid


def predict(sentence_list, phoneme_sequence_list):
    """ Predict your model result.
    @param:
        sentence_list (list): an list of sentence sorted by probability.
        phoneme_sequence_list (list): an list of phoneme sequence sorted by probability.
    @returns:
        prediction (str): a sentence.
    """

    ####### PUT YOUR MODEL INFERENCING CODE HERE #######
    prediction = '喂你好密碼無法進去'


    ####################################################
    if _check_datatype_to_string(prediction):
        return prediction


def _check_datatype_to_string(prediction):
    """ Check if your prediction is in str type or not.
        If not, then raise error.
    @param:
        prediction: your prediction
    @returns:
        True or raise TypeError.
    """
    if isinstance(prediction, str):
        return True
    raise TypeError('Prediction is not in string type.')


@app.route('/inference', methods=['POST'])
def inference():
    """ API that return your model predictions when E.SUN calls this API. """
    data = request.get_json(force=True)

    # 自行取用，可紀錄玉山呼叫的 timestamp
    esun_timestamp = data['esun_timestamp']

    # 取 sentence list 中文
    sentence_list = data['sentence_list']
    # 取 phoneme sequence list (X-SAMPA)
    phoneme_sequence_list = data['phoneme_sequence_list']

    t = datetime.datetime.now()
    ts = str(int(t.utcnow().timestamp()))
    server_uuid = generate_server_uuid(CAPTAIN_EMAIL + ts)

    try:
        answer = predict(sentence_list, phoneme_sequence_list)
    except TypeError as type_error:
        # You can write some log...
        raise type_error
    except Exception as e:
        # You can write some log...
        raise e
    server_timestamp = time.time()

    return jsonify({'esun_uuid': data['esun_uuid'],
                    'server_uuid': server_uuid,
                    'answer': answer,
                    'server_timestamp': server_timestamp})


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8080, help='port')
    arg_parser.add_argument('-d', '--debug', default=True, help='debug')
    options = arg_parser.parse_args()
    
    app.run(host='0.0.0.0', port=options.port, debug=options.debug)