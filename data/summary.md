# robbyrussell/oh-my-zsh
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_plugins_jump_README_md](#_plugins_jump_README_md)

* [_plugins_gcloud_README_md](#_plugins_gcloud_README_md)

* [_plugins_chruby_README_md](#_plugins_chruby_README_md)

* [_plugins_timer_README_md](#_plugins_timer_README_md)

* [_plugins_pj_README_md](#_plugins_pj_README_md)

* [_plugins_sdk_README_md](#_plugins_sdk_README_md)

* [_plugins_ubuntu_README_md](#_plugins_ubuntu_README_md)

* [_plugins_eecms_README_md](#_plugins_eecms_README_md)

* [_plugins_gradle_README_md](#_plugins_gradle_README_md)

* [_plugins_cloudapp_README_md](#_plugins_cloudapp_README_md)

* [_plugins_textastic_README_md](#_plugins_textastic_README_md)

* [_plugins_catimg_README_md](#_plugins_catimg_README_md)

* [_plugins_sbt_README_md](#_plugins_sbt_README_md)

* [_plugins_pyenv_README_md](#_plugins_pyenv_README_md)

* [_plugins_ng_README_md](#_plugins_ng_README_md)

* [_plugins_jsontools_README_md](#_plugins_jsontools_README_md)

* [_plugins_gb_README_md](#_plugins_gb_README_md)

* [_plugins_terraform_README_md](#_plugins_terraform_README_md)

* [_plugins_powify_README_md](#_plugins_powify_README_md)

* [_plugins_git_flow_avh_README_md](#_plugins_git_flow_avh_README_md)

[- Inline](#Inline)

* [_plugins_wd_wd_sh](#_plugins_wd_wd_sh)

* [_plugins_drush_drush_complete_sh](#_plugins_drush_drush_complete_sh)

* [_plugins_git_prompt_gitstatus_py](#_plugins_git_prompt_gitstatus_py)

* [_plugins_z_z_sh](#_plugins_z_z_sh)

* [_plugins_emacs_emacsclient_sh](#_plugins_emacs_emacsclient_sh)

* [_tools_theme_chooser_sh](#_tools_theme_chooser_sh)

* [_tools_install_sh](#_tools_install_sh)

* [_oh_my_zsh_sh](#_oh_my_zsh_sh)

* [_tools_check_for_upgrade_sh](#_tools_check_for_upgrade_sh)

* [_tools_require_tool_sh](#_tools_require_tool_sh)

* [_plugins_gitfast_git_prompt_sh](#_plugins_gitfast_git_prompt_sh)

* [_tools_uninstall_sh](#_tools_uninstall_sh)

* [_plugins_catimg_catimg_sh](#_plugins_catimg_catimg_sh)

* [_tools_upgrade_sh](#_tools_upgrade_sh)

* [_plugins_frontend_search_frontend_search_sh](#_plugins_frontend_search_frontend_search_sh)

[- Issues](#Issues)

* [1677](#1677)

* [2692](#2692)

* [7170](#7170)

* [7600](#7600)

* [5696](#5696)

* [6951](#6951)

* [4861](#4861)

* [7401](#7401)

* [5196](#5196)

* [5073](#5073)

[- Pull](#Pull)

* [2520](#2520)

* [2620](#2620)

* [1969](#1969)

* [5053](#5053)

* [1016](#1016)

* [2551](#2551)

* [1256](#1256)

* [8070](#8070)

* [5307](#5307)

* [4602](#4602)

<!-- toc -->

# Info
## description
🙃 A delightful community-driven (with 1,300+ contributors) framework for managing your zsh configuration. Includes 200+ optional plugins (rails, git, OSX, hub, capistrano, brew, ant, php, python, etc), over 140 themes to spice up your morning, and an auto-update tool so that makes it easy to keep up with the latest updates from the community.

# Markdown
## _plugins_jump_README_md
```# Jump plugin

This plugin allows to easily jump around the file system by manually adding marks.
Those marks are stored as symbolic links in the directory `$MARKPATH` (default `$HOME/.marks`)

To use it, add `jump` to the plugins array in your zshrc file:

zsh
plugins=(... jump)


## Commands

| Command              | Description                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------|
| `jump <mark-name>`   | Jump to the given mark                                                                          |
| `mark [mark-name]`   | Create a mark with the given name or with the name of the current directory if none is provided |
| `unmark <mark-name>` | Remove the given mark                                                                           |
| `marks`              | List the existing marks and the directories they point to                                       |
```
## _plugins_gcloud_README_md
```# gcloud

This plugin provides completion support for the
[Google Cloud SDK CLI](https://cloud.google.com/sdk/gcloud/).

To use it, add `gcloud` to the plugins array in your zshrc file.

zsh
plugins=(... gcloud)


It relies on you having installed the SDK using one of the supported options
listed [here](https://cloud.google.com/sdk/install).

## Plugin Options

* Set `CLOUDSDK_HOME` in your `zshrc` file before you load oh-my-zsh if you have
your GCloud SDK installed in a non-standard location. The plugin will use this
as the base for your SDK if it finds it set already.

* If you do not have a `python2` in your `PATH` you'll also need to set the
`CLOUDSDK_PYTHON` environment variable at the end of your `.zshrc`. This is
used by the SDK to call a compatible interpreter when you run one of the
SDK commands.
```
## _plugins_chruby_README_md
```# chruby plugin

This plugin loads [chruby](https://github.com/postmodern/chruby), a tool that changes the
current Ruby version, and completion and a prompt function to display the Ruby version.
Supports brew and manual installation of chruby.

To use it, add `chruby` to the plugins array in your zshrc file:
zsh
plugins=(... chruby)


## Usage

If you'd prefer to specify an explicit path to load chruby from
you can set variables like so:


zstyle :omz:plugins:chruby path /local/path/to/chruby.sh
zstyle :omz:plugins:chruby auto /local/path/to/auto.sh

```
## _plugins_timer_README_md
```This plugin allows to display command's execution time in a very nonintrusive way.

Timer can be tuned by these two variables:
* `TIMER_PRECISION` allows to control number of decimal places (default `1`)
* `TIMER_FORMAT` allows to adjust display format (default `'/%d'`)

Sample session:

    me@here:~$ sleep 1                                         /1.0s
    me@here:~$ sleep 73                                     /1m13.0s
    me@here:~$ TIMER_FORMAT='[%d]'; TIMER_PRECISION=2        [0.00s]
    me@here:~$ head -c50 < /dev/urandom | hexdump
    0000000 b2 16 20 f0 29 1f 61 2d 8a 29 20 8c 8c 39 5a ab
    0000010 21 47 0e f9 ee a4 76 46 71 9e 4f 6b a4 c4 51 cb
    0000020 f9 1f 7e b9 6f 2c ae dd cf 40 6d 64 a8 fb d3 db
    0000030 09 37
    0000032                                                  [0.02s]
```
## _plugins_pj_README_md
```# pj

The `pj` plugin (short for `Project Jump`) allows you to define several
folders where you store your projects, so that you can jump there directly
by just using the name of the project directory.

Original idea and code by Jan De Poorter ([@DefV](https://github.com/DefV))
Source: https://gist.github.com/pjaspers/368394#gistcomment-1016

## Usage

1. Enable the `pj` plugin:

   zsh
   plugins=(... pj)
   

2. Set `$PROJECT_PATHS` in your ~/.zshrc:

   zsh
   PROJECT_PATHS=(~/src ~/work ~/"dir with spaces")
   

You can now use one of the following commands:

##### `pj my-project`:

`cd` to the directory named "my-project" found in one of the `$PROJECT_PATHS`
directories. If there are several directories named the same, the first one
to appear in `$PROJECT_PATHS` has preference.

For example:
zsh
PROJECT_PATHS=(~/code ~/work)
$ ls ~/code    # ~/code/blog ~/code/react
$ ls ~/work    # ~/work/blog ~/work/project
$ pj blog      # <-- will cd to ~/code/blog


##### `pjo my-project`

Open the project directory with your defined `$EDITOR`. This follows the same
directory rules as the `pj` command above.

Note: `pjo` is an alias of `pj open`.
```
## _plugins_sdk_README_md
```# sdk

Plugin for SDKMAN, a tool for managing parallel versions of multiple Software Development Kits on most Unix based systems.
Provides autocompletion for all known commands.

## Requirements

 * [SDKMAN](http://sdkman.io/)
```
## _plugins_ubuntu_README_md
```# Ubuntu plugin

This plugin adds completions and aliases for [Ubuntu](https://www.ubuntu.com/).

To use it, add `ubuntu` to the plugins array in your zshrc file:

zsh
plugins=(... ubuntu)


## Aliases

Commands that use `$APT` will use `apt` if installed or defer to `apt-get` otherwise.

| Alias   | Command                                                                  | Description                                                                                       |
|---------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| age     | `sudo $APT`                                                              | Run apt-get with sudo                                                                             |
| acs     | `apt-cache search`                                                       | Search the apt-cache with the specified criteria                                                  |
| acp     | `apt-cache policy`                                                       | Display the package source priorities                                                             |
| afs     | `apt-file search --regexp`                                               | Perform a regular expression apt-file search                                                      |
| afu     | `sudo apt-file update`                                                   | Generates or updates the apt-file package database                                                |
| aga     | `sudo $APT autoclean`                                                    | Clears out the local reposityory of retrieved package files that can no longer be downloaded      |
| agb     | `sudo $APT build-dep <source_pkg>`                                       | Installs/Removes packages to satisfy the dependencies of a specified build pkg                    |
| agc     | `sudo $APT clean`                                                        | Clears out the local repository of retrieved package files leaving everything from the lock files |
| agd     | `sudo $APT dselect-upgrade`                                              | Follows dselect choices for package installation                                                  |
| agi     | `sudo $APT install <pkg>`                                                | Install the specified package                                                                     |
| agli    | `apt list --installed`                                                   | List the installed packages                                                                       |
| aglu    | `sudo apt-get -u upgrade --assume-no`                                    | Run an apt-get upgrade assuming no to all prompts                                                 |
| agp     | `sudo $APT purge <pkg>`                                                  | Remove a package including any configuration files                                                |
| agr     | `sudo $APT remove <pkg>`                                                 | Remove a package                                                                                  |
| ags     | `$APT source <pkg>`                                                      | Fetch the source for the specified package                                                        |
| agu     | `sudo $APT update`                                                       | Update package list                                                                               |
| agud    | `sudo $APT update && sudo $APT dist-upgrade`                             | Update packages list and perform a distribution upgrade                                           |
| agug    | `sudo $APT upgrade`                                                      | Upgrade available packages                                                                        |
| agar    | `sudo $APT autoremove`                                                   | Remove automatically installed packages no longer needed                                          |
| aguu    | `sudo $APT update && sudo $APT upgrade`                                  | Update packages list and upgrade available packages                                               |
| allpkgs | `dpkg --get-selections \| grep -v deinstall`                             | Print all installed packages                                                                      |
| kclean  | `sudo aptitude remove -P ?and(~i~nlinux-(ima\|hea) ?not(~n$(uname -r)))` |Remove ALL kernel images and headers EXCEPT the one in use                                         |
| mydeb   | `time dpkg-buildpackage -rfakeroot -us -uc`                              | Create a basic .deb package                                                                       |
| ppap    | `sudo ppa-purge <ppa>`                                                   | Remove the specified PPA                                                                          |


## Functions

| Function          | Usage                                 |Description                                                               |
|-------------------|---------------------------------------|--------------------------------------------------------------------------|
| aar               | `aar ppa:xxxxxx/xxxxxx [packagename]` | apt-add-repository with automatic install/upgrade of the desired package |
| apt-history       | `apt-history <action>`                | Prints the Apt history of the specified action                           |
| apt-list-packages | `apt-list-packages`                   | List packages by size                                                    |
| kerndeb           | `kerndeb`                             | Kernel-package building shortcut                                         |

## Authors:

- [@AlexBio](https://github.com/AlexBio)
- [@dbb](https://github.com/dbb)
- [@Mappleconfusers](https://github.com/Mappleconfusers)
- [@trinaldi](https://github.com/trinaldi)
- [Nicolas Jonas](https://nextgenthemes.com)
- [@loctauxphilippe](https://github.com/loctauxphilippe)
- [@HaraldNordgren](https://github.com/HaraldNordgren)
```
## _plugins_eecms_README_md
```# eecms plugin

This plugin adds auto-completion of console commands for [`eecms`](https://github.com/ExpressionEngine/ExpressionEngine).

To use it, add `eecms` to the plugins array of your `.zshrc` file:

plugins=(... eecms)


It also adds the alias `eecms` which finds the eecms file in the current project
and runs it with php.
```
## _plugins_gradle_README_md
```## Gradle Plugin

This plugin adds completions and aliases for [Gradle](https://gradle.org/).

To use it, add `gradle` to the plugins array in your zshrc file:

zsh
plugins=(... gradle)


## Usage

This plugin creates an alias `gradle` which is used to determine whether the current working directory has a gradlew file. If gradlew is present it will be used otherwise `gradle` is used directly. Gradle tasks can be executed directly without regard for whether it is `gradle` or `gradlew`

Examples:
zsh
gradle test
gradle build


## Completion

The completion provided for this plugin caches the parsed tasks into a file named `.gradletasknamecache` in the current working directory, so you might want to add that to your `.gitignore` file so that it's not accidentally committed.
```
## _plugins_cloudapp_README_md
```# CloudApp plugin

[CloudApp](https://www.getcloudapp.com) brings screen recording, screenshots, and GIF creation to the cloud, in an easy-to-use enterprise-level app. The CloudApp plugin allows you to upload a file to your CloadApp account from the command line.

To use it, add `cloudapp` to the plugins array of your `~/.zshrc` file:


plugins=(... dash)


## Requirements

1. [Aaron Russell's `cloudapp_api` gem](https://github.com/aaronrussell/cloudapp_api#installation)

2. That you set your CloudApp credentials in `~/.cloudapp` as a simple text file like below:
   
   email
   password
   

## Usage

- `cloudapp <filename>`: uploads `<filename>` to your CloudApp account, and if you're using
  macOS, copies the URL to your clipboard.
```
## _plugins_textastic_README_md
```## textastic

Plugin for Textastic, a text and code editor for Mac OS X

### Requirements

 * [Textastic](https://www.textasticapp.com/mac.html)

### Usage

 * If `tt` command is called without an argument, launch Textastic

 * If `tt` is passed a directory, cd to it and open it in Textastic

 * If `tt` is passed a file, open it in Textastic
```
## _plugins_catimg_README_md
```# catimg

Plugin for displaying images on the terminal using the the `catimg.sh` script provided by [posva](https://github.com/posva/catimg)

## Requirements

- `convert` (ImageMagick)

## Enabling the plugin

1. Open your `.zshrc` file and add `catimg` in the plugins section:

   zsh
   plugins=(
       # all your enabled plugins
       catimg
   )
   

2. Reload the source file or restart your Terminal session:

   console
   $ source ~/.zshrc
   $
   

## Functions

| Function | Description                              |
| -------- | ---------------------------------------- |
| `catimg` | Displays the given image on the terminal |

## Usage examples

[![asciicast](https://asciinema.org/a/204702.png)](https://asciinema.org/a/204702)
```
## _plugins_sbt_README_md
```# sbt plugin

This plugin adds completion for the [sbt, the interactive build tool](https://scala-sbt.org/),
as well as some aliases for common sbt commands.

To use it, add `sbt` to the plugins array in your zshrc file:

zsh
plugins=(... sbt)


## Aliases

| Alias | Command               | Description                                                  |
|-------|-----------------------|--------------------------------------------------------------|
| sbc   | `sbt compile`         | Compiles the main sources                                    |
| sbcln | `sbt clean`           | Deletes all generated files                                  |
| sbcc  | `sbt clean compile`   | Deletes generated files, compiles the main sources           |
| sbco  | `sbt console`         | Starts Scala with the compiled sources and all dependencies  |
| sbcq  | `sbt console-quick`   | Starts Scala with all dependencies                           |
| sbcp  | `sbt console-project` | Starts Scala with sbt and the build definitions              |
| sbd   | `sbt doc`             | Generates API documentation for Scala source files           |
| sbdc  | `sbt dist:clean`      | Deletes the distribution packages                            |
| sbdi  | `sbt dist`            | Creates the distribution packages                            |
| sbgi  | `sbt gen-idea`        | Create Idea project files                                    |
| sbp   | `sbt publish`         | Publishes artifacts to the repository                        |
| sbpl  | `sbt publish-local`   | Publishes artifacts to the local Ivy repository              |
| sbr   | `sbt run`             | Runs the main class for the project                          |
| sbrm  | `sbt run-main`        | Runs the specified main class for the project                |
| sbu   | `sbt update`          | Resolves and retrieves external dependencies                 |
| sbx   | `sbt test`            | Compiles and runs all tests                                  |
| sba   | `sbt assembly`        | Create a fat JAR with all dependencies                       |
```
## _plugins_pyenv_README_md
```# pyenv 

This plugin looks for [pyenv](https://github.com/pyenv/pyenv), a Simple Python version
management system, and loads it if it's found. It also loads pyenv-virtualenv, a pyenv
plugin to manage virtualenv, if it's found.

To use it, add `pyenv` to the plugins array in your zshrc file:

zsh
plugins=(... pyenv)


## Functions

- `pyenv_prompt_info`: displays the Python version in use by pyenv; or the global Python
  version, if pyenv wasn't found.
```
## _plugins_ng_README_md
```## NG Plugin

This [ng plugin](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/ng)
 adds completion support for Angular's CLI (named ng).

Ng is hosted on [ng home](https://github.com/catull/angular-cli)

It is used to generate Angular 2 app "stubs", build those apps, configure them,
test them, lint them etc.

Ahem, "stubs" is not what Angular engineers refer to the items ng can generate
for you.

"Stubs" can be any one of:
- class
- component
- directive
- enum
- module
- pipe
- route
- service

At the moment, `ng completion` creates a very rough completion for Zsh and
Bash.

It is missing most of the options and a few arguments.
In future, this plugin may be shortened to simply being

zsh
eval `ng completion`


There is hope this materialises in the 21st century.

### CONTRIBUTOR
 - Carlo Dapor ([catull](https://github.com/catull))
```
## _plugins_jsontools_README_md
```# jsontools

Handy command line tools for dealing with json data.

## Tools

- **pp_json** - pretty prints json
- **is_json** - returns true if valid json; false otherwise
- **urlencode_json** - returns a url encoded string for the given json 
- **urldecode_json** - returns decoded json for the given url encoded string

## Usage
Usage is simple...just take your json data and pipe it into the appropriate jsontool.
sh
<json data> | <jsontools tool>

## Examples

##### pp_json

sh
# curl json data and pretty print the results
curl https://coderwall.com/bobwilliams.json | pp_json


##### is_json
sh
# pretty print the contents of an existing json file
less data.json | is_json


##### urlencode_json
sh
# json data directly from the command line
echo '{"b":2, "a":1}' | urlencode_json


##### urldecode_json
sh
# url encoded string to decode
echo '%7B%22b%22:2,%20%22a%22:1%7D%0A' | urldecode_json
```
## _plugins_gb_README_md
```# `gb` plugin

> A project based build tool for the Go programming language.

See https://getgb.io for the full `gb` documentation

* * * *

- Adds completion support for all `gb` commands.
- Also supports completion for the [`gb-vendor` plugin](https://godoc.org/github.com/constabulary/gb/cmd/gb-vendor).

To use it, add `gb` to your plugins array:
sh
plugins=(... gb)


## Caveats

The `git` plugin defines an alias `gb` that usually conflicts with the `gb` program.
If you're having trouble with it, remove it by adding `unalias gb` at the end of your
zshrc file.
```
## _plugins_terraform_README_md
```## Terraform oh-my-zsh plugin

Plugin for Terraform, a tool from Hashicorp for managing infrastructure safely and efficiently.

Current as of Terraform v0.11.7

### Requirements

 * [Terraform](https://terraform.io/)

### Usage

To use it, add `terraform` to the plugins array of your `~/.zshrc` file:

shell
plugins=(... terraform)


 * Type `terraform` into your prompt and hit `TAB` to see available completion options

### Expanding ZSH prompt with current Terraform workspace name

If you want to get current Terraform workspace name in your ZSH prompt open
your .zsh-theme file and in a chosen place insert:

shell
PROMPT=$'%{$fg[white]%}$(tf_prompt_info)%{$reset_color%} '

```
## _plugins_powify_README_md
```# powify plugin

This plugin adds autocompletion for [powify](https://github.com/sethvargo/powify),
an easy-to-use wrapper for Basecamp's [pow](https://github.com/basecamp/pow).

To use it, add powify to the plugins array of your zshrc file:

sh
plugins=(... powify)

```
## _plugins_git_flow_avh_README_md
```# git-flow (AVH Edition) plugin

This plugin adds completion for the [git-flow (AVH Edition)](https://github.com/petervanderdoes/gitflow-avh).
The AVH Edition of the git extensions that provides high-level repository operations for [Vincent Driessen's branching model](https://nvie.com/posts/a-successful-git-branching-model/).

To use it, add `git-flow-avh` to the plugins array in your zshrc file:

zsh
plugins=(... git-flow-avh)


## Requirements

1. The git-flow tool has to be [installed](https://github.com/petervanderdoes/gitflow-avh#installing-git-flow)
   separately.

2. You have to use zsh's git completion instead of the git project's git completion. This is typically
   done by default so you don't need to do anything else. If you installed git with Homebrew you
   might have to uninstall the git completion it's bundled with.
```
# Inline
## _plugins_wd_wd_sh
### Line 1-37
```
#!/bin/zsh

# WARP DIRECTORY
# ==============
# Jump to custom directories in terminal
# because `cd` takes too long...
#
# @github.com/mfaerevaag/wd

# version
readonly WD_VERSION=0.4.6

# colors
readonly WD_BLUE="\033[96m"
readonly WD_GREEN="\033[92m"
readonly WD_YELLOW="\033[93m"
readonly WD_RED="\033[91m"
readonly WD_NOC="\033[m"

## functions

# helpers
wd_yesorno()
{
    # variables
    local question="${1}"
    local prompt="${question} "
    local yes_RETVAL="0"
    local no_RETVAL="3"
    local RETVAL=""
    local answer=""

    # read-eval loop
    while true ; do
        printf $prompt
        read -r answer

```
### Line 127-136
```
        wd_exit_fail "Unknown warp point '${name_arg}'"
        break
    fi
}

# core

wd_warp()
{
    local point=$1
```
### Line 182-192
```
        wd_remove $point > /dev/null
        printf "%q:%s\n" "${point}" "${PWD/#$HOME/~}" >> $WD_CONFIG

        wd_print_msg $WD_GREEN "Warp point added"

        # override exit code in case wd_remove did not remove any points
        # TODO: we should handle this kind of logic better
        WD_EXIT_CODE=0
    else
        wd_exit_warn "Warp point '${point}' already exists. Use 'add!' to overwrite."
    fi
```
### Line 263-272
```
}

wd_show()
{
    local name_arg=$1
    # if there's an argument we look up the value
    if [[ ! -z $name_arg ]]
    then
        if [[ -z $points[$name_arg] ]]
        then
```
### Line 273-285
```
            wd_print_msg $WD_BLUE "No warp point named $name_arg"
        else
            wd_print_msg $WD_GREEN "Warp point: ${WD_GREEN}$name_arg${WD_NOC} -> $points[$name_arg]"
        fi
    else
        # hax to create a local empty array
        local wd_matches
        wd_matches=()
        # do a reverse lookup to check whether PWD is in $points
        PWD="${PWD/$HOME/~}"
        if [[ ${points[(r)$PWD]} == $PWD ]]
        then
            for name in ${(k)points}
```
### Line 337-348
```
local WD_CONFIG=$HOME/.warprc
local WD_QUIET=0
local WD_EXIT_CODE=0
local WD_DEBUG=0

# Parse 'meta' options first to avoid the need to have them before
# other commands. The `-D` flag consumes recognized options so that
# the actual command parsing won't be affected.

zparseopts -D -E \
    c:=wd_alt_config -config:=wd_alt_config \
    q=wd_quiet_mode -quiet=wd_quiet_mode \
```
### Line 357-402
```
if [[ ! -z $wd_alt_config ]]
then
    WD_CONFIG=$wd_alt_config[2]
fi

# check if config file exists
if [ ! -e $WD_CONFIG ]
then
    # if not, create config file
    touch $WD_CONFIG
fi

# load warp points
typeset -A points
while read -r line
do
    arr=(${(s,:,)line})
    key=${arr[1]}
    # join the rest, in case the path contains colons
    val=${(j,:,)arr[2,-1]}

    points[$key]=$val
done < $WD_CONFIG

# get opts
args=$(getopt -o a:r:c:lhs -l add:,rm:,clean\!,list,ls:,path:,help,show -- $*)

# check if no arguments were given, and that version is not set
if [[ ($? -ne 0 || $#* -eq 0) && -z $wd_print_version ]]
then
    wd_print_usage

    # check if config file is writeable
elif [ ! -w $WD_CONFIG ]
then
    # do nothing
    # can't run `exit`, as this would exit the executing shell
    wd_exit_fail "\'$WD_CONFIG\' is not writeable."

else

    # parse rest of options
    for o
    do
        case "$o"
            in
```
### Line 449-460
```
                ;;
        esac
    done
fi

## garbage collection
# if not, next time warp will pick up variables from this run
# remember, there's no sub shell

unset wd_warp
unset wd_add
unset wd_remove
```

## _plugins_drush_drush_complete_sh
### Line 1-19
```
# BASH completion script for Drush.
#
# Place this in your /etc/bash_completion.d/ directory or source it from your
# ~/.bash_completion or ~/.bash_profile files.  Alternatively, source
# examples/example.bashrc instead, as it will automatically find and source
# this file.
#
# If you're using ZSH instead of BASH, add the following to your ~/.zshrc file
# and source it.
#
#   autoload bashcompinit
#   bashcompinit
#   source /path/to/your/drush.complete.sh

# Ensure drush is available.
which drush > /dev/null || alias drush &> /dev/null || return

__drush_ps1() {
  f="${TMPDIR:-/tmp/}/drush-env-${USER}/drush-drupal-site-$$"
```
### Line 22-50
```
    __DRUPAL_SITE=$(cat "$f")
  else
    __DRUPAL_SITE="$DRUPAL_SITE"
  fi

  # Set DRUSH_PS1_SHOWCOLORHINTS to a non-empty value and define a
  # __drush_ps1_colorize_alias() function for color hints in your Drush PS1
  # prompt. See example.prompt.sh for an example implementation.
  if [ -n "${__DRUPAL_SITE-}" ] && [ -n "${DRUSH_PS1_SHOWCOLORHINTS-}" ]; then
    __drush_ps1_colorize_alias
  fi

  [[ -n "$__DRUPAL_SITE" ]] && printf "${1:- (%s)}" "$__DRUPAL_SITE"
}

# Completion function, uses the "drush complete" command to retrieve
# completions for a specific command line COMP_WORDS.
_drush_completion() {
  # Set IFS to newline (locally), since we only use newline separators, and
  # need to retain spaces (or not) after completions.
  local IFS=$'\n'
  # The '< /dev/null' is a work around for a bug in php libedit stdin handling.
  # Note that libedit in place of libreadline in some distributions. See:
  # https://bugs.launchpad.net/ubuntu/+source/php5/+bug/322214
  COMPREPLY=( $(drush --early=includes/complete.inc "${COMP_WORDS[@]}" < /dev/null 2> /dev/null) )
}

# Register our completion function. We include common short aliases for Drush.
complete -o bashdefault -o default -o nospace -F _drush_completion d dr drush drush5 drush6 drush7 drush8 drush.php
```

## _plugins_git_prompt_gitstatus_py
### Line 1-5
```
#!/usr/bin/env python
from __future__ import print_function

import os
import sys
```
### Line 11-24
```
def get_tagname_or_hash():
    """return tagname if exists else hash"""
    cmd = 'git log -1 --format="%h%d"'
    output = check_output(shlex.split(cmd)).decode('utf-8').strip()
    hash_, tagname = None, None
    # get hash
    m = re.search('\(.*\)$', output)
    if m:
        hash_ = output[:m.start()-1]
    # get tagname
    m = re.search('tag: .*[,\)]', output)
    if m:
        tagname = 'tags/' + output[m.start()+len('tag: '): m.end()-1]

```
### Line 27-43
```
    elif hash_:
        return hash_
    return None


# `git status --porcelain --branch` can collect all information
# branch, remote_branch, untracked, staged, changed, conflicts, ahead, behind
po = Popen(['git', 'status', '--porcelain', '--branch'], env=dict(os.environ, LANG="C"), stdout=PIPE, stderr=PIPE)
stdout, sterr = po.communicate()
if po.returncode != 0:
    sys.exit(0)  # Not a git repository

# collect git status information
untracked, staged, changed, conflicts = [], [], [], []
ahead, behind = 0, 0
status = [(line[0], line[1], line[2:]) for line in stdout.decode('utf-8').splitlines()]
for st in status:
```
### Line 47-62
```
        elif re.search('no branch', st[2]):  # detached status
            branch = get_tagname_or_hash()
        elif len(st[2].strip().split('...')) == 1:
            branch = st[2].strip()
        else:
            # current and remote branch info
            branch, rest = st[2].strip().split('...')
            if len(rest.split(' ')) == 1:
                # remote_branch = rest.split(' ')[0]
                pass
            else:
                # ahead or behind
                divergence = ' '.join(rest.split(' ')[1:])
                divergence = divergence.lstrip('[').rstrip(']')
                for div in divergence.split(', '):
                    if 'ahead' in div:
```

## _plugins_z_z_sh
### Line 1-29
```
# Copyright (c) 2009 rupa deadwyler. Licensed under the WTFPL license, Version 2

# maintains a jump-list of the directories you actually use
#
# INSTALL:
#     * put something like this in your .bashrc/.zshrc:
#         . /path/to/z.sh
#     * cd around for a while to build up the db
#     * PROFIT!!
#     * optionally:
#         set $_Z_CMD in .bashrc/.zshrc to change the command (default z).
#         set $_Z_DATA in .bashrc/.zshrc to change the datafile (default ~/.z).
#         set $_Z_NO_RESOLVE_SYMLINKS to prevent symlink resolution.
#         set $_Z_NO_PROMPT_COMMAND if you're handling PROMPT_COMMAND yourself.
#         set $_Z_EXCLUDE_DIRS to an array of directories to exclude.
#         set $_Z_OWNER to your username if you want use z while sudo with $HOME kept
#
# USE:
#     * z foo     # cd to most frecent dir matching foo
#     * z foo bar # cd to most frecent dir matching foo and bar
#     * z -r foo  # cd to highest ranked dir matching foo
#     * z -t foo  # cd to most recently accessed dir matching foo
#     * z -l foo  # list matches instead of cd
#     * z -e foo  # echo the best match, don't cd
#     * z -c foo  # restrict matches to subdirs of $PWD

[ -d "${_Z_DATA:-$HOME/.z}" ] && {
    echo "ERROR: z.sh's datafile (${_Z_DATA:-$HOME/.z}) is a directory."
}
```
### Line 30-75
```

_z() {

    local datafile="${_Z_DATA:-$HOME/.z}"

    # if symlink, dereference
    [ -h "$datafile" ] && datafile=$(readlink "$datafile")

    # bail if we don't own ~/.z and $_Z_OWNER not set
    [ -z "$_Z_OWNER" -a -f "$datafile" -a ! -O "$datafile" ] && return

    _z_dirs () {
        local line
        while read line; do
            # only count directories
            [ -d "${line%%\|*}" ] && echo "$line"
        done < "$datafile"
        return 0
    }

    # add entries
    if [ "$1" = "--add" ]; then
        shift

        # $HOME isn't worth matching
        [ "$*" = "$HOME" ] && return

        # don't track excluded directory trees
        local exclude
        for exclude in "${_Z_EXCLUDE_DIRS[@]}"; do
            case "$*" in "$exclude*") return;; esac
        done

        # maintain the data file
        local tempfile="$datafile.$RANDOM"
        _z_dirs | awk -v path="$*" -v now="$(date +%s)" -F"|" '
            BEGIN {
                rank[path] = 1
                time[path] = now
            }
            $2 >= 1 {
                # drop ranks below 1
                if( $1 == path ) {
                    rank[$1] = $2 + 1
                    time[$1] = now
                } else {
```
### Line 78-100
```
                }
                count += $2
            }
            END {
                if( count > 9000 ) {
                    # aging
                    for( x in rank ) print x "|" 0.99*rank[x] "|" time[x]
                } else for( x in rank ) print x "|" rank[x] "|" time[x]
            }
        ' 2>/dev/null >| "$tempfile"
        # do our best to avoid clobbering the datafile in a race condition.
        if [ $? -ne 0 -a -f "$datafile" ]; then
            env rm -f "$tempfile"
        else
            [ "$_Z_OWNER" ] && chown $_Z_OWNER:"$(id -ng $_Z_OWNER)" "$tempfile"
            env mv -f "$tempfile" "$datafile" || env rm -f "$tempfile"
        fi

    # tab completion
    elif [ "$1" = "--complete" -a -s "$datafile" ]; then
        _z_dirs | awk -v q="$2" -F"|" '
            BEGIN {
                q = substr(q, 3)
```
### Line 107-116
```
                } else if( $1 ~ q ) print $1
            }
        ' 2>/dev/null

    else
        # list/go
        local echo fnd last list opt typ
        while [ "$1" ]; do case "$1" in
            --) while [ "$1" ]; do shift; fnd="$fnd${fnd:+ }$1";done;;
            -*) opt=${1:1}; while [ "$opt" ]; do case ${opt:0:1} in
```
### Line 124-153
```
                esac; opt=${opt:1}; done;;
             *) fnd="$fnd${fnd:+ }$1";;
        esac; last=$1; [ "$#" -gt 0 ] && shift; done
        [ "$fnd" -a "$fnd" != "^$PWD " ] || list=1

        # if we hit enter on a completion just go there
        case "$last" in
            # completions will always start with /
            /*) [ -z "$list" -a -d "$last" ] && builtin cd "$last" && return;;
        esac

        # no file yet
        [ -f "$datafile" ] || return

        local cd
        cd="$( < <( _z_dirs ) awk -v t="$(date +%s)" -v list="$list" -v typ="$typ" -v q="$fnd" -F"|" '
            function frecent(rank, time) {
                # relate frequency and time
                dx = t - time
                if( dx < 3600 ) return rank * 4
                if( dx < 86400 ) return rank * 2
                if( dx < 604800 ) return rank / 2
                return rank / 4
            }
            function output(matches, best_match, common) {
                # list or return the desired directory
                if( list ) {
                    cmd = "sort -g >&2"
                    for( x in matches ) {
                        if( matches[x] ) {
```
### Line 161-170
```
                    if( common ) best_match = common
                    print best_match
                }
            }
            function common(matches) {
                # find the common root of a list of matches, if it exists
                for( x in matches ) {
                    if( matches[x] && (!short || length(x) < length(short)) ) {
                        short = x
                    }
```
### Line 195-204
```
                    ibest_match = $1
                    ihi_rank = imatches[$1]
                }
            }
            END {
                # prefer case sensitive
                if( best_match ) {
                    output(matches, best_match, common(matches))
                } else if( ibest_match ) {
                    output(imatches, ibest_match, common(imatches))
```
### Line 215-258
```
alias ${_Z_CMD:-z}='_z 2>&1'

[ "$_Z_NO_RESOLVE_SYMLINKS" ] || _Z_RESOLVE_SYMLINKS="-P"

if type compctl >/dev/null 2>&1; then
    # zsh
    [ "$_Z_NO_PROMPT_COMMAND" ] || {
        # populate directory list, avoid clobbering any other precmds.
        if [ "$_Z_NO_RESOLVE_SYMLINKS" ]; then
            _z_precmd() {
                (_z --add "${PWD:a}" &)
                # Reference $RANDOM to refresh its value inside the subshell
                # Otherwise, multiple runs get the same value
                : $RANDOM
            }
        else
            _z_precmd() {
                (_z --add "${PWD:A}" &)
                # Reference $RANDOM to refresh its value inside the subshell
                # Otherwise, multiple runs get the same value
                : $RANDOM
            }
        fi
        [[ -n "${precmd_functions[(r)_z_precmd]}" ]] || {
            precmd_functions[$(($#precmd_functions+1))]=_z_precmd
        }
    }
    _z_zsh_tab_completion() {
        # tab completion
        local compl
        read -l compl
        reply=(${(f)"$(_z --complete "$compl")"})
    }
    compctl -U -K _z_zsh_tab_completion _z
elif type complete >/dev/null 2>&1; then
    # bash
    # tab completion
    complete -o filenames -C '_z --complete "$COMP_LINE"' ${_Z_CMD:-z}
    [ "$_Z_NO_PROMPT_COMMAND" ] || {
        # populate directory list. avoid clobbering other PROMPT_COMMANDs.
        grep "_z --add" <<< "$PROMPT_COMMAND" >/dev/null || {
            PROMPT_COMMAND="$PROMPT_COMMAND"$'\n''(_z --add "$(command pwd '$_Z_RESOLVE_SYMLINKS' 2>/dev/null)" 2>/dev/null &);'
        }
    }
```

## _plugins_emacs_emacsclient_sh
### Line 1-24
```
#!/bin/sh

_emacsfun()
{
    # get list of emacs frames.
    frameslist=`emacsclient --alternate-editor '' --eval '(frame-list)' 2>/dev/null | egrep -o '(frame)+'`

    if [ "$(echo "$frameslist" | sed -n '$=')" -ge 2 ] ;then
        # prevent creating another X frame if there is at least one present.
        emacsclient --alternate-editor "" "$@"
    else
        # Create one if there is no X window yet.
        emacsclient --alternate-editor "" --create-frame "$@"
    fi
}


# adopted from https://github.com/davidshepherd7/emacs-read-stdin/blob/master/emacs-read-stdin.sh
# If the second argument is - then write stdin to a tempfile and open the
# tempfile. (first argument will be `--no-wait` passed in by the plugin.zsh)
if [ "$#" -ge "2" -a "$2" = "-" ]
then
    tempfile="$(mktemp emacs-stdin-$USER.XXXXXXX --tmpdir)"
    cat - > "$tempfile"
```

## _tools_theme_chooser_sh

## _tools_install_sh
### Line 1-44
```
#!/bin/sh
#
# This script should be run via curl:
#   sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
# or wget:
#   sh -c "$(wget -qO- https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
#
# As an alternative, you can first download the install script and run it afterwards:
#   wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh
#   sh install.sh
#
# You can tweak the install behavior by setting variables when running the script. For
# example, to change the path to the Oh My Zsh repository:
#   ZSH=~/.zsh sh install.sh
#
# Respects the following environment variables:
#   ZSH     - path to the Oh My Zsh repository folder (default: $HOME/.oh-my-zsh)
#   REPO    - name of the GitHub repo to install from (default: robbyrussell/oh-my-zsh)
#   REMOTE  - full remote URL of the git repo to install (default: GitHub via HTTPS)
#   BRANCH  - branch to check out immediately after install (default: master)
#
# Other options:
#   CHSH    - 'no' means the installer will not change the default shell (default: yes)
#   RUNZSH  - 'no' means the installer will not run zsh after the install (default: yes)
#
# You can also pass some arguments to the install script to set some these options:
#   --skip-chsh: has the same behavior as setting CHSH to 'no'
#   --unattended: sets both CHSH and RUNZSH to 'no'
# For example:
#   sh install.sh --unattended
#
set -e

# Default settings
ZSH=${ZSH:-~/.oh-my-zsh}
REPO=${REPO:-robbyrussell/oh-my-zsh}
REMOTE=${REMOTE:-https://github.com/${REPO}.git}
BRANCH=${BRANCH:-master}

# Other options
CHSH=${CHSH:-yes}
RUNZSH=${RUNZSH:-yes}


```
### Line 49-58
```
error() {
	echo ${RED}"Error: $@"${RESET} >&2
}

setup_color() {
	# Only use colors if connected to a terminal
	if [ -t 1 ]; then
		RED=$(printf '\033[31m')
		GREEN=$(printf '\033[32m')
		YELLOW=$(printf '\033[33m')
```
### Line 68-81
```
		RESET=""
	fi
}

setup_ohmyzsh() {
	# Prevent the cloned repository from having insecure permissions. Failing to do
	# so causes compinit() calls to fail with "command not found: compdef" errors
	# for users with insecure umasks (e.g., "002", allowing group writability). Note
	# that this will be ignored under Cygwin by default, as Windows ACLs take
	# precedence over umasks except for filesystems mounted with option "noacl".
	umask g-w,o-w

	echo "${BLUE}Cloning Oh My Zsh...${RESET}"

```
### Line 101-115
```

	echo
}

setup_zshrc() {
	# Keep most recent old .zshrc at .zshrc.pre-oh-my-zsh, and older ones
	# with datestamp of installation that moved them aside, so we never actually
	# destroy a user's original zshrc
	echo "${BLUE}Looking for an existing zsh config...${RESET}"

	# Must use this exact name so uninstall.sh can find it
	OLD_ZSHRC=~/.zshrc.pre-oh-my-zsh
	if [ -f ~/.zshrc ] || [ -h ~/.zshrc ]; then
		if [ -e "$OLD_ZSHRC" ]; then
			OLD_OLD_ZSHRC="${OLD_ZSHRC}-$(date +%Y-%m-%d_%H-%M-%S)"
```
### Line 137-156
```

	echo
}

setup_shell() {
	# Skip setup if the user wants or stdin is closed (not running interactively).
	if [ $CHSH = no ]; then
		return
	fi

	# If this user's login shell is already "zsh", do not attempt to switch.
	if [ "$(basename "$SHELL")" = "zsh" ]; then
		return
	fi

	# If this platform doesn't provide a "chsh" command, bail out.
	if ! command_exists chsh; then
		cat <<-EOF
			I can't change your shell automatically because this system does not have chsh.
			${BLUE}Please manually change your default shell to zsh${RESET}
```
### Line 158-183
```
		return
	fi

	echo "${BLUE}Time to change your default shell to zsh:${RESET}"

	# Prompt for user choice on changing the default login shell
	printf "${YELLOW}Do you want to change your default shell to zsh? [Y/n]${RESET} "
	read opt
	case $opt in
		y*|Y*|"") echo "Changing the shell..." ;;
		n*|N*) echo "Shell change skipped."; return ;;
		*) echo "Invalid choice. Shell change skipped."; return ;;
	esac

	# Check if we're running on Termux
	case "$PREFIX" in
		*com.termux*) termux=true; zsh=zsh ;;
		*) termux=false ;;
	esac

	if [ "$termux" != true ]; then
		# Test for the right location of the "shells" file
		if [ -f /etc/shells ]; then
			shells_file=/etc/shells
		elif [ -f /usr/share/defaults/etc/shells ]; then # Solus OS
			shells_file=/usr/share/defaults/etc/shells
```
### Line 184-195
```
		else
			error "could not find /etc/shells file. Change your default shell manually."
			return
		fi

		# Get the path to the right zsh binary
		# 1. Use the most preceding one based on $PATH, then check that it's in the shells file
		# 2. If that fails, get a zsh path from the shells file, then check it actually exists
		if ! zsh=$(which zsh) || ! grep -qx "$zsh" "$shells_file"; then
			if ! zsh=$(grep '^/.*/zsh$' "$shells_file" | tail -1) || [ ! -f "$zsh" ]; then
				error "no zsh binary found or not present in '$shells_file'"
				error "change your default shell manually."
```
### Line 196-212
```
				return
			fi
		fi
	fi

	# We're going to change the default shell, so back up the current one
	if [ -n "$SHELL" ]; then
		echo $SHELL > ~/.shell.pre-oh-my-zsh
	else
		grep "^$USER:" /etc/passwd | awk -F: '{print $7}' > ~/.shell.pre-oh-my-zsh
	fi

	# Actually change the default shell to zsh
	if ! chsh -s "$zsh"; then
		error "chsh command unsuccessful. Change your default shell manually."
	else
		export SHELL="$zsh"
```
### Line 215-230
```

	echo
}

main() {
	# Run as unattended if stdin is closed
	if [ ! -t 0 ]; then
		RUNZSH=no
		CHSH=no
	fi

	# Parse arguments
	while [ $# -gt 0 ]; do
		case $1 in
			--unattended) RUNZSH=no; CHSH=no ;;
			--skip-chsh) CHSH=no ;;
```

## _oh_my_zsh_sh
### Line 1-30
```
# Set ZSH_CACHE_DIR to the path where cache files should be created
# or else we will use the default cache/
if [[ -z "$ZSH_CACHE_DIR" ]]; then
  ZSH_CACHE_DIR="$ZSH/cache"
fi

# Migrate .zsh-update file to $ZSH_CACHE_DIR
if [ -f ~/.zsh-update ] && [ ! -f ${ZSH_CACHE_DIR}/.zsh-update ]; then
    mv ~/.zsh-update ${ZSH_CACHE_DIR}/.zsh-update
fi

# Check for updates on initial load...
if [ "$DISABLE_AUTO_UPDATE" != "true" ]; then
  env ZSH=$ZSH ZSH_CACHE_DIR=$ZSH_CACHE_DIR DISABLE_UPDATE_PROMPT=$DISABLE_UPDATE_PROMPT zsh -f $ZSH/tools/check_for_upgrade.sh
fi

# Initializes Oh My Zsh

# add a function path
fpath=($ZSH/functions $ZSH/completions $fpath)

# Load all stock functions (from $fpath files) called below.
autoload -U compaudit compinit

# Set ZSH_CUSTOM to the path where your custom config files
# and plugins exists, or else we will use the default custom/
if [[ -z "$ZSH_CUSTOM" ]]; then
    ZSH_CUSTOM="$ZSH/custom"
fi

```
### Line 34-44
```
  local name=$2
  test -f $base_dir/plugins/$name/$name.plugin.zsh \
    || test -f $base_dir/plugins/$name/_$name
}

# Add all defined plugins to fpath. This must be done
# before running compinit.
for plugin ($plugins); do
  if is_plugin $ZSH_CUSTOM $plugin; then
    fpath=($ZSH_CUSTOM/plugins/$plugin $fpath)
  elif is_plugin $ZSH $plugin; then
```
### Line 46-103
```
  else
    echo "[oh-my-zsh] plugin '$plugin' not found"
  fi
done

# Figure out the SHORT hostname
if [[ "$OSTYPE" = darwin* ]]; then
  # macOS's $HOST changes with dhcp, etc. Use ComputerName if possible.
  SHORT_HOST=$(scutil --get ComputerName 2>/dev/null) || SHORT_HOST=${HOST/.*/}
else
  SHORT_HOST=${HOST/.*/}
fi

# Save the location of the current completion dump file.
if [ -z "$ZSH_COMPDUMP" ]; then
  ZSH_COMPDUMP="${ZDOTDIR:-${HOME}}/.zcompdump-${SHORT_HOST}-${ZSH_VERSION}"
fi

if [[ $ZSH_DISABLE_COMPFIX != true ]]; then
  source $ZSH/lib/compfix.zsh
  # If completion insecurities exist, warn the user
  handle_completion_insecurities
  # Load only from secure directories
  compinit -i -C -d "${ZSH_COMPDUMP}"
else
  # If the user wants it, load from all found directories
  compinit -u -C -d "${ZSH_COMPDUMP}"
fi


# Load all of the config files in ~/oh-my-zsh that end in .zsh
# TIP: Add files you don't want in git to .gitignore
for config_file ($ZSH/lib/*.zsh); do
  custom_config_file="${ZSH_CUSTOM}/lib/${config_file:t}"
  [ -f "${custom_config_file}" ] && config_file=${custom_config_file}
  source $config_file
done

# Load all of the plugins that were defined in ~/.zshrc
for plugin ($plugins); do
  if [ -f $ZSH_CUSTOM/plugins/$plugin/$plugin.plugin.zsh ]; then
    source $ZSH_CUSTOM/plugins/$plugin/$plugin.plugin.zsh
  elif [ -f $ZSH/plugins/$plugin/$plugin.plugin.zsh ]; then
    source $ZSH/plugins/$plugin/$plugin.plugin.zsh
  fi
done

# Load all of your custom configurations from custom/
for config_file ($ZSH_CUSTOM/*.zsh(N)); do
  source $config_file
done
unset config_file

# Load the theme
if [[ "$ZSH_THEME" == "random" ]]; then
  if [[ "${(t)ZSH_THEME_RANDOM_CANDIDATES}" = "array" ]] && [[ "${#ZSH_THEME_RANDOM_CANDIDATES[@]}" -gt 0 ]]; then
    themes=($ZSH/themes/${^ZSH_THEME_RANDOM_CANDIDATES}.zsh-theme)
  else
```

## _tools_check_for_upgrade_sh
### Line 1-5
```
#!/usr/bin/env zsh

zmodload zsh/datetime

function _current_epoch() {
```
### Line 10-33
```
  echo "LAST_EPOCH=$(_current_epoch)" >! ${ZSH_CACHE_DIR}/.zsh-update
}

function _upgrade_zsh() {
  env ZSH=$ZSH sh $ZSH/tools/upgrade.sh
  # update the zsh file
  _update_zsh_update
}

epoch_target=$UPDATE_ZSH_DAYS
if [[ -z "$epoch_target" ]]; then
  # Default to old behavior
  epoch_target=13
fi

# Cancel upgrade if the current user doesn't have write permissions for the
# oh-my-zsh directory.
[[ -w "$ZSH" ]] || return 0

# Cancel upgrade if git is unavailable on the system
whence git >/dev/null || return 0

if mkdir "$ZSH/log/update.lock" 2>/dev/null; then
  if [ -f ${ZSH_CACHE_DIR}/.zsh-update ]; then
```
### Line 52-61
```
          _update_zsh_update
        fi
      fi
    fi
  else
    # create the zsh file
    _update_zsh_update
  fi

  rmdir $ZSH/log/update.lock
```

## _tools_require_tool_sh
### Line 1-59
```
__require_tool_version_compare ()
{
  (
    # Locally ignore failures, otherwise we'll exit whenever $1 and $2
    # are not equal!
    set +e

awk_strverscmp='
  # Use only awk features that work with 7th edition Unix awk (1978).
  # My, what an old awk you have, Mr. Solaris!
  END {
    while (length(v1) || length(v2)) {
      # Set d1 to be the next thing to compare from v1, and likewise for d2.
      # Normally this is a single character, but if v1 and v2 contain digits,
      # compare them as integers and fractions as strverscmp does.
      if (v1 ~ /^[0-9]/ && v2 ~ /^[0-9]/) {
	# Split v1 and v2 into their leading digit string components d1 and d2,
	# and advance v1 and v2 past the leading digit strings.
	for (len1 = 1; substr(v1, len1 + 1) ~ /^[0-9]/; len1++) continue
	for (len2 = 1; substr(v2, len2 + 1) ~ /^[0-9]/; len2++) continue
	d1 = substr(v1, 1, len1); v1 = substr(v1, len1 + 1)
	d2 = substr(v2, 1, len2); v2 = substr(v2, len2 + 1)
	if (d1 ~ /^0/) {
	  if (d2 ~ /^0/) {
	    # Compare two fractions.
	    while (d1 ~ /^0/ && d2 ~ /^0/) {
	      d1 = substr(d1, 2); len1--
	      d2 = substr(d2, 2); len2--
	    }
	    if (len1 != len2 && ! (len1 && len2 && substr(d1, 1, 1) == substr(d2, 1, 1))) {
	      # The two components differ in length, and the common prefix
	      # contains only leading zeros.  Consider the longer to be less.
	      d1 = -len1
	      d2 = -len2
	    } else {
	      # Otherwise, compare as strings.
	      d1 = "x" d1
	      d2 = "x" d2
	    }
	  } else {
	    # A fraction is less than an integer.
	    exit 1
	  }
	} else {
	  if (d2 ~ /^0/) {
	    # An integer is greater than a fraction.
	    exit 2
	  } else {
	    # Compare two integers.
	    d1 += 0
	    d2 += 0
	  }
	}
      } else {
	# The normal case, without worrying about digits.
	if (v1 == "") d1 = v1; else { d1 = substr(v1, 1, 1); v1 = substr(v1,2) }
	if (v2 == "") d2 = v2; else { d2 = substr(v2, 1, 1); v2 = substr(v2,2) }
      }
      if (d1 < d2) exit 1
```
### Line 75-90
```
{
    echo $@ >/dev/stderr
    return 1
}

# Usage: require_tool program version
# Returns: 0 if $1 version if greater equals than $2, 1 otherwise.
# In case of error, message is written on error output.
#
# Example: require_tool gcc 4.6
# Use GCC environment variable if defined instead of lookup for the tool
# in the environment.
require_tool ()
{
  envvar_name=$(echo $1 | tr '[:lower:]' '[:upper:]')
  tool=$(printenv $envvar_name || echo $1)
```

## _plugins_gitfast_git_prompt_sh
### Line 1-115
```
# bash/zsh git prompt support
#
# Copyright (C) 2006,2007 Shawn O. Pearce <spearce@spearce.org>
# Distributed under the GNU General Public License, version 2.0.
#
# This script allows you to see repository status in your prompt.
#
# To enable:
#
#    1) Copy this file to somewhere (e.g. ~/.git-prompt.sh).
#    2) Add the following line to your .bashrc/.zshrc:
#        source ~/.git-prompt.sh
#    3a) Change your PS1 to call __git_ps1 as
#        command-substitution:
#        Bash: PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ '
#        ZSH:  setopt PROMPT_SUBST ; PS1='[%n@%m %c$(__git_ps1 " (%s)")]\$ '
#        the optional argument will be used as format string.
#    3b) Alternatively, for a slightly faster prompt, __git_ps1 can
#        be used for PROMPT_COMMAND in Bash or for precmd() in Zsh
#        with two parameters, <pre> and <post>, which are strings
#        you would put in $PS1 before and after the status string
#        generated by the git-prompt machinery.  e.g.
#        Bash: PROMPT_COMMAND='__git_ps1 "\u@\h:\w" "\\\$ "'
#          will show username, at-sign, host, colon, cwd, then
#          various status string, followed by dollar and SP, as
#          your prompt.
#        ZSH:  precmd () { __git_ps1 "%n" ":%~$ " "|%s" }
#          will show username, pipe, then various status string,
#          followed by colon, cwd, dollar and SP, as your prompt.
#        Optionally, you can supply a third argument with a printf
#        format string to finetune the output of the branch status
#
# The repository status will be displayed only if you are currently in a
# git repository. The %s token is the placeholder for the shown status.
#
# The prompt status always includes the current branch name.
#
# In addition, if you set GIT_PS1_SHOWDIRTYSTATE to a nonempty value,
# unstaged (*) and staged (+) changes will be shown next to the branch
# name.  You can configure this per-repository with the
# bash.showDirtyState variable, which defaults to true once
# GIT_PS1_SHOWDIRTYSTATE is enabled.
#
# You can also see if currently something is stashed, by setting
# GIT_PS1_SHOWSTASHSTATE to a nonempty value. If something is stashed,
# then a '$' will be shown next to the branch name.
#
# If you would like to see if there're untracked files, then you can set
# GIT_PS1_SHOWUNTRACKEDFILES to a nonempty value. If there're untracked
# files, then a '%' will be shown next to the branch name.  You can
# configure this per-repository with the bash.showUntrackedFiles
# variable, which defaults to true once GIT_PS1_SHOWUNTRACKEDFILES is
# enabled.
#
# If you would like to see the difference between HEAD and its upstream,
# set GIT_PS1_SHOWUPSTREAM="auto".  A "<" indicates you are behind, ">"
# indicates you are ahead, "<>" indicates you have diverged and "="
# indicates that there is no difference. You can further control
# behaviour by setting GIT_PS1_SHOWUPSTREAM to a space-separated list
# of values:
#
#     verbose       show number of commits ahead/behind (+/-) upstream
#     name          if verbose, then also show the upstream abbrev name
#     legacy        don't use the '--count' option available in recent
#                   versions of git-rev-list
#     git           always compare HEAD to @{upstream}
#     svn           always compare HEAD to your SVN upstream
#
# You can change the separator between the branch name and the above
# state symbols by setting GIT_PS1_STATESEPARATOR. The default separator
# is SP.
#
# By default, __git_ps1 will compare HEAD to your SVN upstream if it can
# find one, or @{upstream} otherwise.  Once you have set
# GIT_PS1_SHOWUPSTREAM, you can override it on a per-repository basis by
# setting the bash.showUpstream config variable.
#
# If you would like to see more information about the identity of
# commits checked out as a detached HEAD, set GIT_PS1_DESCRIBE_STYLE
# to one of these values:
#
#     contains      relative to newer annotated tag (v1.6.3.2~35)
#     branch        relative to newer tag or branch (master~4)
#     describe      relative to older annotated tag (v1.6.3.1-13-gdd42c2f)
#     tag           relative to any older tag (v1.6.3.1-13-gdd42c2f)
#     default       exactly matching tag
#
# If you would like a colored hint about the current dirty state, set
# GIT_PS1_SHOWCOLORHINTS to a nonempty value. The colors are based on
# the colored output of "git status -sb" and are available only when
# using __git_ps1 for PROMPT_COMMAND or precmd.
#
# If you would like __git_ps1 to do nothing in the case when the current
# directory is set up to be ignored by git, then set
# GIT_PS1_HIDE_IF_PWD_IGNORED to a nonempty value. Override this on the
# repository level by setting bash.hideIfPwdIgnored to "false".

# check whether printf supports -v
__git_printf_supports_v=
printf -v __git_printf_supports_v -- '%s' yes >/dev/null 2>&1

# stores the divergence from upstream in $p
# used by GIT_PS1_SHOWUPSTREAM
__git_ps1_show_upstream ()
{
	local key value
	local svn_remote svn_url_pattern count n
	local upstream=git legacy="" verbose="" name=""

	svn_remote=()
	# get some config options from git-config
	local output="$(git config -z --get-regexp '^(svn-remote\..*\.url|bash\.showupstream)$' 2>/dev/null | tr '\0\n' '\n ')"
	while read -r key value; do
		case "$key" in
		bash.showupstream)
```
### Line 125-134
```
			upstream=svn+git # default upstream is SVN if available, else git
			;;
		esac
	done <<< "$output"

	# parse configuration values
	for option in ${GIT_PS1_SHOWUPSTREAM}; do
		case "$option" in
		git|svn) upstream="$option" ;;
		verbose) verbose=1 ;;
```
### Line 135-149
```
		legacy)  legacy=1  ;;
		name)    name=1 ;;
		esac
	done

	# Find our upstream
	case "$upstream" in
	git)    upstream="@{upstream}" ;;
	svn*)
		# get the upstream from the "git-svn-id: ..." in a commit message
		# (git-svn uses essentially the same procedure internally)
		local -a svn_upstream
		svn_upstream=($(git log --first-parent -1 \
					--grep="^git-svn-id: \(${svn_url_pattern#??}\)" 2>/dev/null))
		if [[ 0 -ne ${#svn_upstream[@]} ]]; then
```
### Line 153-162
```
			for ((n=1; n <= n_stop; n++)); do
				svn_upstream=${svn_upstream#${svn_remote[$n]}}
			done

			if [[ -z "$svn_upstream" ]]; then
				# default branch name for checkouts with no layout:
				upstream=${GIT_SVN_ID:-git-svn}
			else
				upstream=${svn_upstream#/}
			fi
```
### Line 164-178
```
			upstream="@{upstream}"
		fi
		;;
	esac

	# Find how many commits we are ahead/behind our upstream
	if [[ -z "$legacy" ]]; then
		count="$(git rev-list --count --left-right \
				"$upstream"...HEAD 2>/dev/null)"
	else
		# produce equivalent output to --count for older versions of git
		local commits
		if commits="$(git rev-list --left-right "$upstream"...HEAD 2>/dev/null)"
		then
			local commit behind=0 ahead=0
```
### Line 187-196
```
		else
			count=""
		fi
	fi

	# calculate the result
	if [[ -z "$verbose" ]]; then
		case "$count" in
		"") # no upstream
			p="" ;;
```
### Line 221-251
```
				--abbrev-ref "$upstream" 2>/dev/null)
			if [ "$pcmode" = yes ] && [ "$ps1_expanded" = yes ]; then
				p="$p \${__git_ps1_upstream_name}"
			else
				p="$p ${__git_ps1_upstream_name}"
				# not needed anymore; keep user's
				# environment clean
				unset __git_ps1_upstream_name
			fi
		fi
	fi

}

# Helper function that is meant to be called from __git_ps1.  It
# injects color codes into the appropriate gitstring variables used
# to build a gitstring.
__git_ps1_colorize_gitstring ()
{
	if [[ -n "${ZSH_VERSION-}" ]]; then
		local c_red='%F{red}'
		local c_green='%F{green}'
		local c_lblue='%F{blue}'
		local c_clear='%f'
	else
		# Using \[ and \] around colors is necessary to prevent
		# issues with command line editing/browsing/completion!
		local c_red='\[\e[31m\]'
		local c_green='\[\e[32m\]'
		local c_lblue='\[\e[1;34m\]'
		local c_clear='\[\e[0m\]'
```
### Line 276-306
```
		u="$bad_color$u"
	fi
	r="$c_clear$r"
}

# Helper function to read the first line of a file into a variable.
# __git_eread requires 2 arguments, the file path and the name of the
# variable, in that order.
__git_eread ()
{
	test -r "$1" && IFS=$'\r\n' read "$2" <"$1"
}

# __git_ps1 accepts 0 or 1 arguments (i.e., format string)
# when called from PS1 using command substitution
# in this mode it prints text to add to bash PS1 prompt (includes branch name)
#
# __git_ps1 requires 2 or 3 arguments when called from PROMPT_COMMAND (pc)
# in that case it _sets_ PS1. The arguments are parts of a PS1 string.
# when two arguments are given, the first is prepended and the second appended
# to the state string when assigned to PS1.
# The optional third parameter will be used as printf format string to further
# customize the output of the git-status string.
# In this mode you can request colored hints using GIT_PS1_SHOWCOLORHINTS=true
__git_ps1 ()
{
	# preserve exit status
	local exit=$?
	local pcmode=no
	local detached=no
	local ps1pc_start='\u@\h:\w '
```
### Line 310-362
```
	case "$#" in
		2|3)	pcmode=yes
			ps1pc_start="$1"
			ps1pc_end="$2"
			printf_format="${3:-$printf_format}"
			# set PS1 to a plain prompt so that we can
			# simply return early if the prompt should not
			# be decorated
			PS1="$ps1pc_start$ps1pc_end"
		;;
		0|1)	printf_format="${1:-$printf_format}"
		;;
		*)	return $exit
		;;
	esac

	# ps1_expanded:  This variable is set to 'yes' if the shell
	# subjects the value of PS1 to parameter expansion:
	#
	#   * bash does unless the promptvars option is disabled
	#   * zsh does not unless the PROMPT_SUBST option is set
	#   * POSIX shells always do
	#
	# If the shell would expand the contents of PS1 when drawing
	# the prompt, a raw ref name must not be included in PS1.
	# This protects the user from arbitrary code execution via
	# specially crafted ref names.  For example, a ref named
	# 'refs/heads/$(IFS=_;cmd=sudo_rm_-rf_/;$cmd)' might cause the
	# shell to execute 'sudo rm -rf /' when the prompt is drawn.
	#
	# Instead, the ref name should be placed in a separate global
	# variable (in the __git_ps1_* namespace to avoid colliding
	# with the user's environment) and that variable should be
	# referenced from PS1.  For example:
	#
	#     __git_ps1_foo=$(do_something_to_get_ref_name)
	#     PS1="...stuff...\${__git_ps1_foo}...stuff..."
	#
	# If the shell does not expand the contents of PS1, the raw
	# ref name must be included in PS1.
	#
	# The value of this variable is only relevant when in pcmode.
	#
	# Assume that the shell follows the POSIX specification and
	# expands PS1 unless determined otherwise.  (This is more
	# likely to be correct if the user has a non-bash, non-zsh
	# shell and safer than the alternative if the assumption is
	# incorrect.)
	#
	local ps1_expanded=yes
	[ -z "${ZSH_VERSION-}" ] || [[ -o PROMPT_SUBST ]] || ps1_expanded=no
	[ -z "${BASH_VERSION-}" ] || shopt -q promptvars || ps1_expanded=no

```
### Line 426-442
```
		fi

		if [ -n "$b" ]; then
			:
		elif [ -h "$g/HEAD" ]; then
			# symlink symbolic ref
			b="$(git symbolic-ref HEAD 2>/dev/null)"
		else
			local head=""
			if ! __git_eread "$g/HEAD" head; then
				return $exit
			fi
			# is it a symbolic ref?
			b="${head#ref: }"
			if [ "$head" = "$b" ]; then
				detached=yes
				b="$(
```
### Line 504-513
```
		fi
	fi

	local z="${GIT_PS1_STATESEPARATOR-" "}"

	# NO color option unless in PROMPT_COMMAND mode or it's Zsh
	if [ -n "${GIT_PS1_SHOWCOLORHINTS-}" ]; then
		if [ "$pcmode" = yes ] || [ -n "${ZSH_VERSION-}" ]; then
			__git_ps1_colorize_gitstring
		fi
```

## _tools_uninstall_sh

## _plugins_catimg_catimg_sh
### Line 1-19
```
################################################################################
# catimg script by Eduardo San Martin Morote aka Posva                         #
# https://posva.net                                                            #
#                                                                              #
# Ouput the content of an image to the stdout using the 256 colors of the      #
# terminal.                                                                    #
# GitHub: https://github.com/posva/catimg                                      #
################################################################################

function help() {
  echo "Usage catimg [-h] [-w width] [-c char] img"
  echo "By default char is \"  \" and w is the terminal width"
}

# VARIABLES
COLOR_FILE=$(dirname $0)/colors.png
CHAR="  "

WIDTH=""
```
### Line 51-64
```
REMAP=""
if convert "$IMG" -resize $COLS\> +dither -remap $COLOR_FILE /dev/null ; then
  REMAP="-remap $COLOR_FILE"
else
  echo "The version of convert is too old, don't expect good results :(" >&2
  #convert "$IMG" -colors 256 PNG8:tmp.png
  #IMG="tmp.png"
fi

# Display the image
I=0
convert "$IMG" -resize $COLS\> +dither `echo $REMAP` txt:- 2>/dev/null |
sed -e 's/.*none.*/NO NO NO/g' -e '1d;s/^.*(\(.*\)[,)].*$/\1/g;y/,/ /' |
while read R G B f; do
```
### Line 75-88
```
      + R * 5 / 255 * 36
      + G * 5 / 255 * 6
      + B * 5 / 255
      ))
    fi
    #echo "$R,$G,$B: $IDX"
    echo -ne "\e[48;5;${IDX}m${CHAR}"
  else
    (( I++ ))
    echo -ne "\e[0m${CHAR}"
  fi
  # New lines
  (( $I % $WIDTH )) || echo -e "\e[0m"
done
```

## _tools_upgrade_sh
### Line 1-7
```

# Use colors, but only if connected to a terminal, and that terminal
# supports them.
if which tput >/dev/null 2>&1; then
    ncolors=$(tput colors)
fi
if [ -t 1 ] && [ -n "$ncolors" ] && [ "$ncolors" -ge 8 ]; then
```
### Line 20-33
```
  NORMAL=""
fi

cd "$ZSH"

# Set git-config values known to fix git errors
# Line endings (#4069)
git config core.eol lf
git config core.autocrlf false
# zeroPaddedFilemode fsck errors (#4963)
git config fsck.zeroPaddedFilemode ignore
git config fetch.fsck.zeroPaddedFilemode ignore
git config receive.fsck.zeroPaddedFilemode ignore

```

## _plugins_frontend_search_frontend_search_sh
### Line 1-5
```
#compdef frontend

zstyle ':completion:*:descriptions' format '%B%d%b'
zstyle ':completion::complete:frontend:*:commands' group-name commands
zstyle ':completion::complete:frontend:*:frontend_points' group-name frontend_points
```
### Line 146-157
```
  return $ret
}

_frontend "$@"

# Local Variables:
# mode: Shell-Script
# sh-indentation: 2
# indent-tabs-mode: nil
# sh-basic-offset: 2
# End:
# vim: ft=zsh sw=2 ts=2 et
```

# Issues
## 1677
Title:
```

        Can no longer turn of autocorrect with unsetopt correct_all
      
```
Author:
```
bdtomlin
```
Text:
```

I tried both the following
unsetopt correct_all

and
unsetopt correct

Neither of these will turn off autocorrect. It began failing with the last oh-my update.

```
Author:
```
paulcalabro
```
Text:
```

What happens if you do do the following:
nocorrect <command>


```
Author:
```
bdtomlin
```
Text:
```

Thanks for you quick reply. Sorry for any mis-information. "Unsetting" both options has the expected behavior.
Anyone else who finds this, in order to get the original expected behavior, just add both to you zshrc:
unsetopt correct_all
unsetopt correct


```
Author:
```
paulcalabro
```
Text:
```

Good to know! Thanks!

```
Author:
```
millisami
```
Text:
```

Does this still work?
I've tried with all the options got doing google.
unsetopt correct_all
unsetopt correct
DISABLE_CORRECTION = "true"

None worked for my oh-myzsh!!

```
Author:
```
bdtomlin
```
Text:
```

Still works for me. I only have the first two lines though.

```

## 2692
Title:
```

        xargs -r invalid on OSX
      
```
Author:
```
ryan-mars
```
Text:
```

The alias in the git plugin uses the -r flag for xargs. This is invalid on OSX.
gwip='git add -A; git ls-files --deleted -z | xargs -r0 git rm; git commit -m "--wip--"'

```
Author:
```
ncanceill
```
Text:
```

Confirmed here.
Mac OSX uses the BSD-flavored xargs, which runs with the -r flag implied. However (and, it seems, contrary to the FreeBSD version), the -r flag will return an error on Mac OSX.
So simple fix is:
XARGS_OPTS=
&>/dev/null xargs -r && XARGS_OPTS+="-r"
alias gwip="git add -A; git ls-files --deleted -z | xargs ${XARGS_OPTS} -0 git rm; git commit -m \"--wip--\""
@robbyrussell should I submit a PR?

```
Author:
```
ncanceill
```
Text:
```

This is the second time this bites someone, so I submitted #2714. Please test it if you have time.

```
Author:
```
mcornella
```
Text:
```

Effectively solved and ready to close once #2790 is merged. Just leaving this comment to update the issue and get it out of the way to triage the rest...

```
Author:
```
apjanke
```
Text:
```

Looks like this was fixed by #2790. I don't see any remaining xargs -r uses in the repo. Could you confirm if this is fixed for you, and if so, close this issue?

```
Author:
```
ncanceill
```
Text:
```

Indeed this should be fixed now.

Le 25 juin 2015 à 21:56, Andrew Janke notifications@github.com a écrit :
Looks like this was fixed by #2790. I don't see any remaining xargs -r uses in the repo. Could you confirm if this is fixed for you, and if so, close this issue?
—
Reply to this email directly or view it on GitHub.


```

## 7170
Title:
```

        adding current branch name on all the timestamp lines?
      
```
Author:
```
weilinzung
```
Text:
```

Is possible to add the current branch name on all the timestamp lines? Something like this:
FROM:
[18:37:39] Starting 'build-js'...
[18:37:49] finished 'build-js'...

TO:
[18:37:39 - **current-branch-name** ] Starting 'build-js'...
[18:37:49 - **current-branch-name** ] finished 'build-js'...

Thanks.

```
Author:
```
mcornella
```
Text:
```

That depends on what program is printing those lines, probably not OMZ-related.

```

## 7600
Title:
```

        ssh-agent plugin always asks for passphrase after boot
      
```
Author:
```
panosru
```
Text:
```

Hello, I'm not sure if that is normal behaviour,
I have the following code (part of it) in my .zshrc file:
  ssh-agent
)

zstyle :omz:plugins:ssh-agent agent-forwarding on
zstyle :omz:plugins:ssh-agent identities id_rsa gitlab github


source $ZSH/oh-my-zsh.sh

But every time after the boot of machine, when I run iTerm, I prompted to enter passphrase:
Last login: Sun Feb 17 23:34:58 on ttys001
Enter passphrase for /Users/*****/.ssh/id_rsa:
Identity added: /Users/*****/.ssh/id_rsa (/Users/*****/.ssh/id_rsa)
Identity added: /Users/*****/.ssh/gitlab (/Users/*****/.ssh/gitlab)
Enter passphrase for /Users/*****/.ssh/github:
Identity added: /Users/*****/.ssh/github (*******@gmail.com)

Once I add my passphrase, then if I close iTerm and start it again it won't ask me again. It only asks me when I boot my computer and launching iTerm for the first time after boot.
Is that normal? And if not, how can I fix it? And if yes, is there a way to prevent it or store my passphrase somewhere in my system so it will automatically read it?
Thank you in advance!

```
Author:
```
mcornella
```
Text:
```

ssh-agent caches your identities so that you don't have to enter the passphrase every time you use an identity, e.g. when running ssh or doing a git push.
When you restart your computer the ssh-agent no longer has these cached, so it needs to ask again for the passphrase. It can't store these anywhere since that could be then exploited to extract the passphrases in an offline attack.
I think there are other agents that can set up a master password which is then used to load multiple identities but I can't recommend anything in particular. Look up keychains or keyrings.

```
Author:
```
panosru
```
Text:
```

I see... well that’s frustrating tbh, I think I can live without ssh-agent plugin then.
Cheers!

```

## 5696
Title:
```

        Segmentation Fault on LS -LA alias (l)
      
```
Author:
```
Splace42
```
Text:
```

Try to write l\ and press enter two time
Cya zsh :D

```
Author:
```
mcornella
```
Text:
```

Can't reproduce
$ alias l='ls -la'
$ l\
> 
total 132
drwxr-xr-x  2 XXXX XXXX   4096 dic  8 22:39 .
drwxr-xr-x 83 XXXX XXXX 126976 dic  8 22:39 ..
$ zsh --version
zsh 5.2 (x86_64-debian-linux-gnu)

Please provide more information about your system and test on multiple filesystems.

```
Author:
```
Splace42
```
Text:
```

➜  ~ sh
sh-3.2$ zsh
➜  ~ l\
>
Segmentation fault: 11
sh-3.2$ ZSH
➜  ~ zsh --version
zsh 5.0.8 (x86_64-apple-darwin15.0)
➜  ~
➜  ~


```
Author:
```
mkwardakov
```
Text:
```

It is definitely not a oh-my-zsh issue, please see http://stackoverflow.com/questions/14248514/what-could-possibly-cause-a-linux-ls-command-to-return-a-seg-fault

```
Author:
```
mcornella
```
Text:
```

Closing then. If it turns out to be an Oh My Zsh issue feel free to reopen.

```

## 6951
Title:
```

        oh-my-zsh messes with zsh process substitution
      
```
Author:
```
fzuviria
```
Text:
```

#!/bin/bash
foo() { cat <(cat "$@"); }; foo <(echo bar);
bar
#!/bin/zsh
foo() { cat <(cat "$@"); }; foo <(echo bar);
cat: /proc/self/fd/11: No such file or directory
This is a bug from zsh ([BUG] process substitution breaks when nested or traverses a function) that has been fixed in version 5.5
HOWEVER, when running that in a zsh shell that uses oh-my-zsh, the bug is still there!
I tried disabling all plugins and the problem persists.
I don't expect you guys to be able to fix this, but please try to give me some insight on what is exactly is triggering this behaviour, because the zsh guys don't have enough info to work on this. So if we can narrow it down to something like, "autoloading a function that does x and y and uses this modules leaves zsh unable to do proper process substitution", will be a lot of help.
Thanks in advance

```
Author:
```
fzuviria
```
Text:
```

My bad, problem still happens with vanilla zsh

```

## 4861
Title:
```

        deactivate:unset:1: no such hash table element: pydoc
      
```
Author:
```
Namita26
```
Text:
```

I have upgraded oh my zsh to the latest version. Still, when I activate my virtual environment, I get this line after opening a new terminal or tab. Please suggest a solution.

```
Author:
```
apjanke
```
Text:
```

Which OMZ plugins are you using, and which version of virtualenv are you running?

```
Author:
```
Namita26
```
Text:
```

I am using virutalenv==14.0.1 and zsh 5.0.2 (x86_64-pc-linux-gnu).

```
Author:
```
aaronireland
```
Text:
```

I'm experiencing this too.
I'm running virtualenv version 14.1.0.dev0 and zsh 5.0.8 (x86_64-apple-darwin15.0)
plugins=(git brew dirhistory docker history jsontools pylint python virtualenvwrapper)

```
Author:
```
spapanik
```
Text:
```

This bug has nothing to do with zsh, the problem is with virtualenv. It is fixed in version 15.0.0, but it will persist for venvs created with an earlier venv. You can change in the deactivate function the line unset -f pydoc to unset -f pydoc >/dev/null 2>&1.

```

## 7401
Title:
```

        Calling a function when custom alias called
      
```
Author:
```
Dentrax
```
Text:
```

I'm writing a script to prevent me from entering some wrong commands like rm.
anti_RM() {
   echo "STOP!" >&2
   sleep 3
}

alias rm -fr /*="anti_RM"
alias rm -rf /*="anti_RM"
alias rm -fr /.="anti_RM"
alias rm -rf /.="anti_RM"

When i coded this alias script in my custom .zsh file that calling from .zshrc, i get this error:
/home/dentrax/.zsh/aliases.zsh:20: no matches found: /*=anti_RM
How do I make this right? Am i missing something? or Do we have to do this a different way for ZSH?

```
Author:
```
mcornella
```
Text:
```

You can't define aliases with spaces in them. More correctly: you can define them, but you'll never be able to run them.
The error you're seeing though is not because of that, but because you're using the star character (*) without quoting, which means zsh thinks you want to expand that to filenames of the form /*=anti_RM. If you quote it -- alias 'rm -fr /*'=anti_RM -- you'll get no error.
But as I said, it will not do what you think it will. You can only alias a command, not the command and its arguments. To do what you want you'd need to alias rm to a function, then in that function either stop if the arguments passed match your blacklist, or call command rm with the arguments passed otherwise.
Browse zsh's documentation for further help.

```

## 5196
Title:
```

        nocorrect mv
      
```
Author:
```
sygi
```
Text:
```

When I'm using mv, I'd prefer correction to be turned off, to prevent this:
mv ~/Downloads/index.mp4 2.5.mp4
zsh: correct '2.5.mp4' to '1.5.mp4' [nyae]? 

It seems that the authors thought about this and made aliases for that kind of commands in lib/correction.zsh, but, as one can see above, it is not executed in my case.
Did I do something wrong? What can I do to make zsh correction work as expected with mv? Do I have to turn something on?
I have:
ENABLE_CORRECTION="true"
plugins=(command-not-found common-aliases fasd git python)

in my ~/.zshrc.

```
Author:
```
mcornella
```
Text:
```

The common-aliases overrides the mv alias. You can manually do the alias mv='nocorrect mv' at the end of your zshrc file.

```
Author:
```
sygi
```
Text:
```

Thanks, now it works. Do you think it deserves a pull request like this:
compare

```
Author:
```
mcornella
```
Text:
```

I don't think that's a great way to solve this and it's not immediately obvious to me what the best approach is. For the time being I'll leave this hanging but I'll come back to it right away if someone else has this problem.

```

## 5073
Title:
```

        [Plugin Request] IX command
      
```
Author:
```
Arzte
```
Text:
```

http://ix.io command handler, similar to sprunge in ways

```

# Pull
## 2520
Title:
```

        Displaying current tag in git prompt
      
```
Author:
```
rogerclotet
```
Text:
```

If your current branch is on a specific tag, it will be displayed as the git prompt, instead of the short sha.

```
Author:
```
alexcarol
```
Text:
```

I tried this and it works quite well, hope it gets merged.

```
Author:
```
smoya
```
Text:
```

+1

```
Author:
```
gsemet
```
Text:
```

+1

```
Author:
```
apbarrero
```
Text:
```

I already submitted PR #2061 some time ago for the same feature. The command I added is a bit simpler.

```
Author:
```
robbyrussell
```
Text:
```

Closing this per #2568.

```

## 2620
Title:
```

        Fixed errors if acpitool isn't installed on linux
      
```
Author:
```
reedriley
```
Text:
```

Currently, when acpitool isn't installed, I get an error every time my prompt tries to call battery_pct:
battery_pct:1: command not found: acpi

This change fixes the error by guarding the call to acpi with a check that it's actually installed and executable.
(Also include a small amount of whitespace cleanup.)

```
Author:
```
Omar-Elrefaei
```
Text:
```

WHAT, I spent > 15 min because it didn't say Error: acpi not installed

```

## 1969
Title:
```

        [lib][completion] enable user completion by default
      
```
Author:
```
ghost
```
Text:
```

User completion was disabled by default by commit c4434d2 which purpose is mainly to add .ssh/config's hosts to host completion.
Plus there is a list of ignored users (for completion) in lib/completion.zsh +53, we may want to complete the others.

```
Author:
```
mcornella
```
Text:
```

Obsolete

```

## 5053
Title:
```

        znt: update to v2.1.15
      
```
Author:
```
psprint
```
Text:
```

Hello,
new features:

Approximate matching – every tool can handle typos after pressing Ctrl-F. This will make 1 or 2 errors to be allowed in what's searched (in every word). Near fuzzy matching, but aimed at typos
Most Frequent History Words – new view in n-history, allows to browse words in history instead of entries
Themes – predefined themes for all tools. I've sent a patch to Zsh developers and next Zsh version will support 256 colors in zcurses. Zsh-navigation-tools are ready:
http://imagizer.imageshack.us/a/img924/8896/0kmijJ.gif
Private history – n-history tracks what's executed on its own, shares this information across sessions
Predefined search keywords: pressing F2 in each tool will iterate over predefined keywords: https://www.youtube.com/watch?v=DN9QqssAYB8
Instant selection: option to make "Enter" instantly accept searched entry (normally it will first end search mode).
Zshrc integration: ZNT can be configured from ~/.zshrc


```
Author:
```
psprint
```
Text:
```

There was a bad link to youtube video, correct is: https://www.youtube.com/watch?v=DN9QqssAYB8
Best Regards,
Sebastian Gniazdowski

```
Author:
```
psprint
```
Text:
```

Thanks for the merge!

```

## 1016
Title:
```

        Helpers for encoding/decoding base64
      
```
Author:
```
fuksito
```
Text:
```

$ encode64 fuksito@gmail.com
=> ZnVrc2l0b0BnbWFpbC5jb20=
$ decode64 ZnVrc2l0b0BnbWFpbC5jb20=
=> fuksito@gmail.com

```
Author:
```
robbyrussell
```
Text:
```

Thanks, can you update our Plugins page with the usage examples?

```

## 2551
Title:
```

        Add jtriley-light theme for light background
      
```
Author:
```
kk1fff
```
Text:
```

Add a jtriley-light theme, which is modified from jtriley to be suitable on light background.


```
Author:
```
kk1fff
```
Text:
```

Sorry I didn't notice that README has mentioned not sending theme for now. Closing.

```

## 1256
Title:
```

        Added sf Symfony2 binary alias
      
```
Author:
```
ruimarinho
```
Text:
```


No description provided.


```

## 8070
Title:
```

        Add alias wpreset to reset the database
      
```
Author:
```
pixolin
```
Text:
```

wp db reset removes all tables from the database, opening the website URL in the browser will aks for installation details. It's a convenient way to "start from scratch", if you use the site for tests and development.
Without parameter --yes the user will be prompted to confirm the command.

```

## 5307
Title:
```

        Add alias for checking out develop branch
      
```
Author:
```
smic1909
```
Text:
```


No description provided.


```
Author:
```
mcornella
```
Text:
```

Are you using git-flow? If so, there's a dedicated plugin for that.

```
Author:
```
smic1909
```
Text:
```

Hey,
I´m not using git-flow.

```
Author:
```
mcornella
```
Text:
```

👍

```
Author:
```
kaHaleMaKai
```
Text:
```

That commit introduced a bug into my zsh: I cannot use any git related commands anymore. They just don't print anything. When reverting the commit, it works correct again.
on master branch:
kauai :: ~/.oh-my-zsh % gst
kauai :: ~/.oh-my-zsh %
after reverting the commit:
kauai :: ~/.oh-my-zsh ‹without-b9c3e862› % gst
On branch without-b9c3e862
nothing to commit, working tree clean
specs:

ubuntu 14.04.5
zsh 5.0.2
plugins: git command-not-found gitfast git-extras lein pip python screen ssh-agent sublime urltoos emacs-mode web-search wd

Please tell me if you need anything else.

```
Author:
```
mcornella
```
Text:
```

Can you post the content of $ZSH/plugins/git/git.plugin.zsh on master?

```
Author:
```
kaHaleMaKai
```
Text:
```

Sure. I have attached the file with the extensions txt, so I could upload it (.zsh was prohibited).
git.plugin.zsh.txt

```
Author:
```
mcornella
```
Text:
```

I see nothing wrong with it. Please open a new issue and post your zshrc and the output of git show without-b9c3e862 in the OMZ folder.

```
Author:
```
kaHaleMaKai
```
Text:
```

Thanks for taking the time to investigate that further!
By chance, I just found the problem: I had defined an alias gcd like ages ago, but in that very commit the same alias has been defined, but with another meaning. If I remove the custom alias from my .zshrc, it runs smoothly again.

```

## 4602
Title:
```

        add --no-check-certificate option for wget
      
```
Author:
```
roramirez
```
Text:
```


No description provided.


```
Author:
```
robbyrussell
```
Text:
```

Hi there, I'm going to pass on this because we intentionally removed this back in Februrary after some discussions in #3607. It's not a safe default to instruct everyone to use

```

