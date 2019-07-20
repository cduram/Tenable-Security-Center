from securitycenter import SecurityCenter5 # https://github.com/SteveMcGrath/pySecurityCenter/blob/master/SecurityCenter5_REST_API.md
import json, pprint

sc = SecurityCenter5('<your_server>')
sc.login('api','<api_keyd>') # username, password

response = sc.get('status')

status_results = json.loads(response.text)

# Pretty print.

#pprint.pprint(status_results["response"])

# Write to file

with open('c:\\scripts\\results.json', 'w') as outfile:
    json.dump(status_results, outfile)
