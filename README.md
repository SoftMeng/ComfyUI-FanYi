# ComfyUI_FanYi

## 功能简述

一个简单的中英文翻译，使用的百度翻译(机器翻译).

## 使用图例

### 申请百度翻译

在百度翻译官网申请翻译API：

官网地址：https://api.fanyi.baidu.com/

![fanyi2.png](image%2Ffanyi2.png)

### 修改配置

在[fanyi.py](fanyi.py)中修改如下内容：

```shell
# Set your own appid/appkey.
appid = 'xxxxx'
appkey = 'xxxxxxx'
```

### Node使用

![demo.png](image%2Fdemo.png)

## 工作流举例

SDXL模型下载地址(欢迎点赞点关注): https://www.liblib.art/modelinfo/5913fb0765ce4a4ba210cb1c898df276
工作流文件（直接拖拽到ComfyUI的页面里即可）: [workflow.json](workflow.json)


## For More

### ComfyUI
1. 将中文翻译英文：https://github.com/SoftMeng/ComfyUI-FanYi
2. 从图片提取自然语言：https://github.com/SoftMeng/ComfyUI_ImageToText
3. 随机生成提示词：https://github.com/SoftMeng/ComfyUI-Prompt
4. 通过HTML模版制作AI海报：https://github.com/SoftMeng/ComfyUI_Mexx_Poster
5. 通过图片模版制作AI海报：https://github.com/SoftMeng/ComfyUI_Mexx_Image_Mask
6. Java工程调用ComfyUI生成AI图片（含全自动图片馆）：https://github.com/SoftMeng/comfy-flow-api
### Stable Diffusion WebUI
1. 随机生成提示词：https://github.com/SoftMeng/stable-diffusion-prompt-pai
### Fooocus
1. 汉化：https://github.com/SoftMeng/Fooocus-zh
### 其他
2. 视频会议：https://github.com/SoftMeng/vue-webrtc