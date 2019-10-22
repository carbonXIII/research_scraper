# vuejs/vue
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_github_CONTRIBUTING_md](#_github_CONTRIBUTING_md)

* [_github_CODE_OF_CONDUCT_md](#_github_CODE_OF_CONDUCT_md)

* [_examples_todomvc_readme_md](#_examples_todomvc_readme_md)

* [_benchmarks_ssr_README_md](#_benchmarks_ssr_README_md)

* [_packages_vue_template_compiler_README_md](#_packages_vue_template_compiler_README_md)

* [_dist_README_md](#_dist_README_md)

* [_packages_vue_server_renderer_README_md](#_packages_vue_server_renderer_README_md)

* [_github_ISSUE_TEMPLATE_md](#_github_ISSUE_TEMPLATE_md)

* [_packages_weex_vue_framework_README_md](#_packages_weex_vue_framework_README_md)

* [_README_md](#_README_md)

* [_github_PULL_REQUEST_TEMPLATE_md](#_github_PULL_REQUEST_TEMPLATE_md)

* [_packages_weex_template_compiler_README_md](#_packages_weex_template_compiler_README_md)

* [_BACKERS_md](#_BACKERS_md)

* [_github_COMMIT_CONVENTION_md](#_github_COMMIT_CONVENTION_md)

[- Inline](#Inline)

* [_test_weex_runtime_style_spec_js](#_test_weex_runtime_style_spec_js)

* [_test_e2e_specs_svg_js](#_test_e2e_specs_svg_js)

* [_src_platforms_weex_runtime_components_index_js](#_src_platforms_weex_runtime_components_index_js)

* [_src_core_vdom_modules_ref_js](#_src_core_vdom_modules_ref_js)

* [_src_core_util_env_js](#_src_core_util_env_js)

* [_src_core_instance_render_helpers_resolve_slots_js](#_src_core_instance_render_helpers_resolve_slots_js)

* [_src_core_components_keep_alive_js](#_src_core_components_keep_alive_js)

* [_dist_vue_esm_browser_js](#_dist_vue_esm_browser_js)

* [_test_unit_modules_compiler_compiler_options_spec_js](#_test_unit_modules_compiler_compiler_options_spec_js)

* [_test_ssr_fixtures_async_bar_js](#_test_ssr_fixtures_async_bar_js)

* [_babelrc_js](#_babelrc_js)

* [_src_core_global_api_extend_js](#_src_core_global_api_extend_js)

* [_src_core_vdom_helpers_is_async_placeholder_js](#_src_core_vdom_helpers_is_async_placeholder_js)

* [_test_unit_modules_observer_scheduler_spec_js](#_test_unit_modules_observer_scheduler_spec_js)

* [_test_unit_features_filter_filter_spec_js](#_test_unit_features_filter_filter_spec_js)

* [_src_compiler_to_function_js](#_src_compiler_to_function_js)

* [_src_core_util_perf_js](#_src_core_util_perf_js)

* [_src_core_instance_render_helpers_check_keycodes_js](#_src_core_instance_render_helpers_check_keycodes_js)

* [_packages_vue_template_compiler_browser_js](#_packages_vue_template_compiler_browser_js)

* [_packages_vue_server_renderer_build_prod_js](#_packages_vue_server_renderer_build_prod_js)

[- Issues](#Issues)

* [9401](#9401)

* [5156](#5156)

* [10330](#10330)

* [8869](#8869)

* [8505](#8505)

* [9862](#9862)

* [4894](#4894)

* [9865](#9865)

* [4810](#4810)

* [7030](#7030)

* [2635](#2635)

* [2836](#2836)

* [4277](#4277)

* [1048](#1048)

* [3210](#3210)

* [10132](#10132)

* [9737](#9737)

* [3226](#3226)

* [1655](#1655)

* [9840](#9840)

[- Pull](#Pull)

<!-- toc -->

# Info
## description
🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web.

# Markdown
## _github_CONTRIBUTING_md
```# Vue.js Contributing Guide

Hi! I'm really excited that you are interested in contributing to Vue.js. Before submitting your contribution, please make sure to take a moment and read through the following guidelines:

- [Code of Conduct](https://github.com/vuejs/vue/blob/dev/.github/CODE_OF_CONDUCT.md)
- [Issue Reporting Guidelines](#issue-reporting-guidelines)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)

## Issue Reporting Guidelines

- Always use [https://new-issue.vuejs.org/](https://new-issue.vuejs.org/) to create new issues.

## Pull Request Guidelines

- The `master` branch is just a snapshot of the latest stable release. All development should be done in dedicated branches. **Do not submit PRs against the `master` branch.**

- Checkout a topic branch from the relevant branch, e.g. `dev`, and merge back against that branch.

- Work in the `src` folder and **DO NOT** checkin `dist` in the commits.

- It's OK to have multiple small commits as you work on the PR - GitHub will automatically squash it before merging.

- Make sure `npm test` passes. (see [development setup](#development-setup))

- If adding a new feature:
  - Add accompanying test case.
  - Provide a convincing reason to add this feature. Ideally, you should open a suggestion issue first and have it approved before working on it.

- If fixing bug:
  - If you are resolving a special issue, add `(fix #xxxx[,#xxxx])` (#xxxx is the issue id) in your PR title for a better release log, e.g. `update entities encoding/decoding (fix #3899)`.
  - Provide a detailed description of the bug in the PR. Live demo preferred.
  - Add appropriate test coverage if applicable.

## Development Setup

You will need [Node.js](http://nodejs.org) **version 8+**, [Java Runtime Environment](http://www.oracle.com/technetwork/java/javase/downloads/index.html) (for running Selenium server during e2e tests) and [yarn](https://yarnpkg.com/en/docs/install).

After cloning the repo, run:

''' bash
$ yarn # install the dependencies of the project
'''

### Committing Changes

Commit messages should follow the [commit message convention](./COMMIT_CONVENTION.md) so that changelogs can be automatically generated. Commit messages will be automatically validated upon commit. If you are not familiar with the commit message convention, you can use `npm run commit` instead of `git commit`, which provides an interactive CLI for generating proper commit messages.

### Commonly used NPM scripts

''' bash
# watch and auto re-build dist/vue.js
$ npm run dev

# watch and auto re-run unit tests in Chrome
$ npm run dev:test

# build all dist files, including npm packages
$ npm run build

# run the full test suite, including linting/type checking
$ npm test
'''

There are some other scripts available in the `scripts` section of the `package.json` file.

The default test script will do the following: lint with ESLint -> type check with Flow -> unit tests with coverage -> e2e tests. **Please make sure to have this pass successfully before submitting a PR.** Although the same tests will be run against your PR on the CI server, it is better to have it working locally.

## Project Structure

- **`scripts`**: contains build-related scripts and configuration files. Usually, you don't need to touch them. However, it would be helpful to familiarize yourself with the following files:

  - `scripts/alias.js`: module import aliases used across all source code and tests.

  - `scripts/config.js`: contains the build configurations for all files found in `dist/`. Check this file if you want to find out the entry source file for a dist file.

- **`dist`**: contains built files for distribution. Note this directory is only updated when a release happens; they do not reflect the latest changes in development branches.

  See [dist/README.md](https://github.com/vuejs/vue/blob/dev/dist/README.md) for more details on dist files.

- **`flow`**: contains type declarations for [Flow](https://flowtype.org/). These declarations are loaded **globally** and you will see them used in type annotations in normal source code.

- **`packages`**: contains `vue-server-renderer` and `vue-template-compiler`, which are distributed as separate NPM packages. They are automatically generated from the source code and always have the same version with the main `vue` package.

- **`test`**: contains all tests. The unit tests are written with [Jasmine](http://jasmine.github.io/2.3/introduction.html) and run with [Karma](http://karma-runner.github.io/0.13/index.html). The e2e tests are written for and run with [Nightwatch.js](http://nightwatchjs.org/).

- **`src`**: contains the source code. The codebase is written in ES2015 with [Flow](https://flowtype.org/) type annotations.

  - **`compiler`**: contains code for the template-to-render-function compiler.

    The compiler consists of a parser (converts template strings to element ASTs), an optimizer (detects static trees for vdom render optimization), and a code generator (generate render function code from element ASTs). Note that codegen directly generates code strings from the element AST - it's done this way for smaller code size because the compiler is shipped to the browser in the standalone build.

  - **`core`**: contains universal, platform-agnostic runtime code.

    The Vue 2.0 core is platform-agnostic. That is, the code inside `core` is able to be run in any JavaScript environment, be it the browser, Node.js, or an embedded JavaScript runtime in native applications.

    - **`observer`**: contains code related to the reactivity system.

    - **`vdom`**: contains code related to vdom element creation and patching.

    - **`instance`**: contains Vue instance constructor and prototype methods.

    - **`global-api`**: contains Vue global api.

    - **`components`**: contains universal abstract components.

  - **`server`**: contains code related to server-side rendering.

  - **`platforms`**: contains platform-specific code.

    Entry files for dist builds are located in their respective platform directory.

    Each platform module contains three parts: `compiler`, `runtime` and `server`, corresponding to the three directories above. Each part contains platform-specific modules/utilities which are imported and injected to the core counterparts in platform-specific entry files. For example, the code implementing the logic behind `v-bind:class` is in `platforms/web/runtime/modules/class.js` - which is imported in `entries/web-runtime.js` and used to create the browser-specific vdom patching function.

  - **`sfc`**: contains single-file component (`*.vue` files) parsing logic. This is used in the `vue-template-compiler` package.

  - **`shared`**: contains utilities shared across the entire codebase.

  - **`types`**: contains TypeScript type definitions

    - **`test`**: contains type definitions tests


## Financial Contribution

As a pure community-driven project without major corporate backing, we also welcome financial contributions via Patreon and OpenCollective.

- [Become a backer or sponsor on Patreon](https://www.patreon.com/evanyou)
- [Become a backer or sponsor on OpenCollective](https://opencollective.com/vuejs)

### What's the difference between Patreon and OpenCollective funding?

Funds donated via Patreon go directly to support Evan You's full-time work on Vue.js. Funds donated via OpenCollective are managed with transparent expenses and will be used for compensating work and expenses for core team members or sponsoring community events. Your name/logo will receive proper recognition and exposure by donating on either platform.

## Credits

Thank you to all the people who have already contributed to Vue.js!

<a href="https://github.com/vuejs/vue/graphs/contributors"><img src="https://opencollective.com/vuejs/contributors.svg?width=890" /></a>
```
## _github_CODE_OF_CONDUCT_md
```# Contributor Code of Conduct

As contributors and maintainers of this project, we pledge to respect all people who contribute through reporting issues, posting feature requests, updating documentation, submitting pull requests or patches, and other activities.

We are committed to making participation in this project a harassment-free experience for everyone, regardless of the level of experience, gender, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, age, or religion.

Examples of unacceptable behavior by participants include the use of sexual language or imagery, derogatory comments or personal attacks, trolling, public or private harassment, insults, or other unprofessional conduct.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct. Project maintainers who do not follow the Code of Conduct may be removed from the project team.

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by opening an issue or contacting one or more of the project maintainers.

This Code of Conduct is adapted from the [Contributor Covenant](http://contributor-covenant.org), version 1.0.0, available at [http://contributor-covenant.org/version/1/0/0/](http://contributor-covenant.org/version/1/0/0/)
```
## _examples_todomvc_readme_md
```# Vue.js TodoMVC Example

> Vue.js is a library for building interactive web interfaces. 
It provides data-driven, nestable view components with a simple and flexible API.

> _[Vue.js - vuejs.org](https://vuejs.org)_

## Learning Vue.js
The [Vue.js website](https://vuejs.org/) is a great resource to get started.

Here are some links you may find helpful:

* [Official Guide](https://vuejs.org/guide/)
* [API Reference](https://vuejs.org/api/)
* [Examples](https://vuejs.org/examples/)

Get help from other Vue.js users:

* [Vue.js official forum](http://forum.vuejs.org)
* [Vue.js on Twitter](https://twitter.com/vuejs)
* [Vue.js on Gitter](https://gitter.im/vuejs/vue)

_If you have other helpful links to share, or find any of the links above no longer work, please [let us know](https://github.com/tastejs/todomvc/issues)._

## Credit

This TodoMVC application was created by [Evan You](http://evanyou.me).
```
## _benchmarks_ssr_README_md
```# Vue.js SSR benchmark

This benchmark renders a table of 1000 rows with 10 columns (10k components), with around 30k normal elements on the page. Note this is not something likely to be seen in a typical app. This benchmark is mostly for stress/regression testing and comparing between `renderToString` and `renderToStream`.

To view the results follow the run section. Note that the overall completion time for the results is variable, this is due to other system related variants at run time (available memory, processing power, etc). In ideal circumstances, both should finish within similar results.

`renderToStream` pipes the content through a stream which provides considerable performance benefits (faster time-to-first-byte and non-event-loop-blocking) over `renderToString`. This can be observed through the benchmark.

### run

''' bash
npm run bench:ssr
'''
```
## _packages_vue_template_compiler_README_md
```# vue-template-compiler

> This package is auto-generated. For pull requests please see [src/platforms/web/entry-compiler.js](https://github.com/vuejs/vue/tree/dev/src/platforms/web/entry-compiler.js).

This package can be used to pre-compile Vue 2.0 templates into render functions to avoid runtime-compilation overhead and CSP restrictions. In most cases you should be using it with [`vue-loader`](https://github.com/vuejs/vue-loader), you will only need it separately if you are writing build tools with very specific needs.

## Installation

''' bash
npm install vue-template-compiler
'''

''' js
const compiler = require('vue-template-compiler')
'''

## API

### compiler.compile(template, [options])

Compiles a template string and returns compiled JavaScript code. The returned result is an object of the following format:

''' js
{
  ast: ?ASTElement, // parsed template elements to AST
  render: string, // main render function code
  staticRenderFns: Array<string>, // render code for static sub trees, if any
  errors: Array<string> // template syntax errors, if any
}
'''

Note the returned function code uses `with` and thus cannot be used in strict mode code.

#### Options

- `outputSourceRange` *new in 2.6*
  - Type: `boolean`
  - Default: `false`

  Set this to true will cause the `errors` returned in the compiled result become objects in the form of `{ msg, start, end }`. The `start` and `end` properties are numbers that mark the code range of the error source in the template. This can be passed on to the `compiler.generateCodeFrame` API to generate a code frame for the error.

- `whitespace`
  - Type: `string`
  - Valid values: `'preserve' | 'condense'`
  - Default: `'preserve'`

  The default value `'preserve'` handles whitespaces as follows:

  - A whitespace-only text node between element tags is condensed into a single space.
  - All other whitespaces are preserved as-is.

  If set to `'condense'`:

  - A whitespace-only text node between element tags is removed if it contains new lines. Otherwise, it is condensed into a single space.
  - Consecutive whitespaces inside a non-whitespace-only text node are condensed into a single space.

  Using condense mode will result in smaller compiled code size and slightly improved performance. However, it will produce minor visual layout differences compared to plain HTML in certain cases.

  **This option does not affect the `<pre>` tag.**

  Example:

  ''' html
  <!-- source -->
  <div>
    <span>
      foo
    </span>   <span>bar</span>
  </div>

  <!-- whitespace: 'preserve' -->
  <div> <span>
    foo
    </span> <span>bar</span> </div>

  <!-- whitespace: 'condense' -->
  <div><span> foo </span> <span>bar</span></div>
  '''

- `modules`

  It's possible to hook into the compilation process to support custom template features. **However, beware that by injecting custom compile-time modules, your templates will not work with other build tools built on standard built-in modules, e.g `vue-loader` and `vueify`.**

  An array of compiler modules. For details on compiler modules, refer to the `ModuleOptions` type in [flow declarations](https://github.com/vuejs/vue/blob/dev/flow/compiler.js#L47-L59) and the [built-in modules](https://github.com/vuejs/vue/tree/dev/src/platforms/web/compiler/modules).

- `directives`

  An object where the key is the directive name and the value is a function that transforms an template AST node. For example:

  ''' js
  compiler.compile('<div v-test></div>', {
    directives: {
      test (node, directiveMeta) {
        // transform node based on directiveMeta
      }
    }
  })
  '''

  By default, a compile-time directive will extract the directive and the directive will not be present at runtime. If you want the directive to also be handled by a runtime definition, return `true` in the transform function.

  Refer to the implementation of some [built-in compile-time directives](https://github.com/vuejs/vue/tree/dev/src/platforms/web/compiler/directives).

- `preserveWhitespace` **Deprecated since 2.6**
  - Type: `boolean`
  - Default: `true`

  By default, the compiled render function preserves all whitespace characters between HTML tags. If set to `false`, whitespace between tags will be ignored. This can result in slightly better performance but may affect layout for inline elements.

---

### compiler.compileToFunctions(template)

Similar to `compiler.compile`, but directly returns instantiated functions:

''' js
{
  render: Function,
  staticRenderFns: Array<Function>
}
'''

This is only useful at runtime with pre-configured builds, so it doesn't accept any compile-time options. In addition, this method uses `new Function()` so it is not CSP-compliant.

---

### compiler.ssrCompile(template, [options])

> 2.4.0+

Same as `compiler.compile` but generates SSR-specific render function code by optimizing parts of the template into string concatenation in order to improve SSR performance.

This is used by default in `vue-loader@>=12` and can be disabled using the [`optimizeSSR`](https://vue-loader.vuejs.org/en/options.html#optimizessr) option.

---

### compiler.ssrCompileToFunctions(template)

> 2.4.0+

Same as `compiler.compileToFunction` but generates SSR-specific render function code by optimizing parts of the template into string concatenation in order to improve SSR performance.

---

### compiler.parseComponent(file, [options])

Parse a SFC (single-file component, or `*.vue` file) into a descriptor (refer to the `SFCDescriptor` type in [flow declarations](https://github.com/vuejs/vue/blob/dev/flow/compiler.js)). This is used in SFC build tools like `vue-loader` and `vueify`.

---

### compiler.generateCodeFrame(template, start, end)

Generate a code frame that highlights the part in `template` defined by `start` and `end`. Useful for error reporting in higher-level tooling.

#### Options

#### `pad`

`pad` is useful when you are piping the extracted content into other pre-processors, as you will get correct line numbers or character indices if there are any syntax errors.

- with `{ pad: "line" }`, the extracted content for each block will be prefixed with one newline for each line in the leading content from the original file to ensure that the line numbers align with the original file.
- with `{ pad: "space" }`, the extracted content for each block will be prefixed with one space for each character in the leading content from the original file to ensure that the character count remains the same as the original file.
```
## _dist_README_md
```## Explanation of Build Files

| | UMD | CommonJS | ES Module |
| --- | --- | --- | --- |
| **Full** | vue.js | vue.common.js | vue.esm.js |
| **Runtime-only** | vue.runtime.js | vue.runtime.common.js | vue.runtime.esm.js |
| **Full (production)** | vue.min.js | | |
| **Runtime-only (production)** | vue.runtime.min.js | | |

### Terms

- **Full**: builds that contains both the compiler and the runtime.

- **Compiler**: code that is responsible for compiling template strings into JavaScript render functions.

- **Runtime**: code that is responsible for creating Vue instances, rendering and patching virtual DOM, etc. Basically everything minus the compiler.

- **[UMD](https://github.com/umdjs/umd)**: UMD builds can be used directly in the browser via a `<script>` tag. The default file from Unpkg CDN at [https://unpkg.com/vue](https://unpkg.com/vue) is the Runtime + Compiler UMD build (`vue.js`).

- **[CommonJS](http://wiki.commonjs.org/wiki/Modules/1.1)**: CommonJS builds are intended for use with older bundlers like [browserify](http://browserify.org/) or [webpack 1](https://webpack.github.io). The default file for these bundlers (`pkg.main`) is the Runtime only CommonJS build (`vue.runtime.common.js`).

- **[ES Module](http://exploringjs.com/es6/ch_modules.html)**: ES module builds are intended for use with modern bundlers like [webpack 2](https://webpack.js.org) or [rollup](http://rollupjs.org/). The default file for these bundlers (`pkg.module`) is the Runtime only ES Module build (`vue.runtime.esm.js`).

### Runtime + Compiler vs. Runtime-only

If you need to compile templates on the fly (e.g. passing a string to the `template` option, or mounting to an element using its in-DOM HTML as the template), you will need the compiler and thus the full build.

When using `vue-loader` or `vueify`, templates inside `*.vue` files are compiled into JavaScript at build time. You don't really need the compiler in the final bundle, and can therefore, use the runtime-only build.

Since the runtime-only builds are roughly 30% lighter-weight than their full-build counterparts, you should use it whenever you can. If you wish to use the full build instead, you need to configure an alias in your bundler.

#### Webpack

''' js
module.exports = {
  // ...
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js' // 'vue/dist/vue.common.js' for webpack 1
    }
  }
}
'''

#### Rollup

''' js
const alias = require('rollup-plugin-alias')

rollup({
  // ...
  plugins: [
    alias({
      'vue': 'vue/dist/vue.esm.js'
    })
  ]
})
'''

#### Browserify

Add to your project's `package.json`:

''' js
{
  // ...
  "browser": {
    "vue": "vue/dist/vue.common.js"
  }
}
'''

### Development vs. Production Mode

Development/production modes are hard-coded for the UMD builds: the un-minified files are for development, and the minified files are for production.

CommonJS and ES Module builds are intended for bundlers, therefore we don't provide minified versions for them. You will be responsible for minifying the final bundle yourself.

CommonJS and ES Module builds also preserve raw checks for `process.env.NODE_ENV` to determine the mode they should run in. You should use appropriate bundler configurations to replace these environment variables in order to control which mode Vue will run in. Replacing `process.env.NODE_ENV` with string literals also allows minifiers like UglifyJS to completely drop the development-only code blocks, reducing final file size.

#### Webpack

Use Webpack's [DefinePlugin](https://webpack.js.org/plugins/define-plugin/):

''' js
var webpack = require('webpack')

module.exports = {
  // ...
  plugins: [
    // ...
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('production')
      }
    })
  ]
}
'''

#### Rollup

Use [rollup-plugin-replace](https://github.com/rollup/rollup-plugin-replace):

''' js
const replace = require('rollup-plugin-replace')

rollup({
  // ...
  plugins: [
    replace({
      'process.env.NODE_ENV': JSON.stringify('production')
    })
  ]
}).then(...)
'''

#### Browserify

Apply a global [envify](https://github.com/hughsk/envify) transform to your bundle.

''' bash
NODE_ENV=production browserify -g envify -e main.js | uglifyjs -c -m > build.js
'''
```
## _packages_vue_server_renderer_README_md
```# vue-server-renderer

> This package is auto-generated. For pull requests please see [src/platforms/web/entry-server-renderer.js](https://github.com/vuejs/vue/blob/dev/src/platforms/web/entry-server-renderer.js).

This package offers Node.js server-side rendering for Vue 2.0.

- [API Reference](https://ssr.vuejs.org/en/api.html)
- [Vue.js Server-Side Rendering Guide](https://ssr.vuejs.org)
```
## _github_ISSUE_TEMPLATE_md
```<!--
IMPORTANT: Please use the following link to create a new issue:

  https://new-issue.vuejs.org/

If your issue was not created using the app above, it will be closed immediately.

中文用户请注意：
请使用上面的链接来创建新的 issue。如果不是用上述工具创建的 issue 会被自动关闭。
-->

<!--
Love vuejs? Please consider supporting us via Patreon or OpenCollective:
👉  https://www.patreon.com/evanyou
👉  https://opencollective.com/vuejs/donate
-->
```
## _packages_weex_vue_framework_README_md
```# weex-vue-framework

> This package is auto-generated. For pull requests please see [src/platforms/weex/entry-framework.js](https://github.com/vuejs/vue/blob/dev/src/platforms/weex/entry-framework.js).
```
## _README_md
```<p align="center"><a href="https://vuejs.org" target="_blank" rel="noopener noreferrer"><img width="100" src="https://vuejs.org/images/logo.png" alt="Vue logo"></a></p>

<p align="center">
  <a href="https://circleci.com/gh/vuejs/vue/tree/dev"><img src="https://img.shields.io/circleci/project/github/vuejs/vue/dev.svg" alt="Build Status"></a>
  <a href="https://codecov.io/github/vuejs/vue?branch=dev"><img src="https://img.shields.io/codecov/c/github/vuejs/vue/dev.svg" alt="Coverage Status"></a>
  <a href="https://npmcharts.com/compare/vue?minimal=true"><img src="https://img.shields.io/npm/dm/vue.svg" alt="Downloads"></a>
  <a href="https://www.npmjs.com/package/vue"><img src="https://img.shields.io/npm/v/vue.svg" alt="Version"></a>
  <a href="https://www.npmjs.com/package/vue"><img src="https://img.shields.io/npm/l/vue.svg" alt="License"></a>
  <a href="https://chat.vuejs.org/"><img src="https://img.shields.io/badge/chat-on%20discord-7289da.svg" alt="Chat"></a>
  <br>
  <a href="https://app.saucelabs.com/builds/50f8372d79f743a3b25fb6ca4851ca4c"><img src="https://app.saucelabs.com/buildstatus/vuejs" alt="Build Status"></a>
</p>

<h2 align="center">Supporting Vue.js</h2>

Vue.js is an MIT-licensed open source project with its ongoing development made possible entirely by the support of these awesome [backers](https://github.com/vuejs/vue/blob/dev/BACKERS.md). If you'd like to join them, please consider:

- [Become a backer or sponsor on Patreon](https://www.patreon.com/evanyou).
- [Become a backer or sponsor on Open Collective](https://opencollective.com/vuejs).
- [One-time donation via PayPal or crypto-currencies.](https://vuejs.org/support-vuejs/#One-time-Donations)

#### What's the difference between Patreon and OpenCollective?

Funds donated via Patreon go directly to support Evan You's full-time work on Vue.js. Funds donated via OpenCollective are managed with transparent expenses and will be used for compensating work and expenses for core team members or sponsoring community events. Your name/logo will receive proper recognition and exposure by donating on either platform.

<h3 align="center">Special Sponsors</h3>
<!--special start-->

<p align="center">
  <a href="https://stdlib.com/" target="_blank">
    <img width="260px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/stdlib.png">
  </a>
</p>

<!--special end-->

<h3 align="center">Platinum Sponsors</h3>

<!--platinum start-->
<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://vueschool.io/?utm_source=Vuejs.org&utm_medium=Banner&utm_campaign=Sponsored%20Banner&utm_content=V1" target="_blank">
          <img width="222px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/vueschool.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://vehikl.com/" target="_blank">
          <img width="222px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/vehikl.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.nativescript.org/vue?utm_source=vue-js-org&utm_medium=website&utm_campaign=nativescript-awareness" target="_blank">
          <img width="222px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/nativescript.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://retool.com/?utm_source=sponsor&utm_campaign=vue" target="_blank">
          <img width="222px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/retool.png">
        </a>
      </td>
    </tr><tr></tr>
  </tbody>
</table>
<!--platinum end-->

<!--special-china start-->
<h3 align="center">Platinum Sponsors (China)</h3>
<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="http://www.dcloud.io/?hmsr=vuejsorg&hmpl=&hmcu=&hmkw=&hmci=" target="_blank">
          <img width="177px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/dcloud.gif">
        </a>
      </td>
    </tr><tr></tr>
  </tbody>
</table>
<!--special-china end-->

<h3 align="center">Gold Sponsors</h3>

<!--gold start-->
<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://www.vuemastery.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/vuemastery.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://laravel.com" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/laravel.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://chaitin.cn/en/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/chaitin.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://htmlburger.com" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/html_burger.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.frontenddeveloperlove.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/frontendlove.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://onsen.io/vue/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/onsen_ui.png">
        </a>
      </td>
    </tr><tr></tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://neds.com.au/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/neds.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://icons8.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/icons_8.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://vuejobs.com/?ref=vuejs" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/vuejobs.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://tidelift.com/subscription/npm/vue" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/tidelift.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://opteo.com/vue" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/opteo.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://devsquad.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/devsquad.png">
        </a>
      </td>
    </tr><tr></tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://www.firesticktricks.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/firestick_tricks.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://intygrate.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/intygrate.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://passionatepeople.io/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/passionate_people.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="http://en.shopware.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/shopware_ag.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.vpnranks.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/vpnranks.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.simplyswitch.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/energy_comparison.png">
        </a>
      </td>
    </tr><tr></tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://www.bacancytechnology.com" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/bacancy_technology.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.bestvpn.co/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/bestvpn_co.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://blokt.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/blokt_cryptocurrency_news.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.y8.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/y8.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://js.devexpress.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/devexpress.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://fastcoding.jp/javascript/ " target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/fastcoding_inc.svg">
        </a>
      </td>
    </tr><tr></tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://usave.co.uk/utilities/broadband" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/usave.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.dailynow.co/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/daily.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://storekit.com" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/storekit.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://staffaugmentation.ro/en" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/staff_augmentation.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://piratebay.ink" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/piratebay_proxy.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.programmers.io" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/programmers_io.png">
        </a>
      </td>
    </tr><tr></tr>
  </tbody>
</table>
<!--gold end-->

<h3 align="center">Sponsors via <a href="https://opencollective.com/vuejs">Open Collective</a></h3>

<h4 align="center">Platinum</h4>

<a href="https://opencollective.com/vuejs/tiers/platinum-sponsors/0/website" target="_blank" rel="noopener noreferrer"><img src="https://opencollective.com/vuejs/tiers/platinum-sponsors/0/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/platinum-sponsors/1/website" target="_blank" rel="noopener noreferrer"><img src="https://opencollective.com/vuejs/tiers/platinum-sponsors/1/avatar.svg"></a>

<h4 align="center">Gold</h4>

<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/0/website" target="_blank" rel="noopener noreferrer"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/0/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/1/website" target="_blank" rel="noopener noreferrer"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/1/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/2/website" target="_blank" rel="noopener noreferrer"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/2/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/3/website" target="_blank" rel="noopener noreferrer"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/3/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/4/website" target="_blank" rel="noopener noreferrer"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/4/avatar.svg" height="60px"></a>

---

## Introduction

Vue (pronounced `/vjuː/`, like view) is a **progressive framework** for building user interfaces. It is designed from the ground up to be incrementally adoptable, and can easily scale between a library and a framework depending on different use cases. It consists of an approachable core library that focuses on the view layer only, and an ecosystem of supporting libraries that helps you tackle complexity in large Single-Page Applications.

#### Browser Compatibility

Vue.js supports all browsers that are [ES5-compliant](http://kangax.github.io/compat-table/es5/) (IE8 and below are not supported).

## Ecosystem

| Project | Status | Description |
|---------|--------|-------------|
| [vue-router]          | [![vue-router-status]][vue-router-package] | Single-page application routing |
| [vuex]                | [![vuex-status]][vuex-package] | Large-scale state management |
| [vue-cli]             | [![vue-cli-status]][vue-cli-package] | Project scaffolding |
| [vue-loader]          | [![vue-loader-status]][vue-loader-package] | Single File Component (`*.vue` file) loader for webpack |
| [vue-server-renderer] | [![vue-server-renderer-status]][vue-server-renderer-package] | Server-side rendering support |
| [vue-class-component] | [![vue-class-component-status]][vue-class-component-package] | TypeScript decorator for a class-based API |
| [vue-rx]              | [![vue-rx-status]][vue-rx-package] | RxJS integration |
| [vue-devtools]        | [![vue-devtools-status]][vue-devtools-package] | Browser DevTools extension |

[vue-router]: https://github.com/vuejs/vue-router
[vuex]: https://github.com/vuejs/vuex
[vue-cli]: https://github.com/vuejs/vue-cli
[vue-loader]: https://github.com/vuejs/vue-loader
[vue-server-renderer]: https://github.com/vuejs/vue/tree/dev/packages/vue-server-renderer
[vue-class-component]: https://github.com/vuejs/vue-class-component
[vue-rx]: https://github.com/vuejs/vue-rx
[vue-devtools]:  https://github.com/vuejs/vue-devtools

[vue-router-status]: https://img.shields.io/npm/v/vue-router.svg
[vuex-status]: https://img.shields.io/npm/v/vuex.svg
[vue-cli-status]: https://img.shields.io/npm/v/@vue/cli.svg
[vue-loader-status]: https://img.shields.io/npm/v/vue-loader.svg
[vue-server-renderer-status]: https://img.shields.io/npm/v/vue-server-renderer.svg
[vue-class-component-status]: https://img.shields.io/npm/v/vue-class-component.svg
[vue-rx-status]: https://img.shields.io/npm/v/vue-rx.svg
[vue-devtools-status]: https://img.shields.io/chrome-web-store/v/nhdogjmejiglipccpnnnanhbledajbpd.svg

[vue-router-package]: https://npmjs.com/package/vue-router
[vuex-package]: https://npmjs.com/package/vuex
[vue-cli-package]: https://npmjs.com/package/@vue/cli
[vue-loader-package]: https://npmjs.com/package/vue-loader
[vue-server-renderer-package]: https://npmjs.com/package/vue-server-renderer
[vue-class-component-package]: https://npmjs.com/package/vue-class-component
[vue-rx-package]: https://npmjs.com/package/vue-rx
[vue-devtools-package]: https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd

## Documentation

To check out [live examples](https://vuejs.org/v2/examples/) and docs, visit [vuejs.org](https://vuejs.org).

## Questions

For questions and support please use [the official forum](http://forum.vuejs.org) or [community chat](https://chat.vuejs.org/). The issue list of this repo is **exclusively** for bug reports and feature requests.

## Issues

Please make sure to read the [Issue Reporting Checklist](https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md#issue-reporting-guidelines) before opening an issue. Issues not conforming to the guidelines may be closed immediately.

## Changelog

Detailed changes for each release are documented in the [release notes](https://github.com/vuejs/vue/releases).

## Stay In Touch

- [Twitter](https://twitter.com/vuejs)
- [Blog](https://medium.com/the-vue-point)
- [Job Board](https://vuejobs.com/?ref=vuejs)

## Contribution

Please make sure to read the [Contributing Guide](https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md) before making a pull request. If you have a Vue-related project/component/tool, add it with a pull request to [this curated list](https://github.com/vuejs/awesome-vue)!

Thank you to all the people who already contributed to Vue!

<a href="https://github.com/vuejs/vue/graphs/contributors"><img src="https://opencollective.com/vuejs/contributors.svg?width=890" /></a>


## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2013-present, Yuxi (Evan) You
```
## _github_PULL_REQUEST_TEMPLATE_md
```<!--
Please make sure to read the Pull Request Guidelines:
https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md#pull-request-guidelines
-->

<!-- PULL REQUEST TEMPLATE -->
<!-- (Update "[ ]" to "[x]" to check a box) -->

**What kind of change does this PR introduce?** (check at least one)

- [ ] Bugfix
- [ ] Feature
- [ ] Code style update
- [ ] Refactor
- [ ] Build-related changes
- [ ] Other, please describe:

**Does this PR introduce a breaking change?** (check one)

- [ ] Yes
- [ ] No

If yes, please describe the impact and migration path for existing applications:

**The PR fulfills these requirements:**

- [ ] It's submitted to the `dev` branch for v2.x (or to a previous version branch), _not_ the `master` branch
- [ ] When resolving a specific issue, it's referenced in the PR's title (e.g. `fix #xxx[,#xxx]`, where "xxx" is the issue number)
- [ ] All tests are passing: https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md#development-setup
- [ ] New/updated tests are included

If adding a **new feature**, the PR's description includes:
- [ ] A convincing reason for adding this feature (to avoid wasting your time, it's best to open a suggestion issue first and wait for approval before working on it)

**Other information:**
```
## _packages_weex_template_compiler_README_md
```# weex-template-compiler

> This package is auto-generated. For pull requests please see [src/platforms/weex/entry-compiler.js](https://github.com/vuejs/vue/tree/dev/src/platforms/weex/entry-compiler.js).
```
## _BACKERS_md
```<h1 align="center">Sponsors &amp; Backers</h1>

Vue.js is an MIT-licensed open source project. It's an independent project with its ongoing development made possible entirely thanks to the support by these awesome [backers](https://github.com/vuejs/vue/blob/dev/BACKERS.md). If you'd like to join them, please consider:

- [Become a backer or sponsor on Patreon](https://www.patreon.com/evanyou).
- [Become a backer or sponsor on OpenCollective](https://opencollective.com/vuejs).
- [One-time donation via PayPal or crypto-currencies.](https://vuejs.org/support-vuejs/#One-time-Donations)

#### What's the difference between Patreon and OpenCollective?

Funds donated via Patreon go directly to support Evan You's full-time work on Vue.js. Funds donated via OpenCollective are managed with transparent expenses and will be used for compensating work and expenses for core team members or sponsoring community events. Your name/logo will receive proper recognition and exposure by donating on either platform.

<br><br>

<h2 align="center">Special Sponsors</h2>

<!--special start-->

<p align="center">
  <a href="https://stdlib.com/" target="_blank">
    <img width="260px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/stdlib.png">
  </a>
</p>

<!--special end-->

<h2 align="center">Platinum via Patreon</h2>

<!--platinum start-->
<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://vueschool.io/?utm_source=Vuejs.org&utm_medium=Banner&utm_campaign=Sponsored%20Banner&utm_content=V1" target="_blank">
          <img width="222px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/vueschool.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://vehikl.com/" target="_blank">
          <img width="222px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/vehikl.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.nativescript.org/vue?utm_source=vue-js-org&utm_medium=website&utm_campaign=nativescript-awareness" target="_blank">
          <img width="222px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/nativescript.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://retool.com/?utm_source=sponsor&utm_campaign=vue" target="_blank">
          <img width="222px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/retool.png">
        </a>
      </td>
    </tr><tr></tr>
  </tbody>
</table>
<!--platinum end-->

<!--special-china start-->
<h3 align="center">Platinum Sponsors (China)</h3>
<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="http://www.dcloud.io/?hmsr=vuejsorg&hmpl=&hmcu=&hmkw=&hmci=" target="_blank">
          <img width="177px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/dcloud.gif">
        </a>
      </td>
    </tr><tr></tr>
  </tbody>
</table>
<!--special-china end-->

<h2 align="center">Platinum via OpenCollective</h2>

<a href="https://opencollective.com/vuejs/tiers/platinum-sponsors/0/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/platinum-sponsors/0/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/platinum-sponsors/1/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/platinum-sponsors/1/avatar.svg"></a>

<h2 align="center">Gold via Patreon</h2>

<!--gold start-->
<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://www.vuemastery.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/vuemastery.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://laravel.com" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/laravel.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://chaitin.cn/en/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/chaitin.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://htmlburger.com" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/html_burger.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.frontenddeveloperlove.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/frontendlove.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://onsen.io/vue/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/onsen_ui.png">
        </a>
      </td>
    </tr><tr></tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://neds.com.au/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/neds.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://icons8.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/icons_8.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://vuejobs.com/?ref=vuejs" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/vuejobs.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://tidelift.com/subscription/npm/vue" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/tidelift.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://opteo.com/vue" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/opteo.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://devsquad.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/devsquad.png">
        </a>
      </td>
    </tr><tr></tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://www.firesticktricks.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/firestick_tricks.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://intygrate.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/intygrate.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://passionatepeople.io/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/passionate_people.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="http://en.shopware.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/shopware_ag.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.vpnranks.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/vpnranks.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.simplyswitch.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/energy_comparison.png">
        </a>
      </td>
    </tr><tr></tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://www.bacancytechnology.com" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/bacancy_technology.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.bestvpn.co/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/bestvpn_co.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://blokt.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/blokt_cryptocurrency_news.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.y8.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/y8.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://js.devexpress.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/devexpress.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://fastcoding.jp/javascript/ " target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/fastcoding_inc.svg">
        </a>
      </td>
    </tr><tr></tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://usave.co.uk/utilities/broadband" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/usave.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.dailynow.co/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/daily.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://storekit.com" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/storekit.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://staffaugmentation.ro/en" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/staff_augmentation.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://piratebay.ink" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/piratebay_proxy.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.programmers.io" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/programmers_io.png">
        </a>
      </td>
    </tr><tr></tr>
  </tbody>
</table>
<!--gold end-->

<h2 align="center">Gold via OpenCollective</h2>

<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/0/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/0/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/1/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/1/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/2/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/2/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/3/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/3/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/4/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/4/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/5/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/5/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/6/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/6/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/7/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/7/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/8/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/8/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/9/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/9/avatar.svg" height="60px"></a>
<a href="https://opencollective.com/vuejs/tiers/gold-sponsors/10/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/gold-sponsors/10/avatar.svg" height="60px"></a>

<h2 align="center">Silver via Patreon</h2>

- Matt Mullenweg

<!--silver start-->
<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://dopamine.bg/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/dopamine.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://roadster.com" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/roadster.png">
        </a>
      </td>
    </tr><tr></tr>
  </tbody>
</table>
<!--silver end-->

<h4 align="center">Silver via OpenCollective</h4>

<a href="https://opencollective.com/vuejs/tiers/silver-sponsors/0/website" target="_blank" rel="noopener noreferrer"><img src="https://opencollective.com/vuejs/tiers/silver-sponsors/0/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/silver-sponsors/1/website" target="_blank" rel="noopener noreferrer"><img src="https://opencollective.com/vuejs/tiers/silver-sponsors/1/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/silver-sponsors/2/website" target="_blank" rel="noopener noreferrer"><img src="https://opencollective.com/vuejs/tiers/silver-sponsors/2/avatar.svg"></a>

<h2 align="center">Bronze via Patreon</h2>

<!--bronze start-->
<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://www.accelebrate.com/" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/accelebrate.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://polyglotengineer.com/derek.pollard" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/derek_pollard.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://www.earthlink.ro" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/earthlink.png">
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://twitter.com/philipjbasile" target="_blank">
          <img width="148px" src="https://raw.githubusercontent.com/vuejs/vuejs.org/master/themes/vue/source/images/philip_john_basile.gif">
        </a>
      </td>
    </tr><tr></tr>
  </tbody>
</table>
<!--bronze end-->

<h2 align="center">Bronze via OpenCollective</h2>

<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/0/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/0/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/1/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/1/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/2/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/2/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/3/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/3/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/4/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/4/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/5/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/5/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/6/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/6/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/7/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/7/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/8/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/8/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/9/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/9/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/10/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/10/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/11/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/11/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/12/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/12/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/13/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/13/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/14/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/14/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/15/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/15/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/16/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/16/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/17/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/17/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/18/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/18/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/19/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/19/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/20/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/20/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/21/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/21/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/22/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/22/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/23/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/23/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/24/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/24/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/25/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/25/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/26/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/26/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/27/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/27/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/28/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/28/avatar.svg"></a>
<a href="https://opencollective.com/vuejs/tiers/bronze-sponsors/29/website" target="_blank"><img src="https://opencollective.com/vuejs/tiers/bronze-sponsors/29/avatar.svg"></a>

<h2 align="center">Generous Backers via Patreon ($50+)</h2>

<!--50 start-->
- Wasim Khamlichi
- errorrik
- Alex Balashov
- Konstantin Levinski
- Blaise Laflamme
- Sean Ferguson
- Johnny Ray Austin
- Daniel
<!--50 end-->

<h2 align="center">Backers via Patreon</h2>

<!--10 start-->
- Masahiro Tanaka
- Shawn Wildermuth
- Sean Washington
- Benjamin Listwon
- Keisuke Kita
- Lars Andreas Ness
- Kirk Lewis
- Victor Tolbert
- Wen-Tien Chang
- Stephen Michael Hartley
- Phan An
- Luiz
- James J. Ye
- Barbara Liau
- Matsumoto Takamasa
- Matt Jones
- Niannian Modisette
- Duncan Kenzie
- Guy Gavergun
- Bernhard E. Reiter
- Zoran Knezevic
- Jon Hobbs-Smith
- Pierre Vanhulst
- Asaf Yishai
- Haim Yulzari
- Akiho Nagao
- Anthony Estebe
- Jim Raden
- Jeremy Tan
- IMGNRY
- Tyler
- Guilherme S L de Souza
- Mickaël Andrieu
- Vivekanandhan Natarajan
- Rob Yedlin
- Joe Gregory
- Jordan Oroshiba
- Marcos Moura
- Jessie Hernandez
- Eric
- Ivan Sieder
- Romain Lienard
- username
- Bohdan Kokotko
- Wakana Seki
- Alexander Weiher
- David Ang
- Donald Fischer
- Oskar Lindgren
- Jere Sjöroos
- Domenico Gaudioso
- Jaeyoung Lee
- David Kaplan
- Andy
- Matt Sencenbaugh
- Juan Bermudez
- Hannes Kochniß
- Elon Hung
- Daniel Mattingley
- Chris Calo
- Soichiro Isshiki
- Ed Linklater
- Garion Herman
- Andrew Willis
- Princeyesuraj Edward
- Yusuke Kawabata
- 龙腾道
- Nick Dandakis
- Peter Matkovsky
- Fabien GuySake Ungerer
- Kenneth Crawford
- Nathan Mallison
- Bill Condo
- Pierre Lebrun
- John Thompson
- Ryan Brewer
- Martin Bastien
- Alfonso Herrera
- Bichinger Software & Consulting
- Abhay
- Nicolaas
- Riki Fridrich
- Afif Sohaili
- Diana Bergholz
- Tomasz Kleszczewski
<!--10 end-->

<h2 align="center">Backers via OpenCollective</h2>

<a href="https://opencollective.com/vuejs#backers" target="_blank"><img src="https://opencollective.com/vuejs/backers.svg?width=890"></a>
```
## _github_COMMIT_CONVENTION_md
```## Git Commit Message Convention

> This is adapted from [Angular's commit convention](https://github.com/conventional-changelog/conventional-changelog/tree/master/packages/conventional-changelog-angular).

#### TL;DR:

Messages must be matched by the following regex:

''' js
/^(revert: )?(feat|fix|polish|docs|style|refactor|perf|test|workflow|ci|chore|types)(\(.+\))?: .{1,50}/
'''

#### Examples

Appears under "Features" header, `compiler` subheader:

'''
feat(compiler): add 'comments' option
'''

Appears under "Bug Fixes" header, `v-model` subheader, with a link to issue #28:

'''
fix(v-model): handle events on blur

close #28
'''

Appears under "Performance Improvements" header, and under "Breaking Changes" with the breaking change explanation:

'''
perf(core): improve vdom diffing by removing 'foo' option

BREAKING CHANGE: The 'foo' option has been removed.
'''

The following commit and commit `667ecc1` do not appear in the changelog if they are under the same release. If not, the revert commit appears under the "Reverts" header.

'''
revert: feat(compiler): add 'comments' option

This reverts commit 667ecc1654a317a13331b17617d973392f415f02.
'''

### Full Message Format

A commit message consists of a **header**, **body** and **footer**.  The header has a **type**, **scope** and **subject**:

'''
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
'''

The **header** is mandatory and the **scope** of the header is optional.

### Revert

If the commit reverts a previous commit, it should begin with `revert: `, followed by the header of the reverted commit. In the body, it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit being reverted.

### Type

If the prefix is `feat`, `fix` or `perf`, it will appear in the changelog. However, if there is any [BREAKING CHANGE](#footer), the commit will always appear in the changelog.

Other prefixes are up to your discretion. Suggested prefixes are `docs`, `chore`, `style`, `refactor`, and `test` for non-changelog related tasks.

### Scope

The scope could be anything specifying the place of the commit change. For example `core`, `compiler`, `ssr`, `v-model`, `transition` etc...

### Subject

The subject contains a succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize the first letter
* no dot (.) at the end

### Body

Just as in the **subject**, use the imperative, present tense: "change" not "changed" nor "changes".
The body should include the motivation for the change and contrast this with previous behavior.

### Footer

The footer should contain any information about **Breaking Changes** and is also the place to
reference GitHub issues that this commit **Closes**.

**Breaking Changes** should start with the word `BREAKING CHANGE:` with a space or two newlines. The rest of the commit message is then used for this.
```
# Inline
## _test_weex_runtime_style_spec_js

## _test_e2e_specs_svg_js

## _src_platforms_weex_runtime_components_index_js

## _src_core_vdom_modules_ref_js
### Line 33-42
```
  } else {
    if (vnode.data.refInFor) {
      if (!Array.isArray(refs[key])) {
        refs[key] = [ref]
      } else if (refs[key].indexOf(ref) < 0) {
        // $flow-disable-line
        refs[key].push(ref)
      }
    } else {
      refs[key] = ref

```

## _src_core_util_env_js
### Line 1-10
```
/* @flow */

// can we use __proto__?
export const hasProto = '__proto__' in {}

// Browser environment sniffing
export const inBrowser = typeof window !== 'undefined'
export const inWeex = typeof WXEnvironment !== 'undefined' && !!WXEnvironment.platform
export const weexPlatform = inWeex && WXEnvironment.platform.toLowerCase()
export const UA = inBrowser && window.navigator.userAgent.toLowerCase()

```
### Line 15-24
```
export const isIOS = (UA && /iphone|ipad|ipod|ios/.test(UA)) || (weexPlatform === 'ios')
export const isChrome = UA && /chrome\/\d+/.test(UA) && !isEdge
export const isPhantomJS = UA && /phantomjs/.test(UA)
export const isFF = UA && UA.match(/firefox\/(\d+)/)

// Firefox has a "watch" function on Object.prototype...
export const nativeWatch = ({}).watch

export let supportsPassive = false
if (inBrowser) {

```
### Line 32-58
```
    }: Object)) // https://github.com/facebook/flow/issues/285
    window.addEventListener('test-passive', null, opts)
  } catch (e) {}
}

// this needs to be lazy-evaled because vue may be required before
// vue-server-renderer can set VUE_ENV
let _isServer
export const isServerRendering = () => {
  if (_isServer === undefined) {
    /* istanbul ignore if */
    if (!inBrowser && !inWeex && typeof global !== 'undefined') {
      // detect presence of vue-server-renderer and avoid
      // Webpack shimming the process
      _isServer = global['process'] && global['process'].env.VUE_ENV === 'server'
    } else {
      _isServer = false
    }
  }
  return _isServer
}

// detect devtools
export const devtools = inBrowser && window.__VUE_DEVTOOLS_GLOBAL_HOOK__

/* istanbul ignore next */
export function isNative (Ctor: any): boolean {

```
### Line 64-76
```
  typeof Reflect !== 'undefined' && isNative(Reflect.ownKeys)

let _Set
/* istanbul ignore if */ // $flow-disable-line
if (typeof Set !== 'undefined' && isNative(Set)) {
  // use native Set when available.
  _Set = Set
} else {
  // a non-standard Set polyfill that only works with primitive keys.
  _Set = class Set implements SimpleSet {
    set: Object;
    constructor () {
      this.set = Object.create(null)

```

## _src_core_instance_render_helpers_resolve_slots_js
### Line 14-28
```
  }
  const slots = {}
  for (let i = 0, l = children.length; i < l; i++) {
    const child = children[i]
    const data = child.data
    // remove slot attribute if the node is resolved as a Vue slot node
    if (data && data.attrs && data.attrs.slot) {
      delete data.attrs.slot
    }
    // named slots should only be respected if the vnode was rendered in the
    // same context.
    if ((child.context === context || child.fnContext === context) &&
      data && data.slot != null
    ) {
      const name = data.slot

```
### Line 34-43
```
      }
    } else {
      (slots.default || (slots.default = [])).push(child)
    }
  }
  // ignore slots that contains only whitespace
  for (const name in slots) {
    if (slots[name].every(isWhitespace)) {
      delete slots[name]
    }

```

## _src_core_components_keep_alive_js
### Line 83-118
```
  render () {
    const slot = this.$slots.default
    const vnode: VNode = getFirstComponentChild(slot)
    const componentOptions: ?VNodeComponentOptions = vnode && vnode.componentOptions
    if (componentOptions) {
      // check pattern
      const name: ?string = getComponentName(componentOptions)
      const { include, exclude } = this
      if (
        // not included
        (include && (!name || !matches(include, name))) ||
        // excluded
        (exclude && name && matches(exclude, name))
      ) {
        return vnode
      }

      const { cache, keys } = this
      const key: ?string = vnode.key == null
        // same constructor may get registered as different local components
        // so cid alone is not enough (#3269)
        ? componentOptions.Ctor.cid + (componentOptions.tag ? `::${componentOptions.tag}` : '')
        : vnode.key
      if (cache[key]) {
        vnode.componentInstance = cache[key].componentInstance
        // make current key freshest
        remove(keys, key)
        keys.push(key)
      } else {
        cache[key] = vnode
        keys.push(key)
        // prune oldest entry
        if (this.max && keys.length > parseInt(this.max)) {
          pruneCacheEntry(cache, keys[0], keys, this._vnode)
        }
      }

```

## _dist_vue_esm_browser_js
### Line 5-15
```
 */
/*  */

const emptyObject = Object.freeze({});

// These helpers produce better VM code in JS engines due to their
// explicitness and function inlining.
function isUndef (v) {
  return v === undefined || v === null
}


```
### Line 30-39
```
 */
function isPrimitive (value) {
  return (
    typeof value === 'string' ||
    typeof value === 'number' ||
    // $flow-disable-line
    typeof value === 'symbol' ||
    typeof value === 'boolean'
  )
}

```
### Line 376-385
```

var config = ({
  /**
   * Option merge strategies (used in core/util/options)
   */
  // $flow-disable-line
  optionMergeStrategies: Object.create(null),

  /**
   * Whether to suppress warnings.

```
### Line 417-426
```
  ignoredElements: [],

  /**
   * Custom user key aliases for v-on
   */
  // $flow-disable-line
  keyCodes: Object.create(null),

  /**
   * Check if a tag is reserved so that it cannot be registered as a

```
### Line 515-527
```
  }
}

/*  */

// can we use __proto__?
const hasProto = '__proto__' in {};

// Browser environment sniffing
const inBrowser = typeof window !== 'undefined';
const inWeex = typeof WXEnvironment !== 'undefined' && !!WXEnvironment.platform;
const weexPlatform = inWeex && WXEnvironment.platform.toLowerCase();
const UA = inBrowser && window.navigator.userAgent.toLowerCase();

```
### Line 532-541
```
const isIOS = (UA && /iphone|ipad|ipod|ios/.test(UA)) || (weexPlatform === 'ios');
const isChrome = UA && /chrome\/\d+/.test(UA) && !isEdge;
const isPhantomJS = UA && /phantomjs/.test(UA);
const isFF = UA && UA.match(/firefox\/(\d+)/);

// Firefox has a "watch" function on Object.prototype...
const nativeWatch = ({}).watch;

let supportsPassive = false;
if (inBrowser) {

```
### Line 549-575
```
    })); // https://github.com/facebook/flow/issues/285
    window.addEventListener('test-passive', null, opts);
  } catch (e) {}
}

// this needs to be lazy-evaled because vue may be required before
// vue-server-renderer can set VUE_ENV
let _isServer;
const isServerRendering = () => {
  if (_isServer === undefined) {
    /* istanbul ignore if */
    if (!inBrowser && !inWeex && typeof global !== 'undefined') {
      // detect presence of vue-server-renderer and avoid
      // Webpack shimming the process
      _isServer = global['process'] && global['process'].env.VUE_ENV === 'server';
    } else {
      _isServer = false;
    }
  }
  return _isServer
};

// detect devtools
const devtools = inBrowser && window.__VUE_DEVTOOLS_GLOBAL_HOOK__;

/* istanbul ignore next */
function isNative (Ctor) {

```
### Line 581-593
```
  typeof Reflect !== 'undefined' && isNative(Reflect.ownKeys);

let _Set;
/* istanbul ignore if */ // $flow-disable-line
if (typeof Set !== 'undefined' && isNative(Set)) {
  // use native Set when available.
  _Set = Set;
} else {
  // a non-standard Set polyfill that only works with primitive keys.
  _Set = class Set   {
    
    constructor () {
      this.set = Object.create(null);

```
### Line 733-758
```
      Dep.target.addDep(this);
    }
  }

  notify () {
    // stabilize the subscriber list first
    const subs = this.subs.slice();
    if (!config.async) {
      // subs aren't sorted in scheduler if not running async
      // we need to sort them now to make sure they fire in correct
      // order
      subs.sort((a, b) => a.id - b.id);
    }
    for (let i = 0, l = subs.length; i < l; i++) {
      subs[i].update();
    }
  }
}

// The current target watcher being evaluated.
// This is globally unique because only one watcher
// can be evaluated at a time.
Dep.target = null;
const targetStack = [];

function pushTarget (target) {

```
### Line 772-801
```
  
  
  
  
  
   // rendered in this component's scope
  
  
   // component instance
   // component placeholder node

  // strictly internal
   // contains raw HTML? (server only)
   // hoisted static node
   // necessary for enter transition check
   // empty comment placeholder?
   // is a cloned node?
   // is a v-once node?
   // async component factory function
  
  
  
   // real context vm for functional nodes
   // for SSR caching
   // used to store functional render context for devtools
   // functional scope id support

  constructor (
    tag,
    data,

```
### Line 829-838
```
    this.asyncFactory = asyncFactory;
    this.asyncMeta = undefined;
    this.isAsyncPlaceholder = false;
  }

  // DEPRECATED: alias for componentInstance for backwards compat.
  /* istanbul ignore next */
  get child () {
    return this.componentInstance
  }

```
### Line 847-866
```

function createTextVNode (val) {
  return new VNode(undefined, undefined, undefined, String(val))
}

// optimized shallow clone
// used for static nodes and slot nodes because they may be reused across
// multiple renders, cloning them avoids errors when DOM manipulations rely
// on their elm reference.
function cloneVNode (vnode) {
  const cloned = new VNode(
    vnode.tag,
    vnode.data,
    // #7975
    // clone children array to avoid mutating original in case of cloning
    // a child.
    vnode.children && vnode.children.slice(),
    vnode.text,
    vnode.elm,
    vnode.context,

```
### Line 899-908
```

/**
 * Intercept mutating methods and emit events
 */
methodsToPatch.forEach(function (method) {
  // cache original method
  const original = arrayProto[method];
  def(arrayMethods, method, function mutator (...args) {
    const result = original.apply(this, args);
    const ob = this.__ob__;

```
### Line 915-924
```
      case 'splice':
        inserted = args.slice(2);
        break
    }
    if (inserted) ob.observeArray(inserted);
    // notify change
    ob.dep.notify();
    return result
  });
});

```
### Line 944-953
```
 * collect dependencies and dispatch updates.
 */
class Observer {
  
  
   // number of vms that have this object as root $data

  constructor (value) {
    this.value = value;
    this.dep = new Dep();

```
### Line 985-994
```
      observe(items[i]);
    }
  }
}

// helpers

/**
 * Augment a target Object or Array by intercepting
 * the prototype chain using __proto__

```
### Line 1053-1062
```
  const property = Object.getOwnPropertyDescriptor(obj, key);
  if (property && property.configurable === false) {
    return
  }

  // cater for pre-defined getter/setters
  const getter = property && property.get;
  const setter = property && property.set;
  if ((!getter || setter) && arguments.length === 2) {
    val = obj[key];

```
### Line 1087-1096
```
      }
      /* eslint-enable no-self-compare */
      if (customSetter) {
        customSetter();
      }
      // #7981: for accessor properties without setter
      if (getter && !setter) return
      if (setter) {
        setter.call(obj, newVal);
      } else {

```
### Line 1217-1226
```
    ? Reflect.ownKeys(from)
    : Object.keys(from);

  for (let i = 0; i < keys.length; i++) {
    key = keys[i];
    // in case the object is already observed...
    if (key === '__ob__') continue
    toVal = to[key];
    fromVal = from[key];
    if (!hasOwn(to, key)) {

```
### Line 1243-1272
```
  parentVal,
  childVal,
  vm
) {
  if (!vm) {
    // in a Vue.extend merge, both should be functions
    if (!childVal) {
      return parentVal
    }
    if (!parentVal) {
      return childVal
    }
    // when parentVal & childVal are both present,
    // we need to return a function that returns the
    // merged result of both functions... no need to
    // check if parentVal is a function here because
    // it has to be a function to pass previous merges.
    return function mergedDataFn () {
      return mergeData(
        typeof childVal === 'function' ? childVal.call(this, this) : childVal,
        typeof parentVal === 'function' ? parentVal.call(this, this) : parentVal
      )
    }
  } else {
    return function mergedInstanceDataFn () {
      // instance merge
      const instanceData = typeof childVal === 'function'
        ? childVal.call(vm, vm)
        : childVal;
      const defaultData = typeof parentVal === 'function'

```
### Line 1372-1381
```
  parentVal,
  childVal,
  vm,
  key
) {
  // work around Firefox's Object.prototype.watch...
  if (parentVal === nativeWatch) parentVal = undefined;
  if (childVal === nativeWatch) childVal = undefined;
  /* istanbul ignore if */
  if (!childVal) return Object.create(parentVal || null)

```
### Line 1563-1575
```

  normalizeProps(child, vm);
  normalizeInject(child, vm);
  normalizeDirectives(child);

  // Apply extends and mixins on the child options,
  // but only if it is a raw options object that isn't
  // the result of another mergeOptions call.
  // Only merged options has the _base property.
  if (!child._base) {
    if (child.extends) {
      parent = mergeOptions(parent, child.extends, vm);
    }

```
### Line 1611-1626
```
  /* istanbul ignore if */
  if (typeof id !== 'string') {
    return
  }
  const assets = options[type];
  // check local registration variations first
  if (hasOwn(assets, id)) return assets[id]
  const camelizedId = camelize(id);
  if (hasOwn(assets, camelizedId)) return assets[camelizedId]
  const PascalCaseId = capitalize(camelizedId);
  if (hasOwn(assets, PascalCaseId)) return assets[PascalCaseId]
  // fallback to prototype chain
  const res = assets[id] || assets[camelizedId] || assets[PascalCaseId];
  if (warnMissing && !res) {
    warn(
      'Failed to resolve ' + type.slice(0, -1) + ': ' + id,

```
### Line 1641-1668
```
  vm
) {
  const prop = propOptions[key];
  const absent = !hasOwn(propsData, key);
  let value = propsData[key];
  // boolean casting
  const booleanIndex = getTypeIndex(Boolean, prop.type);
  if (booleanIndex > -1) {
    if (absent && !hasOwn(prop, 'default')) {
      value = false;
    } else if (value === '' || value === hyphenate(key)) {
      // only cast empty string / same name to boolean if
      // boolean has higher priority
      const stringIndex = getTypeIndex(String, prop.type);
      if (stringIndex < 0 || booleanIndex < stringIndex) {
        value = true;
      }
    }
  }
  // check default value
  if (value === undefined) {
    value = getPropDefaultValue(vm, prop, key);
    // since the default value is a fresh copy,
    // make sure to observe it.
    const prevShouldObserve = shouldObserve;
    toggleObserving(true);
    observe(value);
    toggleObserving(prevShouldObserve);

```
### Line 1675-1707
```

/**
 * Get the default value of a prop.
 */
function getPropDefaultValue (vm, prop, key) {
  // no default, return undefined
  if (!hasOwn(prop, 'default')) {
    return undefined
  }
  const def = prop.default;
  // warn against non-factory defaults for Object & Array
  if (isObject(def)) {
    warn(
      'Invalid default value for prop "' + key + '": ' +
      'Props with type Object/Array must use a factory function ' +
      'to return the default value.',
      vm
    );
  }
  // the raw prop value was also undefined from previous render,
  // return previous default value to avoid unnecessary watcher trigger
  if (vm && vm.$options.propsData &&
    vm.$options.propsData[key] === undefined &&
    vm._props[key] !== undefined
  ) {
    return vm._props[key]
  }
  // call factory function for non-Function types
  // a value is Function if its prototype is function even across different execution context
  return typeof def === 'function' && getType(prop.type) !== 'Function'
    ? def.call(vm)
    : def
}

```
### Line 1764-1773
```
  let valid;
  const expectedType = getType(type);
  if (simpleCheckRE.test(expectedType)) {
    const t = typeof value;
    valid = t === expectedType.toLowerCase();
    // for primitive wrapper objects
    if (!valid && t === 'object') {
      valid = value instanceof type;
    }
  } else if (expectedType === 'Object') {

```
### Line 1814-1830
```
    ` Expected ${expectedTypes.map(capitalize).join(', ')}`;
  const expectedType = expectedTypes[0];
  const receivedType = toRawType(value);
  const expectedValue = styleValue(value, expectedType);
  const receivedValue = styleValue(value, receivedType);
  // check if we need to specify expected value
  if (expectedTypes.length === 1 &&
      isExplicable(expectedType) &&
      !isBoolean(expectedType, receivedType)) {
    message += ` with value ${expectedValue}`;
  }
  message += `, got ${receivedType} `;
  // check if we need to specify received value
  if (isExplicable(receivedType)) {
    message += `with value ${receivedValue}.`;
  }
  return message

```
### Line 1850-1860
```
}

/*  */

function handleError (err, vm, info) {
  // Deactivate deps tracking while processing error handler to avoid possible infinite rendering.
  // See: https://github.com/vuejs/vuex/issues/1505
  pushTarget();
  try {
    if (vm) {
      let cur = vm;

```
### Line 1888-1898
```
  let res;
  try {
    res = args ? handler.apply(context, args) : handler.call(context);
    if (res && !res._isVue && isPromise(res) && !res._handled) {
      res.catch(e => handleError(e, vm, info + ` (Promise/async)`));
      // issue #9511
      // avoid catch triggering multiple times when nested calls
      res._handled = true;
    }
  } catch (e) {
    handleError(e, vm, info);

```
### Line 1903-1913
```
function globalHandleError (err, vm, info) {
  if (config.errorHandler) {
    try {
      return config.errorHandler.call(null, err, vm, info)
    } catch (e) {
      // if the user intentionally throws the original error in the handler,
      // do not log it twice
      if (e !== err) {
        logError(e, null, 'config.errorHandler');
      }
    }

```
### Line 1941-1989
```
  for (let i = 0; i < copies.length; i++) {
    copies[i]();
  }
}

// Here we have async deferring wrappers using microtasks.
// In 2.5 we used (macro) tasks (in combination with microtasks).
// However, it has subtle problems when state is changed right before repaint
// (e.g. #6813, out-in transitions).
// Also, using (macro) tasks in event handler would cause some weird behaviors
// that cannot be circumvented (e.g. #7109, #7153, #7546, #7834, #8109).
// So we now use microtasks everywhere, again.
// A major drawback of this tradeoff is that there are some scenarios
// where microtasks have too high a priority and fire in between supposedly
// sequential events (e.g. #4521, #6690, which have workarounds)
// or even between bubbling of the same event (#6566).
let timerFunc;

// The nextTick behavior leverages the microtask queue, which can be accessed
// via either native Promise.then or MutationObserver.
// MutationObserver has wider support, however it is seriously bugged in
// UIWebView in iOS >= 9.3.3 when triggered in touch event handlers. It
// completely stops working after triggering a few times... so, if native
// Promise is available, we will use it:
/* istanbul ignore next, $flow-disable-line */
if (typeof Promise !== 'undefined' && isNative(Promise)) {
  const p = Promise.resolve();
  timerFunc = () => {
    p.then(flushCallbacks);
    // In problematic UIWebViews, Promise.then doesn't completely break, but
    // it can get stuck in a weird state where callbacks are pushed into the
    // microtask queue but the queue isn't being flushed, until the browser
    // needs to do some other work, e.g. handle a timer. Therefore we can
    // "force" the microtask queue to be flushed by adding an empty timer.
    if (isIOS) setTimeout(noop);
  };
  isUsingMicroTask = true;
} else if (!isIE && typeof MutationObserver !== 'undefined' && (
  isNative(MutationObserver) ||
  // PhantomJS and iOS 7.x
  MutationObserver.toString() === '[object MutationObserverConstructor]'
)) {
  // Use MutationObserver where native Promise is not available,
  // e.g. PhantomJS, iOS7, Android 4.4
  // (#6466 MutationObserver is unreliable in IE11)
  let counter = 1;
  const observer = new MutationObserver(flushCallbacks);
  const textNode = document.createTextNode(String(counter));
  observer.observe(textNode, {

```
### Line 1993-2009
```
    counter = (counter + 1) % 2;
    textNode.data = String(counter);
  };
  isUsingMicroTask = true;
} else if (typeof setImmediate !== 'undefined' && isNative(setImmediate)) {
  // Fallback to setImmediate.
  // Techinically it leverages the (macro) task queue,
  // but it is still a better choice than setTimeout.
  timerFunc = () => {
    setImmediate(flushCallbacks);
  };
} else {
  // Fallback to setTimeout.
  timerFunc = () => {
    setTimeout(flushCallbacks, 0);
  };
}

```
### Line 2023-2032
```
  });
  if (!pending) {
    pending = true;
    timerFunc();
  }
  // $flow-disable-line
  if (!cb && typeof Promise !== 'undefined') {
    return new Promise(resolve => {
      _resolve = resolve;
    })

```
### Line 2051-2060
```
    mark = tag => perf.mark(tag);
    measure = (name, startTag, endTag) => {
      perf.measure(name, startTag, endTag);
      perf.clearMarks(startTag);
      perf.clearMarks(endTag);
      // perf.clearMeasures(name)
    };
  }
}


```
### Line 2132-2141
```
    }
  };

  initProxy = function initProxy (vm) {
    if (hasProxy) {
      // determine which proxy handler to use
      const options = vm.$options;
      const handlers = options.render && options.render._withStripped
        ? getHandler
        : hasHandler;

```
### Line 2207-2216
```
      const cloned = fns.slice();
      for (let i = 0; i < cloned.length; i++) {
        invokeWithErrorHandling(cloned[i], null, arguments, vm, `v-on handler`);
      }
    } else {
      // return handler return value for single handlers
      return invokeWithErrorHandling(fns, null, arguments, vm, `v-on handler`)
    }
  }
  invoker.fns = fns;

```
### Line 2265-2289
```
  let invoker;
  const oldHook = def[hookKey];

  function wrappedHook () {
    hook.apply(this, arguments);
    // important: remove merged hook to ensure it's called only once
    // and prevent memory leak
    remove(invoker.fns, wrappedHook);
  }

  if (isUndef(oldHook)) {
    // no existing hook
    invoker = createFnInvoker([wrappedHook]);
  } else {
    /* istanbul ignore if */
    if (isDef(oldHook.fns) && isTrue(oldHook.merged)) {
      // already a merged invoker
      invoker = oldHook;
      invoker.fns.push(wrappedHook);
    } else {
      // existing plain hook
      invoker = createFnInvoker([oldHook, wrappedHook]);
    }
  }


```
### Line 2296-2307
```
function extractPropsFromVNodeData (
  data,
  Ctor,
  tag
) {
  // we are only extracting raw values here.
  // validation and default values are handled in the child
  // component itself.
  const propOptions = Ctor.options.props;
  if (isUndef(propOptions)) {
    return
  }

```
### Line 2358-2378
```
  return false
}

/*  */

// The template compiler attempts to minimize the need for normalization by
// statically analyzing the template at compile time.
//
// For plain HTML markup, normalization can be completely skipped because the
// generated render function is guaranteed to return Array<VNode>. There are
// two cases where extra normalization is needed:

// 1. When the children contains components - because a functional component
// may return an Array instead of a single root. In this case, just a simple
// normalization is needed - if any child is an Array, we flatten the whole
// thing with Array.prototype.concat. It is guaranteed to be only 1-level deep
// because functional components already normalize their own children.
function simpleNormalizeChildren (children) {
  for (let i = 0; i < children.length; i++) {
    if (Array.isArray(children[i])) {
      return Array.prototype.concat.apply([], children)

```
### Line 2379-2391
```
    }
  }
  return children
}

// 2. When the children contains constructs that always generated nested Arrays,
// e.g. <template>, <slot>, v-for, or when the children is provided by user
// with hand-written render functions / JSX. In such cases a full normalization
// is needed to cater to all possible types of children values.
function normalizeChildren (children) {
  return isPrimitive(children)
    ? [createTextVNode(children)]
    : Array.isArray(children)

```
### Line 2403-2438
```
  for (i = 0; i < children.length; i++) {
    c = children[i];
    if (isUndef(c) || typeof c === 'boolean') continue
    lastIndex = res.length - 1;
    last = res[lastIndex];
    //  nested
    if (Array.isArray(c)) {
      if (c.length > 0) {
        c = normalizeArrayChildren(c, `${nestedIndex || ''}_${i}`);
        // merge adjacent text nodes
        if (isTextNode(c[0]) && isTextNode(last)) {
          res[lastIndex] = createTextVNode(last.text + (c[0]).text);
          c.shift();
        }
        res.push.apply(res, c);
      }
    } else if (isPrimitive(c)) {
      if (isTextNode(last)) {
        // merge adjacent text nodes
        // this is necessary for SSR hydration because text nodes are
        // essentially merged when rendered to HTML strings
        res[lastIndex] = createTextVNode(last.text + c);
      } else if (c !== '') {
        // convert primitive to vnode
        res.push(createTextVNode(c));
      }
    } else {
      if (isTextNode(c) && isTextNode(last)) {
        // merge adjacent text nodes
        res[lastIndex] = createTextVNode(last.text + c.text);
      } else {
        // default key for nested array children (likely generated by v-for)
        if (isTrue(children._isVList) &&
          isDef(c.tag) &&
          isUndef(c.key) &&
          isDef(nestedIndex)) {

```
### Line 2477-2494
```
  }
}

function resolveInject (inject, vm) {
  if (inject) {
    // inject is :any because flow is not smart enough to figure out cached
    const result = Object.create(null);
    const keys = hasSymbol
      ? Reflect.ownKeys(inject)
      : Object.keys(inject);

    for (let i = 0; i < keys.length; i++) {
      const key = keys[i];
      // #6574 in case the inject object is observed...
      if (key === '__ob__') continue
      const provideKey = inject[key].from;
      let source = vm;
      while (source) {

```
### Line 2529-2543
```
  }
  const slots = {};
  for (let i = 0, l = children.length; i < l; i++) {
    const child = children[i];
    const data = child.data;
    // remove slot attribute if the node is resolved as a Vue slot node
    if (data && data.attrs && data.attrs.slot) {
      delete data.attrs.slot;
    }
    // named slots should only be respected if the vnode was rendered in the
    // same context.
    if ((child.context === context || child.fnContext === context) &&
      data && data.slot != null
    ) {
      const name = data.slot;

```
### Line 2549-2558
```
      }
    } else {
      (slots.default || (slots.default = [])).push(child);
    }
  }
  // ignore slots that contains only whitespace
  for (const name in slots) {
    if (slots[name].every(isWhitespace)) {
      delete slots[name];
    }

```
### Line 2576-2585
```
  const isStable = slots ? !!slots.$stable : !hasNormalSlots;
  const key = slots && slots.$key;
  if (!slots) {
    res = {};
  } else if (slots._normalized) {
    // fast path 1: child component re-render only, parent did not change
    return slots._normalized
  } else if (
    isStable &&
    prevSlots &&

```
### Line 2586-2596
```
    prevSlots !== emptyObject &&
    key === prevSlots.$key &&
    !hasNormalSlots &&
    !prevSlots.$hasNormal
  ) {
    // fast path 2: stable scoped slots w/ no normal slots to proxy,
    // only need to normalize once
    return prevSlots
  } else {
    res = {};
    for (const key in slots) {

```
### Line 2597-2613
```
      if (slots[key] && key[0] !== '$') {
        res[key] = normalizeScopedSlot(normalSlots, key, slots[key]);
      }
    }
  }
  // expose normal slots on scopedSlots
  for (const key in normalSlots) {
    if (!(key in res)) {
      res[key] = proxyNormalSlot(normalSlots, key);
    }
  }
  // avoriaz seems to mock a non-extensible $scopedSlots object
  // and when that is passed down this would cause an error
  if (slots && Object.isExtensible(slots)) {
    (slots)._normalized = res;
  }
  def(res, '$stable', isStable);

```
### Line 2626-2637
```
      res.length === 0 ||
      (res.length === 1 && res[0].isComment) // #9658
    ) ? undefined
      : res
  };
  // this is a slot using the new v-slot syntax without scope. although it is
  // compiled as a scoped slot, render fn users would expect it to be present
  // on this.$slots because the usage is semantically a normal slot.
  if (fn.proxy) {
    Object.defineProperty(normalSlots, key, {
      get: normalized,
      enumerable: true,

```
### Line 2831-2845
```
  index,
  isInFor
) {
  const cached = this._staticTrees || (this._staticTrees = []);
  let tree = cached[index];
  // if has already-rendered static tree and not inside v-for,
  // we can reuse the same tree.
  if (tree && !isInFor) {
    return tree
  }
  // otherwise, render a fresh tree.
  tree = cached[index] = this.$options.staticRenderFns[index].call(
    this._renderProxy,
    null,
    this // for render fns generated for functional component templates

```
### Line 2907-2916
```
/*  */

function resolveScopedSlots (
  fns, // see flow/vnode
  res,
  // the following are added in 2.6
  hasDynamicKeys,
  contentHashKey
) {
  res = res || { $stable: !hasDynamicKeys };

```
### Line 2917-2926
```
  for (let i = 0; i < fns.length; i++) {
    const slot = fns[i];
    if (Array.isArray(slot)) {
      resolveScopedSlots(slot, res, hasDynamicKeys);
    } else if (slot) {
      // marker for reverse proxying v-slot without scope on this.$slots
      if (slot.proxy) {
        slot.fn.proxy = true;
      }
      res[slot.key] = slot.fn;

```
### Line 2938-2947
```
  for (let i = 0; i < values.length; i += 2) {
    const key = values[i];
    if (typeof key === 'string' && key) {
      baseObj[values[i]] = values[i + 1];
    } else if (key !== '' && key !== null) {
      // null is a speical value for explicitly removing a binding
      warn(
        `Invalid value for dynamic directive argument (expected string or null): ${key}`,
        this
      );

```
### Line 2948-2959
```
    }
  }
  return baseObj
}

// helper to dynamically append modifier runtime markers to event names.
// ensure only append when value is already string, otherwise it will be cast
// to string and cause the type check to miss.
function prependModifier (value, symbol) {
  return typeof value === 'string' ? symbol + value : value
}


```
### Line 2987-3008
```
  children,
  parent,
  Ctor
) {
  const options = Ctor.options;
  // ensure the createElement function in functional components
  // gets a unique context - this is necessary for correct named slot check
  let contextVm;
  if (hasOwn(parent, '_uid')) {
    contextVm = Object.create(parent);
    // $flow-disable-line
    contextVm._original = parent;
  } else {
    // the context vm passed in is a functional context as well.
    // in this case we want to make sure we are able to get a hold to the
    // real context instance.
    contextVm = parent;
    // $flow-disable-line
    parent = parent._original;
  }
  const isCompiled = isTrue(options._compiled);
  const needNormalization = !isCompiled;

```
### Line 3028-3041
```
    get () {
      return normalizeScopedSlots(data.scopedSlots, this.slots())
    }
  }));

  // support for compiled functional template
  if (isCompiled) {
    // exposing $options for renderStatic()
    this.$options = options;
    // pre-resolve slots for renderSlot()
    this.$slots = this.slots();
    this.$scopedSlots = normalizeScopedSlots(data.scopedSlots, this.$slots);
  }


```
### Line 3095-3106
```
    return res
  }
}

function cloneAndMarkFunctionalResult (vnode, data, contextVm, options, renderContext) {
  // #7817 clone node before setting fnContext, otherwise if the node is reused
  // (e.g. it was from a cached normal slot) the fnContext causes named slots
  // that should not be matched to match.
  const clone = cloneVNode(vnode);
  clone.fnContext = contextVm;
  clone.fnOptions = options;
  {

```
### Line 3124-3141
```

/*  */

/*  */

// inline hooks to be invoked on component VNodes during patch
const componentVNodeHooks = {
  init (vnode, hydrating) {
    if (
      vnode.componentInstance &&
      !vnode.componentInstance._isDestroyed &&
      vnode.data.keepAlive
    ) {
      // kept-alive components, treat as a patch
      const mountedNode = vnode; // work around flow
      componentVNodeHooks.prepatch(mountedNode, mountedNode);
    } else {
      const child = vnode.componentInstance = createComponentInstanceForVnode(

```
### Line 3164-3177
```
      componentInstance._isMounted = true;
      callHook(componentInstance, 'mounted');
    }
    if (vnode.data.keepAlive) {
      if (context._isMounted) {
        // vue-router#1212
        // During updates, a kept-alive component's child components may
        // change, so directly walking the tree here may call activated hooks
        // on incorrect children. Instead we push them into a queue which will
        // be processed after the whole patch process ended.
        queueActivatedComponent(componentInstance);
      } else {
        activateChildComponent(componentInstance, true /* direct */);
      }

```
### Line 3203-3234
```
    return
  }

  const baseCtor = context.$options._base;

  // plain options object: turn it into a constructor
  if (isObject(Ctor)) {
    Ctor = baseCtor.extend(Ctor);
  }

  // if at this stage it's not a constructor or an async component factory,
  // reject.
  if (typeof Ctor !== 'function') {
    {
      warn(`Invalid Component definition: ${String(Ctor)}`, context);
    }
    return
  }

  // async component
  let asyncFactory;
  if (isUndef(Ctor.cid)) {
    asyncFactory = Ctor;
    Ctor = resolveAsyncComponent(asyncFactory, baseCtor);
    if (Ctor === undefined) {
      // return a placeholder node for async component, which is rendered
      // as a comment node but preserves all the raw information for the node.
      // the information will be used for async server-rendering and hydration.
      return createAsyncPlaceholder(
        asyncFactory,
        data,
        context,

```
### Line 3238-3286
```
    }
  }

  data = data || {};

  // resolve constructor options in case global mixins are applied after
  // component constructor creation
  resolveConstructorOptions(Ctor);

  // transform component v-model data into props & events
  if (isDef(data.model)) {
    transformModel(Ctor.options, data);
  }

  // extract props
  const propsData = extractPropsFromVNodeData(data, Ctor, tag);

  // functional component
  if (isTrue(Ctor.options.functional)) {
    return createFunctionalComponent(Ctor, propsData, data, context, children)
  }

  // extract listeners, since these needs to be treated as
  // child component listeners instead of DOM listeners
  const listeners = data.on;
  // replace with listeners with .native modifier
  // so it gets processed during parent component patch.
  data.on = data.nativeOn;

  if (isTrue(Ctor.options.abstract)) {
    // abstract components do not keep anything
    // other than props & listeners & slot

    // work around flow
    const slot = data.slot;
    data = {};
    if (slot) {
      data.slot = slot;
    }
  }

  // install component management hooks onto the placeholder node
  installComponentHooks(data);

  // return a placeholder vnode
  const name = Ctor.options.name || tag;
  const vnode = new VNode(
    `vue-component-${Ctor.cid}${name ? `-${name}` : ''}`,
    data, undefined, undefined, undefined, context,

```
### Line 3298-3307
```
  const options = {
    _isComponent: true,
    _parentVnode: vnode,
    parent
  };
  // check inline-template render functions
  const inlineTemplate = vnode.data.inlineTemplate;
  if (isDef(inlineTemplate)) {
    options.render = inlineTemplate.render;
    options.staticRenderFns = inlineTemplate.staticRenderFns;

```
### Line 3321-3339
```
  }
}

function mergeHook$1 (f1, f2) {
  const merged = (a, b) => {
    // flow complains about extra args which is why we use any
    f1(a, b);
    f2(a, b);
  };
  merged._merged = true;
  return merged
}

// transform component v-model info (value and callback) into
// prop and event handler respectively.
function transformModel (options, data) {
  const prop = (options.model && options.model.prop) || 'value';
  const event = (options.model && options.model.event) || 'input'
  ;(data.attrs || (data.attrs = {}))[prop] = data.model.value;

```
### Line 3356-3366
```
/*  */

const SIMPLE_NORMALIZE = 1;
const ALWAYS_NORMALIZE = 2;

// wrapper function for providing a more flexible interface
// without getting yelled at by flow
function createElement (
  context,
  tag,
  data,

```
### Line 3392-3409
```
      'Always create fresh vnode data objects in each render!',
      context
    );
    return createEmptyVNode()
  }
  // object syntax in v-bind
  if (isDef(data) && isDef(data.is)) {
    tag = data.is;
  }
  if (!tag) {
    // in case of component :is set to falsy value
    return createEmptyVNode()
  }
  // warn against non-primitive key
  if (isDef(data) && isDef(data.key) && !isPrimitive(data.key)
  ) {
    {
      warn(

```
### Line 3411-3420
```
        'use string/number value instead.',
        context
      );
    }
  }
  // support single function children as default scoped slot
  if (Array.isArray(children) &&
    typeof children[0] === 'function'
  ) {
    data = data || {};

```
### Line 3429-3456
```
  let vnode, ns;
  if (typeof tag === 'string') {
    let Ctor;
    ns = (context.$vnode && context.$vnode.ns) || config.getTagNamespace(tag);
    if (config.isReservedTag(tag)) {
      // platform built-in elements
      vnode = new VNode(
        config.parsePlatformTagName(tag), data, children,
        undefined, undefined, context
      );
    } else if ((!data || !data.pre) && isDef(Ctor = resolveAsset(context.$options, 'components', tag))) {
      // component
      vnode = createComponent(Ctor, data, context, children, tag);
    } else {
      // unknown or unlisted namespaced elements
      // check at runtime because it may get assigned a namespace when its
      // parent normalizes children
      vnode = new VNode(
        tag, data, children,
        undefined, undefined, context
      );
    }
  } else {
    // direct component options / constructor
    vnode = createComponent(tag, data, context, children);
  }
  if (Array.isArray(vnode)) {
    return vnode

```
### Line 3464-3473
```
}

function applyNS (vnode, ns, force) {
  vnode.ns = ns;
  if (vnode.tag === 'foreignObject') {
    // use default namespace inside foreignObject
    ns = undefined;
    force = true;
  }
  if (isDef(vnode.children)) {

```
### Line 3479-3490
```
      }
    }
  }
}

// ref #5318
// necessary to ensure parent re-render when deep bindings like :style and
// :class are used on slot nodes
function registerDeepBindings (data) {
  if (isObject(data.style)) {
    traverse(data.style);
  }

```
### Line 3501-3520
```
  const options = vm.$options;
  const parentVnode = vm.$vnode = options._parentVnode; // the placeholder node in parent tree
  const renderContext = parentVnode && parentVnode.context;
  vm.$slots = resolveSlots(options._renderChildren, renderContext);
  vm.$scopedSlots = emptyObject;
  // bind the createElement fn to this instance
  // so that we get proper render context inside it.
  // args order: tag, data, children, normalizationType, alwaysNormalize
  // internal version is used by render functions compiled from templates
  vm._c = (a, b, c, d) => createElement(vm, a, b, c, d, false);
  // normalization is always applied for the public version, used in
  // user-written render functions.
  vm.$createElement = (a, b, c, d) => createElement(vm, a, b, c, d, true);

  // $attrs & $listeners are exposed for easier HOC creation.
  // they need to be reactive so that HOCs using them are always updated
  const parentData = parentVnode && parentVnode.data;

  /* istanbul ignore else */
  {

```
### Line 3528-3537
```
}

let currentRenderingInstance = null;

function renderMixin (Vue) {
  // install runtime convenience helpers
  installRenderHelpers(Vue.prototype);

  Vue.prototype.$nextTick = function (fn) {
    return nextTick(fn, this)

```
### Line 3547-3570
```
        vm.$slots,
        vm.$scopedSlots
      );
    }

    // set parent vnode. this allows render functions to have access
    // to the data on the placeholder node.
    vm.$vnode = _parentVnode;
    // render self
    let vnode;
    try {
      // There's no need to maintain a stack becaues all render fns are called
      // separately from one another. Nested component's render fns are called
      // when parent component is patched.
      currentRenderingInstance = vm;
      vnode = render.call(vm._renderProxy, vm.$createElement);
    } catch (e) {
      handleError(e, vm, `render`);
      // return error render result,
      // or previous vnode to prevent render error causing blank component
      /* istanbul ignore else */
      if (vm.$options.renderError) {
        try {
          vnode = vm.$options.renderError.call(vm._renderProxy, vm.$createElement, e);

```
### Line 3576-3589
```
        vnode = vm._vnode;
      }
    } finally {
      currentRenderingInstance = null;
    }
    // if the returned array contains only a single node, allow it
    if (Array.isArray(vnode) && vnode.length === 1) {
      vnode = vnode[0];
    }
    // return empty vnode in case the render function errored out
    if (!(vnode instanceof VNode)) {
      if (Array.isArray(vnode)) {
        warn(
          'Multiple root nodes returned from render function. Render function ' +

```
### Line 3591-3600
```
          vm
        );
      }
      vnode = createEmptyVNode();
    }
    // set parent
    vnode.parent = _parentVnode;
    return vnode
  };
}

```
### Line 3638-3647
```
    return factory.resolved
  }

  const owner = currentRenderingInstance;
  if (owner && isDef(factory.owners) && factory.owners.indexOf(owner) === -1) {
    // already pending
    factory.owners.push(owner);
  }

  if (isTrue(factory.loading) && isDef(factory.loadingComp)) {

```
### Line 3673-3685
```
        }
      }
    };

    const resolve = once((res) => {
      // cache resolved
      factory.resolved = ensureCtor(res, baseCtor);
      // invoke callbacks only if this is not a synchronous resolve
      // (async resolves are shimmed as synchronous during SSR)
      if (!sync) {
        forceRender(true);
      } else {
        owners.length = 0;

```
### Line 3699-3708
```

    const res = factory(resolve, reject);

    if (isObject(res)) {
      if (isPromise(res)) {
        // () => Promise
        if (isUndef(factory.resolved)) {
          res.then(resolve, reject);
        }
      } else if (isPromise(res.component)) {

```
### Line 3739-3748
```
        }
      }
    }

    sync = false;
    // return in case resolved synchronously
    return factory.loading
      ? factory.loadingComp
      : factory.resolved
  }

```
### Line 3772-3781
```
/*  */

function initEvents (vm) {
  vm._events = Object.create(null);
  vm._hasHookEvent = false;
  // init parent attached events
  const listeners = vm.$options._parentListeners;
  if (listeners) {
    updateComponentListeners(vm, listeners);
  }

```
### Line 3819-3829
```
      for (let i = 0, l = event.length; i < l; i++) {
        vm.$on(event[i], fn);
      }
    } else {
      (vm._events[event] || (vm._events[event] = [])).push(fn);
      // optimize hook:event cost by using a boolean flag marked at registration
      // instead of a hash lookup
      if (hookRE.test(event)) {
        vm._hasHookEvent = true;
      }
    }

```
### Line 3841-3871
```
    return vm
  };

  Vue.prototype.$off = function (event, fn) {
    const vm = this;
    // all
    if (!arguments.length) {
      vm._events = Object.create(null);
      return vm
    }
    // array of events
    if (Array.isArray(event)) {
      for (let i = 0, l = event.length; i < l; i++) {
        vm.$off(event[i], fn);
      }
      return vm
    }
    // specific event
    const cbs = vm._events[event];
    if (!cbs) {
      return vm
    }
    if (!fn) {
      vm._events[event] = null;
      return vm
    }
    // specific handler
    let cb;
    let i = cbs.length;
    while (i--) {
      cb = cbs[i];

```
### Line 3918-3927
```
}

function initLifecycle (vm) {
  const options = vm.$options;

  // locate first non-abstract parent
  let parent = options.parent;
  if (parent && !options.abstract) {
    while (parent.$options.abstract && parent.$parent) {
      parent = parent.$parent;

```
### Line 3948-3979
```
    const vm = this;
    const prevEl = vm.$el;
    const prevVnode = vm._vnode;
    const restoreActiveInstance = setActiveInstance(vm);
    vm._vnode = vnode;
    // Vue.prototype.__patch__ is injected in entry points
    // based on the rendering backend used.
    if (!prevVnode) {
      // initial render
      vm.$el = vm.__patch__(vm.$el, vnode, hydrating, false /* removeOnly */);
    } else {
      // updates
      vm.$el = vm.__patch__(prevVnode, vnode);
    }
    restoreActiveInstance();
    // update __vue__ reference
    if (prevEl) {
      prevEl.__vue__ = null;
    }
    if (vm.$el) {
      vm.$el.__vue__ = vm;
    }
    // if parent is an HOC, update its $el as well
    if (vm.$vnode && vm.$parent && vm.$vnode === vm.$parent._vnode) {
      vm.$parent.$el = vm.$el;
    }
    // updated hook is called by the scheduler to ensure that children are
    // updated in a parent's updated hook.
  };

  Vue.prototype.$forceUpdate = function () {
    const vm = this;

```
### Line 3987-4026
```
    if (vm._isBeingDestroyed) {
      return
    }
    callHook(vm, 'beforeDestroy');
    vm._isBeingDestroyed = true;
    // remove self from parent
    const parent = vm.$parent;
    if (parent && !parent._isBeingDestroyed && !vm.$options.abstract) {
      remove(parent.$children, vm);
    }
    // teardown watchers
    if (vm._watcher) {
      vm._watcher.teardown();
    }
    let i = vm._watchers.length;
    while (i--) {
      vm._watchers[i].teardown();
    }
    // remove reference from data ob
    // frozen object may not have observer.
    if (vm._data.__ob__) {
      vm._data.__ob__.vmCount--;
    }
    // call the last hook...
    vm._isDestroyed = true;
    // invoke destroy hooks on current rendered tree
    vm.__patch__(vm._vnode, null);
    // fire destroyed hook
    callHook(vm, 'destroyed');
    // turn off all instance listeners.
    vm.$off();
    // remove __vue__ reference
    if (vm.$el) {
      vm.$el.__vue__ = null;
    }
    // release circular reference (#6759)
    if (vm.$vnode) {
      vm.$vnode.parent = null;
    }
  };

```
### Line 4077-4088
```
    updateComponent = () => {
      vm._update(vm._render(), hydrating);
    };
  }

  // we set this to vm._watcher inside the watcher's constructor
  // since the watcher's initial patch may call $forceUpdate (e.g. inside child
  // component's mounted hook), which relies on vm._watcher being already defined
  new Watcher(vm, updateComponent, noop, {
    before () {
      if (vm._isMounted && !vm._isDestroyed) {
        callHook(vm, 'beforeUpdate');

```
### Line 4089-4099
```
      }
    }
  }, true /* isRenderWatcher */);
  hydrating = false;

  // manually mounted instance, call mounted on self
  // mounted is called for render-created child components in its inserted hook
  if (vm.$vnode == null) {
    vm._isMounted = true;
    callHook(vm, 'mounted');
  }

```
### Line 4109-4134
```
) {
  {
    isUpdatingChildComponent = true;
  }

  // determine whether component has slot children
  // we need to do this before overwriting $options._renderChildren.

  // check if there are dynamic scopedSlots (hand-written or compiled but with
  // dynamic slot names). Static scoped slots compiled from template has the
  // "$stable" marker.
  const newScopedSlots = parentVnode.data.scopedSlots;
  const oldScopedSlots = vm.$scopedSlots;
  const hasDynamicScopedSlot = !!(
    (newScopedSlots && !newScopedSlots.$stable) ||
    (oldScopedSlots !== emptyObject && !oldScopedSlots.$stable) ||
    (newScopedSlots && vm.$scopedSlots.$key !== newScopedSlots.$key)
  );

  // Any static slot children from the parent may have changed during parent's
  // update. Dynamic scoped slots may also have changed. In such cases, a forced
  // update is necessary to ensure correctness.
  const needsForceUpdate = !!(
    renderChildren ||               // has new static slots
    vm.$options._renderChildren ||  // has old static slots
    hasDynamicScopedSlot

```
### Line 4140-4155
```
  if (vm._vnode) { // update child tree's parent
    vm._vnode.parent = parentVnode;
  }
  vm.$options._renderChildren = renderChildren;

  // update $attrs and $listeners hash
  // these are also reactive so they may trigger child update if the child
  // used them during render
  vm.$attrs = parentVnode.data.attrs || emptyObject;
  vm.$listeners = listeners || emptyObject;

  // update props
  if (propsData && vm.$options.props) {
    toggleObserving(false);
    const props = vm._props;
    const propKeys = vm.$options._propKeys || [];

```
### Line 4157-4176
```
      const key = propKeys[i];
      const propOptions = vm.$options.props; // wtf flow?
      props[key] = validateProp(key, propOptions, propsData, vm);
    }
    toggleObserving(true);
    // keep a copy of raw propsData
    vm.$options.propsData = propsData;
  }

  // update listeners
  listeners = listeners || emptyObject;
  const oldListeners = vm.$options._parentListeners;
  vm.$options._parentListeners = listeners;
  updateComponentListeners(vm, listeners, oldListeners);

  // resolve slots + force update if has children
  if (needsForceUpdate) {
    vm.$slots = resolveSlots(renderChildren, parentVnode.context);
    vm.$forceUpdate();
  }

```
### Line 4220-4229
```
    callHook(vm, 'deactivated');
  }
}

function callHook (vm, hook) {
  // #7573 disable dep collection when invoking lifecycle hooks
  pushTarget();
  const handlers = vm.$options[hook];
  const info = `${hook} hook`;
  if (handlers) {

```
### Line 4259-4294
```
    circular = {};
  }
  waiting = flushing = false;
}

// Async edge case #6566 requires saving the timestamp when event listeners are
// attached. However, calling performance.now() has a perf overhead especially
// if the page has thousands of event listeners. Instead, we take a timestamp
// every time the scheduler flushes and use that for all event listeners
// attached during that flush.
let currentFlushTimestamp = 0;

// Async edge case fix requires storing an event listener's attach timestamp.
let getNow = Date.now;

// Determine what event timestamp the browser is using. Annoyingly, the
// timestamp can either be hi-res (relative to page load) or low-res
// (relative to UNIX epoch), so in order to compare time we have to use the
// same timestamp type when saving the flush timestamp.
// All IE versions use low-res event timestamps, and have problematic clock
// implementations (#9632)
if (inBrowser && !isIE) {
  const performance = window.performance;
  if (
    performance &&
    typeof performance.now === 'function' &&
    getNow() > document.createEvent('Event').timeStamp
  ) {
    // if the event timestamp, although evaluated AFTER the Date.now(), is
    // smaller than it, it means the event is using a hi-res timestamp,
    // and we need to use the hi-res version for event listener timestamps as
    // well.
    getNow = () => performance.now();
  }
}


```
### Line 4298-4327
```
function flushSchedulerQueue () {
  currentFlushTimestamp = getNow();
  flushing = true;
  let watcher, id;

  // Sort queue before flush.
  // This ensures that:
  // 1. Components are updated from parent to child. (because parent is always
  //    created before the child)
  // 2. A component's user watchers are run before its render watcher (because
  //    user watchers are created before the render watcher)
  // 3. If a component is destroyed during a parent component's watcher run,
  //    its watchers can be skipped.
  queue.sort((a, b) => a.id - b.id);

  // do not cache length because more watchers might be pushed
  // as we run existing watchers
  for (index = 0; index < queue.length; index++) {
    watcher = queue[index];
    if (watcher.before) {
      watcher.before();
    }
    id = watcher.id;
    has[id] = null;
    watcher.run();
    // in dev build, check and stop circular updates.
    if (has[id] != null) {
      circular[id] = (circular[id] || 0) + 1;
      if (circular[id] > MAX_UPDATE_COUNT) {
        warn(

```
### Line 4335-4354
```
        break
      }
    }
  }

  // keep copies of post queues before resetting state
  const activatedQueue = activatedChildren.slice();
  const updatedQueue = queue.slice();

  resetSchedulerState();

  // call component updated and activated hooks
  callActivatedHooks(activatedQueue);
  callUpdatedHooks(updatedQueue);

  // devtool hook
  /* istanbul ignore if */
  if (devtools && config.devtools) {
    devtools.emit('flush');
  }

```
### Line 4368-4378
```
/**
 * Queue a kept-alive component that was activated during patch.
 * The queue will be processed after the entire tree has been patched.
 */
function queueActivatedComponent (vm) {
  // setting _inactive to false here so that a render function can
  // rely on checking whether it's in an inactive tree (e.g. router-view)
  vm._inactive = false;
  activatedChildren.push(vm);
}


```
### Line 4393-4410
```
  if (has[id] == null) {
    has[id] = true;
    if (!flushing) {
      queue.push(watcher);
    } else {
      // if already flushing, splice the watcher based on its id
      // if already past its id, it will be run next immediately.
      let i = queue.length - 1;
      while (i > index && queue[i].id > watcher.id) {
        i--;
      }
      queue.splice(i + 1, 0, watcher);
    }
    // queue the flush
    if (!waiting) {
      waiting = true;

      if (!config.async) {

```
### Line 4456-4465
```
    this.vm = vm;
    if (isRenderWatcher) {
      vm._watcher = this;
    }
    vm._watchers.push(this);
    // options
    if (options) {
      this.deep = !!options.deep;
      this.user = !!options.user;
      this.lazy = !!options.lazy;

```
### Line 4475-4484
```
    this.deps = [];
    this.newDeps = [];
    this.depIds = new _Set();
    this.newDepIds = new _Set();
    this.expression = expOrFn.toString();
    // parse expression for getter
    if (typeof expOrFn === 'function') {
      this.getter = expOrFn;
    } else {
      this.getter = parsePath(expOrFn);

```
### Line 4511-4521
```
        handleError(e, vm, `getter for watcher "${this.expression}"`);
      } else {
        throw e
      }
    } finally {
      // "touch" every property so they are all tracked as
      // dependencies for deep watching
      if (this.deep) {
        traverse(value);
      }
      popTarget();

```
### Line 4581-4596
```
  run () {
    if (this.active) {
      const value = this.get();
      if (
        value !== this.value ||
        // Deep watchers and watchers on Object/Arrays should fire even
        // when the value is the same, because the value may
        // have mutated.
        isObject(value) ||
        this.deep
      ) {
        // set new value
        const oldValue = this.value;
        this.value = value;
        if (this.user) {
          try {

```
### Line 4627-4638
```
  /**
   * Remove self from all dependencies' subscriber list.
   */
  teardown () {
    if (this.active) {
      // remove self from vm's watcher list
      // this is a somewhat expensive operation so we skip it
      // if the vm is being destroyed.
      if (!this.vm._isBeingDestroyed) {
        remove(this.vm._watchers, this);
      }
      let i = this.deps.length;

```
### Line 4680-4693
```
}

function initProps (vm, propsOptions) {
  const propsData = vm.$options.propsData || {};
  const props = vm._props = {};
  // cache prop keys so that future props updates can iterate using Array
  // instead of dynamic object key enumeration.
  const keys = vm.$options._propKeys = [];
  const isRoot = !vm.$parent;
  // root instance props should be converted
  if (!isRoot) {
    toggleObserving(false);
  }
  for (const key in propsOptions) {

```
### Line 4713-4724
```
            vm
          );
        }
      });
    }
    // static props are already proxied on the component's prototype
    // during Vue.extend(). We only need to proxy props defined at
    // instantiation here.
    if (!(key in vm)) {
      proxy(vm, `_props`, key);
    }
  }

```
### Line 4736-4745
```
      'data functions should return an object:\n' +
      'https://vuejs.org/v2/guide/components.html#data-Must-Be-a-Function',
      vm
    );
  }
  // proxy data on instance
  const keys = Object.keys(data);
  const props = vm.$options.props;
  const methods = vm.$options.methods;
  let i = keys.length;

```
### Line 4761-4775
```
      );
    } else if (!isReserved(key)) {
      proxy(vm, `_data`, key);
    }
  }
  // observe data
  observe(data, true /* asRootData */);
}

function getData (data, vm) {
  // #7573 disable dep collection when invoking data getters
  pushTarget();
  try {
    return data.call(vm, vm)
  } catch (e) {

```
### Line 4781-4792
```
}

const computedWatcherOptions = { lazy: true };

function initComputed (vm, computed) {
  // $flow-disable-line
  const watchers = vm._computedWatchers = Object.create(null);
  // computed properties are just getters during SSR
  const isSSR = isServerRendering();

  for (const key in computed) {
    const userDef = computed[key];

```
### Line 4797-4817
```
        vm
      );
    }

    if (!isSSR) {
      // create internal watcher for the computed property.
      watchers[key] = new Watcher(
        vm,
        getter || noop,
        noop,
        computedWatcherOptions
      );
    }

    // component-defined computed properties are already defined on the
    // component prototype. We only need to define computed properties defined
    // at instantiation here.
    if (!(key in vm)) {
      defineComputed(vm, key, userDef);
    } else {
      if (key in vm.$data) {

```
### Line 4930-4941
```
  }
  return vm.$watch(expOrFn, handler, options)
}

function stateMixin (Vue) {
  // flow somehow has problems with directly declared definition object
  // when using Object.defineProperty, so we have to procedurally build up
  // the object here.
  const dataDef = {};
  dataDef.get = function () { return this._data };
  const propsDef = {};
  propsDef.get = function () { return this._props };

```
### Line 4987-4996
```
let uid$3 = 0;

function initMixin (Vue) {
  Vue.prototype._init = function (options) {
    const vm = this;
    // a uid
    vm._uid = uid$3++;

    let startTag, endTag;
    /* istanbul ignore if */

```
### Line 4998-5013
```
      startTag = `vue-perf-start:${vm._uid}`;
      endTag = `vue-perf-end:${vm._uid}`;
      mark(startTag);
    }

    // a flag to avoid this being observed
    vm._isVue = true;
    // merge options
    if (options && options._isComponent) {
      // optimize internal component instantiation
      // since dynamic options merging is pretty slow, and none of the
      // internal component options needs special treatment.
      initInternalComponent(vm, options);
    } else {
      vm.$options = mergeOptions(
        resolveConstructorOptions(vm.constructor),

```
### Line 5017-5026
```
    }
    /* istanbul ignore else */
    {
      initProxy(vm);
    }
    // expose real self
    vm._self = vm;
    initLifecycle(vm);
    initEvents(vm);
    initRender(vm);

```
### Line 5043-5052
```
  };
}

function initInternalComponent (vm, options) {
  const opts = vm.$options = Object.create(vm.constructor.options);
  // doing this because it's faster than dynamic enumeration.
  const parentVnode = options._parentVnode;
  opts.parent = options.parent;
  opts._parentVnode = parentVnode;


```
### Line 5066-5080
```
  let options = Ctor.options;
  if (Ctor.super) {
    const superOptions = resolveConstructorOptions(Ctor.super);
    const cachedSuperOptions = Ctor.superOptions;
    if (superOptions !== cachedSuperOptions) {
      // super option changed,
      // need to resolve new options.
      Ctor.superOptions = superOptions;
      // check if there are any late-modified/attached options (#4976)
      const modifiedOptions = resolveModifiedOptions(Ctor);
      // update base extend options
      if (modifiedOptions) {
        extend(Ctor.extendOptions, modifiedOptions);
      }
      options = Ctor.options = mergeOptions(superOptions, Ctor.extendOptions);

```
### Line 5120-5129
```
    const installedPlugins = (this._installedPlugins || (this._installedPlugins = []));
    if (installedPlugins.indexOf(plugin) > -1) {
      return this
    }

    // additional parameters
    const args = toArray(arguments, 1);
    args.unshift(this);
    if (typeof plugin.install === 'function') {
      plugin.install.apply(plugin, args);

```
### Line 5182-5223
```
      Super.options,
      extendOptions
    );
    Sub['super'] = Super;

    // For props and computed properties, we define the proxy getters on
    // the Vue instances at extension time, on the extended prototype. This
    // avoids Object.defineProperty calls for each instance created.
    if (Sub.options.props) {
      initProps$1(Sub);
    }
    if (Sub.options.computed) {
      initComputed$1(Sub);
    }

    // allow further extension/mixin/plugin usage
    Sub.extend = Super.extend;
    Sub.mixin = Super.mixin;
    Sub.use = Super.use;

    // create asset registers, so extended classes
    // can have their private assets too.
    ASSET_TYPES.forEach(function (type) {
      Sub[type] = Super[type];
    });
    // enable recursive self-lookup
    if (name) {
      Sub.options.components[name] = Sub;
    }

    // keep a reference to the super options at extension time.
    // later at instantiation we can check if Super's options have
    // been updated.
    Sub.superOptions = Super.options;
    Sub.extendOptions = extendOptions;
    Sub.sealedOptions = extend({}, Sub.options);

    // cache constructor
    cachedCtors[SuperId] = Sub;
    return Sub
  };
}

```
### Line 5350-5385
```
  render () {
    const slot = this.$slots.default;
    const vnode = getFirstComponentChild(slot);
    const componentOptions = vnode && vnode.componentOptions;
    if (componentOptions) {
      // check pattern
      const name = getComponentName(componentOptions);
      const { include, exclude } = this;
      if (
        // not included
        (include && (!name || !matches(include, name))) ||
        // excluded
        (exclude && name && matches(exclude, name))
      ) {
        return vnode
      }

      const { cache, keys } = this;
      const key = vnode.key == null
        // same constructor may get registered as different local components
        // so cid alone is not enough (#3269)
        ? componentOptions.Ctor.cid + (componentOptions.tag ? `::${componentOptions.tag}` : '')
        : vnode.key;
      if (cache[key]) {
        vnode.componentInstance = cache[key].componentInstance;
        // make current key freshest
        remove(keys, key);
        keys.push(key);
      } else {
        cache[key] = vnode;
        keys.push(key);
        // prune oldest entry
        if (this.max && keys.length > parseInt(this.max)) {
          pruneCacheEntry(cache, keys[0], keys, this._vnode);
        }
      }

```
### Line 5395-5404
```
};

/*  */

function initGlobalAPI (Vue) {
  // config
  const configDef = {};
  configDef.get = () => config;
  {
    configDef.set = () => {

```
### Line 5407-5418
```
      );
    };
  }
  Object.defineProperty(Vue, 'config', configDef);

  // exposed util methods.
  // NOTE: these are not considered part of the public API - avoid relying on
  // them unless you are aware of the risk.
  Vue.util = {
    warn,
    extend,
    mergeOptions,

```
### Line 5421-5430
```

  Vue.set = set;
  Vue.delete = del;
  Vue.nextTick = nextTick;

  // 2.6 explicit observable API
  Vue.observable = (obj) => {
    observe(obj);
    return obj
  };

```
### Line 5432-5442
```
  Vue.options = Object.create(null);
  ASSET_TYPES.forEach(type => {
    Vue.options[type + 's'] = Object.create(null);
  });

  // this is used to identify the "base" constructor to extend all plain-object
  // components with in Weex's multi-instance scenarios.
  Vue.options._base = Vue;

  extend(Vue.options.components, builtInComponents);


```
### Line 5457-5479
```
    /* istanbul ignore next */
    return this.$vnode && this.$vnode.ssrContext
  }
});

// expose FunctionalRenderContext for ssr runtime helper installation
Object.defineProperty(Vue, 'FunctionalRenderContext', {
  value: FunctionalRenderContext
});

Vue.version = '2.6.10';

/*  */

// these are reserved for web because they are directly compiled away
// during template compilation
const isReservedAttr = makeMap('style,class');

// attributes that should be using props for binding
const acceptValue = makeMap('input,textarea,option,select,progress');
const mustUseProp = (tag, type, attr) => {
  return (
    (attr === 'value' && acceptValue(tag)) && type !== 'button' ||

```
### Line 5488-5497
```
const isValidContentEditableValue = makeMap('events,caret,typing,plaintext-only');

const convertEnumeratedValue = (key, value) => {
  return isFalsyAttrValue(value) || value === 'false'
    ? 'false'
    // allow arbitrary string value for contenteditable
    : key === 'contenteditable' && isValidContentEditableValue(value)
      ? value
      : 'true'
};

```
### Line 5619-5629
```
  'output,progress,select,textarea,' +
  'details,dialog,menu,menuitem,summary,' +
  'content,element,shadow,template,blockquote,iframe,tfoot'
);

// this map is intentionally selective, only covering SVG elements that may
// contain child elements.
const isSVG = makeMap(
  'svg,animate,circle,clippath,cursor,defs,desc,ellipse,filter,font-face,' +
  'foreignObject,g,glyph,image,line,marker,mask,missing-glyph,path,pattern,' +
  'polygon,polyline,rect,switch,symbol,text,textpath,tspan,use,view',

```
### Line 5638-5648
```

function getTagNamespace (tag) {
  if (isSVG(tag)) {
    return 'svg'
  }
  // basic support for MathML
  // note it doesn't support other MathML elements being component roots
  if (tag === 'math') {
    return 'math'
  }
}

```
### Line 5661-5670
```
  if (unknownElementCache[tag] != null) {
    return unknownElementCache[tag]
  }
  const el = document.createElement(tag);
  if (tag.indexOf('-') > -1) {
    // http://stackoverflow.com/a/28210364/1070244
    return (unknownElementCache[tag] = (
      el.constructor === window.HTMLUnknownElement ||
      el.constructor === window.HTMLElement
    ))

```
### Line 5700-5709
```
function createElement$1 (tagName, vnode) {
  const elm = document.createElement(tagName);
  if (tagName !== 'select') {
    return elm
  }
  // false or null will remove the attribute but undefined will not
  if (vnode.data && vnode.data.attrs && vnode.data.attrs.multiple !== undefined) {
    elm.setAttribute('multiple', 'multiple');
  }
  return elm

```
### Line 5801-5810
```
  } else {
    if (vnode.data.refInFor) {
      if (!Array.isArray(refs[key])) {
        refs[key] = [ref];
      } else if (refs[key].indexOf(ref) < 0) {
        // $flow-disable-line
        refs[key].push(ref);
      }
    } else {
      refs[key] = ref;

```
### Line 5892-5901
```
    return remove$$1
  }

  function removeNode (el) {
    const parent = nodeOps.parentNode(el);
    // element may have already been removed due to v-html / v-text
    if (isDef(parent)) {
      nodeOps.removeChild(parent, el);
    }
  }

```
### Line 5926-5939
```
    nested,
    ownerArray,
    index
  ) {
    if (isDef(vnode.elm) && isDef(ownerArray)) {
      // This vnode was used in a previous render!
      // now it's used as a new node, overwriting its elm would cause
      // potential patch errors down the road when it's used as an insertion
      // reference node. Instead, we clone the node on-demand before creating
      // associated DOM element for it.
      vnode = ownerArray[index] = cloneVNode(vnode);
    }

    vnode.isRootInsert = !nested; // for transition enter check

```
### Line 5990-6002
```
    if (isDef(i)) {
      const isReactivated = isDef(vnode.componentInstance) && i.keepAlive;
      if (isDef(i = i.hook) && isDef(i = i.init)) {
        i(vnode, false /* hydrating */);
      }
      // after calling the init hook, if the vnode is a child component
      // it should've created a child instance and mounted it. the child
      // component also has set the placeholder vnode's elm.
      // in that case we can just return the element and be done.
      if (isDef(vnode.componentInstance)) {
        initComponent(vnode, insertedVnodeQueue);
        insert(parentElm, vnode.elm, refElm);
        if (isTrue(isReactivated)) {

```
### Line 6015-6037
```
    vnode.elm = vnode.componentInstance.$el;
    if (isPatchable(vnode)) {
      invokeCreateHooks(vnode, insertedVnodeQueue);
      setScope(vnode);
    } else {
      // empty component root.
      // skip all element-related modules except for ref (#3455)
      registerRef(vnode);
      // make sure to invoke the insert hook
      insertedVnodeQueue.push(vnode);
    }
  }

  function reactivateComponent (vnode, insertedVnodeQueue, parentElm, refElm) {
    let i;
    // hack for #4339: a reactivated component with inner transition
    // does not trigger because the inner node's created hooks are not called
    // again. It's not ideal to involve module-specific logic in here but
    // there doesn't seem to be a better way to do it.
    let innerNode = vnode;
    while (innerNode.componentInstance) {
      innerNode = innerNode.componentInstance._vnode;
      if (isDef(i = innerNode.data) && isDef(i = i.transition)) {

```
### Line 6040-6050
```
        }
        insertedVnodeQueue.push(innerNode);
        break
      }
    }
    // unlike a newly created component,
    // a reactivated keep-alive component doesn't insert itself
    insert(parentElm, vnode.elm, refElm);
  }

  function insert (parent, elm, ref$$1) {

```
### Line 6088-6099
```
      if (isDef(i.create)) i.create(emptyNode, vnode);
      if (isDef(i.insert)) insertedVnodeQueue.push(vnode);
    }
  }

  // set scope id attribute for scoped CSS.
  // this is implemented as a special case to avoid the overhead
  // of going through the normal attribute patching process.
  function setScope (vnode) {
    let i;
    if (isDef(i = vnode.fnScopeId)) {
      nodeOps.setStyleScope(vnode.elm, i);

```
### Line 6104-6113
```
          nodeOps.setStyleScope(vnode.elm, i);
        }
        ancestor = ancestor.parent;
      }
    }
    // for slot content they should also get the scopeId from the host instance.
    if (isDef(i = activeInstance) &&
      i !== vnode.context &&
      i !== vnode.fnContext &&
      isDef(i = i.$options._scopeId)

```
### Line 6153-6169
```
  function removeAndInvokeRemoveHook (vnode, rm) {
    if (isDef(rm) || isDef(vnode.data)) {
      let i;
      const listeners = cbs.remove.length + 1;
      if (isDef(rm)) {
        // we have a recursively passed down rm callback
        // increase the listeners count
        rm.listeners += listeners;
      } else {
        // directly removing
        rm = createRmCb(vnode.elm, listeners);
      }
      // recursively invoke hooks on child component root node
      if (isDef(i = vnode.componentInstance) && isDef(i = i._vnode) && isDef(i.data)) {
        removeAndInvokeRemoveHook(i, rm);
      }
      for (i = 0; i < cbs.remove.length; ++i) {

```
### Line 6188-6199
```
    let newEndIdx = newCh.length - 1;
    let newStartVnode = newCh[0];
    let newEndVnode = newCh[newEndIdx];
    let oldKeyToIdx, idxInOld, vnodeToMove, refElm;

    // removeOnly is a special flag used only by <transition-group>
    // to ensure removed elements stay in correct relative positions
    // during leaving transitions
    const canMove = !removeOnly;

    {
      checkDuplicateKeys(newCh);

```
### Line 6234-6243
```
          if (sameVnode(vnodeToMove, newStartVnode)) {
            patchVnode(vnodeToMove, newStartVnode, insertedVnodeQueue, newCh, newStartIdx);
            oldCh[idxInOld] = undefined;
            canMove && nodeOps.insertBefore(parentElm, vnodeToMove.elm, oldStartVnode.elm);
          } else {
            // same key but different element. treat as new element
            createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, false, newCh, newStartIdx);
          }
        }
        newStartVnode = newCh[++newStartIdx];

```
### Line 6287-6296
```
    if (oldVnode === vnode) {
      return
    }

    if (isDef(vnode.elm) && isDef(ownerArray)) {
      // clone reused vnode
      vnode = ownerArray[index] = cloneVNode(vnode);
    }

    const elm = vnode.elm = oldVnode.elm;

```
### Line 6302-6314
```
        vnode.isAsyncPlaceholder = true;
      }
      return
    }

    // reuse element for static trees.
    // note we only do this if the vnode is cloned -
    // if the new node is not cloned it means the render functions have been
    // reset by the hot-reload-api and we need to do a proper re-render.
    if (isTrue(vnode.isStatic) &&
      isTrue(oldVnode.isStatic) &&
      vnode.key === oldVnode.key &&
      (isTrue(vnode.isCloned) || isTrue(vnode.isOnce))

```
### Line 6350-6360
```
      if (isDef(i = data.hook) && isDef(i = i.postpatch)) i(oldVnode, vnode);
    }
  }

  function invokeInsertHook (vnode, queue, initial) {
    // delay insert hooks for component root nodes, invoke them after the
    // element is really inserted
    if (isTrue(initial) && isDef(vnode.parent)) {
      vnode.parent.data.pendingInsert = queue;
    } else {
      for (let i = 0; i < queue.length; ++i) {

```
### Line 6362-6377
```
      }
    }
  }

  let hydrationBailed = false;
  // list of modules that can skip create hook during hydration because they
  // are already rendered on the client or has no need for initialization
  // Note: style is excluded because it relies on initial clone for future
  // deep updates (#7063).
  const isRenderedModule = makeMap('attrs,class,staticClass,staticStyle,key');

  // Note: this is a browser-only function so we can assume elms are DOM nodes.
  function hydrate (elm, vnode, insertedVnodeQueue, inVPre) {
    let i;
    const { tag, data, children } = vnode;
    inVPre = inVPre || (data && data.pre);

```
### Line 6379-6408
```

    if (isTrue(vnode.isComment) && isDef(vnode.asyncFactory)) {
      vnode.isAsyncPlaceholder = true;
      return true
    }
    // assert node match
    {
      if (!assertNodeMatch(elm, vnode, inVPre)) {
        return false
      }
    }
    if (isDef(data)) {
      if (isDef(i = data.hook) && isDef(i = i.init)) i(vnode, true /* hydrating */);
      if (isDef(i = vnode.componentInstance)) {
        // child component. it should have hydrated its own tree.
        initComponent(vnode, insertedVnodeQueue);
        return true
      }
    }
    if (isDef(tag)) {
      if (isDef(children)) {
        // empty element, allow client to pick up and populate children
        if (!elm.hasChildNodes()) {
          createChildren(vnode, children, insertedVnodeQueue);
        } else {
          // v-html and domProps: innerHTML
          if (isDef(i = data) && isDef(i = i.domProps) && isDef(i = i.innerHTML)) {
            if (i !== elm.innerHTML) {
              /* istanbul ignore if */
              if (typeof console !== 'undefined' &&

```
### Line 6414-6423
```
                console.warn('client innerHTML: ', elm.innerHTML);
              }
              return false
            }
          } else {
            // iterate and compare children lists
            let childrenMatch = true;
            let childNode = elm.firstChild;
            for (let i = 0; i < children.length; i++) {
              if (!childNode || !hydrate(childNode, children[i], insertedVnodeQueue, inVPre)) {

```
### Line 6424-6434
```
                childrenMatch = false;
                break
              }
              childNode = childNode.nextSibling;
            }
            // if childNode is not null, it means the actual childNodes list is
            // longer than the virtual children list.
            if (!childrenMatch || childNode) {
              /* istanbul ignore if */
              if (typeof console !== 'undefined' &&
                !hydrationBailed

```
### Line 6450-6459
```
            invokeCreateHooks(vnode, insertedVnodeQueue);
            break
          }
        }
        if (!fullInvoke && data['class']) {
          // ensure collecting deps for deep class bindings for future updates
          traverse(data['class']);
        }
      }
    } else if (elm.data !== vnode.text) {

```
### Line 6481-6502
```

    let isInitialPatch = false;
    const insertedVnodeQueue = [];

    if (isUndef(oldVnode)) {
      // empty mount (likely as component), create new root element
      isInitialPatch = true;
      createElm(vnode, insertedVnodeQueue);
    } else {
      const isRealElement = isDef(oldVnode.nodeType);
      if (!isRealElement && sameVnode(oldVnode, vnode)) {
        // patch existing root node
        patchVnode(oldVnode, vnode, insertedVnodeQueue, null, null, removeOnly);
      } else {
        if (isRealElement) {
          // mounting to a real element
          // check if this is server-rendered content and if we can perform
          // a successful hydration.
          if (oldVnode.nodeType === 1 && oldVnode.hasAttribute(SSR_ATTR)) {
            oldVnode.removeAttribute(SSR_ATTR);
            hydrating = true;
          }

```
### Line 6512-6541
```
                '<p>, or missing <tbody>. Bailing hydration and performing ' +
                'full client-side render.'
              );
            }
          }
          // either not server-rendered, or hydration failed.
          // create an empty node and replace it
          oldVnode = emptyNodeAt(oldVnode);
        }

        // replacing existing element
        const oldElm = oldVnode.elm;
        const parentElm = nodeOps.parentNode(oldElm);

        // create new node
        createElm(
          vnode,
          insertedVnodeQueue,
          // extremely rare edge case: do not insert if old element is in a
          // leaving transition. Only happens when combining transition +
          // keep-alive + HOCs. (#4590)
          oldElm._leaveCb ? null : parentElm,
          nodeOps.nextSibling(oldElm)
        );

        // update parent placeholder node element, recursively
        if (isDef(vnode.parent)) {
          let ancestor = vnode.parent;
          const patchable = isPatchable(vnode);
          while (ancestor) {

```
### Line 6545-6559
```
            ancestor.elm = vnode.elm;
            if (patchable) {
              for (let i = 0; i < cbs.create.length; ++i) {
                cbs.create[i](emptyNode, ancestor);
              }
              // #6513
              // invoke insert hooks that may have been merged by create hooks.
              // e.g. for directives that uses the "inserted" hook.
              const insert = ancestor.data.hook.insert;
              if (insert.merged) {
                // start at index 1 to avoid re-invoking component mounted hook
                for (let i = 1; i < insert.fns.length; i++) {
                  insert.fns[i]();
                }
              }

```
### Line 6562-6571
```
            }
            ancestor = ancestor.parent;
          }
        }

        // destroy old node
        if (isDef(parentElm)) {
          removeVnodes(parentElm, [oldVnode], 0, 0);
        } else if (isDef(oldVnode.tag)) {
          invokeDestroyHook(oldVnode);

```
### Line 6606-6621
```
  let key, oldDir, dir;
  for (key in newDirs) {
    oldDir = oldDirs[key];
    dir = newDirs[key];
    if (!oldDir) {
      // new directive, bind
      callHook$1(dir, 'bind', vnode, oldVnode);
      if (dir.def && dir.def.inserted) {
        dirsWithInsert.push(dir);
      }
    } else {
      // existing directive, update
      dir.oldValue = oldDir.value;
      dir.oldArg = oldDir.arg;
      callHook$1(dir, 'update', vnode, oldVnode);
      if (dir.def && dir.def.componentUpdated) {

```
### Line 6646-6655
```
  }

  if (!isCreate) {
    for (key in oldDirs) {
      if (!newDirs[key]) {
        // no longer present, unbind
        callHook$1(oldDirs[key], 'unbind', oldVnode, oldVnode, isDestroy);
      }
    }
  }

```
### Line 6661-6683
```
  dirs,
  vm
) {
  const res = Object.create(null);
  if (!dirs) {
    // $flow-disable-line
    return res
  }
  let i, dir;
  for (i = 0; i < dirs.length; i++) {
    dir = dirs[i];
    if (!dir.modifiers) {
      // $flow-disable-line
      dir.modifiers = emptyModifiers;
    }
    res[getRawDirName(dir)] = dir;
    dir.def = resolveAsset(vm.$options, 'directives', dir.name, true);
  }
  // $flow-disable-line
  return res
}

function getRawDirName (dir) {

```
### Line 6712-6721
```
  }
  let key, cur, old;
  const elm = vnode.elm;
  const oldAttrs = oldVnode.data.attrs || {};
  let attrs = vnode.data.attrs || {};
  // clone observed objects, as the user probably wants to mutate it
  if (isDef(attrs.__ob__)) {
    attrs = vnode.data.attrs = extend({}, attrs);
  }


```
### Line 6724-6734
```
    old = oldAttrs[key];
    if (old !== cur) {
      setAttr(elm, key, cur);
    }
  }
  // #4391: in IE9, setting type can reset value for input[type=radio]
  // #6666: IE/Edge forces progress value down to 1 before setting a max
  /* istanbul ignore if */
  if ((isIE || isEdge) && attrs.value !== oldAttrs.value) {
    setAttr(elm, 'value', attrs.value);
  }

```
### Line 6745-6760
```

function setAttr (el, key, value) {
  if (el.tagName.indexOf('-') > -1) {
    baseSetAttr(el, key, value);
  } else if (isBooleanAttr(key)) {
    // set attribute for blank value
    // e.g. <option disabled>Select one</option>
    if (isFalsyAttrValue(value)) {
      el.removeAttribute(key);
    } else {
      // technically allowfullscreen is a boolean attribute for <iframe>,
      // but Flash expects a value of "true" when used on <embed> tag
      value = key === 'allowfullscreen' && el.tagName === 'EMBED'
        ? 'true'
        : key;
      el.setAttribute(key, value);

```
### Line 6774-6785
```

function baseSetAttr (el, key, value) {
  if (isFalsyAttrValue(value)) {
    el.removeAttribute(key);
  } else {
    // #7138: IE10 & 11 fires input event when setting placeholder on
    // <textarea>... block the first input event and remove the blocker
    // immediately.
    /* istanbul ignore if */
    if (
      isIE && !isIE9 &&
      el.tagName === 'TEXTAREA' &&

```
### Line 6788-6797
```
      const blocker = e => {
        e.stopImmediatePropagation();
        el.removeEventListener('input', blocker);
      };
      el.addEventListener('input', blocker);
      // $flow-disable-line
      el.__ieph = true; /* IE placeholder patched */
    }
    el.setAttribute(key, value);
  }

```
### Line 6820-6835
```
    return
  }

  let cls = genClassForVnode(vnode);

  // handle transition classes
  const transitionClass = el._transitionClasses;
  if (isDef(transitionClass)) {
    cls = concat(cls, stringifyClass(transitionClass));
  }

  // set the class
  if (cls !== el._prevClass) {
    el.setAttribute('class', cls);
    el._prevClass = cls;
  }

```
### Line 6871-6880
```
      exp.charCodeAt(i + 1) !== 0x7C &&
      exp.charCodeAt(i - 1) !== 0x7C &&
      !curly && !square && !paren
    ) {
      if (expression === undefined) {
        // first filter, end of expression
        lastFilterIndex = i + 1;
        expression = exp.slice(0, i).trim();
      } else {
        pushFilter();

```
### Line 6892-6901
```
        case 0x7D: curly--; break                 // }
      }
      if (c === 0x2f) { // /
        let j = i - 1;
        let p;
        // find first non-whitespace prev char
        for (; j >= 0; j--) {
          p = exp.charAt(j);
          if (p !== ' ') break
        }

```
### Line 6927-6936
```
}

function wrapFilter (exp, filter) {
  const i = filter.indexOf('(');
  if (i < 0) {
    // _f: resolveFilter
    return `_f("${filter}")(${exp})`
  } else {
    const name = filter.slice(0, i);
    const args = filter.slice(i + 1);

```
### Line 6968-6977
```
    : (el.attrs || (el.attrs = []));
  attrs.push(rangeSetItem({ name, value, dynamic }, range));
  el.plain = false;
}

// add a raw attr (use this in preTransforms)
function addRawAttr (el, name, value, range) {
  el.attrsMap[name] = value;
  el.attrsList.push(rangeSetItem({ name, value }, range));
}

```
### Line 7012-7021
```
  warn,
  range,
  dynamic
) {
  modifiers = modifiers || emptyObject;
  // warn prevent and passive modifier
  /* istanbul ignore if */
  if (
    warn &&
    modifiers.prevent && modifiers.passive

```
### Line 7025-7036
```
      'Passive handler can\'t prevent default event.',
      range
    );
  }

  // normalize click.right and click.middle since they don't actually fire
  // this is technically browser-specific, but at least for now browsers are
  // the only target envs that have right/middle clicks.
  if (modifiers.right) {
    if (dynamic) {
      name = `(${name})==='click'?'contextmenu':(${name})`;
    } else if (name === 'click') {

```
### Line 7043-7052
```
    } else if (name === 'click') {
      name = 'mouseup';
    }
  }

  // check capture modifier
  if (modifiers.capture) {
    delete modifiers.capture;
    name = prependModifierMarker('!', name, dynamic);
  }

```
### Line 7111-7123
```
      return JSON.stringify(staticValue)
    }
  }
}

// note: this only removes the attr from the Array (attrsList) so that it
// doesn't get processed by processAttrs.
// By default it does NOT remove it from the map (attrsMap) because the map is
// needed during codegen.
function getAndRemoveAttr (
  el,
  name,
  removeFromMap

```
### Line 7232-7242
```
let len, str, chr, index$1, expressionPos, expressionEndPos;



function parseModel (val) {
  // Fix https://github.com/vuejs/vue/pull/7730
  // allow v-model="obj.val " (trailing whitespace)
  val = val.trim();
  len = val.length;

  if (val.indexOf('[') < 0 || val.lastIndexOf(']') < len - 1) {

```
### Line 7315-7325
```

/*  */

let warn$1;

// in some cases, the event used has to be determined at runtime
// so we used some reserved tokens during compile.
const RANGE_TOKEN = '__r';
const CHECKBOX_RADIO_TOKEN = '__c';

function model (

```
### Line 7332-7342
```
  const modifiers = dir.modifiers;
  const tag = el.tag;
  const type = el.attrsMap.type;

  {
    // inputs with type="file" are read only and setting the input's
    // value will throw an error.
    if (tag === 'input' && type === 'file') {
      warn$1(
        `<${el.tag} v-model="${value}" type="file">:\n` +
        `File inputs are read only. Use a v-on:change listener instead.`,

```
### Line 7345-7354
```
    }
  }

  if (el.component) {
    genComponentModel(el, value, modifiers);
    // component v-model doesn't need extra runtime
    return false
  } else if (tag === 'select') {
    genSelect(el, value, modifiers);
  } else if (tag === 'input' && type === 'checkbox') {

```
### Line 7357-7366
```
    genRadioModel(el, value, modifiers);
  } else if (tag === 'input' || tag === 'textarea') {
    genDefaultModel(el, value, modifiers);
  } else if (!config.isReservedTag(tag)) {
    genComponentModel(el, value, modifiers);
    // component v-model doesn't need extra runtime
    return false
  } else {
    warn$1(
      `<${el.tag} v-model="${value}">: ` +

```
### Line 7369-7378
```
      'wrap a library dedicated for that purpose inside a custom component.',
      el.rawAttrsMap['v-model']
    );
  }

  // ensure runtime directive metadata
  return true
}

function genCheckboxModel (

```
### Line 7440-7450
```
  value,
  modifiers
) {
  const type = el.attrsMap.type;

  // warn if v-bind:value conflicts with v-model
  // except for inputs with v-bind:type
  {
    const value = el.attrsMap['v-bind:value'] || el.attrsMap[':value'];
    const typeBinding = el.attrsMap['v-bind:type'] || el.attrsMap[':type'];
    if (value && !typeBinding) {

```
### Line 7485-7507
```
  }
}

/*  */

// normalize v-model event tokens that can only be determined at runtime.
// it's important to place the event as the first in the array because
// the whole point is ensuring the v-model callback gets called before
// user-attached handlers.
function normalizeEvents (on) {
  /* istanbul ignore if */
  if (isDef(on[RANGE_TOKEN])) {
    // IE input[type=range] only supports `change` event
    const event = isIE ? 'change' : 'input';
    on[event] = [].concat(on[RANGE_TOKEN], on[event] || []);
    delete on[RANGE_TOKEN];
  }
  // This was originally intended to fix #4521 but no longer necessary
  // after 2.5. Keeping it for backwards compat with generated code from < 2.4
  /* istanbul ignore if */
  if (isDef(on[CHECKBOX_RADIO_TOKEN])) {
    on.change = [].concat(on[CHECKBOX_RADIO_TOKEN], on.change || []);
    delete on[CHECKBOX_RADIO_TOKEN];

```
### Line 7518-7561
```
      remove$2(event, onceHandler, capture, _target);
    }
  }
}

// #9446: Firefox <= 53 (in particular, ESR 52) has incorrect Event.timeStamp
// implementation and does not fire microtasks in between event propagation, so
// safe to exclude.
const useMicrotaskFix = isUsingMicroTask && !(isFF && Number(isFF[1]) <= 53);

function add$1 (
  name,
  handler,
  capture,
  passive
) {
  // async edge case #6566: inner click event triggers patch, event handler
  // attached to outer element during patch, and triggered again. This
  // happens because browsers fire microtask ticks between event propagation.
  // the solution is simple: we save the timestamp when a handler is attached,
  // and the handler would only fire if the event passed to it was fired
  // AFTER it was attached.
  if (useMicrotaskFix) {
    const attachedTimestamp = currentFlushTimestamp;
    const original = handler;
    handler = original._wrapper = function (e) {
      if (
        // no bubbling, should always fire.
        // this is just a safety net in case event.timeStamp is unreliable in
        // certain weird environments...
        e.target === e.currentTarget ||
        // event is fired after handler attachment
        e.timeStamp >= attachedTimestamp ||
        // bail for environments that have buggy event.timeStamp implementations
        // #9462 iOS 9 bug: event.timeStamp is 0 after history.pushState
        // #9681 QtWebEngine event.timeStamp is negative value
        e.timeStamp <= 0 ||
        // #9448 bail if event is fired in another document in a multi-page
        // electron/nw.js app, since event.timeStamp will be using a different
        // starting reference
        e.target.ownerDocument !== document
      ) {
        return original.apply(this, arguments)
      }

```
### Line 7610-7619
```
  }
  let key, cur;
  const elm = vnode.elm;
  const oldProps = oldVnode.data.domProps || {};
  let props = vnode.data.domProps || {};
  // clone observed objects, as the user probably wants to mutate it
  if (isDef(props.__ob__)) {
    props = vnode.data.domProps = extend({}, props);
  }


```
### Line 7623-7655
```
    }
  }

  for (key in props) {
    cur = props[key];
    // ignore children if the node has textContent or innerHTML,
    // as these will throw away existing DOM nodes and cause removal errors
    // on subsequent patches (#3360)
    if (key === 'textContent' || key === 'innerHTML') {
      if (vnode.children) vnode.children.length = 0;
      if (cur === oldProps[key]) continue
      // #6601 work around Chrome version <= 55 bug where single textNode
      // replaced by innerHTML/textContent retains its parentNode property
      if (elm.childNodes.length === 1) {
        elm.removeChild(elm.childNodes[0]);
      }
    }

    if (key === 'value' && elm.tagName !== 'PROGRESS') {
      // store value as _value as well since
      // non-string values will be stringified
      elm._value = cur;
      // avoid resetting cursor position when value is the same
      const strCur = isUndef(cur) ? '' : String(cur);
      if (shouldUpdateValue(elm, strCur)) {
        elm.value = strCur;
      }
    } else if (key === 'innerHTML' && isSVG(elm.tagName) && isUndef(elm.innerHTML)) {
      // IE doesn't support innerHTML for SVG elements
      svgContainer = svgContainer || document.createElement('div');
      svgContainer.innerHTML = `<svg>${cur}</svg>`;
      const svg = svgContainer.firstChild;
      while (elm.firstChild) {

```
### Line 7657-7681
```
      }
      while (svg.firstChild) {
        elm.appendChild(svg.firstChild);
      }
    } else if (
      // skip the update if old and new VDOM state is the same.
      // `value` is handled separately because the DOM value may be temporarily
      // out of sync with VDOM state due to focus, composition and modifiers.
      // This  #4521 by skipping the unnecesarry `checked` update.
      cur !== oldProps[key]
    ) {
      // some property updates can throw
      // e.g. `value` on <progress> w/ non-finite value
      try {
        elm[key] = cur;
      } catch (e) {}
    }
  }
}

// check platforms/web/util/attrs.js acceptValue


function shouldUpdateValue (elm, checkVal) {
  return (!elm.composing && (

```
### Line 7684-7697
```
    isDirtyWithModifiers(elm, checkVal)
  ))
}

function isNotInFocusAndDirty (elm, checkVal) {
  // return true when textbox (.number and .trim) loses focus and its value is
  // not equal to the updated value
  let notInFocus = true;
  // #6157
  // work around IE bug when accessing document.activeElement in an iframe
  try { notInFocus = document.activeElement !== elm; } catch (e) {}
  return notInFocus && elm.value !== checkVal
}


```
### Line 7727-7746
```
    }
  });
  return res
});

// merge static and dynamic style data on the same vnode
function normalizeStyleData (data) {
  const style = normalizeStyleBinding(data.style);
  // static style is pre-processed into an object during compilation
  // and is always a fresh object, so it's safe to merge into it
  return data.staticStyle
    ? extend(data.staticStyle, style)
    : style
}

// normalize possible array / string values into Object
function normalizeStyleBinding (bindingStyle) {
  if (Array.isArray(bindingStyle)) {
    return toObject(bindingStyle)
  }

```
### Line 7795-7806
```
  } else if (importantRE.test(val)) {
    el.style.setProperty(hyphenate(name), val.replace(importantRE, ''), 'important');
  } else {
    const normalizedName = normalize(name);
    if (Array.isArray(val)) {
      // Support values array created by autoprefixer, e.g.
      // {display: ["-webkit-box", "-ms-flexbox", "flex"]}
      // Set them one by one, and the browser will only set those it can recognize
      for (let i = 0, len = val.length; i < len; i++) {
        el.style[normalizedName] = val[i];
      }
    } else {

```
### Line 7840-7856
```
  let cur, name;
  const el = vnode.elm;
  const oldStaticStyle = oldData.staticStyle;
  const oldStyleBinding = oldData.normalizedStyle || oldData.style || {};

  // if static style exists, stylebinding already merged into it when doing normalizeStyleData
  const oldStyle = oldStaticStyle || oldStyleBinding;

  const style = normalizeStyleBinding(vnode.data.style) || {};

  // store normalized style under a different key for next diff
  // make sure to clone it if it's reactive, since the user likely wants
  // to mutate it.
  vnode.data.normalizedStyle = isDef(style.__ob__)
    ? extend({}, style)
    : style;


```
### Line 7862-7871
```
    }
  }
  for (name in newStyle) {
    cur = newStyle[name];
    if (cur !== oldStyle[name]) {
      // ie9 setting to null has no effect, must use empty string
      setProp(el, name, cur == null ? '' : cur);
    }
  }
}

```
### Line 7971-7980
```

const hasTransition = inBrowser && !isIE9;
const TRANSITION = 'transition';
const ANIMATION = 'animation';

// Transition property/event sniffing
let transitionProp = 'transition';
let transitionEndEvent = 'transitionend';
let animationProp = 'animation';
let animationEndEvent = 'animationend';

```
### Line 7992-8001
```
    animationProp = 'WebkitAnimation';
    animationEndEvent = 'webkitAnimationEnd';
  }
}

// binding to window is necessary to make hot reload work in IE in strict mode
const raf = inBrowser
  ? window.requestAnimationFrame
    ? window.requestAnimationFrame.bind(window)
    : setTimeout

```
### Line 8052-8061
```

const transformRE = /\b(transform|all)(,|$)/;

function getTransitionInfo (el, expectedType) {
  const styles = window.getComputedStyle(el);
  // JSDOM may return undefined for transition properties
  const transitionDelays = (styles[transitionProp + 'Delay'] || '').split(', ');
  const transitionDurations = (styles[transitionProp + 'Duration'] || '').split(', ');
  const transitionTimeout = getTimeout(transitionDelays, transitionDurations);
  const animationDelays = (styles[animationProp + 'Delay'] || '').split(', ');

```
### Line 8111-8123
```
  return Math.max.apply(null, durations.map((d, i) => {
    return toMs(d) + toMs(delays[i])
  }))
}

// Old versions of Chromium (below 61.0.3163.100) formats floating pointer numbers
// in a locale-dependent way, using a comma instead of a dot.
// If comma is not replaced with a dot, the input will be rounded down (i.e. acting
// as a floor function) causing unexpected behaviors
function toMs (s) {
  return Number(s.slice(0, -1).replace(',', '.')) * 1000
}


```
### Line 8124-8133
```
/*  */

function enter (vnode, toggleDisplay) {
  const el = vnode.elm;

  // call leave callback now
  if (isDef(el._leaveCb)) {
    el._leaveCb.cancelled = true;
    el._leaveCb();
  }

```
### Line 8160-8172
```
    afterAppear,
    appearCancelled,
    duration
  } = data;

  // activeInstance will always be the <transition> component managing this
  // transition. One edge case to check is when the <transition> is placed
  // as the root node of a child component. In that case we need to check
  // <transition>'s parent for appear check.
  let context = activeInstance;
  let transitionNode = activeInstance.$vnode;
  while (transitionNode && transitionNode.parent) {
    context = transitionNode.context;

```
### Line 8230-8239
```
    }
    el._enterCb = null;
  });

  if (!vnode.data.show) {
    // remove pending leave element on enter by injecting an insert hook
    mergeVNodeHook(vnode, 'insert', () => {
      const parent = el.parentNode;
      const pendingNode = parent && parent._pending && parent._pending[vnode.key];
      if (pendingNode &&

```
### Line 8244-8253
```
      }
      enterHook && enterHook(el, cb);
    });
  }

  // start enter transition
  beforeEnterHook && beforeEnterHook(el);
  if (expectsCSS) {
    addTransitionClass(el, startClass);
    addTransitionClass(el, activeClass);

```
### Line 8277-8286
```
}

function leave (vnode, rm) {
  const el = vnode.elm;

  // call enter callback now
  if (isDef(el._enterCb)) {
    el._enterCb.cancelled = true;
    el._enterCb();
  }

```
### Line 8347-8360
```
  } else {
    performLeave();
  }

  function performLeave () {
    // the delayed leave may have already been cancelled
    if (cb.cancelled) {
      return
    }
    // record leaving element
    if (!vnode.data.show && el.parentNode) {
      (el.parentNode._pending || (el.parentNode._pending = {}))[(vnode.key)] = vnode;
    }
    beforeLeave && beforeLeave(el);

```
### Line 8380-8389
```
      cb();
    }
  }
}

// only used in dev mode
function checkDuration (val, name, vnode) {
  if (typeof val !== 'number') {
    warn(
      `<transition> explicit ${name} duration is not a valid number - ` +

```
### Line 8413-8422
```
  if (isUndef(fn)) {
    return false
  }
  const invokerFns = fn.fns;
  if (isDef(invokerFns)) {
    // invoker
    return getHookArgumentsLength(
      Array.isArray(invokerFns)
        ? invokerFns[0]
        : invokerFns

```
### Line 8454-8464
```
  transition
];

/*  */

// the directive module should be applied last, after all
// built-in modules have been applied.
const modules = platformModules.concat(baseModules);

const patch = createPatchFunction({ nodeOps, modules });


```
### Line 8467-8476
```
 * properties to Elements.
 */

/* istanbul ignore if */
if (isIE9) {
  // http://www.matts411.com/post/internet-explorer-9-oninput/
  document.addEventListener('selectionchange', () => {
    const el = document.activeElement;
    if (el && el.vmodel) {
      trigger(el, 'input');

```
### Line 8479-8488
```
}

const directive = {
  inserted (el, binding, vnode, oldVnode) {
    if (vnode.tag === 'select') {
      // #6903
      if (oldVnode.elm && !oldVnode.elm._vOptions) {
        mergeVNodeHook(vnode, 'postpatch', () => {
          directive.componentUpdated(el, binding, vnode);
        });

```
### Line 8493-8505
```
    } else if (vnode.tag === 'textarea' || isTextInputType(el.type)) {
      el._vModifiers = binding.modifiers;
      if (!binding.modifiers.lazy) {
        el.addEventListener('compositionstart', onCompositionStart);
        el.addEventListener('compositionend', onCompositionEnd);
        // Safari < 10.2 & UIWebView doesn't fire compositionend when
        // switching focus before confirming composition choice
        // this also fixes the issue where some browsers e.g. iOS Chrome
        // fires "change" instead of "input" on autocomplete.
        el.addEventListener('change', onCompositionEnd);
        /* istanbul ignore if */
        if (isIE9) {
          el.vmodel = true;

```
### Line 8509-8526
```
  },

  componentUpdated (el, binding, vnode) {
    if (vnode.tag === 'select') {
      setSelected(el, binding, vnode.context);
      // in case the options rendered by v-for have changed,
      // it's possible that the value is out-of-sync with the rendered options.
      // detect such cases and filter out values that no longer has a matching
      // option in the DOM.
      const prevOptions = el._vOptions;
      const curOptions = el._vOptions = [].map.call(el.options, getValue);
      if (curOptions.some((o, i) => !looseEqual(o, prevOptions[i]))) {
        // trigger change event if
        // no matching option found for at least one value
        const needReset = el.multiple
          ? binding.value.some(v => hasNoMatchingOption(v, curOptions))
          : binding.value !== binding.oldValue && hasNoMatchingOption(binding.value, curOptions);
        if (needReset) {

```
### Line 8589-8598
```
function onCompositionStart (e) {
  e.target.composing = true;
}

function onCompositionEnd (e) {
  // prevent triggering an input event for no reason
  if (!e.target.composing) return
  e.target.composing = false;
  trigger(e.target, 'input');
}

```
### Line 8603-8612
```
  el.dispatchEvent(e);
}

/*  */

// recursively search for possible transition defined inside the component root
function locateNode (vnode) {
  return vnode.componentInstance && (!vnode.data || !vnode.data.transition)
    ? locateNode(vnode.componentInstance._vnode)
    : vnode

```
### Line 8685-8695
```
  appearActiveClass: String,
  appearToClass: String,
  duration: [Number, String, Object]
};

// in case the child is also an abstract component, e.g. <keep-alive>
// we want to recursively retrieve the real component to be rendered
function getRealChild (vnode) {
  const compOptions = vnode && vnode.componentOptions;
  if (compOptions && compOptions.Ctor.options.abstract) {
    return getRealChild(getFirstComponentChild(compOptions.children))

```
### Line 8699-8713
```
}

function extractTransitionData (comp) {
  const data = {};
  const options = comp.$options;
  // props
  for (const key in options.propsData) {
    data[key] = comp[key];
  }
  // events.
  // extract listeners and pass them directly to the transition methods
  const listeners = options._parentListeners;
  for (const key in listeners) {
    data[camelize(key)] = listeners[key];
  }

```
### Line 8747-8763
```
    let children = this.$slots.default;
    if (!children) {
      return
    }

    // filter out text nodes (possible whitespaces)
    children = children.filter(isNotTextNode);
    /* istanbul ignore if */
    if (!children.length) {
      return
    }

    // warn multiple elements
    if (children.length > 1) {
      warn(
        '<transition> can only be used on a single element. Use ' +
        '<transition-group> for lists.',

```
### Line 8765-8774
```
      );
    }

    const mode = this.mode;

    // warn invalid mode
    if (mode && mode !== 'in-out' && mode !== 'out-in'
    ) {
      warn(
        'invalid <transition> mode: ' + mode,

```
### Line 8776-8792
```
      );
    }

    const rawChild = children[0];

    // if this is a component root node and the component's
    // parent container node also has transition, skip.
    if (hasParentTransition(this.$vnode)) {
      return rawChild
    }

    // apply transition data to child
    // use getRealChild() to ignore abstract components e.g. keep-alive
    const child = getRealChild(rawChild);
    /* istanbul ignore if */
    if (!child) {
      return rawChild

```
### Line 8794-8805
```

    if (this._leaving) {
      return placeholder(h, rawChild)
    }

    // ensure a key that is unique to the vnode type and to this transition
    // component instance. This key will be used to remove pending leaving nodes
    // during entering.
    const id = `__transition-${this._uid}-`;
    child.key = child.key == null
      ? child.isComment
        ? id + 'comment'

```
### Line 8810-8820
```

    const data = (child.data || (child.data = {})).transition = extractTransitionData(this);
    const oldRawChild = this._vnode;
    const oldChild = getRealChild(oldRawChild);

    // mark v-show
    // so that the transition module can hand over the control to the directive
    if (child.data.directives && child.data.directives.some(isVShowDirective)) {
      child.data.show = true;
    }


```
### Line 8821-8838
```
    if (
      oldChild &&
      oldChild.data &&
      !isSameChild(child, oldChild) &&
      !isAsyncPlaceholder(oldChild) &&
      // #6687 component root is a comment node
      !(oldChild.componentInstance && oldChild.componentInstance._vnode.isComment)
    ) {
      // replace old child transition data with fresh one
      // important for dynamic transitions!
      const oldData = oldChild.data.transition = extend({}, data);
      // handle transition mode
      if (mode === 'out-in') {
        // return placeholder node and queue update when leave finishes
        this._leaving = true;
        mergeVNodeHook(oldData, 'afterLeave', () => {
          this._leaving = false;
          this.$forceUpdate();

```
### Line 8868-8877
```

  beforeMount () {
    const update = this._update;
    this._update = (vnode, hydrating) => {
      const restoreActiveInstance = setActiveInstance(this);
      // force removing pass
      this.__patch__(
        this._vnode,
        this.kept,
        false, // hydrating

```
### Line 8931-8948
```
    const moveClass = this.moveClass || ((this.name || 'v') + '-move');
    if (!children.length || !this.hasMove(children[0].elm, moveClass)) {
      return
    }

    // we divide the work into three loops to avoid mixing DOM reads and writes
    // in each iteration - which helps prevent layout thrashing.
    children.forEach(callPendingCbs);
    children.forEach(recordPosition);
    children.forEach(applyTranslation);

    // force reflow to put everything in position
    // assign to this to avoid being removed in tree-shaking
    // $flow-disable-line
    this._reflow = document.body.offsetHeight;

    children.forEach((c) => {
      if (c.data.moved) {

```
### Line 8972-8985
```
      }
      /* istanbul ignore if */
      if (this._hasMove) {
        return this._hasMove
      }
      // Detect whether an element with the move class applied has
      // CSS transitions. Since the element may be inside an entering
      // transition at this very moment, we make a clone of it and remove
      // all other transition classes applied to ensure only the move class
      // is applied.
      const clone = el.cloneNode();
      if (el._transitionClasses) {
        el._transitionClasses.forEach((cls) => { removeClass(clone, cls); });
      }

```
### Line 9026-9058
```
  TransitionGroup
};

/*  */

// install platform specific utils
Vue.config.mustUseProp = mustUseProp;
Vue.config.isReservedTag = isReservedTag;
Vue.config.isReservedAttr = isReservedAttr;
Vue.config.getTagNamespace = getTagNamespace;
Vue.config.isUnknownElement = isUnknownElement;

// install platform runtime directives & components
extend(Vue.options.directives, platformDirectives);
extend(Vue.options.components, platformComponents);

// install platform patch function
Vue.prototype.__patch__ = inBrowser ? patch : noop;

// public mount method
Vue.prototype.$mount = function (
  el,
  hydrating
) {
  el = el && inBrowser ? query(el) : undefined;
  return mountComponent(this, el, hydrating)
};

// devtools global hook
/* istanbul ignore next */
if (inBrowser) {
  setTimeout(() => {
    if (config.devtools) {

```
### Line 9102-9116
```
  const rawTokens = [];
  let lastIndex = tagRE.lastIndex = 0;
  let match, index, tokenValue;
  while ((match = tagRE.exec(text))) {
    index = match.index;
    // push text token
    if (index > lastIndex) {
      rawTokens.push(tokenValue = text.slice(lastIndex, index));
      tokens.push(JSON.stringify(tokenValue));
    }
    // tag token
    const exp = parseFilters(match[1].trim());
    tokens.push(`_s(${exp})`);
    rawTokens.push({ '@binding': exp });
    lastIndex = index + match[0].length;

```
### Line 9230-9246
```
const isUnaryTag = makeMap(
  'area,base,br,col,embed,frame,hr,img,input,isindex,keygen,' +
  'link,meta,param,source,track,wbr'
);

// Elements that you can, intentionally, leave open
// (and which close themselves)
const canBeLeftOpenTag = makeMap(
  'colgroup,dd,dt,li,options,p,td,tfoot,th,thead,tr,source'
);

// HTML5 tags https://html.spec.whatwg.org/multipage/indices.html#elements-3
// Phrasing Content https://html.spec.whatwg.org/multipage/dom.html#phrasing-content
const isNonPhrasingTag = makeMap(
  'address,article,aside,base,blockquote,body,caption,col,colgroup,dd,' +
  'details,dialog,div,dl,dt,fieldset,figcaption,figure,footer,form,' +
  'h1,h2,h3,h4,h5,h6,head,header,hgroup,hr,html,legend,li,menuitem,meta,' +

```
### Line 9250-9272
```

/**
 * Not type-checking this file because it's mostly vendor code.
 */

// Regular Expressions for parsing tags and attributes
const attribute = /^\s*([^\s"'<>\/=]+)(?:\s*(=)\s*(?:"([^"]*)"+|'([^']*)'+|([^\s"'=<>`]+)))?/;
const dynamicArgAttribute = /^\s*((?:v-[\w-]+:|@|:|#)\[[^=]+\][^\s"'<>\/=]*)(?:\s*(=)\s*(?:"([^"]*)"+|'([^']*)'+|([^\s"'=<>`]+)))?/;
const ncname = `[a-zA-Z_][\\-\\.0-9_a-zA-Z${unicodeRegExp.source}]*`;
const qnameCapture = `((?:${ncname}\\:)?${ncname})`;
const startTagOpen = new RegExp(`^<${qnameCapture}`);
const startTagClose = /^\s*(\/?)>/;
const endTag = new RegExp(`^<\\/${qnameCapture}[^>]*>`);
const doctype = /^<!DOCTYPE [^>]+>/i;
// #7298: escape - to avoid being pased as HTML comment when inlined in page
const comment = /^<!\--/;
const conditionalComment = /^<!\[/;

// Special Elements (can contain anything)
const isPlainTextElement = makeMap('script,style,textarea', true);
const reCache = {};

const decodingMap = {

```
### Line 9279-9288
```
  '&#39;': "'"
};
const encodedAttr = /&(?:lt|gt|quot|amp|#39);/g;
const encodedAttrWithNewLines = /&(?:lt|gt|quot|amp|#39|#10|#9);/g;

// #5992
const isIgnoreNewlineTag = makeMap('pre,textarea', true);
const shouldIgnoreFirstNewline = (tag, html) => tag && isIgnoreNewlineTag(tag) && html[0] === '\n';

function decodeAttr (value, shouldDecodeNewlines) {

```
### Line 9297-9310
```
  const canBeLeftOpenTag$$1 = options.canBeLeftOpenTag || no;
  let index = 0;
  let last, lastTag;
  while (html) {
    last = html;
    // Make sure we're not in a plaintext content element like script/style
    if (!lastTag || !isPlainTextElement(lastTag)) {
      let textEnd = html.indexOf('<');
      if (textEnd === 0) {
        // Comment:
        if (comment.test(html)) {
          const commentEnd = html.indexOf('-->');

          if (commentEnd >= 0) {

```
### Line 9314-9323
```
            advance(commentEnd + 3);
            continue
          }
        }

        // http://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment
        if (conditionalComment.test(html)) {
          const conditionalEnd = html.indexOf(']>');

          if (conditionalEnd >= 0) {

```
### Line 9324-9349
```
            advance(conditionalEnd + 2);
            continue
          }
        }

        // Doctype:
        const doctypeMatch = html.match(doctype);
        if (doctypeMatch) {
          advance(doctypeMatch[0].length);
          continue
        }

        // End tag:
        const endTagMatch = html.match(endTag);
        if (endTagMatch) {
          const curIndex = index;
          advance(endTagMatch[0].length);
          parseEndTag(endTagMatch[1], curIndex, index);
          continue
        }

        // Start tag:
        const startTagMatch = parseStartTag();
        if (startTagMatch) {
          handleStartTag(startTagMatch);
          if (shouldIgnoreFirstNewline(startTagMatch.tagName, html)) {

```
### Line 9360-9369
```
          !endTag.test(rest) &&
          !startTagOpen.test(rest) &&
          !comment.test(rest) &&
          !conditionalComment.test(rest)
        ) {
          // < in plain text, be forgiving and treat it as text
          next = rest.indexOf('<', 1);
          if (next < 0) break
          textEnd += next;
          rest = html.slice(textEnd);

```
### Line 9413-9422
```
      }
      break
    }
  }

  // Clean up any remaining tags
  parseEndTag();

  function advance (n) {
    index += n;

```
### Line 9494-9517
```
  function parseEndTag (tagName, start, end) {
    let pos, lowerCasedTagName;
    if (start == null) start = index;
    if (end == null) end = index;

    // Find the closest opened tag of the same type
    if (tagName) {
      lowerCasedTagName = tagName.toLowerCase();
      for (pos = stack.length - 1; pos >= 0; pos--) {
        if (stack[pos].lowerCasedTag === lowerCasedTagName) {
          break
        }
      }
    } else {
      // If no tag name is provided, clean shop
      pos = 0;
    }

    if (pos >= 0) {
      // Close all the open elements, up the stack
      for (let i = stack.length - 1; i >= pos; i--) {
        if (i > pos || !tagName &&
          options.warn
        ) {

```
### Line 9523-9532
```
        if (options.end) {
          options.end(stack[i].tag, start, end);
        }
      }

      // Remove the open elements from the stack
      stack.length = pos;
      lastTag = pos && stack[pos - 1].tag;
    } else if (lowerCasedTagName === 'br') {
      if (options.start) {

```
### Line 9565-9574
```

const decodeHTMLCached = cached(he.decode);

const emptySlotScopeToken = `_empty_`;

// configurable state
let warn$2;
let delimiters;
let transforms;
let preTransforms;

```
### Line 9634-9645
```
  function closeElement (element) {
    trimEndingWhitespace(element);
    if (!inVPre && !element.processed) {
      element = processElement(element, options);
    }
    // tree management
    if (!stack.length && element !== root) {
      // allow root elements with v-if, v-else-if and v-else
      if (root.if && (element.elseif || element.else)) {
        {
          checkRootConstraints(element);
        }

```
### Line 9659-9699
```
    if (currentParent && !element.forbidden) {
      if (element.elseif || element.else) {
        processIfConditions(element, currentParent);
      } else {
        if (element.slotScope) {
          // scoped slot
          // keep it in the children list so that v-else(-if) conditions can
          // find it as the prev node.
          const name = element.slotTarget || '"default"'
          ;(currentParent.scopedSlots || (currentParent.scopedSlots = {}))[name] = element;
        }
        currentParent.children.push(element);
        element.parent = currentParent;
      }
    }

    // final children cleanup
    // filter out scoped slots
    element.children = element.children.filter(c => !(c).slotScope);
    // remove trailing whitespace node again
    trimEndingWhitespace(element);

    // check pre state
    if (element.pre) {
      inVPre = false;
    }
    if (platformIsPreTag(element.tag)) {
      inPre = false;
    }
    // apply post-transforms
    for (let i = 0; i < postTransforms.length; i++) {
      postTransforms[i](element, options);
    }
  }

  function trimEndingWhitespace (el) {
    // remove trailing whitespace node
    if (!inPre) {
      let lastNode;
      while (
        (lastNode = el.children[el.children.length - 1]) &&

```
### Line 9730-9743
```
    shouldDecodeNewlines: options.shouldDecodeNewlines,
    shouldDecodeNewlinesForHref: options.shouldDecodeNewlinesForHref,
    shouldKeepComment: options.comments,
    outputSourceRange: options.outputSourceRange,
    start (tag, attrs, unary, start, end) {
      // check namespace.
      // inherit parent ns if there is one
      const ns = (currentParent && currentParent.ns) || platformGetTagNamespace(tag);

      // handle IE svg bug
      /* istanbul ignore if */
      if (isIE && ns === 'svg') {
        attrs = guardIESVGBug(attrs);
      }

```
### Line 9778-9787
```
          `<${tag}>` + ', as they will not be parsed.',
          { start: element.start }
        );
      }

      // apply pre-transforms
      for (let i = 0; i < preTransforms.length; i++) {
        element = preTransforms[i](element, options) || element;
      }


```
### Line 9795-9804
```
        inPre = true;
      }
      if (inVPre) {
        processRawAttrs(element);
      } else if (!element.processed) {
        // structural directives
        processFor(element);
        processIf(element);
        processOnce(element);
      }

```
### Line 9818-9827
```
      }
    },

    end (tag, start, end) {
      const element = stack[stack.length - 1];
      // pop stack
      stack.length -= 1;
      currentParent = stack[stack.length - 1];
      if (options.outputSourceRange) {
        element.end = end;

```
### Line 9844-9853
```
            );
          }
        }
        return
      }
      // IE textarea placeholder bug
      /* istanbul ignore if */
      if (isIE &&
        currentParent.tag === 'textarea' &&
        currentParent.attrsMap.placeholder === text

```
### Line 9856-9870
```
      }
      const children = currentParent.children;
      if (inPre || text.trim()) {
        text = isTextTag(currentParent) ? text : decodeHTMLCached(text);
      } else if (!children.length) {
        // remove the whitespace-only node right after an opening tag
        text = '';
      } else if (whitespaceOption) {
        if (whitespaceOption === 'condense') {
          // in condense mode, remove the whitespace node if it contains
          // line break, otherwise condense to a single space
          text = lineBreakRE.test(text) ? '' : ' ';
        } else {
          text = ' ';
        }

```
### Line 9871-9880
```
      } else {
        text = preserveWhitespace ? ' ' : '';
      }
      if (text) {
        if (!inPre && whitespaceOption === 'condense') {
          // condense consecutive whitespaces into single space
          text = text.replace(whitespaceRE$1, ' ');
        }
        let res;
        let child;

```
### Line 9899-9909
```
          children.push(child);
        }
      }
    },
    comment (text, start, end) {
      // adding anyting as a sibling to the root node is forbidden
      // comments should still be allowed, but ignored
      if (currentParent) {
        const child = {
          type: 3,
          text,

```
### Line 9940-9949
```
        attrs[i].start = list[i].start;
        attrs[i].end = list[i].end;
      }
    }
  } else if (!el.pre) {
    // non root node in pre blocks with no attributes
    el.plain = true;
  }
}


```
### Line 9951-9961
```
  element,
  options
) {
  processKey(element);

  // determine whether this is a plain element after
  // removing structural attributes
  element.plain = (
    !element.key &&
    !element.scopedSlots &&
    !element.attrsList.length

```
### Line 10108-10118
```
  if (once$$1 != null) {
    el.once = true;
  }
}

// handle content being passed to a component as slot,
// e.g. <template slot="xxx">, <div slot-scope="xxx">
function processSlotContent (el) {
  let slotScope;
  if (el.tag === 'template') {
    slotScope = getAndRemoveAttr(el, 'scope');

```
### Line 10140-10164
```
      );
    }
    el.slotScope = slotScope;
  }

  // slot="xxx"
  const slotTarget = getBindingAttr(el, 'slot');
  if (slotTarget) {
    el.slotTarget = slotTarget === '""' ? '"default"' : slotTarget;
    el.slotTargetDynamic = !!(el.attrsMap[':slot'] || el.attrsMap['v-bind:slot']);
    // preserve slot as an attribute for native shadow DOM compat
    // only for non-scoped slots.
    if (el.tag !== 'template' && !el.slotScope) {
      addAttr(el, 'slot', slotTarget, getRawBindingAttr(el, 'slot'));
    }
  }

  // 2.6 v-slot syntax
  {
    if (el.tag === 'template') {
      // v-slot on <template>
      const slotBinding = getAndRemoveAttrByRegex(el, slotRE);
      if (slotBinding) {
        {
          if (el.slotTarget || el.slotScope) {

```
### Line 10179-10188
```
        el.slotTarget = name;
        el.slotTargetDynamic = dynamic;
        el.slotScope = slotBinding.value || emptySlotScopeToken; // force it into a scoped slot for perf
      }
    } else {
      // v-slot on component, denotes default slot
      const slotBinding = getAndRemoveAttrByRegex(el, slotRE);
      if (slotBinding) {
        {
          if (!maybeComponent(el)) {

```
### Line 10203-10212
```
              `<template> syntax when there are other named slots.`,
              slotBinding
            );
          }
        }
        // add the component's children to its default slot
        const slots = el.scopedSlots || (el.scopedSlots = {});
        const { name, dynamic } = getSlotName(slotBinding);
        const slotContainer = slots[name] = createASTElement('template', [], el);
        slotContainer.slotTarget = name;

```
### Line 10216-10227
```
            c.parent = slotContainer;
            return true
          }
        });
        slotContainer.slotScope = slotBinding.value || emptySlotScopeToken;
        // remove children as they are returned from scopedSlots now
        el.children = [];
        // mark el non-plain so data gets generated
        el.plain = false;
      }
    }
  }

```
### Line 10238-10253
```
        binding
      );
    }
  }
  return dynamicArgRE.test(name)
    // dynamic [name]
    ? { name: name.slice(1, -1), dynamic: true }
    // static name
    : { name: `"${name}"`, dynamic: false }
}

// handle <slot/> outlets
function processSlotOutlet (el) {
  if (el.tag === 'slot') {
    el.slotName = getBindingAttr(el, 'name');
    if (el.key) {

```
### Line 10276-10289
```
  let i, l, name, rawName, value, modifiers, syncGen, isDynamic;
  for (i = 0, l = list.length; i < l; i++) {
    name = rawName = list[i].name;
    value = list[i].value;
    if (dirRE.test(name)) {
      // mark element as dynamic
      el.hasBindings = true;
      // modifiers
      modifiers = parseModifiers(name.replace(dirRE, ''));
      // support .foo shorthand syntax for the .prop modifier
      if (modifiers) {
        name = name.replace(modifierRE, '');
      }
      if (bindRE.test(name)) { // v-bind

```
### Line 10330-10339
```
                  warn$2,
                  list[i]
                );
              }
            } else {
              // handler w/ dynamic event name
              addHandler(
                el,
                `"update:"+(${name})`,
                syncGen,

```
### Line 10360-10369
```
          name = name.slice(1, -1);
        }
        addHandler(el, name, value, modifiers, false, warn$2, list[i], isDynamic);
      } else { // normal directives
        name = name.replace(dirRE, '');
        // parse arg
        const argMatch = name.match(argRE);
        let arg = argMatch && argMatch[1];
        isDynamic = false;
        if (arg) {

```
### Line 10377-10386
```
        if (name === 'model') {
          checkForAliasModel(el, value);
        }
      }
    } else {
      // literal attribute
      {
        const res = parseText(value, delimiters);
        if (res) {
          warn$2(

```
### Line 10391-10401
```
            list[i]
          );
        }
      }
      addAttr(el, name, JSON.stringify(value), list[i]);
      // #6887 firefox doesn't update muted state if set via attribute
      // even immediately after element creation
      if (!el.component &&
          name === 'muted' &&
          platformMustUseProp(el.tag, el.attrsMap.type, name)) {
        addProp(el, name, 'true', list[i]);

```
### Line 10435-10444
```
    map[attrs[i].name] = attrs[i].value;
  }
  return map
}

// for script (e.g. type="x/template") or style, do not decode content
function isTextTag (el) {
  return el.tag === 'script' || el.tag === 'style'
}


```
### Line 10505-10516
```
    if (typeBinding) {
      const ifCondition = getAndRemoveAttr(el, 'v-if', true);
      const ifConditionExtra = ifCondition ? `&&(${ifCondition})` : ``;
      const hasElse = getAndRemoveAttr(el, 'v-else', true) != null;
      const elseIfCondition = getAndRemoveAttr(el, 'v-else-if', true);
      // 1. checkbox
      const branch0 = cloneASTElement(el);
      // process for on the main node
      processFor(branch0);
      addRawAttr(branch0, 'type', 'checkbox');
      processElement(branch0, options);
      branch0.processed = true; // prevent it from double-processed

```
### Line 10517-10535
```
      branch0.if = `(${typeBinding})==='checkbox'` + ifConditionExtra;
      addIfCondition(branch0, {
        exp: branch0.if,
        block: branch0
      });
      // 2. add radio else-if condition
      const branch1 = cloneASTElement(el);
      getAndRemoveAttr(branch1, 'v-for', true);
      addRawAttr(branch1, 'type', 'radio');
      processElement(branch1, options);
      addIfCondition(branch0, {
        exp: `(${typeBinding})==='radio'` + ifConditionExtra,
        block: branch1
      });
      // 3. other
      const branch2 = cloneASTElement(el);
      getAndRemoveAttr(branch2, 'v-for', true);
      addRawAttr(branch2, ':type', typeBinding);
      processElement(branch2, options);

```
### Line 10620-10631
```
 */
function optimize (root, options) {
  if (!root) return
  isStaticKey = genStaticKeysCached(options.staticKeys || '');
  isPlatformReservedTag = options.isReservedTag || no;
  // first pass: mark all non-static nodes.
  markStatic$1(root);
  // second pass: mark static roots.
  markStaticRoots(root, false);
}

function genStaticKeys$1 (keys) {

```
### Line 10636-10647
```
}

function markStatic$1 (node) {
  node.static = isStatic(node);
  if (node.type === 1) {
    // do not make component slot content static. this avoids
    // 1. components not able to mutate slot nodes
    // 2. static slot content fails for hot-reloading
    if (
      !isPlatformReservedTag(node.tag) &&
      node.tag !== 'slot' &&
      node.attrsMap['inline-template'] == null

```
### Line 10670-10681
```
function markStaticRoots (node, isInFor) {
  if (node.type === 1) {
    if (node.static || node.once) {
      node.staticInFor = isInFor;
    }
    // For a node to qualify as a static root, it should have children that
    // are not just static text. Otherwise the cost of hoisting out will
    // outweigh the benefits and it's better off to just always render it fresh.
    if (node.static && node.children.length && !(
      node.children.length === 1 &&
      node.children[0].type === 3
    )) {

```
### Line 10731-10740
```

const fnExpRE = /^([\w$_]+|\([^)]*?\))\s*=>|^function\s*(?:[\w$]+)?\s*\(/;
const fnInvokeRE = /\([^)]*?\);*$/;
const simplePathRE = /^[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*|\['[^']*?']|\["[^"]*?"]|\[\d+]|\[[A-Za-z_$][\w$]*])*$/;

// KeyboardEvent.keyCode aliases
const keyCodes = {
  esc: 27,
  tab: 9,
  enter: 13,

```
### Line 10744-10772
```
  right: 39,
  down: 40,
  'delete': [8, 46]
};

// KeyboardEvent.key aliases
const keyNames = {
  // #7880: IE11 and Edge use `Esc` for Escape key name.
  esc: ['Esc', 'Escape'],
  tab: 'Tab',
  enter: 'Enter',
  // #9112: IE11 uses `Spacebar` for Space key name.
  space: [' ', 'Spacebar'],
  // #7806: IE11 uses key names without `Arrow` prefix for arrow keys.
  up: ['Up', 'ArrowUp'],
  left: ['Left', 'ArrowLeft'],
  right: ['Right', 'ArrowRight'],
  down: ['Down', 'ArrowDown'],
  // #9112: IE11 uses `Del` for Delete key name.
  'delete': ['Backspace', 'Delete', 'Del']
};

// #4868: modifiers that prevent the execution of the listener
// need to explicitly return null so that we can determine whether to remove
// the listener for .once
const genGuard = condition => `if(${condition})return null;`;

const modifierCode = {
  stop: '$event.stopPropagation();',

```
### Line 10829-10838
```
    let genModifierCode = '';
    const keys = [];
    for (const key in handler.modifiers) {
      if (modifierCode[key]) {
        genModifierCode += modifierCode[key];
        // left/right
        if (keyCodes[key]) {
          keys.push(key);
        }
      } else if (key === 'exact') {

```
### Line 10848-10857
```
      }
    }
    if (keys.length) {
      code += genKeyFilter(keys);
    }
    // Make sure modifiers like prevent and stop get executed after key filtering
    if (genModifierCode) {
      code += genModifierCode;
    }
    const handlerCode = isMethodPath

```
### Line 10865-10876
```
  }
}

function genKeyFilter (keys) {
  return (
    // make sure the key filters only apply to KeyboardEvents
    // #9441: can't use 'keyCode' in $event because Chrome autofill fires fake
    // key events that do not have keyCode property...
    `if(!$event.type.indexOf('key')&&` +
    `${keys.map(genFilterCode).join('&&')})return null;`
  )
}

```
### Line 10982-10991
```
  } else if (el.tag === 'template' && !el.slotTarget && !state.pre) {
    return genChildren(el, state) || 'void 0'
  } else if (el.tag === 'slot') {
    return genSlot(el, state)
  } else {
    // component or element
    let code;
    if (el.component) {
      code = genComponent(el.component, el, state);
    } else {

```
### Line 10999-11021
```
        data ? `,${data}` : '' // data
      }${
        children ? `,${children}` : '' // children
      })`;
    }
    // module transforms
    for (let i = 0; i < state.transforms.length; i++) {
      code = state.transforms[i](el, code);
    }
    return code
  }
}

// hoist static sub-trees out
function genStatic (el, state) {
  el.staticProcessed = true;
  // Some elements (templates) need to behave differently inside of a v-pre
  // node.  All pre nodes are static roots, so we can use this as a location to
  // wrap a state change and reset it upon exiting the pre node.
  const originalPreState = state.pre;
  if (el.pre) {
    state.pre = el.pre;
  }

```
### Line 11026-11035
```
  }${
    el.staticInFor ? ',true' : ''
  })`
}

// v-once
function genOnce (el, state) {
  el.onceProcessed = true;
  if (el.if && !el.ifProcessed) {
    return genIf(el, state)

```
### Line 11085-11094
```
    }`
  } else {
    return `${genTernaryExp(condition.block)}`
  }

  // v-if with v-once should generate code like (a)?_m(0):_m(1)
  function genTernaryExp (el) {
    return altGen
      ? altGen(el, state)
      : el.once

```
### Line 11130-11191
```
}

function genData$2 (el, state) {
  let data = '{';

  // directives first.
  // directives may mutate the el's other properties before they are generated.
  const dirs = genDirectives(el, state);
  if (dirs) data += dirs + ',';

  // key
  if (el.key) {
    data += `key:${el.key},`;
  }
  // ref
  if (el.ref) {
    data += `ref:${el.ref},`;
  }
  if (el.refInFor) {
    data += `refInFor:true,`;
  }
  // pre
  if (el.pre) {
    data += `pre:true,`;
  }
  // record original tag name for components using "is" attribute
  if (el.component) {
    data += `tag:"${el.tag}",`;
  }
  // module data generation functions
  for (let i = 0; i < state.dataGenFns.length; i++) {
    data += state.dataGenFns[i](el);
  }
  // attributes
  if (el.attrs) {
    data += `attrs:${genProps(el.attrs)},`;
  }
  // DOM props
  if (el.props) {
    data += `domProps:${genProps(el.props)},`;
  }
  // event handlers
  if (el.events) {
    data += `${genHandlers(el.events, false)},`;
  }
  if (el.nativeEvents) {
    data += `${genHandlers(el.nativeEvents, true)},`;
  }
  // slot target
  // only for non-scoped slots
  if (el.slotTarget && !el.slotScope) {
    data += `slot:${el.slotTarget},`;
  }
  // scoped slots
  if (el.scopedSlots) {
    data += `${genScopedSlots(el, el.scopedSlots, state)},`;
  }
  // component v-model
  if (el.model) {
    data += `model:{value:${
      el.model.value
    },callback:${

```
### Line 11192-11219
```
      el.model.callback
    },expression:${
      el.model.expression
    }},`;
  }
  // inline-template
  if (el.inlineTemplate) {
    const inlineTemplate = genInlineTemplate(el, state);
    if (inlineTemplate) {
      data += `${inlineTemplate},`;
    }
  }
  data = data.replace(/,$/, '') + '}';
  // v-bind dynamic argument wrap
  // v-bind with dynamic arguments must be applied using the same v-bind object
  // merge helper so that class/style/mustUseProp attrs are handled correctly.
  if (el.dynamicAttrs) {
    data = `_b(${data},"${el.tag}",${genProps(el.dynamicAttrs)})`;
  }
  // v-bind data wrap
  if (el.wrapData) {
    data = el.wrapData(data);
  }
  // v-on data wrap
  if (el.wrapListeners) {
    data = el.wrapListeners(data);
  }
  return data

```
### Line 11228-11238
```
  for (i = 0, l = dirs.length; i < l; i++) {
    dir = dirs[i];
    needRuntime = true;
    const gen = state.directives[dir.name];
    if (gen) {
      // compile-time directive that manipulates AST.
      // returns true if it also needs a runtime counterpart.
      needRuntime = !!gen(el, dir, state.warn);
    }
    if (needRuntime) {
      hasRuntime = true;

```
### Line 11271-11283
```
function genScopedSlots (
  el,
  slots,
  state
) {
  // by default scoped slots are considered "stable", this allows child
  // components with only scoped slots to skip forced updates from parent.
  // but in some cases we have to bail-out of this optimization
  // for example if the slot contains dynamic names, has v-if or v-for on them...
  let needsForceUpdate = el.for || Object.keys(slots).some(key => {
    const slot = slots[key];
    return (
      slot.slotTargetDynamic ||

```
### Line 11285-11304
```
      slot.for ||
      containsSlotChild(slot) // is passing down slot from parent which may be dynamic
    )
  });

  // #9534: if a component with scoped slots is inside a conditional branch,
  // it's possible for the same component to be reused but with different
  // compiled slot content. To avoid that, we generate a unique key based on
  // the generated code of all the slot contents.
  let needsKey = !!el.if;

  // OR when it is inside another scoped slot or v-for (the reactivity may be
  // disconnected due to the intermediate scope variable)
  // #9438, #9506
  // TODO: this can be further optimized by properly analyzing in-scope bindings
  // and skip force updating ones that do not actually use scope variables.
  if (!needsForceUpdate) {
    let parent = el.parent;
    while (parent) {
      if (

```
### Line 11364-11373
```
      ? el.if && isLegacySyntax
        ? `(${el.if})?${genChildren(el, state) || 'undefined'}:undefined`
        : genChildren(el, state) || 'undefined'
      : genElement(el, state)
    }}`;
  // reverse proxy v-slot without scope on this.$slots
  const reverseProxy = slotScope ? `` : `,proxy:true`;
  return `{key:${el.slotTarget || `"default"`},fn:${fn}${reverseProxy}}`
}


```
### Line 11379-11388
```
  altGenNode
) {
  const children = el.children;
  if (children.length) {
    const el = children[0];
    // optimize single v-for
    if (children.length === 1 &&
      el.for &&
      el.tag !== 'template' &&
      el.tag !== 'slot'

```
### Line 11400-11412
```
      normalizationType ? `,${normalizationType}` : ''
    }`
  }
}

// determine the normalization needed for the children array.
// 0: no normalization needed
// 1: simple normalization needed (possible 1-level deep nested array)
// 2: full normalization needed
function getNormalizationType (
  children,
  maybeComponent
) {

```
### Line 11458-11467
```
  const slotName = el.slotName || '"default"';
  const children = genChildren(el, state);
  let res = `_t(${slotName}${children ? `,${children}` : ''}`;
  const attrs = el.attrs || el.dynamicAttrs
    ? genProps((el.attrs || []).concat(el.dynamicAttrs || []).map(attr => ({
        // slot props are camelized
        name: camelize(attr.name),
        value: attr.value,
        dynamic: attr.dynamic
      })))

```
### Line 11477-11486
```
    res += `${attrs ? '' : ',null'},${bind$$1}`;
  }
  return res + ')'
}

// componentName is el.component, take it as argument to shun flow's pessimistic refinement
function genComponent (
  componentName,
  el,
  state

```
### Line 11509-11518
```
  } else {
    return staticProps
  }
}

// #3895, #4268
function transformSpecialNewlines (text) {
  return text
    .replace(/\u2028/g, '\\u2028')
    .replace(/\u2029/g, '\\u2029')

```
### Line 11520-11545
```

/*  */



// these keywords should not appear inside expressions, but operators like
// typeof, instanceof and in are allowed
const prohibitedKeywordRE = new RegExp('\\b' + (
  'do,if,for,let,new,try,var,case,else,with,await,break,catch,class,const,' +
  'super,throw,while,yield,delete,export,import,return,switch,default,' +
  'extends,finally,continue,debugger,function,arguments'
).split(',').join('\\b|\\b') + '\\b');

// these unary operators should not be used as property/method names
const unaryOperatorsRE = new RegExp('\\b' + (
  'delete,typeof,void'
).split(',').join('\\s*\\([^\\)]*\\)|\\b') + '\\s*\\([^\\)]*\\)');

// strip strings in expressions
const stripStringRE = /'(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*"|`(?:[^`\\]|\\.)*\$\{|\}(?:[^`\\]|\\.)*`|`(?:[^`\\]|\\.)*`/g;

// detect problematic expressions in a template
function detectErrors (ast, warn) {
  if (ast) {
    checkNode(ast, warn);
  }

```
### Line 11648-11657
```
      for (let j = i - range; j <= i + range || end > count; j++) {
        if (j < 0 || j >= lines.length) continue
        res.push(`${j + 1}${repeat(` `, 3 - String(j + 1).length)}|  ${lines[j]}`);
        const lineLength = lines[j].length;
        if (j === i) {
          // push underline
          const pad = start - (count - lineLength) + 1;
          const length = end > count ? lineLength - pad : end - start;
          res.push(`   |  ` + repeat(` `, pad) + repeat(`^`, length));
        } else if (j > i) {

```
### Line 11706-11715
```
    const warn$$1 = options.warn || warn;
    delete options.warn;

    /* istanbul ignore if */
    {
      // detect possible CSP restriction
      try {
        new Function('return 1');
      } catch (e) {
        if (e.toString().match(/unsafe-eval|CSP/)) {

```
### Line 11722-11742
```
          );
        }
      }
    }

    // check cache
    const key = options.delimiters
      ? String(options.delimiters) + template
      : template;
    if (cache[key]) {
      return cache[key]
    }

    // compile
    const compiled = compile(template, options);

    // check compilation errors/tips
    {
      if (compiled.errors && compiled.errors.length) {
        if (options.outputSourceRange) {
          compiled.errors.forEach(e => {

```
### Line 11761-11780
```
          compiled.tips.forEach(msg => tip(msg, vm));
        }
      }
    }

    // turn code into functions
    const res = {};
    const fnGenErrors = [];
    res.render = createFunction(compiled.render, fnGenErrors);
    res.staticRenderFns = compiled.staticRenderFns.map(code => {
      return createFunction(code, fnGenErrors)
    });

    // check function generation errors.
    // this should only happen if there is a bug in the compiler itself.
    // mostly for codegen development use
    /* istanbul ignore if */
    {
      if ((!compiled.errors || !compiled.errors.length) && fnGenErrors.length) {
        warn$$1(

```
### Line 11805-11814
```
        (tip ? tips : errors).push(msg);
      };

      if (options) {
        if (options.outputSourceRange) {
          // $flow-disable-line
          const leadingSpaceLength = template.match(/^\s*/)[0].length;

          warn = (msg, range, tip) => {
            const data = { msg };

```
### Line 11821-11842
```
              }
            }
            (tip ? tips : errors).push(data);
          };
        }
        // merge custom modules
        if (options.modules) {
          finalOptions.modules =
            (baseOptions.modules || []).concat(options.modules);
        }
        // merge custom directives
        if (options.directives) {
          finalOptions.directives = extend(
            Object.create(baseOptions.directives || null),
            options.directives
          );
        }
        // copy other options
        for (const key in options) {
          if (key !== 'modules' && key !== 'directives') {
            finalOptions[key] = options[key];
          }

```
### Line 11861-11872
```
  }
}

/*  */

// `createCompilerCreator` allows creating compilers that use alternative
// parser/optimizer/codegen, e.g the SSR optimizing compiler.
// Here we just export a default compiler using the default parts.
const createCompiler = createCompilerCreator(function baseCompile (
  template,
  options
) {

```
### Line 11886-11905
```

const { compile, compileToFunctions } = createCompiler(baseOptions);

/*  */

// check whether current browser encodes a char inside attribute values
let div;
function getShouldDecode (href) {
  div = div || document.createElement('div');
  div.innerHTML = href ? `<a href="\n"/>` : `<div a="\n"/>`;
  return div.innerHTML.indexOf('&#10;') > 0
}

// #3663: IE encodes newlines inside attribute values while other browsers don't
const shouldDecodeNewlines = inBrowser ? getShouldDecode(false) : false;
// #6828: chrome encodes content in a[href]
const shouldDecodeNewlinesForHref = inBrowser ? getShouldDecode(true) : false;

/*  */


```
### Line 11922-11931
```
    );
    return this
  }

  const options = this.$options;
  // resolve template/el and convert to render function
  if (!options.render) {
    let template = options.template;
    if (template) {
      if (typeof template === 'string') {

```

## _test_unit_modules_compiler_compiler_options_spec_js
### Line 40-58
```
              data += `validators:${JSON.stringify(el.validators)},`
            }
            return data
          },
          transformCode (el, code) {
            // check
            if (!el.validate || !el.validators) {
              return code
            }
            // setup validation result props
            const result = { dirty: false } // define something other prop
            el.validators.forEach(validator => {
              result[validator.name] = null
            })
            // generate code
            return `_c('validate',{props:{
              field:${JSON.stringify(el.validate.field)},
              groups:${JSON.stringify(el.validate.groups)},
              validators:${JSON.stringify(el.validators)},

```
### Line 90-107
```
              }
              return ret
            }
          },
          mounted () {
            // initialize validation
            const value = this.$el.value
            this.validators.forEach(validator => {
              const ret = this[validator.name](value, validator.rule)
              this.result[validator.name] = ret
            })
          },
          methods: {
            // something validators logic
            required (val) {
              return val.length > 0
            },
            max (val, rule) {

```

## _test_ssr_fixtures_async_bar_js

## _babelrc_js
### Line 1-16
```
const babelPresetFlowVue = {
  plugins: [
    require('@babel/plugin-proposal-class-properties'),
    // require('@babel/plugin-syntax-flow'), // not needed, included in transform-flow-strip-types
    require('@babel/plugin-transform-flow-strip-types')
  ]
}

module.exports = {
  presets: [
    require('@babel/preset-env'),
    // require('babel-preset-flow-vue')
    babelPresetFlowVue
  ],
  plugins: [
    require('babel-plugin-transform-vue-jsx'),

```

## _src_core_global_api_extend_js
### Line 40-81
```
      Super.options,
      extendOptions
    )
    Sub['super'] = Super

    // For props and computed properties, we define the proxy getters on
    // the Vue instances at extension time, on the extended prototype. This
    // avoids Object.defineProperty calls for each instance created.
    if (Sub.options.props) {
      initProps(Sub)
    }
    if (Sub.options.computed) {
      initComputed(Sub)
    }

    // allow further extension/mixin/plugin usage
    Sub.extend = Super.extend
    Sub.mixin = Super.mixin
    Sub.use = Super.use

    // create asset registers, so extended classes
    // can have their private assets too.
    ASSET_TYPES.forEach(function (type) {
      Sub[type] = Super[type]
    })
    // enable recursive self-lookup
    if (name) {
      Sub.options.components[name] = Sub
    }

    // keep a reference to the super options at extension time.
    // later at instantiation we can check if Super's options have
    // been updated.
    Sub.superOptions = Super.options
    Sub.extendOptions = extendOptions
    Sub.sealedOptions = extend({}, Sub.options)

    // cache constructor
    cachedCtors[SuperId] = Sub
    return Sub
  }
}

```

## _src_core_vdom_helpers_is_async_placeholder_js

## _test_unit_modules_observer_scheduler_spec_js
### Line 72-81
```
      expect(calls).toEqual([1, 2])
    }).then(done)
  })

  it('call user watcher triggered by component re-render immediately', done => {
    // this happens when a component re-render updates the props of a child
    const calls = []
    const vm = new Vue({
      data: {
        a: 1

```
### Line 145-154
```
    waitForUpdate(() => {
      expect(callOrder).toEqual([1, 2, 3])
    }).then(done)
  })

  // GitHub issue #5191
  it('emit should work when updated hook called', done => {
    const el = document.createElement('div')
    const vm = new Vue({
      template: `<div><child @change="bar" :foo="foo"></child></div>`,

```

## _test_unit_features_filter_filter_spec_js

## _src_compiler_to_function_js
### Line 30-39
```
    const warn = options.warn || baseWarn
    delete options.warn

    /* istanbul ignore if */
    if (process.env.NODE_ENV !== 'production') {
      // detect possible CSP restriction
      try {
        new Function('return 1')
      } catch (e) {
        if (e.toString().match(/unsafe-eval|CSP/)) {

```
### Line 46-66
```
          )
        }
      }
    }

    // check cache
    const key = options.delimiters
      ? String(options.delimiters) + template
      : template
    if (cache[key]) {
      return cache[key]
    }

    // compile
    const compiled = compile(template, options)

    // check compilation errors/tips
    if (process.env.NODE_ENV !== 'production') {
      if (compiled.errors && compiled.errors.length) {
        if (options.outputSourceRange) {
          compiled.errors.forEach(e => {

```
### Line 85-104
```
          compiled.tips.forEach(msg => tip(msg, vm))
        }
      }
    }

    // turn code into functions
    const res = {}
    const fnGenErrors = []
    res.render = createFunction(compiled.render, fnGenErrors)
    res.staticRenderFns = compiled.staticRenderFns.map(code => {
      return createFunction(code, fnGenErrors)
    })

    // check function generation errors.
    // this should only happen if there is a bug in the compiler itself.
    // mostly for codegen development use
    /* istanbul ignore if */
    if (process.env.NODE_ENV !== 'production') {
      if ((!compiled.errors || !compiled.errors.length) && fnGenErrors.length) {
        warn(

```

## _src_core_util_perf_js
### Line 16-24
```
    mark = tag => perf.mark(tag)
    measure = (name, startTag, endTag) => {
      perf.measure(name, startTag, endTag)
      perf.clearMarks(startTag)
      perf.clearMarks(endTag)
      // perf.clearMeasures(name)
    }
  }
}

```

## _src_core_instance_render_helpers_check_keycodes_js

## _packages_vue_template_compiler_browser_js

## _packages_vue_server_renderer_build_prod_js

# Issues
## 9401
Title:
```

        Vue version 2.5.22 is missing vue.esm.browser.js in the dist folder.
      
```
Author:
```
Giwayume
```
Text:
```

Version
2.5.22
Reproduction link
https://repl.it/repls/CreepyStaticInstitute
Steps to reproduce
npm init
npm install vue@2.5.22

View the contents of node_modules/vue/dist. The file 'vue.esm.browser.js` is missing.
What is expected?
'vue.esm.browser.js` should exist, like in version 2.5.21
What is actually happening?
'vue.esm.browser.js` is missing.

```
Author:
```
Justineo
```
Text:
```

See #7110 (comment).

```

## 5156
Title:
```

        this.$el is a comment when using v-if on root element
      
```
Author:
```
milimetric
```
Text:
```

If you're using v-if on a root element, and the condition of the v-if is false when your created event fires, then this.$el will be a comment element instead of the root you might expect.  This makes sense, but might be as confusing to others as it was to me.  Some warning in the documentation or on template compilation might be useful to others.  Example:
<template>
<div v-if="thisLoadsAsyncButIsFalseNow">
...
</div>
</template>

<script>
export default {
    created () {
        console.log(this.$el) // this might log correctly if your browser interprets it after the async update, but it's a comment node when the created event fires
    }
}
</script>


```
Author:
```
LinusBorg
```
Text:
```

Yes, this is expected behaviour, Vue needs some root node, and falsl back on a comment if your code doesn't provide a real one.
If you think this should be made clear in the docs, please open an issue in the website's repository at github.com/vuejs/vuejs.org

```
Author:
```
darkiron
```
Text:
```

I have the same issue on IE 11 without v-if on mounted event
is expected behavior ?

```
Author:
```
damien-roche
```
Text:
```

^^ same without v-if on mounted event in production only (works fine in dev). Fun times 👍

```
Author:
```
koga73
```
Text:
```


^^ same without v-if on mounted event in production only (works fine in dev). Fun times 👍

For me vue was in production which is why I didn't see the actual error. One of my templates wouldn't compile in IE11 due to syntax problem

```

## 10330
Title:
```

        nested v-slot is not reactive when using abbreviated syntax (v-slot on component itself) combined with an v-if/v-else
      
```
Author:
```
dattn
```
Text:
```

Version
2.6.10
Reproduction link
https://codesandbox.io/s/vue-template-j1w3r
Steps to reproduce
In my example change the value by typing in the input field.
In the working example both values change.
In the not working example only the nested value changes.
The only difference is the wrapping <template> node
What is expected?
scoped slot params (controllerSlotData) should be reactive in both cases
What is actually happening?
scoped slot params (controllerSlotData) is not reative

The problem exists only when combining v-slot on component itself in combination with v-if/v-else

```

## 8869
Title:
```

        Cannot find module .vue single in ts
      
```
Author:
```
LY1993
```
Text:
```

webpack:
{
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        ts: 'babel-loader!ts-loader',
                        tsx: 'babel-loader!ts-loader'
                    }
                }
  }

test.vue:
<template>
    <div>hhhh</div>
</template>
<script>
export default {
    name: 'ttt'
}
</script>

app.vue:
import ttt from '../components/test.vue';


Cannot find module '../components/test.vue'.
if i add lang='ts' that is ok
but i dont want to add lang='ts', how can i do
Expected Behaviour
Actual Behaviour
Cannot find module '../components/test.vue'.
Steps to Reproduce the Problem
Location of a Minimal Repository that Demonstrates the Issue.

```
Author:
```
vue-bot
```
Text:
```

Hello, your issue has been closed because it does not conform to our issue requirements. In order to ensure every issue provides the necessary information for us to investigate, we require the use of the Issue Helper when creating new issues. Thank you!

```

## 8505
Title:
```

        How to render array of component instances in vue.js?
      
```
Author:
```
meowofficial
```
Text:
```

I need to build list of dynamical components that I can group in group component. Then I need to send all information about builded components and groups.
I can use <component v-for="componentName in myComponents" :is="componentName"></component>, and get information about components using this.$children.map(component => component.getInformation()), but then I can't move some component to group component, because I have only component name not the component instance with data (it just render with default data).
I also can use this:
    <template>
      <div ref="container"> </div>
    </template>
        
    <script>
      import someComponent from 'someComponent.vue'
      import Vue from 'vue'
    
      export default {
        data () {
    	  return {
    	    myComponents: []
    	  }
    	},
    	methods: {
    	  addSomeComponent () {
		let ComponentClass = Vue.extend(someComponent);
		let instance = new ComponentClass({});
		myComponents.push(instance);
		instance.$mount();
		this.$refs.container.appendChild(instance.$el)
	  },
          getInformation () {
            return this.myComponents.map(component => component.getInformation());
          }
    	}
      }
    </script>

But then I can't use reactivity, directives (e.g. directives for drag and drop), and it's not data driven pattern.
Any suggestions?

```
Author:
```
vue-bot
```
Text:
```

Hello, your issue has been closed because it does not conform to our issue requirements. In order to ensure every issue provides the necessary information for us to investigate, we require the use of the Issue Helper when creating new issues. Thank you!

```

## 9862
Title:
```

        v-if cannot access slot scope with new slot syntax
      
```
Author:
```
econic
```
Text:
```

Version
2.6.10
Reproduction link
https://codesandbox.io/s/7j9o6o4310?fontsize=14
Steps to reproduce
Use a component that defines a scoped slot like this
<MyComponent>
  <template v-if="scope.foo" #myslotname="scope">...</template>
</MyComponent>

What is expected?
The template should evaluate the slot directive first, v-if second. Just as it is done with v-for first, v-if second.
What is actually happening?
The template evaluates the v-if first, resulting in an error (unknown component property)

This functionality was present in the deprecated slot syntax, i stumbled upon it while refactoring to the new one.
It is possible to workaround this with a nested template with the respected v-if
I'm using latest Vue, TypeScript, SFC

```
Author:
```
posva
```
Text:
```

I couldn't find the duplicate of this but this is now expected behaviour because the v-if has higher priority. As you said, using a nested template is the way to go

```

## 4894
Title:
```

        Transitions don't work on Electron
      
```
Author:
```
snapeuh
```
Text:
```

Hello,
I am using Vue for my app and I packaged it as an Electron app. Unfortunately I noticed that the transitions weren't working on Electron (while it is on Chrome or Safari).
I loaded the documentation page about Transitions on electron-quick-start (on Github) and most examples don't work.
I am using a transition with a dynamic name in out-in mode. I tested on a Mac.
Any hint on why it doesn't work on Electron?
Regards,
Romain.

```
Author:
```
posva
```
Text:
```

I tested by adding window.location = 'https://vuejs.org/v2/guide/transitions.html' to the index.html file and they all work nicely. can you please be more precise?

```
Author:
```
snapeuh
```
Text:
```

Hey,
Here's my steps to reproduce :
git clone https://github.com/electron/electron-quick-start
cd electron-quick-start
npm install

The output from npm install tells me that it installed electron@1.4.15.
Then I edit the main.js with :
mainWindow.loadURL('https://vuejs.org/v2/guide/transitions.html')

Here's a link to the whole file on Gist : Here.
I run npm start. It loads Electron, loads the Vue.js website and if I click on the first Toggle button and there's no animation happening. Same for the next at least 5 examples.
Tested on Mac 10.11.6 (El Capitan).
Regards,
Romain.

```
Author:
```
snapeuh
```
Text:
```

I did a little screencast so you can see what I am experiencing :
http://re.d.pr/14guc

```
Author:
```
posva
```
Text:
```

Can you try using the latest version of electron, please?
Can you share the output of clientInformation.appVersion, please?
edit: I tried with electron 1.4.1 and it works too

```
Author:
```
snapeuh
```
Text:
```

I tried with Electron 1.6.0 and I have the same problem.
I didn't find how to use clientInformation.appVersion and I obviously had this error :
ReferenceError: clientInformation is not defined

Are you on Mac? Which OS version?
Also I have this error on the console :
Uncaught ReferenceError: FastClick is not defined at HTMLDocument.<anonymous> (transitions.html:1502)

I don't think it's linked because that error doesn't show up on my app and still transitions don't work.
Just to be clear, it works on Chrome and Safari without any issue.
Thanks for looking into it! 😊

```
Author:
```
posva
```
Text:
```

I have Sierra (10.12.3)

I didn't find how to use clientInformation.appVersion and I obviously had this error

Well, that's weird. Could it be you have an older non-supported version? Not sure about how to clean that cache, though

```
Author:
```
snapeuh
```
Text:
```

Hey,
I figured out I just needed to type that on the inspector console, I previously did a console.log on main.js which obviously failed, here's the output :
5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) electron-quick-start/1.0.0 Chrome/56.0.2924.87 Electron/1.6.0 Safari/537.36

I tested on Windows and Linux and it worked without any issue. It's just strange it doesn't work on my platform which is only 1 version behind the current Mac OS release.
Do you have any hint?
If you don't, please close the issue as it works like a charm on other platforms.
Romain.

```
Author:
```
posva
```
Text:
```

I'm sorry, I really don't know what may be causing that...
I tested with the same versions except for the os X version. It'd be very strange if that's the issue 😆
Closing since there's nothing we can do. If you find out the problem, please, come back and share 😄

```
Author:
```
JanGunzenhauser
```
Text:
```

@snapeuh Same issue on OS X 10.12.5. It works after adding a duration, e.g.
<transition name="fade" mode="out-in" :duration="350"> ... </transition>

```
Author:
```
ToniApps
```
Text:
```

Same fail

```
Author:
```
achimkoellner
```
Text:
```

Same on OSX 10.11.6

```
Author:
```
vdcrea
```
Text:
```

Thanks @JanGunzenhauser, it works with duration. #4894 (comment)

```
Author:
```
SteffenDE
```
Text:
```

Strange, same issue with
5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) electron-quick-start/1.0.0 Chrome/58.0.3029.110 Electron/1.7.9 Safari/537.36
Unfortunately I can't use the duration workaround, since I'm using vuetify's transitions:
window.location = 'https://vuetifyjs.com/motion/transitions'
The in transition works but the out transition doesn't...

```
Author:
```
phablulo
```
Text:
```

Same issue with 5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) electron-open-app/1.0.0 Chrome/61.0.3163.100 Electron/2.0.5 Safari/537.36 on a Mac OS High Sierra 10.13.5 and Electron 2.0.5 (latest).
Transitions works only when duration is bigger than 1s. Otherwise it fails even when using the duration tag.

```
Author:
```
phablulo
```
Text:
```

After some while I found the problem:
floating point numbers on the object returned by Electron's window.getComputedStyle comes with a comma instead of a dot. Thus Vue will always parse it as 0 as we can see here.
I submitted a PR to fix this.


```
Author:
```
SteffenDE
```
Text:
```

Thank you @phablulo, let's hope this gets merged soon!
This is the mentioned pull request: #8495

```

## 9865
Title:
```

        Vue global component registration is broken with vue-devtools on
      
```
Author:
```
shawwwn
```
Text:
```

Version
2.6.10
Reproduction link
https://jsfiddle.net/myen70g1/6/
Steps to reproduce

Copy the code in jsfiddle and save it to a html.
Enable vue-devtools in chrome.
Open the html we saved in step 1 in chrome, notice 'Hello World!' should be displayed after 1s.
Inspect the page, switch to Vue tab by vue-devtools.
Reload the page, no more 'Hello World!' will be displayed.

From now on, you may refresh the page however you want, no message will be displayed.
What is expected?
'Hello World!' even with vue-devtools on
What is actually happening?
No 'Hello World!', not happy!

It seems dev tool is breaking the prototyping between Vue.option.components and vm.$option.components.

```
Author:
```
posva
```
Text:
```

Could you open the issue on the devtools repository? thanks!

```

## 4810
Title:
```

        Different behaviour of :value and v-model in a select tag when dynamically adding options while none is yet selected
      
```
Author:
```
jonjanisch
```
Text:
```

My custom "select" component behaves differently when compared to simply using a raw select element in my template.
When the custom select's value is null and the options are loaded async, the first option is automatically selected.
Expected: The custom select's "selected" value should remain empty. This is the behavior when using a raw select in the template (not a custom component).
Here's a simple fiddle illustrating the issue:
https://jsfiddle.net/33df9qu8/3/

If you uncomment the option with a null optionId in my fiddle:
{ text: 'Not selected', optionId: null },
...the select behaves perfectly fine and selects that option. But that's not really a workaround as it forces us to add a null option and changes our UX.
It may be related to these similar issues here:
#1008
#3673
Vue.js version
2.1.10
Chrome version
55.0.2883.95 (64-bit)
Reproduction Link
https://jsfiddle.net/33df9qu8/3/

```
Author:
```
posva
```
Text:
```

The behaviour is different because of the value binding instead of the v-model.
As a workaround you can use a computed property in the custom select and use the v-model directive instead of :value
https://jsfiddle.net/dux6q43p/

```
Author:
```
jonjanisch
```
Text:
```

Thank you. The workaround worked great but I'm not quite sure why it works. Is there anywhere in the docs where this is explained further?

```
Author:
```
jonjanisch
```
Text:
```

I noticed that neither my custom select nor the workaround demonstrated by @posva handle a null option properly (contrary to what I originally stated in my first comment).
{ text: 'Yellow', optionId: 'YELLOW'},
{ text: 'Not selected', optionId: null }, // <--- null option
{ text: 'Blue', optionId: 'BLUE'}

If the original select value is null, it properly selects Not Selected when the options are added dynamically initially. However, if you toggle to Blue and then back to Not selected, it will show an empty combobox (instead of Not Selected).
EDIT: For completeness I found a workaround for this problem as well. But it would be nice if component developers did not have to do this.  I've updated the fiddle with the following workaround:
onChange(value) {
  if (value === '') {
    value = null;
  }
  this.$emit('input', value);
}

See here:
https://jsfiddle.net/dux6q43p/1/

```
Author:
```
posva
```
Text:
```

That's actually because the value of the select dom element is always a string. So instead of being null, it's just an empty string

```
Author:
```
tiagomatosweb
```
Text:
```

I think I'm experiencing something similar to this issue. I have asked in here, but not luck yet https://forum.vuejs.org/t/vuejs-ajax-populating-select-and-weird-behaviour/6222.
However I could figure out any workaround! Can someone give me a clue?
Much appreciated.

```
Author:
```
yyx990803
```
Text:
```

Closing due to inactivity (also because a workaround has been pointed out).

```

## 7030
Title:
```

        img src being [Object Object]
      
```
Author:
```
yyccQQu
```
Text:
```





import imgUP from 'common/SVG/thumb_up.svg'
import imgDown from 'common/SVG/thumb_down.svg'
data() {
return{
imgUP,
imgDown
}
The work is "",   Why ?

```
Author:
```
vue-bot
```
Text:
```

Hello, your issue has been closed because it does not conform to our issue requirements. Please use the Issue Helper to create an issue - thank you!

```

## 2635
Title:
```

        vue现在的版本可以对<input type="file"> 模型绑定么
      
```
Author:
```
erbing
```
Text:
```


No description provided.


```
Author:
```
erbing
```
Text:
```

最后，采取了最糟糕的做法，操作DOM ......     T T

```
Author:
```
yyx990803
```
Text:
```

v-model 不支持 type="file"，需要自行用第三方库处理。

```

## 2836
Title:
```

        Can I pass data of a component to its slot (so users can get data from slot)?
      
```
Author:
```
hectorguo
```
Text:
```

I have viewed this example created by Evan, it looks great to custom and repeat  elements.
<!-- Component -->
<script>
Vue.component('test_slot', {
    template: '<table><thead><th v-for="item in items">{{item}}</th></thead><tbody><tr v-for="item in items"><td><slot name="test"></slot><td></tr></tbody></table>',
    props: ["items"]
});
<script>

<!-- APP -->
<test_slot :items="items">
    <span slot="test">foo</span>
</test_slot>

<script>
new Vue({
    el: 'body',
    data: {
        items: ['A', 'B', 'C']
    }
})
</script>
but I wonder if I could pass some dynamic data to the slot.
Something like this:
<test_slot :items="items">
    <span slot="test">{{item}}</span>
</test_slot>
Note that, {{item}} is from v-for="item in items".
and it will render like this:
<td>A</td>
<td>B</td>
<td>C</td>
rather than the fixed value:
<td>foo</td>
<td>foo</td>
<td>foo</td>
I am not sure if there are some solutions to support this feature.
Ask for help !!!

```
Author:
```
fnlctrl
```
Text:
```

I think it's not possible because v-for is compiled inside test_slot's scope, and <span slot="test">{{item}}</span> is compiled inside body's scope.

```
Author:
```
phanan
```
Text:
```

Please adhere to the contributing guide and direct this question to Gitter or the forum. I'm sure you'll get lots of help there. If you believe this is a missing feature and want to request for it instead, feel free to modify/reword this issue as such, or open a new one. Thanks.

```
Author:
```
simplesmiler
```
Text:
```

@fnlctrl #2509 (comment)

```
Author:
```
fnlctrl
```
Text:
```

@simplesmiler Thanks!

```

## 4277
Title:
```

        list items delete and refresh of virtual dom
      
```
Author:
```
Hishengs
```
Text:
```

vue version: 2.0.7
I have a list( fetched by Ajax from server ) on my page which looks like :
(generated by using v-for)
<ul>
    <li id="a"></li>
    <li id="b"></li>
    <li id="c"></li>
</ul>

then I want to delete an item, such as item b, first I use jQuery to hide the element, and then send a delete request to server, then fetch  new data and replace the old items.

(use jQuery to hide item b: $('#b').hide() )

<ul>
    <li id="a"></li>
    <li id="b" style="display:none;"></li>
    <li id="c"></li>
</ul>

2.send request and got new data, the list should be:
<ul>
    <li id="a"></li>
    <li id="c"></li>
</ul>

but it showed to be:
<ul>
    <li id="a"></li>
    <li id="c" style="display:none;"></li>
</ul>

the last one item was hidden.
I have try using document.getElementById('b') to delete item, but it still the same.
If using $().remove(), the new last one also be removed.
and then I try hide all the items after delete one item.then fetch new data to build the list. but it cames that the all new items was hidden...I'm now so confused.

```
Author:
```
yyx990803
```
Text:
```

Please make sure to read the Issue Reporting Guidelines before opening new issues. The issue list only accepts bug reports and feature requests. Questions should be posted to the Gitter chat room,  forum or StackOverflow. Thanks.

```

## 1048
Title:
```

        Global event 
      
```
Author:
```
thelinuxlich
```
Text:
```

It would be useful if $dispatch(or a new method) could trigger a event for every vm, independently of the hierarchy

```
Author:
```
yyx990803
```
Text:
```

You could just use an external event bus for that.

```
Author:
```
azamat-sharapov
```
Text:
```

Speaking about external event buses, what do you recommend Evan? haven't ever used one, advice appreciated.

```
Author:
```
yyx990803
```
Text:
```

@azamat-sharapov Node's built-in EventEmitter is probably the easiest one. Both webpack and browserify mock it for you I believe. Or you can also use https://www.npmjs.com/package/component-emitter or https://github.com/mroderick/PubSubJS

```
Author:
```
azamat-sharapov
```
Text:
```

Thank you

```
Author:
```
MAAARKIN
```
Text:
```

@yyx990803 i'm using vuejs and i'm try to emit a event global like u recommend, i trying to do something like this:
...
eventEmitter.emit('my-event', 'my-message');
and in my other component ComponentB.vue
i do like this:
events: {
'my-event': function (msg) {
console.log(msg)
}
}
can i use events: {} from the componentB to get my event?

```
Author:
```
LinusBorg
```
Text:
```

@MAAARKIN No. you will have to register a listener on the same bus, like eventEmitter.on(cb)
Also, this issue is closed and Github issues are reserved for feature proposals and bug reports.
Please consider opening a thread on our community forums at forum.vuejs.org

```

## 3210
Title:
```

        Parsing object as a filter argument fails with spaces inside
      
```
Author:
```
sqal
```
Text:
```

Vue.js version
1.0.26
Reproduction Link
https://jsfiddle.net/0o853fzd/
Take a look at example. You can see that when i try to pass object to the filter as an argument it doesn't work when there is some space in the string.

Isn't supposed to PR #834 fix this issue? or is it forbidden to use spaces when passing obejct to the filter like this?

```
Author:
```
yyx990803
```
Text:
```

This is because the 1.x filter syntax uses space as the argument delimiter. If anyone wants to work on this, the relevant logic is here: https://github.com/vuejs/vue/blob/dev/src/parsers/directive.js#L20-L35

```
Author:
```
defcc
```
Text:
```

I am working on a simple expression parser to parse the filter syntax rather then the regex way。Is it an acceptable method ? If so I will make a pull request soon.

```
Author:
```
yyx990803
```
Text:
```

@defcc code size is also a concern here. We don't want to bloat the code for a relatively rare use case.

```
Author:
```
defcc
```
Text:
```

ok, got it. @yyx990803

```

## 10132
Title:
```

        <transition> updates item slot while animating in, but not while animating out
      
```
Author:
```
sp00x
```
Text:
```

Version
2.6.10
Reproduction link
https://codesandbox.io/s/vue-template-lfgvz
Steps to reproduce
Press "add" to animate in some items - the timer and color changes according to the "state" property - in both upper and lower versions.
Press "remove" on an item and the timer and color is "frozen" with what it was when last rendered in a "visible" state (in the lower list, with transition) but keeps updating in the upper (logically, since it's not being transitioned)
What is expected?
Same behavior of in and out - that the slot is alive and reactive to changes as it is while animating in
What is actually happening?
Different behavior of in and out

I understand this may be in an attempt to optimize something, but maybe an additional property for  could be added to get the same behavior of in and out?
The example is not really how I was planning to use this, but just to illustrate the problem.

```
Author:
```
posva
```
Text:
```

It doesn't update because the element is being removed per v-if being false. It is consistent with v if which prevents anything inside from rendering. If you want to animate something and then remove it yourself, you can listen to the same event and remove the wrapper after the transitionend or animationend event is triggered

```

## 9737
Title:
```

        datetime-picker支持itemHeight
      
```
Author:
```
Dongsheng-Zhang
```
Text:
```

What problem does this feature solve?
可以自定义高度
What does the proposed API look like?
:itemHeight

```
Author:
```
Dongsheng-Zhang
```
Text:
```

<mt-datetime-picker  ref="picker"  confirmText="确认"  v-model="pickerVisible"  type="date"  :visibleItemCount="Number(3)"  :itemHeight="Number(50)"  year-format="{value} 年"  month-format="{value} 月"  date-format="{value} 日"  @confirm="handleConfirm()"> </mt-datetime-picker>

```
Author:
```
sodatea
```
Text:
```

这个跟 Vue 有什么关系……你想问的是某个组件库？请去组件库自己的仓库提 issue

```

## 3226
Title:
```

        web workers
      
```
Author:
```
wormen
```
Text:
```

tell me how to run Vue in  web workers
now he's not working because in web workers there is no window object

```
Author:
```
yyx990803
```
Text:
```

Please make sure to read the Issue Reporting Guidelines before opening new issues. The issue list only accepts bug reports and feature requests. Questions should be posted to the Gitter chat room,  forum or StackOverflow. Thanks.

```
Author:
```
matthiasg
```
Text:
```

@wormen did you find a way ? It seems it isn't possible just yet and its feasibility depends on the way the vdom is used after binding to actual dom nodes. It also imposes some code splitting since even if vue were capable of rendering from the web worker, any legacy e.g jquery stuff or other libraries would still have to render in the ui thread.
PS: I know this should be discussed on the Gitter chat room or forum or stackoverflow, but nobody answered there as far as I could find. At least not when the question was posted on Gitter.

```
Author:
```
wormen
```
Text:
```

@matthiasg Yes, I found a solution to his problem, but with VueJS has nothing to do

```
Author:
```
matthiasg
```
Text:
```

@wormen May I ask whether you are still using/considering Vue ? If not, is it because you the vue community wasn't responsive to your inquiry or because you needed rendering inside of web workers and had to look elsewhere?

```
Author:
```
andreiglingeanu
```
Text:
```

@matthiasg What's the point of doing rendering inside workers? Am I missing something very obvious or you're just having something super complex to render out?

```
Author:
```
wormen
```
Text:
```

@matthiasg the functionality, which I would like to take advantage of VueJS in web workers, I wrote myself as VueJS not use in web workers

```
Author:
```
matthiasg
```
Text:
```

@andreiglingeanu personally I don't need it right now, but I did investigate, since some DOM updates and other interactions in angular took a few ms which interfered with scrolling speed and caused intermittent slow downs. we ourselves are planning to move our product from Angular 1 to vue in the next few weeks and do need SSR but not necessarily web workers yet.
But we are interested in potentially rendering inside a service worker as an experimental option which would require a similar architecture. The idea being that the server could push certain data updates to dormant devices every once in a while and the service worker would use that to pre-render the matching HTML. When the client requested the html it would already be pre-filled with more up-to-date data and make full use of streaming rendering.

```
Author:
```
andreiglingeanu
```
Text:
```

@matthiasg Hm, you'll then have to set HTML to the actual DOM via some sort of v-html directive, no? I'm not sure if that's a more faster approach...

```
Author:
```
matthiasg
```
Text:
```

@andreiglingeanu there are a number of projects / blog posts discussing the merits with some example implementations. basically they render into the vdom in the worker then transmit the patch to the ui thread which then applies it to the actual dom and the dom event handlers forward to the web worker. there is more work total but spread across two threads (which most even low level phones have cores for) and the ui thread is not blocked easily by xmlhttprequest parsing etc.
but as I said its not a priority right now for us either. I am interested in seeing vue succeed though and was concerned that @wormen's question went totally without response of any kind. I am glad he found another solution for his issue of course

```

## 1655
Title:
```

        class name propagation
      
```
Author:
```
pcalin
```
Text:
```

vue components do not propagate css class names more than one level deep.
working example using jade:
parent component
  component1.first-class-name

component1
  div
final outcome:
div.first-class-name
perfect
however when using another components inside component1...
failing example using jade:
parent component
  component1.first-class-name

component1
  component2

component2
  div
final outcome:
div
the first-class-name is missing.

```
Author:
```
OEvgeny
```
Text:
```

It is by design. See docs: fragment instance.

```
Author:
```
yyx990803
```
Text:
```

As said, this is by design. Will have better warnings in this case in later releases.

```

## 9840
Title:
```

        Memory leak when using "transition" and "keep-alive"
      
```
Author:
```
Aaron-Bird
```
Text:
```

Why are some "Vue Component" not cleared when using "transition" and "keep-alive"?
I wrote a demo:
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>demo</title>
  </head>
  <body>
    <script src="https://unpkg.com/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>

    <div id="app">
      <transition>
        <keep-alive include="foo">
          <router-view></router-view>
        </keep-alive>
      </transition>
    </div>
    <script>
      const Foo = {
        name: "foo",
        template: `<div><router-link to="/bar">Go to Bar</router-link></div>`
      };
      const Bar = {
        name: "bar",
        template: `<div><router-link to="/foo">Go to Foo</router-link></div>`
      };
      const routes = [
        { path: "/foo", component: Foo, alias: "/" },
        { path: "/bar", component: Bar }
      ];
      const router = new VueRouter({
        routes
      });
      const app = new Vue({
        router
      }).$mount("#app");
    </script>
  </body>
</html>
The debugging process is as follows:
1 Click "Collect garbage" and "take heap snapshot"(snapshot 1)
2 Click the routing button on the left 10 times, then click "Collect garbage" and "take heap snapshot"(snapshot 2)
3 Click the routing button on the left 10 times, then click "Collect garbage" and "take heap snapshot"(snapshot 3)

The generated "snapshot" is as follows:
snapshot 1:

snapshot 2:

snapshot 3:

VueComponent is not being recycled, is this a bug?

```
Author:
```
vue-bot
```
Text:
```

Hello, your issue has been closed because it does not conform to our issue requirements. In order to ensure every issue provides the necessary information for us to investigate, we require the use of the Issue Helper when creating new issues. Thank you!

```
Author:
```
posva
```
Text:
```

If you open a new issue again, please remove vue-router. There is already an open bug on vue router about keep-alive + transition

```
Author:
```
Aaron-Bird
```
Text:
```

@posva
Could you  delete this issue?

```
Author:
```
posva
```
Text:
```

it doesn't matter

```

# Pull
