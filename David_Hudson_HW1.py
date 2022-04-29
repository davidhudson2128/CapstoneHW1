from dataclasses import dataclass

WIC_TAX_RATE_MA = 0
WIC_TAX_RATE_NH = 0
WIC_TAX_RATE_ME = 0

CLOTHING_TAX_RATE_MA = 0
CLOTHING_TAX_RATE_NH = 0
CLOTHING_TAX_RATE_ME = .055

SALES_TAX_MA = .0625
SALES_TAX_NH = 0
SALES_TAX_ME = .055


@dataclass
class Record:
    item_name: str
    type: str
    quantity: int
    price: float

    def __init__(self, item_name: str, quantity=1):
        if quantity < 0:
            self.item_name = "N/A"
            self.type = "N/A"
            self.quantity = 0
            self.price = 0
            return

        self.item_name = item_name.lower()
        self.quantity = quantity
        self.type = self.get_item_type(self.item_name)
        self.price = self.get_item_price(self.item_name) * self.quantity

    def get_item_type(self, item_name):
        item_type = ""
        if item_name == "eggs":
            item_type = "wic eligible foods"
        elif item_name == "yogurt":
            item_type = "wic eligible foods"
        elif item_name == "milk":
            item_type = "wic eligible foods"
        elif item_name == "cheese":
            item_type = "wic eligible foods"

        elif item_name == "socks":
            item_type = "clothing"
        elif item_name == "pants":
            item_type = "clothing"
        elif item_name == "shirt":
            item_type = "clothing"
        elif item_name == "hat":
            item_type = "clothing"

        elif item_name == "candy":
            item_type = "everything else"
        elif item_name == "bowl":
            item_type = "everything else"
        elif item_name == "paper":
            item_type = "everything else"
        elif item_name == "pencil":
            item_type = "everything else"

        return item_type

    def get_item_price(self, item_name):
        item_price = ""
        if item_name == "eggs":
            item_price = 3
        elif item_name == "yogurt":
            item_price = 4
        elif item_name == "milk":
            item_price = 3
        elif item_name == "cheese":
            item_price = 5

        elif item_name == "socks":
            item_price = 10
        elif item_name == "pants":
            item_price = 20
        elif item_name == "shirt":
            item_price = 12
        elif item_name == "hat":
            item_price = 10

        elif item_name == "candy":
            item_price = 2
        elif item_name == "bowl":
            item_price = 8
        elif item_name == "paper":
            item_price = 5
        elif item_name == "pencil":
            item_price = 1

        return item_price


def calculate_sub_total(records_list: [Record]):
    sub_total = 0
    for record in records_list:
        sub_total += record.price
    return sub_total


def calculate_massachusetts_tax_on_record(record: Record):
    tax = 0

    if record.type == 'wic eligible foods':
        tax += record.price * WIC_TAX_RATE_MA
    elif record.type == "clothing":
        tax += record.price * CLOTHING_TAX_RATE_MA
    elif record.type == "everything else":
        tax += record.price * SALES_TAX_MA

    return tax


def calculate_new_hampshire_tax_on_record(record: Record):
    tax = 0

    if record.type == 'wic eligible foods':
        tax += record.price * WIC_TAX_RATE_NH
    elif record.type == "clothing":
        tax += record.price * CLOTHING_TAX_RATE_NH
    elif record.type == "everything else":
        tax += record.price * SALES_TAX_NH

    return tax


def calculate_maine_tax_on_record(record: Record):
    tax = 0

    if record.type == 'wic eligible foods':
        tax += record.price * WIC_TAX_RATE_ME
    elif record.type == "clothing":
        tax += record.price * CLOTHING_TAX_RATE_ME
    elif record.type == "everything else":
        tax += record.price * SALES_TAX_ME

    return tax


def calculate_taxes(records_list: [Record], state: str):

    total_tax = 0
    if state == "ma":
        for record in records_list:
            total_tax += calculate_massachusetts_tax_on_record(record)

    elif state == "nh":
        for record in records_list:
            total_tax += calculate_new_hampshire_tax_on_record(record)

    elif state == "me":
        for record in records_list:
            total_tax += calculate_maine_tax_on_record(record)

    return total_tax


def round_total_price(price):

    if (price - round(price, 2)) <= 0:
        total_price = round(price, 2)
    else:
        total_price = round(price + .01, 2)

    return total_price


def calculate_total_price(state: str, records_list: [Record]) -> int:
    if state != "nh" and state != "ma" and state != "me":
        return "Invalid State"
    if type(state) != str:
        return "Invalid State"
    if type(records_list) != list:
        return "Invalid Cart"
    if len(records_list) == 0:
        return "Invalid Cart"
    elif type(records_list[0]) != Record:
        return "Invalid Cart"

    state = state.lower()

    sub_total = calculate_sub_total(records_list)
    taxes = calculate_taxes(records_list, state)

    total_price = round_total_price((sub_total + taxes))

    print(f"Sub Total: ${round(sub_total, 2)}")
    print(f"Taxes: ${round(taxes, 2)}")

    return total_price


def main():
    items_to_buy = [Record("milk", quantity=3), Record("hat"), Record("shirt"), Record("Bowl", quantity=3),
                    Record("paper", quantity=3)]

    total_price = calculate_total_price("me", items_to_buy)
    print(f"Total price: ${total_price}")


if __name__ == '__main__':
    main()


# Items For Sale
#    Wic Eligible Foods:
#       - Eggs       $3
#       - Yogurt     $4
#       - Milk       $3
#       - Cheese     $5
#
#    Clothing:
#       - Socks     $10
#       - Pants     $20
#       - Shirt     $12
#       - Hat       $10
#
#    Everything Else:
#       - Candy     $2
#       - Bowl      $8
#       - Paper     $5
#       - Pencil    $1
