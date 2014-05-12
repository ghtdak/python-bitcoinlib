# Distributed under the MIT/X11 software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import unittest

from bitcoin.messages import msg_version, msg_verack, msg_addr, msg_alert, \
    msg_inv, msg_getdata, msg_getblocks, msg_getheaders, msg_headers, msg_tx, \
    msg_block, msg_getaddr, msg_ping, msg_pong, msg_mempool, MsgSerializable

import sys
if sys.version > '3':
    from io import BytesIO
else:
    from cStringIO import StringIO as BytesIO


class MessageTestCase(unittest.TestCase):

    def serialization_test(self, cls):
        m = cls()
        mSerialized = m.to_bytes()
        mDeserialzed = cls.from_bytes(mSerialized)
        mSerialzedTwice = mDeserialzed.to_bytes()
        self.assertEqual(mSerialized, mSerialzedTwice)


class Test_msg_version(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_version)


class Test_msg_verack(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_verack)


class Test_msg_addr(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_addr)


class Test_msg_alert(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_alert)


class Test_msg_inv(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_inv)


class Test_msg_getdata(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_getdata)


class Test_msg_getblocks(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_getblocks)


class Test_msg_getheaders(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_getheaders)


class Test_msg_headers(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_headers)


class Test_msg_tx(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_tx)


class Test_msg_block(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_block)


class Test_msg_getaddr(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_getaddr)


class Test_msg_ping(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_ping)


class Test_msg_pong(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_pong)


class Test_msg_mempool(MessageTestCase):

    def test_serialization(self):
        super().serialization_test(msg_mempool)


class Test_messages(unittest.TestCase):
    verackbytes = b'\xf9\xbe\xb4\xd9verack\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00]\xf6\xe0\xe2'

    def test_read_msg_verack(self):
        f = BytesIO(__class__.verackbytes)
        m = MsgSerializable.stream_deserialize(f)
        self.assertEqual(m.command, msg_verack.command)

    def test_msg_verack_to_bytes(self):
        m = msg_verack()
        b = m.to_bytes()
        self.assertEqual(__class__.verackbytes, b)
