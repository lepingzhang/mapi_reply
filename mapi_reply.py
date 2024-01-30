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
        self.is_active = True

    def did_receive_message(self, event: Event):
        if event.message.is_group:
            sender_id = event.message.sender_id
            message_content = event.message.content

            if sender_id in self.user_replies:
                if "停止拍马屁" in message_content:
                    self.is_active = False
                    reply_text = "🤐好的老板"
                    text_reply = Reply(ReplyType.TEXT, reply_text)
                    event.reply = text_reply
                    event.bypass()
                    return
                elif "开始拍马屁" in message_content:
                    self.is_active = True
                    reply_text = "🤩中!!!"
                    text_reply = Reply(ReplyType.TEXT, reply_text)
                    event.reply = text_reply
                    event.bypass()
                    return

            if not self.is_active:
                return

            user_config = self.user_replies.get(sender_id, {})
            keywords = user_config.get('keywords', [])
            reply_texts = user_config.get('replies', [])

            if user_config and reply_texts:
                if keywords and any(keyword in message_content for keyword in keywords):
                    reply_text = random.choice(reply_texts)
                    text_reply = Reply(ReplyType.TEXT, reply_text)
                    event.reply = text_reply
                    event.bypass()

    def help(self, **kwargs) -> str:
        return "通过配置群聊id，随机回复特定用户的发言。"

    def will_generate_reply(self, event: Event):
        pass

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass
