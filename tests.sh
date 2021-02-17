#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

trap "docker-compose -f test.yml logs && docker-compose -f test.yml down && docker-compose -f test.yml rm" EXIT
docker-compose -f test.yml build
docker-compose -f test.yml run --rm --entrypoint pytest django_test
docker-compose -f test.yml down
docker-compose -f test.yml rm
