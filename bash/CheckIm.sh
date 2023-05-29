#!/bin/bash

# Verify if the folder path is provided as a command line
if [ $# -eq 0 ]; then
    echo "Give me the path of the folder as a command line: "
    exit 1
fi

folder_path=$1
# comment

# Check if it exists
if [ ! -d "$folder_path" ]; then
    echo "Maybe you typed wrong: folder does not exist. Retry."
    exit 1
fi

# Iterate over all files in the folder
for file in "$folder_path"/*; do
    # Check if the file ends with ".png" or ".jpg"
    if [[ $file == *.png || $file == *.jpg ]]; then
        echo "The file $file is an image."
    fi
done