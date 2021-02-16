#from  pycrypto.lib.Crypto.Cipher import DES
#from Crypto.Cipher import DES
from des import DesKey
import click

class PinBlock:
    def __init__(self, pin, pan, twk, tmk):
        self.pin = pin
        self.pan = pan
        self.twk = twk
        self.tmk = tmk
    
    def clear_pin_block(self):
        """This function computes pin block given that we have acquired the working key.
        It computes as following:
            p1 = [0] + [pin_length] + [pin] + [10*f]
            p2 = [0000] + last_12_digits_of_pan_length-1
            clear PIN Block = p1 XOR p2
        """
        p1 = "0" + str(len(self.pin)) + str(self.pin) + 10 * "f"
        p2 = 4 * "0" + self.pan[:-1][-12:]
        assert len(p2) == len(p1)
        clear_pin_block = hex(int(p1, 16) ^ int(p2, 16))
        return "0" + clear_pin_block[2:]

    #def encrypted_pin_block(self):
        """This function computes the pin block.
        1. decrypt the working key using the masterkey
        2. encrypt the clear pin block using the decrypted working key
        3. return the encrypted pin block
        """
        # clear_pin_block = self.clear_pin_block()
        # des_master_key = DES.new(bytes.fromhex(self.tmk))
        # decrypted_working_key = des_master_key.decrypt(bytes.fromhex(self.twk))
        # assert isinstance(decrypted_working_key, bytes)
        # d = DES.new(decrypted_working_key)
        # pin_block = d.encrypt(bytes.fromhex(clear_pin_block))
        # return pin_block.hex()


    def encrypted_pin_block(self):
        clear_pin_block = self.clear_pin_block()
        des_master_key = DesKey(bytes.fromhex(self.tmk))
        decrypted_working_key = des_master_key.decrypt(bytes.fromhex(self.twk))
        assert isinstance(decrypted_working_key, bytes)
        d = DesKey(decrypted_working_key)
        pin_block = d.encrypt(bytes.fromhex(clear_pin_block))
        return pin_block.hex()




# import requests
# import random
# import datetime


# headers={
#     "content-type":"application/json",
#     "API-KEY":"5d6f54d4-3af4-4ffc-b78d-c2f1ca7827d9"    
# }

# terminalId='08001062'
# systemTraceAuditNumber=random.randrange(0, 9998)+1
# tranDateTime=str(datetime.datetime.now())

# body = {
#     "terminalId":terminalId,
#     "systemTraceAuditNumber":systemTraceAuditNumber,
#     "tranDateTime":tranDateTime
# }
# PAN='9222081700188054728'
# PIN='1198'
# expDate='2203'
# tranCurrencyCode='SDG'

# request =requests.post('https://212.0.129.118/terminal_api/workingKey/', headers=headers , json = body , verify=False)

# print(request.json())
# twk = request.json()["workingKey"]
# pinb =PinBlock(PIN,PAN,twk,'D020855E862F2A4F')
# encripted_pin = pinb.encrypted_pin_block()
# body = {
#     "terminalId":terminalId,
#     "systemTraceAuditNumber":systemTraceAuditNumber,
#     "tranDateTime":tranDateTime,
#     "PAN":PAN,
#     "PIN":encripted_pin,
#     "expDate":expDate,
#     "tranCurrencyCode":tranCurrencyCode

# }



# #transactions/balance/

# request =requests.post('https://212.0.129.118/terminal_api/transactions/balance/', headers=headers , json = body , verify=False)

# print(request.json())