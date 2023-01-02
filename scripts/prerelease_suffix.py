#!/usr/bin/env python3

import os
import re


def find_prerelease_suffix(name_branch):

    name_branch_lower = name_branch.lower()

    suffix_array = re.findall("alpha|beta|prerelease", name_branch_lower)

    env_file = os.getenv('GITHUB_ENV')

    with open(env_file, 'w') as myfile:
        myfile.write("PRERELEASE=" + suffix_array[0])

    return suffix_array[0]


def main():

    # Variables declaration
    name_branch = os.environ['NAME_BRANCH']

    # Call to functions
    prerelease_suffix = find_prerelease_suffix(name_branch)


if __name__ == '__main__':
    main()


