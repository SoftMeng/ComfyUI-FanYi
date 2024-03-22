import requests
import random
import json
from hashlib import md5

# Set your own appid/appkey.
appid = 'xxxxx'
appkey = 'xxxxxxx'

# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
from_lang = 'zh'
to_lang =  'en'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path

# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

class ComfyUI_FanYi:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_positive": ("STRING", {"default": "专业摄影，使用富士胶片Provia 400X拍摄的RAW照片，HD，HDR，细节纹理，自然皮肤，生动的颜色，18岁的中国女孩，晚上，穿着连帽衫，户外，", "multiline": True}),
                "log_prompt": (["No", "Yes"], {"default":"Yes"}),
            },
        }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('text_positive',)
    FUNCTION = "fanyi"
    OUTPUT_NODE = True
    CATEGORY = "ComfyUI_Mexx"

    def fanyi(self, text_positive, log_prompt):
        salt = random.randint(32768, 65536)
        sign = make_md5(appid + text_positive + str(salt) + appkey)

        # Build request
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': appid, 'q': text_positive, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

        # Send request
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()

        if log_prompt == "Yes":
            print(f"中文: {text_positive}")
            print(json.dumps(result, indent=4, ensure_ascii=False))

        en = result["trans_result"][0]["dst"]
        if log_prompt == "Yes":
            print(f"英文: {en}")
        return en


NODE_CLASS_MAPPINGS = {
    "ComfyUI_FanYi": ComfyUI_FanYi
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_FanYi": "ComfyUI_FanYi"
}
