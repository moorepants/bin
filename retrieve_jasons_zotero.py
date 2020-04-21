from pyzotero import zotero

library_id = '425053'
library_type = 'user'
api_key = # TODO : Load key from file.

zot = zotero.Zotero(library_id, library_type, api_key)
items = zot.publications()

for item in items:
    print('Item: {} | Key: {}'.format(item['data']['itemType'], item['data']['key']))
