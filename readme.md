# Version Monitoring Chicken

The Version Monitoring Chicken is a friendly bot that will parse provided RAW dependency json files on Github or Bitbucket to retrieve configured package versions. It then reports back it's finding through a Slack private channel.

![alt text][screenshot]

[screenshot]: screenshot.png "Good morning!"

## Requirements

	pip install requests
	pip install slackclient

## Usage

### Configurations

In the `config-default.py` file:

1. Retrieve your Slack API token from `https://api.slack.com/web#authentication`
2. Enter the channel name you wish to post to (don't forget the `#` for channels, `@` for users)
3. Retrieve the *RAW* `json` urls you would like to parse and fill out the `repositories` configuration object
4. Save your changes as `config.py`

Note that if parsing *Composer* dependency files, you will need to replace `data['dependencies'][package]` to `data['require'][package]`.

### Scheduling the reports

You will need set up a CRON task that runs the `core.py` script periodically. 
I used Window's `Task Scheduler` to silently run this from my working station, but this can easily be setup using `crontab -e` on a Linux machine.

