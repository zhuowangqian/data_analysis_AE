# coding = utf-8
import crawles
import re
import httpx
import utils


def get_ck():
    url = 'https://www.zhipin.com/hangzhou/'
    res = httpx.request('GET', url)
    cookies = str(res.cookies)
    # cookie = re.findall('', cookies)
    # token = re.findall(r"var _CSRF = '(.*?)';", res.text)
    # print(res.text)
    # print(cookie)
    return cookies


print(get_ck())
# cookie = get_ck()
# for index, i in enumerate(cookie):
#     print(index, i)
# cookie = ';'.join(cookie)
# print(cookie)

# import the requests library

# str1 = str + str(i)
# print(str)


def index():
    c, t = get_ck()
    url = 'aHR0cDovL3d3dy56am1hemhhbmcuZ292LmNuL2hkamxwdC9sZXR0ZXIvcHViTGlzdA=='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': t,
        'Cookie': 'XSRF-TOKEN={};szxx_session={}'.format(t, c)
    }
    data = {
        "offset": "0",
        "limit": "20",
        "site_id": "759010",
    }
    res = httpx.post(url, data=data, headers=headers)
    if res.status_code == 200:
        print(res.text)
    else:
        print('请求错误')


# index()

url = 'https://www.aliexpress.us/item/3256803817028291.html'

cookies = {
    'aep_common_f': 'S/MVm6T6yJbDgpwuZLp0+mepUxJIsAcSCB6JXoNYXlM/BGzIEblZbw==',
    '_ga_save': 'yes',
    'cna': 'A0NfHbGscV4CAXWTa0ou3K3W',
    '_gcl_au': '1.1.313344858.1692420089',
    '_ym_uid': '1692420095424565094',
    '_ym_d': '1692420095',
    'x_router_us_f': 'x_alimid=4465986603',
    'xman_us_t': 'x_lid=us2865472608lydae&sign=y&rmb_pp=zhuowangqian0522@gmail.com&x_user=ReJ5rJMvHyqJrynt4f/Ac+We1v6HGskbxWxS8HkIkY8=&ctoken=ruig_stusgyn&l_source=aliexpress',
    'acs_usuc_t': 'acs_rt=edbf4ffd62fd4a42ac5a3e024daa3555&x_csrf=f0ofx3tw7a7u',
    'sgcookie': 'E100XCBSYlVPSFGBGmXmiUfPAhxIhZ57W2bf6CForczSWY3jDCxM2OIyKWTGmLSjDYJtrtjTAlrV0G4bQu4l/sblnQoqYjng+OpIrxj8J4q/iXI=',
    'xman_f': 'mPANTRcajMWUSa/H5SdBcoYu1MmBlgm43gSBdQ8/cHJX6+O0EjaJTIb+jUELxvn0UJXCe9dvUt08bURrbsAtIx45o6a1IM7i7lpAji7bK1O4mclYygLdDa9pD8eqZ+7NCnzes7yFaoGIaEByN819xPRJX0RsyWHBGLHbxu2U36wCiBbR02P8jhKeHcRoG4bEE2SGV6QoWhd4vZTYL2/TYlWZ2uB/mvwxgRRpBKTAHATsFvTxZseZ+T8oz86cnyyXjbCg2+J/zkRAFyHkQKMauyt/zd1r3feTFmLSezQpfkFYjB7ZxsDNy5shkW5gAAxLled93bYp2pv0VbwYAEtmI7dBTT2IrA1joNDKD0f7stLMwL/X+R58XXXGZF+XyRSF8EauTRpzGpq2WP/0eMy6MrKp5Fg0eYVIA/VfaST6y3fPFNY7DyhKMZ08fbikgq9e',
    'intl_locale': 'en_US',
    'x5sec': '7b22733b32223a2237323031333563363639333761613938222c2261656272696467653b32223a22623236333965383531356264393032346237303034326530643165336637346143502b74684b6747454d5377353441444d4e4c616d6266372f2f2f2f2f77464141773d3d227d',
    'XSRF-TOKEN': 'd06f77f2-6a2a-4771-adce-9f2a99ff352a',
    'aep_history': 'keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%093256803817028291',
    'xman_us_f': 'zero_order=y&x_locale=en_US&x_l=0&x_user=US|wangqian|Zhuo|ifm|4465986603&x_lid=us2865472608lydae&x_c_chg=1&x_c_synced=1&x_as_i=%7B%22aeuCID%22%3A%22388e78b777464d3496caa07e75368ae8-1694569476740-04735-_Dnq8dIv%22%2C%22af%22%3A%224176642736%22%2C%22channel%22%3A%22AFFILIATE%22%2C%22cookieCacheEffectTime%22%3A1694569784744%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%2C%22pid%22%3A%224176642736%22%2C%22tagtime%22%3A1694569476740%7D&acs_rt=6837107a988a41f2aeefd19712beff8a',
    'xlly_s': '1',
    '_m_h5_tk': '545c29dd7cf198392f36feafdcb66113_1694572316773',
    '_m_h5_tk_enc': '608aa27437742c3fe4d085c8a8b32740',
    'cto_bundle': 'n-ryaV8zT3ROck04NkZkUjNiWXZRaUFkQUpYclkwb2lRUDZjc0hReVY0emw1SVdLS1cwSHB4em9Yd2NUUlpMVjhMb3F4WnpBeXZyUFhVMzR5RTh4UGVaeVQzM1ZJS0NCd1hkZHNMTElXOVdvZTh0NEJ3Nnk3ZjJ3ZHVGVVBFNW5YcmNGVmxrSGQxSHA0JTJCUko2Tmg3dk9wcG5BTWhWcDQ5RVJKUmlYbEt0SEtqN0x3cyUzRA',
    '_gid': 'GA1.2.979277347.1694570398',
    '_gat': '1',
    '_ga_VED1YSGNC7': 'GS1.1.1694570397.2.0.1694570397.60.0.0',
    '_ga': 'GA1.1.2000821855.1692419935',
    'tfstk': 'd2ReSAAebXhFXaBkEt5yusou--1disnbZQs5rUYlRMj3OWZkQ3tMRpN5NTVyrUBudM1naaxXbMVhEw2gSaQ8qwVhZO4Gzw7hEQsWa45p1pN5ADCyrn1rcmGjGeLdM_mjcHaHJeI6kCbrGjTpJdjBU9hjJ6EIQToBnWZEnOiDPGAQG65068Ylb7V4kwWhRjIaZ7ON8FScQGqRS3CewpruU9bO7igZ7eEPhxf..',
    'l': 'fBTfACbeN9STyUgkBOfwFurza77O_IRAguPzaNbMi9fP9w5w5-2OW1hjUxYeCnGVF6SvR3-WjmOpBeYBqnAgvByw31P7xyHmn_vWSGf..',
    'isg': 'BC8v-1xRlqcaxpN6dhYZ1FxpvkM51IP2hSaJQUG86h6lkE-SSacZR2VCFoCu6Ftu',
    '_ym_isad': '1',
    '_ym_visorc': 'b',
    'JSESSIONID': '6711C4913E7E61CAA7F57A68572FEB09',
    'intl_common_forever': '0nXGlCyEkjhssfDrdp0X+cJwA8yxTLedoMTP6PjgwEKtDoSlPHPzaw==',
    'xman_t': '8KUtS3B7yCJNjciQ9Nj2yl2zlow5PPJa9kfjGXNedaJ2CVjyb31sofy5N7YsBMoCnu2yIZBpcWZj0QukT+efcLVE2Xwpmp2yjNsYcdO/rZOX38PwGYPG5xtiFyb3ey4mbRpQnHjrEQ5pnGpwTLTqMR3XHF6KdPkpqyDumu4nJNxDl1nu6WR0zIUsdis3IYyc1Qejk22D08X0RlRPfII9xjK6vhqDzqVkZ1YgTd5KA4D1lgRQg0XfzzSytVzeAT8zWBXbrJHjM+A3WCElsOC80CWQHvXf1oCd66Cv+kSRMN3rzXMU1GEqN0heJkgTeAiFJ2X2xQ9Vx7iRxS68Scqq2x9ggbThs9LUJrsLEH1V6eZ85HNr2Rrxz6EDGKk0mzBczLo25mS8G5ocOA3rnWsD+UhfWklkYcGec21BrsaAuuGu640AJPVFkTZfLguju8TJ31VnobbtnehFYcd3rp5O7LcG82s5FQPlHC+RVXVHz8ab3XFRS7yta9Fifa05Rl3nOqt0uL9kclGStBWvMM3lARv9PGf48xwboG/UeKXUAjyvON8xsHhe7hQDYdUqMCNnPwM0su03xu2YCU7Y+up21abtYaxr3/gQECeAktx+YpgTvJ00qZzekyLz5Bw+K6dGJydM2Rwor0Gt7FaAP6an7dFMAGorSrNfu4aH5bhUs/0SBNu29Sdursk3tbM2TntkSiy2aQT17e8SCY81B/QCJ3cftRSdPpcRBJtzRpLqj7/W9GxJHoGZQdTWFotApAnd25tRm+iqjYc=',
    'aep_usuc_f': 'site=usa&province=922873780000000000&city=922873786976000000&c_tp=USD&x_alimid=4465986603&isb=y&region=US&b_locale=en_US',
}

headers = {
    'authority': 'www.aliexpress.us',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'referer': 'https://www.aliexpress.us//item/3256803817028291.html/_____tmd_____/punish?x5secdata=xcXkClqpHilKpwNKv%2f5plHehqbV9VnaxMFEVTG0t42sa0n%2btnjopk5HAYxAR3dknmmq8somuFDQ81ASvun%2flPMDyMLL4MJgZuO1c%2f3UdQ3j4yzzhRYJISKZJLYWVghE%2fHUUZVQ%2fbH1Q1WXFn6xJ6amcLEVRT9Z9y1ZeFUufFo1Kyq70NY5okSQfEWq8HHogC37H%2b4yzRBb50r1%2fNH4k6NFBt%2bh5a3NUZQABfxiAA07fh2ngDP%2fGmNUT17dFhOLRAhu__bx__www.aliexpress.us%2fitem%2f3256803817028291.html&x5step=1',
    'sec-ch-ua': '\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '\"Windows\"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

params = {
    'spm': 'a2g0o.productlist.main.21.2e68443faTBOtJ',
    'algo_pvid': '39239cea-32a9-40e3-bc39-78b1415b3b75',
    'algo_exp_id': '39239cea-32a9-40e3-bc39-78b1415b3b75-10',
    'pdp_npi': '4@dis!USD!10.54!1.75!!!10.54!!@212c01e916945699168372436ef395!12000027707346066!sea!US!4465986603!AS',
    'curPageLogUid': 'qr3lTQ4jOv2T',
}

response = crawles.get(url, headers=headers, params=params, cookies=cookies)
# print(response.text)
