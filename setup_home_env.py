#!/usr/bin/env python

import os
import subprocess
import shlex
import platform
from shutil import copy2 as cp


def _get_platform_os():
    return platform.system().lower()


def _install_dependencies():
    install_command = "sudo apt-get install build-essential autoconf"
    subprocess_install_command = shlex.split(install_command)
    subprocess.call(subprocess_install_command)
    return True


def _install_vundle(HOME_DIR):
    try:
        if not os.path.isdir("{0}/.vim/bundle/Vundle.vim".format(HOME_DIR)):
            clone_command = "git clone https://github.com/gmarik/Vundle.vim.git {0}/.vim/bundle/Vundle.vim".format(HOME_DIR)
            subprocess_clone_command = shlex.split(clone_command)
            subprocess.call(subprocess_clone_command)
    except:
        print "\033[0;32mERROR:\033[0;37m\033[0;m Vundle already installed."
    return True


def _make_vim_undo_dir(HOME_DIR, UNDO_DIR):
    if not os.path.exists(UNDO_DIR):
        os.makedirs(UNDO_DIR)
    return True


def _make_vimrc(HOME_DIR):
    # Copy vimrc_settings_file.txt file to user's home dir
    source_file = "{0}/{1}".format(os.getcwd(), "vimrc_settings_file.txt")
    destination = "{0}/.vimrc".format(HOME_DIR)
    cp(source_file, destination)
    return True


def _install_vundle_plugins(HOME_DIR):
    install_command = "vim +PluginInstall +qall"
    subprocess_install_command = shlex.split(install_command)
    subprocess.call(subprocess_install_command)
    return True


def _install_tmux(HOME_DIR):
    try:
        subprocess.check_output(["which", "tmux"])
    except:
        operating_sys = _get_platform_os()
        if operating_sys == "linux":
            install_command = "sudo apt-get install tmux"
        elif operating_sys == "darwin":
            install_command = "brew install tmux"
        else:
            print "\033[0;31mERROR:\033[0;37m\033[0;m Could not determine your Operating System. Please install tmux manually."
            return False
        subprocess_install_command = shlex.split(install_command)
        subprocess.call(subprocess_install_command)
    return True


def _make_tmux_config(HOME_DIR):
    # Copy tmux_settings_file.txt file to user's home dir
    source_file = "{0}/{1}".format(os.getcwd(), "tmux_settings_file.txt")
    destination = "{0}/.tmux.conf".format(HOME_DIR)
    cp(source_file, destination)
    return True


def _make_profile(HOME_DIR):
    operating_sys = _get_platform_os()
    if operating_sys == "linux":
        print "\033[0;31mERROR:\033[0;37m\033[0;m Don't have anything for you yet..."
        return False
    elif operating_sys == "darwin":
        source_file = "{0}/{1}".format(os.getcwd(), "profile_settings_file.txt")
        destination = "{0}/.bash_profile".format(HOME_DIR)
        cp(source_file, destination)
        source_file = "{0}/{1}".format(os.getcwd(), "input_settings_file.txt")
        destination = "{0}/.inputrc".format(HOME_DIR)
        cp(source_file, destination)
    else:
        print "\033[0;31mERROR:\033[0;37m\033[0;m Could not determine your Operating System. Setup your profile yourself."
        return False
    return True


def _install_thefuck(HOME_DIR):
    operating_sys = _get_platform_os()
    if operating_sys == "linux":
        thefuck_install_command = "sudo pip install thefuck"
    elif operating_sys == "darwin":
        thefuck_install_command = "pip install thefuck"
    else:
        print "\033[0;31mERROR:\033[0;37m\033[0;m Go to https://github.com/nvbn/thefuck to see how to install for your OS"
        return False
    subprocess.call(shlex.split(thefuck_install_command))
    return True


def main():
    # Install OS Dependency
    operating_sys = _get_platform_os()
    if operating_sys == "linux":
        _install_dependencies()
    
    # Install Vundle (https://github.com/gmarik/Vundle.vim):
    HOME_DIR = os.path.expanduser("~")
    _install_vundle(HOME_DIR)

    # Create VIM undo directory
    UNDO_DIR = "{0}/.vim/undodir/".format(HOME_DIR)
    _make_vim_undo_dir(HOME_DIR, UNDO_DIR)

    # Create VIMRC file
    _make_vimrc(HOME_DIR)

    # Install Vundle Plug-ins
    _install_vundle_plugins(HOME_DIR)

    # Setup Tmux
    tmux_install_status = _install_tmux(HOME_DIR)
    if tmux_install_status:
        _make_tmux_config(HOME_DIR)
    else:
        print "\033[0;31mERROR:\033[0;37m\033[0;m tmux was not installed."

    # Profile config
    _make_profile(HOME_DIR)

    # Install TheFuck (https://github.com/nvbn/thefuck)
    _install_thefuck(HOME_DIR)


if __name__ == "__main__":
    main()
