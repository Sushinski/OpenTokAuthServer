from django.shortcuts import render
import json
from django.http import JsonResponse


# Create your views here.
def session_view(request):
    if request.method == 'GET':
        responce = dict()
        responce['apiKey'] = r'45900062'
        responce['sessionId'] = r'2_MX40NTkwMDA2Mn5-MTQ5ODI0ODYyMzI1MH5GcTh4RWhtSnVZdzM5R0gzSmFIa3dLblR-fg'
        responce['token'] = r'T1==cGFydG5lcl9pZD00NTkwMDA2MiZzaWc9MGI4MGE0MjY0OGFjYmI2ZTkxMjA1ZmIzYjQ1YjhjMmI3YmUzYTRiZjpzZXNzaW9uX2lkPTJfTVg0ME5Ua3dNREEyTW41LU1UUTVPREkwT0RZeU16STFNSDVHY1RoNFJXaHRTblZaZHpNNVIwZ3pTbUZJYTNkTGJsUi1mZyZjcmVhdGVfdGltZT0xNDk4MjQ4NzA3Jm5vbmNlPTAuOTI0MjMxMDUyNTI1NzI5MyZyb2xlPW1vZGVyYXRvciZleHBpcmVfdGltZT0xNTAwODQwNzA0'
        return JsonResponse(responce)
    else:
        return None
