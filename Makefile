.PHONY: help build publish

CONVERT=jupyter nbconvert
CONVERT_OPTS=--to html --output index.html


help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Convert notebooks to webpages
	@echo Hello
	for nb in */*.ipynb ; do ${CONVERT} $$nb ${CONVERT_OPTS} ; done
