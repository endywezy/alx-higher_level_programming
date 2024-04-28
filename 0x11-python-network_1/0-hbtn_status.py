#!/usr/bin/python3
"""fetches url https://alx-intranet.hbtn.io/status using urllib"""

if __name__ == "__main__":
    from urllib.request import urlopen
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
