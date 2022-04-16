#!/usr/bin/env python

import os
import sys
import json
import shutil
import logging
import argparse
import subprocess

import utils


logger = logging.getLogger(__name__)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-n', '--dry-run', action='store_true')
    parser.add_argument('-s', '--source-dir', default=os.getcwd())
    parser.add_argument('-t', '--target-dir', default=os.getcwd())
    parser.add_argument('--git-cmd', default='git')
    parser.add_argument('--git-diff-cmd',
                        default='git diff --name-only --diff-filter=ACMR')
    parser.add_argument('--git-diff-cached-cmd',
                        default='git diff --cached --name-only --diff-filter=ACMR')
    parser.add_argument('--git-log-cmd',
                        default='git log --name-only --pretty=format:')
    parser.add_argument('--git-log-cached-cmd',
                        default='git log --cached --name-only --pretty=format:')
    parser.add_argument('--git-log-since-cmd',
                        default='git log --name-only --pretty=format: --since=')
    parser.add_argument('--git-log-since-cached-cmd',
                        default='git log --cached --name-only --pretty=format: --since=')
    return parser.parse_args()


def get_git_cmd(args, cmd):
    return '"{}" {}'.format(args.git_cmd, cmd)


def get_git_diff_cmd(args):
    return get_git_cmd(args, args.git_diff_cmd)


def get_git_diff_cached_cmd(args):
    return get_git_cmd(args, args.git_diff_cached_cmd)


def get_git_log_cmd(args):
    return get_git_cmd(args, args.git_log_cmd)


def get_git_log_cached_cmd(args):
    return get_git_cmd(args, args.git_log_cached_cmd)


def get_git_log_since_cmd(args):
    return get_git_cmd(args, args.git_log_since_cmd)


def get_git_log_since_cached_cmd(args):
    return get_git_cmd(args, args.git_log_since_cached_cmd)


def get_git_diff_files(args, cached=False):
    cmd = get_git_diff_cmd(args) if not cached else get_git_diff_cached_cmd(args)
    output = subprocess.check_output(cmd, shell=True)
    files = output.decode('utf-8').split()
    return [os.path.normpath(f) for f in files]


def get_git_log_files(args, since, cached=False):
    if since:
        cmd = get_git_log_since_cmd(args) + since if not cached else get_git_log_since_cached_cmd(args) + since
    else:
        cmd = get_git_log_cmd(args) if not cached else get_git_log_cached_cmd(args)
    output = subprocess.check_output(cmd, shell=True)
    files = output.decode('utf-8').split()
    return [os.path.normpath(f) for f in files]


def get_changed_files(args, since=None):
    diff_files = get_git_diff_files(args)
    diff_cached_files = get_git_diff_files(args, cached=True)
    log_files = get_git_log_files(args, since)
    log_cached_files = get_git_log_files(args, since, cached=True)
    changed_files = set(diff_files + diff_cached_files + log_files + log_cached_files)
    return changed_files


def get_changed_dirs(args, since=None):
    changed_files = get_changed_files(args, since)
    changed_dirs = set()
    for f in changed_files:
        d = os.path.dirname(f)
        changed_dirs.add(d)
    return changed_dirs


def copy_changed_files(args, since=None):
    changed_files = get_changed_files(args, since)
    for f in changed_files:
        src = os.path.join(args.source_dir, f)
        dst = os.path.join(args.target_dir, f)
        if not os.path.exists(src):
            logger.warning('source file does not exist: {}'.format(src))
            continue
        if os.path.isdir(src):
            logger.warning('source file is a directory: {}'.format(src))
            continue
        d = os.path.dirname(dst)
        if not os.path.exists(d):
            os.makedirs(d)
        logger.info('copying {} to {}'.format(src, dst))
        if not args.dry_run:
            shutil.copy(src, dst)


def copy_changed_dirs(args, since=None):
    changed_dirs = get_changed_dirs(args, since)
    for d in changed_dirs:
        src = os.path.join(args.source_dir, d)
        dst = os.path.join(args.target_dir, d)
        if not os.path.exists(src):
            logger.warning('source directory does not exist: {}'.format(src))
            continue
        if os.path.isfile(src):
            logger.warning('source directory is a file: {}'.format(src))
            continue
        if not os.path.exists(dst):
            logger.info('creating directory: {}'.format(dst))
            if not args.dry_run:
                os.makedirs(dst)


def main():
    args = get_args()
    utils.setup_logging(args)
    copy_changed_dirs(args)
    copy_changed_files(args)


if __name__ == '__main__':
    main()

# TODO
