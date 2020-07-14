from helpers import fetch

baseUri = 'https://catalogue-labs.tax.service.gov.uk/service-configs/config-by-key/'
serviceName = 'business-tax-account'
blacklist = ['localhost']
configWhiteList = []

response = fetch(baseUri + serviceName)

for key in response.keys():
  environment = response.get(key).get('production')
  if environment is not None:
    environment = sorted(environment, key=lambda i: i['precedence'], reverse=True)[0]
    environmentValue = environment.get('value').lower()
    for item in blacklist:
      if item in environmentValue and key not in configWhiteList:
        print(f"key:\t{key}")
        print(f"source:\t{environment.get('source')}")
        print(f"value:\t{environmentValue}")
        print('---------------------------')