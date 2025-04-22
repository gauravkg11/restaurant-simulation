from config import menu


async def export_bill_txt(order):
    filename = f"exports/bill no_{order.order_id}.txt"
    with open(filename, "w") as f:
        f.write(f"========= BILL =========\n")
        f.write(f"Order ID     : {order.order_id}\n")
        f.write(f"Customer     : {order.customer_name}\n")
        f.write(f"Item         : {order.item}\n")
        f.write(f"Waiter       : {order.waiter_name}\n")
        f.write(f"Chef Attempts: {order.attempts + 1}\n")
        f.write(f"Prep Time    : {order.item_prep_time} seconds\n")
        f.write(f"Total Time   : {round(order.duration(), 2)} seconds\n")
        f.write(f"Amount       : {float(menu[order.item][1])}\n")
        f.write(f"Status       : {order.status}\n")
        f.write(f"Placed At    : {order.placed_at.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Served At    : {order.served_at.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"========================\n")