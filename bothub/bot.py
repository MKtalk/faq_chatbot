# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.messages import Message 


class Bot(BaseBot):

    def handle_message(self, event, context):
        message = event.get('content')
        menu = self.get_project_data().get('keyboard').split(',')

        if message == '/start':
            msg = Message(event).set_text('Start Message')
            for item in menu:
                msg.add_keyboard_button(item)
            self.send_message(msg)

        elif message in menu:
            self.auto_response(event, message)

        else:
            self.send_message('This feature is not supported.')

    def auto_response(self, event, message):
        answer = self.get_project_data().get(message)
        msg = Message(event).set_text(answer.get('answer'))
        if answer.get('link'):
            msg.add_url_button(answer.get('title'), answer.get('link'))

        self.send_message(msg)
        
        
