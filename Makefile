SHELL = /usr/bin/env bash -xeuo pipefail

stack_name:=api-gw-lambda-load-test-001-01-dynamodb


deploy:
	poetry run aws cloudformation deploy \
		--stack-name $(stack_name) \
		--template-file template.yml \
		--capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
		--no-fail-on-empty-changeset

prepare-dynamodb:
	STACK_NAME=$(stack_name) \
	poetry run python scripts/put_items.py

.PHONY: \
	deploy \
	prepare-dynamodb
