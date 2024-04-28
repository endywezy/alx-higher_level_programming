#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    try:
        response = requests.get("https://alx-intranet.hbtn.io/status")
        response.raise_for_status()

        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
