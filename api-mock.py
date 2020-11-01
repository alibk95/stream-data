from flask import Flask, Response, stream_with_context, render_template
import time
import uuid
import random

APP = Flask(__name__)


@APP.route("/",  methods=["GET"])
def home():
    return render_template('index.html')


@APP.route("/request_data/<int:rowcount>", methods=["GET"])
def get_large_request(rowcount):
    """retunrs N rows of data"""
    def f():
        """The generator of mock data"""
        for _i in range(rowcount):
            time.sleep(.1)
            txid = uuid.uuid4()
            print(txid)
            uid = uuid.uuid4()
            amount = round(random.uniform(-1000, 1000), 2)
            yield f"('{txid}', '{uid}', {amount})\n"
    return Response(stream_with_context(f()))


if __name__ == "__main__":
    APP.run(debug=True, port=8080)