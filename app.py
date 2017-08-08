#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2017-07-24 13:59
# @Author  : George Wei (weichenqi@gmail.com)
# @Link    : http://weichenqi.com
# @Version :
from __future__ import print_function
import subprocess
from websocket import create_connection

r_user = "root"
r_ip = "ip"
r_port = port
r_log = log_dir

ws_server = "ws://127.0.0.1:8000/"

cmd = "/usr/bin/ssh -p {port} {user}@{ip} /usr/bin/tailf {log_path}".format(user=r_user,ip=r_ip,port=r_port,log_path=r_log)

def tailfLog():
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print('连接成功')
    ws = create_connection(ws_server)
    while True:
        line = popen.stdout.readline().strip()
        if line:
            ws.send(line)
        print(ws.recv_data())


if __name__ == '__main__':
    tailfLog()