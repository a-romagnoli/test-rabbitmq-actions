import unittest

from pika import BlockingConnection, ConnectionParameters


class TestRabbitMQ(unittest.TestCase):

    def test_creation_works(self):

        host = '127.0.0.1'
        queue = 'testqueue'

        self.connection = BlockingConnection(ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue)
