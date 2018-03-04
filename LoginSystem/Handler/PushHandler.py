from tornado.websocket import WebSocketHandler

class PushHandler(WebSocketHandler):

    users = set()  # 用来存放在线用户的容器

    def open(self):
        self.users.add(self)  # 建立连接后添加用户到容器中

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        self.users.remove(self) # 用户关闭连接后从容器中移除用户
