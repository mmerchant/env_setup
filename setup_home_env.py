#!/usr/bin/env python

import os
import subprocess
import shlex
import platform
from shutil import copy2 as cp

HOME_DIR = os.path.expanduser("~")
ST_LOCATION = "{}/Library/Application Support/Sublime Text 3/Packages".format(
    HOME_DIR)
PYTHON_VERSION = 2


def _get_python_version():
    global PYTHON_VERSION
    try:
        input = raw_input
    except NameError:
        PYTHON_VERSION = 3

def _get_platform_os():
    return platform.system().lower(), platform.release().lower()


def _install_dependencies(platform_release):
    if "amzn" in platform_release:
        install_command = ("sudo yum install "
                           "python27-devel python27-pip gcc "
                           "vim")
    else:
        install_command = ("sudo apt-get install "
                           "build-essential autoconf "
                           "python-dev python-pip vim")
        git_bash_command = ("git clone "
                            "https://github.com/magicmonty/bash-git-prompt.git"
                            " {}/.bash-git-prompt --depth=1".format(HOME_DIR))
    try:
        subprocess_install_command = shlex.split(install_command)
        git_install_command = shlex.split(git_bash_command)
        subprocess.call(subprocess_install_command)
        subprocess.call(git_install_command)
    except:
        pass
    return True


def _install_vundle(HOME_DIR):
    try:
        if not os.path.isdir("{0}/.vim/bundle/Vundle.vim".format(HOME_DIR)):
            clone_command = ("git clone "
                             "https://github.com/gmarik/Vundle.vim.git "
                             "{0}/.vim/bundle/Vundle.vim").format(HOME_DIR)
            subprocess_clone_command = shlex.split(clone_command)
            subprocess.call(subprocess_clone_command)
    except:
        print("\033[0;32mERROR:\033[0;37m\033[0;m Vundle already installed.")
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
        operating_sys, platform_release = _get_platform_os()
        if operating_sys == "linux":
            if "amzn" in platform_release:
                install_command = "sudo yum install tmux"
            else:
                install_command = "sudo apt-get install tmux"
        elif operating_sys == "darwin":
            install_command = "brew install tmux"
        else:
            print ("\033[0;31mERROR:\033[0;37m\033[0;m Could not determine "
                   "your Operating System. Please install tmux manually.")
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
    operating_sys, platform_release = _get_platform_os()
    if operating_sys == "linux":
        if "amzn" in platform_release:
            print ("\033[0;31mERROR:\033[0;37m\033[0;m "
                   "Don't have anything for you yet...")
        else:
            # Let's just create a backup of your bashrc in case
            try:
                source_file = "{0}/.bashrc".format(HOME_DIR)
                destination = "{0}/.bashrc.bak".format(HOME_DIR)
                cp(source_file, destination)
            except:
                pass
            # Now we'll replace the file
            source_file = "{0}/{1}".format(
                os.getcwd(), "profile_settings_file.txt")
            destination = "{0}/.bashrc".format(HOME_DIR)
            cp(source_file, destination)
            source_file = "{0}/{1}".format(os.getcwd(), "input_settings_file.txt")
            destination = "{0}/.inputrc".format(HOME_DIR)
            cp(source_file, destination)
        return True
    elif operating_sys == "darwin":
        # Let's just create a backup of your bashrc in case
        try:
            source_file = "{0}/.bash_profile".format(HOME_DIR)
            destination = "{0}/.bash_profile.bak".format(HOME_DIR)
        except:
            pass
        # Now we'll replace the file
        source_file = "{0}/{1}".format(
            os.getcwd(), "profile_settings_file.txt")
        destination = "{0}/.bash_profile".format(HOME_DIR)
        cp(source_file, destination)
        source_file = "{0}/{1}".format(os.getcwd(), "input_settings_file.txt")
        destination = "{0}/.inputrc".format(HOME_DIR)
        cp(source_file, destination)
    else:
        print ("\033[0;31mERROR:\033[0;37m\033[0;m Could not determine your "
               "Operating System. Setup your profile yourself.")
        return False
    return True


def _install_thefuck(HOME_DIR):
    operating_sys, platform_release = _get_platform_os()
    if operating_sys == "linux":
        thefuck_install_command = "sudo -H pip install thefuck"
    elif operating_sys == "darwin":
        thefuck_install_command = "pip install thefuck"
    else:
        print ("\033[0;31mERROR:\033[0;37m\033[0;m Go to "
               "https://github.com/nvbn/thefuck to see how "
               "to install for your OS")
        return False
    subprocess.call(shlex.split(thefuck_install_command))
    return True


def _install_redshift_console(HOME_DIR):
    operating_sys, platform_release = _get_platform_os()
    if operating_sys == "linux":
        thefuck_install_command = "sudo -H pip install redshift-console"
    elif operating_sys == "darwin":
        thefuck_install_command = "pip install redshift-console"
    else:
        print ("\033[0;31mERROR:\033[0;37m\033[0;m Go to "
               "https://github.com/everythingme/redshift_console to see how "
               "to install for your OS")
        return False
    subprocess.call(shlex.split(thefuck_install_command))
    return True


def _make_psqlrc(HOME_DIR):
    # Copy psqlrc_settings_file.txt file to user's home dir
    source_file = "{0}/{1}".format(os.getcwd(), "psqlrc_settings_file.txt")
    destination = "{0}/.psqlrc".format(HOME_DIR)
    cp(source_file, destination)
    return True


def _set_hostname():
    operating_sys, platform_release = _get_platform_os()
    if operating_sys == "linux":
        if "amzn" in platform_release:
            print("Can't set the hostname yet.")
        else:
            new_hostname = input(
                "\033[0;31mEnter hostname for this machine: \033[0;37m\033[0;m"
                )
            if new_hostname:
                set_hostname_command = "sudo hostname {0}".format(new_hostname)
                subprocess.call(shlex.split(set_hostname_command))
            else:
                print("No hostname given. None set.")
    else:
        return False
    return True


def _install_autovenv(HOME_DIR):
    operating_sys, platform_release = _get_platform_os()
    if operating_sys == "linux":
        thefuck_install_command = "sudo -H pip install autovenv"
    elif operating_sys == "darwin":
        thefuck_install_command = "pip install autovenv"
    else:
        print ("\033[0;31mERROR:\033[0;37m\033[0;m Go to "
               "https://autovenv.readthedocs.org/en/latest/ to see how "
               "to install for your OS")
        return False
    subprocess.call(shlex.split(thefuck_install_command))
    return True


def _install_custom_sublimetext_syntax(HOME_DIR):
    operating_sys, platform_release = _get_platform_os()
    if operating_sys == "darwin":
        custom_configs = [
            "https://github.com/pnlarsson/SublimeKamailioConfig.git"
        ]
        for custom_syntax in custom_configs:
            proj_name = os.path.basename(custom_syntax).split(".")[0]
            if os.path.isdir(ST_LOCATION):
                git_cmd = ("git clone {} {}/{}".format(
                    custom_syntax, ST_LOCATION, proj_name)
                )
                subprocess_install_command = shlex.split(git_cmd)
                subprocess.call(subprocess_install_command)
            else:
                print("Update your Sublime Text location!")


def main():
    # Check python version because of raw_input vs input:
    global PYTHON_VERSION
    print(PYTHON_VERSION)
    PYTHON_VERSION = _get_python_version()
    # Install OS Dependency
    operating_sys, platform_release = _get_platform_os()
    if operating_sys == "linux":
        _install_dependencies(platform_release)

    # Install Vundle (https://github.com/gmarik/Vundle.vim):
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
        print("\033[0;31mERROR:\033[0;37m\033[0;m tmux was not installed.")

    # Profile config
    _make_profile(HOME_DIR)

    # Install TheFuck (https://github.com/nvbn/thefuck)
    _install_thefuck(HOME_DIR)

    # Install Redshift Console
    answer = input("\033[0;31mInstall Redshift Console:\033[0;37m\033[0;m "
                       "(https://github.com/everythingme/redshift_console)? ")
    if answer.upper() in ("Y", "YES"):
        _install_redshift_console(HOME_DIR)

    # Install autoenv helper
    _install_autovenv(HOME_DIR)

    # Create PSQLRC file
    _make_psqlrc(HOME_DIR)

    # Set hostname for machine
    _set_hostname()

    # Install custom Sublime text syntax highlighting
    _install_custom_sublimetext_syntax(HOME_DIR)
    print(PYTHON_VERSION)

if __name__ == "__main__":
    main()
