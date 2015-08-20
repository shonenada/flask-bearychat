import json

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
        """A decorator for registering a command handler.
        Example::

            @bearychat.command('hi')
            def hi(**kwargs):
                user_name = kwargs.get('user_name')
                return bearychat.response('Hi, %s' % user_name)

        :param command: the command to register.
        :param kwargs: extra args pass to the function.
        """
        def wrapper(func):
            self._funcs[command] = (func, kwargs)
            return func
        return wrapper

    def dispatch(self):
        """A flask view function which dispath the http request to
        matching registered command handler.
        Before using Flask-BearyChat, you should add url rule with this method
        as `view_func`.
        """
        data = json.loads(request.data)
        trigger_word = data.get('trigger_word')
        text = data.get('text')
        command = text[len(trigger_word) + 1:].split()
        if len(command) > 0:
            command = command[0]
        func, kwargs = self._funcs[command]
        kwargs.update(data)
        return func(**kwargs)

    dispatch.methods = ['POST']

    def repsonse(self, text, attachments=None):
        """Generate a response for BearyChat's outgoing robot.

        :param text: A text which going to response to robot.
        :param attachments: options attachements.
        """
        resp = OutgoingResponse()
        resp.set_text(text)
        if attachments is not None and isinstance(attachments, list):
            for each in attachments:
                resp.add_attachment(**each)
        return resp.make_response()
