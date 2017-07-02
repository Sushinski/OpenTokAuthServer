# OpenTokAuthServer
Simple OpenTok Authorization django-based server for Android video-chat example application

This Django-based authorization server uses Tokbox (https://tokbox.com) server-api for generating video/audio chat session keys.
Server generates keys for relayed paired connections using free Tokbox account. It used by Android video/audio chat demo application
(https://github.com/Sushinski/TokBoxChat).

To adjust it reassign TEST_API_KEY and TEST_API_SECRET variables ones takem from own account, re-set wsgi virtualenv initialization
(or use djago test serv).
