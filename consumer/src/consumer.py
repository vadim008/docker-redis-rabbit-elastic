import pika
import time
import os
import sys
import redis

exchange_name = os.environ['FRIEND_EXCHANGE'] if "FRIEND_EXCHANGE" in os.environ else "friends-talk"
routing_key = os.environ['ROUTING_KEY'] if "ROUTING_KEY" in os.environ else "friends.talk.back"


def connect_to_rabbit():


    #time.sleep(30)
    rabbit = os.environ['RABBIT'] if "RABBIT" in os.environ else "127.0.0.1"

    print(rabbit)

    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit))
    channel = connection.channel()

    return (connection, channel)

def got_the_message(m_channel, m_method, m_properties, body):
  #  channel.basic_ack(delivery_tag=method.delivery_tag)
    print(" From rabbitMQ :" + str(body))
    sys.stdout.flush()

    payload = r.lpop("payload")
    print(" Consumer from redis :" + str(payload))
    sys.stdout.flush()

   # queue = channel.queue_declare(queue=m_properties.reply_to)

    channel.basic_publish(exchange = "",
                          routing_key=m_properties.reply_to,
                          properties=pika.BasicProperties(
                          reply_to="no reply",
                          correlation_id="asddsa",
                           ),
                               body="cho nado")

    # channel.basic_publish(exchange="",
    #                            routing_key=properties.reply_to,
    #                            properties=properties,
    #                            body=" [s] Poshel v jopu :")


if __name__ == '__main__':

    redis_host = os.environ['REDIS'] if "REDIS" in os.environ else "127.0.0.1"
    r = redis.Redis(host=redis_host, port=6379, password="ppp")

    time.sleep(30)
    print(" Starting CONSUMER!'")
    sys.stdout.flush()

    connection, channel = connect_to_rabbit()

    print(" Connected to rabbit!'")
    sys.stdout.flush()

    queue = channel.queue_declare(queue='hello', exclusive=True).method.queue
    channel.queue_bind(exchange=exchange_name, queue=queue, routing_key='friends.*.*')

    print("Bind Queque !!!!")
    sys.stdout.flush()

    channel.basic_consume(got_the_message, queue=queue, no_ack=True)

    channel.start_consuming()


    connection.close()


