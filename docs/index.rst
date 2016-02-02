.. Flask-BearyChat documentation master file, created by
   sphinx-quickstart on Wed Jan 27 12:38:40 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Flask-BearyChat's documentation!
===========================================

**Flask-BearyChat** is a Flask Extension to help you work with `BearyChat <https://bearychat.com>`_.


Installation
------------

You can install `Flask-BearyChat` with `pip` or `easy_install`::

    $ pip install flask-bearychat

    $ easy_install flask-bearychat


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


API References
--------------

.. toctree::
   :maxdepth: 2

   bearychat
