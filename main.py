import typesense
import json

# ------ INIT TYPESENSE
# TYPESENSE_API_KEY = 'abcde'
# client = typesense.Client({
#     'nodes': [{
#         'host': 'localhost',
#         'port': '8108',
#         'protocol': 'http',
#     }],
#     'api_key': TYPESENSE_API_KEY,
#     'connection_timeout_seconds': 2
# })

# ------ CREATE COLLECTION
# books_schema = {
#     'name': 'books',
#     'fields': [
#         {'name': 'title', 'type': 'string'},
#         {'name': 'authors', 'type': 'string[]', 'facet': True},

#         {'name': 'publication_year', 'type': 'int32', 'facet': True},
#         {'name': 'ratings_count', 'type': 'int32'},
#         {'name': 'average_rating', 'type': 'float'}
#     ],
#     'default_sorting_field': 'ratings_count'
# }

# client.collections.create(books_schema)

# ------ INSERT DOCUMENTS
# with open('./books.jsonl') as jsonl_file:
#     client.collections['books'].documents.import_(
#         jsonl_file.read().encode('utf-8'))

# ------ QUERYING DOCUMENT
# search_parameters = {
#     'q': 'harry potter',
#     'query_by': 'title',
#     'sort_by': 'ratings_count:desc'
# }

# result = client.collections['books'].documents.search(search_parameters)
# print(json.dumps(result, sort_keys=True, indent=4))
