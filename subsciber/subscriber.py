import pika


def consume_callback(ch, method, properties, body):
    print(" [x] Received %r" % body)



connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()


channel.queue_declare(queue='hello')



channel.basic_consume(consume_callback,
                      queue='hello',
                      no_ack=True)



print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

