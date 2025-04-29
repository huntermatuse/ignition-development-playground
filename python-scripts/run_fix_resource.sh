#!/bin/bash
set -e

for file in "$@"; do
  if [ -f "$file" ]; then
    echo "Fixing $file"
    cat "$file" | python3 python-scripts/fix_resource.py > "$file.tmp"
    mv "$file.tmp" "$file"
  fi
done
