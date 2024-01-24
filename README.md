# wechat-gptbot 马屁精回复插件

本项目作为 `wechat-gptbot` 插件，可以根据用户id回复马屁。

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
  "name": "mapi_reply",
  "user_replies": {
    "wxid_1234567890": ["👍"]
  }
}
```

### 3. 停止与开启
默认开启，发送`停止拍马屁`以及`开始拍马屁`关闭或开启，可修改触发词以及回复内容。
