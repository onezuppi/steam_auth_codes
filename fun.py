import time
import hmac
import base64
import struct
import os 
from hashlib import sha1


def generate_auth_code(shared_secret: str, timestamp: int = None) -> str:
    if timestamp is None:
        timestamp = int(time.time())
    time_buffer = struct.pack('>Q', timestamp // 30)  # pack as Big endian, uint64
    time_hmac = hmac.new(base64.b64decode(shared_secret), time_buffer, digestmod=sha1).digest()
    begin = ord(time_hmac[19:20]) & 0xf
    full_code = struct.unpack('>I', time_hmac[begin:begin + 4])[0] & 0x7fffffff
    characters = '23456789BCDFGHJKMNPQRTVWXY'
    auth_code = ''
    for _ in range(5):
        full_code, i = divmod(full_code, len(characters))
        auth_code += characters[i]
    return auth_code

def clean():
    if "nt" in os.name:
        os.system("cls")
    else:
        os.system("clear")


def color(color:str, text:str):
    colors = {"BLACK":30,"RED": 31,"GREEN": 32,"YELLOW": 33,"BLUE":34,"VIOLET":35,"TURQUOISE":36,"WHITE":37}
    return f"\033[{colors[color] if colors.get(color) else colors['BLACK']}m{text}"
