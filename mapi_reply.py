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
        self.is_active = True  # 默认插件是激活状态
        self.bot_name = config.get('bot_name')  # 从配置文件读取机器人名字

    def did_receive_message(self, event: Event):
        if event.message.is_group:
            sender_id = event.message.sender_id
            message_content = event.message.content
            is_at_bot = self.bot_name in message_content  # 检查消息是否@了机器人
            is_at_other = "@" in message_content and self.bot_name not in message_content  # 检查消息是否@了其他人

            # 特殊命令处理
            if sender_id in self.user_replies:
                if "停止拍马屁" in message_content:
                    self.is_active = False
                    reply_text = "🤐好的老板"  # 添加回复消息
                    text_reply = Reply(ReplyType.TEXT, reply_text)
                    event.reply = text_reply
                    event.bypass()  # 防止消息被多个插件处理
                    return
                elif "开始拍马屁" in message_content:
                    self.is_active = True
                    reply_text = "🤩中!!!"  # 添加回复消息
                    text_reply = Reply(ReplyType.TEXT, reply_text)
                    event.reply = text_reply
                    event.bypass()  # 防止消息被多个插件处理
                    return

            # 如果插件是非激活状态，则不处理消息
            if not self.is_active:
                return

            # 获取用户配置
            user_config = self.user_replies.get(sender_id, {})
            keywords = user_config.get('keywords', [])
            reply_texts = user_config.get('replies', [])

            # 检查是否满足回复条件
            if user_config and reply_texts:
                should_reply = False
                # 特定成员发送了包含关键字的消息，且没有@其他人
                if keywords and any(keyword in message_content for keyword in keywords) and not is_at_other:
                    should_reply = True
                # 消息中@了机器人，并且内容包含关键字
                elif is_at_bot and any(keyword in message_content for keyword in keywords):
                    should_reply = True

                # 回复逻辑
                if should_reply:
                    reply_text = random.choice(reply_texts)
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
