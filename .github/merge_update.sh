#!/bin/bash

# Update feature branch
git checkout features
git pull origin main

# Switch to the main branch
git checkout main

# Merge the feature branch
git merge features

# Resolve merge conflicts (if any)
# [Manual step, not automated in the script]

# Commit the merge
git commit -m "Merge features branch into main"

echo "Updating version to $version"

# Update the version number in setup.py
current_version=$(grep -oP "(?<=version=')[^']+?(?=')" setup.py)
new_version=$(awk -F. -v OFS=. '{$NF++; print}' <<< "$current_version")

sed -i "s/version='$current_version'/version='$new_version'/" setup.py

# Commit the changes to setup.py
git add setup.py
git commit -m "Update version in setup.py"

# Push the changes
git push origin main

echo "Merge and version update completed successfully!"

# Update the version variable for the next run
sed -i "s/version='$new_version'/version='$new_version'/" "${BASH_SOURCE[0]}"
