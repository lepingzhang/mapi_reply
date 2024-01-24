import os
import json
import random
from plugins import register, Plugin, Event, Reply, ReplyType

@register
class MapiReply(Plugin):
    name = 'mapi_reply'

    def __init__(self, config: dict):
        super().__init__(config)
        # 配置文件中的user_replies字段应该是一个字典，键为用户ID，值为回复列表
        self.user_replies = config.get('user_replies', {})

    def did_receive_message(self, event: Event):
        sender_id = event.message.sender_id
        # 检查消息发送者是否在user_replies字典的键中
        if sender_id in self.user_replies:
            # 如果是，从该用户的回复列表中随机选择一个回复
            reply_text = random.choice(self.user_replies[sender_id])
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
