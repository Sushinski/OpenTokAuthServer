from django.http import JsonResponse
from OpenTokAuthServer.models import Connection, SessionKeys

TEST_TOKEN = r'T1==cGFydG5lcl9pZD00NTkwMDA2MiZzaWc9MGI4MGE0MjY0OGFjYmI2ZTkxMjA1ZmIzYjQ1YjhjMmI3YmUzYTRiZjpzZXNzaW9uX2lkPTJfTVg0ME5Ua3dNREEyTW41LU1UUTVPREkwT0RZeU16STFNSDVHY1RoNFJXaHRTblZaZHpNNVIwZ3pTbUZJYTNkTGJsUi1mZyZjcmVhdGVfdGltZT0xNDk4MjQ4NzA3Jm5vbmNlPTAuOTI0MjMxMDUyNTI1NzI5MyZyb2xlPW1vZGVyYXRvciZleHBpcmVfdGltZT0xNTAwODQwNzA0'
TEST_SESSION_ID = r'2_MX40NTkwMDA2Mn5-MTQ5ODI0ODYyMzI1MH5GcTh4RWhtSnVZdzM5R0gzSmFIa3dLblR-fg'
TEST_API_KEY = r'45900062'


def session_view(request):
    if request.method == 'GET':
        responce = dict()
        # try to get pending client keys
        conn_obj = Connection.objects.filter(connections__lt=Connection.ALLOWED_CONNECTIONS).last()
        if conn_obj:
            responce['apiKey'] = conn_obj.session_key.api_key
            responce['sessionId'] = conn_obj.session_key.session_id
            responce['token'] = conn_obj.session_key.token
            conn_obj.connections += 1
            conn_obj.save()
        else:  # to get: new keys
            responce['apiKey'] = TEST_API_KEY  # todo get real api key
            responce['sessionId'] = TEST_SESSION_ID  # todo real ses id
            responce['token'] = TEST_TOKEN  # todo real token
            new_ses_keys = SessionKeys()
            new_ses_keys.api_key = responce['apiKey']
            new_ses_keys.session_id = responce['sessionId']
            new_ses_keys.token = responce['token']
            new_ses_keys.save()
            new_con = Connection()
            new_con.session_key = new_ses_keys
            new_con.connections = 1
            new_con.save()
        return JsonResponse(responce)
    else:
        return None
