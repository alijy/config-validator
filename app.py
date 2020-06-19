from data_fetcher import fetch

baseUri = 'https://catalogue-labs.tax.service.gov.uk/service-configs/config-by-key/'
serviceName = 'business-tax-account'

response = fetch(baseUri + serviceName)

for key in response.keys():
  print(response.get(key).get('qa'))
  print(response.get(key).get('staging'))
  print(response.get(key).get('production'))

