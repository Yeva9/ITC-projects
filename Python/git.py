'''
This module is intended to print git commands.
'''

import sys
#import git
import subprocess


def print_command():
    command = sys.argv[1]
    arr = ["status", "st", "commit", "com", "branch", "br"]

    if command in arr:
        print("/usr/bin/git", command)
        #subprocess.run(["git", command], check=True, stdout=subprocess.PIPE).stdout

    else:
        print("Invalid argument.")


print_command()

'''
repo = git.Repo('usr/bin/git')
repo.remotes.origin.status()

g = git.cmd.Git(git_dir)
g.status()

import subprocess
process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
output = process.communicate()[0]
'''

