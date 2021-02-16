# from django.test import TestCase
# import random
# import datetime

# import Transactions_body
# from views import Morsal_APIs
# from PinBlock import PinBlock
# # Create your tests here.

# mors =Morsal_APIs()
# mastercard_body=[]
# TWK = mors.getWorking_Key(Transactions_body.Working_Key)
# pinb =PinBlock("6427",Transactions_body.payCard['PAN'],TWK,Transactions_body.TMK)
# Transactions_body.payCard['systemTraceAuditNumber']=(random.randrange(0, 9998)+1)
# Transactions_body.payCard['tranDateTime']=str(datetime.datetime.now())
# Transactions_body.payCard['PIN']= pinb.encrypted_pin_block()
# Transactions_body.payCard['expDate']="2203"
# balance = mors.PayCard(Transactions_body.payCard)
# if balance.status_code == 200:
#     print(balance.json())
# else:
#     print(balance.text)