#!/bin/bash

files=(testing-cicd/package.json testing-cicd/.gitignore testing-cicd/.prettierrc testing-cicd/.prettierignore testing-cicd/.env)

curl_files=()

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        curl_files+=("-F" "files=@$file")
    else
        echo "Warning: $file not found, skipping."
    fi
done

if [ ${#curl_files[@]} -eq 0 ]; then
    echo "Error: No files to upload."
    exit 1
fi

#echo "Uploading: ${curl_files[*]}"


curl -X POST "http://localhost:8000/upload" "${curl_files[@]}"
