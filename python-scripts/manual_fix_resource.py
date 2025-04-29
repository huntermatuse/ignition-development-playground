#!/usr/bin/env python3
import sys
import re
import os
import json
import argparse


def fix_resource_json(text):
    """Apply the specified transformations to the resource.json content"""
    text = re.sub(r'"actor": ".*?"', r'"actor": "system"', text)
    text = re.sub(r'"timestamp": ".*?"', r'"timestamp": "2022-01-01T00:00:00Z"', text)
    text = re.sub(r'"lastModificationSignature": ".*?"', r'"lastModificationSignature": "4a15e0122c9a955ca05b407bd9fa06810c1a05bd02f35e6ab4cc38c0654af46"', text)
    return text


def process_directory(directory_path):
    """Recursively process all resource.json files in the given directory"""
    count = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file == 'resource.json':
                file_path = os.path.join(root, file)
                try:
                    # Read the original content
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Apply fixes
                    updated_content = fix_resource_json(content)
                    
                    # Write back if changes were made
                    if content != updated_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        print(f"Updated: {file_path}")
                        count += 1
                    else:
                        print(f"No changes needed: {file_path}")
                
                except Exception as e:
                    print(f"Error processing {file_path}: {e}", file=sys.stderr)
    
    print(f"\nProcessed {count} resource.json files")


def main():
    parser = argparse.ArgumentParser(description='Update resource.json files in a directory')
    parser.add_argument('directory', help='Directory to search for resource.json files')
    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory", file=sys.stderr)
        sys.exit(1)
    
    process_directory(args.directory)


if __name__ == "__main__":
    main()