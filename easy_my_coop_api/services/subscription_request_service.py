# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.addons.component.core import Component
from odoo.fields import Date
from . import schemas




class SubscriptionRequestService(Component):
    _inherit = "base.rest.service"
    _name = "subscription.request.services"
    _usage = "subscription_request"  # service_name
    _collection = "emc.services"
    _description = """
    Subscription requests
    """

    def _to_dict(self, sr):
        sr.ensure_one()
        return {
            "id": sr.id,
            "name": sr.name,
            "email": sr.email,
            "date": Date.to_string(sr.date),
            "ordered_parts": sr.ordered_parts,
            "share_product": {
                "id": sr.share_product_id.id,
                "name": sr.share_product_id.name,
            },
            "address": {
                "street": sr.address,
                "zip_code": sr.zip_code,
                "city": sr.city,
                "country": sr.country_id.code,
            },
            "lang": sr.lang,
        }

    def get(self, _id):

        try:
            _id = int(_id)
        except TypeError as e:
            raise e  # todo do better than this

        # fixme remove sudo
        sr = self.env["subscription.request"].sudo().browse(_id)
        if sr:
            return self._to_dict(sr)
        else:
            raise Exception  # todo better than this

        return {"response": "Get called with message " + message}

    def search(self, params=None):
        # fixme remove sudo
        if params is None:
            requests = self.env["subscription.request"].sudo().search([])
        else:
            requests = self.env["subscription.request"].sudo().search([])

        response = {
            "count": len(requests),
            "rows": [
                self._to_dict(sr) for sr in requests
            ]
        }
        return response

    # def update(self, _id, message):
    #     return {'response': 'PUT called with message ' + message}

    # pylint:disable=method-required-super
    # def create(self, **params):
    #     return {'response': 'POST called with message ' + params['message']}

    def _validator_get(self):
        return {"_id": {"type": "integer"}}

    def _validator_return_get(self):
        return schemas.S_SUBSCRIPTION_REQUEST

    def _validator_search(self):
        return {}

    def _validator_return_search(self):
        return schemas.S_SUBSCRIPTION_REQUEST_LIST

    # def _validator_update(self):
    #     return {'message': {'type': 'string'}}
    #
    # def _validator_create(self):
    #     return {'message': {'type': 'string'}}
