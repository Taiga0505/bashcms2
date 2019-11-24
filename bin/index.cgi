#!/bin/bash

source "$(dirname $0)/conf"

md="$contentsdir/posts/template/main.md"

echo -e "Content-Type: text/html\n"
pandoc -f markdown_github+yaml_metadata_block "$md"

### OUTPUT ###
pandoc --template="$viewdir/template.html" -f markdown_github+yaml_metadata_block "$md"

