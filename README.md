# Bitcoin Price Alarm

## Install requirements

`sudo apt-get install python3-pip`

`pip3 install -r requirements.txt`


This simple script gets Bitcoin prices from [Coindesk](https://www.coindesk.com/price/bitcoin) and alarms on your price that you have set.

For receiveing alarm on Slack you should replace your slack's webhook with `YOUR_SLACK_HOOK`

`SLACK_URL='YOUR_SLACK_HOOK'`

If you don't have webhook, please follow this instructions:

[https://api.slack.com/messaging/webhooks](https://api.slack.com/messaging/webhooks)

Now you can set your price on `YOUR_PRICE` variable (56 means $56,000)

`YOUR_PRICE=56`

## Usage

`python3 bitcoin_price.py`