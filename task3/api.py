#-*- encoding: utf-8 -*-
from flask import Flask, request, jsonify
from appearance import appearance

app = Flask(__name__)

@app.route('/', methods=["POST"])
def only_endpoint():
    input_json = request.get_json(force = True)
    to_return = {'result': appearance(input_json)}
    return(jsonify(to_return))

if __name__ == "__main__":
    app.run()
