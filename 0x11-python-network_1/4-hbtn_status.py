#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using requests."""
import requests


def main():
  """Fetches the status and prints the response in a formatted way."""
  url = "https://alx-intranet.hbtn.io/status"
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
  except requests.exceptions.RequestException as e:
    print("Error: {}".format(e))


if __name__ == "__main__":
  main()
