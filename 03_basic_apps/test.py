import decimal
import math 

pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_88_4_197_169_399_375')


decimal.getcontext().prec = 120
science = 2 * decimal.Decimal(pi) * decimal.Decimal(23.452346) ** 2
print(len(str(science)) - 5)