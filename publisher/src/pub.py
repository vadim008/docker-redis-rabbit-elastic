import pika
import time
import os
import sys
from flask import Flask, render_template, logging, redirect, flash, url_for, sessions

import redis
import publisher


app = Flask(__name__)

exchange_name = os.environ['FRIEND_EXCHANGE'] if "FRIEND_EXCHANGE" in os.environ else "friends-talk"
routing_key = os.environ['ROUTING_KEY'] if "ROUTING_KEY" in os.environ else "friends.talk.flask"


@app.route('/')
def index():
   print ("sdfsdfsdfsd")
   sys.stdout.flush()
   return "welcome"

@app.route('/pub/<payload>')
def pub(payload):
    """Simple Flask implementation for making asynchronous Rpc calls. """
    print(payload)
    sys.stdout.flush()

    corr_id = pub.send_request(payload)
    r.lpushx("payload", payload)


    while pub.queue[corr_id] is None:
        time.sleep(0.1)

    return pub.queue[corr_id]


if __name__ == '__main__':

    print(" Connect to Redis")
    redis_host = os.environ['REDIS'] if "REDIS" in os.environ else "127.0.0.1"
    r = redis.Redis(host=redis_host, port=6379, password="ppp")

    r.("routing", routing_key)

    p = r.get("routing")
    print(p)


    time.sleep(30)
    print(" Starting publisher!'")
    sys.stdout.flush()


    pub = publisher.Publisher(exchange_name, routing_key)
    pub.connect_to_rabbit_blocking()


    pub.channel.queue_declare(queue='friends.talk.back')

    try:
        app.run(host='0.0.0.0')
    finally:
        pub.connection.close()



