import os
import time
import json
import fun


this = {}

while True:
    print(fun.color("RED","Команды:"))
    print(fun.color("BLUE", "   0)Current akkaunt\n   1)Choice akkaunt.\n   2)Get mobile guard code."))
    posy = input()
    if posy == "0":
        fun.clean()
        if this:
            print(fun.color("GREEN",f"Current akkaunt:\n   id:"), fun.color("RED",this['id']), fun.color("GREEN","login:"), fun.color("WHITE",this['login']) )
        else:
            print(fun.color("RED","Not selected accaunt."))
    elif posy == "1":
        fun.clean()
        mafiles = os.listdir("mafiles")
        print(fun.color("WHITE","Choice accaunt."))
        for akk in range(len(mafiles)):
            with open(f"mafiles/{mafiles[akk]}","r",encoding="utf-8") as f:
                data = json.load(f)
            print(fun.color("GREEN",f"   {akk+1:03}) id:"), fun.color("VIOLET",data['Session']['SteamLogin'].split('%')[0]) ,fun.color("GREEN","login :"), fun.color("WHITE",data['account_name']))
        number = int(input())
        while not  (0 < number <= len(mafiles) + 1):
            print(fun.color("RED","ERROR NUMBER!"))
            number = int(input())
        with open(f"mafiles/{mafiles[number-1]}","r",encoding="utf-8") as f:
            data = json.load(f)
            this['login'] = data['account_name']
            this['id'] = data['Session']['SteamLogin'].split('%')[0]
            this['shared_secret'] = data['shared_secret']
            this['identity_secret'] = data['identity_secret']
            fun.clean()
        print(fun.color("GREEN","Accaunt was load."))
    elif posy == "2":
        fun.clean()
        if this:
            print(fun.color("YELLOW","Your code:"), fun.color("WHITE",fun.generate_auth_code(this['shared_secret'])))
            time.sleep(2)
        else:
            print(fun.color("RED","Not selected accaunt."))
    else:
        fun.clean()
        print(fun.color("RED","ERROR COMMAND!."))
