#!/bin/bash
# Claude Code startup script with local plugins

cd "$(dirname "$0")"

# Add plugin directories as needed
PLUGIN_DIRS=(
  ./plugins/conf-analysis
  # Add more plugins here: ./another-plugin
)

# Build plugin arguments
PLUGIN_ARGS=()
for dir in "${PLUGIN_DIRS[@]}"; do
  if [ -d "$dir" ]; then
    PLUGIN_ARGS+=("--plugin-dir" "$dir")
  fi
done

claude \
  "${PLUGIN_ARGS[@]}" \
  "$@"