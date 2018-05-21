#!/usr/bin/env python2
"""This script is for downloading and configuring all the mumble moderator modules"""
from __future__ import print_function
import subprocess as sp
import sys
import os
import fnmatch
import shutil

class Clr(object): # pylint: disable=too-few-public-methods
    """colors for print"""
    WRN = '\x1b[0;30;43m'
    OKG = '\x1b[6;30;42m'
    RST = '\x1b[0m'

def git_clone(clone_string, to_dir=""):
    """a little git clone wrapper function. It will clone with --depth=1,
    which leads to smaler downloads, because the history will not ne downloaded"""
    print("normal clone: " + clone_string)
    previous_dir = os.getcwd()
    os.chdir(to_dir)
    return_value = sp.check_call(["git", "clone", "--depth=1", clone_string])
    os.chdir(previous_dir)
    return return_value

def clone_github(user_repo_string, to_dir=""):
    """same as git_clone but downloads only from github and you only need
    'user/repo' or 'group/repo'"""
    print("github clone: " + user_repo_string)
    previous_dir = os.getcwd()
    os.chdir(to_dir)
    return_value = sp.check_call(["git", "clone", "--depth=1",
                                  "https://github.com/" + user_repo_string + ".git"])
    os.chdir(previous_dir)
    return return_value

def choose(clone_string, to_dir=""):
    """from the clone_string try to find out which git clone functio to use"""
    if clone_string.startswith(("https://", "http://")):
        return git_clone(clone_string, to_dir=to_dir)
    elif clone_string.count("/") == 1:
        return clone_github(clone_string, to_dir=to_dir)
    else:
        raise ValueError(clone_string + " is an unkown clone url type")

def find_files_recursive(pattern, directory):
    """search a pattern in a directory and all directory below it.
    The pattern is from the fnmatch library from core python. Please look there"""
    for root, _, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            yield os.path.join(root, filename)



def mumo_modules_move(pattern, from_path, to_path):
    """find all files with given pattern in given from_path and move it to_path :)"""
    for file_path in find_files_recursive(pattern, from_path):
        print(Clr.OKG + "FROM:" + Clr.RST, " ",
              file_path,
              " " + Clr.OKG + "TO:" + Clr.RST + " ",
              to_path)
        try:
            shutil.move(file_path, to_path)
        except shutil.Error:
            # TODO change to logging
            print(Clr.WRN + "WARNING" + Clr.RST + " File already exsists: ", file_path,
                  " in ", to_path)

def main():
    """Just does the thing ^^"""
    base_dir = os.environ["HOME"]
    modules_dir = os.path.join(base_dir, "modules")

    os.mkdir(modules_dir)

    print("## cloning to: " + base_dir)
    print()
    clone_github("mumble-voip/mumo", os.getcwd())

    clone_array = ("aselus-hub/chatimg-mumo",
                   "while-loop/mumo-videoinfo",
                   "ExplodingFist/mumo-opcommand",
                   "Natenom/mumblemoderator-module-collection",
                   "Betriebsrat/mumo-password")
    print("## cloning to:" + modules_dir)
    print()
    for clone_string in clone_array:
        choose(clone_string, modules_dir)

    modules_available_path = os.path.join(base_dir, "mumo", "modules-available")
    mumo_modules_move("*.ini", modules_dir, modules_available_path)

    modules_path = os.path.join(base_dir, "mumo", "modules")
    mumo_modules_move("*.py", modules_dir, modules_path)

    # fixing derangment of prints
    sys.stdout.flush()

    sp.check_call(("tree", modules_dir))
    sp.check_call(("tree", os.environ["HOME"]))
    print("I merged all the downloaded modules into the main mumo repo.\n",
          "Please check if i forgot something.")
    if "DO_NOT_DELETE_ADDONS" in os.environ:
        print("I won't delete the modules because DO_NOT_DELETE_ADDONS variable is set")
    else:
        print("Deleting modules now")
        shutil.rmtree(modules_dir, ignore_errors=True)

if __name__ == "__main__":
    sys.exit(main())
