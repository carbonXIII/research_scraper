# vlang/v
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_CHANGELOG_md](#_CHANGELOG_md)

* [_vlib_ui_examples_users_gui_README_md](#_vlib_ui_examples_users_gui_README_md)

* [_examples_word_counter_README_md](#_examples_word_counter_README_md)

* [_vlib_vweb_README_md](#_vlib_vweb_README_md)

* [_examples_vcasino_README_md](#_examples_vcasino_README_md)

* [_examples_game_of_life_README_md](#_examples_game_of_life_README_md)

* [_github_ISSUE_TEMPLATE_bug_report_md](#_github_ISSUE_TEMPLATE_bug_report_md)

* [_vlib_gg_README_md](#_vlib_gg_README_md)

* [_github_ISSUE_TEMPLATE_feature_request_md](#_github_ISSUE_TEMPLATE_feature_request_md)

* [_README_md](#_README_md)

* [_CONTRIBUTING_md](#_CONTRIBUTING_md)

* [_vlib_ui_README_md](#_vlib_ui_README_md)

* [_CODE_OF_CONDUCT_md](#_CODE_OF_CONDUCT_md)

* [_github_ISSUE_TEMPLATE_bug_report_for_v_md](#_github_ISSUE_TEMPLATE_bug_report_for_v_md)

* [_vlib_compiler_tests_repl_README_md](#_vlib_compiler_tests_repl_README_md)

* [_examples_tetris_README_md](#_examples_tetris_README_md)

[- Inline](#Inline)

* [_thirdparty_cJSON_cJSON_c](#_thirdparty_cJSON_cJSON_c)

* [_thirdparty_zip_zip_c](#_thirdparty_zip_zip_c)

* [_vlib_compiler_tests_bench_val_vs_ptr_c](#_vlib_compiler_tests_bench_val_vs_ptr_c)

* [_thirdparty_vschannel_vschannel_c](#_thirdparty_vschannel_vschannel_c)

* [_thirdparty_glad_glad_c](#_thirdparty_glad_glad_c)

[- Issues](#Issues)

* [2465](#2465)

* [158](#158)

* [1451](#1451)

* [253](#253)

* [136](#136)

* [1169](#1169)

* [2164](#2164)

* [145](#145)

[- Pull](#Pull)

* [1251](#1251)

* [429](#429)

* [2236](#2236)

* [1135](#1135)

* [2346](#2346)

* [1916](#1916)

* [475](#475)

* [2108](#2108)

* [1572](#1572)

* [2496](#2496)

* [1499](#1499)

* [1477](#1477)

<!-- toc -->

# Info
## description
Simple, fast, safe, compiled language for developing maintainable software. Compiles itself in <1s with zero dependencies. 1.0 release in December 2019. https://vlang.io

# Markdown
## _CHANGELOG_md
```## V 0.1.21
*30 Sep 2019*

- `none` keyword for optionals.
- Solaris support.
- All table lookup functions now use `none`.
- varargs: `fn foo(bar int, params ...string) {`
- Double quotes (`"`) can now also be used to denote strings.
- GitHub Actions CI in addition to Travis.
- `-compress` option. The V binary built with `-compress` is only ~90 KB!
- More memory management.
- Unused modules result in an error.
- "Unused variable/module" errors are now warnings in non-production builds.
- Duplicate methods with the same name can no longer be defined.
- Struct names must be capitalized, variable/function names must use snake_case.
- Error messages are now even nicer!
- Lots of fixes in automatic `.str()` method generation for structs and arrays.
- ~30% faster parser (files are no longer parsed separately for each pass).
- `_` is no longer a variable, but an actual syntax construct to skip unused values, like in Go.
- Multiple returns (`fn foo() (int, string) {`).
- `!` can now only be used with booleans.


## V 0.1.20
*17 Sep 2019*

- JavaScript backend!
- Hundreds of C warnings were fixed. `gcc v.c` now builds without
any warnings.
- The mutability check now applies to function args (mutable
receivers that are not modified result in a compilation error).
- V tests now show how long each test took.
- Official Android support (only console applications via Termux for now).
- Typo check. If a variable/function/module etc is misspelled,
V will suggest the correct name.
- Lots of Microsoft C fixes, and a separate Travis instance for
this backend.
- Bitwise operators `|`, `^`, `&` no longer work with booleans.





## V 0.1.19
*12 Sep 2019*

- Lots of refactoring, simplifications, and optimizations in the compiler.
- Experimental memory management at compilation (only for the V compiler itself for now).
- Lots of ORM fixes.
- Functions can now be inlined via the `[inline]` attribute.
- New `mysql` module.
- Better error format that is supported by all major editors (go to error).
- Error messages now point to the actual place where the error happened.
- Custom json field names: `struct User { last_name string [json:lastName] }`.
- Raw json fields via the `[raw]` attribute.
- All C code was removed from the `freetype` module.
- `gg` module can now render all Unicode characters.
- `[typedef]` attribute for imported C struct typedefs.
- Support of Objective C interfaces (primarily for using Cocoa).
- REPL: clear command and custom functions.
- REPL tests (which are also used for testing certain compiler errors).
- Syntax bug fixed: `foo[0] += 10` is now possible.
- http: support plain HTTP protocol and follow redirects.
- http: header data is now processed correctly.
- net: basic UDP support.
- `import const` was removed from the language.
- `array.contains()` was removed from the language (`in` should be used instead).
- `[0; len]` syntax was removed (replaced with a simpler `[0].repeat(len)`)
- Primitive aliases were removed to simplify the language.
- GitHub supports V now!
- Backtraces are now printed on panics.
- A new awesome `readline` module.
- V.c is now regenerated automatically after every commit.
- A bug with struct ordering was fixed, now structs can be declared in any order.
- V modules can now be built with `v build module`.
- `@FILE, @LINE, @FN, @COLUMN` for debugging.






## V 0.1.18
*16 Aug 2019*

- Built-in ORM (`uk_customers = db.select from Customer where country == 'uk' && nr_orders > 0`)
- Map initialization syntax: `m := { ‘foo’: ‘bar’, ‘baz’: ‘foo’ }`
- `map.delete(key)`.
- `libcurl` dependency was removed from the `http` module.
- All function arguments are now immutable by default (previously they could be
  modifed inside the function).
- `http` functions now return optionals.
- `sync.WaitGroup`.
- `vweb` static files serving.
- `crypto.rand` module.
- `v up` to update V.
- SChannel support on Windows.
- `net.urllib` module.
- vpm package manager, `v install`.
- `()` are now required in complex bool expressions: `(a && b) || c` instead of `a && b || c
- All arrays now have a default `.str()` method.
- Bootstrapping V with MSVC.
- Experimental `≠` etc support.
- `encoding.csv` module.
- `$if debug {` for running code in debug mode only.
- Map struct fields are now initialized automatically, just like arrays.
- Maps now support array values.
- `json` functions can no longer be used if the `json` module is not imported.



## V 0.1.17
*29 Jul 2019*
- `vweb` module for developing web apps in V.
- vtalk, open source V forum software.
- Generics (very limited right now, but they will be gradually improved).
- Comptime codegen (`foo.$method()` where `method` is a string).
- @ for escaping keywords (e.g. `struct Foo { @type string }`).
- Windows Unicode fixes (V can now work with non-ASCII paths etc on Windows).
- Fix mutable args bugs + don't allow primitive arguments to be modified.
- Declaring a mutable variable and never modifying it results in a compilation error.
- Interactive debugging support.
- `sync` module for Windows.
- `#!` support on Unix systems (V scripts).
- Lots of Visual Studio fixes.
- `crypto.aes` and `crypto.rc4` modules.
- Internal modules.





## V 0.1.16
*23 Jul 2019*
- V can now be used with Visual Studio!
- Hot code reloading now works with graphical applications (e.g. graph.v, bounce.v).
- Compile time memory management for arrays.
- High order functions.
- `match` expression (replacing `switch`).
- Import cycle detection.
- `crypto/md5`, `crypto/sha256`, and `crypro/sha512` modules.
- `os.executable()` - a cross platform function that returns full path to current executable.
- `~/.vlang` and `VROOT` were removed entirely. The installation is a lot cleaner now.
- V can now be packaged for all Linux distros.
- Arch Linux package.
- `string(bytes_buffer, len)`, `string(bytes_array)` casts.
- Multiple `defer`s.
- `key in map` syntax (replacing `map.exists(key)`).



## V 0.1.15
*15 Jul 2019*
- FreeBSD, OpenBSD, NetBSD, DragonFly support.
- Hot code reloading now works with graphical applications: [bounce.v](https://github.com/vlang/v/blob/master/examples/hot_code_reloading/bounce.v)
- VROOT was removed, the installation process is now much simpler.
- `defer` statement.
- map.v was re-written. It's now much faster.
- `for key, val in map` syntax.
- `flag` module for parsing command line arguments.
- `zip` module.
- `crypto/sha1` module.
- Submodules and module aliases (`import encoding.base64 as b64`).




## V 0.1.14
*12 Jul 2019*
- `gg` module Windows support, V Tetris runs on Windows.
- `glad` and `cJSON` are now compiled only once, this makes compilation of programs using `gg` and `json
  a bit faster.
- `v.c` has been cleaned up and minimized (~16k => ~10k lines of code).
- `type` aliases can now have methods.
- Const overflow check during compilation (`byte(1000)` will no longer compile)


## V 0.1.13
*10 Jul 2019*
- New enum syntax (`token == .name`), enum values are no longer global consts.
- Submodules (`import encoding.base64`).
- Hot code reloading.
- Special `err` variable for getting error values.
- Complex numbers.
- `<<` can now append arrays (`numbers << [1, 2, 3]`).
- Lots of Windows fixes (Windows still needs some work).
- Lots of REPL improvements (e.g. `>> 2 + 3` works now, no `println` required).
- The website was made easily translatable, it's now partially available in several languages.


## V 0.1.12
*4 Jul 2019*
- V can finally compile itself on Windows. (https://github.com/vlang/v#mingw-w64)
- `os` module now uses optionals in all functions that return `File`. Lots of  bugs with optionals fixed.
- `println` was optimized. It no longer results in allocations. Now it also works correctly with all integer types.
- Lots of `vfmt` fixes, it will be enabled tomorrow.
- New `strings` module.
- Lots of other fixes and improvements, thanks to all the contributors.


## V 0.1.11
*1 Jul 2019*
- Cross compilation for Windows!
- Lots of Windows fixes
- socket.v
- maps fixed


## V 0.1.9 - 0.1.10
*29 Jun 2019*
- Windows support via MinGW-w64. Pre-built Windows binary.
- File structure has been simplified: all vlib modules were moved to the vlib/ directory,
  makefile was moved to the root.
- One single archive with pre-built binaries for all operating systems.
- `mut var := val` was fixed (previously `mut var = val` was allowed as well).

## V 0.1.8
*28 Jun 2019*
- Single file programs without `fn main` now work as expected.
- REPL has been fixed: it now supports imports, consts, function definitions, etc.

## V 0.1.7
*27 Jun 2019*
- All C code in the compiler and vlib has been replaced with V.
- `#` syntax for embedding C code has been removed.
- Exported functions now need to be marked with `pub`, all public vlib functions have been updated.
- CI has been set up (Travis + Azure). On every commit and PR it is made sure that V
  can compile itself, all tests pass, and all examples compile.
- More tests have been uploaded.
- Cleaner bytes to string conversion: `tos2(bytes)` => `string(bytes)`.
- The home page has 3 more examples next to 'hello world' that show the features of the language.
- Lots of bugs and issues fixed.
```
## _vlib_ui_examples_users_gui_README_md
```<img src='https://raw.githubusercontent.com/vlang/v/master/vlib/ui/examples/users_gui/screenshot.png' width=612>
```
## _examples_word_counter_README_md
```'''
usage: word_counter [text_file]
using cinderella.txt
a => 25
able => 2
after => 1
afterwards => 1
again => 10
against => 2
all => 12
allow => 1
allowed => 2
along => 1
also => 2
always => 2
an => 4
and => 140
anew => 1
anger => 1
another => 2
answered => 1
any => 1
anyone => 2
...
'''
```
## _vlib_vweb_README_md
```This is pre-alpha software.

Lots of things are broken and not implemented yet in V and vweb.

There's no documentation yet, have a look at a simple example: 

https://github.com/vlang/v/tree/master/examples/vweb/test_app.v 

There's also the V forum: https://github.com/vlang/vorum 

`vorum.v` contains all GET and POST actions.

'''Go
pub fn (app mut App) index() {
	posts := app.find_all_posts()
	$vweb.html()
}

// TODO ['/post/:id/:title'] 
// TODO `fn (app App) post(id int)` 
pub fn (app App) post() {
	id := app.get_post_id() 
	post := app.retrieve_post(id) or {
		app.vweb.redirect('/') 
		return 
	}
	comments := app.find_comments(id)
	show_form := true 
	$vweb.html()
}

'''

`index.html` is an example of the V template language:

'''html
@for post in posts 
	<div class=post>
		<a class=topic href="@post.url">@post.title</a> 
		<img class=comment-img> 
		<span class=nr-comments>@post.nr_comments</span> 
		<span class=time>@post.time</span>
	</div>
@end
'''

`$vweb.html()` compiles an HTML template into V during compilation, and embeds the resulting code in current action.

That means that the template automatically has access to that action's entire environment.


### Deploying vweb apps

Everything, including HTML templates, is in one binary file. That's all you need to deploy.

```
## _examples_vcasino_README_md
```# VCasino
VCasino is a very simple game made to learn V.

# Compile and Run

Use this to generate a binary and then launch the game.
'''bash
v VCasino.v
./VCasino
'''

And this to compile and launch the game directly.
'''bash
v run VCasino.v
'''

Created by Thomas Senechal : https://github.com/thomas-senechal/VCasino
```
## _examples_game_of_life_README_md
```# Conway's Game of Life

![](https://github.com/fuyutarow/Conways-Game-of-Life-with-Vlang/raw/master/v-gun.gif)


'''v
v run life.v
'''

Created by fuyutarow: https://github.com/fuyutarow/Conways-Game-of-Life-with-Vlang


```
## _github_ISSUE_TEMPLATE_bug_report_md
```---
name: Bug report
about: Bug report
title: ''
labels: bug
assignees: ''

---

**V version:** 
**OS:** 

**What did you do?**


**What did you expect to see?**

 
**What did you see instead?**
```
## _vlib_gg_README_md
````gg` will be moved to its own repository:

https://github.com/vlang/gg
```
## _github_ISSUE_TEMPLATE_feature_request_md
```---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: feature request
assignees: ''

---


```
## _README_md
```# The V Programming Language

[![Build Status](https://github.com/vlang/v/workflows/CI/badge.svg)](https://github.com/vlang/v/commits/master)
[![Build Status](https://travis-ci.org/vlang/v.svg?branch=master)](https://travis-ci.org/vlang/v)
<a href='https://patreon.com/vlang'><img src='https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fshieldsio-patreon.herokuapp.com%2Fvlang%2Fpledges&style=for-the-badge' height='20'></a>

https://vlang.io

Documentation: [vlang.io/docs](https://vlang.io/docs)

Changelog: [github.com/vlang/v/blob/master/CHANGELOG.md](https://github.com/vlang/v/blob/master/CHANGELOG.md) 

Twitter: [twitter.com/v_language](https://twitter.com/v_language)

Discord (primary community): [discord.gg/n7c74HM](https://discord.gg/n7c74HM)

Installing V: [github.com/vlang/v#installing-v-from-source](https://github.com/vlang/v#installing-v-from-source)


## Key Features of V

- Simplicity: the language can be learned in less than an hour
- Fast compilation: ≈100k — 1.2 million loc/s
- Easy to develop: V compiles itself in less than a second
- Performance: within 3% of C
- Safety: no null, no globals, no undefined behavior, immutability by default
- C to V translation
- Hot code reloading
- Powerful UI and graphics libraries
- Easy cross compilation
- REPL
- Built-in ORM
- C and JavaScript backends

V 1.0 release is planned for December 2019. Right now V is in an alpha stage.

## Installing V from source

### Linux, macOS, Windows, *BSD, Solaris, WSL, Android, Raspbian


'''bash
git clone https://github.com/vlang/v
cd v
make
'''

That's it! Now you have a V executable at `[path to V repo]/v`. `[path to V repo]` can be anywhere.

(On Windows `make` means running `make.bat`, so make sure you use `cmd.exe`.)

V is being constantly updated. To update V, simply run

'''
v up
'''


### C compiler

You'll need Clang or GCC or Visual Studio. If you are doing development, you most likely already have one of those installed.

Otherwise, follow these instructions:

[https://github.com/vlang/v/wiki/Installing-a-C-compiler-on-Linux-macOS](https://github.com/vlang/v/wiki/Installing-a-C-compiler-on-Linux-macOS)

[github.com/vlang/v/wiki/Installing-a-C-compiler-on-Windows](https://github.com/vlang/v/wiki/Installing-a-C-compiler-on-Windows)


### Symlinking

You can create a `/usr/local/bin/v` symlink so that V is globally available:

'''bash
sudo ./v symlink
'''


### Docker

'''bash
git clone https://github.com/vlang/v
cd v
docker build -t vlang .
docker run --rm -it vlang:latest
v
'''



### Testing and running the examples

Make sure V can compile itself:

'''
v v.v
'''

'''bash
$ v
V 0.1.x
Use Ctrl-C or `exit` to exit

>>> println('hello world')
hello world
>>>
'''


'''bash
cd examples
v hello_world.v && ./hello_world    # or simply
v run hello_world.v                 # this builds the program and runs it right away

v word_counter.v && ./word_counter cinderella.txt
v run news_fetcher.v
v run tetris/tetris.v
'''

<img src='https://raw.githubusercontent.com/vlang/v/master/examples/tetris/screenshot.png' width=300>

In order to build Tetris and anything else using the graphics module, you will need to install glfw and freetype libraries.

If you plan to use the http package, you also need to install OpenSSL on non-Windows systems.

'''
macOS:
brew install glfw freetype openssl

Debian/Ubuntu:
sudo apt install libglfw3 libglfw3-dev libfreetype6-dev libssl-dev

Arch/Manjaro:
sudo pacman -S glfw-x11 freetype2

Fedora:
sudo dnf install glfw glfw-devel freetype-devel

Windows:
git clone --depth=1 https://github.com/ubawurinna/freetype-windows-binaries [path to v repo]/thirdparty/freetype/

'''

glfw dependency will be removed soon.

## JavaScript backend

[examples/hello_v_js.v](examples/hello_v_js.v):

'''v
fn main() {
        for i := 0; i < 3; i++ {
                println('Hello from V.js')
        }
}
'''

'''bash
v -o hi.js examples/hello_v_js.v && node hi.js
Hello from V.js
Hello from V.js
Hello from V.js
'''

## Troubleshooting:

https://github.com/vlang/v/wiki/Troubleshooting


## Contributing

Code structure:

https://github.com/vlang/v/blob/master/CONTRIBUTING.md

If you introduce a breaking change and rebuild V, you will no longer be able to use V to build itself. So it's a good idea to make a backup copy of a working compiler executable.


```
## _CONTRIBUTING_md
```## Code Structure

I tried making the code of the compiler and vlib as simple and readable as possible. One of V's goals is to be open to developers with different levels of experience in compiler development. Compilers don't need to be black boxes full of magic that only few people understand.

The compiler itself is located in `vlib/compiler/`. It's a module that can be used by other
applications.

The main files are:

1. `v.v` and `vlib/compiler/main.v`. The entry point.

- V figures out the build mode.
- Constructs the compiler object (`struct V`).
- Creates a list of .v files that need to be parsed.
- Creates a parser object for each file and runs `parse()` on them (this should work concurrently in the future). The parser emits C or x64 code directly. For performance reasons, there are no intermediate steps (no AST or Assembly code generation).
- If the parsing is successful, a single C file is generated by merging the output from the parsers and carefully arranging all definitions (C is a single pass language).
- Finally, a C compiler is called to compile this C file and generate an executable or a library.

2. `parser.v` The core of the compiler. This is the largest file (~3.5k loc). `parse()` method asks the scanner to generate a list of tokens for the file it needs to parse. Then it simply goes through all the tokens one by one.

   In V, objects can be used before declaration, so there are 2 passes. During the first pass, it only looks at declarations and skips function bodies. It memorizes all function signatures, types, consts, etc. During the second pass it looks at function bodies and generates C (e.g. `cgen('if ($expr) {'`) or machine code (e.g. `gen.mov(EDI, 1)`).

   The formatter is embedded in the parser. Correctly formatted tokens are emitted as they are parsed. This allowed us to simplify the compiler and avoid duplication, but slowed it down a bit. In the future, this will be fixed with build flags and separate binaries for C generation, machine code generation, and formatting. This way there will be no unnecessary branching and function calls.

3. `scanner.v` The scanner's job is to parse a list of characters and convert them to tokens. It also takes care of string interpolation, which is a mess at the moment.

4. `token.v` This is simply a list of all tokens, their string values, and a couple of helper functions.

5. `table.v` V creates one table object that is shared by all parsers. It contains all types, consts, and functions, as well as several helpers to search for objects by name, register new objects, modify types' fields, etc.

6. `cgen.v` The small `Cgen` struct helps generate C code. It's also shared by all parsers. It has a couple of functions that allow to go back and set something that was previously unknown (like with `a := 0` => `int a = 0;`). Some of these functions are hacky and need improvements and simplifications.

7. `fn.v` Handles declaring and calling normal and async functions and methods. This file is about 1000 lines of code, and has some complex logic. It needs to be cleaned up and simplified a bit.

8. `json.v` defines the json code generation. This file will be removed once V supports comptime code generation, and it will be possible to do this using the language's tools.

9. `x64/` is the directory with all the machine code generation logic. It's not released yet. Obviously this is the most complex part of the compiler. It defines a set of functions that translates assembly instructions to machine code, it builds complicated binaries from scratch byte by byte. It manually builds all headers, segments, sections, symtable, relocations, etc. Right now it only has basic support of the x64 platform/Mach-O format, and it can only generate `.o` files, which then have to be linked with `lld`.

The rest of the directories are vlib modules: `builtin/` (strings, arrays, maps), `time/`, `os/`, etc. Their documentation is pretty clear.

## Example Workflow for Contributing
##### (provided by [@spytheman](https://github.com/spytheman))

(If you don't already have a Github account, please create one. Your Github username will be referred to later as 'YOUR_GITHUB_USERNAME'. Change it accordingly in the steps below.)

1. Clone https://github.com/vlang/v in a folder, say nv (`git clone https://github.com/vlang/v nv`)
1. `cd nv`
1. `git remote add pullrequest git@github.com:YOUR_GITHUB_USERNAME/v.git`  # (NOTE: this is your own forked repo of: https://github.com/vlang/v - After this, we just do normal git operations such as: `git pull` and so on.)
1. When finished with a feature/bugfix, you can: `git checkout -b fix_alabala`
1. `git push pullrequest`  # (NOTE: the pullrequest remote was setup on step 3)
1. On Github's web interface, I go to: https://github.com/vlang/v/pulls  Here the UI shows a nice dialog with a button to make a new pull request based on the new pushed branch. (Example dialogue: https://url4e.com/gyazo/images/364edc04.png)
1. After making your pullrequest (aka, PR), you can continue to work on the branch... just do step #5 when you have more commits.
1. If there are merge conflicts, or a branch lags too much behind V's master, you can do the following:
   1. `git checkout master`
   1. `git pull`
   1. `git checkout fix_alabala`
   1. `git rebase master`  # solve conflicts and do git rebase --continue
   1. `git push pullrequest -f`

The point of doing the above steps to never directly push to the main V repository, only to your own fork. Since your local master branch tracks the main V repository's master, then `git checkout master; git pull --rebase origin master` work as expected (this is actually used by `v up`) and it can always do so cleanly. Git is very flexible, so there may be simpler/easier ways to accomplish the same thing.
```
## _vlib_ui_README_md
```# V UI

V UI is a cross-platform UI toolkit for Windows, macOS, Linux, Android, and iOS. It uses native widgets on each platform.

V UI is licensed under GPL3. A commercial license will be available.

Open-source projects will have access to the commercial license for free. That means that if you have an open-source non-GPL project, you won't have to relicense it under GPL to use V UI.

Every single feature will be open-sourced right away and available under both licenses.
```
## _CODE_OF_CONDUCT_md
```# Code of Conduct

Be nice and respectful.

```
## _github_ISSUE_TEMPLATE_bug_report_for_v_md
```---
name: Bug report for V
about: Please use the apropriate label when submitting an issue: bug/feature request/question.
title: "New issue"
labels: ''
assignees: ''

---

#### V version:


#### OS:


#### C Compiler:


## What did you do?


### What did you expect to see?


### What did you see instead?
```
## _vlib_compiler_tests_repl_README_md
```# V REPL Tests Script

### How to write a new test
  - Create a new file named `*.repl`
  - Write the input to be given to REPL
  - Add `===output===`
  - Write the output expected
  
### Notes
Keep in mind, that the way V repl works for now, every non empty line
would cause a new recompilation of the entire repl content that was
collected so far. 

*Longer REPL files would cause measurably*
*longer recompilation/testing times.*

Also, longer repl files would be slower to debug when they fail,
*It is better to have several smaller files vs one huge REPL file.*

### Example :
'''
a := 1
println(a)
===output===
1
```
## _examples_tetris_README_md
```<img src='https://raw.githubusercontent.com/vlang/v/master/examples/tetris/screenshot.png' width=300>

Tetris has a temporary dependency on GLFW. 

## macOS
`brew install glfw` 
 
## Ubuntu 
`sudo apt install libglfw3 libglfw3-dev`

## Arch (and Manjaro)
`sudo pacman -S glfw-x11` 

## Windows 
Copy `thirdparty/glfw/glfw3.dll` to this directory. 
```
# Inline
## _thirdparty_cJSON_cJSON_c
### Line 22-73
```

/* cJSON */
/* JSON parser in C. */

/* disable warnings about old C89 functions in MSVC */
#if !defined(_CRT_SECURE_NO_DEPRECATE) && defined(_MSC_VER)
#define _CRT_SECURE_NO_DEPRECATE
#endif

#ifdef __GNUC__
#pragma GCC visibility push(default)
#endif
#if defined(_MSC_VER)
#pragma warning (push)
/* disable warning about single line comments in system headers */
#pragma warning (disable : 4001)
#endif

#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <ctype.h>

#ifdef ENABLE_LOCALES
#include <locale.h>
#endif

#if defined(_MSC_VER)
#pragma warning (pop)
#endif
#ifdef __GNUC__
#pragma GCC visibility pop
#endif

#include "cJSON.h"

/* define our own boolean type */
#ifdef true
#undef true
#endif
#define true ((cJSON_bool)1)

#ifdef false
#undef false
#endif
#define false ((cJSON_bool)0)

typedef struct {
    const unsigned char *json;
    size_t position;

```
### Line 86-97
```

    return item->valuestring;
}

/* This is a safeguard to prevent copy-pasters from using incompatible C and header files */
#if (CJSON_VERSION_MAJOR != 1) || (CJSON_VERSION_MINOR != 7) || (CJSON_VERSION_PATCH != 12)
    #error cJSON.h and cJSON.c have different versions. Make sure that both have the same.
#endif

CJSON_PUBLIC(const char*) cJSON_Version(void)
{
    static char version[15];

```
### Line 129-138
```
    void *(CJSON_CDECL *allocate)(size_t size);
    void (CJSON_CDECL *deallocate)(void *pointer);
    void *(CJSON_CDECL *reallocate)(void *pointer, size_t size);
} internal_hooks;

#if defined(_MSC_VER)
/* work around MSVC error C2322: '...' address of dillimport '...' is not static */
static void * CJSON_CDECL internal_malloc(size_t size)
{
    return malloc(size);

```
### Line 143-159
```
}
static void * CJSON_CDECL internal_realloc(void *pointer, size_t size)
{
    return realloc(pointer, size);
}
#else
#define internal_malloc malloc
#define internal_free free
#define internal_realloc realloc
#endif

/* strlen of character literals resolved at compile time */
#define static_strlen(string_literal) (sizeof(string_literal) - sizeof(""))

static internal_hooks global_hooks = { internal_malloc, internal_free, internal_realloc };

static unsigned char* cJSON_strdup(const unsigned char* string, const internal_hooks * const hooks)

```
### Line 245-259
```
}

/* get the decimal point character of the current locale */
static unsigned char get_decimal_point(void)
{
#ifdef ENABLE_LOCALES
    struct lconv *lconv = localeconv();
    return (unsigned char) lconv->decimal_point[0];
#else
    return '.';
#endif
}

typedef struct
{

```
### Line 263-277
```
    size_t depth; /* How deeply nested (in arrays/objects) is the input at the current offset. */
    internal_hooks hooks;
} parse_buffer;

/* check if the given size is left to read in a given parse buffer (starting with 1) */
#define can_read(buffer, size) ((buffer != NULL) && (((buffer)->offset + size) <= (buffer)->length))
/* check if the buffer can be accessed at the given index (starting with 0) */
#define can_access_at_index(buffer, index) ((buffer != NULL) && (((buffer)->offset + index) < (buffer)->length))
#define cannot_access_at_index(buffer, index) (!can_access_at_index(buffer, index))
/* get a pointer to the buffer at the position */
#define buffer_at_offset(buffer) ((buffer)->content + (buffer)->offset)

/* Parse the input text to generate a number, and populate the result into item. */
static cJSON_bool parse_number(cJSON * const item, parse_buffer * const input_buffer)
{

```
### Line 1090-1099
```
CJSON_PUBLIC(cJSON *) cJSON_Parse(const char *value)
{
    return cJSON_ParseWithOpts(value, 0, 0);
}

#define cjson_min(a, b) ((a < b) ? a : b)

static unsigned char *print(const cJSON * const item, cJSON_bool format, const internal_hooks * const hooks)
{
    static const size_t default_buffer_size = 256;

```
### Line 1888-1910
```
CJSON_PUBLIC(void) cJSON_AddItemToArray(cJSON *array, cJSON *item)
{
    add_item_to_array(array, item);
}

#if defined(__clang__) || (defined(__GNUC__)  && ((__GNUC__ > 4) || ((__GNUC__ == 4) && (__GNUC_MINOR__ > 5))))
    #pragma GCC diagnostic push
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wcast-qual"
#endif
/* helper function to cast away const */
static void* cast_away_const(const void* string)
{
    return (void*)string;
}
#if defined(__clang__) || (defined(__GNUC__)  && ((__GNUC__ > 4) || ((__GNUC__ == 4) && (__GNUC_MINOR__ > 5))))
    #pragma GCC diagnostic pop
#endif


static cJSON_bool add_item_to_object(cJSON * const object, const char * const string, cJSON * const item, const internal_hooks * const hooks, const cJSON_bool constant_key)
{

```

## _thirdparty_zip_zip_c
### Line 5-57
```
 * IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 * OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 * ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 */
#define __STDC_WANT_LIB_EXT1__ 1

#include <errno.h>
#include <sys/stat.h>
#include <time.h>

#if defined(_WIN32) || defined(__WIN32__) || defined(_MSC_VER) ||              \
    defined(__MINGW32__)
/* Win32, DOS, MSVC, MSVS */
#include <direct.h>

#define MKDIR(DIRNAME) _mkdir(DIRNAME)
#define STRCLONE(STR) ((STR) ? _strdup(STR) : NULL)
#define HAS_DEVICE(P)                                                          \
  ((((P)[0] >= 'A' && (P)[0] <= 'Z') || ((P)[0] >= 'a' && (P)[0] <= 'z')) &&   \
   (P)[1] == ':')
#define FILESYSTEM_PREFIX_LEN(P) (HAS_DEVICE(P) ? 2 : 0)

#else

#include <unistd.h> // needed for symlink() on BSD
int symlink(const char *target, const char *linkpath); // needed on Linux

#define MKDIR(DIRNAME) mkdir(DIRNAME, 0755)
#define STRCLONE(STR) ((STR) ? strdup(STR) : NULL)

#endif

#include "miniz.h"
#include "zip.h"

#ifndef HAS_DEVICE
#define HAS_DEVICE(P) 0
#endif

#ifndef FILESYSTEM_PREFIX_LEN
#define FILESYSTEM_PREFIX_LEN(P) 0
#endif

#ifndef ISSLASH
#define ISSLASH(C) ((C) == '/' || (C) == '\\')
#endif

#define CLEANUP(ptr)                                                           \
  do {                                                                         \
    if (ptr) {                                                                 \
      free((void *)ptr);                                                       \
      ptr = NULL;                                                              \

```
### Line 83-105
```
  int len = 0;
  int has_device = HAS_DEVICE(path);

  memset(npath, 0, MAX_PATH + 1);
  if (has_device) {
    // only on windows
    npath[0] = path[0];
    npath[1] = path[1];
    len = 2;
  }
  for (p = path + len; *p && len < MAX_PATH; p++) {
    if (ISSLASH(*p) && ((!has_device && len > 0) || (has_device && len > 2))) {
#if defined(_WIN32) || defined(__WIN32__) || defined(_MSC_VER) ||              \
    defined(__MINGW32__)
#else
      if ('\\' == *p) {
        *p = '/';
      }
#endif

      if (MKDIR(npath) == -1) {
        if (errno != EEXIST) {
          return -1;

```
### Line 154-171
```
};

struct zip_t *zip_open(const char *zipname, int level, char mode) {
  struct zip_t *zip = NULL;
  if (!zipname || strlen(zipname) < 1) {
    // zip_t archive name is empty or NULL
    printf("%s", "name len");
    goto cleanup;
  }

  if (level < 0)
    level = MZ_DEFAULT_LEVEL;
  if ((level & 0xF) > MZ_UBER_COMPRESSION) {
    // Wrong compression level
    printf("%s", "Wrong compression");
    goto cleanup;
  }


```
### Line 175-184
```
    goto cleanup;

  zip->level = (mz_uint)level;
  switch (mode) {
  case 'w':
    // Create a new archive.
    if (!mz_zip_writer_init_file(&(zip->archive), zipname, 0)) {
      printf("%s", "Cannot initialize zip_archive writer");
      goto cleanup;
    }

```
### Line 187-197
```
  case 'r':
  case 'a':
    if (!mz_zip_reader_init_file(
            &(zip->archive), zipname,
            zip->level | MZ_ZIP_FLAG_DO_NOT_SORT_CENTRAL_DIRECTORY)) {
      // An archive file does not exist or cannot initialize
      // zip_archive reader
      goto cleanup;
    }
    if (mode == 'a' &&
        !mz_zip_writer_init_from_reader(&(zip->archive), zipname)) {

```
### Line 212-222
```
}

void zip_close(struct zip_t *zip) {
  printf("%s", "try to close");
  if (zip) {
    // Always finalize, even if adding failed for some reason, so we have a
    // valid central directory.
    mz_zip_writer_finalize_archive(&(zip->archive));

    mz_zip_writer_end(&(zip->archive));
    mz_zip_reader_end(&(zip->archive));

```
### Line 251-260
```
    and UNIX file systems etc.  If input came from standard
    input, there is no file name field.
  */
  zip->entry.name = strrpl(entryname, entrylen, '\\', '/');
  if (!zip->entry.name) {
    // Cannot parse zip entry name
    return -1;
  }

  pzip = &(zip->archive);

```
### Line 288-327
```
  zip->entry.offset = zip->archive.m_archive_size;
  zip->entry.header_offset = zip->archive.m_archive_size;
  memset(zip->entry.header, 0, MZ_ZIP_LOCAL_DIR_HEADER_SIZE * sizeof(mz_uint8));
  zip->entry.method = 0;

  // UNIX or APPLE
#if MZ_PLATFORM == 3 || MZ_PLATFORM == 19
  // regular file with rw-r--r-- persmissions
  zip->entry.external_attr = (mz_uint32)(0100644) << 16;
#else
  zip->entry.external_attr = 0;
#endif

  num_alignment_padding_bytes =
      mz_zip_writer_compute_padding_needed_for_file_alignment(pzip);

  if (!pzip->m_pState || (pzip->m_zip_mode != MZ_ZIP_MODE_WRITING)) {
    // Wrong zip mode
    goto cleanup;
  }
  if (zip->level & MZ_ZIP_FLAG_COMPRESSED_DATA) {
    // Wrong zip compression level
    goto cleanup;
  }
  // no zip64 support yet
  if ((pzip->m_total_files == 0xFFFF) ||
      ((pzip->m_archive_size + num_alignment_padding_bytes +
        MZ_ZIP_LOCAL_DIR_HEADER_SIZE + MZ_ZIP_CENTRAL_DIR_HEADER_SIZE +
        entrylen) > 0xFFFFFFFF)) {
    // No zip64 support yet
    goto cleanup;
  }
  if (!mz_zip_writer_write_zeros(pzip, zip->entry.offset,
                                 num_alignment_padding_bytes +
                                     sizeof(zip->entry.header))) {
    // Cannot memset zip entry header
    goto cleanup;
  }

  zip->entry.header_offset += num_alignment_padding_bytes;

```
### Line 331-340
```
  }
  zip->entry.offset += num_alignment_padding_bytes + sizeof(zip->entry.header);

  if (pzip->m_pWrite(pzip->m_pIO_opaque, zip->entry.offset, zip->entry.name,
                     entrylen) != entrylen) {
    // Cannot write data to zip entry
    goto cleanup;
  }

  zip->entry.offset += entrylen;

```
### Line 347-356
```
    if (tdefl_init(&(zip->entry.comp), mz_zip_writer_add_put_buf_callback,
                   &(zip->entry.state),
                   (int)tdefl_create_comp_flags_from_zip_params(
                       (int)level, -15, MZ_DEFAULT_STRATEGY)) !=
        TDEFL_STATUS_OKAY) {
      // Cannot initialize the zip compressor
      goto cleanup;
    }
  }


```
### Line 369-397
```
  mz_uint namelen;
  const mz_uint8 *pHeader;
  const char *pFilename;

  if (!zip) {
    // zip_t handler is not initialized
    return -1;
  }

  pZip = &(zip->archive);
  if (pZip->m_zip_mode != MZ_ZIP_MODE_READING) {
    // open by index requires readonly mode
    return -1;
  }

  if (index < 0 || (mz_uint)index >= pZip->m_total_files) {
    // index out of range
    return -1;
  }

  if (!(pHeader = &MZ_ZIP_ARRAY_ELEMENT(
            &pZip->m_pState->m_central_dir, mz_uint8,
            MZ_ZIP_ARRAY_ELEMENT(&pZip->m_pState->m_central_dir_offsets,
                                 mz_uint32, index)))) {
    // cannot find header in central directory
    return -1;
  }

  namelen = MZ_READ_LE16(pHeader + MZ_ZIP_CDH_FILENAME_LEN_OFS);

```
### Line 408-417
```
    and UNIX file systems etc.  If input came from standard
    input, there is no file name field.
  */
  zip->entry.name = strrpl(pFilename, namelen, '\\', '/');
  if (!zip->entry.name) {
    // local entry name is NULL
    return -1;
  }

  if (!mz_zip_reader_file_stat(pZip, (mz_uint)index, &stats)) {

```
### Line 438-447
```
  mz_uint16 entrylen;
  mz_uint16 dos_time, dos_date;
  int status = -1;

  if (!zip) {
    // zip_t handler is not initialized
    goto cleanup;
  }

  pzip = &(zip->archive);

```
### Line 452-497
```

  level = zip->level & 0xF;
  if (level) {
    done = tdefl_compress_buffer(&(zip->entry.comp), "", 0, TDEFL_FINISH);
    if (done != TDEFL_STATUS_DONE && done != TDEFL_STATUS_OKAY) {
      // Cannot flush compressed buffer
      goto cleanup;
    }
    zip->entry.comp_size = zip->entry.state.m_comp_size;
    zip->entry.offset = zip->entry.state.m_cur_archive_file_ofs;
    zip->entry.method = MZ_DEFLATED;
  }

  entrylen = (mz_uint16)strlen(zip->entry.name);
  // no zip64 support yet
  if ((zip->entry.comp_size > 0xFFFFFFFF) || (zip->entry.offset > 0xFFFFFFFF)) {
    // No zip64 support, yet
    goto cleanup;
  }

  mz_zip_time_t_to_dos_time(zip->entry.m_time, &dos_time, &dos_date);
  if (!mz_zip_writer_create_local_dir_header(
          pzip, zip->entry.header, entrylen, 0, zip->entry.uncomp_size,
          zip->entry.comp_size, zip->entry.uncomp_crc32, zip->entry.method, 0,
          dos_time, dos_date)) {
    // Cannot create zip entry header
    goto cleanup;
  }

  if (pzip->m_pWrite(pzip->m_pIO_opaque, zip->entry.header_offset,
                     zip->entry.header,
                     sizeof(zip->entry.header)) != sizeof(zip->entry.header)) {
    // Cannot write zip entry header
    goto cleanup;
  }

  if (!mz_zip_writer_add_to_central_dir(
          pzip, zip->entry.name, entrylen, NULL, 0, "", 0,
          zip->entry.uncomp_size, zip->entry.comp_size, zip->entry.uncomp_crc32,
          zip->entry.method, 0, dos_time, dos_date, zip->entry.header_offset,
          zip->entry.external_attr)) {
    // Cannot write to zip central dir
    goto cleanup;
  }

  pzip->m_total_files++;

```
### Line 506-538
```
  return status;
}

const char *zip_entry_name(struct zip_t *zip) {
  if (!zip) {
    // zip_t handler is not initialized
    return NULL;
  }

  return zip->entry.name;
}

int zip_entry_index(struct zip_t *zip) {
  if (!zip) {
    // zip_t handler is not initialized
    return -1;
  }

  return zip->entry.index;
}

int zip_entry_isdir(struct zip_t *zip) {
  if (!zip) {
    // zip_t handler is not initialized
    return -1;
  }

  if (zip->entry.index < 0) {
    // zip entry is not opened
    return -1;
  }

  return (int)mz_zip_reader_is_file_a_directory(&zip->archive,

```
### Line 551-560
```
  mz_uint level;
  mz_zip_archive *pzip = NULL;
  tdefl_status status;

  if (!zip) {
    // zip_t handler is not initialized
    return -1;
  }

  pzip = &(zip->archive);

```
### Line 565-583
```

    level = zip->level & 0xF;
    if (!level) {
      if ((pzip->m_pWrite(pzip->m_pIO_opaque, zip->entry.offset, buf,
                          bufsize) != bufsize)) {
        // Cannot write buffer
        return -1;
      }
      zip->entry.offset += bufsize;
      zip->entry.comp_size += bufsize;
    } else {
      status = tdefl_compress_buffer(&(zip->entry.comp), buf, bufsize,
                                     TDEFL_NO_FLUSH);
      if (status != TDEFL_STATUS_DONE && status != TDEFL_STATUS_OKAY) {
        // Cannot compress buffer
        return -1;
      }
    }
  }

```
### Line 591-624
```
  FILE *stream = NULL;
  mz_uint8 buf[MZ_ZIP_MAX_IO_BUF_SIZE];
  struct MZ_FILE_STAT_STRUCT file_stat;

  if (!zip) {
    // zip_t handler is not initialized
    return -1;
  }

  memset(buf, 0, MZ_ZIP_MAX_IO_BUF_SIZE);
  memset((void *)&file_stat, 0, sizeof(struct MZ_FILE_STAT_STRUCT));
  if (MZ_FILE_STAT(filename, &file_stat) != 0) {
    // problem getting information - check errno
    return -1;
  }

  if ((file_stat.st_mode & 0200) == 0) {
    // MS-DOS read-only attribute
    zip->entry.external_attr |= 0x01;
  }
  zip->entry.external_attr |= (mz_uint32)((file_stat.st_mode & 0xFFFF) << 16);
  zip->entry.m_time = file_stat.st_mtime;

#if defined(_MSC_VER)
  if (fopen_s(&stream, filename, "rb"))
#else
  if (!(stream = fopen(filename, "rb")))
#endif
  {
    // Cannot open filename
    return -1;
  }

  while ((n = fread(buf, sizeof(mz_uint8), MZ_ZIP_MAX_IO_BUF_SIZE, stream)) >

```
### Line 637-658
```
  mz_zip_archive *pzip = NULL;
  mz_uint idx;
  size_t size = 0;

  if (!zip) {
    // zip_t handler is not initialized
    return -1;
  }

  pzip = &(zip->archive);
  if (pzip->m_zip_mode != MZ_ZIP_MODE_READING || zip->entry.index < 0) {
    // the entry is not found or we do not have read access
    return -1;
  }

  idx = (mz_uint)zip->entry.index;
  if (mz_zip_reader_is_file_a_directory(pzip, idx)) {
    // the entry is a directory
    return -1;
  }

  *buf = mz_zip_reader_extract_to_heap(pzip, idx, &size, 0);

```
### Line 664-679
```

ssize_t zip_entry_noallocread(struct zip_t *zip, void *buf, size_t bufsize) {
  mz_zip_archive *pzip = NULL;

  if (!zip) {
    // zip_t handler is not initialized
    return -1;
  }

  pzip = &(zip->archive);
  if (pzip->m_zip_mode != MZ_ZIP_MODE_READING || zip->entry.index < 0) {
    // the entry is not found or we do not have read access
    return -1;
  }

  if (!mz_zip_reader_extract_to_mem_no_alloc(pzip, (mz_uint)zip->entry.index,

```
### Line 689-722
```
  mz_uint idx;
  mz_uint32 xattr = 0;
  mz_zip_archive_file_stat info;

  if (!zip) {
    // zip_t handler is not initialized
    return -1;
  }

  memset((void *)&info, 0, sizeof(mz_zip_archive_file_stat));
  pzip = &(zip->archive);
  if (pzip->m_zip_mode != MZ_ZIP_MODE_READING || zip->entry.index < 0) {
    // the entry is not found or we do not have read access
    return -1;
  }

  idx = (mz_uint)zip->entry.index;
  if (mz_zip_reader_is_file_a_directory(pzip, idx)) {
    // the entry is a directory
    return -1;
  }

  if (!mz_zip_reader_extract_to_file(pzip, idx, filename, 0)) {
    return -1;
  }

#if defined(_MSC_VER)
#else
  if (!mz_zip_reader_file_stat(pzip, idx, &info)) {
    // Cannot get information about zip archive;
    return -1;
  }

  xattr = (info.m_external_attr >> 16) & 0xFFFF;

```
### Line 723-732
```
  if (xattr > 0) {
    if (chmod(filename, (mode_t)xattr) < 0) {
      return -1;
    }
  }
#endif

  return 0;
}


```
### Line 736-751
```
                      void *arg) {
  mz_zip_archive *pzip = NULL;
  mz_uint idx;

  if (!zip) {
    // zip_t handler is not initialized
    return -1;
  }

  pzip = &(zip->archive);
  if (pzip->m_zip_mode != MZ_ZIP_MODE_READING || zip->entry.index < 0) {
    // the entry is not found or we do not have read access
    return -1;
  }

  idx = (mz_uint)zip->entry.index;

```
### Line 754-763
```
             : -1;
}

int zip_total_entries(struct zip_t *zip) {
  if (!zip) {
    // zip_t handler is not initialized
    return -1;
  }

  return (int)zip->archive.m_total_files;

```
### Line 769-789
```
  mz_zip_archive zip_archive;
  struct MZ_FILE_STAT_STRUCT file_stat;
  mz_uint32 ext_attributes = 0;

  if (!zipname || strlen(zipname) < 1) {
    // zip_t archive name is empty or NULL
    return -1;
  }

  // Create a new archive.
  if (!memset(&(zip_archive), 0, sizeof(zip_archive))) {
    // Cannot memset zip archive
    return -1;
  }

  if (!mz_zip_writer_init_file(&zip_archive, zipname, 0)) {
    // Cannot initialize zip_archive writer
    return -1;
  }

  memset((void *)&file_stat, 0, sizeof(struct MZ_FILE_STAT_STRUCT));

```
### Line 794-816
```
      status = -1;
      break;
    }

    if (MZ_FILE_STAT(name, &file_stat) != 0) {
      // problem getting information - check errno
      return -1;
    }

    if ((file_stat.st_mode & 0200) == 0) {
      // MS-DOS read-only attribute
      ext_attributes |= 0x01;
    }
    ext_attributes |= (mz_uint32)((file_stat.st_mode & 0xFFFF) << 16);

    if (!mz_zip_writer_add_file(&zip_archive, base_name(name), name, "", 0,
                                ZIP_DEFAULT_COMPRESSION_LEVEL,
                                ext_attributes)) {
      // Cannot add file to zip_archive
      status = -1;
      break;
    }
  }

```
### Line 832-905
```
  mz_uint32 xattr = 0;

  memset(path, 0, sizeof(path));
  memset(symlink_to, 0, sizeof(symlink_to));
  if (!memset(&(zip_archive), 0, sizeof(zip_archive))) {
    // Cannot memset zip archive
    return -1;
  }

  if (!zipname || !dir) {
    // Cannot parse zip archive name
    return -1;
  }

  dirlen = strlen(dir);
  if (dirlen + 1 > MAX_PATH) {
    return -1;
  }

  // Now try to open the archive.
  if (!mz_zip_reader_init_file(&zip_archive, zipname, 0)) {
    // Cannot initialize zip_archive reader
    return -1;
  }

  memset((void *)&info, 0, sizeof(mz_zip_archive_file_stat));

#if defined(_MSC_VER)
  strcpy_s(path, MAX_PATH, dir);
#else
  strcpy(path, dir);
#endif

  if (!ISSLASH(path[dirlen - 1])) {
#if defined(_WIN32) || defined(__WIN32__)
    path[dirlen] = '\\';
#else
    path[dirlen] = '/';
#endif
    ++dirlen;
  }

  // Get and print information about each file in the archive.
  n = mz_zip_reader_get_num_files(&zip_archive);
  for (i = 0; i < n; ++i) {
    if (!mz_zip_reader_file_stat(&zip_archive, i, &info)) {
      // Cannot get information about zip archive;
      goto out;
    }
#if defined(_MSC_VER)
    strncpy_s(&path[dirlen], MAX_PATH - dirlen, info.m_filename,
              MAX_PATH - dirlen);
#else
    strncpy(&path[dirlen], info.m_filename, MAX_PATH - dirlen);
#endif
    if (mkpath(path) < 0) {
      // Cannot make a path
      goto out;
    }

    if ((((info.m_version_made_by >> 8) == 3) ||
         ((info.m_version_made_by >> 8) ==
          19)) // if zip is produced on Unix or macOS (3 and 19 from
               // section 4.4.2.2 of zip standard)
        && info.m_external_attr &
               (0x20 << 24)) { // and has sym link attribute (0x80 is file, 0x40
                               // is directory)
#if defined(_WIN32) || defined(__WIN32__) || defined(_MSC_VER) ||              \
    defined(__MINGW32__)
#else
      if (info.m_uncomp_size > MAX_PATH ||
          !mz_zip_reader_extract_to_mem_no_alloc(&zip_archive, i, symlink_to,
                                                 MAX_PATH, 0, NULL, 0)) {
        goto out;

```
### Line 906-932
```
      }
      symlink_to[info.m_uncomp_size] = '\0';
      if (symlink(symlink_to, path) != 0) {
        goto out;
      }
#endif
    } else {
      if (!mz_zip_reader_is_file_a_directory(&zip_archive, i)) {
        if (!mz_zip_reader_extract_to_file(&zip_archive, i, path, 0)) {
          // Cannot extract zip archive to file
          goto out;
        }
      }

#if defined(_MSC_VER)
#else
      xattr = (info.m_external_attr >> 16) & 0xFFFF;
      if (xattr > 0) {
        if (chmod(path, (mode_t)xattr) < 0) {
          goto out;
        }
      }
#endif
    }

    if (on_extract) {
      if (on_extract(path, arg) < 0) {

```
### Line 935-946
```
    }
  }
  status = 0;

out:
  // Close the archive, freeing any resources it was using
  if (!mz_zip_reader_end(&zip_archive)) {
    // Cannot end zip reader
    status = -1;
  }

  return status;

```

## _vlib_compiler_tests_bench_val_vs_ptr_c
### Line 1-20
```

```

## _thirdparty_vschannel_vschannel_c
### Line 1-26
```

```
### Line 37-69
```

```
### Line 75-84
```

```
### Line 98-124
```

```
### Line 125-160
```

```
### Line 173-183
```

```
### Line 185-197
```

```
### Line 214-232
```

```
### Line 242-251
```

```
### Line 291-322
```

```
### Line 335-344
```

```
### Line 354-363
```

```
### Line 383-392
```

```
### Line 393-412
```

```
### Line 426-437
```

```
### Line 458-467
```

```
### Line 469-478
```

```
### Line 501-512
```

```
### Line 516-535
```

```
### Line 551-563
```

```
### Line 568-579
```

```
### Line 580-597
```

```
### Line 606-633
```

```
### Line 642-692
```

```
### Line 697-706
```

```
### Line 727-768
```

```
### Line 785-815
```

```
### Line 821-830
```

```
### Line 837-852
```

```
### Line 856-880
```

```
### Line 882-895
```

```
### Line 897-912
```

```
### Line 943-952
```

```
### Line 957-966
```

```
### Line 1010-1026
```

```
### Line 1030-1039
```

```
### Line 1042-1054
```

```
### Line 1065-1094
```

```

## _thirdparty_glad_glad_c
### Line 16-67
```

```
### Line 70-112
```

```
### Line 117-143
```

```
### Line 153-164
```

```
### Line 165-178
```

```
### Line 194-203
```

```
### Line 210-221
```

```
### Line 234-243
```

```
### Line 246-255
```

```
### Line 1664-1677
```

```

# Issues
## 2465
Title:
```

        error : ft2build.h 
      
```
Author:
```
hunylee
```
Text:
```

V version:
** V 0.1.21 dfc654f
OS:
** mac os
What did you do?
** v/examples/tetris/tetris.tmp.c:167:10: fatal error: 'ft2build.h' file not found
What did you expect to see?
** I won't  ft2build.h'
What did you see instead?
** ft2build.h is add

```
Author:
```
medvednikov
```
Text:
```

it's mentioned in the readme: brew install freetype

```

## 158
Title:
```

        It's probably a bug.
      
```
Author:
```
xywf221
```
Text:
```

I'm trying to run the following code
fn main() {
        str := '123'
	println()
}

output : test.v:3. Unexpected token: ') ',I think he should have given me the error. The function parameter is empty

```
Author:
```
ntrel
```
Text:
```

That is the error ;-)
I think it's planned for println to accept multiple arguments. If so probably no arguments could be supported too. (So this would hopefully be a new language feature: variadic function arguments. And println would be a standard library function).

```
Author:
```
ntrel
```
Text:
```

But yes, it would be better for V to print the function signature when the argument types or argument count do not match the function parameter(s).

```
Author:
```
medvednikov
```
Text:
```

Fixed:
not enough arguments in call to `println` 


```
Author:
```
medvednikov
```
Text:
```


So this would hopefully be a new language feature: variadic function arguments

Yes, varargs will be supported.

```

## 1451
Title:
```

        Line number of compile error missing
      
```
Author:
```
l8atnight
```
Text:
```

V version: lastest
OS: win64
What did you do?
compile with error
What did you expect to see?
line number of error
What did you see instead?
F:\v\mylib>..\v test.v
unexpected token: ]

```
Author:
```
joe-conigliaro
```
Text:
```

This will be updated so line number is always shown

```
Author:
```
medvednikov
```
Text:
```

Please paste the code that results in this.
I get
k.v:3 panic: unexpected token: `}`


```
Author:
```
l8atnight
```
Text:
```

fn main() {

   mut matrix := [0.0,0.0][0.5,0.5]
   matrix[0] = 0.5
   matrix[40] = 0.5   //F:\v\mylib>test
                               //  V panic: array index out of range: 40 / 2
                              //without the below line!

  matrix[0][0] = 0.5  //F:\v\mylib>..\v test.v
                               //Cant [] non-array/string/map. Got type "f32"
                               //no line number!!

	println(matrix[40])
}


```
Author:
```
medvednikov
```
Text:
```

Strange, I just tested on macOS and Windows, and I get error lines.
You need [[0.0,0.0], [0.5,0.5]], and [0][0] syntax doesn't work yet.

```
Author:
```
l8atnight
```
Text:
```

I thought so too. I update always with:
git pull origin master
make
could that be a reason?

```
Author:
```
joe-conigliaro
```
Text:
```

yes can you also try:
git pull origin master
make
v -o v1 compiler
mv v1 v

```
Author:
```
l8atnight
```
Text:
```

@joe-conigliaro  i did that
F:\v\mylib>..\v1 test.v
pass=2 fn=main
test.v:10 panic: Cant [] non-array/string/map. Got type "f32"
and it works.

```

## 253
Title:
```

        V compiles in 0.6s?
      
```
Author:
```
mr-del
```
Text:
```

How could V compiles in 0.6s if the code generate an error syntax? Was it 0.6s because of an error?
https://vlang.io/compilation_speed



v/website/compilation_speed_test_gen.v


         Line 69
      in
      e2a19cc






 fn gen_v() { 





test.v:2
unexpected token: ;
fn main() { mut a := 0 
a = 0; println(a);
a = 1; println(a);
a = 2; println(a);
a = 3; println(a);
.
.
.
}


```
Author:
```
MaxUNof
```
Text:
```

Vlang doesn't support ;
Correct gen_v():
fn gen_v() {
	println('fn main() { mut a := 0 ')
	for i := 0; i < N * 1000; i++ {
		println('a = $i\nprintln(a)')
	}
	println('}')
}

Fix it and check time of compilation ;-)

```
Author:
```
mr-del
```
Text:
```

I knew removing the semicolon fix it. The concern is how long does it took to compile in 200K println (not the time to generate 200K of V code) and what is your machine specification?

```
Author:
```
medvednikov
```
Text:
```

As discussed here the test is not very good and useful: #126
I'll update it as soon as the language is open-sourced.

```

## 136
Title:
```

        bug of stack size check
      
```
Author:
```
bronze1man
```
Text:
```

Put follow code into https://vlang.io/play
fn fib(n int) int {
	if n <= 1 {
		return 1
	}
	return fib(n - 1) * 3 + 1
}

fn main() {
	println(fib(1000000))
}

Then I got nothing.
But When I change the 1000000 to 100000, it will output some overflowed int result.
Follow code will get time out error like Your program was running for too long (> 1 sec):
fn main() {
	for i := 0; i < 1000000000; i++ {
	}
	println(1)
}

I think there may be process crash or other bad stuff happened. The playground just can not handle it.

```

## 1169
Title:
```

        V 0.1.15 with *BSD support, hot code reloading, fixed VROOT, defer statement, and more!
      
```
Author:
```
medvednikov
```
Text:
```

V 0.1.15
15 Jul 2019

FreeBSD, OpenBSD, NetBSD, DragonFly support.
Hot code reloading now works with graphical applications:  bounce.v
VROOT was removed, the installation process is now much simpler.
defer statement.
map.v was re-written. It's now much faster.
for key, val in map syntax.
flag module for parsing command line arguments.
zip module.
crypto/sha1 module.
Submodules and module aliases (import encoding.base64 as b64).


```
Author:
```
changrui
```
Text:
```

Panic：  os_win.v:5， redefination of os.PathSeparator, please fix it.

```
Author:
```
medvednikov
```
Text:
```

@changrui make sure you run git pull and make

```
Author:
```
lhmwzy
```
Text:
```

git pull;make
rm -f v.c v vprod
curl -Os https://raw.githubusercontent.com/vlang/vc/master/v.c
cc -std=gnu11 -w -o v v.c -lm
./v -o v compiler
*** Signal 11
Stop.
make: stopped in /home/lhm/v
./v examples/hello_world.v
fish: './v examples/hello_world.v' terminated by signal SIGSEGV (Address boundary error)
uname -a:
DragonFly gxdb 5.6-RELEASE DragonFly v5.6.0.1.g3d5034-RELEASE #0: Tue Jun 18 09:09:55 CST 2019

```
Author:
```
medvednikov
```
Text:
```

I tested on FreeBSD and OpenBSD only. I assumed it would just work.
I'll install DragonFly and test it there.

```
Author:
```
lhmwzy
```
Text:
```

the core file is here:
https://github.com/lhmwzy/v_error

```
Author:
```
kingofoz
```
Text:
```

Hi @medvednikov Did you fix #1004?

```
Author:
```
medvednikov
```
Text:
```

@lhmwzy can you try again please?

```
Author:
```
ernierasta
```
Text:
```

Hi Alex,
thank You for implementing sane (POSIG/GNU) flags! In golang I always have to use non standard library pflag library.

```
Author:
```
Chiiruno
```
Text:
```

Great work!
Do you plan on adding this release to the releases page on this repo?

```
Author:
```
medvednikov
```
Text:
```

@Chiiruno done
There are no pre-built binaries right now, they have to built from source. But it's very easy to do (git clone + make).

```
Author:
```
JohnAZoidberg
```
Text:
```

Could you please add the notes to the releases in the future?

```
Author:
```
elimisteve
```
Text:
```

@JohnAZoidberg Great idea; seconded 👍
EDIT: @medvednikov Then the release notes would appear at https://github.com/vlang/v/releases/tag/0.1.15

```
Author:
```
lhmwzy
```
Text:
```


@lhmwzy can you try again please?

OK now.thks @medvednikov

```
Author:
```
medvednikov
```
Text:
```


Then the release notes would appear at https://github.com/vlang/v/releases/tag/0.1.15

Ok, will do @elimisteve @JohnAZoidberg

```

## 2164
Title:
```

        Cannot compile empty filenames
      
```
Author:
```
radare
```
Text:
```

V version: V 0.1.20 e72fe25
OS: macOS 10.14
What did you do?
$ v .v
ld: can't open output file for writing: , errno=2 for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
V error: C error. This should never happen. Please create a GitHub issue: https://github.com/vlang/v/issues/new/choose

What did you expect to see?
Maybe an a.out or main? or a more meaningful error message
What did you see instead?

```
Author:
```
nsauzede
```
Text:
```

trying to compile some equivalently named ".c" file gives this :
$ cat .c
int main() {
	return 0;
}
$ gcc .c
/usr/bin/ld:.c: file format not recognized; treating as linker script
/usr/bin/ld:.c:1: syntax error
collect2: error: ld returned 1 exit status

So I would say that it should not be an issue if V also refuses such kind of bogus file name
But I agree that the error message could be more explicit (ie: V compiler forbidding empty file radix)

```
Author:
```
radare
```
Text:
```

Works perfectly fine with clang
$ cat .c
main() {}
$ clang .c
.c:1:1: warning: type specifier missing, defaults to 'int' [-Wimplicit-int]
main() {}
^
1 warning generated.
$


```

## 145
Title:
```

        bug of type check 5
      
```
Author:
```
bronze1man
```
Text:
```

may relative to #133
fn main() {
	test_hello()
	println(1)
}

// hello.v
fn hello() string {
	return 'Hello world'
}

// hello_test.v
fn test_hello() {
	assert hello() 
}

Then I got
You just found a bug. V can't compile this program, but it should. Please create a GitHub issue.


```
Author:
```
medvednikov
```
Text:
```

Fixed.
expected type `bool`, but got `string`


```

# Pull
## 1251
Title:
```

        vlib/os: fix memory leaks in write, exec and more
      
```
Author:
```
Rendims
```
Text:
```

This fixes some of the memory leaks in the os module but not all.
Calling functions with internal leakage in a loop as in issue #1004 can quickly exhaust all available memory.
''.clone() might look odd but it is to make sure the return string owns the allocated data. It's required so that a caller of exec can call free() on the return value without the risk of freeing a slice or something that wasn't allocated with malloc.
I tested this on Android and can't test it on windows so I skipped closing the process in exec on windows since I don't want to introduce errors.
The compiler can still compile itself and make test tests pass (some examples fail to build on Android).
Also ran the compiler with valgrind and got no errors except more leaks.

```
Author:
```
medvednikov
```
Text:
```

Thanks. All of these (except for .clone()) are going to be inserted by the compiler automatically.
I'm hoping to release this tomorrow.

```
Author:
```
medvednikov
```
Text:
```

All of these are now cleaned up by the compiler.

```

## 429
Title:
```

        Remove logging from mac's http fetches
      
```
Author:
```
kcorey
```
Text:
```


No description provided.


```

## 2236
Title:
```

        Grammar fix on readme.md file
      
```
Author:
```
ybaruchel
```
Text:
```

Grammar fix on readme.md file

```

## 1135
Title:
```

        Fix clang build for windows.
      
```
Author:
```
0x9ef
```
Text:
```

Fixed:
C:\Users\C182~1\AppData\Local\Temp\ccb5oFDP.o: In function `os__fork':
C:/Users/─рэ //.vlang//v2.exe.c:4831: undefined reference to `fork'
C:\Users\C182~1\AppData\Local\Temp\ccb5oFDP.o: In function `os__wait':
C:/Users/─рэ //.vlang//v2.exe.c:4840: undefined reference to `wait'
collect2.exe: error: ld returned 1 exit status


```

## 2346
Title:
```

        Add getters for complex numbers
      
```
Author:
```
shsr04
```
Text:
```

Added getters for re/im part of complex numbers. (Fixes #2344)
c := cmplx.complex(5,2)
re := c.real()
im := c.imag()

```
Author:
```
lppedd
```
Text:
```

Hi! Out of curiosity, can I ask why not just publishing the im and re fields?
I'd have simply renamed them to imag and real, just that it's still in 0.1.*.
I feel getters are mostly redundant.

```
Author:
```
avitkauskas
```
Text:
```

Yes, I also think we should just make the fields public, without changing their names. So just:
struct Complex {
pub:
	re f64
	im f64
}

```
Author:
```
medvednikov
```
Text:
```

Yes, V doesn't need getters because of the immutable struct fields.

```
Author:
```
lppedd
```
Text:
```

Morning everyone. @avitkauskas yes, you're right, since math uses Im and Re. My bad.

```

## 1916
Title:
```

        compiler: add vmft() to reduce complexity
      
```
Author:
```
vbrazo
```
Text:
```

Isolate responsibility to reduce complexity in the main method.
Similar PR: #1910

```
Author:
```
dumblob
```
Text:
```

This is IMHO unnecessary (I don't find it complex at all and second, the function is used just on one place).

```
Author:
```
dumblob
```
Text:
```

What is the new binary file examples/database/pg/customer good for?

```
Author:
```
vbrazo
```
Text:
```

I pushed examples/database/pg/customer by mistake.
Since this is unnecessary, we're closing this PR.

```
Author:
```
medvednikov
```
Text:
```

I think it's fine @vbrazo
You can bring it back, just call the function fn vfmt

```
Author:
```
vbrazo
```
Text:
```

@medvednikov done!

```

## 475
Title:
```

        update rand.v to produce more guaranteed random results
      
```
Author:
```
alyx
```
Text:
```

Per RFC 1194.5, the statically returned random number from vlang's rand.next() function should not be 0.
The standard, IEEE-vetted and approved random number is 4.

```
Author:
```
LouCle
```
Text:
```

I know you're joking, but just to make sure, the function actually produces a random number as the # specifier allows for the inclusion of C code. Thus the last return doesn't actually do anything.

```

## 2108
Title:
```

        compiler: small fixes with blank identifier
      
```
Author:
```
joe-conigliaro
```
Text:
```

compiler: small fixes with blank identifier

```

## 1572
Title:
```

        v install: fix installing a single module
      
```
Author:
```
spytheman
```
Text:
```

Fixes 'v install singlemodule', while avoiding changing the behavior of v, that always rebuilds vget (PR #1570).

```

## 2496
Title:
```

        tetris.v: minor User Interface improvements
      
```
Author:
```
Sag-Dev
```
Text:
```

I've improved the user interface of the tetris example. These are the changes I've done:

I've added a gray (almost white, but less saturated) background to make it less eye straining. This also allows to differentiate the play area from the rest of the window when the user resizes it.
I've added an upper bar that shows where the limit is, the player can see when he's going to lose clearer.
I've added a background color to the pause and gameover texts.

This image resumes all the changes:


```
Author:
```
medvednikov
```
Text:
```

Thoughts on the gray background?
I prefer white to be honest.

```
Author:
```
Sag-Dev
```
Text:
```

I thought an almost white gray would be less tiring for the eyes and still get the same feeling. But I see why you prefer white, it looks cleaner indeed. Its other purpose was to make the play area stand out from the rest of the window.
I think the best solution could be just in the middle. I can set the play area background to white and the rest of the window to gray. Would you like that better?

```

## 1499
Title:
```

        flag: allow to define flags with abbreviation
      
```
Author:
```
spacesinmotion
```
Text:
```

flag: allow to define flags with abbreviation
flags could be defined to use a single char as abbreviation like
'--output' or '-o'
'--help' or '-h'
the usage output is adapted as well

```

## 1477
Title:
```

        compiler: cleanup module, rename pkg to mod. auto save file import table after import parse
      
```
Author:
```
joe-conigliaro
```
Text:
```

file import tables automatically added to table.file_imports no need to manually add any more after parse

```

