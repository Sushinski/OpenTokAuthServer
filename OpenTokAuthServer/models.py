from django.db import models


class SessionKeys(models.Model):
    _id = models.AutoField(primary_key=True)
    api_key = models.TextField()
    session_id = models.TextField()
    token = models.TextField()


class Connection(models.Model):
    ALLOWED_CONNECTIONS = 2
    _id = models.AutoField(primary_key=True)
    session_key = models.ForeignKey(SessionKeys, blank=False, null=False)
    connections = models.IntegerField(default=0)
    opener_app_key = models.UUIDField(default="")
