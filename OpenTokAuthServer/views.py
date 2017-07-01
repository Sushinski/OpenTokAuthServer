import uuid
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from OpenTokAuthServer.models import Connection, SessionKeys
from opentok import OpenTok, MediaModes

TEST_API_KEY = r'45900062'
TEST_API_SECRET = r'd4c973383d8f9eca272a89e31be614dbd07e60c3'


def session_new(request, app_key):
    if request.method == 'GET':
        responce = dict()
        # try to get pending client`s keys
        conn_obj = Connection.objects.filter(connections__lt=Connection.ALLOWED_CONNECTIONS).last()
        if conn_obj:
            responce['apiKey'] = conn_obj.session_key.api_key
            responce['sessionId'] = conn_obj.session_key.session_id
            responce['token'] = conn_obj.session_key.token
            if uuid.UUID(app_key) != conn_obj.opener_app_key:
                conn_obj.connections += 1
            conn_obj.save()
        else:  # to get: new keys
            opentok_ses = OpenTok(TEST_API_KEY, TEST_API_SECRET)
            session = opentok_ses.create_session(media_mode=MediaModes.relayed)
            responce['apiKey'] = TEST_API_KEY
            responce['sessionId'] = session.session_id
            responce['token'] = session.generate_token()
            new_ses_keys = SessionKeys()
            new_ses_keys.api_key = responce['apiKey']
            new_ses_keys.session_id = responce['sessionId']
            new_ses_keys.token = responce['token']
            new_ses_keys.save()
            new_con = Connection()
            new_con.session_key = new_ses_keys
            new_con.connections = 1
            new_con.opener_app_key = app_key
            new_con.save()
        return JsonResponse(responce)
    else:
        return None


@csrf_exempt
def session_delete(request, session_id):
    if request.method == 'DELETE':
        delete_session(session_id)
        return HttpResponse(status=200)
    else:
        return None


def delete_session(session_id):
    if session_id:
        conn_obj = Connection.objects.filter(session_key__session_id=session_id)
        if conn_obj:
            conn_obj.delete()

