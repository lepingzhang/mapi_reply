import os
import json
import random
from plugins import register, Plugin, Event, Reply, ReplyType

@register
class MapiReply(Plugin):
    name = 'mapi_reply'

    def __init__(self, config: dict):
        super().__init__(config)
        self.user_replies = config.get('user_replies', {})
        # 新增一个过滤关键词配置
        self.filtered_keywords = config.get('filtered_keywords', [])

    def did_receive_message(self, event: Event):
        # 使用 event.message.is_group 来检查消息是否来自群聊
        if event.message.is_group:  # 使用 event.message.is_group
            sender_id = event.message.sender_id
            message_content = event.message.content  # 获取消息内容

            # 检查消息是否包含过滤关键词，如果包含，则不处理
            if any(keyword in message_content for keyword in self.filtered_keywords):
                return

            if sender_id in self.user_replies:
                reply_text = random.choice(self.user_replies[sender_id])
                text_reply = Reply(ReplyType.TEXT, reply_text)
                event.reply = text_reply
                event.bypass()  # 防止消息被多个插件处理
        # 如果不是群聊消息，插件不做处理

    def will_generate_reply(self, event: Event):
        pass

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "通过配置群聊id，随机回复特定用户的发言，并且可以设置不处理的关键词。"
