# Mastering Tuple Packing and Unpacking in Python

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

def order_data_string_formatter(detail):
    res = ""
    for i in detail:
        name, equipment, quality = i
        if quality == 1:
            res += f"{name} ordered {quality} {equipment}.\n"
        elif quality > 1:
            res += f"{name} ordered {quality} {equipment}s."
    return res


print(order_data_string_formatter(orders))