import serverless_wsgi
from flask import Flask, request, redirect, url_for, send_from_directory
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
#import requests
#import re



from flask_cors import CORS, cross_origin
import json  
import os
import catch_prices_model_pipeline

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=[ 'POST'])
@cross_origin()
def predictTarget():
    inputs  = request.args.get('inputs', None)
    rec_json = json.loads(inputs)
    rec_dict = rec_json 

    if request.method == 'POST':
        print(inputs)
        out = catch_prices_model_pipeline.predictTarget(rec_dict)
        print(out)

        return str(out)
    else:
        return "The 'get' method is not acceptable for calling this webservice, please use the 'post' method instead."
    
    
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)
def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)