from django.shortcuts import render
from morsal.Request import SendRequest
import random
import datetime



headers={"content-type":"application/json","API-KEY":"5d6f54d4-3af4-4ffc-b78d-c2f1ca7827d9"}
URL='https://212.0.129.118/terminal_api'

class Morsal_APIs:
    def getWorking_Key(self,body):
        url=URL+'/workingKey/'
        Request=SendRequest(url,headers,body)
        R=Request.POST_Send().json()["workingKey"]
        return R
        
    def getBalanceInquery(self,body):
        url='https://212.0.129.118/terminal_api/transactions/balance/'
        Request = SendRequest(url,headers,body)
        return Request.POST_Send()
    def PayCard(self,body):
        url='https://212.0.129.118/terminal_api/register_card/'
        Request = SendRequest(url,headers,body)
        return Request.POST_Send()
    def Card_to_Card(self,body):
        url='https://212.0.129.118/terminal_api/transactions/cardTransfer/'
        Request = SendRequest(url,headers,body)
        return Request.POST_Send()
        # billPayment
    def billInquiry(self,body):
        url='https://212.0.129.118/terminal_api/transactions/billInquiry/'
        Request = SendRequest(url,headers,body)
        return Request.POST_Send()
    def billPayment(self,body):
        url='https://212.0.129.118/terminal_api/transactions/billPayment/'
        Request = SendRequest(url,headers,body)
        return Request.POST_Send()
    #register_card
    def miniStatement(self,body):
        url='https://212.0.129.118/terminal_api/transactions/miniStatement/'
        Request = SendRequest(url,headers,body)
        return Request.POST_Send()
    
    def ChangePIN(self,body):
        url='https://212.0.129.118/terminal_api/transactions/changePin/'
        Request = SendRequest(url,headers,body)
        return Request.POST_Send()