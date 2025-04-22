import asyncio
import random
import os
from config import waiter_names, chef_names
from utils.logger import logger
from core.chef import Chef
from core.customer import customer
from core.waiter import waiter

os.makedirs("exports", exist_ok=True)


async def main():
    order_queue = asyncio.Queue()
    num = random.randint(1, 5)
    waiter_queue = asyncio.Queue()

    logger.info(f"\n[System] Processing {num} customers order....\n")

    chefs = [Chef(name) for name in chef_names]

    for name in waiter_names:
        await waiter_queue.put(name)

    waiter_task = [asyncio.create_task(waiter(waiter_queue, order_queue, chefs)) for _ in waiter_names]

    customers = [customer(i, order_queue) for i in range(num)]  # creates a list of coroutines
    await asyncio.gather(*customers)

    await order_queue.join()

    for _ in waiter_names:
        await order_queue.put(None)

    await asyncio.gather(*waiter_task)

    logger.info("\n[System] All order have been served")  # Unpack list of coroutines


asyncio.run(main())
