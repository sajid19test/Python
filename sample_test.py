import unittest
import sample as AccountClass

class Test(unittest.TestCase):
    accInfo=AccountClass.account()

    def test_check_password_length(self):
        print('Checking sample password \n') 
        passwordlist=['eastiswheresunrise','eastindian','powerfulness']

        for passwd in passwordlist:
            print('Checking password '+passwd +'\n')
            passInfo=self.accInfo.check_password_length(passwd)
            self.assertTrue(passInfo)

if __name__=='__main__':
    unittest.main()
