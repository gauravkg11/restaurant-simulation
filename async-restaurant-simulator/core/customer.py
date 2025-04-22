import asyncio
from core.order import Order
import random
from config import customer_list, menu
from utils.logger import logger
from colorama import Fore


async def customer(order_id, order_queue):
    await asyncio.sleep(1)
    order = Order(
        order_id=order_id,
        customer_name=random.choice(customer_list),
        item=random.choice(list(menu)),
    )
    await order_queue.put(order)

    logger.info(
        f"{Fore.GREEN}[{order.placed_at}][Order#{order.order_id}] {order.customer_name} placed an order for {order.item}")