S_SUBSCRIPTION_REQUEST = {
    "id": {"type": "integer"},
    "name": {"type": "string"},
    "email": {"type": "string"},
    "date": {"type": "string"},  # todo date?
    "ordered_parts": {"type": "integer"},
    "share_product": {
        "type": "dict",
        "schema": {"id": {"type": "integer"}, "name": {"type": "string"}},
    },
    "address": {
        "type": "dict",
        "schema": {
            "street": {"type": "string"},
            "zip_code": {"type": "string"},
            "city": {"type": "string"},
            "country": {"type": "string"},
        },
    },
    "lang": {"type": "string"},
}

S_SUBSCRIPTION_REQUEST_LIST = {
    "count": {"type": "integer"},
    "rows": {
        "type": "list",
        "schema": {"type": "dict", "schema": S_SUBSCRIPTION_REQUEST},
    }
}
