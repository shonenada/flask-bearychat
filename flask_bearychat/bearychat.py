import json
from functools import wraps

from flask import request, Response


class OutgoingResponse(object):

    ATTACHMENT_FILEDS = ('title', 'text', 'color', 'images')

    def __init__(self):
        self.text = None
        self._attachments = []

    def set_text(self, text):
        self.text = text

    def add_attachment(self, **kwargs):
        attachment = {k: v for k, v in kwargs if k in self.ATTACHMENT_FILEDS}
        self._attachments.append(attachment)

    def make_response(self):
        payload = {
            'text': self.text,
            'attachment': self._attachments,
        }
        return Response(json.dumps(payload),
                        content_type="application/json")


class BearyChat(object):

    def __init__(self):
        self._funcs = {}

    def command(self, command, **kwargs):
        @wraps
        def wrapper(func):
            self._funcs[command] = (func, kwargs)
            return func
        return wrapper

    def dispatch(self):
        data = request.data
        trigger_word = data.get('trigger_word')
        text = data.get('text')

        command = text[len(trigger_word):]

        func, kwargs = self._funcs[command]
        kwargs.update(data.to_dict())
        return func(**kwargs)

    def repsonse(self, text, attachments=None):
        resp = OutgoingResponse()
        resp.set_text(text)
        if attachments is not None and isinstance(attachments, dict):
            for each in attachments:
                resp.add_attachment(**each)
        return resp
