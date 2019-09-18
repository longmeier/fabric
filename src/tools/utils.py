import pika
import time
from django.conf import settings
import logging
log = logging.getLogger(__name__)


def create_msg(msg, msg_=''):
    """
    消息发送方
    :param msg:
    :return:
    """
    msg = msg + msg_
    # rabbit_name = settings.RABBIT_NAME
    # rabbit_pwd = settings.RABBIT_PWD
    # rabbit_url = settings.RABBIT_URL
    # # log.info('name:%s;pwd:%s;url:%s', str(rabbit_name), str(rabbit_pwd), str(rabbit_url))
    # credentials = pika.PlainCredentials(rabbit_name, rabbit_pwd)
    # connection = pika.BlockingConnection(pika.ConnectionParameters(
    #     host=rabbit_url, port=5672, credentials=credentials))  # 定义连接池
    # channel = connection.channel()  # 声明队列以向其发送消息消息
    # # durable server挂了 队列仍然存在
    # channel.queue_declare(queue='fabric_log', durable=True)
    # # delivery_mode=2：使消息持久化。和队列名称绑定routing_key
    # channel.basic_publish(exchange='', routing_key='fabric_log', body=msg,
    #                       properties=pika.BasicProperties(delivery_mode=2))
    # connection.close()
