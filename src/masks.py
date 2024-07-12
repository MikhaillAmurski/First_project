import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8')
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def card_number_hider(payment_number: int) -> str:
    """Функция для скрытия номера карты"""
    logger.info("Маскируем карту клиента")
    str_payment_number = str(payment_number)
    if len(str_payment_number) == 16:
        hidden_payment_number = f"{str_payment_number[0:4]} {str_payment_number[4:6]}** **** {str_payment_number[-4:]}"
        return hidden_payment_number
    else:
        logger.error('Пользователь ввёл некоректные данные')
        return "Неизвестный счёт"


def account_number_hider(account: int) -> str:
    """Функция для скрытия номера счёта"""
    logger.info('Маскируем номер счёта')
    str_account = str(account)
    if len(str_account) == 20:
        hidden_payment_account = "**" + str_account[-4:]
        return hidden_payment_account
    else:
        logger.error('Пользователь ввёл некоректные данные')
        return "Неизвестный счёт"

