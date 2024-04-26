#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        print(f"""
        Body response:
        \t- type: {type(body)}
        \t- content: {body}
        \t- utf8 content: {body.decode('utf-8')}
        """)
