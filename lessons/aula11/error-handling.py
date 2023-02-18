# @file: error-handling.py @author: Osvaldo Alves @date: 09/02/2023
# @description: Learning to use try an except.

import time

try:
    a = 1200/'a'
except ZeroDivisionError:
    print('Divisão por zero. Não existe!')
except Exception as error:
    print('Exception ERROR:', error) 
    time.sleep(2)