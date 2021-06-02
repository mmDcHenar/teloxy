from django.http import JsonResponse, HttpResponse
from telethon.sync import TelegramClient as Tc
from re import findall

def test(req):
    return HttpResponse('test!')

def home(req):
    return HttpResponse('Hello World!')


def download(req):
    android = {'Current_version': '0.7.1',
               'Info': 'bugs fixed',
               'Download_link': 'http://rozup.ir/download/3357262/Teloxy-1.0-armeabi-v7a-release-unsigned.apk',
               'Telegram_link': 'tg://resolve?domain=teloxy_app&post=4'}

    return JsonResponse({'android': android})


def proxy(req):
    cli = Tc('cli', 1029913, 'c89b062fb1b8ef18bc24a1e0c893f2ec').start() # , proxy=('socks5', '127.0.0.1', 9050))
    hack_proxy = cli.get_messages(cli.get_entity('hack_proxy'), limit=10) 
    channels = [hack_proxy]
    mtp_roto = cli.get_messages(cli.get_entity('MTP_roto'), limit=10)
    channels.append(mtp_roto)
    counter = 0
    result = {}
    for channel in channels:
        for msg in channel:
            proxies = findall("(?:\s|\n|)((?:https://t\.me/|tg://)proxy\?server=.+?&port=\d+?&secret=.+)(?:\s|\n|)", msg.text)
            for proxy in proxies:
                if proxy not in list(result.values()):
                    result[str(counter)] = proxy
                    counter += 1
    cli.disconnect()
    return JsonResponse(result)

