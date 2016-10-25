#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from slackclient import SlackClient
import configs

sc = SlackClient(configs.slack['token'])

sc.api_call(
	"chat.postMessage", 
	channel=configs.slack['channel'], 
	text='Good morning :sparkles: \nHere is your daily _Package Version_ report:', 
	username=configs.slack['username'], 
	icon_emoji=':rooster:'
)

message = ""

for repositoryName, repositoryPath in configs.repositories.items():
	r = requests.get(repositoryPath)

	message += '*' + repositoryName + '*\n';
	
	if r.status_code != 200 :
		message += "_Error " + str(r.status_code) + " - Failed retrieving repository._\n"
		continue

	try:
		data = r.json()
	except:
		message += "_Error " + str(r.status_code) + " - Failed retrieving JSON data from repository._\n"
		continue


	for package in configs.packages:
		message += '`' + package + '` : '

		try:
			message += '`' + data['dependencies'][package] + '`\n'
		except KeyError:
			message += "_Unable to find requirement in composer.json file._\n"


sc.api_call(
    'chat.postMessage', 
    channel=configs.slack['channel'], 
    text=message,
    username=configs.slack['username'], 
    icon_emoji=':rooster:'
)	

