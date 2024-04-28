#!/usr/bin/python3
"""
    Module for getting the status of alx-intranet.hbtn.io/status.
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as re:
            if re is not None:
                html = resp.read()
                print("Body response:")
                print("\t- type: {}".format(type(html)))
                print("\t- content: {}".format(html))
                print("\t- utf8 content: {}".format(html.decode('utf-8')))
