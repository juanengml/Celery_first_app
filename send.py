import pika

class Publish(object):
    def __init__(self,host,msg,queue):
        self.host = host
        self.comm =  pika.BlockingConnection(pika.ConnectionParameters(host=self.host,heartbeat=30))
        self.msg = msg
        self.queue = queue
    def send(self):
       self.channel = self.comm.channel()
       self.channel.queue_declare(queue=self.queue)
       self.channel.basic_publish(exchange='', routing_key=self.queue, body=self.msg)
       print("["+self.queue+"] : message: "+self.msg)
    def  close_comm(self):
       self.comm.close()
