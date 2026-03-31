import os
import pathspec
import re

def parse_file_filter(filter_string):
    """
    Parse a file filter string into a pathspec
    """
    return pathspec.PathSpec.from_lines('gitignore', filter_string.splitlines())

def is_hidden(filename):
    """
    Check if a filename is hidden (starts with '.')
    """
    return filename.startswith('.')

def match_file_filters(filename, filters):
    """
    Check if a filename matches a list of filters
    """
    for filter in filters:
        if re.match(filter, filename):
            return True
    return False