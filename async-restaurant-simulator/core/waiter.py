import asyncio
import random
from utils.logger import logger
from colorama import Fore
from datetime import datetime
from utils.billing import bill_generation
from utils.expoter import export_bill_txt


async def waiter(waiter_queue, order_queue, chefs):
    while True:
        order = await order_queue.get()
        if order is None:
            break

        order.waiter_name = await waiter_queue.get()

        await asyncio.sleep(1)
        logger.info(
            f"{Fore.BLUE}[{datetime.now()}][Order #{order.order_id}] {order.waiter_name} took the order from {order.customer_name}")
        await asyncio.sleep(1)

        chef = random.choice(chefs)
        await chef.prepare_order(order)

        await asyncio.sleep(1)
        if order.status == "Cancelled":
            logger.info(f"{Fore.RED}[{datetime.now()}][Order #{order.order_id}] "
                        f"{order.waiter_name} informs {order.customer_name} unable to process currently")
        else:
            order.served_at = datetime.now()
            logger.info(
                f"[{order.served_at}][Order #{order.order_id}] "
                f"{order.waiter_name} served {order.item} to {order.customer_name}")
            total_time_to_serve = order.duration()
            logger.info(f"{Fore.BLUE}[{datetime.now()}][Order #{order.order_id}] of {order.item}"
                        f" took {total_time_to_serve} seconds from placement to serving.")

        await bill_generation(order)
        await export_bill_txt(order)
        await waiter_queue.put(order.waiter_name)


        order_queue.task_done()
        