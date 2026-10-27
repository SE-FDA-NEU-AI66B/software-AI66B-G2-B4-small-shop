#let's all use the fake data in this file

class FakeProductRepo:
    def __init__(
        self,
        available_products=None,
        expired_products=None,
        unavailable_products=None
    ):
        self.available_products = available_products or []
        self.expired_products = expired_products or []
        self.unavailable_products = unavailable_products or []