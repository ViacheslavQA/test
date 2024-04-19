from datetime import datetime
import requests

SLACK_URL = "https://hooks.slack.com/services/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"
urls = ['https://freevpnplanet.com/',
        "https://freevpnplanet.com/blog/",
        "https://content.freevpnplanet.com/blog/",
        "https://content.freevpnplanet.com/ru/blog/",
        "https://content.freevpnplanet.com/",
        "https://planetvpnarab.com/",
        "https://planetvpnarab.com/blog/",
        "https://content.planetvpnarab.com/",
        "https://planetvpn.app/",
        "https://freevpnmentor.com/",
        "https://vpnly.com/",
        "https://blokirovki.net/",
        "https://vpncheckers.com/",
        "https://planet-vpn.ru/"]


def sites_availability(urls):
    result = ""
    date = datetime.today().strftime("%d.%m.%Y(%H:%M)")
    for url in urls:
        try:
            response = requests.get(url)
            print(url, response)
            if response.status_code != 200:
                send_result_to_slack(url, response.status_code)
            result += f"{response.status_code} - {url} - {date}\n"
        except Exception as ex:
            pass
    with open('result.txt', 'w') as file:
        file.write(result)


def send_result_to_slack(url: str, status_code: int) -> int:
    """"""
    date = datetime.today().strftime("%d.%m.%Y(%H:%M)")
    payload = {"blocks": [{"type": "section",
                           "text": {"type": "mrkdwn",
                                    "text": f":exclamation: Status code {status_code}  {date} \n URL : {url} "}}]}
    headers = {
        "content-type": "application/json",
    }

    response = requests.post(SLACK_URL, json=payload, headers=headers)
    return response.status_code


sites_availability(urls)
