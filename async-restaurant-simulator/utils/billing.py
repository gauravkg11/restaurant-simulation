from utils.logger import logger
from config import menu
from colorama import Fore


async def bill_generation(order):
    logger.info(f"{Fore.CYAN}========= BILL =========")
    logger.info(f"{Fore.CYAN}Order ID     : {order.order_id}")
    logger.info(f"{Fore.CYAN}Customer     : {order.customer_name}")
    logger.info(f"{Fore.CYAN}Item         : {order.item}")
    logger.info(f"{Fore.CYAN}Waiter       : {order.waiter_name}")
    logger.info(f"{Fore.CYAN}Chef Attempts: {order.attempts + 1}")
    logger.info(f"{Fore.CYAN}Prep Time    : {order.item_prep_time} seconds")
    logger.info(f"{Fore.CYAN}Total Time   : {round(order.duration(), 2)} seconds")
    logger.info(f"{Fore.CYAN}Amount       : {float(menu[order.item][1])}")
    logger.info(f"{Fore.CYAN}Status       : {order.status}")
    logger.info(f"{Fore.CYAN}Placed At    : {order.placed_at.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"{Fore.CYAN}Served At    : {order.served_at.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"{Fore.CYAN}========================\n")