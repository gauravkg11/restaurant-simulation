from core.order import Order
from config import menu
from colorama import Fore
from utils.logger import logger
from datetime import datetime
import asyncio
import random


class Chef:
    def __init__(self, name: str):
        self.name = name

    async def prepare_order(self, order: Order):
        order.item_prep_time = menu[order.item][0]
        logger.info(
            f"{Fore.MAGENTA}[{datetime.now()}][Order #{order.order_id}] {self.name} is preparing {order.item}...")

        while order.attempts <= 2:
            if order.attempts == 2:
                logger.info(f"{Fore.RED}[{datetime.now()}][Order #{order.order_id}] {self.name} canceled {order.item}")
                order.status = "Cancelled"
                break
            if random.random() < 0.2:
                order.status = "Preparation Failed"
                order.attempts += 1
                continue
            else:
                await asyncio.sleep(order.item_prep_time)
                order.status = "Prepared"
                logger.info(
                    f"{Fore.GREEN}[{datetime.now()}][Order #{order.order_id}] {self.name} finished preparing {order.item}")
                logger.info(f"[{datetime.now()}][Order #{order.order_id}] "
                            f"Preparation time for {order.item} {order.item_prep_time} seconds")
                break
