import pytest

from David_Hudson_HW1 import Record, calculate_total_price, CLOTHING_TAX_RATE_MA, CLOTHING_TAX_RATE_ME, \
    CLOTHING_TAX_RATE_NH, WIC_TAX_RATE_MA, WIC_TAX_RATE_NH, WIC_TAX_RATE_ME, SALES_TAX_MA, SALES_TAX_ME, SALES_TAX_NH, \
    round_total_price


def test_happy_path_maine():
    items_to_buy = [Record("eggs", quantity=3), Record("socks"), Record("pants"), Record("Bowl", quantity=3),
                    Record("Pencil", quantity=3)]

    total_price = calculate_total_price("me", items_to_buy)

    assert total_price == 69.14


def test_happy_path_massachusetts():
    items_to_buy = [Record("eggs", quantity=3), Record("socks"), Record("pants"), Record("Bowl", quantity=3),
                    Record("Pencil", quantity=3)]

    total_price = calculate_total_price("ma", items_to_buy)

    assert total_price == 67.69


def test_happy_path_new_hampshire():
    items_to_buy = [Record("eggs", quantity=3), Record("socks"), Record("pants"), Record("Bowl", quantity=3),
                    Record("Pencil", quantity=3)]

    total_price = calculate_total_price("nh", items_to_buy)

    assert total_price == 66


def test_clothing_tax():
    items_to_buy = [Record("hat")]

    total_price = calculate_total_price("ma", items_to_buy)
    assert total_price == round_total_price(10 + 10 * CLOTHING_TAX_RATE_MA)

    total_price = calculate_total_price("nh", items_to_buy)
    assert total_price == round_total_price(10 + 10 * CLOTHING_TAX_RATE_NH)

    total_price = calculate_total_price("me", items_to_buy)
    assert total_price == round_total_price(10 + 10 * CLOTHING_TAX_RATE_ME)


def test_wic_tax():
    items_to_buy = [Record("milk")]

    total_price = calculate_total_price("ma", items_to_buy)
    assert total_price == round_total_price(3 + 3 * WIC_TAX_RATE_MA)

    total_price = calculate_total_price("nh", items_to_buy)
    assert total_price == round_total_price(3 + 3 * WIC_TAX_RATE_NH)

    total_price = calculate_total_price("me", items_to_buy)
    assert total_price == round_total_price(3 + 3 * WIC_TAX_RATE_ME)


def test_everything_else_tax():
    items_to_buy = [Record("pencil")]

    total_price = calculate_total_price("ma", items_to_buy)
    assert total_price == round_total_price(1 + 1 * SALES_TAX_MA)

    total_price = calculate_total_price("nh", items_to_buy)
    assert total_price == round_total_price(1 + 1 * SALES_TAX_NH)

    total_price = calculate_total_price("me", items_to_buy)
    assert total_price == round_total_price(1 + 1 * SALES_TAX_ME)


def test_high_quantity():
    items_to_buy = [Record("pencil", quantity=1000000013)]

    total_price = calculate_total_price("ma", items_to_buy)
    assert total_price == 1062500013.82


def test_invalid_cart():
    items_to_buy = []
    total_price = calculate_total_price("me", items_to_buy)
    assert total_price == "Invalid Cart"

    items_to_buy = "chicken"
    total_price = calculate_total_price("ma", items_to_buy)
    assert total_price == "Invalid Cart"

    items_to_buy = ["eggs", "milk", "cheese"]
    total_price = calculate_total_price("ma", items_to_buy)
    assert total_price == "Invalid Cart"


def test_invalid_state():
    items_to_buy = [Record("milk", quantity=3), Record("hat"), Record("shirt"), Record("Bowl", quantity=3),
                    Record("paper", quantity=3)]

    total_price = calculate_total_price("az", items_to_buy)
    assert total_price == "Invalid State"

    total_price = calculate_total_price(0, items_to_buy)
    assert total_price == "Invalid State"


def test_negative_quantity():
    items_to_buy = [Record("pants", quantity=10), Record("hat", quantity=-2)]
    total_price = calculate_total_price("nh", items_to_buy)
    assert total_price == 200

    items_to_buy = [Record("hat", quantity=-25)]
    total_price = calculate_total_price("nh", items_to_buy)
    assert total_price == 0
