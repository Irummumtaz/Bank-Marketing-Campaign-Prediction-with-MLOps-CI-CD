from Bank_Marketing.logger import logging
from Bank_Marketing.exception import BankMarketingException
import sys

logging.info('Welcome to our custom log')
try:
    a=2/0
except Exception as e:
    raise BankMarketingException(e,sys)