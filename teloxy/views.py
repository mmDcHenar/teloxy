from django.http import JsonResponse, HttpResponse
from telethon.sync import TelegramClient as Tc
from re import findall

def test(req):
    try:
        if req.GET['pass'] == 'mmdlov3':
            res = 'nice job!'
        else:
            res = 'nope!'
    except:
        res = 'nope!'
    return HttpResponse(res+'\n'+str(req.META['REMOTE_USER']))

def home(req):
    cli = Tc('cli', 1029913, 'c89b062fb1b8ef18bc24a1e0c893f2ec').start() # , proxy=('socks5', '127.0.0.1', 9050))
    msgs = cli.get_messages(cli.get_entity('hack_proxy'), limit=10)
    counter = 0
    result = {}
    for msg in msgs:
        proxies = findall("(?:\s|\n|)((?:https://t\.me/|tg://)proxy\?server=.+?&port=\d+?&secret=.+)(?:\s|\n|)", msg.text)
        for proxy in proxies:
            result[str(counter)] = proxy
            counter += 1
    cli.disconnect()
    return JsonResponse(result)

