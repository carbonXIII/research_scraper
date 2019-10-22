# vuejs/vue
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_packages_weex_vue_framework_README_md](#_packages_weex_vue_framework_README_md)

* [_benchmarks_ssr_README_md](#_benchmarks_ssr_README_md)

* [_dist_README_md](#_dist_README_md)

* [_packages_vue_server_renderer_README_md](#_packages_vue_server_renderer_README_md)

* [_packages_vue_template_compiler_README_md](#_packages_vue_template_compiler_README_md)

* [_examples_todomvc_readme_md](#_examples_todomvc_readme_md)

* [_BACKERS_md](#_BACKERS_md)

* [_github_ISSUE_TEMPLATE_md](#_github_ISSUE_TEMPLATE_md)

* [_packages_weex_template_compiler_README_md](#_packages_weex_template_compiler_README_md)

* [_github_PULL_REQUEST_TEMPLATE_md](#_github_PULL_REQUEST_TEMPLATE_md)

* [_github_CONTRIBUTING_md](#_github_CONTRIBUTING_md)

* [_github_CODE_OF_CONDUCT_md](#_github_CODE_OF_CONDUCT_md)

* [_README_md](#_README_md)

* [_github_COMMIT_CONVENTION_md](#_github_COMMIT_CONVENTION_md)

[- Inline](#Inline)

* [_src_core_global_api_use_js](#_src_core_global_api_use_js)

* [_src_platforms_weex_runtime_modules_class_js](#_src_platforms_weex_runtime_modules_class_js)

* [_src_core_util_perf_js](#_src_core_util_perf_js)

* [_src_core_vdom_modules_ref_js](#_src_core_vdom_modules_ref_js)

* [_test_weex_compiler_style_spec_js](#_test_weex_compiler_style_spec_js)

* [_src_core_config_js](#_src_core_config_js)

* [_src_shared_constants_js](#_src_shared_constants_js)

* [_src_core_observer_array_js](#_src_core_observer_array_js)

* [_test_unit_features_component_component_keep_alive_spec_js](#_test_unit_features_component_component_keep_alive_spec_js)

* [_src_platforms_web_entry_server_renderer_js](#_src_platforms_web_entry_server_renderer_js)

* [_test_ssr_fixtures_async_bar_js](#_test_ssr_fixtures_async_bar_js)

* [_test_unit_features_options_inheritAttrs_spec_js](#_test_unit_features_options_inheritAttrs_spec_js)

* [_src_platforms_weex_runtime_modules_events_js](#_src_platforms_weex_runtime_modules_events_js)

* [_src_core_global_api_assets_js](#_src_core_global_api_assets_js)

* [_packages_vue_template_compiler_build_js](#_packages_vue_template_compiler_build_js)

* [_src_platforms_web_runtime_directives_model_js](#_src_platforms_web_runtime_directives_model_js)

* [_test_unit_modules_observer_watcher_spec_js](#_test_unit_modules_observer_watcher_spec_js)

* [_test_unit_features_options_template_spec_js](#_test_unit_features_options_template_spec_js)

* [_src_platforms_web_compiler_options_js](#_src_platforms_web_compiler_options_js)

* [_test_weex_helpers_index_js](#_test_weex_helpers_index_js)

[- Issues](#Issues)

* [8637](#8637)

* [6466](#6466)

* [9024](#9024)

* [632](#632)

* [568](#568)

* [1052](#1052)

* [7241](#7241)

* [2727](#2727)

* [8257](#8257)

* [2798](#2798)

* [2044](#2044)

* [3991](#3991)

* [9664](#9664)

* [10081](#10081)

* [9707](#9707)

* [3554](#3554)

* [6654](#6654)

[- Pull](#Pull)

* [9116](#9116)

* [7450](#7450)

<!-- toc -->

# Info
## description
🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web.

# Markdown
## _packages_weex_vue_framework_README_md
```# weex-vue-framework

> This package is auto-generated. For pull requests please see [src/platforms/weex/entry-framework.js](https://github.com/vuejs/vue/blob/dev/src/platforms/weex/entry-framework.js).
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
## _packages_weex_template_compiler_README_md
```# weex-template-compiler

> This package is auto-generated. For pull requests please see [src/platforms/weex/entry-compiler.js](https://github.com/vuejs/vue/tree/dev/src/platforms/weex/entry-compiler.js).
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
## _src_core_global_api_use_js
### Line 7-16
```
    const installedPlugins = (this._installedPlugins || (this._installedPlugins = []))
    if (installedPlugins.indexOf(plugin) > -1) {
      return this
    }

    // additional parameters
    const args = toArray(arguments, 1)
    args.unshift(this)
    if (typeof plugin.install === 'function') {
      plugin.install.apply(plugin, args)
```

## _src_platforms_weex_runtime_modules_class_js
### Line 32-41
```
  }
}

function makeClassList (data: VNodeData): Array<string> {
  const classList = []
  // unlike web, weex vnode staticClass is an Array
  const staticClass: any = data.staticClass
  const dataClass = data.class
  if (staticClass) {
    classList.push.apply(classList, staticClass)
```
### Line 49-59
```
  }
  return classList
}

function getStyle (oldClassList: Array<string>, classList: Array<string>, ctx: Component): Object {
  // style is a weex-only injected object
  // compiled from <style> tags in weex files
  const stylesheet: any = ctx.$options.style || {}
  const result = {}
  classList.forEach(name => {
    const style = stylesheet[name]
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

## _test_weex_compiler_style_spec_js

## _src_core_config_js
### Line 7-16
```
} from 'shared/util'

import { LIFECYCLE_HOOKS } from 'shared/constants'

export type Config = {
  // user
  optionMergeStrategies: { [key: string]: Function };
  silent: boolean;
  productionTip: boolean;
  performance: boolean;
```
### Line 18-46
```
  errorHandler: ?(err: Error, vm: Component, info: string) => void;
  warnHandler: ?(msg: string, vm: Component, trace: string) => void;
  ignoredElements: Array<string | RegExp>;
  keyCodes: { [key: string]: number | Array<number> };

  // platform
  isReservedTag: (x?: string) => boolean;
  isReservedAttr: (x?: string) => boolean;
  parsePlatformTagName: (x: string) => string;
  isUnknownElement: (x?: string) => boolean;
  getTagNamespace: (x?: string) => string | void;
  mustUseProp: (tag: string, type: ?string, name: string) => boolean;

  // private
  async: boolean;

  // legacy
  _lifecycleHooks: Array<string>;
};

export default ({
  /**
   * Option merge strategies (used in core/util/options)
   */
  // $flow-disable-line
  optionMergeStrategies: Object.create(null),

  /**
   * Whether to suppress warnings.
```
### Line 78-87
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

## _src_shared_constants_js

## _src_core_observer_array_js
### Line 20-29
```

/**
 * Intercept mutating methods and emit events
 */
methodsToPatch.forEach(function (method) {
  // cache original method
  const original = arrayProto[method]
  def(arrayMethods, method, function mutator (...args) {
    const result = original.apply(this, args)
    const ob = this.__ob__
```
### Line 36-45
```
      case 'splice':
        inserted = args.slice(2)
        break
    }
    if (inserted) ob.observeArray(inserted)
    // notify change
    ob.dep.notify()
    return result
  })
})
```

## _test_unit_features_component_component_keep_alive_spec_js
### Line 154-163
```
    }).then(() => {
      expect(vm.$el.textContent).toBe('two')
      assertHookCalls(one, [1, 1, 2, 1, 0])
      assertHookCalls(two, [1, 1, 2, 1, 0])
    }).then(() => {
      // toggle sub component when activated
      oneInstance.ok = false
    }).then(() => {
      expect(vm.$el.textContent).toBe('')
      assertHookCalls(one, [1, 1, 2, 1, 0])
```
### Line 173-182
```
    }).then(() => {
      expect(vm.$el.textContent).toBe('')
      assertHookCalls(one, [1, 1, 2, 2, 0])
      assertHookCalls(two, [1, 1, 3, 3, 0])
    }).then(() => {
      // toggle sub component when parent is deactivated
      oneInstance.ok = false
    }).then(() => {
      expect(vm.$el.textContent).toBe('')
      assertHookCalls(one, [1, 1, 2, 2, 0])
```
### Line 415-424
```
      assertHookCalls(two, [1, 1, 1, 0, 0])
      vm.include = 'one'
      vm.view = 'one'
    }).then(() => {
      assertHookCalls(one, [1, 1, 2, 1, 0])
      // two should be pruned
      assertHookCalls(two, [1, 1, 1, 1, 1])
    }).then(done)
  })

```
### Line 447-456
```
      assertHookCalls(one, [1, 1, 1, 0, 1])
      assertHookCalls(two, [1, 1, 1, 0, 0])
    }).then(done)
  })

  // #3882
  it('deeply nested keep-alive should be destroyed properly', done => {
    one.template = `<div><keep-alive><two></two></keep-alive></div>`
    one.components = { two }
    const vm = new Vue({
```
### Line 472-481
```
      assertHookCalls(one, [1, 1, 1, 1, 1])
      assertHookCalls(two, [1, 1, 1, 1, 1])
    }).then(done)
  })

  // #4237
  it('should update latest props/listeners for a re-activated component', done => {
    const one = {
      props: ['prop'],
      template: `<div>one {{ prop }}</div>`
```
### Line 557-574
```
    vm.n = 'bb'
    waitForUpdate(() => {
      assertCount([1, 0, 1, 0, 0, 0])
      vm.n = 'cc'
    }).then(() => {
      // should prune A because max cache reached
      assertCount([1, 1, 1, 0, 1, 0])
      vm.n = 'bb'
    }).then(() => {
      // B should be reused, and made latest
      assertCount([1, 1, 1, 0, 1, 0])
      vm.n = 'aa'
    }).then(() => {
      // C should be pruned because B was used last so C is the oldest cached
      assertCount([2, 1, 1, 0, 1, 1])
    }).then(done)
  })

```
### Line 577-586
```
      template: `<keep-alive><foo/></keep-alive>`
    }).$mount()
    expect(`Unknown custom element: <foo>`).toHaveBeenWarned()
  })

  // #6938
  it('should not cache anonymous component when include is specified', done => {
    const Foo = {
      name: 'foo',
      template: `<div>foo</div>`,
```
### Line 683-692
```
      expect(vm.$el.textContent).toBe('bar')
      assert(1, 1)
    }).then(done)
  })

  // #7105
  it('should not destroy active instance when pruning cache', done => {
    const Foo = {
      template: `<div>foo</div>`,
      destroyed: jasmine.createSpy('destroyed')
```
### Line 702-711
```
      data: {
        include: ['foo']
      },
      components: { Foo }
    }).$mount()
    // condition: a render where a previous component is reused
    vm.include = ['foo']
    waitForUpdate(() => {
      vm.include = ['']
    }).then(() => {
```
### Line 1007-1022
```
      }).thenWaitFor(nextFrame).then(() => {
        expect(vm.$el.innerHTML).toBe(
          '<div class="test">one</div>' +
          '<div class="test test-enter-active test-enter-to">two</div>'
        )
        // switch again before enter finishes,
        // this cancels both enter and leave.
        vm.view = 'one'
      }).then(() => {
        // 1. the pending leaving "one" should be removed instantly.
        // 2. the entering "two" should be placed into its final state instantly.
        // 3. a new "one" is created and entering
        expect(vm.$el.innerHTML).toBe(
          '<div class="test">two</div>' +
          '<div class="test test-enter test-enter-active">one</div>'
        )
```
### Line 1045-1054
```
          '<div class="test">one</div>'
        )
      }).then(done).then(done)
    })

    // #4339
    it('component with inner transition', done => {
      const vm = new Vue({
        template: `
          <div>
```
### Line 1062-1071
```
          foo: { template: '<transition><div class="test">foo</div></transition>' },
          bar: { template: '<transition name="test"><div class="test">bar</div></transition>' }
        }
      }).$mount(el)

      // should not apply transition on initial render by default
      expect(vm.$el.innerHTML).toBe('<div class="test">foo</div>')
      vm.view = 'bar'
      waitForUpdate(() => {
        expect(vm.$el.innerHTML).toBe(
```
### Line 1150-1159
```
        }).thenWaitFor(nextFrame).then(() => {
          expect(vm.$el.innerHTML).toBe(
            '<div class="test test-enter-active test-enter-to">one</div>'
          )
        }).thenWaitFor(_next => { next = _next }).then(() => {
          // foo afterEnter get called
          expect(vm.$el.innerHTML).toBe('<div class="test">one</div>')
          vm.view = 'bar'
        }).thenWaitFor(nextFrame).then(() => {
          assertHookCalls(one, [1, 1, 1, 1, 0])
```
### Line 1160-1170
```
          assertHookCalls(two, [0, 0, 0, 0, 0])
          expect(vm.$el.innerHTML).toBe(
            '<div class="test test-leave-active test-leave-to">one</div><!---->'
          )
        }).thenWaitFor(_next => { next = _next }).then(() => {
          // foo afterLeave get called
          // and bar has already been resolved before afterLeave get called
          expect(barResolve.calls.count()).toBe(1)
          expect(vm.$el.innerHTML).toBe('<!---->')
        }).thenWaitFor(nextFrame).then(() => {
          expect(vm.$el.innerHTML).toBe(
```
### Line 1175-1184
```
        }).thenWaitFor(nextFrame).then(() => {
          expect(vm.$el.innerHTML).toBe(
            '<div class="test test-enter-active test-enter-to">two</div>'
          )
        }).thenWaitFor(_next => { next = _next }).then(() => {
          // bar afterEnter get called
          expect(vm.$el.innerHTML).toBe('<div class="test">two</div>')
        }).then(done)
      }
    })
```

## _src_platforms_web_entry_server_renderer_js
### Line 16-26
```
} {
  return _createRenderer(extend(extend({}, options), {
    isUnaryTag,
    canBeLeftOpenTag,
    modules,
    // user can provide server-side implementations for custom directives
    // when creating the renderer.
    directives: extend(baseDirectives, options.directives)
  }))
}

```

## _test_ssr_fixtures_async_bar_js

## _test_unit_features_options_inheritAttrs_spec_js

## _src_platforms_weex_runtime_modules_events_js

## _src_core_global_api_assets_js

## _packages_vue_template_compiler_build_js
### Line 9-19
```

/*  */

var emptyObject = Object.freeze({});

// These helpers produce better VM code in JS engines due to their
// explicitness and function inlining.
function isUndef (v) {
  return v === undefined || v === null
}

```
### Line 22-31
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
### Line 215-231
```
var isUnaryTag = makeMap(
  'area,base,br,col,embed,frame,hr,img,input,isindex,keygen,' +
  'link,meta,param,source,track,wbr'
);

// Elements that you can, intentionally, leave open
// (and which close themselves)
var canBeLeftOpenTag = makeMap(
  'colgroup,dd,dt,li,options,p,td,tfoot,th,thead,tr,source'
);

// HTML5 tags https://html.spec.whatwg.org/multipage/indices.html#elements-3
// Phrasing Content https://html.spec.whatwg.org/multipage/dom.html#phrasing-content
var isNonPhrasingTag = makeMap(
  'address,article,aside,base,blockquote,body,caption,col,colgroup,dd,' +
  'details,dialog,div,dl,dt,fieldset,figcaption,figure,footer,form,' +
  'h1,h2,h3,h4,h5,h6,head,header,hgroup,hr,html,legend,li,menuitem,meta,' +
```
### Line 256-278
```

/**
 * Not type-checking this file because it's mostly vendor code.
 */

// Regular Expressions for parsing tags and attributes
var attribute = /^\s*([^\s"'<>\/=]+)(?:\s*(=)\s*(?:"([^"]*)"+|'([^']*)'+|([^\s"'=<>`]+)))?/;
var dynamicArgAttribute = /^\s*((?:v-[\w-]+:|@|:|#)\[[^=]+\][^\s"'<>\/=]*)(?:\s*(=)\s*(?:"([^"]*)"+|'([^']*)'+|([^\s"'=<>`]+)))?/;
var ncname = "[a-zA-Z_][\\-\\.0-9_a-zA-Z" + (unicodeRegExp.source) + "]*";
var qnameCapture = "((?:" + ncname + "\\:)?" + ncname + ")";
var startTagOpen = new RegExp(("^<" + qnameCapture));
var startTagClose = /^\s*(\/?)>/;
var endTag = new RegExp(("^<\\/" + qnameCapture + "[^>]*>"));
var doctype = /^<!DOCTYPE [^>]+>/i;
// #7298: escape - to avoid being pased as HTML comment when inlined in page
var comment = /^<!\--/;
var conditionalComment = /^<!\[/;

// Special Elements (can contain anything)
var isPlainTextElement = makeMap('script,style,textarea', true);
var reCache = {};

var decodingMap = {
```
### Line 285-294
```
  '&#39;': "'"
};
var encodedAttr = /&(?:lt|gt|quot|amp|#39);/g;
var encodedAttrWithNewLines = /&(?:lt|gt|quot|amp|#39|#10|#9);/g;

// #5992
var isIgnoreNewlineTag = makeMap('pre,textarea', true);
var shouldIgnoreFirstNewline = function (tag, html) { return tag && isIgnoreNewlineTag(tag) && html[0] === '\n'; };

function decodeAttr (value, shouldDecodeNewlines) {
```
### Line 303-316
```
  var canBeLeftOpenTag$$1 = options.canBeLeftOpenTag || no;
  var index = 0;
  var last, lastTag;
  while (html) {
    last = html;
    // Make sure we're not in a plaintext content element like script/style
    if (!lastTag || !isPlainTextElement(lastTag)) {
      var textEnd = html.indexOf('<');
      if (textEnd === 0) {
        // Comment:
        if (comment.test(html)) {
          var commentEnd = html.indexOf('-->');

          if (commentEnd >= 0) {
```
### Line 320-329
```
            advance(commentEnd + 3);
            continue
          }
        }

        // http://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment
        if (conditionalComment.test(html)) {
          var conditionalEnd = html.indexOf(']>');

          if (conditionalEnd >= 0) {
```
### Line 330-355
```
            advance(conditionalEnd + 2);
            continue
          }
        }

        // Doctype:
        var doctypeMatch = html.match(doctype);
        if (doctypeMatch) {
          advance(doctypeMatch[0].length);
          continue
        }

        // End tag:
        var endTagMatch = html.match(endTag);
        if (endTagMatch) {
          var curIndex = index;
          advance(endTagMatch[0].length);
          parseEndTag(endTagMatch[1], curIndex, index);
          continue
        }

        // Start tag:
        var startTagMatch = parseStartTag();
        if (startTagMatch) {
          handleStartTag(startTagMatch);
          if (shouldIgnoreFirstNewline(startTagMatch.tagName, html)) {
```
### Line 366-375
```
          !endTag.test(rest) &&
          !startTagOpen.test(rest) &&
          !comment.test(rest) &&
          !conditionalComment.test(rest)
        ) {
          // < in plain text, be forgiving and treat it as text
          next = rest.indexOf('<', 1);
          if (next < 0) { break }
          textEnd += next;
          rest = html.slice(textEnd);
```
### Line 419-428
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
### Line 500-523
```
  function parseEndTag (tagName, start, end) {
    var pos, lowerCasedTagName;
    if (start == null) { start = index; }
    if (end == null) { end = index; }

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
      for (var i = stack.length - 1; i >= pos; i--) {
        if (process.env.NODE_ENV !== 'production' &&
          (i > pos || !tagName) &&
          options.warn
```
### Line 530-539
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
### Line 651-661
```
      currentBlock.end = start;
      var text = content.slice(currentBlock.start, currentBlock.end);
      if (options.deindent !== false) {
        text = deindent(text);
      }
      // pad content so that linters and pre-processors can output correct
      // line numbers in errors and warnings
      if (currentBlock.type !== 'template' && options.pad) {
        text = padContent(currentBlock, options.pad) + text;
      }
      currentBlock.content = text;
```
### Line 686-698
```
  return sfc
}

/*  */

// can we use __proto__?
var hasProto = '__proto__' in {};

// Browser environment sniffing
var inBrowser = typeof window !== 'undefined';
var inWeex = typeof WXEnvironment !== 'undefined' && !!WXEnvironment.platform;
var weexPlatform = inWeex && WXEnvironment.platform.toLowerCase();
var UA = inBrowser && window.navigator.userAgent.toLowerCase();
```
### Line 703-712
```
var isIOS = (UA && /iphone|ipad|ipod|ios/.test(UA)) || (weexPlatform === 'ios');
var isChrome = UA && /chrome\/\d+/.test(UA) && !isEdge;
var isPhantomJS = UA && /phantomjs/.test(UA);
var isFF = UA && UA.match(/firefox\/(\d+)/);

// Firefox has a "watch" function on Object.prototype...
var nativeWatch = ({}).watch;
if (inBrowser) {
  try {
    var opts = {};
```
### Line 716-742
```
    })); // https://github.com/facebook/flow/issues/285
    window.addEventListener('test-passive', null, opts);
  } catch (e) {}
}

// this needs to be lazy-evaled because vue may be required before
// vue-server-renderer can set VUE_ENV
var _isServer;
var isServerRendering = function () {
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
var devtools = inBrowser && window.__VUE_DEVTOOLS_GLOBAL_HOOK__;

/* istanbul ignore next */
function isNative (Ctor) {
```
### Line 748-760
```
  typeof Reflect !== 'undefined' && isNative(Reflect.ownKeys);

var _Set;
/* istanbul ignore if */ // $flow-disable-line
if (typeof Set !== 'undefined' && isNative(Set)) {
  // use native Set when available.
  _Set = Set;
} else {
  // a non-standard Set polyfill that only works with primitive keys.
  _Set = /*@__PURE__*/(function () {
    function Set () {
      this.set = Object.create(null);
    }
```
### Line 799-808
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
### Line 840-849
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
### Line 1009-1033
```
    Dep.target.addDep(this);
  }
};

Dep.prototype.notify = function notify () {
  // stabilize the subscriber list first
  var subs = this.subs.slice();
  if (process.env.NODE_ENV !== 'production' && !config.async) {
    // subs aren't sorted in scheduler if not running async
    // we need to sort them now to make sure they fire in correct
    // order
    subs.sort(function (a, b) { return a.id - b.id; });
  }
  for (var i = 0, l = subs.length; i < l; i++) {
    subs[i].update();
  }
};

// The current target watcher being evaluated.
// This is globally unique because only one watcher
// can be evaluated at a time.
Dep.target = null;

/*  */

```
### Line 1066-1075
```
  this.isAsyncPlaceholder = false;
};

var prototypeAccessors = { child: { configurable: true } };

// DEPRECATED: alias for componentInstance for backwards compat.
/* istanbul ignore next */
prototypeAccessors.child.get = function () {
  return this.componentInstance
};
```
### Line 1096-1105
```

/**
 * Intercept mutating methods and emit events
 */
methodsToPatch.forEach(function (method) {
  // cache original method
  var original = arrayProto[method];
  def(arrayMethods, method, function mutator () {
    var args = [], len = arguments.length;
    while ( len-- ) args[ len ] = arguments[ len ];
```
### Line 1115-1124
```
      case 'splice':
        inserted = args.slice(2);
        break
    }
    if (inserted) { ob.observeArray(inserted); }
    // notify change
    ob.dep.notify();
    return result
  });
});
```
### Line 1175-1184
```
  for (var i = 0, l = items.length; i < l; i++) {
    observe(items[i]);
  }
};

// helpers

/**
 * Augment a target Object or Array by intercepting
 * the prototype chain using __proto__
```
### Line 1243-1252
```
  var property = Object.getOwnPropertyDescriptor(obj, key);
  if (property && property.configurable === false) {
    return
  }

  // cater for pre-defined getter/setters
  var getter = property && property.get;
  var setter = property && property.set;
  if ((!getter || setter) && arguments.length === 2) {
    val = obj[key];
```
### Line 1277-1286
```
      }
      /* eslint-enable no-self-compare */
      if (process.env.NODE_ENV !== 'production' && customSetter) {
        customSetter();
      }
      // #7981: for accessor properties without setter
      if (getter && !setter) { return }
      if (setter) {
        setter.call(obj, newVal);
      } else {
```
### Line 1378-1387
```
    ? Reflect.ownKeys(from)
    : Object.keys(from);

  for (var i = 0; i < keys.length; i++) {
    key = keys[i];
    // in case the object is already observed...
    if (key === '__ob__') { continue }
    toVal = to[key];
    fromVal = from[key];
    if (!hasOwn(to, key)) {
```
### Line 1404-1433
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
      var instanceData = typeof childVal === 'function'
        ? childVal.call(vm, vm)
        : childVal;
      var defaultData = typeof parentVal === 'function'
```
### Line 1533-1542
```
  parentVal,
  childVal,
  vm,
  key
) {
  // work around Firefox's Object.prototype.watch...
  if (parentVal === nativeWatch) { parentVal = undefined; }
  if (childVal === nativeWatch) { childVal = undefined; }
  /* istanbul ignore if */
  if (!childVal) { return Object.create(parentVal || null) }
```
### Line 1615-1638
```
  for (var i = 0; i < copies.length; i++) {
    copies[i]();
  }
}

// The nextTick behavior leverages the microtask queue, which can be accessed
// via either native Promise.then or MutationObserver.
// MutationObserver has wider support, however it is seriously bugged in
// UIWebView in iOS >= 9.3.3 when triggered in touch event handlers. It
// completely stops working after triggering a few times... so, if native
// Promise is available, we will use it:
/* istanbul ignore next, $flow-disable-line */
if (typeof Promise !== 'undefined' && isNative(Promise)) ; else if (!isIE && typeof MutationObserver !== 'undefined' && (
  isNative(MutationObserver) ||
  // PhantomJS and iOS 7.x
  MutationObserver.toString() === '[object MutationObserverConstructor]'
)) {
  // Use MutationObserver where native Promise is not available,
  // e.g. PhantomJS, iOS7, Android 4.4
  // (#6466 MutationObserver is unreliable in IE11)
  var counter = 1;
  var observer = new MutationObserver(flushCallbacks);
  var textNode = document.createTextNode(String(counter));
  observer.observe(textNode, {
```
### Line 1642-1655
```

/*  */

/*  */

// these are reserved for web because they are directly compiled away
// during template compilation
var isReservedAttr = makeMap('style,class');

// attributes that should be using props for binding
var acceptValue = makeMap('input,textarea,option,select,progress');
var mustUseProp = function (tag, type, attr) {
  return (
    (attr === 'value' && acceptValue(tag)) && type !== 'button' ||
```
### Line 1688-1698
```
  'output,progress,select,textarea,' +
  'details,dialog,menu,menuitem,summary,' +
  'content,element,shadow,template,blockquote,iframe,tfoot'
);

// this map is intentionally selective, only covering SVG elements that may
// contain child elements.
var isSVG = makeMap(
  'svg,animate,circle,clippath,cursor,defs,desc,ellipse,filter,font-face,' +
  'foreignObject,g,glyph,image,line,marker,mask,missing-glyph,path,pattern,' +
  'polygon,polyline,rect,switch,symbol,text,textpath,tspan,use,view',
```
### Line 1707-1717
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
### Line 1751-1760
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
### Line 1772-1781
```
        case 0x7D: curly--; break                 // }
      }
      if (c === 0x2f) { // /
        var j = i - 1;
        var p = (void 0);
        // find first non-whitespace prev char
        for (; j >= 0; j--) {
          p = exp.charAt(j);
          if (p !== ' ') { break }
        }
```
### Line 1807-1816
```
}

function wrapFilter (exp, filter) {
  var i = filter.indexOf('(');
  if (i < 0) {
    // _f: resolveFilter
    return ("_f(\"" + filter + "\")(" + exp + ")")
  } else {
    var name = filter.slice(0, i);
    var args = filter.slice(i + 1);
```
### Line 1843-1857
```
  var rawTokens = [];
  var lastIndex = tagRE.lastIndex = 0;
  var match, index, tokenValue;
  while ((match = tagRE.exec(text))) {
    index = match.index;
    // push text token
    if (index > lastIndex) {
      rawTokens.push(tokenValue = text.slice(lastIndex, index));
      tokens.push(JSON.stringify(tokenValue));
    }
    // tag token
    var exp = parseFilters(match[1].trim());
    tokens.push(("_s(" + exp + ")"));
    rawTokens.push({ '@binding': exp });
    lastIndex = index + match[0].length;
```
### Line 1896-1905
```
    : (el.attrs || (el.attrs = []));
  attrs.push(rangeSetItem({ name: name, value: value, dynamic: dynamic }, range));
  el.plain = false;
}

// add a raw attr (use this in preTransforms)
function addRawAttr (el, name, value, range) {
  el.attrsMap[name] = value;
  el.attrsList.push(rangeSetItem({ name: name, value: value }, range));
}
```
### Line 1940-1949
```
  warn,
  range,
  dynamic
) {
  modifiers = modifiers || emptyObject;
  // warn prevent and passive modifier
  /* istanbul ignore if */
  if (
    process.env.NODE_ENV !== 'production' && warn &&
    modifiers.prevent && modifiers.passive
```
### Line 1953-1964
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
      name = "(" + name + ")==='click'?'contextmenu':(" + name + ")";
    } else if (name === 'click') {
```
### Line 1971-1980
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
### Line 2039-2051
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
### Line 2265-2275
```
var len, str, chr, index, expressionPos, expressionEndPos;



function parseModel (val) {
  // Fix https://github.com/vuejs/vue/pull/7730
  // allow v-model="obj.val " (trailing whitespace)
  val = val.trim();
  len = val.length;

  if (val.indexOf('[') < 0 || val.lastIndexOf(']') < len - 1) {
```
### Line 2368-2377
```

var decodeHTMLCached = cached(he.decode);

var emptySlotScopeToken = "_empty_";

// configurable state
var warn$1;
var delimiters;
var transforms;
var preTransforms;
```
### Line 2437-2448
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
        if (process.env.NODE_ENV !== 'production') {
          checkRootConstraints(element);
        }
```
### Line 2462-2502
```
    if (currentParent && !element.forbidden) {
      if (element.elseif || element.else) {
        processIfConditions(element, currentParent);
      } else {
        if (element.slotScope) {
          // scoped slot
          // keep it in the children list so that v-else(-if) conditions can
          // find it as the prev node.
          var name = element.slotTarget || '"default"'
          ;(currentParent.scopedSlots || (currentParent.scopedSlots = {}))[name] = element;
        }
        currentParent.children.push(element);
        element.parent = currentParent;
      }
    }

    // final children cleanup
    // filter out scoped slots
    element.children = element.children.filter(function (c) { return !(c).slotScope; });
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
    for (var i = 0; i < postTransforms.length; i++) {
      postTransforms[i](element, options);
    }
  }

  function trimEndingWhitespace (el) {
    // remove trailing whitespace node
    if (!inPre) {
      var lastNode;
      while (
        (lastNode = el.children[el.children.length - 1]) &&
```
### Line 2533-2546
```
    shouldDecodeNewlines: options.shouldDecodeNewlines,
    shouldDecodeNewlinesForHref: options.shouldDecodeNewlinesForHref,
    shouldKeepComment: options.comments,
    outputSourceRange: options.outputSourceRange,
    start: function start (tag, attrs, unary, start$1, end) {
      // check namespace.
      // inherit parent ns if there is one
      var ns = (currentParent && currentParent.ns) || platformGetTagNamespace(tag);

      // handle IE svg bug
      /* istanbul ignore if */
      if (isIE && ns === 'svg') {
        attrs = guardIESVGBug(attrs);
      }
```
### Line 2581-2590
```
          "<" + tag + ">" + ', as they will not be parsed.',
          { start: element.start }
        );
      }

      // apply pre-transforms
      for (var i = 0; i < preTransforms.length; i++) {
        element = preTransforms[i](element, options) || element;
      }

```
### Line 2598-2607
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
### Line 2621-2630
```
      }
    },

    end: function end (tag, start, end$1) {
      var element = stack[stack.length - 1];
      // pop stack
      stack.length -= 1;
      currentParent = stack[stack.length - 1];
      if (process.env.NODE_ENV !== 'production' && options.outputSourceRange) {
        element.end = end$1;
```
### Line 2647-2656
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
### Line 2659-2673
```
      }
      var children = currentParent.children;
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
### Line 2674-2683
```
      } else {
        text = preserveWhitespace ? ' ' : '';
      }
      if (text) {
        if (!inPre && whitespaceOption === 'condense') {
          // condense consecutive whitespaces into single space
          text = text.replace(whitespaceRE, ' ');
        }
        var res;
        var child;
```
### Line 2702-2712
```
          children.push(child);
        }
      }
    },
    comment: function comment (text, start, end) {
      // adding anyting as a sibling to the root node is forbidden
      // comments should still be allowed, but ignored
      if (currentParent) {
        var child = {
          type: 3,
          text: text,
```
### Line 2743-2752
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
### Line 2754-2764
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
### Line 2911-2921
```
  if (once$$1 != null) {
    el.once = true;
  }
}

// handle content being passed to a component as slot,
// e.g. <template slot="xxx">, <div slot-scope="xxx">
function processSlotContent (el) {
  var slotScope;
  if (el.tag === 'template') {
    slotScope = getAndRemoveAttr(el, 'scope');
```
### Line 2943-2967
```
      );
    }
    el.slotScope = slotScope;
  }

  // slot="xxx"
  var slotTarget = getBindingAttr(el, 'slot');
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
      var slotBinding = getAndRemoveAttrByRegex(el, slotRE);
      if (slotBinding) {
        if (process.env.NODE_ENV !== 'production') {
          if (el.slotTarget || el.slotScope) {
```
### Line 2984-2993
```
        el.slotTarget = name;
        el.slotTargetDynamic = dynamic;
        el.slotScope = slotBinding.value || emptySlotScopeToken; // force it into a scoped slot for perf
      }
    } else {
      // v-slot on component, denotes default slot
      var slotBinding$1 = getAndRemoveAttrByRegex(el, slotRE);
      if (slotBinding$1) {
        if (process.env.NODE_ENV !== 'production') {
          if (!maybeComponent(el)) {
```
### Line 3008-3017
```
              "<template> syntax when there are other named slots.",
              slotBinding$1
            );
          }
        }
        // add the component's children to its default slot
        var slots = el.scopedSlots || (el.scopedSlots = {});
        var ref$1 = getSlotName(slotBinding$1);
        var name$1 = ref$1.name;
        var dynamic$1 = ref$1.dynamic;
```
### Line 3023-3034
```
            c.parent = slotContainer;
            return true
          }
        });
        slotContainer.slotScope = slotBinding$1.value || emptySlotScopeToken;
        // remove children as they are returned from scopedSlots now
        el.children = [];
        // mark el non-plain so data gets generated
        el.plain = false;
      }
    }
  }
```
### Line 3045-3060
```
        binding
      );
    }
  }
  return dynamicArgRE.test(name)
    // dynamic [name]
    ? { name: name.slice(1, -1), dynamic: true }
    // static name
    : { name: ("\"" + name + "\""), dynamic: false }
}

// handle <slot/> outlets
function processSlotOutlet (el) {
  if (el.tag === 'slot') {
    el.slotName = getBindingAttr(el, 'name');
    if (process.env.NODE_ENV !== 'production' && el.key) {
```
### Line 3083-3096
```
  var i, l, name, rawName, value, modifiers, syncGen, isDynamic;
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
### Line 3138-3147
```
                  warn$1,
                  list[i]
                );
              }
            } else {
              // handler w/ dynamic event name
              addHandler(
                el,
                ("\"update:\"+(" + name + ")"),
                syncGen,
```
### Line 3168-3177
```
          name = name.slice(1, -1);
        }
        addHandler(el, name, value, modifiers, false, warn$1, list[i], isDynamic);
      } else { // normal directives
        name = name.replace(dirRE, '');
        // parse arg
        var argMatch = name.match(argRE);
        var arg = argMatch && argMatch[1];
        isDynamic = false;
        if (arg) {
```
### Line 3185-3194
```
        if (process.env.NODE_ENV !== 'production' && name === 'model') {
          checkForAliasModel(el, value);
        }
      }
    } else {
      // literal attribute
      if (process.env.NODE_ENV !== 'production') {
        var res = parseText(value, delimiters);
        if (res) {
          warn$1(
```
### Line 3199-3209
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
### Line 3244-3253
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
### Line 3314-3325
```
    if (typeBinding) {
      var ifCondition = getAndRemoveAttr(el, 'v-if', true);
      var ifConditionExtra = ifCondition ? ("&&(" + ifCondition + ")") : "";
      var hasElse = getAndRemoveAttr(el, 'v-else', true) != null;
      var elseIfCondition = getAndRemoveAttr(el, 'v-else-if', true);
      // 1. checkbox
      var branch0 = cloneASTElement(el);
      // process for on the main node
      processFor(branch0);
      addRawAttr(branch0, 'type', 'checkbox');
      processElement(branch0, options);
      branch0.processed = true; // prevent it from double-processed
```
### Line 3326-3344
```
      branch0.if = "(" + typeBinding + ")==='checkbox'" + ifConditionExtra;
      addIfCondition(branch0, {
        exp: branch0.if,
        block: branch0
      });
      // 2. add radio else-if condition
      var branch1 = cloneASTElement(el);
      getAndRemoveAttr(branch1, 'v-for', true);
      addRawAttr(branch1, 'type', 'radio');
      processElement(branch1, options);
      addIfCondition(branch0, {
        exp: "(" + typeBinding + ")==='radio'" + ifConditionExtra,
        block: branch1
      });
      // 3. other
      var branch2 = cloneASTElement(el);
      getAndRemoveAttr(branch2, 'v-for', true);
      addRawAttr(branch2, ':type', typeBinding);
      processElement(branch2, options);
```
### Line 3374-3384
```

/*  */

var warn$2;

// in some cases, the event used has to be determined at runtime
// so we used some reserved tokens during compile.
var RANGE_TOKEN = '__r';

function model$1 (
  el,
```
### Line 3390-3400
```
  var modifiers = dir.modifiers;
  var tag = el.tag;
  var type = el.attrsMap.type;

  if (process.env.NODE_ENV !== 'production') {
    // inputs with type="file" are read only and setting the input's
    // value will throw an error.
    if (tag === 'input' && type === 'file') {
      warn$2(
        "<" + (el.tag) + " v-model=\"" + value + "\" type=\"file\">:\n" +
        "File inputs are read only. Use a v-on:change listener instead.",
```
### Line 3403-3412
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
### Line 3415-3424
```
    genRadioModel(el, value, modifiers);
  } else if (tag === 'input' || tag === 'textarea') {
    genDefaultModel(el, value, modifiers);
  } else if (!config.isReservedTag(tag)) {
    genComponentModel(el, value, modifiers);
    // component v-model doesn't need extra runtime
    return false
  } else if (process.env.NODE_ENV !== 'production') {
    warn$2(
      "<" + (el.tag) + " v-model=\"" + value + "\">: " +
```
### Line 3427-3436
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
### Line 3498-3508
```
  value,
  modifiers
) {
  var type = el.attrsMap.type;

  // warn if v-bind:value conflicts with v-model
  // except for inputs with v-bind:type
  if (process.env.NODE_ENV !== 'production') {
    var value$1 = el.attrsMap['v-bind:value'] || el.attrsMap[':value'];
    var typeBinding = el.attrsMap['v-bind:type'] || el.attrsMap[':type'];
    if (value$1 && !typeBinding) {
```
### Line 3603-3614
```
 */
function optimize (root, options) {
  if (!root) { return }
  isStaticKey = genStaticKeysCached(options.staticKeys || '');
  isPlatformReservedTag = options.isReservedTag || no;
  // first pass: mark all non-static nodes.
  markStatic(root);
  // second pass: mark static roots.
  markStaticRoots(root, false);
}

function genStaticKeys$1 (keys) {
```
### Line 3619-3630
```
}

function markStatic (node) {
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
### Line 3653-3664
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
### Line 3714-3723
```

var fnExpRE = /^([\w$_]+|\([^)]*?\))\s*=>|^function\s*(?:[\w$]+)?\s*\(/;
var fnInvokeRE = /\([^)]*?\);*$/;
var simplePathRE = /^[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*|\['[^']*?']|\["[^"]*?"]|\[\d+]|\[[A-Za-z_$][\w$]*])*$/;

// KeyboardEvent.keyCode aliases
var keyCodes = {
  esc: 27,
  tab: 9,
  enter: 13,
```
### Line 3727-3755
```
  right: 39,
  down: 40,
  'delete': [8, 46]
};

// KeyboardEvent.key aliases
var keyNames = {
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
var genGuard = function (condition) { return ("if(" + condition + ")return null;"); };

var modifierCode = {
  stop: '$event.stopPropagation();',
```
### Line 3810-3819
```
    var genModifierCode = '';
    var keys = [];
    for (var key in handler.modifiers) {
      if (modifierCode[key]) {
        genModifierCode += modifierCode[key];
        // left/right
        if (keyCodes[key]) {
          keys.push(key);
        }
      } else if (key === 'exact') {
```
### Line 3829-3838
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
    var handlerCode = isMethodPath
```
### Line 3846-3857
```
  }
}

function genKeyFilter (keys) {
  return (
    // make sure the key filters only apply to KeyboardEvents
    // #9441: can't use 'keyCode' in $event because Chrome autofill fires fake
    // key events that do not have keyCode property...
    "if(!$event.type.indexOf('key')&&" +
    (keys.map(genFilterCode).join('&&')) + ")return null;"
  )
}
```
### Line 3947-3956
```
  } else if (el.tag === 'template' && !el.slotTarget && !state.pre) {
    return genChildren(el, state) || 'void 0'
  } else if (el.tag === 'slot') {
    return genSlot(el, state)
  } else {
    // component or element
    var code;
    if (el.component) {
      code = genComponent(el.component, el, state);
    } else {
```
### Line 3960-3982
```
      }

      var children = el.inlineTemplate ? null : genChildren(el, state, true);
      code = "_c('" + (el.tag) + "'" + (data ? ("," + data) : '') + (children ? ("," + children) : '') + ")";
    }
    // module transforms
    for (var i = 0; i < state.transforms.length; i++) {
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
  var originalPreState = state.pre;
  if (el.pre) {
    state.pre = el.pre;
  }
```
### Line 3983-3992
```
  state.staticRenderFns.push(("with(this){return " + (genElement(el, state)) + "}"));
  state.pre = originalPreState;
  return ("_m(" + (state.staticRenderFns.length - 1) + (el.staticInFor ? ',true' : '') + ")")
}

// v-once
function genOnce (el, state) {
  el.onceProcessed = true;
  if (el.if && !el.ifProcessed) {
    return genIf(el, state)
```
### Line 4038-4047
```
    return ("(" + (condition.exp) + ")?" + (genTernaryExp(condition.block)) + ":" + (genIfConditions(conditions, state, altGen, altEmpty)))
  } else {
    return ("" + (genTernaryExp(condition.block)))
  }

  // v-if with v-once should generate code like (a)?_m(0):_m(1)
  function genTernaryExp (el) {
    return altGen
      ? altGen(el, state)
      : el.once
```
### Line 4084-4167
```
}

function genData$2 (el, state) {
  var data = '{';

  // directives first.
  // directives may mutate the el's other properties before they are generated.
  var dirs = genDirectives(el, state);
  if (dirs) { data += dirs + ','; }

  // key
  if (el.key) {
    data += "key:" + (el.key) + ",";
  }
  // ref
  if (el.ref) {
    data += "ref:" + (el.ref) + ",";
  }
  if (el.refInFor) {
    data += "refInFor:true,";
  }
  // pre
  if (el.pre) {
    data += "pre:true,";
  }
  // record original tag name for components using "is" attribute
  if (el.component) {
    data += "tag:\"" + (el.tag) + "\",";
  }
  // module data generation functions
  for (var i = 0; i < state.dataGenFns.length; i++) {
    data += state.dataGenFns[i](el);
  }
  // attributes
  if (el.attrs) {
    data += "attrs:" + (genProps(el.attrs)) + ",";
  }
  // DOM props
  if (el.props) {
    data += "domProps:" + (genProps(el.props)) + ",";
  }
  // event handlers
  if (el.events) {
    data += (genHandlers(el.events, false)) + ",";
  }
  if (el.nativeEvents) {
    data += (genHandlers(el.nativeEvents, true)) + ",";
  }
  // slot target
  // only for non-scoped slots
  if (el.slotTarget && !el.slotScope) {
    data += "slot:" + (el.slotTarget) + ",";
  }
  // scoped slots
  if (el.scopedSlots) {
    data += (genScopedSlots(el, el.scopedSlots, state)) + ",";
  }
  // component v-model
  if (el.model) {
    data += "model:{value:" + (el.model.value) + ",callback:" + (el.model.callback) + ",expression:" + (el.model.expression) + "},";
  }
  // inline-template
  if (el.inlineTemplate) {
    var inlineTemplate = genInlineTemplate(el, state);
    if (inlineTemplate) {
      data += inlineTemplate + ",";
    }
  }
  data = data.replace(/,$/, '') + '}';
  // v-bind dynamic argument wrap
  // v-bind with dynamic arguments must be applied using the same v-bind object
  // merge helper so that class/style/mustUseProp attrs are handled correctly.
  if (el.dynamicAttrs) {
    data = "_b(" + data + ",\"" + (el.tag) + "\"," + (genProps(el.dynamicAttrs)) + ")";
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
### Line 4176-4186
```
  for (i = 0, l = dirs.length; i < l; i++) {
    dir = dirs[i];
    needRuntime = true;
    var gen = state.directives[dir.name];
    if (gen) {
      // compile-time directive that manipulates AST.
      // returns true if it also needs a runtime counterpart.
      needRuntime = !!gen(el, dir, state.warn);
    }
    if (needRuntime) {
      hasRuntime = true;
```
### Line 4211-4223
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
  var needsForceUpdate = el.for || Object.keys(slots).some(function (key) {
    var slot = slots[key];
    return (
      slot.slotTargetDynamic ||
```
### Line 4225-4244
```
      slot.for ||
      containsSlotChild(slot) // is passing down slot from parent which may be dynamic
    )
  });

  // #9534: if a component with scoped slots is inside a conditional branch,
  // it's possible for the same component to be reused but with different
  // compiled slot content. To avoid that, we generate a unique key based on
  // the generated code of all the slot contents.
  var needsKey = !!el.if;

  // OR when it is inside another scoped slot or v-for (the reactivity may be
  // disconnected due to the intermediate scope variable)
  // #9438, #9506
  // TODO: this can be further optimized by properly analyzing in-scope bindings
  // and skip force updating ones that do not actually use scope variables.
  if (!needsForceUpdate) {
    var parent = el.parent;
    while (parent) {
      if (
```
### Line 4299-4308
```
    "return " + (el.tag === 'template'
      ? el.if && isLegacySyntax
        ? ("(" + (el.if) + ")?" + (genChildren(el, state) || 'undefined') + ":undefined")
        : genChildren(el, state) || 'undefined'
      : genElement(el, state)) + "}";
  // reverse proxy v-slot without scope on this.$slots
  var reverseProxy = slotScope ? "" : ",proxy:true";
  return ("{key:" + (el.slotTarget || "\"default\"") + ",fn:" + fn + reverseProxy + "}")
}

```
### Line 4314-4323
```
  altGenNode
) {
  var children = el.children;
  if (children.length) {
    var el$1 = children[0];
    // optimize single v-for
    if (children.length === 1 &&
      el$1.for &&
      el$1.tag !== 'template' &&
      el$1.tag !== 'slot'
```
### Line 4333-4345
```
    var gen = altGenNode || genNode;
    return ("[" + (children.map(function (c) { return gen(c, state); }).join(',')) + "]" + (normalizationType$1 ? ("," + normalizationType$1) : ''))
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
### Line 4390-4399
```
  var slotName = el.slotName || '"default"';
  var children = genChildren(el, state);
  var res = "_t(" + slotName + (children ? ("," + children) : '');
  var attrs = el.attrs || el.dynamicAttrs
    ? genProps((el.attrs || []).concat(el.dynamicAttrs || []).map(function (attr) { return ({
        // slot props are camelized
        name: camelize(attr.name),
        value: attr.value,
        dynamic: attr.dynamic
      }); }))
```
### Line 4409-4418
```
    res += (attrs ? '' : ',null') + "," + bind$$1;
  }
  return res + ')'
}

// componentName is el.component, take it as argument to shun flow's pessimistic refinement
function genComponent (
  componentName,
  el,
  state
```
### Line 4439-4448
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
### Line 4450-4475
```

/*  */



// these keywords should not appear inside expressions, but operators like
// typeof, instanceof and in are allowed
var prohibitedKeywordRE = new RegExp('\\b' + (
  'do,if,for,let,new,try,var,case,else,with,await,break,catch,class,const,' +
  'super,throw,while,yield,delete,export,import,return,switch,default,' +
  'extends,finally,continue,debugger,function,arguments'
).split(',').join('\\b|\\b') + '\\b');

// these unary operators should not be used as property/method names
var unaryOperatorsRE = new RegExp('\\b' + (
  'delete,typeof,void'
).split(',').join('\\s*\\([^\\)]*\\)|\\b') + '\\s*\\([^\\)]*\\)');

// strip strings in expressions
var stripStringRE = /'(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*"|`(?:[^`\\]|\\.)*\$\{|\}(?:[^`\\]|\\.)*`|`(?:[^`\\]|\\.)*`/g;

// detect problematic expressions in a template
function detectErrors (ast, warn) {
  if (ast) {
    checkNode(ast, warn);
  }
```
### Line 4581-4590
```
      for (var j = i - range; j <= i + range || end > count; j++) {
        if (j < 0 || j >= lines.length) { continue }
        res.push(("" + (j + 1) + (repeat$1(" ", 3 - String(j + 1).length)) + "|  " + (lines[j])));
        var lineLength = lines[j].length;
        if (j === i) {
          // push underline
          var pad = start - (count - lineLength) + 1;
          var length = end > count ? lineLength - pad : end - start;
          res.push("   |  " + repeat$1(" ", pad) + repeat$1("^", length));
        } else if (j > i) {
```
### Line 4639-4648
```
    var warn$$1 = options.warn || warn;
    delete options.warn;

    /* istanbul ignore if */
    if (process.env.NODE_ENV !== 'production') {
      // detect possible CSP restriction
      try {
        new Function('return 1');
      } catch (e) {
        if (e.toString().match(/unsafe-eval|CSP/)) {
```
### Line 4655-4675
```
          );
        }
      }
    }

    // check cache
    var key = options.delimiters
      ? String(options.delimiters) + template
      : template;
    if (cache[key]) {
      return cache[key]
    }

    // compile
    var compiled = compile(template, options);

    // check compilation errors/tips
    if (process.env.NODE_ENV !== 'production') {
      if (compiled.errors && compiled.errors.length) {
        if (options.outputSourceRange) {
          compiled.errors.forEach(function (e) {
```
### Line 4694-4713
```
          compiled.tips.forEach(function (msg) { return tip(msg, vm); });
        }
      }
    }

    // turn code into functions
    var res = {};
    var fnGenErrors = [];
    res.render = createFunction(compiled.render, fnGenErrors);
    res.staticRenderFns = compiled.staticRenderFns.map(function (code) {
      return createFunction(code, fnGenErrors)
    });

    // check function generation errors.
    // this should only happen if there is a bug in the compiler itself.
    // mostly for codegen development use
    /* istanbul ignore if */
    if (process.env.NODE_ENV !== 'production') {
      if ((!compiled.errors || !compiled.errors.length) && fnGenErrors.length) {
        warn$$1(
```
### Line 4743-4752
```
        (tip ? tips : errors).push(msg);
      };

      if (options) {
        if (process.env.NODE_ENV !== 'production' && options.outputSourceRange) {
          // $flow-disable-line
          var leadingSpaceLength = template.match(/^\s*/)[0].length;

          warn = function (msg, range, tip) {
            var data = { msg: msg };
```
### Line 4759-4780
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
        for (var key in options) {
          if (key !== 'modules' && key !== 'directives') {
            finalOptions[key] = options[key];
          }
```
### Line 4799-4810
```
  }
}

/*  */

// `createCompilerCreator` allows creating compilers that use alternative
// parser/optimizer/codegen, e.g the SSR optimizing compiler.
// Here we just export a default compiler using the default parts.
var createCompiler = createCompilerCreator(function baseCompile (
  template,
  options
) {
```
### Line 4880-4897
```



var plainStringRE = /^"(?:[^"\\]|\\.)*"$|^'(?:[^'\\]|\\.)*'$/;

// let the model AST transform translate v-model into appropriate
// props bindings
function applyModelTransform (el, state) {
  if (el.directives) {
    for (var i = 0; i < el.directives.length; i++) {
      var dir = el.directives[i];
      if (dir.name === 'model') {
        state.directives.model(el, dir, state.warn);
        // remove value for textarea as its converted to text
        if (el.tag === 'textarea' && el.props) {
          el.props = el.props.filter(function (p) { return p.name !== 'value'; });
        }
        break
```
### Line 4930-4941
```
  return segments
}

function genAttrSegment (name, value) {
  if (plainStringRE.test(value)) {
    // force double quote
    value = value.replace(/^'|'$/g, '"');
    // force enumerated attr to "true"
    if (isEnumeratedAttr(name) && value !== "\"false\"") {
      value = "\"true\"";
    }
    return {
```
### Line 4986-4995
```
  }
}

/*  */

// optimizability constants
var optimizability = {
  FALSE: 0,    // whole sub tree un-optimizable
  FULL: 1,     // whole sub tree optimizable
  SELF: 2,     // self optimizable but has some un-optimizable children
```
### Line 5008-5017
```
function walk (node, isRoot) {
  if (isUnOptimizableTree(node)) {
    node.ssrOptimizability = optimizability.FALSE;
    return
  }
  // root node or nodes with custom directives should always be a VNode
  var selfUnoptimizable = isRoot || hasCustomDirective(node);
  var check = function (child) {
    if (child.ssrOptimizability !== optimizability.FULL) {
      node.ssrOptimizability = selfUnoptimizable
```
### Line 5071-5081
```
  for (var i = 0; i < children.length; i++) {
    var c = children[i];
    if (c.ssrOptimizability === optimizability.FULL) {
      currentOptimizableGroup.push(c);
    } else {
      // wrap fully-optimizable adjacent siblings inside a template tag
      // so that they can be optimized into a single ssrNode by codegen
      pushGroup();
      optimizedChildren.push(c);
    }
  }
```
### Line 5103-5113
```
    node.directives &&
    node.directives.some(function (d) { return !isBuiltInDir(d.name); })
  )
}

// <select v-model> cannot be optimized because it requires a runtime check
// to determine proper selected option
function isSelectWithModel (node) {
  return (
    node.type === 1 &&
    node.tag === 'select' &&
```
### Line 5119-5128
```
/*  */




// segment types
var RAW = 0;
var INTERPOLATION = 1;
var EXPRESSION = 2;

```
### Line 5149-5170
```
      : genSSRChildren(el, state) || 'void 0'
  }

  switch (el.ssrOptimizability) {
    case optimizability.FULL:
      // stringify whole tree
      return genStringElement(el, state)
    case optimizability.SELF:
      // stringify self and check children
      return genStringElementWithChildren(el, state)
    case optimizability.CHILDREN:
      // generate self as VNode and stringify children
      return genNormalElement(el, state, true)
    case optimizability.PARTIAL:
      // generate self as VNode and check children
      return genNormalElement(el, state, false)
    default:
      // bail whole tree
      return genElement(el, state)
  }
}

```
### Line 5204-5213
```
function elementToString (el, state) {
  return ("(" + (flattenSegments(elementToSegments(el, state))) + ")")
}

function elementToSegments (el, state) {
  // v-for / v-if
  if (el.for && !el.forProcessed) {
    el.forProcessed = true;
    return [{
      type: EXPRESSION,
```
### Line 5235-5267
```

function elementToOpenTagSegments (el, state) {
  applyModelTransform(el, state);
  var binding;
  var segments = [{ type: RAW, value: ("<" + (el.tag)) }];
  // attrs
  if (el.attrs) {
    segments.push.apply(segments, genAttrSegments(el.attrs));
  }
  // domProps
  if (el.props) {
    segments.push.apply(segments, genDOMPropSegments(el.props, el.attrs));
  }
  // v-bind="object"
  if ((binding = el.attrsMap['v-bind'])) {
    segments.push({ type: EXPRESSION, value: ("_ssrAttrs(" + binding + ")") });
  }
  // v-bind.prop="object"
  if ((binding = el.attrsMap['v-bind.prop'])) {
    segments.push({ type: EXPRESSION, value: ("_ssrDOMProps(" + binding + ")") });
  }
  // class
  if (el.staticClass || el.classBinding) {
    segments.push.apply(
      segments,
      genClassSegments(el.staticClass, el.classBinding)
    );
  }
  // style & v-show
  if (el.staticStyle || el.styleBinding || el.attrsMap['v-show']) {
    segments.push.apply(
      segments,
      genStyleSegments(
```
### Line 5270-5279
```
        el.styleBinding,
        el.attrsMap['v-show']
      )
    );
  }
  // _scopedId
  if (state.options.scopeId) {
    segments.push({ type: RAW, value: (" " + (state.options.scopeId)) });
  }
  segments.push({ type: RAW, value: ">" });
```

## _src_platforms_web_runtime_directives_model_js
### Line 8-17
```
import { mergeVNodeHook } from 'core/vdom/helpers/index'
import { warn, isIE9, isIE, isEdge } from 'core/util/index'

/* istanbul ignore if */
if (isIE9) {
  // http://www.matts411.com/post/internet-explorer-9-oninput/
  document.addEventListener('selectionchange', () => {
    const el = document.activeElement
    if (el && el.vmodel) {
      trigger(el, 'input')
```
### Line 20-29
```
}

const directive = {
  inserted (el, binding, vnode, oldVnode) {
    if (vnode.tag === 'select') {
      // #6903
      if (oldVnode.elm && !oldVnode.elm._vOptions) {
        mergeVNodeHook(vnode, 'postpatch', () => {
          directive.componentUpdated(el, binding, vnode)
        })
```
### Line 34-46
```
    } else if (vnode.tag === 'textarea' || isTextInputType(el.type)) {
      el._vModifiers = binding.modifiers
      if (!binding.modifiers.lazy) {
        el.addEventListener('compositionstart', onCompositionStart)
        el.addEventListener('compositionend', onCompositionEnd)
        // Safari < 10.2 & UIWebView doesn't fire compositionend when
        // switching focus before confirming composition choice
        // this also fixes the issue where some browsers e.g. iOS Chrome
        // fires "change" instead of "input" on autocomplete.
        el.addEventListener('change', onCompositionEnd)
        /* istanbul ignore if */
        if (isIE9) {
          el.vmodel = true
```
### Line 50-67
```
  },

  componentUpdated (el, binding, vnode) {
    if (vnode.tag === 'select') {
      setSelected(el, binding, vnode.context)
      // in case the options rendered by v-for have changed,
      // it's possible that the value is out-of-sync with the rendered options.
      // detect such cases and filter out values that no longer has a matching
      // option in the DOM.
      const prevOptions = el._vOptions
      const curOptions = el._vOptions = [].map.call(el.options, getValue)
      if (curOptions.some((o, i) => !looseEqual(o, prevOptions[i]))) {
        // trigger change event if
        // no matching option found for at least one value
        const needReset = el.multiple
          ? binding.value.some(v => hasNoMatchingOption(v, curOptions))
          : binding.value !== binding.oldValue && hasNoMatchingOption(binding.value, curOptions)
        if (needReset) {
```
### Line 130-139
```
function onCompositionStart (e) {
  e.target.composing = true
}

function onCompositionEnd (e) {
  // prevent triggering an input event for no reason
  if (!e.target.composing) return
  e.target.composing = false
  trigger(e.target, 'input')
}
```

## _test_unit_modules_observer_watcher_spec_js
### Line 34-43
```
  })

  it('non-existent path, set later', done => {
    const watcher1 = new Watcher(vm, 'b.e', spy)
    expect(watcher1.value).toBeUndefined()
    // check $add should not affect isolated children
    const child2 = new Vue({ parent: vm })
    const watcher2 = new Watcher(child2, 'b.e', spy)
    expect(watcher2.value).toBeUndefined()
    Vue.set(vm.b, 'e', 123)
```

## _test_unit_features_options_template_spec_js

## _src_platforms_web_compiler_options_js

## _test_weex_helpers_index_js
### Line 17-26
```
  return (new Function(`return ${readFile(filename)}`))()
}

console.debug = () => {}

// http://stackoverflow.com/a/35478115
const matchOperatorsRe = /[|\\{}()[\]^$+*?.]/g
export function strToRegExp (str) {
  return new RegExp(str.replace(matchOperatorsRe, '\\$&'))
}
```
### Line 133-142
```

export function getRoot (instance) {
  return omitUseless(instance.$getRoot())
}

// Get all binding events in the instance
export function getEvents (instance) {
  const events = []
  const recordEvent = node => {
    if (!node) { return }
```

# Issues
## 8637
Title:
```

        Lookup from a Vuex observed property containing many rows is very slow!
      
```
Author:
```
mheere
```
Text:
```

Hi - I am trying to render a long list of items through a number of fixed cells in a home made grid with around 50 fixed rows.  When I scroll I read out different values from a Vuex store data property with around 5000 rows.
So it is important to understand that I do not create new cells or rows, Once created I merely update their content upon scrolling.
<template>
    <div ref="mygridcell" class='vg-data-cell' v-bind:style='mhstyle'>
            
            <span>{{ thevalue }}</span>

        </div>
</template>
...partial...

export default Vue.extend({
    props: ['rowNo', 'colDef', 'rowNoVis'],
    data: () => new MyData(),
    computed: {
        thevalue (): string {
            let row = this.$store.state.rowsPrepared[this.rowNo];
            return row["lastName"];
        },
   
I am using a Vuex store and have a property on its state called 'rowsPrepared' that contains the 5000 rows.
The problem
When I start scrolling and read out the values for the cells through the 'rowsPrepared' Vuex property it is dreadfully slow.
However, if I read the data from a stand-alone static (non observed) data object containing the 5000 rows it is super fast!
Why is reading from an 'observable' vuex property so slow and is there a way around it?
What I have done is attach the 'rowsPrepared' property after the store is created so it is not observed and indeed, scrolling is super fast.  However, if an item changes its value it is not automatically tracked so I will be forced to do a hacky refresh - stuff that is meant to be done by Vue itself l!!
Any help much appreciated!

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
yyx990803
```
Text:
```

Hey, we can't really help without any runnable code to look at.

```

## 6466
Title:
```

        IE11: Keystrokes missing if v-model is used
      
```
Author:
```
ckittelmann
```
Text:
```

Version
2.4.2
Reproduction link
http://jsfiddle.net/zjsuzqgu/15/
Steps to reproduce
This issue only occurs in Internet Exporer 11 on textareas and input fields when using v-model binding.

Open the http://jsfiddle.net/zjsuzqgu/15/ with IE 11
Quickly enter text into the second textarea (maybe you should press 3 buttons at same time)

We used a barcode scanner to enter the texts, but its also possible to reproduce it with the keyboard.
We also recognized that it happens more often on slow machines
What is expected?
All keys are recognized
What is actually happening?
Some letters are missing randomly

We made a video of this behaviour: https://youtu.be/w-IYuPBGdR0
You could reproduce this even on the vuejs page https://vuejs.org/v2/guide/forms.html#Text
I just added a v-on:input to the textarea to see whats logged there.
The result was
A
A
AC
AC
The B was never recognized even in input event
I also changed the intercharacter delay of the scanner from 1 ms to 25 ms without success

```
Author:
```
posva
```
Text:
```

I cannot test it right now but if using an input listener yields that result, it's probably something wrong with IE messing up v-model

```
Author:
```
jsnanigans
```
Text:
```

I don't know for sure what going on in the source that could cause this, but its definitely not the input listener, if you don't use v-model and instead use @input it works fine in ie11.
test: http://jsfiddle.net/zjsuzqgu/21/
@ckittelmann I imagine that if you are using a barcode scanner you only need to listen to the keyup event, and if you don't need the two-way data-binding then this might be a solution for you.

```
Author:
```
marinru
```
Text:
```

Pressing several buttons at the same time fires several input events (one for each button the keyboard sends), that's ok. What is not ok with IE11 with v-model binding is the fact that every other event handler gets fired before the input value is changed, the pattern is like this:

a char is added to the input value
input handler is fired
input handler is fired
a char is added to the input value
...

I suspect it may have something to do with the nextTick behavior. BTW, timerFunc is called only half the time in IE11 unlike, for example, Chrome or FF.

```
Author:
```
posva
```
Text:
```

Finally, could test on IE11. It's also weird when you keep 3 keys pressed because only 1 gets repeated.
v-model has some fixes to work around IE crazy behaviour and here, it's definitely messing up some other things. Not sure to mark this as an improvement or a bug, or both.
As a workaround, use an input listener, which does yield the expected result you want

```
Author:
```
ckittelmann
```
Text:
```

Thx @jsnanigans for the workaround I will look at our application, but I think we need the two way binding.
I just tested this behaviour in 1.0.28 and 2.0.0. It only occurs in 2.0.0+
Some examples to test it:
Version 1.0.28 http://jsfiddle.net/8hg4f5gv/3/
Version 2.0.0 http://jsfiddle.net/8hg4f5gv/2/

```

## 9024
Title:
```

        Hiding/Unhidding jQuery DataTables breaks column widths
      
```
Author:
```
RotateAt60MPH
```
Text:
```

Version
2.5.17
Reproduction link
http://jsfiddle.net/cardinal177/m7bzjsag/3/
Steps to reproduce
Create a page with multiple jQuery DataTables that are hidden/shown via v-show to a vue data variable.  The initially 'shown' datatable looks fine.  When you switch to the second table, showing it, the column formats are all wrong.  If you change back to the originally working table, it's column widths are broken as well.  .columns.adjust().draw() does not appear to fix this.I know jQuery plugins are dicey, at best, but all of the DataTables work in done post-rendering of the page.  Don't know why vue.js would prevent this from working.What is expected?The table column widths should be preserved.What is actually happening?Columns widths on an unhidden table has widths all = 0px;


```
Author:
```
Justineo
```
Text:
```

You should try to force a layout recalculation of the plugin (something like .adjust().draw() as you mentioned only when the container is attached to DOM. You may want to put this in this.$nextTick().

```

## 632
Title:
```

        v-focus directive
      
```
Author:
```
thelinuxlich
```
Text:
```

So we can programmatically focus input elements

```
Author:
```
yyx990803
```
Text:
```

I think this should be left in user space, no?

```
Author:
```
thelinuxlich
```
Text:
```

okie dokie

```

## 568
Title:
```

        Firefox compatibility issue
      
```
Author:
```
jzfsdev
```
Text:
```

component below:
<input   type="checkbox"
v-model="status"
v-on="click:changeStatus(status)">
on chrome or safari execute _set method in model directive before changeStatus,
but in Firefox changeStatus execute before _set method
jsfiddle link
http://jsfiddle.net/Joe_Zhong/2yrfpu3k/

```
Author:
```
yyx990803
```
Text:
```

The order of change and click events fire in different orders in Firefox, and this is not something Vue can control.
Logically, what you want is react to the change of the status property, so you should $watch('status', changeStatus) instead of using a click listener.

```
Author:
```
jzfsdev
```
Text:
```

Ok, thanks for you relay.
My case is different.
See http://jsfiddle.net/Joe_Zhong/2yrfpu3k/2/
How can i $watch the status in the list?

```
Author:
```
yyx990803
```
Text:
```

In this case you can listen on change instead of click.

```
Author:
```
jzfsdev
```
Text:
```

Resolved. Thanks a lot.

```
Author:
```
jzfsdev
```
Text:
```

but it does not work on 0.10.6.
http://jsfiddle.net/2yrfpu3k/4/
Only working on 0.11.0
encounter some exception and warning when migrate to 0.11.0.
Any advice? thanks.

```
Author:
```
yyx990803
```
Text:
```

0.10 to 0.11 upgrade change list here: https://github.com/yyx990803/vue/blob/master/changes.md

```

## 1052
Title:
```

        0.12.7给组件显式传参没效果
      
```
Author:
```
PeakTai
```
Text:
```

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>component</title>
    <script src="bower_components/vue/dist/vue.js"></script>
</head>
<body>
<my-component v-with="name:name"></my-component>
<script>
    window.onload = function () {
        Vue.component("my-component", {
            template: "Hello {{name}}"
        });
        new Vue({
            el: "body",
            data: {
                name: "Peak"
            }
        });
    }
</script>
</body>
</html>
打开网页，只显示一个Hello，就不截图了。

```
Author:
```
bjtqti
```
Text:
```

需要显示的增加inherit
Vue.component("my-component", {
inherit: true,
template: "Hello {{name}}"
});

```
Author:
```
butsalt
```
Text:
```

v-with在0.12.0的时代就已经被废除了，中文版的文档还停留在0.11.5。建议你在英文版的官网查阅相关文档，你所关心的问题在这里。所以，在0.12.7@Vue下的正确的写法应该是这样，为了避免name属性对dom的影响，个人推荐写法是在传参属性名之前加上data-前缀。对了，有关Vue的使用问题或讨论应该在讨论版进行，这里主要是用来提出bug或者建议的。

```
Author:
```
yyx990803
```
Text:
```

@butsalt 多谢详细的回答 :)

```

## 7241
Title:
```

        not working with IE 11
      
```
Author:
```
akahen
```
Text:
```

Version
2.5.9
Reproduction link
https://jsfiddle.net/2dwrr91q/
Steps to reproduce
none
What is expected?
a simple form as shown in any other browser
What is actually happening?
html in template is not showing
computed item in html within {{}} is not rendering

pulled in Vue via CDN, and not using any transcribe utility (i.e. babel)
by default, the site uses bootstrap and jquery, yet pulling Vue at the very end.
thanks

```
Author:
```
yyx990803
```
Text:
```

The repro requirements clearly stated that we expect minimal reproductions, and it must have inspectable source code, not full apps.

```
Author:
```
akahen
```
Text:
```

updated link to jsfiddle, https://jsfiddle.net/2dwrr91q/ thanks

```

## 2727
Title:
```

        [Bug ?] Render a component with component definition bound to is attribute
      
```
Author:
```
AlexandreBonaventure
```
Text:
```

Vue.js version
1.0.21
Reproduction Link
https://jsfiddle.net/oe7axeab/789/
What is Expected?
According to 1.0.19 release note, components can now be rendered dynamically by bounding is attribute with a component definition.
In the fiddle I try to make the example work but b component is not rendered. Did I miss something here ?
Thanks

```
Author:
```
pespantelis
```
Text:
```

Please check this section of  the documentation carefully.
Working demo

```
Author:
```
AlexandreBonaventure
```
Text:
```

Ok, I got it. We have to pass a constructor via Vue.extend
Heres a working fiddle https://jsfiddle.net/oe7axeab/790/

```
Author:
```
AlexandreBonaventure
```
Text:
```

@pespantelis Thanks, but it was not the behaviour I was looking for.
See https://github.com/vuejs/vue/releases/tag/v1.0.19.
I don't think it appears in official doc yet.

```

## 8257
Title:
```

        errorCaptured hook
      
```
Author:
```
zhaosaisai
```
Text:
```

Why this hook function is used to catch subcomponent errors instead of catching their own errors?
The source code is as follows:
function handleError (err: Error, vm: any, info: string) {
  if (vm) {
    let cur = vm
    while ((cur = cur.$parent)) {
      const hooks = cur.$options.errorCaptured
      if (hooks) {
        for (let i = 0; i < hooks.length; i++) {
          try {
            const capture = hooks[i].call(cur, err, vm, info) === false
            if (capture) return
          } catch (e) {
            globalHandleError(e, cur, 'errorCaptured hook')
          }
        }
      }
    }
  }
  globalHandleError(err, vm, info)
}
Why not design this way?
function handleError (err: Error, vm: any, info: string) {
  if (vm) {
    let cur = vm
    while (cur) {
      const hooks = cur.$options.errorCaptured
      if (hooks) {
        for (let i = 0; i < hooks.length; i++) {
          try {
            const capture = hooks[i].call(cur, err, vm, info) === false
            if (capture) return
          } catch (e) {
            globalHandleError(e, cur, 'errorCaptured hook')
          }
        }
      }
      cur = cur.$parent
    }
  }
  globalHandleError(err, vm, info)
}

```
Author:
```
vue-bot
```
Text:
```

Hello, your issue has been closed because it does not conform to our issue requirements. In order to ensure every issue provides the necessary information for us to investigate, we require the use of the Issue Helper when creating new issues. Thank you!

```

## 2798
Title:
```

        v-show will not work properly when other css class has "display:none;"
      
```
Author:
```
yunhor
```
Text:
```

v-show 在元素其它类包含有 display:none; 时，监控变量为true时 输出是空，这样的渲染的结果是元素不可见！不知道是我刚用Vue不知道是不是有其它的用法？
我简单在 toggle修改了下：
function toggle() { el.style.display = value ? 'block' : 'none'; } 
暂时解决这个问题

```
Author:
```
yyx990803
```
Text:
```

既然用了 v-show 就不要用 css 去控制了... 用 v-show 绑定的值去控制啊

```
Author:
```
yunhor
```
Text:
```

可是有些场景下原本就有这些类存在，只是简单的用v-show控制下 ，比如 在 登录页面 有好几个form 切换登录/注册/忘记密码 我只是简单在每个form加个变量用v-show控制显示 。但这些form有许多其它css ,其中就有题目所说的 隐藏 样式 ，总不能手工将其它地方的样式改掉吧

```
Author:
```
yyx990803
```
Text:
```

v-show 要保留初始 display 值，因为你也可能需要 display inline。既然这个元素是需要动态切换的你的 css 就不应该默认是 display: none，你改样式显然比改 Vue 的源码合理。

```
Author:
```
yunhor
```
Text:
```

有道理，只是实际操作中，有时是改造旧代码，有时是从别人现有工作开始，有时就会碰到不是很方便改动样式，另外，也是偷懒，不想去详细跟踪样式设计，所以简单修改了事

```
Author:
```
yunhor
```
Text:
```

也许终极方案是扩展一个指令或是v-show能带外饰符或是参数

```

## 2044
Title:
```

        v-ref inside v-for is not defined
      
```
Author:
```
noirbizarre
```
Text:
```

When using v-ref on a component with v-for it produces a list of components.
But, when using components inside a v-for and using v-ref on this component, I expect the same behavior but the component list is not present in $refs.
See this code sample illustrating the issue with Vue.js 1.0.11: https://jsfiddle.net/noirbizarre/jms2gzpt
I think this is related to #1850 and to #1697

```
Author:
```
yyx990803
```
Text:
```

This is currently intended behavior: refs are only defined in the v-for scope it is in.
I'm not sure it it makes sense to define the refs on the surrounding component - it could lead to some pretty tricky cases:
<div v-for="item in items">
  <comp v-ref:nested :value="item"></comp>
  {{ $refs.nested }} <!-- should this be a single component, or an array? -->
</div>
And with nested v-fors:
<div v-for="item in items">
  <div v-for="sub in item.subs">
    <comp v-ref:nested></comp>
  </div>
</div>
What should $refs.nested be in this case? A nested array? That doesn't really sound that useful.

```
Author:
```
yyx990803
```
Text:
```

Closing since it doesn't seem to be a common use case (lack of discussion).

```
Author:
```
zyf0330
```
Text:
```

@yyx990803 I have the same problem. And I think you should let developers decide how to name for v-ref. Developer will solve the conflict of v-ref name. Let's see below code.
Situation 1:
<div v-for="item in items">
  <comp v-ref:nested{{item}} :value="item"></comp>
</div>

We can use $refs.nested{{index}} to name them.
Situation 2:
<div v-for="item in items">
  <div v-for="sub in item.subs">
    <comp v-ref:nested{{item.sub}}></comp>
  </div>
</div>

What we need to do is add a feature to make v-ref accept variable.
How about that?

```
Author:
```
zyf0330
```
Text:
```

@yyx990803 Couldn't you see me here?

```
Author:
```
YerkoPalma
```
Text:
```

I'm also having the same problem. Is there posible to have some syntax like what @zyf0330 proposed? or are there any workaround to get a specific component inside a v-for loop?

```
Author:
```
zyf0330
```
Text:
```

@YerkoPalma if you can ensure only one kind of component inside a v-for, then you can use $children. Or you can use css selector with $el as the base element.

```
Author:
```
noirbizarre
```
Text:
```

finally I agree with @yyx990803
I case of $els, it can become very complex to understand. I rethinked my solution to avoid that.

```
Author:
```
matfish2
```
Text:
```

I agree with @zyf0330. Dynamic v-ref's could be really useful. For example, if you have multiple instances of a component and you want to track one down and call a method on it, a unique id can be assigned to each component as a required prop, which can then be used by the consumer to easily fetch it, without having to hunt it down the tree.
E.g, i've built a pagination component which accepts a 'for' prop:
  <pagination for="table2" per-page="25" records="100"></pagination>

would be nice if the consumer could do something like
this.$refs.table2.setPage(1)


```
Author:
```
zyf0330
```
Text:
```

Sorry, but I don't see your example is related with what i said.
@matfish2

```
Author:
```
matfish2
```
Text:
```

Well, I probably misunderstood... Sorry about that

```
Author:
```
FrankFang
```
Text:
```

@noirbizarre How did your resolve this in the end.

```
Author:
```
ptempelman
```
Text:
```

@FrankFang did you manage to fix this already? I have the exact same problem..

```
Author:
```
FrankFang
```
Text:
```

@MrPhilipT I use
this.$el.querySelector(`[name="whatever-${index}"]`)

;)

```
Author:
```
ptempelman
```
Text:
```

@FrankFang okay, I was able to resolve my issue using v-model in the selector instead of v-ref, so for instance <selector v-model="something"><option v-for="option in options">{{ option }} </option></selector> and putting something:"", in data, turns out I didn't really need v-ref..

```
Author:
```
bezborodow
```
Text:
```

As an example, this is how I worked around the problem:
<tr v-for="contract in contracts" :key="contract.id">
   <td>
        <button @click="showModal(contract)">Edit</button>

        <contract-modal :contract="contract" ref="modals"></contract-modal>

[...]

    showModal(contract) {
        this.$refs.modals.find(ref => ref.contract.id === contract.id).show = true;
    },



Note that the component ContractModal in this example has a boolean property show, which controls the visibility of the modal. The essence of this example is the call to this.$refs.modals.find() that fetches the component from the array.

```

## 3991
Title:
```

        Vue.js v1.0.26 【v-if】
      
```
Author:
```
lgc
```
Text:
```

Vue.js version
1.0.26
Reproduction Link
https://jsfiddle.net/garvinlgc/opxcad19/4/
Steps to reproduce
What is Expected?
What is actually happening?

```
Author:
```
fnlctrl
```
Text:
```

Hi, please make sure to follow the Issue Reporting Guidelines before opening an issue. Thanks!

```

## 9664
Title:
```

        npm run build gets killed (errno 137)
      
```
Author:
```
Rolanddoda
```
Text:
```

Version
2.6.8
Reproduction link
https://codesandbox.io/s/vue
Steps to reproduce
I have the code below which works fine.
let imports = []

function importAll(filePaths) {
  filePaths.keys().forEach(filePath => {
    const path = filePath.replace('.', '')
    imports.push(require(`@/modules${path}`).default)
  })
  return imports
}

export const importAllRoutes = () =>
  importAll(require.context('@/modules/', true, /routes.js/))


When I do npm run build locally works perfectly fine. But when I do npm run build on the server (to deploy) the build process gets killed.
What is expected?
This is supposed to work but the build process gets killed.
What is actually happening?
My guess is that is a RAM issue but I am not sure.

Sorry but I can't provide Link to minimal reproduction. Also I am not sure that is a vue.js issue, a npm one or webpack. But if I remove the code snippet above, everything works fine.

```
Author:
```
posva
```
Text:
```

Hey, please do not open issues without providing repros or to ask questions, this is not the first time you it so please stop doing it.
Remember you can and should use the forum or the Discord chat to ask questions!

```
Author:
```
Rolanddoda
```
Text:
```

There is no a way to provide repro. I thought this is an issue since the build process gets killed that's why I opened an issue. But anyway thanks. I will use the forum.

```

## 10081
Title:
```

        <transition> does not work for functionals components if use <componen :is="">
      
```
Author:
```
artpoddybnyy
```
Text:
```

Version
2.6.10
Reproduction link
https://repl.it/@artpoddybnyy/vue-transition-functional
Steps to reproduce
Press the button show B then show A
What is expected?
Opacity animation when change component
What is actually happening?
Opacity animation does not work

```
Author:
```
posva
```
Text:
```

You are missing the key
<!DOCTYPE html>
<html>

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width">
	<title>repl.it</title>

<style>
   .fade-enter-active, .fade-leave-active {
      transition: opacity 0.5s;
    }
    .fade-enter, .fade-leave-to  {
      opacity: 0;
    }
</style>

	<script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>
</head>

<body>
	<div id="app">
		  <transition name="fade" mode="out-in">
			    <component :is="compoName" :key="compoName">
			  </transition>
				<button @click="showCompo('compoA')"> show A </button>
        <button @click="showCompo('compoB')"> show B </button>
    </div>

    <script>
        const compoA ={
          functional: true,
          render (h, ctx) {
            return h('h1', ctx.data, 'Component A', )
          }          
        }
        const compoB = {
            functional: true,
            render (h, ctx) {
              return h('h1', ctx.data, 'Component B', )
           }           
        }

        new Vue({
          components: {
            compoA, compoB
          },
              data () {
            return {
              compoName: 'compoA'
            }
          },
           methods: {
             showCompo (name) {
               this.compoName = name
             }
           }
        }).$mount('#app')
    </script>
  </body>
</html>

```
Author:
```
artpoddybnyy
```
Text:
```

@posva Thank for help
Could You explain please why this case won't work with
<template functional>
</template>


```
Author:
```
posva
```
Text:
```

it does, but you need to pass the key manually as well from data.key in the template
<template functional>
  <h1 :key="data.key">hey</h1>
</template>

```

## 9707
Title:
```

         Different behaviors of  Arrow function and function 
      
```
Author:
```
zhangenming
```
Text:
```

Version
2.6.8
Reproduction link
https://codepen.io/zhangenming/pen/GexZQK
Steps to reproduce
    <input :value="price" @input="e=>price=e.target.value">
Compiled:
    with(this){return _c('input',{domProps:{"value":price},on:{"input":e=>price=e.target.value}})}
    <input :value="price" @input="function f(e){price=e.target.value}">// this wont' be work
Compiled:
    with(this){return _c('input',{domProps:{"value":price},on:{"input":function($event){function f(e){price=e.target.value}}}})}
What is expected?
can be work
What is actually happening?
this wont' be work

```
Author:
```
Justineo
```
Text:
```

I helped re-formatted your issue and fixed a typo.
It seems that the template compiler is not generating correct code with function literals with a function name.
See the difference here.

```
Author:
```
DanielDanaee
```
Text:
```

Why would you expect this to work? directive values should be method names or methods only.
Have a look at the following part of the documentation:
https://vuejs.org/v2/guide/events.html#Method-Event-Handlers
This is probably what you should be doing:
<input :value="price" @input="getTargetValue(e)">
getTargetValue(e){ return (this.price =  e.target.value) }

```

## 3554
Title:
```

        Struggling on how to make a numeric field comma formatter work on 2.0
      
```
Author:
```
marcalc
```
Text:
```

In 1.0 we had filters which helped us translate comma-separated decimals in text inputs to javascript numbers (eg. '2,91' to 2.91). It was very straightforward.
How can such translation be implemented in 2.0? Maybe extending v-model directive? Creating a totally new directive and repeating all v-model boilerplate? Computed get/setters?
Thanks a lot!

```
Author:
```
yyx990803
```
Text:
```

Please make sure to read the Issue Reporting Guidelines before opening new issues. The issue list only accepts bug reports and feature requests. Questions should be posted to the Gitter chat room,  forum or StackOverflow. Thanks.

Regarding your need, the recommended approach in 2.0 is creating an extended component that handles the underlying conversion logic, e.g. <numeric-input v-model="val"></numeric-input>

```

## 6654
Title:
```

        Production setup memory loss after 39hrs
      
```
Author:
```
acidjazz
```
Text:
```

This is a production nuxt.js build but I am posting this issue here since the stack seems to point at vue.runtime.common.js on either lines 3362, 3296, or 4181.
Here are a couple dumps of the crash, it's pretty consistent, almost even with how long it runs for.
First one a couple days ago
<--- Last few GCs --->

[8202:0x2822f10] 148084153 ms: Mark-sweep 1399.9 (1494.4) -> 1399.9 (1494.4) MB, 2284.2 / 0.0 ms  allocation failure GC in old space requested
[8202:0x2822f10] 148086478 ms: Mark-sweep 1399.9 (1494.4) -> 1399.9 (1494.4) MB, 2323.0 / 0.0 ms  last resort
[8202:0x2822f10] 148088794 ms: Mark-sweep 1399.9 (1494.4) -> 1399.9 (1494.4) MB, 2315.4 / 0.0 ms  last resort

<--- JS stacktrace --->

==== JS stack trace =========================================

Security context: 0x37a56a69cca1 <JSObject>
    1: initWatch(aka initWatch) [/home/ec2-user/api/web/node_modules/vue/dist/vue.runtime.common.js:~3296] [pc=0x16c066f78f0b](this=0x37a56a682241 <undefined>,vm=0x361f52ccf229 <Vue$3 map = 0x3a932c4ded49>,watch=0x1374913debb1 <Object map = 0x25ca00203649>)
    2: _init [/home/ec2-user/api/web/node_modules/vue/dist/vue.runtime.common.js:~4181] [pc=0x16c06696451c](this=0x361f52ccf229 <Vue$3 map =...

FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory
 1: node::Abort() [node]
 2: 0x136916c [node]
 3: v8::Utils::ReportOOMFailure(char const*, bool) [node]
 4: v8::internal::V8::FatalProcessOutOfMemory(char const*, bool) [node]
 5: v8::internal::Factory::NewTransitionArray(int) [node]
 6: v8::internal::TransitionArray::Insert(v8::internal::Handle<v8::internal::Map>, v8::internal::Handle<v8::internal::Name>, v8::internal::Handle<v8::internal::Map>, v8::internal::SimpleTransitionFlag) [node]
 7: v8::internal::Map::CopyReplaceDescriptors(v8::internal::Handle<v8::internal::Map>, v8::internal::Handle<v8::internal::DescriptorArray>, v8::internal::Handle<v8::internal::LayoutDescriptor>, v8::internal::TransitionFlag, v8::internal::MaybeHandle<v8::internal::Name>, char const*, v8::internal::SimpleTransitionFlag) [node]
 8: v8::internal::Map::CopyAddDescriptor(v8::internal::Handle<v8::internal::Map>, v8::internal::Descriptor*, v8::internal::TransitionFlag) [node]
 9: v8::internal::Map::CopyWithField(v8::internal::Handle<v8::internal::Map>, v8::internal::Handle<v8::internal::Name>, v8::internal::Handle<v8::internal::FieldType>, v8::internal::PropertyAttributes, v8::internal::PropertyConstness, v8::internal::Representation, v8::internal::TransitionFlag) [node]
10: v8::internal::Map::TransitionToDataProperty(v8::internal::Handle<v8::internal::Map>, v8::internal::Handle<v8::internal::Name>, v8::internal::Handle<v8::internal::Object>, v8::internal::PropertyAttributes, v8::internal::PropertyConstness, v8::internal::Object::StoreFromKeyed) [node]
11: v8::internal::LookupIterator::PrepareTransitionToDataProperty(v8::internal::Handle<v8::internal::JSObject>, v8::internal::Handle<v8::internal::Object>, v8::internal::PropertyAttributes, v8::internal::Object::StoreFromKeyed) [node]
12: v8::internal::StoreIC::LookupForWrite(v8::internal::LookupIterator*, v8::internal::Handle<v8::internal::Object>, v8::internal::Object::StoreFromKeyed) [node]
13: v8::internal::StoreIC::UpdateCaches(v8::internal::LookupIterator*, v8::internal::Handle<v8::internal::Object>, v8::internal::Object::StoreFromKeyed) [node]
14: v8::internal::StoreIC::Store(v8::internal::Handle<v8::internal::Object>, v8::internal::Handle<v8::internal::Name>, v8::internal::Handle<v8::internal::Object>, v8::internal::Object::StoreFromKeyed) [node]
15: v8::internal::Runtime_StoreIC_Miss(int, v8::internal::Object**, v8::internal::Isolate*) [node]
16: 0x16c0667840dd
Done in 148089.23s.

And again today
yarn start v0.27.5
$ HOST=0.0.0.0 nuxt start

 OPEN  http://localhost:3000

control-settings
control-settings
control-images

<--- Last few GCs --->

[16624:0x2b58f10] 143724943 ms: Mark-sweep 1400.0 (1486.9) -> 1400.0 (1486.9) MB, 2268.4 / 0.0 ms  allocation failure GC in old space requested
[16624:0x2b58f10] 143726690 ms: Mark-sweep 1400.0 (1486.9) -> 1400.0 (1486.9) MB, 1746.2 / 0.0 ms  last resort
[16624:0x2b58f10] 143728669 ms: Mark-sweep 1400.0 (1486.9) -> 1400.0 (1486.9) MB, 1979.9 / 0.0 ms  last resort


<--- JS stacktrace --->

==== JS stack trace =========================================

Security context: 0x10cc8381cca1 <JSObject>
    2: $watch [/home/ec2-user/api/web/node_modules/vue/dist/vue.runtime.common.js:3362] [bytecode=0xa9573cc5771 offset=58](this=0x3374d9153869 <Vue$3 map = 0x16794112bb81>,expOrFn=0x27709a2361b1 <String[8]: nuxt.err>,cb=0x3374d91549f9 <JSFunction boundFn (sfi = 0xa9573cc3f21)>,options=0x3374d9154ca9 <Object map = 0x13ee4d484829>)
    4: createWatcher(aka createWatcher) [/home/ec2-user/api/web/no...

FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory
 1: node::Abort() [node]
 2: 0x136916c [node]
 3: v8::Utils::ReportOOMFailure(char const*, bool) [node]
 4: v8::internal::V8::FatalProcessOutOfMemory(char const*, bool) [node]
 5: v8::internal::Factory::NewTransitionArray(int) [node]
 6: v8::internal::TransitionArray::Insert(v8::internal::Handle<v8::internal::Map>, v8::internal::Handle<v8::internal::Name>, v8::internal::Handle<v8::internal::Map>, v8::internal::SimpleTransitionFlag) [node]
 7: v8::internal::Map::CopyReplaceDescriptors(v8::internal::Handle<v8::internal::Map>, v8::internal::Handle<v8::internal::DescriptorArray>, v8::internal::Handle<v8::internal::LayoutDescriptor>, v8::internal::TransitionFlag, v8::internal::MaybeHandle<v8::internal::Name>, char const*, v8::internal::SimpleTransitionFlag) [node]
 8: v8::internal::Map::CopyAddDescriptor(v8::internal::Handle<v8::internal::Map>, v8::internal::Descriptor*, v8::internal::TransitionFlag) [node]
 9: v8::internal::Map::CopyWithField(v8::internal::Handle<v8::internal::Map>, v8::internal::Handle<v8::internal::Name>, v8::internal::Handle<v8::internal::FieldType>, v8::internal::PropertyAttributes, v8::internal::PropertyConstness, v8::internal::Representation, v8::internal::TransitionFlag) [node]
10: v8::internal::Map::TransitionToDataProperty(v8::internal::Handle<v8::internal::Map>, v8::internal::Handle<v8::internal::Name>, v8::internal::Handle<v8::internal::Object>, v8::internal::PropertyAttributes, v8::internal::PropertyConstness, v8::internal::Object::StoreFromKeyed) [node]
11: v8::internal::LookupIterator::PrepareTransitionToDataProperty(v8::internal::Handle<v8::internal::JSObject>, v8::internal::Handle<v8::internal::Object>, v8::internal::PropertyAttributes, v8::internal::Object::StoreFromKeyed) [node]
12: v8::internal::StoreIC::LookupForWrite(v8::internal::LookupIterator*, v8::internal::Handle<v8::internal::Object>, v8::internal::Object::StoreFromKeyed) [node]
13: v8::internal::StoreIC::UpdateCaches(v8::internal::LookupIterator*, v8::internal::Handle<v8::internal::Object>, v8::internal::Object::StoreFromKeyed) [node]
14: v8::internal::StoreIC::Store(v8::internal::Handle<v8::internal::Object>, v8::internal::Handle<v8::internal::Name>, v8::internal::Handle<v8::internal::Object>, v8::internal::Object::StoreFromKeyed) [node]
15: v8::internal::Runtime_StoreIC_Miss(int, v8::internal::Object**, v8::internal::Isolate*) [node]
16: 0x2007965840dd
Done in 143729.38s.


```
Author:
```
vue-bot
```
Text:
```

Hello, your issue has been closed because it does not conform to our issue requirements. Please use the Issue Helper to create an issue - thank you!

```

# Pull
## 9116
Title:
```

        chore: fix grammar in core/observer/index.js comments
      
```
Author:
```
HusamIbrahim
```
Text:
```

What kind of change does this PR introduce? (check at least one)

 Bugfix
 Feature
 Code style update
 Refactor
 Build-related changes
 Other, please describe:

Does this PR introduce a breaking change? (check one)

 Yes
 No

If yes, please describe the impact and migration path for existing applications:
The PR fulfills these requirements:

 It's submitted to the dev branch for v2.x (or to a previous version branch), not the master branch
 When resolving a specific issue, it's referenced in the PR's title (e.g. fix #xxx[,#xxx], where "xxx" is the issue number)
 All tests are passing: https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md#development-setup
 New/updated tests are included

If adding a new feature, the PR's description includes:

 A convincing reason for adding this feature (to avoid wasting your time, it's best to open a suggestion issue first and wait for approval before working on it)

Other information:

```

## 7450
Title:
```

        perf(state.js): check NODE_ENV before other if-statements - for better dead code elimination
      
```
Author:
```
Platonn
```
Text:
```

What kind of change does this PR introduce? (check at least one)

 Bugfix
 Feature
 Code style update
 Refactor
 Build-related changes
 Other, please describe: Performance

Does this PR introduce a breaking change? (check one)

 Yes
 No

If yes, please describe the impact and migration path for existing applications:
The PR fulfills these requirements:

 It's submitted to the dev branch for v2.x (or to a previous version branch), not the master branch
 When resolving a specific issue, it's referenced in the PR's title (e.g. fix #xxx[,#xxx], where "xxx" is the issue number)
 All tests are passing: https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md#development-setup
 New/updated tests are included

If adding a new feature, the PR's description includes:

 A convincing reason for adding this feature (to avoid wasting your time, it's best to open a suggestion issue first and wait for approval before working on it)

Other information:

```
Author:
```
yyx990803
```
Text:
```

This is intentional, invalid data return values must be normalized into objects, and the behavior needs to be consistent between dev and prod.

```

