import pika
import time
import os
import sys


exchange_name = os.environ['FRIEND_EXCHANGE']

def connect_to_rabbit():


    #time.sleep(30)

    rabbit = os.environ['RABBIT']
    print(os.environ['RABBIT'])

    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit))
    channel = connection.channel()

    return (connection, channel)

def got_the_message(channel, method, properties, body):
    print(" [s] GET:" + str(body))
    sys.stdout.flush()



if __name__ == '__main__':

    print(" Starting publisher!'")
    sys.stdout.flush()

    connection, channel = connect_to_rabbit()

    print(" Connected to rabbit!'")
    sys.stdout.flush()

    queue = channel.queue_declare(queue='hello', exclusive=True).method.queue
    channel.queue_bind(exchange=exchange_name, queue=queue, routing_key='friend.*.*')

    print("Bind Queque !!!!")
    sys.stdout.flush()

    channel.basic_consume(got_the_message, queue=queue, no_ack=True)

    channel.start_consuming()


    connection.close()


