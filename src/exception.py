import sys
from src.logger import logging

def get_error_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename()
    error_message = "Error occured in python script [{0}] line number [{1}] error message[{2}]".format()
    file_name,exc_tb.tb_lineno,str(error)
    
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_deatail:sys):
        super().__init__(error_message)
        self.error_message=get_error_details(error_message,error_detail=error_deatail)
        
    def __str__(self):
        return self.error_message
    
