import unittest

from pika import BlockingConnection, ConnectionParameters


class TestRabbitMQ(unittest.TestCase):

    def test_creation_works(self):

        host = 'localhost'
        queue = 'testqueue'
        whitelist = tuple()
        blacklist = tuple()

        self.connection = BlockingConnection(ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.queue = queue
        self.whitelist = whitelist
        self.blacklist = blacklist
        self.channel.queue_declare(queue=self.queue, durable=True)
