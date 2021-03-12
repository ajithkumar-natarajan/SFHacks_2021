import requests
import pgeocode

zipcode = input("Please enter the zipcode: ")

nomi = pgeocode.Nominatim('us')


cookies = {
    '$cookie: check': 'true',
    'mbox': 'session#ea3f22d353504c22957abbe8dc0e695c#1615118857',
    '_elevaate_session_id': 'dec27f65-764f-4782-b13f-f327b1c3abfe',
    'AMCVS_3B2A35975CF1D9620A495FA9%40AdobeOrg': '1',
    '__rutmb': '149436981',
    '__ruid': '149436981-lr-7d-40-1p-x8wwdlogricmqepf1f3i-1615116997273',
    '__rcmp': '0\\u0021bj1fZ2MsZj1nYyxzPTAsYz0xNDgsdHI9MCxybj01MDksdHM9MjAyMTAzMDcuMTEzNixkPXBj',
    's_cc': 'true',
    'rxVisitor': '1615116999589MG9S9SQEU8ITTH9IO3P944A86QD5T71V',
    'dtSa': '-',
    'dtLatC': '18',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'rxvt': '1615118799987|1615116999613',
    'form_key': 'gBBa53Se9TLkBVdp',
    'mage-messages': '',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'dtCookie': 'v_4_srv_2_sn_D0MK2BATI4ACATINGNJL49HB0C9OB5HF_app-3Ab52fc261121850f8_1_ol_0_perc_100000_mul_1',
    'PHPSESSID': '3a53380d9ef384eda42905f4e9a8f6c6',
    'wp_customerGroup': 'NOT+LOGGED+IN',
    'section_data_ids': '%7B%22cart%22%3A1615117003%2C%22prop65%22%3A1615117004%7D',
    'dtPC': "2$516999574_106h-vHFSQPCDVBVMEWFRLFFUOGABOHHNBKFHK-0e1",
    'gpv_Page': 'no%20previous%20value',
    's_plt': '13.65',
    's_pltp': 'web%3Apharmacy%3Acovid-qualifier',
    's_sq': '%5B%5BB%5D%5D',
    's_campaign': '%7Cstate%7Cweb%7CCovid19%7C%7CCovid19scheduler_CA_2_12_21%7C',
    '__rutma': '149436981-lr-7d-40-1p-x8wwdlogricmqepf1f3i-1615116997273.1615116997273.1615116997273.1.7.7',
    '__rpck': '0\\u0021eyJwcm8iOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsImJ0Ijp7IjAiOnRydWUsIjEiOjAsIjIiOm51bGwsIjMiOjF9LCJDIjp7fSwiTiI6e30sImR0cyI6OTUuNSwiY3NwIjp7ImIiOjUwNDkzLCJ0IjoyODIsInNwIjoxNDMyNDI1LCJjIjoxfX0~',
    'AMCV_3B2A35975CF1D9620A495FA9%40AdobeOrg': '77933605%7CMCIDTS%7C18694%7CMCMID%7C79681738152645808990980332024825527657%7CMCOPTOUT-1615124446s%7CNONE%7CvVersion%7C4.5.1',
    '__rpckx': '0\\u0021eyJ0NyI6eyIyIjoxNjE1MTE3MDA3Njc0LCIzIjoxNjE1MTE3MDcxNTEyfSwidDd2Ijp7IjIiOjE2MTUxMTcwNjg1OTksIjMiOjE2MTUxMTcyNTI1OTF9LCJpdGltZSI6IjIwMjEwMzA3LjExMzYiLCJlYyI6Mn0~',
}

headers = {
    'authority': 'www.riteaid.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not\\"A\\\\Brand";v="99"',
    'accept': '*/*',
    'dnt': '1',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.riteaid.com/pharmacy/apt-scheduler',
    'accept-language': 'en-US,en;q=0.9',
}

params = (
    ('address', str(zipcode)),
    ('attrFilter', 'PREF-112'),
    ('fetchMechanismVersion', '2'),
    ('radius', '50'),
)

response = requests.get('https://www.riteaid.com/services/ext/v2/stores/getStores', headers=headers, params=params, cookies=cookies)

# print(response.json())

if(len(response.json()['Data']['stores'])>0):
  print("Appointment is available")
else:
  print("Appointment is not available")
