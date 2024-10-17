import os
import sys

import numpy as np
import pandas as pd
from Bank_Marketing.entity.config_entity import BankmarketingPredictorConfig
from Bank_Marketing.entity.s3_estimator import BankmarketingEstimator
from Bank_Marketing.exception import BankMarketingException
from Bank_Marketing.logger import logging
from Bank_Marketing.utils.main_utils import read_yaml_file
from pandas import DataFrame


class BankmarketingData:
    def __init__(self,
                 job,
                 marital,  
                 education,
                 default,
                 housing,
                 loan,
                 contact,
                 month,
                 day_of_week,
                 poutcome,
                 age,
                 duration,
                 campaign,
                 pdays,
                 previous,
                 emp_var_rate,  # Using underscores for Python-friendly names
                 cons_price_idx,
                 cons_conf_idx,
                 euribor3m,
                 nr_employed):
        
        """
        Bank Marketing Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.job = job
            self.marital = marital  # Assigning the passed value to self.marital
            self.education = education
            self.default = default
            self.housing = housing
            self.loan = loan
            self.contact = contact
            self.month = month
            self.day_of_week = day_of_week
            self.poutcome = poutcome
            self.age = age
            self.duration = duration
            self.campaign = campaign
            self.pdays = pdays
            self.previous = previous
            self.emp_var_rate = emp_var_rate
            self.cons_price_idx = cons_price_idx
            self.cons_conf_idx = cons_conf_idx
            self.euribor3m = euribor3m
            self.nr_employed = nr_employed

        except Exception as e:
            raise BankMarketingException(e, sys) from e

    def get_bank_input_data_frame(self)-> DataFrame:
        """
        This function returns a DataFrame from Bankdata class input
        """
        try:
            
            bank_input_dict = self.get_bank_data_as_dict()
            return DataFrame(bank_input_dict)
        
        except Exception as e:
            raise BankMarketingException(e, sys) from e


    def get_bank_data_as_dict(self):
        """
        This function returns a dictionary from BankmarketingData class input 
        """
        logging.info("Entered get_bank_data_as_dict method as BankmarketingData class")

        try:
            input_data = {
                "job": [self.job],
                "education": [self.education],
                "marital": [self.marital],
                "default": [self.default],
                "housing": [self.housing],
                "loan": [self.loan],
                "month": [self.month],
                "day_of_week": [self.day_of_week],
                "poutcome": [self.poutcome],
                "age": [self.age],
                "duration": [self.duration],
                "campaign": [self.campaign],
                "pdays": [self.pdays],
                "previous": [self.previous],
                "emp.var.rate": [self.emp_var_rate],
                "cons.price.idx": [self.cons_price_idx],
                "cons.conf.idx": [self.cons_conf_idx],
                "euribor3m": [self.euribor3m],
                "nr.employed": [self.nr_employed],
                "contact": [self.contact],
            }

            logging.info("Created bank data dict")

            logging.info("Exited get_bank_data_as_dict method as BankmarketingData class")

            return input_data

        except Exception as e:
            raise BankMarketingException(e, sys) from e

class BankClassifier:
    def __init__(self,prediction_pipeline_config: BankmarketingPredictorConfig = BankmarketingPredictorConfig(),) -> None:
        """
        :param prediction_pipeline_config: Configuration for prediction the value
        """
        try:
            # self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise BankMarketingException(e, sys)


    def predict(self, dataframe) -> str:
        """
        This is the method of BankClassifier
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of BankClassifier class")
            model = BankmarketingEstimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )
            result =  model.predict(dataframe)
            
            return result
        
        except Exception as e:
            raise BankMarketingException(e, sys)