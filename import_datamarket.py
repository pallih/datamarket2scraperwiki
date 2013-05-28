#!/usr/bin/env python
import sys
import requests
import scraperwiki


URL = "https://datamarket.com/api/v1/list.json?ds=%s&callback=&secret_key=%s"


dstring = sys.argv[1]
apikey = sys.argv[2]

batch = []
print URL % (dstring, apikey)

data = requests.get(URL % (apikey, dstring), verify=False).json()

title = data[0]['title']



columns = []
for items in data[0]['columns']:
    columns.append( items['title'] )

no_columns = len(columns)
batch = []

for items in data[0]['data']:
    import_data = {}
    internal_item = 0
    while internal_item != no_columns:
        import_data[columns[internal_item]] = items[internal_item]
        internal_item = internal_item +1
    batch.append(import_data)



scraperwiki.sqlite.save(['country','year'],data=batch,table_name=title)
