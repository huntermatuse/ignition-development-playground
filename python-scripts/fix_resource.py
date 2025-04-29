#!/usr/bin/env python3
import sys
import re

def fix_resource_json(text):
    text = re.sub(r'"actor": ".*?"', r'"actor": "system"', text)
    text = re.sub(r'"timestamp": ".*?"', r'"timestamp": "2022-01-01T00:00:00Z"', text)
    text = re.sub(r'"lastModificationSignature": ".*?"', r'"lastModificationSignature": "4a15e0122c9a955ca05b407bd9fa06810c1a05bd02f35e6ab4cc38c0654af46"', text)
    return text

input_data = sys.stdin.read()
output_data = fix_resource_json(input_data)
sys.stdout.write(output_data)