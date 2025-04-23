#!/bin/bash
# Tests
set -e

# See https://github.com/dcycle/docker-python-lint
echo ""
echo "To ignore a line, you can add this before the line"
echo "# pylint: disable=E0401"
echo ""
docker run --rm -v $(pwd)/docker-resources:/app/code dcycle/python-lint:2 ./code
docker pull python:alpine
docker build -t local-translate-api-image .

! docker run --rm local-translate-api-image agentic_ai.py --name my_file_manager --prompt "File manager with grid view, search, and dark mode"
echo "[ok] agentic_ai.py returns an error if no environment vars are set"

# docker run --rm \
#   -e MS_ENDPOINT="https://this has to start with https:// but otherwise can be anything" \
#   -e MS_LOC="this can be anything to make preflight pass" \
#   -e MS_KEY="this can be anything to make preflight pass" \
#   -e MS_SIMULATE="true" \
#   local-translate-api-image preflight.py

docker run --rm \
  -e GEMINI_API_KEY="AIzaSyDTV6eMOwe6ibRj_t9t3NVV6ywAjmhIuT0"
  local-translate-api-image agentic_ai.py --name my_file_manager --prompt "File manager with grid view, search, and dark mode"

echo "[ok] preflight.py passes if environment vars are set"
