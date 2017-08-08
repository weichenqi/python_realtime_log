#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2017-07-24 13:59 
# @Author  : George Wei (weichenqi@gmail.com)
# @Link    : http://weichenqi.com
# @Version : 
from websocket_server import WebsocketServer


# Called when a client sends a message
def message_received(client, server, message):
	if len(message) > 0:
		message = message[0:]
        server.send_message_to_all(str(client['address'])+message)
	print("Client(%s) said: %s" % (client['address'], message))


# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])

PORT=8000
server = WebsocketServer(PORT,host='0.0.0.0')
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()