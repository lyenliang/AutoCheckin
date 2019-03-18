#!/usr/bin/env python3

import requests
import re
import os

# package contains the login credential
package = os.getenv('package')

# checkin to get 1 point
def checkin():
    headers = {
        'Host': 'api.feebee.com.tw',
        'package': package,
        'user-agent': 'android-prod-release-v2.7.2-2017071140'
    }
    # print(headers)
    session = requests.Session()
    session.headers.update(headers)

    resp = session.post('https://api.feebee.com.tw/v2/checkin')
    print('response: ' + str(resp.text))

if __name__ == '__main__':
    checkin()