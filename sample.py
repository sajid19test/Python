class account:
         def check_password_length(self,password):
             if len(password)>8:
                 return True
             else:
                 return False
         def check_spcl_char(self,password):
            if password.__contains__('*'):
                return True
            else:
                return False

if __name__=='__main__':
    accVerify=account()
    print('Password length is '+str(accVerify.check_password_length('offtoschool')))
    print('Password conatains special character ' +str(accVerify.check_spcl_char('offtoschool')))
    print('Password test complted')
    print('Webhook check and test')
