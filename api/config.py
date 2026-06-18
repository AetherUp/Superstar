# -*- coding: utf-8 -*-
class GlobalConst:
    AESKey = "u2oh6Vu^HWe4_AES"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Sec-Ch-Ua": '"Chromium";v="131", "Google Chrome";v="131", "Not=A?Brand";v="24"',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }
    COOKIES_PATH = "cookies.txt"
    VIDEO_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer": "https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2024-1128-1450",
        "Origin": "https://mooc1.chaoxing.com",
        "Host": "mooc1.chaoxing.com",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    AUDIO_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer": "https://mooc1.chaoxing.com/ananas/modules/audio/index_new.html?v=2024-0428-1705",
        "Origin": "https://mooc1.chaoxing.com",
        "Host": "mooc1.chaoxing.com",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    THRESHOLD = 3

    @classmethod
    def set_cookies_path(cls, path: str):
        """允许外部设置 Cookie 文件路径（多账号运行时使用）"""
        cls.COOKIES_PATH = path
