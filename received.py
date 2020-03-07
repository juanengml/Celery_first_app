import pika
from time import sleep
import logging
import threading
import time


def LOADING_API():
    for p in range(200):
        sleep(1)
        print(p," [x] LOADING DATA")



def callback(ch, method, properties, body):
    data = body.decode("utf-8")
    print(" [x] Received %s" % data)
    if data == "start_rubicon_job":
     processo = threading.Thread(target=LOADING_API)
     processo.start()
    sleep(1)




connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
connection.process_data_events(time_limit=1)
channel = connection.channel()

channel.queue_declare(queue='rubicon')


channel.basic_consume(
    queue='rubicon', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
