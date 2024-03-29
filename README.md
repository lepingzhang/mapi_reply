# wechat-gptbot 马屁精回复插件

本项目作为 `wechat-gptbot` 插件，可以根据用户id回复马屁。

#### 工作机制
1. 特定成员（通过ID配置）发送的消息，如果包含关键字，无论是否@机器人，都会回复。


2. 当消息中@了机器人，且消息内容符合关键字，进行回复。


3. 非特定成员发送的消息，无论是否@机器人，如果内容符合关键字，都不回复。


4. 特定成员@其他人发送的消息，即使内容符合关键字，也不回复。

## 安装指南

### 1. 添加插件源
在 `plugins/source.json` 文件中添加以下配置：
```
{
  "keyword_reply": {
    "repo": "https://github.com/lepingzhang/mapi_reply.git",
    "desc": "群聊拍马屁"
  }
}
```

### 2. 插件配置
在 `config.json` 文件中添加以下配置：
```
{
  "plugins": [
    {
      "name": "mapi_reply",
      "user_replies": {
        "wxid_1234567890": { //指定群内某个id，支持多个
          "replies": ["OK"], //设置机器人回复内容
          "keywords": ["大家", "所有人", "各位同事"] //设置机器人匹配关键字，留空则全部消息都会回复
        }
      }
    }
  ]
}
```

### 3. 停止与开启
插件默认开启，需要配置了id的人发送`停止拍马屁`以及`开始拍马屁`关闭或开启(可修改触发词以及回复内容)。
