import pika
import time
import os
import sys
from flask import Flask, render_template, logging, redirect, flash, url_for, sessions

from publisher import Publisher

app = Flask(__name__)

exchange_name = os.environ['FRIEND_EXCHANGE'] if "FRIEND_EXCHANGE" in os.environ else "friends-talk"
routing_key = os.environ['ROUTING_KEY'] if "ROUTING_KEY" in os.environ else "friends.talk.flask"


@app.route('/')
def index():
   print ("sdfsdfsdfsd")
   return "welcome"

@app.route('/pub/<payload>')
def pub(payload):
    """Simple Flask implementation for making asynchronous Rpc calls. """
    corr_id = pub.send_request(payload)

    while pub.queue[corr_id] is None:
        time.sleep(0.1)

    return pub.queue[corr_id]


if __name__ == '__main__':

    time.sleep(30)
    print(" Starting publisher!'")
    sys.stdout.flush()


    pub = Publisher(exchange_name, routing_key)
    pub.connect_to_rabbit_blocking()


    pub.channel.queue_declare(queue='friends.talk.back')

    try:
        app.run(host='127.0.0.1',port='12344')
    finally:
        pub.connection.close()


#class RegisterForm (Form):
