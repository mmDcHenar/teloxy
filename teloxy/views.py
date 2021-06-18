from django.http import JsonResponse, HttpResponse
from telethon.sync import TelegramClient as Tc
from re import findall
from bs4 import BeautifulSoup
from requests import get

def test(req):
    return HttpResponse('test!')

def home(req):
    return HttpResponse('Hello World!')


def download(req):
    android = {'Current_version': '1.0',
               'Info': 'Released!',
               'Download_link': 'http://rozup.ir/download/3357262/Teloxy-1.0-armeabi-v7a-release-unsigned.apk',
               'Telegram_link': 'tg://resolve?domain=teloxy_app&post=4'}

    return JsonResponse({'android': android})


def proxy(req):
	url = "https://t.me/s/hack_proxy/"
	channel = requests.get(url).text
	soup = BeautifulSoup(channel, 'lxml')
	tgpost = soup.find_all('div', class_ ='tgme_widget_message')
	hack_proxy = []

	for content in tgpost:
		msg = content.find('div', class_ = 'tgme_widget_message_text')
		try:
			msgs.append(msg.text)
		except:
			pass

	channels = [hack_proxy]

	for channel in channels:
		for msg in channel:
			proxies = findall("(?:\s|\n|)((?:https://t\.me/|tg://)proxy\?server=.+?&port=\d+?&secret=.+)(?:\s|\n|)", msg)
			for proxy in proxies:
				if proxy not in list(result.values()):
					result[str(counter)] = proxy
					counter += 1
	return JsonResponse(result)

