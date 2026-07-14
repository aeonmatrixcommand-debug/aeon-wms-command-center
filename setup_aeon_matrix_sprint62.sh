#!/bin/bash

set -e

ORG="aeonmatrixcommand-debug"
PROJECT_TITLE="🌍 AEON MATRIX Enterprise Operating System Delivery"

echo "🚀 Creating AEON MATRIX Sprint 62 Governance..."

# Create Project
PROJECT_URL=$(gh project create \
  --owner "$ORG" \
  --title "$PROJECT_TITLE" \
  --format json | jq -r '.url')

echo "Project created: $PROJECT_URL"

# Add labels to current repo
LABELS=(
"ai-agent"
"architecture"
"gateway"
"communication"
"event-bus"
"wms"
"tms"
"security"
"governance"
"mobile"
"cloud"
"P0-Critical"
"P1-Enterprise"
"P2-Feature"
"P3-Improvement"
"Sprint 62"
"Sprint 63"
"Sprint 64"
)

for label in "${LABELS[@]}"
do
  gh label create "$label" \
    --color "0E8A16" \
    --description "AEON MATRIX Engineering Label" \
    --force || true
done

# Create milestone
gh api \
  repos/$ORG/$(basename $(git rev-parse --show-toplevel))/milestones \
  -f title="Sprint 62" \
  -f description="Enterprise AI Nervous System Foundation" \
  -f due_on="2026-07-31T23:59:59Z" \
  || true

echo ""
echo "✅ AEON MATRIX Sprint 62 setup completed"
echo "🌍 Enterprise Delivery Board Ready"

