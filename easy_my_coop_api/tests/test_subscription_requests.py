# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


import json

from datetime import date, timedelta
from odoo.fields import Date
from odoo.addons.base_rest.controllers.main import _PseudoCollection
from odoo.addons.component.core import WorkContext

from .common import BaseEMCRestCase


class TestSRController(BaseEMCRestCase):
    def test_service(self):
        # kept as example
        # useful if you need to change data in database and check db type
        collection = _PseudoCollection("emc.services", self.env)
        emc_services_env = WorkContext(
            model_name="rest.service.registration", collection=collection
        )

        service = emc_services_env.component(usage="subscription_request")

        result = service.get(self.demo_request_1.id)
        self.assertEquals(self.demo_request_1_dict, result)

    def test_get_route(self):
        id_ = self.demo_request_1.id
        route = "/api/subscription_request/%s" % id_
        response = self.http_get(route)
        self.assertEquals(response.status_code, 200)

        content = json.loads(response.content)
        self.assertEquals(self.demo_request_1_dict, content)

    def test_search_route(self):
        route = "/api/subscription_request"
        response = self.http_get(route)
        self.assertEquals(response.status_code, 200)

        content = json.loads(response.content)

        self.assertIn(
            self.demo_request_1_dict, content["rows"]
        )

    # def test_search_route_from_date(self):
    #     from_ = Date.to_string(date.today() - timedelta(days=12))
    #     response = self.http_get("/api/subscription_request?from=%s" % from_)
    #     self.assertEquals(response.status_code, 200)
    #
    #     content = json.loads(response.content)
    #     self.assertTrue("message" in content)
