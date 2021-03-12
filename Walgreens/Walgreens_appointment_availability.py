import requests
import pgeocode

zipcode = input("Please enter the zipcode: ")

nomi = pgeocode.Nominatim('us')

cookies = {
    'rxVisitor': '1614469013989TLPQKLKO5OMB1JC3BGA6Q0JOK9FUT0H2',
    'uts': '1614469020236',
    'at_check': 'true',
    'session_id': '3d6a9f6f-3ab3-4669-992e-5977b1f852e0',
    'XSRF-TOKEN': '7xVEAaR8/7375A==.KjywqOXGhbaJbqwZ0KLUdS0g2slQVE6h/Cm7NsesN/s=',
    'dtCookie': "6$7FFEAGNBR74I1CJ3AM8QBJ8SQNFTEH0N|0eed2717dafcc06d|1",
    'AMCVS_5E16123F5245B2970A490D45%40AdobeOrg': '1',
    'gRxAlDis': 'N',
    's_cc': 'true',
    'IM_throttle_1223': 'off',
    'USER_LOC': '5K48AZ9EjJueHdeGxVUeBwuAIjJ7tdA3OzqkiSw6ORXxyE%2FZoeEkuc0O6uydMJPA',
    'liveagent_oref': 'https://www.walgreens.com/login.jsp?ru=%2Ffindcare%2Fvaccination%2Fcovid-19%2Feligibility-survey%3Fflow%3Dcovidvaccine%26register%3Drx',
    'liveagent_ptid': '68fcaaed-3ff8-439b-abda-25629eda8f24',
    'liveagent_sid': 'f133ecea-9fcc-4478-bcfe-7e8164ac8360',
    'liveagent_vc': '3',
    'FirstName': 'Test',
    'ACO_LOGIN': 'true',
    '3s': 'xKXDt+KCrMWkw5cuxKbDs8O9xI5JxY4=',
    'meHshId': 'y0CisdTIL5sjZ9ljxnDzavGZw2LdTgN6mxJJk7g2iGA=',
    'profileId': '200014691794',
    'USER_TYPE': 'Rx',
    '2fa': 'ae2a68e352477d68fef9a173ce5ec754',
    'cm.BgF4rQB9bKQHB9zfIXAPXrvd.B9bKQHZQh': '1614501369',
    'rvi': 'prodNumber',
    'strOfrId': '{"WAStrId":"3288"}',
    'str_nbr_do': '3288',
    'fc_vnum': '2',
    'dtSa': '-',
    'AMCV_5E16123F5245B2970A490D45%40AdobeOrg': '-1124106680%7CMCIDTS%7C18693%7CMCMID%7C45811785186894816677786311730696744036%7CMCOPTOUT-1615061535s%7CNONE%7CvVersion%7C5.2.0',
    'mbox': 'PC#f6776ab1e1c442a0b8b5d2ee1e291192.34_0#1678299136|session#300a19894d194c7cb3e3d967065a0c7f#1615056195',
    's_sq': '%5B%5BB%5D%5D',
    'bm_sz': 'DE83E5111F95ED403E63FEC3954DF66A~YAAQhb7CF7xRuLZ3AQAA6tscDAsn2i0sddIYDyw8ezJjpbwE6kPPW17+wxwNqL67XR3UkYEkGBLzo7xd1mleRYOJH9gy2ZsRli3yIkPXD6GB2Dnf2oH3qOf5txqgVAlx0hnIkkDXxlhJ1L1pb5iZPFp/cib1hYfyGXz8p4IL8H0dT4c4DgX4pLKXTYDm5p8QcwSV',
    'bm_mi': '9D8B70A723675655C3CB9B89A93201F2~2UApwKhBkhGEkI+UmIh94M8Y6i/par6pUow8wkjtRZk11YsF6q2NM7F2hASBTFSudD8zje7dJam90Izubq9g5xlVtSv/lHtzrDHzMU9a3ax9SC7xJdhzdjADyJPDe6Ma7vVxuJcxZ4vLr0oUVxP2mmpwcGONK1YtMaTOjetzif82JKc/l2c3OlNMbE9Dkkln2z8fYkARdoRfomPWCpxoSUL7xpMFCtRZuyc26lSe/K590Ut/qHUgVU8Wys+u2PJfxCwIee+26TJTQvEEqua7bt23aMW1W02oE72hy3kw8Y7Qsd6XBMnOiRxFiBCVe+9BjDZ4ra+7YeKhRkZ6x/plmg==',
    'wag_sid': 't00std5jsw7e8fk9umnwpkdw',
    'ak_bmsc': 'CCE95247B4021AF0CAE2E67DD7DCFFB117C2BE85CD35000009A34460B4C95267~plVFOYydc69D+XquM1AbdBnKiG0H1Fvudj8Pl6RQp5xIVHbVIwkKri9o97qi1S140SUn4aY9dYWWrE1ApFEMz0W4DlRHcwdIEQJKUodOgwFyRTRPnHM2CdWoCqYRWxFoKfKGOXSPhmzxRgDzsQxrcPoBSC0l4Iij9j9RVO99jDLvgwwfqPdMJk/Hu7F4at8v71mG6m3W4nLeWSjgH9fOMsCzRRQOMB5HZ1iG26sV0SrgXRruFHDOuOJmasgqbgSskLMAJrXxX5a+FQAXWFwTPDAA==',
    'rxvt': '1615113279613|1615110999547',
    'dtPC': "6$511479361_221h-vFKPHAROTLKUCWCIKBWUAGIOMAKFEMKRJ-0e6",
    'dtLatC': '3',
    'akavpau_walgreens': '1615112121~id=075e75052a3e962748c6e8cb8c23a49d',
    'bm_sv': 'F823ACC9109F017B0388485491CB0CD5~En53UjJgx+yXHLcdozj4Zpm7V8tGtc4SYCx/UEtmtR2o1qcuLNgppLcGRMiR3g+OZQT3lkblRa/phM6L2qtlBB77U5+JJcu5PjFx+C6vozIrqkxFI7F1MYhVyNfuyWQhJ/mUOdT8LycVGJGSMzc1hHJeiwiZqNYOCRcyMPhDj4k=',
    '_abck': 'F89A564A2E8570E3ACA6045EBB15E862~0~YAAQLfo7F2PGfu13AQAAupcqDAXxl9GxCSscVxEJ1oqiTjNcCyf53PeiJZyExNHGSH4S+Y2MdH9/sonKl0eU5NQHQJLuALPVYwm2kn++s7chHMmklDrhG/JXglgQoRDCuZqCvyzCG842SfwQlwaoDrc5KcW56NwFr39a+Ar5UdRiSsWHlsfwYLn/a8Ia5SUhv579V1bth+c397SEuQk4jwaSJqVTQyRMGz5ZXQtu8jvY/RXomtJqa0mwgPN65uvNBBXcBXNDFPqiPu3Vuumwn8iyk+Cb178erMmb+0wZR9RWTYI1akqsViNohPWxDv3uQLpa5bntBf1FKjQiAHHTvo783kHbSuHF9ICJfOMDMBHF3xvlVV91ff8tRYxMShzw83/DixrCZhsSAzOya7wqZtRl1Re07M9lNFhMRg==~-1~-1~-1',
}

headers = {
    'authority': 'www.walgreens.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not\\"A\\\\Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'x-xsrf-token': 'U3Kf34OPjj9fjQ==.cWLb+Zi9LtiKKSaeob+5tBweACmsflofhCfOOg7yZHM=',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://www.walgreens.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.walgreens.com/findcare/vaccination/covid-19/location-screening',
    'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8',
}

data = '{"serviceId":"99","position":{"latitude":'+str(nomi.query_postal_code(str(zipcode))['latitude'])+',"longitude":'+str(nomi.query_postal_code(str(zipcode))['longitude'])+'},"appointmentAvailability":{"startDateTime":"2021-03-08"},"radius":25}'

response = requests.post('https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability', headers=headers, cookies=cookies, data=data)

if(response.json()['appointmentsAvailable']):
  print("Appointment is available")
else:
  print("Appointment is not available")
