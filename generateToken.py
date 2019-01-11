"""
title: generateToken
author: sxv3240
date: 1/11/2019 11:02 AM
"""


import requests
import json
import os
import config


data = [
  ('grant_type', 'client_credentials'),
]
url = 'https://master-data-security.apps-np.homedepot.com/security/oauth/token'
def newToken():
    try:
        response = requests.post(url,
                         data=data,
                         auth=
                            (
                             config.AUTH_CLIENT_ID,
                             config.AUTH_CLIENT_SECRET
                            )
                         )
        response_json =response.json()

        token = response_json["access_token"]
        head = {'Authorization': 'Bearer ' + token}

        #print("Got Token!", response_json["access_token"])
        #print("Got Token!\n", head)
        print("Got Token!")
        return head

    except:
        print("Error with Token")
        return("Error with Token\n")

#print(response.content)
#print(response.json())
#print(json.dumps(response.json(), indent=4))

if __name__ == '__main__':
    newToken()