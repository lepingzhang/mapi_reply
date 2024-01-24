import os
import json
import random
from plugins import register, Plugin, Event, Reply, ReplyType

@register
class MapiReply(Plugin):
    name = 'mapi_reply'

    def __init__(self, config: dict):
        super().__init__(config)
        self.trigger_users = config.get('trigger_users', [])
        self.replies = config.get('replies', [])
        self.user_responses = self.load_user_responses()

    def load_user_responses(self):
        # 在这里，您可以定义一个JSON文件来存储触发用户和响应，或者直接在配置中设置
        return {user: self.replies for user in self.trigger_users}

    def did_receive_message(self, event: Event):
        if event.message.sender_id in self.user_responses:
            reply_text = random.choice(self.user_responses[event.message.sender_id])
            text_reply = Reply(ReplyType.TEXT, reply_text)
            event.reply = text_reply
            event.bypass()  # 防止消息被多个插件处理

    def will_generate_reply(self, event: Event):
        pass

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "通过配置群聊id，随机回复特定用户的发言。"
