class OrderError(Exception):
    def __init__(self, status, message):
        self.status = status
        self.message = message


def create_order(repo, products):

    if len(products) == 0:
        raise OrderError(
            422,
            "Order must contain at least one product"
        )

    for product in products:

        if product["name"] in repo.expired_products:
            raise OrderError(
                409,
                "This product is expired and cannot be sold!"
            )

        if product["name"] in repo.unavailable_products:
            raise OrderError(
                409,
                "This product is insufficient at the moment!"
            )

    return {"status": 201}