#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-

import argparse
import os


"""
rename  a group of files
"""


def batch_rename(work_dir, old_ext, new_ext):
    """
    rename  a group of files
    """

    for filename in os.listdir(work_dir):

        split_file = os.path.splitext(filename)
        file_ext = split_file[1]

        if old_ext == file_ext:
            newfile = split_file[0] + new_ext
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )

    print("Rename is over")
    print(os.listdir(work_dir))
