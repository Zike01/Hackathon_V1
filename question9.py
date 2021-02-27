"""
9 - Write a function that will work out the amount of VAT (https://en.wikipedia.org/wiki/Valueadded_tax) that is associated with a sale of a product. The function should take a gross price of
the product as an input, and then return the net price (without VAT) and the amount of VAT to pay.
UK VAT is 20%.
"""


def vat(gross_price, tax):
    tax_percentage = tax/100

    # Subtracts the tax price from the gross price
    net_price = round(gross_price * (1-tax_percentage), 2)

    vat_to_pay = round(gross_price * tax_percentage, 2)
    return net_price, vat_to_pay


price = float(input("Enter the gross price: £"))
vat_value = float(input("Enter the VAT percentage: %"))
net_price_and_vat = vat(price, vat_value)

print(f"Net Price = £{net_price_and_vat[0]}")
print(f"VAT to pay = £{net_price_and_vat[1]}")

