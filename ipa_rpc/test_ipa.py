from unittest import TestCase
import unittest
import ipa_rpc
import time
import json

class TestIpa(TestCase):

    USERNAME = ""
    PASSWORD = ""
    SERVER = ""

    def setUp(self):
        self.LOG_FILE = 'test.log'
        self.log = file(self.LOG_FILE, 'a')
        print >> self.log, time.asctime()
        self.log.flush()

        self.myipa = ipa_rpc.ipa(self.SERVER)

    def tearDown(self):
        print >> self.log, time.asctime()
        self.log.flush()
        self.log.close
        self.myipa = None

    @unittest.skip
    def test_login(self):
        response = None

        response = self.myipa.login(user=self.USERNAME, password=self.PASSWORD)
        self.assertIsNotNone(response)
        # print response

    # def test_makeReq(self):
    #     response = None
    #
    #     response = self.myipa.makeReq(pdict=None)
    #
    #     self.assertIsNotNone(response)
    #     print response

    # def test_config_show(self):
    #     response = None
    #     self.myipa.login(user=self.USERNAME, password="")
    #     response = self.myipa.config_show()
    #     print response
    #     self.assertIsNotNone(response)

    @unittest.skip
    def test_dnsrecord_show(self):

        response = None
        self.myipa.login(user=self.USERNAME, password=self.PASSWORD)
        response = self.myipa.dnsrecord_show(dns_zone="spoc.linux", record_name="glance.os")
        print response
        error = response.get('error')
        self.assertIsNone(error)
        self.assertIsNotNone(response)

    @unittest.skip
    def test_dnsrecord_find(self):
        response = None
        self.myipa.login(user=self.USERNAME, password=self.PASSWORD)
        response = self.myipa.dnsrecord_find(dns_zone="spoc.linux", query_string=".os")
        print response
        error = response.get('error')
        self.assertIsNone(error)
        self.assertIsNotNone(response)

    @unittest.skip
    def test_dnsrecord_add(self):
        response = None
        self.myipa.login(user=self.USERNAME, password=self.PASSWORD)
        response = self.myipa.dnsrecord_add(dns_zone="spoc.linux", record_name="foobar.os",
                                            ip_address="1.2.3.4")
        print response
        error = response.get('error')
        self.assertIsNone(error)
        self.assertIsNotNone(response)

    @unittest.skip
    def test_dnsrecord_del(self):
        response = None
        self.myipa.login(user=self.USERNAME, password=self.PASSWORD)
        response = self.myipa.dnsrecord_del(dns_zone="spoc.linux", record_name="foobar.os")
        print response
        error = response.get('error')
        self.assertIsNone(error)
        self.assertIsNotNone(response)

    def test_is_valid_ipv4_address(self):
        self.myipa.login(user=self.USERNAME, password=self.PASSWORD)
        response = self.myipa.is_valid_ipv4_address('1.2.3.4456')
        print response


# response = None
#
# response = self.myipa.
# print response
# self.assertIsNotNone(response)
#