#!/bin/bash
# Tests a connection to Microsft Translation
set -e

# docker run --rm \
#   -e MS_ENDPOINT="$MS_ENDPOINT" \
#   -e MS_LOC="$MS_LOC" \
#   -e MS_KEY="$MS_KEY" \
#   local-translate-api-image preflight.py

docker run --rm local-translate-api-image agentic_ai.py --name my_file_manager --prompt "File manager with grid view, search, and dark mode"
