

import pika
import time
import os
import sys
import uuid
import threading

class Publisher:
    internal_lock = threading.Lock()
    queue = {}

    def __init__(self, exchange_name, routing_key):
        self.exchange_name = exchange_name
        self.routing_key = routing_key
        pass

    def connect_to_rabbit_blocking(self):
        #time.sleep(30)
        rabbit = os.environ['RABBIT'] if "RABBIT" in os.environ else "127.0.0.1"

        print (rabbit)
        sys.stdout.flush()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit))
        self.channel = self.connection.channel()

        # This will create the exchange if it doesn't already exist.
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='topic', durable=True)
        result = self.channel.queue_declare(queue='friend.talk.back')
        self.callback_queue = result.method.queue

        thread = threading.Thread(target=self._process_data_events)
        thread.setDaemon(True)
        thread.start()

        return (self.connection, self.channel)



    def send_request(self, payload):

        corr_id = str(uuid.uuid4())
        self.queue[corr_id] = None
        with self.internal_lock:
            self.channel.basic_publish(exchange=self.exchange_name,
                                       routing_key=self.routing_key,
                                       properties=pika.BasicProperties(
                                           reply_to=self.callback_queue,
                                           correlation_id=corr_id,
                                       ),
                                       body=payload)
        return corr_id

    def _process_data_events(self):
        """Check for incoming data events.
        We do this on a thread to allow the flask instance to send
        asynchronous requests.
        It is important that we lock the thread each time we check for events.
        """
        self.channel.basic_consume(self._on_response, no_ack=True,
                                   queue=self.callback_queue)
        while True:
            with self.internal_lock:
                self.connection.process_data_events()
                time.sleep(0.1)

    def _on_response(self, ch, method, props, body):
        """On response we simply store the result in a local dictionary."""
        self.queue[props.correlation_id] = body
        print ("Publisher: " + body)
        sys.stdout.flush()
