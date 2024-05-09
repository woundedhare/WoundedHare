import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
API_KEY = os.getenv("API")
JOKE_URL = os.getenv("URL")
API_YA = os.getenv("YANDEX-API")
STIKERS = ['CAACAgIAAxkBAAEKQYxk_G926IYLUwpS9-wsHsnjKNaSXgACSgEAAzigCpydmfjnXbh-MAQ',
           'CAACAgIAAxkBAAEKQYRk_G8rrpiXKcBBGHuY6Dn-laBgLQACPwEAAzigClVGk7NU2b2xMAQ',
           'CAACAgIAAxkBAAEKQXRk_G64Z409E28BLVkhnqijoXut8AACSAEAAzigCpn_CLs0tRoGMAQ',
           'CAACAgIAAxkBAAEKQW9k_G5VaGkEbukxr22tmKeiJ9zWfgACUAEAAzigCqBetrko8wydMAQ',
           'CAACAgIAAxkBAAEKQUtk_G1KjEUTHtlXCr15nyZAmzPRnwAC6QAEOKAKSndrbn6hA3EwBA',
           'CAACAgIAAxkBAAEKQUdk_G0aKdYHOfLwBIiJIe7-0B7cqwACHwEAAzigCmCIkOB_zmI0MAQ',
           'CAACAgIAAxkBAAEKQN1k_CvOHTOWBatbeA9TSDn2yN3BYwACpAEAAzigCmQLvu1OqzgRMAQ']