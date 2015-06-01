#!/usr/bin/env python

import os
import subprocess
import shlex
import platform


def install_vundle(HOME_DIR):
    clone_command = 'git clone https://github.com/gmarik/Vundle.vim.git {0}/.vim/bundle/Vundle.vim'.format(HOME_DIR)
    subprocess_clone_command = shlex.split(clone_command)
    subprocess.call(subprocess_clone_command)


def make_vim_undo_dir(HOME_DIR, UNDO_DIR):
    if not os.path.exists(UNDO_DIR):
        os.makedirs(UNDO_DIR)


def make_vimrc(HOME_DIR):
    # Build VIMrc
    vimrc_settings = """set nocompatible
filetype off

" Time to Vundle: https://github.com/gmarik/vundle
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Install awseome VIM bundles
Plugin 'mattn/webapi-vim'
Plugin 'mattn/gist-vim'
Plugin 'vim-scripts/PyChimp'
Plugin 'altercation/vim-colors-solarized'
Plugin 'bronson/vim-crosshairs'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on

" Additional modifications for a VIM-tastic experience
set ruler
syntax enable

" Set tabs to have 4 spaces
set ts=4

" Show a visual line under the cursor's current line
set cursorline

" Undo directory!
set undofile
set undodir=~/.vim/undodir

" Enable all Python syntax highlighting features
let python_highlight_all = 1

let g:gist_post_private = 1 " Make gist posts private by default
" By default, make ctrlp search files, buffers, and MRU files.
let g:ctrlp_cmd = 'CtrlPMixed'

" If using a dark background within the editing area and syntax highlighting
" turn on this option as well
set background=light

" Vim5 and later versions support syntax highlighting. Uncommenting the
" following enables syntax highlighting by default.
if has("syntax")
  syntax on
endif

" Uncomment the following to have Vim jump to the last position when
" reopening a file
if has("autocmd")
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif

" Uncomment the following to have Vim load indentation rules and plugins
" according to the detected filetype.
" if has("autocmd")
"   filetype off
"   filetype plugin indent on
" endif

set grepprg=grep\ -nH\ $*

" The following are commented out as they cause vim to behave a lot
" differently from regular Vi. They are highly recommended though.
set showcmd     " Show (partial) command in status line.
set showmatch       " Show matching brackets.
set ignorecase      " Do case insensitive matching
set smartcase       " Do smart case matching
"set incsearch      " Incremental search
set autowrite       " Automatically save before commands like :next and :make
set nohidden             " Hide buffers when they are abandoned
"set mouse=a        " Enable mouse usage (all modes)
"
set foldmethod=marker

set tabstop=4
set shiftwidth=4
set cursorline
set hlsearch

" Map F5 to toggle highlighting after a search
map <F5> :set invhls!<bar>set hls?<CR>

" Enable for Django templates
autocmd FileType html,htmldjango,xhtml let b:surround_37 = "{% \r %}"
" PHP stuff
autocmd FileType php let b:surround_45 = "<?php \r ?>"

" Source a global configuration file if available
if filereadable("/etc/vim/vimrc.local")
  source /etc/vim/vimrc.local
endif

set backspace=eol,start,indent
" Show line numbers
set number
" Indent when moving to the next line while writing code
set autoindent
" Expand tabs into spaces
set expandtab
set smarttab


if version >= 700
    set spl=en spell
    set nospell
endif

set wildmenu
set wildmode=list:longest,full

"{{{ Paste Toggle
let paste_mode = 0 " 0 = normal, 1 = paste

func! Paste_on_off()
   if g:paste_mode == 0
      set paste
      let g:paste_mode = 1
   else
      set nopaste
      let g:paste_mode = 0
   endif
   return
endfunc
"}}}

" Paste Mode!  Dang! <F10>
nnoremap <silent> <F10> :call Paste_on_off()<CR>
set pastetoggle=<F10>

" Remove trailing whitespace
nnoremap <Leader>rtw :%s/\s\+$//e<CR>

" Edit vimrc \ev
nnoremap <silent> <Leader>ev :tabnew<CR>:e ~/.vimrc<CR>

" Edit gvimrc \gv
nnoremap <silent> <Leader>gv :tabnew<CR>:e ~/.gvimrc<CR>

" Search mappings: These will make it so that going to the next one in a
" search will center on the line it's found in.
map N Nzz
map n nzz

" Testing
set completeopt=longest,menuone,preview

" Space will toggle folds!
nnoremap <space> za

" Show trailing whitespace and spaces before a tab:
highlight ExtraWhitespace ctermbg=red guibg=red
match ExtraWhitespace /\s\+$/
match ExtraWhitespace /\s\+$\| \+\ze\t/

" make keypad work in vim with iTerm on OS X!
map <Esc>Oq 1
map <Esc>Or 2
map <Esc>Os 3
map <Esc>Ot 4
map <Esc>Ou 5
map <Esc>Ov 6
map <Esc>Ow 7
map <Esc>Ox 8
map <Esc>Oy 9
map <Esc>Op 0
map <Esc>On .
map <Esc>OQ /
" map <Esc>OR
map <kPlus> +
map <Esc>OS -
map! <Esc>Oq 1
map! <Esc>Or 2
map! <Esc>Os 3
map! <Esc>Ot 4
map! <Esc>Ou 5
map! <Esc>Ov 6
map! <Esc>Ow 7
map! <Esc>Ox 8
map! <Esc>Oy 9
map! <Esc>Op 0
map! <Esc>On .
map! <Esc>OQ /
" map! <Esc>OR
map! <kPlus> +
map! <Esc>OS -

" Enable Crosshairs
highlight CursorLine   cterm=NONE ctermbg=235
highlight CursorColumn cterm=NONE ctermbg=235
nnoremap <Leader>c :set cursorline cursorcolumn<CR>
"""
    vimrc_file = "{0}/.vimrc".format(HOME_DIR)
    with open(vimrc_file, 'w') as vimrc_conf:
        vimrc_conf.write(vimrc_settings)


def install_vundle_plugins(HOME_DIR):
    install_command = 'vim +PluginInstall +qall'
    subprocess_install_command = shlex.split(install_command)
    subprocess.call(subprocess_install_command)


def install_tmux(HOME_DIR):
    try:
        subprocess.check_output(['which', 'tmux'])
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
    tmux_settings = """# Tmux settings

# Set XTerm key bindings
setw -g xterm-keys on

# Set colors
set-option -g default-terminal "screen-256color"

# Set reload key to r
bind r source-file ~/.tmux.conf

# Count sessions start at 1
set -g base-index 1

# Use vim bindings
setw -g mode-keys vi

# Remap window navigation to vim
unbind-key j
bind-key j select-pane -D
unbind-key k
bind-key k select-pane -U
unbind-key h
bind-key h select-pane -L
unbind-key l
bind-key l select-pane -R
unbind C-b
set -g prefix C-w
bind C-w send-prefix

# Set the title bar
set -g set-titles on
set -g set-titles-string '#(whoami) :: #h :: #(curl ipecho.net/plain;echo)'

# Set status bar
set -g status-utf8 on
set -g status-bg black
set -g status-fg white
set -g status-interval 5
set -g status-left-length 90
set -g status-right-length 60
set -g status-left "#[fg=Green]#(whoami)#[fg=white]::#[fg=blue]#(hostname -s)#[fg=white]::#[fg=yellow]#(curl ipecho.net/plain;echo)"
set -g status-justify left
set -g status-right '#[fg=Cyan]#S #[fg=white]%a %d %b %R'

# History limit for scrollback lines
set-option -g history-limit 5000
"""
    tmux_file = "{0}/.tmux.conf".format(HOME_DIR)
    with open(tmux_file, 'w') as tmux_conf:
        tmux_conf.write(tmux_settings)


def main():
    # Install Vundle (https://github.com/gmarik/Vundle.vim):
    HOME_DIR = os.path.expanduser("~")
    install_vundle(HOME_DIR)

    # Create VIM undo directory
    UNDO_DIR = '{0}/.vim/undodir/'
    make_vim_undo_dir(HOME_DIR, UNDO_DIR)

    # Install Vundle Plug-ins
    install_vundle_plugins(HOME_DIR)

    # Setup Tmux
    tmux_install_status = install_tmux(HOME_DIR)
    make_tmux_config(HOME_DIR)


if __name__ == '__main__':
    main()
