Flask-BearyChat
===============

Flask-BearyChat is a Flask Extension to help you work with `BearyChat <https://bearychat.com>`_.

Installation
------------

::

    $ pip install flask-bearychat

Usage
-----

.. code-block:: python

    from flask import Flask
    from flask.ext.bearychat import BearyChat

    app = Flask(__name__)
    app.config['BEARYCHAT_TOKEN'] = 'token-from-bearychat-robot'
    app.config['BEARYCHAT_CALLBACK'] = '/hook'
    bearychat = BearyChat(app)

    @bearychat.command('hello')
    def list(**kwargs):
        username = kwargs.get('username')
        text = 'Hello, %s' % username
        return bearychat.response(text=text)

    if __name__ == '__main__':
        app.run()
