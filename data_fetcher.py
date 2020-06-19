import requests


def fetch(url):
  res = requests.get(url)
  print(res.status_code, res.headers['content-type'])
  return res.json()
