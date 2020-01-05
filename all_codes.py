import os
import json
import fun
import time

akkaunts = ["star"]
akkaunts_codes = []

while True:
    if akkaunts_codes != [fun.generate_auth_code(i) for i in akkaunts]:
        fun.clean()
        akkaunts = []
        akkaunts_codes = []
        mafiles = os.listdir("mafiles")
        print(fun.color("WHITE","Your akkaunts:"))
        for akk in range(len(mafiles)):
            with open(f"mafiles/{mafiles[akk]}","r",encoding="utf-8") as f:
                data = json.load(f)
            print(fun.color("BLUE", f"{akk+1:03})"),  fun.color("GREEN","login:"),fun.color("WHITE",data['account_name'].ljust(30," ")),fun.color("GREEN","code:"),fun.color("YELLOW",fun.generate_auth_code(data['shared_secret'])))
            akkaunts.append(data['shared_secret'])
            akkaunts_codes.append(fun.generate_auth_code(data['shared_secret']))
    else:
        time.sleep(1)
