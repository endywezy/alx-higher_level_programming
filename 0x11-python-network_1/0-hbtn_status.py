#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
            body = response.read()
            print("Body response:")
            print(f"\t- type: {type(body)}")
            print(f"\t- content: {body}")
            print(f"\t- utf8 content: {body.decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print("Error: {}".format(e))
