# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


import requests
import odoo

from odoo.addons.base_rest.tests.common import BaseRestCase

HOST = "127.0.0.1"
PORT = odoo.tools.config["http_port"]


class BaseEMCRestCase(BaseRestCase):
    def setUp(self):
        super().setUp()
        self.session = requests.Session()
        self.demo_request_1 = self.browse_ref(
            "easy_my_coop.subscription_request_1_demo"
        )
        self.demo_request_1_dict = {
            "id": self.demo_request_1.id,
            "name": "Manuel Dublues",
            "email": "manuel@demo.net",
            "date": "2020-02-23",
            "ordered_parts": 3,
            "share_product": {
                "id": self.demo_request_1.share_product_id.id,
                "name": "Part B - Worker",
            },
            "address": {
                "street": "schaerbeekstraat",
                "zip_code": "1111",
                "city": "Brussels",
                "country": "BE",
            },
            "lang": "en_US",
        }

    def http_get(self, url):
        if url.startswith("/"):
            url = "http://%s:%s%s" % (HOST, PORT, url)
        return self.session.get(url)

    def http_post(self, url, data):
        if url.startswith("/"):
            url = "http://%s:%s%s" % (HOST, PORT, url)
        return self.session.post(url, data=data)
