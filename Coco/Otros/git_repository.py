# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 21:56:44 2021

@author: Pmontenegro
"""

# Git clone project

## Install pip

# python -m pip install gitpython

import git
import sys
import os
from git import Repo

print(sys.path)

# `git init new_repo`

# new_repo = git.Repo.init('new_repo')

# repository existing

## my_repo = git.Repo('existing_repo')


# Check out via HTTPS Dura demasiado en ejecutarse

# git.Git("C:/Users/pmontenegro/Desktop/personal").clone("https://github.com/CocoUrbina/Python.git")

# Repo.clone_from("https://github.com/CocoUrbina/Python.git", "C:/Users/pmontenegro/Desktop/personal")

my_repo = git.Repo('C:/Users/pmontenegro/Desktop/Python')


# with my_repo.config_writer() as git_config:
#     git_config.set_value('Pedro', 'montenegromasis@hotmail.com','monte777')
#     git_config.set_value('Pedro','montenegromasis@hotmail.com','montenegromasis@hotmail.com')
    
# os.system("git config --global user.name \"monte777\"")
# os.system("git config --global user.email \"montenegromasis@hotmail.com\"")    
    
# List remotes
print('Remotes:')
for remote in my_repo.remotes:
    print(f'- {remote.name} {remote.url}')
    
def get_name():
    return "Pedro"

my_repo.index.add(["git_repository.py"])
# Provide a commit message
my_repo.index.commit('Initial commit.')


# Pull from remote repo
print(my_repo.remotes.origin.pull())

# Push changes
print(my_repo.remotes.origin.push())
my_repo.git.push("my remote repo url")
