from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings

import requests
# Create your views here.


def get_graph_token():
    url = settings.AD_URL

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

    data = {
        'grant_type': 'client_credentials',
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'scope': 'https://graph.microsoft.com/.default',
    }

    response = requests.post(url, headers=headers, data=data)
    json_response = response.json()
    return json_response


    # ----------------
    # user_upn = request.user.username
    # url = 'https://graph.microsoft.com/beta/users/' + user_upn + '?$select=Country,City'
    # ----------------

def login_successful(request):
    try:

        graph_token = get_graph_token()['access_token']

        url = 'https://graph.microsoft.com/v1.0/users/'+ request.user.username  # user_upn

        headers = {'Authorization': 'Bearer ' + graph_token, 'Content-Type': 'application/json'}

        response = requests.get(url, headers=headers)

        json_response = response.json()

        print(f'Display Name: {json_response["displayName"]}, Job Title: {json_response["jobTitle"]}, Mobile: {json_response["mobilePhone"]}, Office location: {json_response["officeLocation"]}')

        return HttpResponse(f'Hey {json_response["displayName"]}, login succesful.')

    except:
        return HttpResponse("Failed to read values from graph explorer.")
