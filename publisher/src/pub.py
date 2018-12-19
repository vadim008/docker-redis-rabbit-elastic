import pika
import time
import os
import sys


def connect_to_rabbit():


    time.sleep(30)

    rabbit = os.environ['RABBIT']
    print(os.environ['RABBIT'])

    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit))
    channel = connection.channel()

    return (connection, channel)



if __name__ == '__main__':

    print(" Starting publisher!'")
    sys.stdout.flush()

    connection, channel = connect_to_rabbit()
    channel.queue_declare(queue='hello')

    print(" Connected to rabbit!'")
    sys.stdout.flush()

    while 1:
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body='Hello World!')
        print(" [x] Sent 'Hello World!'")
        sys.stdout.flush()
        time.sleep(10)

    connection.close()


