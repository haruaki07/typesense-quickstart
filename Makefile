TYPESENSE_API_KEY ?=abcde

download-dummy-data: 
	curl -O https://dl.typesense.org/datasets/books.jsonl.gz
	gunzip books.jsonl.gz

start-typesense:
	docker run -d --rm -p 8108:8108 -v/tmp/typesense-data:/data typesense/typesense:0.23.0 --data-dir /data --api-key=$(TYPESENSE_API_KEY)

.PHONY: start-typesense download-dummy-data