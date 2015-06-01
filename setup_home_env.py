#!/usr/bin/env python

import os
import subprocess
import shlex
import platform
from shutil import copy2 as cp


def install_vundle(HOME_DIR):
    clone_command = 'git clone https://github.com/gmarik/Vundle.vim.git {0}/.vim/bundle/Vundle.vim'.format(HOME_DIR)
    subprocess_clone_command = shlex.split(clone_command)
    subprocess.call(subprocess_clone_command)


def make_vim_undo_dir(HOME_DIR, UNDO_DIR):
    if not os.path.exists(UNDO_DIR):
        os.makedirs(UNDO_DIR)


def make_vimrc(HOME_DIR):
    # Copy vimrc_settings_file.txt file to user's home dir
    source_file = '{0}/{1}'.format(os.getcwd(), 'vimrc_settings_file.txt')
    destination = '{0}/.vimrc'.format(HOME_DIR)
    cp(source_file, destination)


def install_vundle_plugins(HOME_DIR):
    install_command = 'vim +PluginInstall +qall'
    subprocess_install_command = shlex.split(install_command)
    subprocess.call(subprocess_install_command)


def install_tmux(HOME_DIR):
    try:
        subprocess.check_output(['which', 'tmux'])
        tmux_install_status = True
    except:
        operating_sys = platform.system().lower()
        if operating_sys == 'linux':
            install_command = 'sudo apt-get install tmux'
            tmux_install_status = True
        elif operating_sys == 'darwin':
            install_command = 'brew install tmux'
            tmux_install_status = True
        else:
            print '\033[0;31mERROR:\033[0;37m\033[0;m Could not determine your Operating System. Please install tmux manually.'
            tmux_install_status = False
        subprocess_install_command = shlex.split(install_command)
        subprocess.call(subprocess_install_command)
    return tmux_install_status


def make_tmux_config(HOME_DIR):
    # Copy tmux_settings_file.txt file to user's home dir
    source_file = '{0}/{1}'.format(os.getcwd(), 'tmux_settings_file.txt')
    destination = '{0}/.tmux.conf'.format(HOME_DIR)
    cp(source_file, destination)


def main():
    # Install Vundle (https://github.com/gmarik/Vundle.vim):
    HOME_DIR = os.path.expanduser("~")
    install_vundle(HOME_DIR)

    # Create VIM undo directory
    UNDO_DIR = '{0}/.vim/undodir/'.format(HOME_DIR)
    make_vim_undo_dir(HOME_DIR, UNDO_DIR)

    # Create VIMRC file
    make_vimrc(HOME_DIR)

    # Install Vundle Plug-ins
    install_vundle_plugins(HOME_DIR)

    # Setup Tmux
    tmux_install_status = install_tmux(HOME_DIR)
    make_tmux_config(HOME_DIR)


if __name__ == '__main__':
    main()
