# ComfyUI_FanYi

## 功能简述

一个简单的中英文翻译，使用的百度翻译.

## 使用图例

### 申请百度翻译

在百度翻译官网申请翻译API：

官网地址：https://api.fanyi.baidu.com/

![fanyi.png](image%2Ffanyi.png)

### 修改配置

在[fanyi.py](fanyi.py)中修改如下内容：

```shell
# Set your own appid/appkey.
appid = 'xxxxx'
appkey = 'xxxxxxx'
```

### Node使用

![node.png](image%2Fnode.png)

## 工作流举例

SDXL模型下载地址(欢迎点赞点关注): https://www.liblib.art/modelinfo/5913fb0765ce4a4ba210cb1c898df276
工作流文件（直接拖拽到ComfyUI的页面里即可）: [中文翻译的工作流.json](%E4%B8%AD%E6%96%87%E7%BF%BB%E8%AF%91%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%B5%81.json)