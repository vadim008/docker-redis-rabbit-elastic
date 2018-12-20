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



if __name__ == '__main__':

    print(" Starting publisher!'")
    sys.stdout.flush()

    connection, channel = connect_to_rabbit()
    # This will create the exchange if it doesn't already exist.
    channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)
    #channel.queue_declare(queue='hello')

    print(" Connected to rabbit!'")
    sys.stdout.flush()

    while 1:
        channel.basic_publish(exchange=exchange_name,
                              routing_key='friend.hello.skot',
                              body='Hello Skot!',
                              properties=pika.BasicProperties(delivery_mode=2)
                              )

        print(" [x] Sent 'Hello Skot!'")
        sys.stdout.flush()
        time.sleep(10)

    connection.close()


