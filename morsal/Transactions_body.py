import random
import datetime
from morsal.PinBlock import PinBlock


TMK = 'D020855E862F2A4F'
terminalId='08001052'
systemTraceAuditNumber=random.randrange(0, 9998)+1
tranDateTime=str(datetime.datetime.now())


Working_Key={"terminalId":terminalId,"systemTraceAuditNumber":random.randrange(0, 9998)+1,"tranDateTime":tranDateTime}
PinBlock = {
"PIN":'',
"PAN":'',
"TWK":''
}
Balance ={
    
    "terminalId":terminalId,
    "systemTraceAuditNumber":(random.randrange(0, 9998)+1),
    "tranDateTime":tranDateTime,
    "PAN":"",
    "PIN":"",
    "expDate":"",
    "tranCurrencyCode":"SDG"


}
Card_to_Card = {

    "terminalId":terminalId,
    "systemTraceAuditNumber":random.randrange(0, 9998)+1,
    "tranDateTime":tranDateTime,
    "expDate":'',
    "PIN":'',
    "toCard":'',
    "tranCurrencyCode":'SDG',
    "tranAmount":'',
    "PAN":''


}


changePIN={
    "terminalId":terminalId,
    "systemTraceAuditNumber":(random.randrange(0, 9998)+1),
    "tranDateTime":tranDateTime,
    "PAN":"",
    "PIN":"",
    "newPIN":"7691",
    "expDate":"",
    # "tranCurrencyCode":"SDG"
    
}
payCard={
"terminalId":terminalId,
"systemTraceAuditNumber":random.randrange(0, 9998)+1,
"tranDateTime":tranDateTime,
 "mobile_number": "0994915556",
 "toCard": "",
 "expDate":'',
 "PIN":'',
 "tranAmount": "", 
 "full_name": "MOHAMED", 
 "password2": "Mors@123",
 "password1": "Mors@123",
 "pan": "9222221700215429597",
 #9222221700214007535 Iman Babiker Elhussain / 0912999361
 "PAN": "9222081700188054728",
 'clientId': 'Ashrafcom',
'tranCurrencyCode': 'SDG', 
}
# {'expDate': '2203',
#  'clientId': 'Ashrafcom', 
# 'systemTraceAuditNumber': 1139, 
# 'toCard': '9222081709682058000', 
# 'tranAmount': '50.00',
#  'terminalId': '08001051', 
#  'PIN': '206041CD36EE17A8',
#  'tranCurrencyCode': 'SDG', 
#  'PAN': '9222081700851945012',
#   'tranDateTime': '251020162642'}
Mini_statement={
 
    "terminalId":terminalId,
    "systemTraceAuditNumber":(random.randrange(0, 9998)+1),
    "tranDateTime":tranDateTime,
    "PAN":"",
    "PIN":"",
    "expDate":"",
    "tranCurrencyCode":"SDG"

}
billInquiry = {
    "terminalId":terminalId,
    "systemTraceAuditNumber":random.randrange(0, 9998)+1,
    "tranDateTime":tranDateTime,
    "expDate":"",
    "PIN":"",
    "payeeId":"",
    "personalPaymentInfo":"",
    "tranCurrencyCode":'SDG',
    "tranAmount":"",
    "PAN":"",
}
