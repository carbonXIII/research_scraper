# facebook/react
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_packages_react_interactions_accessibility_docs_FocusContain_md](#_packages_react_interactions_accessibility_docs_FocusContain_md)

* [_packages_babel_plugin_react_jsx_README_md](#_packages_babel_plugin_react_jsx_README_md)

* [_CHANGELOG_md](#_CHANGELOG_md)

* [_fixtures_dom_src_components_fixtures_text_inputs_README_md](#_fixtures_dom_src_components_fixtures_text_inputs_README_md)

* [_scripts_eslint_rules_README_md](#_scripts_eslint_rules_README_md)

* [_packages_react_is_README_md](#_packages_react_is_README_md)

* [_packages_react_dom_README_md](#_packages_react_dom_README_md)

* [_packages_react_devtools_README_md](#_packages_react_devtools_README_md)

* [_packages_react_devtools_shared_src_node_modules_react_window_CHANGELOG_md](#_packages_react_devtools_shared_src_node_modules_react_window_CHANGELOG_md)

* [_packages_react_reconciler_README_md](#_packages_react_reconciler_README_md)

* [_packages_react_devtools_inline_README_md](#_packages_react_devtools_inline_README_md)

* [_fixtures_dom_README_md](#_fixtures_dom_README_md)

* [_fixtures_ssr_README_md](#_fixtures_ssr_README_md)

* [_packages_jest_mock_scheduler_README_md](#_packages_jest_mock_scheduler_README_md)

* [_scripts_release_README_md](#_scripts_release_README_md)

* [_scripts_error_codes_README_md](#_scripts_error_codes_README_md)

* [_packages_react_interactions_events_README_md](#_packages_react_interactions_events_README_md)

* [_fixtures_unstable_async_time_slicing_README_md](#_fixtures_unstable_async_time_slicing_README_md)

* [_CONTRIBUTING_md](#_CONTRIBUTING_md)

* [_packages_react_interactions_accessibility_docs_FocusManager_md](#_packages_react_interactions_accessibility_docs_FocusManager_md)

[- Inline](#Inline)

* [_packages_scheduler_src_TracingSubscriptions_js](#_packages_scheduler_src_TracingSubscriptions_js)

* [_packages_react_refresh_src_tests_ReactFresh_test_js](#_packages_react_refresh_src_tests_ReactFresh_test_js)

* [_packages_react_devtools_shared_src_devtools_views_Profiler_SidebarInteractions_js](#_packages_react_devtools_shared_src_devtools_views_Profiler_SidebarInteractions_js)

* [_fixtures_dom_src_components_fixtures_number_inputs_index_js](#_fixtures_dom_src_components_fixtures_number_inputs_index_js)

* [_packages_react_is_npm_index_js](#_packages_react_is_npm_index_js)

* [_scripts_bench_stats_js](#_scripts_bench_stats_js)

* [_packages_react_reconciler_src_tests_ReactLazy_test_internal_js](#_packages_react_reconciler_src_tests_ReactLazy_test_internal_js)

* [_scripts_rollup_shims_facebook_www_renderSubtreeIntoContainer_DO_NOT_USE_js](#_scripts_rollup_shims_facebook_www_renderSubtreeIntoContainer_DO_NOT_USE_js)

* [_packages_react_dom_src_events_tests_SyntheticClipboardEvent_test_js](#_packages_react_dom_src_events_tests_SyntheticClipboardEvent_test_js)

* [_scripts_jest_matchers_reactTestMatchers_js](#_scripts_jest_matchers_reactTestMatchers_js)

* [_packages_react_devtools_shared_src_tests_profilerContext_test_js](#_packages_react_devtools_shared_src_tests_profilerContext_test_js)

* [_packages_react_devtools_shared_src_devtools_views_TabBar_js](#_packages_react_devtools_shared_src_devtools_views_TabBar_js)

* [_packages_react_dom_src_tests_ReactIdentity_test_js](#_packages_react_dom_src_tests_ReactIdentity_test_js)

* [_packages_react_reconciler_src_ReactFiberInstrumentation_js](#_packages_react_reconciler_src_ReactFiberInstrumentation_js)

* [_packages_react_src_ReactCreateRef_js](#_packages_react_src_ReactCreateRef_js)

* [_packages_react_dom_src_shared_CSSShorthandProperty_js](#_packages_react_dom_src_shared_CSSShorthandProperty_js)

* [_packages_scheduler_npm_umd_scheduler_development_js](#_packages_scheduler_npm_umd_scheduler_development_js)

* [_packages_react_stream_inline_typed_js](#_packages_react_stream_inline_typed_js)

* [_fixtures_ssr_src_components_Suspend_js](#_fixtures_ssr_src_components_Suspend_js)

* [_packages_react_dom_src_tests_ReactLegacyErrorBoundaries_test_internal_js](#_packages_react_dom_src_tests_ReactLegacyErrorBoundaries_test_internal_js)

[- Issues](#Issues)

* [1580](#1580)

* [2400](#2400)

* [2886](#2886)

* [13104](#13104)

* [14408](#14408)

* [9085](#9085)

* [10204](#10204)

* [1107](#1107)

* [847](#847)

[- Pull](#Pull)

* [6133](#6133)

* [2512](#2512)

* [8279](#8279)

* [4114](#4114)

* [821](#821)

* [15346](#15346)

* [14673](#14673)

* [9881](#9881)

* [9634](#9634)

* [3129](#3129)

* [5287](#5287)

<!-- toc -->

# Info
## description
A declarative, efficient, and flexible JavaScript library for building user interfaces.

# Markdown
## _packages_react_interactions_accessibility_docs_FocusContain_md
```# FocusContain

`FocusContain` is a component that contains user-focusability to only that
of the children of the component. This means focus control will not escape
unless the componoent is disabled (using the `disabled` prop) or unmounted.
Additionally, `FocusContain` can contain tab focus when passed a `ReactScope`
using the `tabFocus` prop.

## Usage

'''jsx
import FocusContain from 'react-interactions/accessibility/focus-contain';
import tabbableScopeQuery from 'react-interactions/accessibility/tabbable-scope-query';

function MyDialog(props) {
  return (
    <FocusContain scopeQuery={tabbableScopeQuery} disabled={false}>
      <div>
        <h2>{props.title}<h2>
        <p>{props.text}</p>
        <Button onPress={...}>Accept</Button>
        <Button onPress={...}>Close</Button>
      </div>
    </FocusContain>
  )
}
'''
```
## _packages_babel_plugin_react_jsx_README_md
```This package is intended to eventually replace the current `@babel/plugin-transform-react-jsx`, changing the JSX transform from targeting `React.createElement(type, props, children)` to `React.jsx(types, props, key)`. 

https://github.com/reactjs/rfcs/blob/createlement-rfc/text/0000-create-element-changes.md

**This is experimental and not intended to be used directly.**
```
## _CHANGELOG_md
```## [Unreleased]
<details>
  <summary>
    Changes that have landed in master but are not yet released.
    Click to see more.
  </summary>
</details>

## 16.10.2 (October 3, 2019)

### React DOM

* Fix regression in react-native-web by restoring order of arguments in event plugin extractors ([@necolas](https://github.com/necolas) in [#16978](https://github.com/facebook/react/pull/16978))

## 16.10.1 (September 28, 2019)

### React DOM

* Fix regression in Next.js apps by allowing Suspense mismatch during hydration to silently proceed ([@sebmarkbage](https://github.com/sebmarkbage) in [#16943](https://github.com/facebook/react/pull/16943))

## 16.10.0 (September 27, 2019)

### React DOM

* Fix edge case where a hook update wasn't being memoized. ([@sebmarkbage](http://github.com/sebmarkbage) in [#16359](https://github.com/facebook/react/pull/16359))
* Fix heuristic for determining when to hydrate, so we don't incorrectly hydrate during an update. ([@sebmarkbage](http://github.com/sebmarkbage) in [#16739](https://github.com/facebook/react/pull/16739))
* Clear additional fiber fields during unmount to save memory. ([@trueadm](http://github.com/trueadm) in [#16807](https://github.com/facebook/react/pull/16807))
* Fix bug with required text fields in Firefox. ([@halvves](http://github.com/halvves) in [#16578](https://github.com/facebook/react/pull/16578))
* Prefer `Object.is` instead of inline polyfill, when available. ([@ku8ar](http://github.com/ku8ar) in [#16212](https://github.com/facebook/react/pull/16212))
* Fix bug when mixing Suspense and error handling. ([@acdlite](http://github.com/acdlite) in [#16801](https://github.com/facebook/react/pull/16801))


### Scheduler (Experimental)

* Improve queue performance by switching its internal data structure to a min binary heap. ([@acdlite](http://github.com/acdlite) in [#16245](https://github.com/facebook/react/pull/16245))
* Use `postMessage` loop with short intervals instead of attempting to align to frame boundaries with `requestAnimationFrame`. ([@acdlite](http://github.com/acdlite) in [#16214](https://github.com/facebook/react/pull/16214))

### useSubscription

* Avoid tearing issue when a mutation happens and the previous update is still in progress. ([@bvaughn](http://github.com/bvaughn) in [#16623](https://github.com/facebook/react/pull/16623))

## 16.9.0 (August 8, 2019)

### React

* Add `<React.Profiler>` API for gathering performance measurements programmatically. ([@bvaughn](https://github.com/bvaughn) in [#15172](https://github.com/facebook/react/pull/15172))
* Remove `unstable_ConcurrentMode` in favor of `unstable_createRoot`. ([@acdlite](https://github.com/acdlite) in [#15532](https://github.com/facebook/react/pull/15532))

### React DOM

* Deprecate old names for the `UNSAFE_*` lifecycle methods. ([@bvaughn](https://github.com/bvaughn) in [#15186](https://github.com/facebook/react/pull/15186) and [@threepointone](https://github.com/threepointone) in [#16103](https://github.com/facebook/react/pull/16103))
* Deprecate `javascript:` URLs as a common attack surface. ([@sebmarkbage](https://github.com/sebmarkbage) in [#15047](https://github.com/facebook/react/pull/15047))
* Deprecate uncommon "module pattern" (factory) components. ([@sebmarkbage](https://github.com/sebmarkbage) in [#15145](https://github.com/facebook/react/pull/15145))
* Add support for the `disablePictureInPicture` attribute on `<video>`. ([@eek](https://github.com/eek) in [#15334](https://github.com/facebook/react/pull/15334))
* Add support for `onLoad` event for `<embed>`. ([@cherniavskii](https://github.com/cherniavskii) in [#15614](https://github.com/facebook/react/pull/15614))
* Add support for editing `useState` state from DevTools. ([@bvaughn](https://github.com/bvaughn) in [#14906](https://github.com/facebook/react/pull/14906))
* Add support for toggling Suspense from DevTools. ([@gaearon](https://github.com/gaearon) in [#15232](https://github.com/facebook/react/pull/15232))
* Warn when `setState` is called from `useEffect`, creating a loop. ([@gaearon](https://github.com/gaearon) in [#15180](https://github.com/facebook/react/pull/15180))
* Fix a memory leak. ([@paulshen](https://github.com/paulshen) in [#16115](https://github.com/facebook/react/pull/16115))
* Fix a crash inside `findDOMNode` for components wrapped in `<Suspense>`. ([@acdlite](https://github.com/acdlite) in [#15312](https://github.com/facebook/react/pull/15312))
* Fix pending effects from being flushed too late. ([@acdlite](https://github.com/acdlite) in [#15650](https://github.com/facebook/react/pull/15650))
* Fix incorrect argument order in a warning message. ([@brickspert](https://github.com/brickspert) in [#15345](https://github.com/facebook/react/pull/15345))
* Fix hiding Suspense fallback nodes when there is an `!important` style. ([@acdlite](https://github.com/acdlite) in [#15861](https://github.com/facebook/react/pull/15861) and [#15882](https://github.com/facebook/react/pull/15882))
* Slightly improve hydration performance. ([@bmeurer](https://github.com/bmeurer) in [#15998](https://github.com/facebook/react/pull/15998))

### React DOM Server

* Fix incorrect output for camelCase custom CSS property names. ([@bedakb](https://github.com/bedakb) in [#16167](https://github.com/facebook/react/pull/16167))

### React Test Utilities and Test Renderer

* Add `act(async () => ...)` for testing asynchronous state updates. ([@threepointone](https://github.com/threepointone) in [#14853](https://github.com/facebook/react/pull/14853))
* Add support for nesting `act` from different renderers. ([@threepointone](https://github.com/threepointone) in [#16039](https://github.com/facebook/react/pull/16039) and [#16042](https://github.com/facebook/react/pull/16042))
* Warn in Strict Mode if effects are scheduled outside an `act()` call. ([@threepointone](https://github.com/threepointone) in [#15763](https://github.com/facebook/react/pull/15763) and [#16041](https://github.com/facebook/react/pull/16041))
* Warn when using `act` from the wrong renderer. ([@threepointone](https://github.com/threepointone) in [#15756](https://github.com/facebook/react/pull/15756))

### ESLint Plugin: React Hooks

* Report Hook calls at the top level as a violation. ([gaearon](https://github.com/gaearon) in [#16455](https://github.com/facebook/react/pull/16455))

## 16.8.6 (March 27, 2019)

### React DOM

* Fix an incorrect bailout in `useReducer()`. ([@acdlite](https://github.com/acdlite) in [#15124](https://github.com/facebook/react/pull/15124))
* Fix iframe warnings in Safari DevTools. ([@renanvalentin](https://github.com/renanvalentin) in [#15099](https://github.com/facebook/react/pull/15099))
* Warn if `contextType` is set to `Context.Consumer` instead of `Context`. ([@aweary](https://github.com/aweary) in [#14831](https://github.com/facebook/react/pull/14831))
* Warn if `contextType` is set to invalid values. ([@gaearon](https://github.com/gaearon) in [#15142](https://github.com/facebook/react/pull/15142))

## 16.8.5 (March 22, 2019)

### React DOM

* Don't set the first option as selected in select tag with `size` attribute. ([@kulek1](https://github.com/kulek1) in [#14242](https://github.com/facebook/react/pull/14242))
* Improve the `useEffect(async () => ...)` warning message. ([@gaearon](https://github.com/gaearon) in [#15118](https://github.com/facebook/react/pull/15118))
* Improve the error message sometimes caused by duplicate React. ([@jaredpalmer](https://github.com/jaredpalmer) in [#15139](https://github.com/facebook/react/pull/15139))

### React DOM Server

* Improve the `useLayoutEffect` warning message when server rendering. ([@gaearon](https://github.com/gaearon) in [#15158](https://github.com/facebook/react/pull/15158))

### React Shallow Renderer

* Fix `setState` in shallow renderer to work with Hooks. ([@gaearon](https://github.com/gaearon) in [#15120](https://github.com/facebook/react/pull/15120))
* Fix shallow renderer to support `React.memo`. ([@aweary](https://github.com/aweary) in [#14816](https://github.com/facebook/react/pull/14816))
* Fix shallow renderer to support Hooks inside `forwardRef`. ([@eps1lon](https://github.com/eps1lon) in [#15100](https://github.com/facebook/react/pull/15100))

## 16.8.4 (March 5, 2019)

### React DOM and other renderers

- Fix a bug where DevTools caused a runtime error when inspecting a component that used a `useContext` hook. ([@bvaughn](https://github.com/bvaughn) in [#14940](https://github.com/facebook/react/pull/14940))

## 16.8.3 (February 21, 2019)

### React DOM

* Fix a bug that caused inputs to behave incorrectly in UMD builds. ([@gaearon](https://github.com/gaearon) in [#14914](https://github.com/facebook/react/pull/14914))
* Fix a bug that caused render phase updates to be discarded. ([@gaearon](https://github.com/gaearon) in [#14852](https://github.com/facebook/react/pull/14852))

### React DOM Server
* Unwind the context stack when a stream is destroyed without completing, to prevent incorrect values during a subsequent render. ([@overlookmotel](https://github.com/overlookmotel) in [#14706](https://github.com/facebook/react/pull/14706/))

### ESLint Plugin for React Hooks

* Add a new recommended `exhaustive-deps` rule. ([@gaearon](https://github.com/gaearon) in [#14636](https://github.com/facebook/react/pull/14636))

## 16.8.2 (February 14, 2019)

### React DOM

* Fix `ReactDOM.render` being ignored inside `useEffect`. ([@gaearon](https://github.com/gaearon) in [#14799](https://github.com/facebook/react/pull/14799))
* Fix a crash when unmounting empty portals. ([@gaearon](https://github.com/gaearon) in [#14820](https://github.com/facebook/react/pull/14820))
* Fix `useImperativeHandle` to work correctly when no deps are specified. ([@gaearon](https://github.com/gaearon) in [#14801](https://github.com/facebook/react/pull/14801))
* Fix `crossOrigin` attribute to work in SVG `image` elements. ([@aweary](https://github.com/aweary) in [#14832](https://github.com/facebook/react/pull/14832))
* Fix a false positive warning when using Suspense with Hooks. ([@gaearon](https://github.com/gaearon) in [#14821](https://github.com/facebook/react/pull/14821))

### React Test Utils and React Test Renderer

* Include component stack into the `act()` warning. ([@threepointone](https://github.com/threepointone) in [#14855](https://github.com/facebook/react/pull/14855))

## 16.8.1 (February 6, 2019)

### React DOM and React Test Renderer

* Fix a crash when used together with an older version of React. ([@bvaughn](https://github.com/bvaughn) in [#14770](https://github.com/facebook/react/pull/14770))

### React Test Utils

* Fix a crash in Node environment. ([@threepointone](https://github.com/threepointone) in [#14768](https://github.com/facebook/react/pull/14768))

## 16.8.0 (February 6, 2019)

### React

* Add [Hooks](https://reactjs.org/docs/hooks-intro.html) — a way to use state and other React features without writing a class. ([@acdlite](https://github.com/acdlite) et al. in [#13968](https://github.com/facebook/react/pull/13968))
* Improve the `useReducer` Hook lazy initialization API. ([@acdlite](https://github.com/acdlite) in [#14723](https://github.com/facebook/react/pull/14723))

### React DOM

* Bail out of rendering on identical values for `useState` and `useReducer` Hooks. ([@acdlite](https://github.com/acdlite) in [#14569](https://github.com/facebook/react/pull/14569))
* Use `Object.is` algorithm for comparing `useState` and `useReducer` values. ([@Jessidhia](https://github.com/Jessidhia) in [#14752](https://github.com/facebook/react/pull/14752))
* Don’t compare the first argument passed to `useEffect`/`useMemo`/`useCallback` Hooks. ([@acdlite](https://github.com/acdlite) in [#14594](https://github.com/facebook/react/pull/14594))
* Support synchronous thenables passed to `React.lazy()`. ([@gaearon](https://github.com/gaearon) in [#14626](https://github.com/facebook/react/pull/14626))
* Render components with Hooks twice in Strict Mode (DEV-only) to match class behavior. ([@gaearon](https://github.com/gaearon) in [#14654](https://github.com/facebook/react/pull/14654))
* Warn about mismatching Hook order in development. ([@threepointone](https://github.com/threepointone) in [#14585](https://github.com/facebook/react/pull/14585) and [@acdlite](https://github.com/acdlite) in [#14591](https://github.com/facebook/react/pull/14591))
* Effect clean-up functions must return either `undefined` or a function. All other values, including `null`, are not allowed. [@acdlite](https://github.com/acdlite) in [#14119](https://github.com/facebook/react/pull/14119)

### React Test Renderer and Test Utils

* Support Hooks in the shallow renderer. ([@trueadm](https://github.com/trueadm) in [#14567](https://github.com/facebook/react/pull/14567))
* Fix wrong state in `shouldComponentUpdate` in the presence of `getDerivedStateFromProps` for Shallow Renderer. ([@chenesan](https://github.com/chenesan) in [#14613](https://github.com/facebook/react/pull/14613))
* Add `ReactTestRenderer.act()` and `ReactTestUtils.act()` for batching updates so that tests more closely match real behavior. ([@threepointone](https://github.com/threepointone) in [#14744](https://github.com/facebook/react/pull/14744))


### ESLint Plugin: React Hooks

* Initial [release](https://www.npmjs.com/package/eslint-plugin-react-hooks). ([@calebmer](https://github.com/calebmer) in [#13968](https://github.com/facebook/react/pull/13968))
* Fix reporting after encountering a loop. ([@calebmer](https://github.com/calebmer) and [@Yurickh](https://github.com/Yurickh) in [#14661](https://github.com/facebook/react/pull/14661))
* Don't consider throwing to be a rule violation. ([@sophiebits](https://github.com/sophiebits) in [#14040](https://github.com/facebook/react/pull/14040))

## 16.7.0 (December 19, 2018)

### React DOM

* Fix performance of `React.lazy` for large numbers of lazily-loaded components. ([@acdlite](http://github.com/acdlite) in [#14429](https://github.com/facebook/react/pull/14429))
* Clear fields on unmount to avoid memory leaks. ([@trueadm](http://github.com/trueadm) in [#14276](https://github.com/facebook/react/pull/14276))
* Fix bug with SSR and context when mixing `react-dom/server@16.6` and `react@<16.6`. ([@gaearon](http://github.com/gaearon) in [#14291](https://github.com/facebook/react/pull/14291))
* Fix a performance regression in profiling mode. ([@bvaughn](http://github.com/bvaughn) in [#14383](https://github.com/facebook/react/pull/14383))

### Scheduler (Experimental)

* Post to MessageChannel instead of window. ([@acdlite](http://github.com/acdlite) in [#14234](https://github.com/facebook/react/pull/14234))
* Reduce serialization overhead. ([@developit](http://github.com/developit) in [#14249](https://github.com/facebook/react/pull/14249))
* Fix fallback to `setTimeout` in testing environments. ([@bvaughn](http://github.com/bvaughn) in [#14358](https://github.com/facebook/react/pull/14358))
* Add methods for debugging. ([@mrkev](http://github.com/mrkev) in [#14053](https://github.com/facebook/react/pull/14053))


## 16.6.3 (November 12, 2018)

### React DOM

* Fix bugs in `Suspense` and `lazy`. ([@acdlite](https://github.com/acdlite) in [#14133](https://github.com/facebook/react/pull/14133), [#14157](https://github.com/facebook/react/pull/14157), and [#14164](https://github.com/facebook/react/pull/14164))
* Fix highlighting of `React.memo` updates in React DevTools. ([@bvaughn](https://github.com/bvaughn) in [#14141](https://github.com/facebook/react/pull/14141))
* Fix interaction of Suspense with the React Profiler. ([@bvaughn](https://github.com/bvaughn) in [#14065](https://github.com/facebook/react/pull/14065))
* Fix a false positive warning when using Suspense. ([@acdlite](https://github.com/acdlite) in [#14158](https://github.com/facebook/react/pull/14158))

### React DOM Server

* Fix incorrect sharing of context state between `renderToNodeStream()` calls. ([@sebmarkbage](https://github.com/sebmarkbage) in [#14182](https://github.com/facebook/react/pull/14182))
* Add a warning about incorrect usage of the context API. ([@trueadm](https://github.com/trueadm) in [#14033](https://github.com/facebook/react/pull/14033))

## 16.6.2 (November 12, 2018)

This release was published in a broken state and should be skipped.

## 16.6.1 (November 6, 2018)

### React DOM

* Fallback should not remount every time a promise resolves. ([@acdlite](https://github.com/acdlite) in [#14083](https://github.com/facebook/react/pull/14083))
* Fix bug where Suspense keeps showing fallback even after everything finishes loading. ([@acdlite](https://github.com/acdlite) in [#14083](https://github.com/facebook/react/pull/14083))
* Fix a crash when Suspense finishes loading in IE11. ([@sophiebits](https://github.com/sophiebits) in [#14126](https://github.com/facebook/react/pull/14126))
* Fix unresolved default props in lifecycle methods of a lazy component. ([@gaearon](https://github.com/gaearon) in [#14112](https://github.com/facebook/react/pull/14112))
* Fix bug when recovering from an error thrown during complete phase. ([@gaearon](https://github.com/gaearon) in [#14104](https://github.com/facebook/react/pull/14104))

### Scheduler (Experimental)

* Switch from deadline object to `shouldYield` API. ([@acdlite](https://github.com/acdlite) in [#14025](https://github.com/facebook/react/pull/14025))


## 16.6.0 (October 23, 2018)

### React

* Add `React.memo()` as an alternative to `PureComponent` for functions. ([@acdlite](https://github.com/acdlite) in [#13748](https://github.com/facebook/react/pull/13748))
* Add `React.lazy()` for code splitting components. ([@acdlite](https://github.com/acdlite) in [#13885](https://github.com/facebook/react/pull/13885))
* `React.StrictMode` now warns about legacy context API. ([@bvaughn](https://github.com/bvaughn) in [#13760](https://github.com/facebook/react/pull/13760))
* `React.StrictMode` now warns about `findDOMNode`. ([@sebmarkbage](https://github.com/sebmarkbage) in [#13841](https://github.com/facebook/react/pull/13841))
* Rename `unstable_AsyncMode` to `unstable_ConcurrentMode`. ([@trueadm](https://github.com/trueadm) in [#13732](https://github.com/facebook/react/pull/13732))
* Rename `unstable_Placeholder` to `Suspense`, and `delayMs` to `maxDuration`. ([@gaearon](https://github.com/gaearon) in [#13799](https://github.com/facebook/react/pull/13799) and [@sebmarkbage](https://github.com/sebmarkbage) in [#13922](https://github.com/facebook/react/pull/13922))

### React DOM

* Add `contextType` as a more ergonomic way to subscribe to context from a class. ([@bvaughn](https://github.com/bvaughn) in [#13728](https://github.com/facebook/react/pull/13728))
* Add `getDerivedStateFromError` lifecycle method for catching errors in a future asynchronous server-side renderer. ([@bvaughn](https://github.com/bvaughn) in [#13746](https://github.com/facebook/react/pull/13746))
* Warn when `<Context>` is used instead of `<Context.Consumer>`. ([@trueadm](https://github.com/trueadm) in [#13829](https://github.com/facebook/react/pull/13829))
* Fix gray overlay on iOS Safari. ([@philipp-spiess](https://github.com/philipp-spiess) in [#13778](https://github.com/facebook/react/pull/13778))
* Fix a bug caused by overwriting `window.event` in development. ([@sergei-startsev](https://github.com/sergei-startsev) in [#13697](https://github.com/facebook/react/pull/13697))

### React DOM Server

* Add support for `React.memo()`. ([@alexmckenley](https://github.com/alexmckenley) in [#13855](https://github.com/facebook/react/pull/13855))
* Add support for `contextType`. ([@alexmckenley](https://github.com/alexmckenley) and [@sebmarkbage](https://github.com/sebmarkbage) in [#13889](https://github.com/facebook/react/pull/13889))

### Scheduler (Experimental)

* Rename the package to `scheduler`. ([@gaearon](https://github.com/gaearon) in [#13683](https://github.com/facebook/react/pull/13683))
* Support priority levels, continuations, and wrapped callbacks. ([@acdlite](https://github.com/acdlite) in [#13720](https://github.com/facebook/react/pull/13720) and [#13842](https://github.com/facebook/react/pull/13842))
* Improve the fallback mechanism in non-DOM environments. ([@acdlite](https://github.com/acdlite) in [#13740](https://github.com/facebook/react/pull/13740))
* Schedule `requestAnimationFrame` earlier. ([@acdlite](https://github.com/acdlite) in [#13785](https://github.com/facebook/react/pull/13785))
* Fix the DOM detection to be more thorough. ([@trueadm](https://github.com/trueadm) in [#13731](https://github.com/facebook/react/pull/13731))
* Fix bugs with interaction tracing. ([@bvaughn](https://github.com/bvaughn) in [#13590](https://github.com/facebook/react/pull/13590))
* Add the `envify` transform to the package. ([@mridgway](https://github.com/mridgway) in [#13766](https://github.com/facebook/react/pull/13766))

## 16.5.2 (September 18, 2018)

### React DOM

* Fixed a recent `<iframe>` regression ([@JSteunou](https://github.com/JSteunou) in [#13650](https://github.com/facebook/react/pull/13650))
* Fix `updateWrapper` so that `<textarea>`s no longer re-render when data is unchanged ([@joelbarbosa](https://github.com/joelbarbosa) in [#13643](https://github.com/facebook/react/pull/13643))

### Schedule (Experimental)

* Renaming "tracking" API to "tracing" ([@bvaughn](https://github.com/bvaughn) in [#13641](https://github.com/facebook/react/pull/13641))
* Add UMD production+profiling entry points ([@bvaughn](https://github.com/bvaughn) in [#13642](https://github.com/facebook/react/pull/13642))
* Refactored `schedule` to remove some React-isms and improve performance for when deferred updates time out ([@acdlite](https://github.com/acdlite) in [#13582](https://github.com/facebook/react/pull/13582))

## 16.5.1 (September 13, 2018)

### React

* Improve the warning when `React.forwardRef` receives an unexpected number of arguments. ([@andresroberto](https://github.com/andresroberto) in [#13636](https://github.com/facebook/react/issues/13636))

### React DOM

* Fix a regression in unstable exports used by React Native Web. ([@aweary](https://github.com/aweary) in [#13598](https://github.com/facebook/react/issues/13598))
* Fix a crash when component defines a method called `isReactComponent`. ([@gaearon](https://github.com/gaearon) in [#13608](https://github.com/facebook/react/issues/13608))
* Fix a crash in development mode in IE9 when printing a warning. ([@link-alex](https://github.com/link-alex) in [#13620](https://github.com/facebook/react/issues/13620))
* Provide a better error message when running `react-dom/profiling` with `schedule/tracking`. ([@bvaughn](https://github.com/bvaughn) in [#13605](https://github.com/facebook/react/issues/13605))
* If a `ForwardRef` component defines a `displayName`, use it in warnings. ([@probablyup](https://github.com/probablyup) in [#13615](https://github.com/facebook/react/issues/13615))

### Schedule (Experimental)

* Add a separate profiling entry point at `schedule/tracking-profiling`. ([@bvaughn](https://github.com/bvaughn) in [#13605](https://github.com/facebook/react/issues/13605))

## 16.5.0 (September 5, 2018)

### React

* Add a warning if `React.forwardRef` render function doesn't take exactly two arguments ([@bvaughn](https://github.com/bvaughn) in [#13168](https://github.com/facebook/react/issues/13168))
* Improve the error message when passing an element to `createElement` by mistake ([@DCtheTall](https://github.com/DCtheTall) in [#13131](https://github.com/facebook/react/issues/13131))
* Don't call profiler `onRender` until after mutations ([@bvaughn](https://github.com/bvaughn) in [#13572](https://github.com/facebook/react/issues/13572))

### React DOM

* Add support for React DevTools Profiler ([@bvaughn](https://github.com/bvaughn) in [#13058](https://github.com/facebook/react/issues/13058))
* Add `react-dom/profiling` entry point alias for profiling in production ([@bvaughn](https://github.com/bvaughn) in [#13570](https://github.com/facebook/react/issues/13570))
* Add `onAuxClick` event for browsers that support it ([@jquense](https://github.com/jquense) in [#11571](https://github.com/facebook/react/issues/11571))
* Add `movementX` and `movementY` fields to mouse events ([@jasonwilliams](https://github.com/jasonwilliams) in [#9018](https://github.com/facebook/react/issues/9018))
* Add `tangentialPressure` and `twist` fields to pointer events ([@motiz88](https://github.com/motiz88) in [#13374](https://github.com/facebook/react/issues/13374))
* Minimally support iframes (nested browsing contexts) in selection event handling ([@acusti](https://github.com/acusti) in [#12037](https://github.com/facebook/react/issues/12037))
* Support passing booleans to the `focusable` SVG attribute ([@gaearon](https://github.com/gaearon) in [#13339](https://github.com/facebook/react/issues/13339))
* Ignore `<noscript>` on the client when hydrating ([@Ephem](https://github.com/Ephem) in [#13537](https://github.com/facebook/react/issues/13537))
* Fix `gridArea` to be treated as a unitless CSS property ([@mgol](https://github.com/mgol) in [#13550](https://github.com/facebook/react/issues/13550))
* Fix incorrect data in `compositionend` event when typing Korean on IE11 ([@crux153](https://github.com/crux153) in [#12563](https://github.com/facebook/react/issues/12563))
* Fix a crash when using dynamic `children` in the `<option>` tag ([@Slowyn](https://github.com/Slowyn) in [#13261](https://github.com/facebook/react/issues/13261), [@gaearon](https://github.com/gaearon) in [#13465](https://github.com/facebook/react/pull/13465))
* Fix the `checked` attribute not getting initially set on the `input` ([@dilidili](https://github.com/dilidili) in [#13114](https://github.com/facebook/react/issues/13114))
* Fix hydration of `dangerouslySetInnerHTML` when `__html` is not a string ([@gaearon](https://github.com/gaearon) in [#13353](https://github.com/facebook/react/issues/13353))
* Fix a warning about missing controlled `onChange` to fire on falsy values too ([@nicolevy](https://github.com/nicolevy) in [#12628](https://github.com/facebook/react/issues/12628))
* Fix `submit` and `reset` buttons getting an empty label ([@ellsclytn](https://github.com/ellsclytn) in [#12780](https://github.com/facebook/react/issues/12780))
* Fix the `onSelect` event not being triggered after drag and drop ([@gaearon](https://github.com/gaearon) in [#13422](https://github.com/facebook/react/issues/13422))
* Fix the `onClick` event not working inside a portal on iOS ([@aweary](https://github.com/aweary) in [#11927](https://github.com/facebook/react/issues/11927))
* Fix a performance issue when thousands of roots are re-rendered ([@gaearon](https://github.com/gaearon) in [#13335](https://github.com/facebook/react/issues/13335))
* Fix a performance regression that also caused `onChange` to not fire in some cases ([@gaearon](https://github.com/gaearon) in [#13423](https://github.com/facebook/react/issues/13423))
* Handle errors in more edge cases gracefully ([@gaearon](https://github.com/gaearon) in [#13237](https://github.com/facebook/react/issues/13237) and [@acdlite](https://github.com/acdlite) in [#13269](https://github.com/facebook/react/issues/13269))
* Don't use proxies for synthetic events in development ([@gaearon](https://github.com/gaearon) in [#12171](https://github.com/facebook/react/issues/12171))
* Warn when `"false"` or `"true"` is the value of a boolean DOM prop ([@motiz88](https://github.com/motiz88) in [#13372](https://github.com/facebook/react/issues/13372))
* Warn when `this.state` is initialized to `props` ([@veekas](https://github.com/veekas) in [#11658](https://github.com/facebook/react/issues/11658))
* Don't compare `style` on hydration in IE due to noisy false positives ([@mgol](https://github.com/mgol) in [#13534](https://github.com/facebook/react/issues/13534))
* Include `StrictMode` in the component stack ([@gaearon](https://github.com/gaearon) in [#13240](https://github.com/facebook/react/issues/13240))
* Don't overwrite `window.event` in IE ([@ConradIrwin](https://github.com/ConradIrwin) in [#11696](https://github.com/facebook/react/issues/11696))
* Improve component stack for the `folder/index.js` naming convention ([@gaearon](https://github.com/gaearon) in [#12059](https://github.com/facebook/react/issues/12059))
* Improve a warning when using `getDerivedStateFromProps` without initialized state ([@flxwu](https://github.com/flxwu) in [#13317](https://github.com/facebook/react/issues/13317))
* Improve a warning about invalid textarea usage ([@raunofreiberg](https://github.com/raunofreiberg) in [#13361](https://github.com/facebook/react/issues/13361))
* Treat invalid Symbol and function values more consistently ([@raunofreiberg](https://github.com/raunofreiberg) in [#13362](https://github.com/facebook/react/issues/13362) and [#13389](https://github.com/facebook/react/issues/13389))
* Allow Electron `<webview>` tag without warnings ([@philipp-spiess](https://github.com/philipp-spiess) in [#13301](https://github.com/facebook/react/issues/13301))
* Don't show the uncaught error addendum if `e.preventDefault()` was called ([@gaearon](https://github.com/gaearon) in [#13384](https://github.com/facebook/react/issues/13384))
* Warn about rendering Generators ([@gaearon](https://github.com/gaearon) in [#13312](https://github.com/facebook/react/issues/13312))
* Remove irrelevant suggestion of a legacy method from a warning ([@zx6658](https://github.com/zx6658) in [#13169](https://github.com/facebook/react/issues/13169))
* Remove `unstable_deferredUpdates` in favor of `unstable_scheduleWork` from `schedule` ([@gaearon](https://github.com/gaearon) in [#13488](https://github.com/facebook/react/issues/13488))
* Fix unstable asynchronous mode from doing unnecessary work when an update takes too long ([@acdlite](https://github.com/acdlite) in [#13503](https://github.com/facebook/react/issues/13503))

### React DOM Server

* Fix crash with nullish children when using `dangerouslySetInnerHtml` in a selected `<option>` ([@mridgway](https://github.com/mridgway) in [#13078](https://github.com/facebook/react/issues/13078))
* Fix crash when `setTimeout` is missing ([@dustinsoftware](https://github.com/dustinsoftware) in [#13088](https://github.com/facebook/react/issues/13088))

### React Test Renderer and Test Utils

* Fix `this` in a functional component for shallow renderer to be `undefined` ([@koba04](https://github.com/koba04) in [#13144](https://github.com/facebook/react/issues/13144))
* Deprecate a Jest-specific `ReactTestUtils.mockComponent()` helper ([@bvaughn](https://github.com/bvaughn) in [#13193](https://github.com/facebook/react/issues/13193))
* Warn about `ReactDOM.createPortal` usage within the test renderer ([@bvaughn](https://github.com/bvaughn) in [#12895](https://github.com/facebook/react/issues/12895))
* Improve a confusing error message ([@gaearon](https://github.com/gaearon) in [#13351](https://github.com/facebook/react/issues/13351))

### React ART

* Add support for DevTools ([@yunchancho](https://github.com/yunchancho) in [#13173](https://github.com/facebook/react/issues/13173))

### Schedule (Experimental)

* New package for cooperatively scheduling work in a browser environment. It's used by React internally, but its public API is not finalized yet. ([@flarnie](https://github.com/flarnie) in [#12624](https://github.com/facebook/react/pull/12624))

## 16.4.2 (August 1, 2018)

### React DOM Server

* Fix a [potential XSS vulnerability when the attacker controls an attribute name](https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html) (`CVE-2018-6341`). This fix is available in the latest `react-dom@16.4.2`, as well as in previous affected minor versions: `react-dom@16.0.1`, `react-dom@16.1.2`, `react-dom@16.2.1`, and `react-dom@16.3.3`. ([@gaearon](https://github.com/gaearon) in [#13302](https://github.com/facebook/react/pull/13302))

* Fix a crash in the server renderer when an attribute is called `hasOwnProperty`. This fix is only available in `react-dom@16.4.2`. ([@gaearon](https://github.com/gaearon) in [#13303](https://github.com/facebook/react/pull/13303))

## 16.4.1 (June 13, 2018)

### React

* You can now assign `propTypes` to components returned by `React.ForwardRef`. ([@bvaughn](https://github.com/bvaughn) in [#12911](https://github.com/facebook/react/pull/12911))

### React DOM

* Fix a crash when the input `type` changes from some other types to `text`. ([@spirosikmd](https://github.com/spirosikmd) in [#12135](https://github.com/facebook/react/pull/12135))
* Fix a crash in IE11 when restoring focus to an SVG element. ([@ThaddeusJiang](https://github.com/ThaddeusJiang) in [#12996](https://github.com/facebook/react/pull/12996))
* Fix a range input not updating in some cases. ([@Illu](https://github.com/Illu) in [#12939](https://github.com/facebook/react/pull/12939))
* Fix input validation triggering unnecessarily in Firefox. ([@nhunzaker](https://github.com/nhunzaker) in [#12925](https://github.com/facebook/react/pull/12925))
* Fix an incorrect `event.target` value for the `onChange` event in IE9. ([@nhunzaker](https://github.com/nhunzaker) in [#12976](https://github.com/facebook/react/pull/12976))
* Fix a false positive error when returning an empty `<React.Fragment />` from a component. ([@philipp-spiess](https://github.com/philipp-spiess) in [#12966](https://github.com/facebook/react/pull/12966))

### React DOM Server

* Fix an incorrect value being provided by new context API. ([@ericsoderberghp](https://github.com/ericsoderberghp) in [#12985](https://github.com/facebook/react/pull/12985), [@gaearon](https://github.com/gaearon) in [#13019](https://github.com/facebook/react/pull/13019))

### React Test Renderer

* Allow multiple root children in test renderer traversal API. ([@gaearon](https://github.com/gaearon) in [#13017](https://github.com/facebook/react/pull/13017))
* Fix `getDerivedStateFromProps()` in the shallow renderer to not discard the pending state. ([@fatfisz](https://github.com/fatfisz) in [#13030](https://github.com/facebook/react/pull/13030))

## 16.4.0 (May 23, 2018)

### React

* Add a new [experimental](https://github.com/reactjs/rfcs/pull/51) `React.unstable_Profiler` component for measuring performance. ([@bvaughn](https://github.com/bvaughn) in [#12745](https://github.com/facebook/react/pull/12745))

### React DOM

* Add support for the Pointer Events specification. ([@philipp-spiess](https://github.com/philipp-spiess) in [#12507](https://github.com/facebook/react/pull/12507))
* Properly call `getDerivedStateFromProps()` regardless of the reason for re-rendering. ([@acdlite](https://github.com/acdlite) in [#12600](https://github.com/facebook/react/pull/12600) and [#12802](https://github.com/facebook/react/pull/12802))
* Fix a bug that prevented context propagation in some cases. ([@gaearon](https://github.com/gaearon) in [#12708](https://github.com/facebook/react/pull/12708))
* Fix re-rendering of components using `forwardRef()` on a deeper `setState()`. ([@gaearon](https://github.com/gaearon) in [#12690](https://github.com/facebook/react/pull/12690))
* Fix some attributes incorrectly getting removed from custom element nodes. ([@airamrguez](https://github.com/airamrguez) in [#12702](https://github.com/facebook/react/pull/12702))
* Fix context providers to not bail out on children if there's a legacy context provider above. ([@gaearon](https://github.com/gaearon) in [#12586](https://github.com/facebook/react/pull/12586))
* Add the ability to specify `propTypes` on a context provider component. ([@nicolevy](https://github.com/nicolevy) in [#12658](https://github.com/facebook/react/pull/12658))
* Fix a false positive warning when using `react-lifecycles-compat` in `<StrictMode>`. ([@bvaughn](https://github.com/bvaughn) in [#12644](https://github.com/facebook/react/pull/12644))
* Warn when the `forwardRef()` render function has `propTypes` or `defaultProps`. ([@bvaughn](https://github.com/bvaughn) in [#12644](https://github.com/facebook/react/pull/12644))
* Improve how `forwardRef()` and context consumers are displayed in the component stack. ([@sophiebits](https://github.com/sophiebits) in [#12777](https://github.com/facebook/react/pull/12777))
* Change internal event names. This can break third-party packages that rely on React internals in unsupported ways. ([@philipp-spiess](https://github.com/philipp-spiess) in [#12629](https://github.com/facebook/react/pull/12629))

### React Test Renderer

* Fix the `getDerivedStateFromProps()` support to match the new React DOM behavior. ([@koba04](https://github.com/koba04) in [#12676](https://github.com/facebook/react/pull/12676))
* Fix a `testInstance.parent` crash when the parent is a fragment or another special node. ([@gaearon](https://github.com/gaearon) in [#12813](https://github.com/facebook/react/pull/12813))
* `forwardRef()` components are now discoverable by the test renderer traversal methods. ([@gaearon](https://github.com/gaearon) in [#12725](https://github.com/facebook/react/pull/12725))
* Shallow renderer now ignores `setState()` updaters that return `null` or `undefined`. ([@koba04](https://github.com/koba04) in [#12756](https://github.com/facebook/react/pull/12756))

### React ART

* Fix reading context provided from the tree managed by React DOM. ([@acdlite](https://github.com/acdlite) in [#12779](https://github.com/facebook/react/pull/12779))

### React Call Return (Experimental)

* This experiment was deleted because it was affecting the bundle size and the API wasn't good enough. It's likely to come back in the future in some other form. ([@gaearon](https://github.com/gaearon) in [#12820](https://github.com/facebook/react/pull/12820))

### React Reconciler (Experimental)

* The [new host config shape](https://github.com/facebook/react/blob/c601f7a64640290af85c9f0e33c78480656b46bc/packages/react-noop-renderer/src/createReactNoop.js#L82-L285) is flat and doesn't use nested objects. ([@gaearon](https://github.com/gaearon) in [#12792](https://github.com/facebook/react/pull/12792))

## 16.3.3 (August 1, 2018)

### React DOM Server

* Fix a [potential XSS vulnerability when the attacker controls an attribute name](https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html) (`CVE-2018-6341`). This fix is available in the latest `react-dom@16.4.2`, as well as in previous affected minor versions: `react-dom@16.0.1`, `react-dom@16.1.2`, `react-dom@16.2.1`, and `react-dom@16.3.3`. ([@gaearon](https://github.com/gaearon) in [#13302](https://github.com/facebook/react/pull/13302))

## 16.3.2 (April 16, 2018)

### React

* Improve the error message when passing `null` or `undefined` to `React.cloneElement`. ([@nicolevy](https://github.com/nicolevy) in [#12534](https://github.com/facebook/react/pull/12534))

### React DOM

* Fix an IE crash in development when using `<StrictMode>`. ([@bvaughn](https://github.com/bvaughn) in [#12546](https://github.com/facebook/react/pull/12546))
* Fix labels in User Timing measurements for new component types. ([@bvaughn](https://github.com/bvaughn) in [#12609](https://github.com/facebook/react/pull/12609))
* Improve the warning about wrong component type casing. ([@nicolevy](https://github.com/nicolevy) in [#12533](https://github.com/facebook/react/pull/12533))
* Improve general performance in development mode. ([@gaearon](https://github.com/gaearon) in [#12537](https://github.com/facebook/react/pull/12537))
* Improve performance of the experimental `unstable_observedBits` API with nesting. ([@gaearon](https://github.com/gaearon) in [#12543](https://github.com/facebook/react/pull/12543))

### React Test Renderer

* Add a UMD build. ([@bvaughn](https://github.com/bvaughn) in [#12594](https://github.com/facebook/react/pull/12594))

## 16.3.1 (April 3, 2018)

### React

* Fix a false positive warning in IE11 when using `Fragment`. ([@heikkilamarko](https://github.com/heikkilamarko) in [#12504](https://github.com/facebook/react/pull/12504))
* Prefix a private API. ([@Andarist](https://github.com/Andarist) in [#12501](https://github.com/facebook/react/pull/12501))
* Improve the warning when calling `setState()` in constructor. ([@gaearon](https://github.com/gaearon) in [#12532](https://github.com/facebook/react/pull/12532))

### React DOM

* Fix `getDerivedStateFromProps()` not getting applied in some cases. ([@acdlite](https://github.com/acdlite) in [#12528](https://github.com/facebook/react/pull/12528))
* Fix a performance regression in development mode. ([@gaearon](https://github.com/gaearon) in [#12510](https://github.com/facebook/react/pull/12510))
* Fix error handling bugs in development mode. ([@gaearon](https://github.com/gaearon) and [@acdlite](https://github.com/acdlite) in [#12508](https://github.com/facebook/react/pull/12508))
* Improve user timing API messages for profiling. ([@flarnie](https://github.com/flarnie) in [#12384](https://github.com/facebook/react/pull/12384))

### Create Subscription

* Set the package version to be in sync with React releases. ([@bvaughn](https://github.com/bvaughn) in [#12526](https://github.com/facebook/react/pull/12526))
* Add a peer dependency on React 16.3+. ([@NMinhNguyen](https://github.com/NMinhNguyen) in [#12496](https://github.com/facebook/react/pull/12496))

## 16.3.0 (March 29, 2018)

### React

* Add a new officially supported context API. ([@acdlite](https://github.com/acdlite) in [#11818](https://github.com/facebook/react/pull/11818))
* Add a new `React.createRef()` API as an ergonomic alternative to callback refs. ([@trueadm](https://github.com/trueadm) in [#12162](https://github.com/facebook/react/pull/12162))
* Add a new `React.forwardRef()` API to let components forward their refs to a child. ([@bvaughn](https://github.com/bvaughn) in [#12346](https://github.com/facebook/react/pull/12346))
* Fix a false positive warning in IE11 when using `React.Fragment`. ([@XaveScor](https://github.com/XaveScor) in [#11823](https://github.com/facebook/react/pull/11823))
* Replace `React.unstable_AsyncComponent` with `React.unstable_AsyncMode`. ([@acdlite](https://github.com/acdlite) in [#12117](https://github.com/facebook/react/pull/12117))
* Improve the error message when calling `setState()` on an unmounted component. ([@sophiebits](https://github.com/sophiebits) in [#12347](https://github.com/facebook/react/pull/12347))

### React DOM

* Add a new `getDerivedStateFromProps()` lifecycle and `UNSAFE_` aliases for the legacy lifecycles. ([@bvaughn](https://github.com/bvaughn) in [#12028](https://github.com/facebook/react/pull/12028))
* Add a new `getSnapshotBeforeUpdate()` lifecycle. ([@bvaughn](https://github.com/bvaughn) in [#12404](https://github.com/facebook/react/pull/12404))
* Add a new `<React.StrictMode>` wrapper to help prepare apps for async rendering. ([@bvaughn](https://github.com/bvaughn) in [#12083](https://github.com/facebook/react/pull/12083))
* Add support for `onLoad` and `onError` events on the `<link>` tag. ([@roderickhsiao](https://github.com/roderickhsiao) in [#11825](https://github.com/facebook/react/pull/11825))
* Add support for `noModule` boolean attribute on the `<script>` tag. ([@aweary](https://github.com/aweary) in [#11900](https://github.com/facebook/react/pull/11900))
* Fix minor DOM input bugs in IE and Safari. ([@nhunzaker](https://github.com/nhunzaker) in [#11534](https://github.com/facebook/react/pull/11534))
* Correctly detect Ctrl + Enter in `onKeyPress` in more browsers. ([@nstraub](https://github.com/nstraub) in [#10514](https://github.com/facebook/react/pull/10514))
* Fix containing elements getting focused on SSR markup mismatch. ([@koba04](https://github.com/koba04) in [#11737](https://github.com/facebook/react/pull/11737))
* Fix `value` and `defaultValue` to ignore Symbol values. ([@nhunzaker](https://github.com/nhunzaker) in [#11741](https://github.com/facebook/react/pull/11741))
* Fix refs to class components not getting cleaned up when the attribute is removed. ([@bvaughn](https://github.com/bvaughn) in [#12178](https://github.com/facebook/react/pull/12178))
* Fix an IE/Edge issue when rendering inputs into a different window. ([@M-ZubairAhmed](https://github.com/M-ZubairAhmed) in [#11870](https://github.com/facebook/react/pull/11870))
* Throw with a meaningful message if the component runs after jsdom has been destroyed. ([@gaearon](https://github.com/gaearon) in [#11677](https://github.com/facebook/react/pull/11677))
* Don't crash if there is a global variable called `opera` with a `null` value. [@alisherdavronov](https://github.com/alisherdavronov) in [#11854](https://github.com/facebook/react/pull/11854))
* Don't check for old versions of Opera. ([@skiritsis](https://github.com/skiritsis) in [#11921](https://github.com/facebook/react/pull/11921))
* Deduplicate warning messages about `<option selected>`. ([@watadarkstar](https://github.com/watadarkstar) in [#11821](https://github.com/facebook/react/pull/11821))
* Deduplicate warning messages about invalid callback. ([@yenshih](https://github.com/yenshih) in [#11833](https://github.com/facebook/react/pull/11833))
* Deprecate `ReactDOM.unstable_createPortal()` in favor of `ReactDOM.createPortal()`. ([@prometheansacrifice](https://github.com/prometheansacrifice) in [#11747](https://github.com/facebook/react/pull/11747))
* Don't emit User Timing entries for context types. ([@abhaynikam](https://github.com/abhaynikam) in [#12250](https://github.com/facebook/react/pull/12250))
* Improve the error message when context consumer child isn't a function. ([@raunofreiberg](https://github.com/raunofreiberg) in [#12267](https://github.com/facebook/react/pull/12267))
* Improve the error message when adding a ref to a functional component. ([@skiritsis](https://github.com/skiritsis) in [#11782](https://github.com/facebook/react/pull/11782))

### React DOM Server

* Prevent an infinite loop when attempting to render portals with SSR. ([@gaearon](https://github.com/gaearon) in [#11709](https://github.com/facebook/react/pull/11709))
* Warn if a class doesn't extend `React.Component`. ([@wyze](https://github.com/wyze) in [#11993](https://github.com/facebook/react/pull/11993))
* Fix an issue with `this.state` of different components getting mixed up. ([@sophiebits](https://github.com/sophiebits) in [#12323](https://github.com/facebook/react/pull/12323))
* Provide a better message when component type is undefined. ([@HeroProtagonist](https://github.com/HeroProtagonist) in [#11966](https://github.com/facebook/react/pull/11966))

## React Test Renderer

* Fix handling of fragments in `toTree()`. ([@maciej-ka](https://github.com/maciej-ka) in [#12107](https://github.com/facebook/react/pull/12107) and [@gaearon](https://github.com/gaearon) in [#12154](https://github.com/facebook/react/pull/12154))
* Shallow renderer should assign state to `null` for components that don't set it. ([@jwbay](https://github.com/jwbay) in [#11965](https://github.com/facebook/react/pull/11965))
* Shallow renderer should filter legacy context according to `contextTypes`. ([@koba04](https://github.com/koba04) in [#11922](https://github.com/facebook/react/pull/11922))
* Add an unstable API for testing asynchronous rendering. ([@acdlite](https://github.com/acdlite) in [#12478](https://github.com/facebook/react/pull/12478))

### React Is (New)

* First release of the [new package](https://github.com/facebook/react/tree/master/packages/react-is) that libraries can use to detect different React node types. ([@bvaughn](https://github.com/bvaughn) in [#12199](https://github.com/facebook/react/pull/12199))
* Add `ReactIs.isValidElementType()` to help higher-order components validate their inputs. ([@jamesreggio](https://github.com/jamesreggio) in [#12483](https://github.com/facebook/react/pull/12483))

### React Lifecycles Compat (New)

* First release of the [new package](https://github.com/reactjs/react-lifecycles-compat) to help library developers target multiple versions of React. ([@bvaughn](https://github.com/bvaughn) in [#12105](https://github.com/facebook/react/pull/12105))

### Create Subscription (New)

* First release of the [new package](https://github.com/facebook/react/tree/master/packages/create-subscription) to subscribe to external data sources safely for async rendering. ([@bvaughn](https://github.com/bvaughn) in [#12325](https://github.com/facebook/react/pull/12325))

### React Reconciler (Experimental)

* Expose `react-reconciler/persistent` for building renderers that use persistent data structures. ([@gaearon](https://github.com/gaearon) in [#12156](https://github.com/facebook/react/pull/12156))
* Pass host context to `finalizeInitialChildren()`. ([@jquense](https://github.com/jquense) in [#11970](https://github.com/facebook/react/pull/11970))
* Remove `useSyncScheduling` from the host config. ([@acdlite](https://github.com/acdlite) in [#11771](https://github.com/facebook/react/pull/11771))

### React Call Return (Experimental)

* Fix a crash on updates. ([@rmhartog](https://github.com/rmhartog) in [#11955](https://github.com/facebook/react/pull/11955))

## 16.2.1 (August 1, 2018)

### React DOM Server

* Fix a [potential XSS vulnerability when the attacker controls an attribute name](https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html) (`CVE-2018-6341`). This fix is available in the latest `react-dom@16.4.2`, as well as in previous affected minor versions: `react-dom@16.0.1`, `react-dom@16.1.2`, `react-dom@16.2.1`, and `react-dom@16.3.3`. ([@gaearon](https://github.com/gaearon) in [#13302](https://github.com/facebook/react/pull/13302))

## 16.2.0 (November 28, 2017)

### React

* Add `Fragment` as named export to React. ([@clemmy](https://github.com/clemmy) in [#10783](https://github.com/facebook/react/pull/10783))
* Support experimental Call/Return types in `React.Children` utilities. ([@MatteoVH](https://github.com/MatteoVH) in [#11422](https://github.com/facebook/react/pull/11422))

### React DOM

* Fix radio buttons not getting checked when using multiple lists of radios. ([@landvibe](https://github.com/landvibe) in [#11227](https://github.com/facebook/react/pull/11227))
* Fix radio buttons not receiving the `onChange` event in some cases. ([@jquense](https://github.com/jquense) in [#11028](https://github.com/facebook/react/pull/11028))

### React Test Renderer

* Fix `setState()` callback firing too early when called from `componentWillMount`. ([@accordeiro](https://github.com/accordeiro) in [#11507](https://github.com/facebook/react/pull/11507))

### React Reconciler

* Expose `react-reconciler/reflection` with utilities useful to custom renderers. ([@rivenhk](https://github.com/rivenhk) in [#11683](https://github.com/facebook/react/pull/11683))

### Internal Changes

* Many tests were rewritten against the public API. Big thanks to [everyone who contributed](https://github.com/facebook/react/issues/11299)!

## 16.1.2 (August 1, 2018)

### React DOM Server

* Fix a [potential XSS vulnerability when the attacker controls an attribute name](https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html) (`CVE-2018-6341`). This fix is available in the latest `react-dom@16.4.2`, as well as in previous affected minor versions: `react-dom@16.0.1`, `react-dom@16.1.2`, `react-dom@16.2.1`, and `react-dom@16.3.3`. ([@gaearon](https://github.com/gaearon) in [#13302](https://github.com/facebook/react/pull/13302))

## 16.1.1 (November 13, 2017)

### React

* Improve the warning about undefined component type. ([@selbekk](https://github.com/selbekk) in [#11505](https://github.com/facebook/react/pull/11505))

### React DOM

* Support string values for the `capture` attribute. ([@maxschmeling](https://github.com/maxschmeling) in [#11424](https://github.com/facebook/react/pull/11424))

### React DOM Server

* Don't freeze the `ReactDOMServer` public API. ([@travi](https://github.com/travi) in [#11531](https://github.com/facebook/react/pull/11531))
* Don't emit `autoFocus={false}` attribute on the server. ([@gaearon](https://github.com/gaearon) in [#11543](https://github.com/facebook/react/pull/11543))

### React Reconciler

* Change the hydration API for better Flow typing. ([@sebmarkbage](https://github.com/sebmarkbage) in [#11493](https://github.com/facebook/react/pull/11493))

## 16.1.0 (November 9, 2017)

### Discontinuing Bower Releases

Starting with 16.1.0, we will no longer be publishing new releases on Bower. You can continue using Bower for old releases, or point your Bower configs to the [React UMD builds hosted on unpkg](https://reactjs.org/docs/installation.html#using-a-cdn) that mirror npm releases and will continue to be updated.

### All Packages

* Fix an accidental extra global variable in the UMD builds. ([@gaearon](https://github.com/gaearon) in [#10935](https://github.com/facebook/react/pull/10935))

### React

* Add support for portals in `React.Children` utilities. ([@MatteoVH](https://github.com/MatteoVH) in [#11378](https://github.com/facebook/react/pull/11378))
* Warn when a class has a `render` method but doesn't extend a known base class. ([@sw-yx](https://github.com/sw-yx) in [#11168](https://github.com/facebook/react/pull/11168))
* Improve the warning when accidentally returning an object from constructor. ([@deanbrophy](https://github.com/deanbrophy) in [#11395](https://github.com/facebook/react/pull/11395))

### React DOM

* Allow `on` as a custom attribute for AMP. ([@nuc](https://github.com/nuc) in [#11153](https://github.com/facebook/react/pull/11153))
* Fix `onMouseEnter` and `onMouseLeave` firing on wrong elements. ([@gaearon](https://github.com/gaearon) in [#11164](https://github.com/facebook/react/pull/11164))
* Fix `null` showing up in a warning instead of the component stack. ([@gaearon](https://github.com/gaearon) in [#10915](https://github.com/facebook/react/pull/10915))
* Fix IE11 crash in development mode. ([@leidegre](https://github.com/leidegre) in [#10921](https://github.com/facebook/react/pull/10921))
* Fix `tabIndex` not getting applied to SVG elements. ([@gaearon](https://github.com/gaearon) in [#11034](https://github.com/facebook/react/pull/11034))
* Fix SVG children not getting cleaned up on `dangerouslySetInnerHTML` in IE. ([@OriR](https://github.com/OriR) in [#11108](https://github.com/facebook/react/pull/11108))
* Fix false positive text mismatch warning caused by newline normalization. ([@gaearon](https://github.com/gaearon) in [#11119](https://github.com/facebook/react/pull/11119))
* Fix `form.reset()` to respect `defaultValue` on uncontrolled `<select>`. ([@aweary](https://github.com/aweary) in [#11057](https://github.com/facebook/react/pull/11057))
* Fix `<textarea>` placeholder not rendering on IE11. ([@gaearon](https://github.com/gaearon) in [#11177](https://github.com/facebook/react/pull/11177))
* Fix a crash rendering into shadow root. ([@gaearon](https://github.com/gaearon) in [#11037](https://github.com/facebook/react/pull/11037))
* Fix false positive warning about hydrating mixed case SVG tags. ([@gaearon](https://github.com/gaearon) in [#11174](https://github.com/facebook/react/pull/11174))
* Suppress the new unknown tag warning for `<dialog>` element. ([@gaearon](https://github.com/gaearon) in [#11035](https://github.com/facebook/react/pull/11035))
* Warn when defining a non-existent `componentDidReceiveProps` method. ([@iamtommcc](https://github.com/iamtommcc) in [#11479](https://github.com/facebook/react/pull/11479))
* Warn about function child no more than once. ([@andreysaleba](https://github.com/andreysaleba) in [#11120](https://github.com/facebook/react/pull/11120))
* Warn about nested updates no more than once. ([@anushreesubramani](https://github.com/anushreesubramani) in [#11113](https://github.com/facebook/react/pull/11113))
* Deduplicate other warnings about updates. ([@anushreesubramani](https://github.com/anushreesubramani) in [#11216](https://github.com/facebook/react/pull/11216))
* Include component stack into the warning about `contentEditable` and `children`. ([@Ethan-Arrowood](https://github.com/Ethan-Arrowood) in [#11208](https://github.com/facebook/react/pull/11208))
* Improve the warning about booleans passed to event handlers. ([@NicBonetto](https://github.com/NicBonetto) in [#11308](https://github.com/facebook/react/pull/11308))
* Improve the warning when a multiple `select` gets null `value`. ([@Hendeca](https://github.com/Hendeca) in [#11141](https://github.com/facebook/react/pull/11141))
* Move link in the warning message to avoid redirect. ([@marciovicente](https://github.com/marciovicente) in [#11400](https://github.com/facebook/react/pull/11400))
* Add a way to suppress the React DevTools installation prompt. ([@gaearon](https://github.com/gaearon) in [#11448](https://github.com/facebook/react/pull/11448))
* Remove unused code. ([@gaearon](https://github.com/gaearon) in [#10802](https://github.com/facebook/react/pull/10802), [#10803](https://github.com/facebook/react/pull/10803))

### React DOM Server

* Add a new `suppressHydrationWarning` attribute for intentional client/server text mismatches. ([@sebmarkbage](https://github.com/sebmarkbage) in [#11126](https://github.com/facebook/react/pull/11126))
* Fix markup generation when components return strings. ([@gaearon](https://github.com/gaearon) in [#11109](https://github.com/facebook/react/pull/11109))
* Fix obscure error message when passing an invalid style value. ([@iamdustan](https://github.com/iamdustan) in [#11173](https://github.com/facebook/react/pull/11173))
* Include the `autoFocus` attribute into SSR markup. ([@gaearon](https://github.com/gaearon) in [#11192](https://github.com/facebook/react/pull/11192))
* Include the component stack into more warnings. ([@gaearon](https://github.com/gaearon) in [#11284](https://github.com/facebook/react/pull/11284))

### React Test Renderer and Test Utils

* Fix multiple `setState()` calls in `componentWillMount()` in shallow renderer. ([@Hypnosphi](https://github.com/Hypnosphi) in [#11167](https://github.com/facebook/react/pull/11167))
* Fix shallow renderer to ignore `shouldComponentUpdate()` after `forceUpdate()`. ([@d4rky-pl](https://github.com/d4rky-pl) in [#11239](https://github.com/facebook/react/pull/11239) and [#11439](https://github.com/facebook/react/pull/11439))
* Handle `forceUpdate()` and `React.PureComponent` correctly. ([@koba04](https://github.com/koba04) in [#11440](https://github.com/facebook/react/pull/11440))
* Add back support for running in production mode. ([@gaearon](https://github.com/gaearon) in [#11112](https://github.com/facebook/react/pull/11112))
* Add a missing `package.json` dependency. ([@gaearon](https://github.com/gaearon) in [#11340](https://github.com/facebook/react/pull/11340))

### React ART

* Add a missing `package.json` dependency. ([@gaearon](https://github.com/gaearon) in [#11341](https://github.com/facebook/react/pull/11341))
* Expose `react-art/Circle`, `react-art/Rectangle`, and `react-art/Wedge`. ([@gaearon](https://github.com/gaearon) in [#11343](https://github.com/facebook/react/pull/11343))

### React Reconciler (Experimental)

* First release of the [new experimental package](https://github.com/facebook/react/blob/master/packages/react-reconciler/README.md) for creating custom renderers. ([@iamdustan](https://github.com/iamdustan) in [#10758](https://github.com/facebook/react/pull/10758))
* Add support for React DevTools. ([@gaearon](https://github.com/gaearon) in [#11463](https://github.com/facebook/react/pull/11463))

### React Call Return (Experimental)

* First release of the [new experimental package](https://github.com/facebook/react/tree/master/packages/react-call-return) for parent-child communication. ([@gaearon](https://github.com/gaearon) in [#11364](https://github.com/facebook/react/pull/11364))

## 16.0.1 (August 1, 2018)

### React DOM Server

* Fix a [potential XSS vulnerability when the attacker controls an attribute name](https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html) (`CVE-2018-6341`). This fix is available in the latest `react-dom@16.4.2`, as well as in previous affected minor versions: `react-dom@16.0.1`, `react-dom@16.1.2`, `react-dom@16.2.1`, and `react-dom@16.3.3`. ([@gaearon](https://github.com/gaearon) in [#13302](https://github.com/facebook/react/pull/13302))

## 16.0.0 (September 26, 2017)

### New JS Environment Requirements

 * React 16 depends on the collection types [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) and [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set), as well as [requestAnimationFrame](https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame). If you support older browsers and devices which may not yet provide these natively (e.g. <IE11), [you may want to include a polyfill](https://gist.github.com/gaearon/9a4d54653ae9c50af6c54b4e0e56b583).

### New Features
* Components can now return arrays and strings from `render`. (Docs coming soon!)
* Improved error handling with introduction of "error boundaries". [Error boundaries](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html) are React components that catch JavaScript errors anywhere in their child component tree, log those errors, and display a fallback UI instead of the component tree that crashed.
* First-class support for declaratively rendering a subtree into another DOM node with `ReactDOM.createPortal()`. (Docs coming soon!)
* Streaming mode for server side rendering is enabled with `ReactDOMServer.renderToNodeStream()` and `ReactDOMServer.renderToStaticNodeStream()`. ([@aickin](https://github.com/aickin) in [#10425](https://github.com/facebook/react/pull/10425), [#10044](https://github.com/facebook/react/pull/10044), [#10039](https://github.com/facebook/react/pull/10039), [#10024](https://github.com/facebook/react/pull/10024), [#9264](https://github.com/facebook/react/pull/9264), and others.)
* [React DOM now allows passing non-standard attributes](https://reactjs.org/blog/2017/09/08/dom-attributes-in-react-16.html). ([@nhunzaker](https://github.com/nhunzaker) in [#10385](https://github.com/facebook/react/pull/10385), [10564](https://github.com/facebook/react/pull/10564), [#10495](https://github.com/facebook/react/pull/10495) and others)

### Breaking Changes
- There are several changes to the behavior of scheduling and lifecycle methods:
  * `ReactDOM.render()` and `ReactDOM.unstable_renderIntoContainer()` now return `null` if called from inside a lifecycle method.
    * To work around this, you can either use [the new portal API](https://github.com/facebook/react/issues/10309#issuecomment-318433235) or [refs](https://github.com/facebook/react/issues/10309#issuecomment-318434635).
  * Minor changes to `setState` behavior:
    * Calling `setState` with null no longer triggers an update. This allows you to decide in an updater function if you want to re-render.
    * Calling `setState` directly in render always causes an update. This was not previously the case. Regardless, you should not be calling `setState` from render.
    * `setState` callback (second argument) now fires immediately after `componentDidMount` / `componentDidUpdate` instead of after all components have rendered.
  * When replacing `<A />` with `<B />`,  `B.componentWillMount` now always happens before  `A.componentWillUnmount`. Previously, `A.componentWillUnmount` could fire first in some cases.
  * Previously, changing the `ref` to a component would always detach the ref before that component's render is called. Now, we change the `ref` later, when applying the changes to the DOM.
  * It is not safe to re-render into a container that was modified by something other than React. This worked previously in some cases but was never supported. We now emit a warning in this case. Instead you should clean up your component trees using `ReactDOM.unmountComponentAtNode`. [See this example.](https://github.com/facebook/react/issues/10294#issuecomment-318820987)
  * `componentDidUpdate` lifecycle no longer receives `prevContext` param. ([@bvaughn](https://github.com/bvaughn) in [#8631](https://github.com/facebook/react/pull/8631))
  * Non-unique keys may now cause children to be duplicated and/or omitted. Using non-unique keys is not (and has never been) supported, but previously it was a hard error.
  * Shallow renderer no longer calls `componentDidUpdate()` because DOM refs are not available. This also makes it consistent with `componentDidMount()` (which does not get called in previous versions either).
  * Shallow renderer does not implement `unstable_batchedUpdates()` anymore.
  * `ReactDOM.unstable_batchedUpdates` now only takes one extra argument after the callback.
- The names and paths to the single-file browser builds have changed to emphasize the difference between development and production builds. For example:
  - `react/dist/react.js` → `react/umd/react.development.js`
  - `react/dist/react.min.js` → `react/umd/react.production.min.js`
  - `react-dom/dist/react-dom.js` → `react-dom/umd/react-dom.development.js`
  - `react-dom/dist/react-dom.min.js` → `react-dom/umd/react-dom.production.min.js`
* The server renderer has been completely rewritten, with some improvements:
  * Server rendering does not use markup validation anymore, and instead tries its best to attach to existing DOM, warning about inconsistencies. It also doesn't use comments for empty components and data-reactid attributes on each node anymore.
  * Hydrating a server rendered container now has an explicit API. Use `ReactDOM.hydrate` instead of `ReactDOM.render` if you're reviving server rendered HTML. Keep using `ReactDOM.render` if you're just doing client-side rendering.
* When "unknown" props are passed to DOM components, for valid values, React will now render them in the DOM. [See this post for more details.](https://reactjs.org/blog/2017/09/08/dom-attributes-in-react-16.html) ([@nhunzaker](https://github.com/nhunzaker) in [#10385](https://github.com/facebook/react/pull/10385), [10564](https://github.com/facebook/react/pull/10564), [#10495](https://github.com/facebook/react/pull/10495) and others)
* Errors in the render and lifecycle methods now unmount the component tree by default. To prevent this, add [error boundaries](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html) to the appropriate places in the UI.

### Removed Deprecations

- There is no `react-with-addons.js` build anymore. All compatible addons are published separately on npm, and have single-file browser versions if you need them.
- The deprecations introduced in 15.x have been removed from the core package. `React.createClass` is now available as create-react-class, `React.PropTypes` as prop-types, `React.DOM` as react-dom-factories, react-addons-test-utils as react-dom/test-utils, and shallow renderer as react-test-renderer/shallow. See [15.5.0](https://reactjs.org/blog/2017/04/07/react-v15.5.0.html) and [15.6.0](https://reactjs.org/blog/2017/06/13/react-v15.6.0.html) blog posts for instructions on migrating code and automated codemods.

## 15.6.2 (September 25, 2017)

### All Packages
* Switch from BSD + Patents to MIT license

### React DOM

* Fix a bug where modifying `document.documentMode` would trigger IE detection in other browsers, breaking change events. ([@aweary](https://github.com/aweary) in [#10032](https://github.com/facebook/react/pull/10032))
* CSS Columns are treated as unitless numbers. ([@aweary](https://github.com/aweary) in [#10115](https://github.com/facebook/react/pull/10115))
* Fix bug in QtWebKit when wrapping synthetic events in proxies. ([@walrusfruitcake](https://github.com/walrusfruitcake) in [#10115](https://github.com/facebook/react/pull/10011))
* Prevent event handlers from receiving extra argument in development. ([@aweary](https://github.com/aweary) in [#10115](https://github.com/facebook/react/pull/8363))
* Fix cases where `onChange` would not fire with `defaultChecked` on radio inputs. ([@jquense](https://github.com/jquense) in [#10156](https://github.com/facebook/react/pull/10156))
* Add support for `controlList` attribute to DOM property whitelist ([@nhunzaker](https://github.com/nhunzaker) in [#9940](https://github.com/facebook/react/pull/9940))
* Fix a bug where creating an element with a ref in a constructor did not throw an error in development. ([@iansu](https://github.com/iansu) in [#10025](https://github.com/facebook/react/pull/10025))

## 15.6.1 (June 14, 2017)

### React DOM

* Fix a crash on iOS Safari. ([@jquense](https://github.com/jquense) in [#9960](https://github.com/facebook/react/pull/9960))
* Don't add `px` to custom CSS property values. ([@TrySound](https://github.com/TrySound) in [#9966](https://github.com/facebook/react/pull/9966))

## 15.6.0 (June 13, 2017)

### React

* Downgrade deprecation warnings to use `console.warn` instead of `console.error`. ([@flarnie](https://github.com/flarnie) in [#9753](https://github.com/facebook/react/pull/9753))
* Add a deprecation warning for `React.createClass`. Points users to `create-react-class` instead. ([@flarnie](https://github.com/flarnie) in [#9771](https://github.com/facebook/react/pull/9771))
* Add deprecation warnings and separate module for `React.DOM` factory helpers. ([@nhunzaker](https://github.com/nhunzaker) in [#8356](https://github.com/facebook/react/pull/8356))
* Warn for deprecation of `React.createMixin` helper, which was never used. ([@aweary](https://github.com/aweary) in [#8853](https://github.com/facebook/react/pull/8853))

### React DOM

* Add support for CSS variables in `style` attribute. ([@aweary](https://github.com/aweary) in [#9302](https://github.com/facebook/react/pull/9302))
* Add support for CSS Grid style properties. ([@ericsakmar](https://github.com/ericsakmar) in [#9185](https://github.com/facebook/react/pull/9185))
* Fix bug where inputs mutated value on type conversion. ([@nhunzaker](https://github.com/mhunzaker) in [#9806](https://github.com/facebook/react/pull/9806))
* Fix issues with `onChange` not firing properly for some inputs. ([@jquense](https://github.com/jquense) in [#8575](https://github.com/facebook/react/pull/8575))
* Fix bug where controlled number input mistakenly allowed period. ([@nhunzaker](https://github.com/nhunzaker) in [#9584](https://github.com/facebook/react/pull/9584))
* Fix bug where performance entries were being cleared. ([@chrisui](https://github.com/chrisui) in [#9451](https://github.com/facebook/react/pull/9451))

### React Addons

* Fix AMD support for addons depending on `react`. ([@flarnie](https://github.com/flarnie) in [#9919](https://github.com/facebook/react/issues/9919))
* Fix `isMounted()` to return `true` in `componentWillUnmount`. ([@mridgway](https://github.com/mridgway) in [#9638](https://github.com/facebook/react/issues/9638))
* Fix `react-addons-update` to not depend on native `Object.assign`. ([@gaearon](https://github.com/gaearon) in [#9937](https://github.com/facebook/react/pull/9937))
* Remove broken Google Closure Compiler annotation from `create-react-class`. ([@gaearon](https://github.com/gaearon) in [#9933](https://github.com/facebook/react/pull/9933))
* Remove unnecessary dependency from `react-linked-input`. ([@gaearon](https://github.com/gaearon) in [#9766](https://github.com/facebook/react/pull/9766))
* Point `react-addons-(css-)transition-group` to the new package. ([@gaearon](https://github.com/gaearon) in [#9937](https://github.com/facebook/react/pull/9937))

## 15.5.4 (April 11, 2017)

### React Addons
* **Critical Bugfix:** Update the version of `prop-types` to fix critical bug.  ([@gaearon](https://github.com/gaearon) in [545c87f](https://github.com/facebook/react/commit/545c87fdc348f82eb0c3830bef715ed180785390))
* Fix `react-addons-create-fragment` package to include `loose-envify` transform for Browserify users. ([@mridgway](https://github.com/mridgway) in [#9642](https://github.com/facebook/react/pull/9642))

### React Test Renderer
* Fix compatibility with Enzyme by exposing `batchedUpdates` on shallow renderer. ([@gaearon](https://github.com/gaearon) in [9382](https://github.com/facebook/react/commit/69933e25c37cf5453a9ef132177241203ee8d2fd))

## 15.5.3 (April 7, 2017)

**Note: this release has a critical issue and was deprecated. Please update to 15.5.4 or higher.**

### React Addons
* Fix `react-addons-create-fragment` package to export correct thing. ([@gaearon](https://github.com/gaearon) in [#9385](https://github.com/facebook/react/pull/9383))
* Fix `create-react-class` package to include `loose-envify` transform for Browserify users. ([@mridgway](https://github.com/mridgway) in [#9642](https://github.com/facebook/react/pull/9642))

## 15.5.2 (April 7, 2017)

**Note: this release has a critical issue and was deprecated. Please update to 15.5.4 or higher.**

### React Addons
* Fix the production single-file builds to not include the development code. ([@gaearon](https://github.com/gaearon) in [#9385](https://github.com/facebook/react/pull/9383))
* Apply better minification to production single-file builds. ([@gaearon](https://github.com/gaearon) in [#9385](https://github.com/facebook/react/pull/9383))
* Add missing and remove unnecessary dependencies to packages. ([@gaearon](https://github.com/gaearon) in [#9385](https://github.com/facebook/react/pull/9383))

## 15.5.1 (April 7, 2017)

**Note: this release has a critical issue and was deprecated. Please update to 15.5.4 or higher.**

### React
* Fix erroneous PropTypes access warning. ([@acdlite](https://github.com/acdlite) in ([ec97ebb](https://github.com/facebook/react/commit/ec97ebbe7f15b58ae2f1323df39d06f119873344))

## 15.5.0 (April 7, 2017)

**Note: this release has a critical issue and was deprecated. Please update to 15.5.4 or higher.**

### React
* <s>Added a deprecation warning for `React.createClass`. Points users to create-react-class instead. ([@acdlite](https://github.com/acdlite) in [#d9a4fa4](https://github.com/facebook/react/commit/d9a4fa4f51c6da895e1655f32255cf72c0fe620e))</s>
* Added a deprecation warning for `React.PropTypes`. Points users to prop-types instead. ([@acdlite](https://github.com/acdlite) in [#043845c](https://github.com/facebook/react/commit/043845ce75ea0812286bbbd9d34994bb7e01eb28))
* Fixed an issue when using `ReactDOM` together with `ReactDOMServer`. ([@wacii](https://github.com/wacii) in [#9005](https://github.com/facebook/react/pull/9005))
* Fixed issue with Closure Compiler. ([@anmonteiro](https://github.com/anmonteiro) in [#8895](https://github.com/facebook/react/pull/8895))
* Another fix for Closure Compiler. ([@Shastel](https://github.com/Shastel) in [#8882](https://github.com/facebook/react/pull/8882))
* Added component stack info to invalid element type warning. ([@n3tr](https://github.com/n3tr) in [#8495](https://github.com/facebook/react/pull/8495))

### React DOM
* Fixed Chrome bug when backspacing in number inputs. ([@nhunzaker](https://github.com/nhunzaker) in [#7359](https://github.com/facebook/react/pull/7359))
* Added `react-dom/test-utils`, which exports the React Test Utils. ([@bvaughn](https://github.com/bvaughn))

### React Test Renderer
* Fixed bug where `componentWillUnmount` was not called for children. ([@gre](https://github.com/gre) in [#8512](https://github.com/facebook/react/pull/8512))
* Added `react-test-renderer/shallow`, which exports the shallow renderer. ([@bvaughn](https://github.com/bvaughn))

### React Addons
* Last release for addons; they will no longer be actively maintained.
* Removed `peerDependencies` so that addons continue to work indefinitely. ([@acdlite](https://github.com/acdlite) and [@bvaughn](https://github.com/bvaughn) in [8a06cd7](https://github.com/facebook/react/commit/8a06cd7a786822fce229197cac8125a551e8abfa) and [67a8db3](https://github.com/facebook/react/commit/67a8db3650d724a51e70be130e9008806402678a))
* Updated to remove references to `React.createClass` and `React.PropTypes` ([@acdlite](https://github.com/acdlite) in [12a96b9](https://github.com/facebook/react/commit/12a96b94823d6b6de6b1ac13bd576864abd50175))
* `react-addons-test-utils` is deprecated. Use `react-dom/test-utils` and `react-test-renderer/shallow` instead. ([@bvaughn](https://github.com/bvaughn))

## 15.4.2 (January 6, 2017)

### React
* Fixed build issues with the Brunch bundler. ([@gaearon](https://github.com/gaearon) in [#8686](https://github.com/facebook/react/pull/8686))
* Improved error messages for invalid element types. ([@sophiebits](https://github.com/sophiebits) in [#8612](https://github.com/facebook/react/pull/8612))
* Removed a warning about `getInitialState` when `this.state` is set. ([@bvaughn](https://github.com/bvaughn) in [#8594](https://github.com/facebook/react/pull/8594))
* Removed some dead code. ([@diegomura](https://github.com/diegomura) in [#8050](https://github.com/facebook/react/pull/8050), [@dfrownfelter](https://github.com/dfrownfelter) in [#8597](https://github.com/facebook/react/pull/8597))

### React DOM
* Fixed a decimal point issue on uncontrolled number inputs. ([@nhunzaker](https://github.com/nhunzaker) in [#7750](https://github.com/facebook/react/pull/7750))
* Fixed rendering of textarea placeholder in IE11. ([@aweary](https://github.com/aweary) in [#8020](https://github.com/facebook/react/pull/8020))
* Worked around a script engine bug in IE9. ([@eoin](https://github.com/eoin) in [#8018](https://github.com/facebook/react/pull/8018))

### React Addons
* Fixed build issues in RequireJS and SystemJS environments. ([@gaearon](https://github.com/gaearon) in [#8686](https://github.com/facebook/react/pull/8686))
* Added missing package dependencies. ([@kweiberth](https://github.com/kweiberth) in [#8467](https://github.com/facebook/react/pull/8467))

## 15.4.1 (November 22, 2016)

### React
* Restructure variable assignment to work around a Rollup bug ([@gaearon](https://github.com/gaearon) in [#8384](https://github.com/facebook/react/pull/8384))

### React DOM
* Fixed event handling on disabled button elements ([@sophiebits](https://github.com/sophiebits) in [#8387](https://github.com/facebook/react/pull/8387))
* Fixed compatibility of browser build with AMD environments ([@zpao](https://github.com/zpao) in [#8374](https://github.com/facebook/react/pull/8374))

## 15.4.0 (November 16, 2016)

### React
* React package and browser build no longer "secretly" includes React DOM. ([@sebmarkbage](https://github.com/sebmarkbage) in [#7164](https://github.com/facebook/react/pull/7164) and [#7168](https://github.com/facebook/react/pull/7168))
* Required PropTypes now fail with specific messages for null and undefined. ([@chenglou](https://github.com/chenglou) in [#7291](https://github.com/facebook/react/pull/7291))
* Improved development performance by freezing children instead of copying. ([@keyanzhang](https://github.com/keyanzhang) in [#7455](https://github.com/facebook/react/pull/7455))

### React DOM
* Fixed occasional test failures when React DOM is used together with shallow renderer. ([@goatslacker](https://github.com/goatslacker) in [#8097](https://github.com/facebook/react/pull/8097))
* Added a warning for invalid `aria-` attributes. ([@jessebeach](https://github.com/jessebeach) in [#7744](https://github.com/facebook/react/pull/7744))
* Added a warning for using `autofocus` rather than `autoFocus`. ([@hkal](https://github.com/hkal) in [#7694](https://github.com/facebook/react/pull/7694))
* Removed an unnecessary warning about polyfilling `String.prototype.split`. ([@nhunzaker](https://github.com/nhunzaker) in [#7629](https://github.com/facebook/react/pull/7629))
* Clarified the warning about not calling PropTypes manually. ([@jedwards1211](https://github.com/jedwards1211) in [#7777](https://github.com/facebook/react/pull/7777))
* The unstable `batchedUpdates` API now passes the wrapped function's return value through. ([@bgnorlov](https://github.com/bgnorlov) in [#7444](https://github.com/facebook/react/pull/7444))
* Fixed a bug with updating text in IE 8. ([@mnpenner](https://github.com/mnpenner) in [#7832](https://github.com/facebook/react/pull/7832))

### React Perf
* When ReactPerf is started, you can now view the relative time spent in components as a chart in Chrome Timeline. ([@gaearon](https://github.com/gaearon) in [#7549](https://github.com/facebook/react/pull/7549))

### React Test Utils
* If you call `Simulate.click()` on a `<input disabled onClick={foo} />` then `foo` will get called whereas it didn't before. ([@nhunzaker](https://github.com/nhunzaker) in [#7642](https://github.com/facebook/react/pull/7642))

### React Test Renderer
* Due to packaging changes, it no longer crashes when imported together with React DOM in the same file. ([@sebmarkbage](https://github.com/sebmarkbage) in [#7164](https://github.com/facebook/react/pull/7164) and [#7168](https://github.com/facebook/react/pull/7168))
* `ReactTestRenderer.create()` now accepts `{createNodeMock: element => mock}` as an optional argument so you can mock refs with snapshot testing. ([@Aweary](https://github.com/Aweary) in [#7649](https://github.com/facebook/react/pull/7649), [#8261](https://github.com/facebook/react/pull/8261))


## 15.3.2 (September 19, 2016)

### React
- Remove plain object warning from React.createElement & React.cloneElement. ([@spudly](https://github.com/spudly) in [#7724](https://github.com/facebook/react/pull/7724))

### React DOM
- Add `playsInline` to supported HTML attributes. ([@reaperhulk](https://github.com/reaperhulk) in [#7519](https://github.com/facebook/react/pull/7519))
- Add `as` to supported HTML attributes. ([@kevinslin](https://github.com/kevinslin) in [#7582](https://github.com/facebook/react/pull/7582))
- Improve DOM nesting validation warning about whitespace. ([@sophiebits](https://github.com/sophiebits) in [#7515](https://github.com/facebook/react/pull/7515))
- Avoid "Member not found" exception in IE10 when calling `preventDefault()` in Synthetic Events. ([@g-palmer](https://github.com/g-palmer) in [#7411](https://github.com/facebook/react/pull/7411))
- Fix memory leak in `onSelect` implementation. ([@AgtLucas](https://github.com/AgtLucas) in [#7533](https://github.com/facebook/react/pull/7533))
- Improve robustness of `document.documentMode` checks to handle Google Tag Manager. ([@SchleyB](https://github.com/SchleyB) in [#7594](https://github.com/facebook/react/pull/7594))
- Add more cases to controlled inputs warning. ([@marcin-mazurek](https://github.com/marcin-mazurek) in [#7544](https://github.com/facebook/react/pull/7544))
- Handle case of popup blockers overriding `document.createEvent`. ([@Andarist](https://github.com/Andarist) in [#7621](https://github.com/facebook/react/pull/7621))
- Fix issue with `dangerouslySetInnerHTML` and SVG in Internet Explorer. ([@zpao](https://github.com/zpao) in [#7618](https://github.com/facebook/react/pull/7618))
- Improve handling of Japanese IME on Internet Explorer. ([@msmania](https://github.com/msmania) in [#7107](https://github.com/facebook/react/pull/7107))

### React Test Renderer
- Support error boundaries. ([@millermedeiros](https://github.com/millermedeiros) in [#7558](https://github.com/facebook/react/pull/7558), [#7569](https://github.com/facebook/react/pull/7569), [#7619](https://github.com/facebook/react/pull/7619))
- Skip null ref warning. ([@Aweary](https://github.com/Aweary) in [#7658](https://github.com/facebook/react/pull/7658))

### React Perf Add-on
- Ensure lifecycle timers are stopped on errors. ([@gaearon](https://github.com/gaearon) in [#7548](https://github.com/facebook/react/pull/7548))


## 15.3.1 (August 19, 2016)

### React

- Improve performance of development builds in various ways. ([@gaearon](https://github.com/gaearon) in [#7461](https://github.com/facebook/react/pull/7461), [#7463](https://github.com/facebook/react/pull/7463), [#7483](https://github.com/facebook/react/pull/7483), [#7488](https://github.com/facebook/react/pull/7488), [#7491](https://github.com/facebook/react/pull/7491), [#7510](https://github.com/facebook/react/pull/7510))
- Cleanup internal hooks to improve performance of development builds. ([@gaearon](https://github.com/gaearon) in [#7464](https://github.com/facebook/react/pull/7464), [#7472](https://github.com/facebook/react/pull/7472), [#7481](https://github.com/facebook/react/pull/7481), [#7496](https://github.com/facebook/react/pull/7496))
- Upgrade fbjs to pick up another performance improvement from [@gaearon](https://github.com/gaearon) for development builds. ([@zpao](https://github.com/zpao) in [#7532](https://github.com/facebook/react/pull/7532))
- Improve startup time of React in Node. ([@zertosh](https://github.com/zertosh) in [#7493](https://github.com/facebook/react/pull/7493))
- Improve error message of `React.Children.only`. ([@sophiebits](https://github.com/sophiebits) in [#7514](https://github.com/facebook/react/pull/7514))

### React DOM
- Avoid `<input>` validation warning from browsers when changing `type`. ([@nhunzaker](https://github.com/nhunzaker) in [#7333](https://github.com/facebook/react/pull/7333))
- Avoid "Member not found" exception in IE10 when calling `stopPropagation()` in Synthetic Events. ([@nhunzaker](https://github.com/nhunzaker) in [#7343](https://github.com/facebook/react/pull/7343))
- Fix issue resulting in inability to update some `<input>` elements in mobile browsers. ([@keyanzhang](https://github.com/keyanzhang) in [#7397](https://github.com/facebook/react/pull/7397))
- Fix memory leak in server rendering. ([@keyanzhang](https://github.com/keyanzhang) in [#7410](https://github.com/facebook/react/pull/7410))
- Fix issue resulting in `<input type="range">` values not updating when changing `min` or `max`. ([@troydemonbreun](https://github.com/troydemonbreun) in [#7486](https://github.com/facebook/react/pull/7486))
- Add new warning for rare case of attempting to unmount a container owned by a different copy of React. ([@ventuno](https://github.com/ventuno) in [#7456](https://github.com/facebook/react/pull/7456))

### React Test Renderer
- Fix ReactTestInstance::toJSON() with empty top-level components. ([@Morhaus](https://github.com/Morhaus) in [#7523](https://github.com/facebook/react/pull/7523))

### React Native Renderer
- Change `trackedTouchCount` invariant into a console.error for better reliability. ([@yungsters](https://github.com/yungsters) in [#7400](https://github.com/facebook/react/pull/7400))


## 15.3.0 (July 29, 2016)

### React
- Add `React.PureComponent` - a new base class to extend, replacing `react-addons-pure-render-mixin` now that mixins don't work with ES2015 classes. ([@sophiebits](https://github.com/sophiebits) in [#7195](https://github.com/facebook/react/pull/7195))
- Add new warning when modifying `this.props.children`. ([@jimfb](https://github.com/jimfb) in [#7001](https://github.com/facebook/react/pull/7001))
- Fixed issue with ref resolution order. ([@gaearon](https://github.com/gaearon) in [#7101](https://github.com/facebook/react/pull/7101))
- Warn when mixin is undefined. ([@swaroopsm](https://github.com/swaroopsm) in [#6158](https://github.com/facebook/react/pull/6158))
- Downgrade "unexpected batch number" invariant to a warning. ([@sophiebits](https://github.com/sophiebits) in [#7133](https://github.com/facebook/react/pull/7133))
- Validate arguments to `oneOf` and `oneOfType` PropTypes sooner. ([@troydemonbreun](https://github.com/troydemonbreun) in [#6316](https://github.com/facebook/react/pull/6316))
- Warn when calling PropTypes directly. ([@Aweary](https://github.com/Aweary) in [#7132](https://github.com/facebook/react/pull/7132), [#7194](https://github.com/facebook/react/pull/7194))
- Improve warning when using Maps as children. ([@keyanzhang](https://github.com/keyanzhang) in [#7260](https://github.com/facebook/react/pull/7260))
- Add additional type information to the `PropTypes.element` warning. ([@alexzherdev](https://github.com/alexzherdev) in [#7319](https://github.com/facebook/react/pull/7319))
- Improve component identification in no-op `setState` warning. ([@keyanzhang](https://github.com/keyanzhang) in [#7326](https://github.com/facebook/react/pull/7326))

### React DOM
- Fix issue with nested server rendering. ([@Aweary](https://github.com/Aweary) in [#7033](https://github.com/facebook/react/pull/7033))
- Add `xmlns`, `xmlnsXlink` to supported SVG attributes. ([@salzhrani](https://github.com/salzhrani) in [#6471](https://github.com/facebook/react/pull/6471))
- Add `referrerPolicy` to supported HTML attributes. ([@Aweary](https://github.com/Aweary) in [#7274](https://github.com/facebook/react/pull/7274))
- Fix issue resulting in `<input type="range">` initial value being rounded. ([@troydemonbreun](https://github.com/troydemonbreun) in [#7251](https://github.com/facebook/react/pull/7251))

### React Test Renderer
- Initial public release of package allowing more focused testing. Install with `npm install react-test-renderer`. ([@sophiebits](https://github.com/sophiebits) in [#6944](https://github.com/facebook/react/pull/6944), [#7258](https://github.com/facebook/react/pull/7258), [@iamdustan](https://github.com/iamdustan) in [#7362](https://github.com/facebook/react/pull/7362))

### React Perf Add-on
- Fix issue resulting in excessive warnings when encountering an internal measurement error. ([@sassanh](https://github.com/sassanh) in [#7299](https://github.com/facebook/react/pull/7299))

### React TestUtils Add-on
- Implement `type` property on for events created via `TestUtils.Simulate.*`. ([@yaycmyk](https://github.com/yaycmyk) in [#6154](https://github.com/facebook/react/pull/6154))
- Fix crash when running TestUtils with the production build of React. ([@gaearon](https://github.com/gaearon) in [#7246](https://github.com/facebook/react/pull/7246))


## 15.2.1 (July 8, 2016)

### React
- Fix errant warning about missing React element. ([@gaearon](https://github.com/gaearon) in [#7193](https://github.com/facebook/react/pull/7193))
- Better removal of dev-only code, leading to a small reduction in the minified production bundle size. ([@gaearon](https://github.com/gaearon) in [#7188](https://github.com/facebook/react/pull/7188), [#7189](https://github.com/facebook/react/pull/7189))

### React DOM
- Add stack trace to null input value warning. ([@jimfb](https://github.com/jimfb) in [#7040](https://github.com/facebook/react/pull/7040))
- Fix webcomponents example. ([@jalexanderfox](https://github.com/jalexanderfox) in [#7057](https://github.com/facebook/react/pull/7057))
- Fix `unstable_renderSubtreeIntoContainer` so that context properly updates when linked to state. ([@gaearon](https://github.com/gaearon) in [#7125](https://github.com/facebook/react/pull/7125))
- Improve invariant wording for void elements. ([@starkch](https://github.com/starkch) in [#7066](https://github.com/facebook/react/pull/7066))
- Ensure no errors are thrown due to event handlers in server rendering. ([@rricard](https://github.com/rricard) in [#7127](https://github.com/facebook/react/pull/7127))
- Fix regression resulting in `value`-less submit and reset inputs removing the browser-default text. ([@zpao](https://github.com/zpao) in [#7197](https://github.com/facebook/react/pull/7197))
- Fix regression resulting in empty `name` attribute being added to inputs when not provided. ([@okonet](https://github.com/okonet) in [#7199](https://github.com/facebook/react/pull/7199))
- Fix issue with nested server rendering. ([@Aweary](https://github.com/Aweary) in [#7033](https://github.com/facebook/react/pull/7033))

### React Perf Add-on
- Make `ReactPerf.start()` work properly during lifecycle methods. ([@gaearon](https://github.com/gaearon) in [#7208](https://github.com/facebook/react/pull/7208)).

### React CSSTransitionGroup Add-on
- Fix issue resulting in spurious unknown property warnings. ([@batusai513](https://github.com/batusai513) in [#7165](https://github.com/facebook/react/pull/7165))

### React Native Renderer
- Improve error handling in cross-platform touch event handling. ([@yungsters](https://github.com/yungsters) in [#7143](https://github.com/facebook/react/pull/7143))


## 15.2.0 (July 1, 2016)

### React
- Add error codes to production invariants, with links to the view the full error text. ([@keyanzhang](https://github.com/keyanzhang) in [#6948](https://github.com/facebook/react/pull/6948))
- Include component stack information in PropType validation warnings. ([@troydemonbreun](https://github.com/troydemonbreun) in [#6398](https://github.com/facebook/react/pull/6398), [@sophiebits](https://github.com/sophiebits) in [#6771](https://github.com/facebook/react/pull/6771))
- Include component stack information in key warnings. ([@keyanzhang](https://github.com/keyanzhang) in [#6799](https://github.com/facebook/react/pull/6799))
- Stop validating props at mount time, only validate at element creation. ([@keyanzhang](https://github.com/keyanzhang) in [#6824](https://github.com/facebook/react/pull/6824))
- New invariant providing actionable error in missing instance case. ([@yungsters](https://github.com/yungsters) in [#6990](https://github.com/facebook/react/pull/6990))
- Add `React.PropTypes.symbol` to support ES2015 Symbols as props. ([@puradox](https://github.com/puradox) in [#6377](https://github.com/facebook/react/pull/6377))
- Fix incorrect coercion of ref or key that are undefined in development ([@gaearon](https://github.com/gaearon) in [#6880](https://github.com/facebook/react/pull/6880))
- Fix a false positive when passing other element’s props to cloneElement ([@ericmatthys](https://github.com/ericmatthys) in [#6268](https://github.com/facebook/react/pull/6268))
- Warn if you attempt to define `childContextTypes` on a functional component ([@Aweary](https://github.com/Aweary) in [#6933](https://github.com/facebook/react/pull/6933))

### React DOM
- Add warning for unknown properties on DOM elements. ([@jimfb](https://github.com/jimfb) in [#6800](https://github.com/facebook/react/pull/6800), [@gm758](https://github.com/gm758) in [#7152](https://github.com/facebook/react/pull/7152))
- Properly remove attributes from custom elements. ([@grassator](https://github.com/grassator) in [#6748](https://github.com/facebook/react/pull/6748))
- Fix invalid unicode escape in attribute name regular expression. ([@nbjahan](https://github.com/nbjahan) in [#6772](https://github.com/facebook/react/pull/6772))
- Add `onLoad` handling to `<link>` element. ([@roderickhsiao](https://github.com/roderickhsiao) in [#6815](https://github.com/facebook/react/pull/6815))
- Add `onError` handling to `<source>` element. ([@wadahiro](https://github.com/wadahiro) in [#6941](https://github.com/facebook/react/pull/6941))
- Handle `value` and `defaultValue` more accurately in the DOM. ([@jimfb](https://github.com/jimfb) in [#6406](https://github.com/facebook/react/pull/6406))
- Fix events issue in environments with mutated `Object.prototype`. ([@Weizenlol](https://github.com/Weizenlol) in [#6886](https://github.com/facebook/react/pull/6886))
- Fix issue where `is="null"` ended up in the DOM in Firefox. ([@darobin](https://github.com/darobin) in [#6896](https://github.com/facebook/react/pull/6896))
- Improved performance of text escaping by using [escape-html](https://github.com/component/escape-html). ([@aickin](https://github.com/aickin) in [#6862](https://github.com/facebook/react/pull/6862))
- Fix issue with `dangerouslySetInnerHTML` and SVG in Internet Explorer. ([@joshhunt](https://github.com/joshhunt) in [#6982](https://github.com/facebook/react/pull/6982))
- Fix issue with `<textarea>` placeholders. ([@jimfb](https://github.com/jimfb) in [#7002](https://github.com/facebook/react/pull/7002))
- Fix controlled vs uncontrolled detection of `<input type="radio"/>`. ([@jimfb](https://github.com/jimfb) in [#7003](https://github.com/facebook/react/pull/7003))
- Improve performance of updating text content. ([@trueadm](https://github.com/trueadm) in [#7005](https://github.com/facebook/react/pull/7005))
- Ensure controlled `<select>` components behave the same on initial render as they do on updates. ([@yiminghe](https://github.com/yiminghe) in [#5362](https://github.com/facebook/react/pull/5362))

### React Perf Add-on
- Add `isRunning()` API. ([@nfcampos](https://github.com/nfcampos) in [#6763](https://github.com/facebook/react/pull/6763))
- Improve accuracy of lifecycle hook timing. ([@gaearon](https://github.com/gaearon) in [#6858](https://github.com/facebook/react/pull/6858))
- Fix internal errors when using ReactPerf with portal components. ([@gaearon](https://github.com/gaearon) in [#6860](https://github.com/facebook/react/pull/6860))
- Fix performance regression. ([@sophiebits](https://github.com/sophiebits) in [#6770](https://github.com/facebook/react/pull/6770))
- Add warning that ReactPerf is not enabled in production. ([@sashashakun](https://github.com/sashashakun) in [#6884](https://github.com/facebook/react/pull/6884))

### React CSSTransitionGroup Add-on
- Fix timing issue with `null` node. ([@keyanzhang](https://github.com/keyanzhang) in [#6958](https://github.com/facebook/react/pull/6958))

### React Native Renderer
- Dependencies on React Native modules use CommonJS requires instead of providesModule. ([@davidaurelio](https://github.com/davidaurelio) in [#6715](https://github.com/facebook/react/pull/6715))


## 15.1.0 (May 20, 2016)

### React
- Ensure we're using the latest `object-assign`, which has protection against a non-spec-compliant native `Object.assign`. ([@zpao](https://github.com/zpao) in [#6681](https://github.com/facebook/react/pull/6681))
- Add a new warning to communicate that `props` objects passed to `createElement` must be plain objects. ([@richardscarrott](https://github.com/richardscarrott) in [#6134](https://github.com/facebook/react/pull/6134))
- Fix a batching bug resulting in some lifecycle methods incorrectly being called multiple times. ([@sophiebits](https://github.com/sophiebits) in [#6650](https://github.com/facebook/react/pull/6650))

### React DOM
- Fix regression in custom elements support. ([@jscissr](https://github.com/jscissr) in [#6570](https://github.com/facebook/react/pull/6570))
- Stop incorrectly warning about using `onScroll` event handler with server rendering. ([@Aweary](https://github.com/Aweary) in [#6678](https://github.com/facebook/react/pull/6678))
- Fix grammar in the controlled input warning. ([@jakeboone02](https://github.com/jakeboone02) in [#6657](https://github.com/facebook/react/pull/6657))
- Fix issue preventing `<object>` nodes from being able to read `<param>` nodes in IE. ([@syranide](https://github.com/syranide) in [#6691](https://github.com/facebook/react/pull/6691))
- Fix issue resulting in crash when using experimental error boundaries with server rendering. ([@jimfb](https://github.com/jimfb) in [#6694](https://github.com/facebook/react/pull/6694))
- Add additional information to the controlled input warning. ([@borisyankov](https://github.com/borisyankov) in [#6341](https://github.com/facebook/react/pull/6341))

### React Perf Add-on
- Completely rewritten to collect data more accurately and to be easier to maintain. ([@gaearon](https://github.com/gaearon) in [#6647](https://github.com/facebook/react/pull/6647), [#6046](https://github.com/facebook/react/pull/6046))

### React Native Renderer
- Remove some special cases for platform specific branching. ([@sebmarkbage](https://github.com/sebmarkbage) in [#6660](https://github.com/facebook/react/pull/6660))
- Remove use of `merge` utility. ([@sebmarkbage](https://github.com/sebmarkbage) in [#6634](https://github.com/facebook/react/pull/6634))
- Renamed some modules to better indicate usage ([@javache](https://github.com/javache) in [#6643](https://github.com/facebook/react/pull/6643))


## 15.0.2 (April 29, 2016)

### React
- Removed extraneous files from npm package. ([@gaearon](https://github.com/gaearon) in [#6388](https://github.com/facebook/react/pull/6388))
- Ensure `componentWillUnmount` is only called once. ([@jimfb](https://github.com/jimfb) in [#6613](https://github.com/facebook/react/pull/6613))

### ReactDOM
- Fixed bug resulting in disabled buttons responding to mouse events in IE. ([@nhunzaker](https://github.com/nhunzaker) in [#6215](https://github.com/facebook/react/pull/6215))
- Ensure `<option>`s are correctly selected when inside `<optgroup>`. ([@trevorsmith](https://github.com/trevorsmith) in [#6442](https://github.com/facebook/react/pull/6442))
- Restore support for rendering into a shadow root. ([@Wildhoney](https://github.com/Wildhoney) in [#6462](https://github.com/facebook/react/pull/6462))
- Ensure nested `<body>` elements are caught when warning for invalid markup. ([@keyanzhang](https://github.com/keyanzhang) in [#6469](https://github.com/facebook/react/pull/6469))
- Improve warning when encountering multiple elements with the same key. ([@hkal](https://github.com/hkal) in [#6500](https://github.com/facebook/react/pull/6500))

### React TestUtils Add-on
- Ensure that functional components do not have an owner. ([@gaearon](https://github.com/gaearon) in [#6362](https://github.com/facebook/react/pull/6362))
- Handle invalid arguments to `scryRenderedDOMComponentsWithClass` better. ([@ipeters90](https://github.com/ipeters90) in [#6529](https://github.com/facebook/react/pull/6529))

### React Perf Add-on
- Ignore DOM operations that occur outside the batch operation. ([@gaearon](https://github.com/gaearon) in [#6516](https://github.com/facebook/react/pull/6516))

### React Native Renderer
- These files are now shipped inside the React npm package. They have no impact on React core or ReactDOM.


## 15.0.1 (April 8, 2016)

### React
- Restore `React.__spread` API to unbreak code compiled with some tools making use of this undocumented API. It is now officially deprecated. ([@zpao](https://github.com/zpao) in [#6444](https://github.com/facebook/react/pull/6444))

### ReactDOM
- Fixed issue resulting in loss of cursor position in controlled inputs. ([@sophiebits](https://github.com/sophiebits) in [#6449](https://github.com/facebook/react/pull/6449))


## 15.0.0 (April 7, 2016)

### Major changes

- **Initial render now uses `document.createElement` instead of generating HTML.** Previously we would generate a large string of HTML and then set `node.innerHTML`. At the time, this was decided to be faster than using `document.createElement` for the majority of cases and browsers that we supported. Browsers have continued to improve and so overwhelmingly this is no longer true. By using `createElement` we can make other parts of React faster. ([@sophiebits](https://github.com/sophiebits) in [#5205](https://github.com/facebook/react/pull/5205))
- **`data-reactid` is no longer on every node.** As a result of using `document.createElement`, we can prime the node cache as we create DOM nodes, allowing us to skip a potential lookup (which used the `data-reactid` attribute). Root nodes will have a `data-reactroot` attribute and server generated markup will still contain `data-reactid`. ([@sophiebits](https://github.com/sophiebits) in [#5205](https://github.com/facebook/react/pull/5205))
- **No more extra `<span>`s.** ReactDOM will now render plain text nodes interspersed with comment nodes that are used for demarcation. This gives us the same ability to update individual pieces of text, without creating extra nested nodes. If you were targeting these `<span>`s in your CSS, you will need to adjust accordingly. You can always render them explicitly in your components. ([@mwiencek](https://github.com/mwiencek) in [#5753](https://github.com/facebook/react/pull/5753))
- **Rendering `null` now uses comment nodes.** Previously `null` would render to `<noscript>` elements. We now use comment nodes. This may cause issues if making use of `:nth-child` CSS selectors. While we consider this rendering behavior an implementation detail of React, it's worth noting the potential problem. ([@sophiebits](https://github.com/sophiebits) in [#5451](https://github.com/facebook/react/pull/5451))
- **Functional components can now return `null`.** We added support for [defining stateless components as functions](/react/blog/2015/09/10/react-v0.14-rc1.html#stateless-function-components) in React 0.14. However, React 0.14 still allowed you to define a class component without extending `React.Component` or using `React.createClass()`, so [we couldn’t reliably tell if your component is a function or a class](https://github.com/facebook/react/issues/5355), and did not allow returning `null` from it. This issue is solved in React 15, and you can now return `null` from any component, whether it is a class or a function. ([@jimfb](https://github.com/jimfb) in [#5884](https://github.com/facebook/react/pull/5884))
- **Improved SVG support.** All SVG tags are now fully supported. (Uncommon SVG tags are not present on the `React.DOM` element helper, but JSX and `React.createElement` work on all tag names.) All SVG attributes that are implemented by the browsers should be supported too. If you find any attributes that we have missed, please [let us know in this issue](https://github.com/facebook/react/issues/1657). ([@zpao](https://github.com/zpao) in [#6243](https://github.com/facebook/react/pull/6243))

### Breaking changes

- **No more extra `<span>`s.**
- **`React.cloneElement()` now resolves `defaultProps`.** We fixed a bug in `React.cloneElement()` that some components may rely on. If some of the `props` received by `cloneElement()` are `undefined`, it used to return an element with `undefined` values for those props. We’re changing it to be consistent with `createElement()`. Now any `undefined` props passed to `cloneElement()` are resolved to the corresponding component’s `defaultProps`. ([@truongduy134](https://github.com/truongduy134) in [#5997](https://github.com/facebook/react/pull/5997))
- **`ReactPerf.getLastMeasurements()` is opaque.** This change won’t affect applications but may break some third-party tools. We are [revamping `ReactPerf` implementation](https://github.com/facebook/react/pull/6046) and plan to release it during the 15.x cycle. The internal performance measurement format is subject to change so, for the time being, we consider the return value of `ReactPerf.getLastMeasurements()` an opaque data structure that should not be relied upon. ([@gaearon](https://github.com/gaearon) in [#6286](https://github.com/facebook/react/pull/6286))

#### Removed deprecations

These deprecations were introduced nine months ago in v0.14 with a warning and are removed:

- Deprecated APIs are removed from the `React` top-level export: `findDOMNode`, `render`, `renderToString`, `renderToStaticMarkup`, and `unmountComponentAtNode`. As a reminder, they are now available on `ReactDOM` and `ReactDOMServer`. ([@jimfb](https://github.com/jimfb) in [#5832](https://github.com/facebook/react/pull/5832))
- Deprecated addons are removed: `batchedUpdates` and `cloneWithProps`. ([@jimfb](https://github.com/jimfb) in [#5859](https://github.com/facebook/react/pull/5859), [@zpao](https://github.com/zpao) in [#6016](https://github.com/facebook/react/pull/6016))
- Deprecated component instance methods are removed: `setProps`, `replaceProps`, and `getDOMNode`. ([@jimfb](https://github.com/jimfb) in [#5570](https://github.com/facebook/react/pull/5570))
- Deprecated CommonJS `react/addons` entry point is removed. As a reminder, you should use separate `react-addons-*` packages instead. This only applies if you use the CommonJS builds. ([@gaearon](https://github.com/gaearon) in [#6285](https://github.com/facebook/react/pull/6285))
- Passing `children` to void elements like `<input>` was deprecated, and now throws an error. ([@jonhester](https://github.com/jonhester) in [#3372](https://github.com/facebook/react/pull/3372))
- React-specific properties on DOM `refs` (e.g. `this.refs.div.props`) were deprecated, and are removed now. ([@jimfb](https://github.com/jimfb) in [#5495](https://github.com/facebook/react/pull/5495))

### New deprecations, introduced with a warning

Each of these changes will continue to work as before with a new warning until the release of React 16 so you can upgrade your code gradually.

- `LinkedStateMixin` and `valueLink` are now deprecated due to very low popularity. If you need this, you can use a wrapper component that implements the same behavior: [react-linked-input](https://www.npmjs.com/package/react-linked-input). ([@jimfb](https://github.com/jimfb) in [#6127](https://github.com/facebook/react/pull/6127))
- Future versions of React will treat `<input value={null}>` as a request to clear the input. However, React 0.14 has been ignoring `value={null}`. React 15 warns you on a `null` input value and offers you to clarify your intention. To fix the warning, you may explicitly pass an empty string to clear a controlled input, or pass `undefined` to make the input uncontrolled. ([@antoaravinth](https://github.com/antoaravinth) in [#5048](https://github.com/facebook/react/pull/5048))
- `ReactPerf.printDOM()` was renamed to `ReactPerf.printOperations()`, and `ReactPerf.getMeasurementsSummaryMap()` was renamed to `ReactPerf.getWasted()`. ([@gaearon](https://github.com/gaearon) in [#6287](https://github.com/facebook/react/pull/6287))

### New helpful warnings

- If you use a minified copy of the _development_ build, React DOM kindly encourages you to use the faster production build instead. ([@sophiebits](https://github.com/sophiebits) in [#5083](https://github.com/facebook/react/pull/5083))
- React DOM: When specifying a unit-less CSS value as a string, a future version will not add `px` automatically. This version now warns in this case (ex: writing `style={{width: '300'}}`. Unitless *number* values like `width: 300` are unchanged. ([@pluma](https://github.com/pluma) in [#5140](https://github.com/facebook/react/pull/5140))
- Synthetic Events will now warn when setting and accessing properties (which will not get cleared appropriately), as well as warn on access after an event has been returned to the pool. ([@kentcdodds](https://github.com/kentcdodds) in [#5940](https://github.com/facebook/react/pull/5940) and [@koba04](https://github.com/koba04) in [#5947](https://github.com/facebook/react/pull/5947))
- Elements will now warn when attempting to read `ref` and `key` from the props. ([@prometheansacrifice](https://github.com/prometheansacrifice) in [#5744](https://github.com/facebook/react/pull/5744))
- React will now warn if you pass a different `props` object to `super()` in the constructor. ([@prometheansacrifice](https://github.com/prometheansacrifice) in [#5346](https://github.com/facebook/react/pull/5346))
- React will now warn if you call `setState()` inside `getChildContext()`. ([@raineroviir](https://github.com/raineroviir) in [#6121](https://github.com/facebook/react/pull/6121))
- React DOM now attempts to warn for mistyped event handlers on DOM elements, such as `onclick` which should be `onClick`. ([@ali](https://github.com/ali) in [#5361](https://github.com/facebook/react/pull/5361))
- React DOM now warns about `NaN` values in `style`. ([@jontewks](https://github.com/jontewks) in [#5811](https://github.com/facebook/react/pull/5811))
- React DOM now warns if you specify both `value` and `defaultValue` for an input. ([@mgmcdermott](https://github.com/mgmcdermott) in [#5823](https://github.com/facebook/react/pull/5823))
- React DOM now warns if an input switches between being controlled and uncontrolled. ([@TheBlasfem](https://github.com/TheBlasfem) in [#5864](https://github.com/facebook/react/pull/5864))
- React DOM now warns if you specify `onFocusIn` or `onFocusOut` handlers as they are unnecessary in React. ([@jontewks](https://github.com/jontewks) in [#6296](https://github.com/facebook/react/pull/6296))
- React now prints a descriptive error message when you pass an invalid callback as the last argument to `ReactDOM.render()`, `this.setState()`, or `this.forceUpdate()`. ([@conorhastings](https://github.com/conorhastings) in [#5193](https://github.com/facebook/react/pull/5193) and [@gaearon](https://github.com/gaearon) in [#6310](https://github.com/facebook/react/pull/6310))
- Add-Ons: `TestUtils.Simulate()` now prints a helpful message if you attempt to use it with shallow rendering. ([@conorhastings](https://github.com/conorhastings) in [#5358](https://github.com/facebook/react/pull/5358))
- PropTypes: `arrayOf()` and `objectOf()` provide better error messages for invalid arguments. ([@chicoxyzzy](https://github.com/chicoxyzzy) in [#5390](https://github.com/facebook/react/pull/5390))

### Notable bug fixes

- Fixed multiple small memory leaks. ([@sophiebits](https://github.com/sophiebits) in [#4983](https://github.com/facebook/react/pull/4983) and [@victor-homyakov](https://github.com/victor-homyakov) in [#6309](https://github.com/facebook/react/pull/6309))
- Input events are handled more reliably in IE 10 and IE 11; spurious events no longer fire when using a placeholder. ([@jquense](https://github.com/jquense) in [#4051](https://github.com/facebook/react/pull/4051))
- The `componentWillReceiveProps()` lifecycle method is now consistently called when `context` changes. ([@milesj](https://github.com/milesj) in [#5787](https://github.com/facebook/react/pull/5787))
- `React.cloneElement()` doesn’t append slash to an existing `key` when used inside `React.Children.map()`. ([@ianobermiller](https://github.com/ianobermiller) in [#5892](https://github.com/facebook/react/pull/5892))
- React DOM now supports the `cite` and `profile` HTML attributes. ([@AprilArcus](https://github.com/AprilArcus) in [#6094](https://github.com/facebook/react/pull/6094) and [@saiichihashimoto](https://github.com/saiichihashimoto) in [#6032](https://github.com/facebook/react/pull/6032))
- React DOM now supports `cssFloat`, `gridRow` and `gridColumn` CSS properties. ([@stevenvachon](https://github.com/stevenvachon) in [#6133](https://github.com/facebook/react/pull/6133) and  [@mnordick](https://github.com/mnordick) in [#4779](https://github.com/facebook/react/pull/4779))
- React DOM now correctly handles `borderImageOutset`, `borderImageWidth`, `borderImageSlice`, `floodOpacity`, `strokeDasharray`, and `strokeMiterlimit` as unitless CSS properties. ([@rofrischmann](https://github.com/rofrischmann) in [#6210](https://github.com/facebook/react/pull/6210) and [#6270](https://github.com/facebook/react/pull/6270))
- React DOM now supports the `onAnimationStart`, `onAnimationEnd`, `onAnimationIteration`, `onTransitionEnd`, and `onInvalid` events. Support for `onLoad` has been added to `object` elements. ([@tomduncalf](https://github.com/tomduncalf) in [#5187](https://github.com/facebook/react/pull/5187),  [@milesj](https://github.com/milesj) in [#6005](https://github.com/facebook/react/pull/6005), and [@ara4n](https://github.com/ara4n) in [#5781](https://github.com/facebook/react/pull/5781))
- React DOM now defaults to using DOM attributes instead of properties, which fixes a few edge case bugs. Additionally the nullification of values (ex: `href={null}`) now results in the forceful removal, no longer trying to set to the default value used by browsers in the absence of a value. ([@syranide](https://github.com/syranide) in [#1510](https://github.com/facebook/react/pull/1510))
- React DOM does not mistakenly coerce `children` to strings for Web Components. ([@jimfb](https://github.com/jimfb) in [#5093](https://github.com/facebook/react/pull/5093))
- React DOM now correctly normalizes SVG `<use>` events. ([@edmellum](https://github.com/edmellum) in [#5720](https://github.com/facebook/react/pull/5720))
- React DOM does not throw if a `<select>` is unmounted while its `onChange` handler is executing. ([@sambev](https://github.com/sambev) in [#6028](https://github.com/facebook/react/pull/6028))
- React DOM does not throw in Windows 8 apps. ([@Andrew8xx8](https://github.com/Andrew8xx8) in [#6063](https://github.com/facebook/react/pull/6063))
- React DOM does not throw when asynchronously unmounting a child with a `ref`. ([@yiminghe](https://github.com/yiminghe) in [#6095](https://github.com/facebook/react/pull/6095))
- React DOM no longer forces synchronous layout because of scroll position tracking. ([@syranide](https://github.com/syranide) in [#2271](https://github.com/facebook/react/pull/2271))
- `Object.is` is used in a number of places to compare values, which leads to fewer false positives, especially involving `NaN`. In particular, this affects the `shallowCompare` add-on. ([@chicoxyzzy](https://github.com/chicoxyzzy) in [#6132](https://github.com/facebook/react/pull/6132))
- Add-Ons: ReactPerf no longer instruments adding or removing an event listener because they don’t really touch the DOM due to event delegation. ([@antoaravinth](https://github.com/antoaravinth) in [#5209](https://github.com/facebook/react/pull/5209))

### Other improvements

- React now uses `loose-envify` instead of `envify` so it installs fewer transitive dependencies. ([@qerub](https://github.com/qerub) in [#6303](https://github.com/facebook/react/pull/6303))
- Shallow renderer now exposes `getMountedInstance()`. ([@glenjamin](https://github.com/glenjamin) in [#4918](https://github.com/facebook/react/pull/4918))
- Shallow renderer now returns the rendered output from `render()`. ([@simonewebdesign](https://github.com/simonewebdesign) in [#5411](https://github.com/facebook/react/pull/5411))
- React no longer depends on ES5 *shams* for `Object.create` and `Object.freeze` in older environments. It still, however, requires ES5 *shims* in those environments. ([@dgreensp](https://github.com/dgreensp) in [#4959](https://github.com/facebook/react/pull/4959))
- React DOM now allows `data-` attributes with names that start with numbers. ([@nLight](https://github.com/nLight) in [#5216](https://github.com/facebook/react/pull/5216))
- React DOM adds a new `suppressContentEditableWarning` prop for components like [Draft.js](https://facebook.github.io/draft-js/) that intentionally manage `contentEditable` children with React. ([@mxstbr](https://github.com/mxstbr) in [#6112](https://github.com/facebook/react/pull/6112))
- React improves the performance for `createClass()` on complex specs. ([@sophiebits](https://github.com/sophiebits) in [#5550](https://github.com/facebook/react/pull/5550))


## 0.14.8 (March 29, 2016)

### React
- Fixed memory leak when rendering on the server

## 0.14.7 (January 28, 2016)

### React
- Fixed bug with `<option>` tags when using `dangerouslySetInnerHTML`
- Fixed memory leak in synthetic event system

### React TestUtils Add-on
- Fixed bug with calling `setState` in `componentWillMount` when using shallow rendering


## 0.14.6 (January 6, 2016)

### React
- Updated `fbjs` dependency to pick up change affecting handling of undefined document.


## 0.14.5 (December 29, 2015)

### React
- More minor internal changes for better compatibility with React Native


## 0.14.4 (December 29, 2015)

### React
- Minor internal changes for better compatibility with React Native

### React DOM
- The `autoCapitalize` and `autoCorrect` props are now set as attributes in the DOM instead of properties to improve cross-browser compatibility
- Fixed bug with controlled `<select>` elements not handling updates properly

### React Perf Add-on
- Some DOM operation names have been updated for clarity in the output of `.printDOM()`


## 0.14.3 (November 18, 2015)

### React DOM
- Added support for `nonce` attribute for `<script>` and `<style>` elements
- Added support for `reversed` attribute for `<ol>` elements

### React TestUtils Add-on
- Fixed bug with shallow rendering and function refs

### React CSSTransitionGroup Add-on
- Fixed bug resulting in timeouts firing incorrectly when mounting and unmounting rapidly

### React on Bower
- Added `react-dom-server.js` to expose `renderToString` and `renderToStaticMarkup` for usage in the browser


## 0.14.2 (November 2, 2015)

### React DOM
- Fixed bug with development build preventing events from firing in some versions of Internet Explorer & Edge
- Fixed bug with development build when using es5-sham in older versions of Internet Explorer
- Added support for `integrity` attribute
- Fixed bug resulting in `children` prop being coerced to a string for custom elements, which was not the desired behavior
- Moved `react` from `dependencies` to `peerDependencies` to match expectations and align with `react-addons-*` packages


## 0.14.1 (October 28, 2015)

### React DOM
- Fixed bug where events wouldn't fire in old browsers when using React in development mode
- Fixed bug preventing use of `dangerouslySetInnerHTML` with Closure Compiler Advanced mode
- Added support for `srcLang`, `default`, and `kind` attributes for `<track>` elements
- Added support for `color` attribute
- Ensured legacy `.props` access on DOM nodes is updated on re-renders

### React TestUtils Add-on
- Fixed `scryRenderedDOMComponentsWithClass` so it works with SVG

### React CSSTransitionGroup Add-on
- Fix bug preventing `0` to be used as a timeout value

### React on Bower
- Added `react-dom.js` to `main` to improve compatibility with tooling


## 0.14.0 (October 7, 2015)

### Major changes

- Split the main `react` package into two: `react` and `react-dom`.  This paves the way to writing components that can be shared between the web version of React and React Native.  This means you will need to include both files and some functions have been moved from `React` to `ReactDOM`.
- Addons have been moved to separate packages (`react-addons-clone-with-props`, `react-addons-create-fragment`, `react-addons-css-transition-group`, `react-addons-linked-state-mixin`, `react-addons-perf`, `react-addons-pure-render-mixin`, `react-addons-shallow-compare`, `react-addons-test-utils`, `react-addons-transition-group`, `react-addons-update`, `ReactDOM.unstable_batchedUpdates`).
- Stateless functional components - React components were previously created using React.createClass or using ES6 classes.  This release adds a [new syntax](https://reactjs.org/docs/reusable-components.html#stateless-functions) where a user defines a single [stateless render function](https://reactjs.org/docs/reusable-components.html#stateless-functions) (with one parameter: `props`) which returns a JSX element, and this function may be used as a component.
- Refs to DOM components as the DOM node itself. Previously the only useful thing you can do with a DOM component is call `getDOMNode()` to get the underlying DOM node. Starting with this release, a ref to a DOM component _is_ the actual DOM node. **Note that refs to custom (user-defined) components work exactly as before; only the built-in DOM components are affected by this change.**


### Breaking changes

- `React.initializeTouchEvents` is no longer necessary and has been removed completely. Touch events now work automatically.
- Add-Ons: Due to the DOM node refs change mentioned above, `TestUtils.findAllInRenderedTree` and related helpers are no longer able to take a DOM component, only a custom component.
- The `props` object is now frozen, so mutating props after creating a component element is no longer supported. In most cases, [`React.cloneElement`](https://reactjs.org/docs/react-api.html#cloneelement) should be used instead. This change makes your components easier to reason about and enables the compiler optimizations mentioned above.
- Plain objects are no longer supported as React children; arrays should be used instead. You can use the [`createFragment`](https://reactjs.org/docs/create-fragment.html) helper to migrate, which now returns an array.
- Add-Ons: `classSet` has been removed. Use [classnames](https://github.com/JedWatson/classnames) instead.
- Web components (custom elements) now use native property names.  Eg: `class` instead of `className`.

### Deprecations

- `this.getDOMNode()` is now deprecated and `ReactDOM.findDOMNode(this)` can be used instead. Note that in the common case, `findDOMNode` is now unnecessary since a ref to the DOM component is now the actual DOM node.
- `setProps` and `replaceProps` are now deprecated. Instead, call ReactDOM.render again at the top level with the new props.
- ES6 component classes must now extend `React.Component` in order to enable stateless function components. The [ES3 module pattern](https://reactjs.org/blog/2015/01/27/react-v0.13.0-beta-1.html#other-languages) will continue to work.
- Reusing and mutating a `style` object between renders has been deprecated. This mirrors our change to freeze the `props` object.
- Add-Ons: `cloneWithProps` is now deprecated. Use [`React.cloneElement`](https://reactjs.org/docs/react-api.html#cloneelement) instead (unlike `cloneWithProps`, `cloneElement` does not merge `className` or `style` automatically; you can merge them manually if needed).
- Add-Ons: To improve reliability, `CSSTransitionGroup` will no longer listen to transition events. Instead, you should specify transition durations manually using props such as `transitionEnterTimeout={500}`.

### Notable enhancements

- Added `React.Children.toArray` which takes a nested children object and returns a flat array with keys assigned to each child. This helper makes it easier to manipulate collections of children in your `render` methods, especially if you want to reorder or slice `this.props.children` before passing it down. In addition, `React.Children.map` now returns plain arrays too.
- React uses `console.error` instead of `console.warn` for warnings so that browsers show a full stack trace in the console. (Our warnings appear when you use patterns that will break in future releases and for code that is likely to behave unexpectedly, so we do consider our warnings to be “must-fix” errors.)
- Previously, including untrusted objects as React children [could result in an XSS security vulnerability](http://danlec.com/blog/xss-via-a-spoofed-react-element). This problem should be avoided by properly validating input at the application layer and by never passing untrusted objects around your application code. As an additional layer of protection, [React now tags elements](https://github.com/facebook/react/pull/4832) with a specific [ES2015 (ES6) `Symbol`](http://www.2ality.com/2014/12/es6-symbols.html) in browsers that support it, in order to ensure that React never considers untrusted JSON to be a valid element. If this extra security protection is important to you, you should add a `Symbol` polyfill for older browsers, such as the one included by [Babel’s polyfill](https://babeljs.io/docs/usage/polyfill/).
- When possible, React DOM now generates XHTML-compatible markup.
- React DOM now supports these standard HTML attributes: `capture`, `challenge`, `inputMode`, `is`, `keyParams`, `keyType`, `minLength`, `summary`, `wrap`. It also now supports these non-standard attributes: `autoSave`, `results`, `security`.
- React DOM now supports these SVG attributes, which render into namespaced attributes: `xlinkActuate`, `xlinkArcrole`, `xlinkHref`, `xlinkRole`, `xlinkShow`, `xlinkTitle`, `xlinkType`, `xmlBase`, `xmlLang`, `xmlSpace`.
- The `image` SVG tag is now supported by React DOM.
- In React DOM, arbitrary attributes are supported on custom elements (those with a hyphen in the tag name or an `is="..."` attribute).
- React DOM now supports these media events on `audio` and `video` tags: `onAbort`, `onCanPlay`, `onCanPlayThrough`, `onDurationChange`, `onEmptied`, `onEncrypted`, `onEnded`, `onError`, `onLoadedData`, `onLoadedMetadata`, `onLoadStart`, `onPause`, `onPlay`, `onPlaying`, `onProgress`, `onRateChange`, `onSeeked`, `onSeeking`, `onStalled`, `onSuspend`, `onTimeUpdate`, `onVolumeChange`, `onWaiting`.
- Many small performance improvements have been made.
- Many warnings show more context than before.
- Add-Ons: A [`shallowCompare`](https://github.com/facebook/react/pull/3355) add-on has been added as a migration path for `PureRenderMixin` in ES6 classes.
- Add-Ons: `CSSTransitionGroup` can now use [custom class names](https://github.com/facebook/react/blob/48942b85/docs/docs/10.1-animation.md#custom-classes) instead of appending `-enter-active` or similar to the transition name.

### New helpful warnings

- React DOM now warns you when nesting HTML elements invalidly, which helps you avoid surprising errors during updates.
- Passing `document.body` directly as the container to `ReactDOM.render` now gives a warning as doing so can cause problems with browser extensions that modify the DOM.
- Using multiple instances of React together is not supported, so we now warn when we detect this case to help you avoid running into the resulting problems.

### Notable bug fixes

- Click events are handled by React DOM more reliably in mobile browsers, particularly in Mobile Safari.
- SVG elements are created with the correct namespace in more cases.
- React DOM now renders `<option>` elements with multiple text children properly and renders `<select>` elements on the server with the correct option selected.
- When two separate copies of React add nodes to the same document (including when a browser extension uses React), React DOM tries harder not to throw exceptions during event handling.
- Using non-lowercase HTML tag names in React DOM (e.g., `React.createElement('DIV')`) no longer causes problems, though we continue to recommend lowercase for consistency with the JSX tag name convention (lowercase names refer to built-in components, capitalized names refer to custom components).
- React DOM understands that these CSS properties are unitless and does not append “px” to their values: `animationIterationCount`, `boxOrdinalGroup`, `flexOrder`, `tabSize`, `stopOpacity`.
- Add-Ons: When using the test utils, `Simulate.mouseEnter` and `Simulate.mouseLeave` now work.
- Add-Ons: ReactTransitionGroup now correctly handles multiple nodes being removed simultaneously.


### React Tools / Babel

#### Breaking Changes

- The `react-tools` package and `JSXTransformer.js` browser file [have been deprecated](https://reactjs.org/blog/2015/06/12/deprecating-jstransform-and-react-tools.html). You can continue using version `0.13.3` of both, but we no longer support them and recommend migrating to [Babel](https://babeljs.io), which has built-in support for React and JSX.

#### New Features

- Babel 5.8.24 introduces **Inlining React elements:** The `optimisation.react.inlineElements` transform converts JSX elements to object literals like `{type: 'div', props: ...}` instead of calls to `React.createElement`.  This should only be enabled in production, since it disables some development warnings/checks.
- Babel 5.8.24 introduces **Constant hoisting for React elements:** The `optimisation.react.constantElements` transform hoists element creation to the top level for subtrees that are fully static, which reduces calls to `React.createElement` and the resulting allocations. More importantly, it tells React that the subtree hasn’t changed so React can completely skip it when reconciling.  This should only be enabled in production, since it disables some development warnings/checks.


## 0.13.3 (May 8, 2015)

### React Core

#### New Features

* Added `clipPath` element and attribute for SVG
* Improved warnings for deprecated methods in plain JS classes

#### Bug Fixes

* Loosened `dangerouslySetInnerHTML` restrictions so `{__html: undefined}` will no longer throw
* Fixed extraneous context warning with non-pure `getChildContext`
* Ensure `replaceState(obj)` retains prototype of `obj`

### React with Add-ons

### Bug Fixes

* Test Utils: Ensure that shallow rendering works when components define `contextTypes`


## 0.13.2 (April 18, 2015)

### React Core

#### New Features

* Added `strokeDashoffset`, `flexPositive`, `flexNegative` to the list of unitless CSS properties
* Added support for more DOM properties:
  * `scoped` - for `<style>` elements
  * `high`, `low`, `optimum` - for `<meter>` elements
  * `unselectable` - IE-specific property to prevent user selection

#### Bug Fixes

* Fixed a case where re-rendering after rendering null didn't properly pass context
* Fixed a case where re-rendering after rendering with `style={null}` didn't properly update `style`
* Update `uglify` dependency to prevent a bug in IE8
* Improved warnings

### React with Add-Ons

#### Bug Fixes

* Immutability Helpers: Ensure it supports `hasOwnProperty` as an object key

### React Tools

* Improve documentation for new options


## 0.13.1 (March 16, 2015)

### React Core

#### Bug Fixes

* Don't throw when rendering empty `<select>` elements
* Ensure updating `style` works when transitioning from `null`

### React with Add-Ons

#### Bug Fixes

* TestUtils: Don't warn about `getDOMNode` for ES6 classes
* TestUtils: Ensure wrapped full page components (`<html>`, `<head>`, `<body>`) are treated as DOM components
* Perf: Stop double-counting DOM components

### React Tools

#### Bug Fixes

* Fix option parsing for `--non-strict-es6module`


## 0.13.0 (March 10, 2015)

### React Core

#### Breaking Changes

* Deprecated patterns that warned in 0.12 no longer work: most prominently, calling component classes without using JSX or React.createElement and using non-component functions with JSX or createElement
* Mutating `props` after an element is created is deprecated and will cause warnings in development mode; future versions of React will incorporate performance optimizations assuming that props aren't mutated
* Static methods (defined in `statics`) are no longer autobound to the component class
* `ref` resolution order has changed slightly such that a ref to a component is available immediately after its `componentDidMount` method is called; this change should be observable only if your component calls a parent component's callback within your `componentDidMount`, which is an anti-pattern and should be avoided regardless
* Calls to `setState` in life-cycle methods are now always batched and therefore asynchronous. Previously the first call on the first mount was synchronous.
* `setState` and `forceUpdate` on an unmounted component now warns instead of throwing. That avoids a possible race condition with Promises.
* Access to most internal properties has been completely removed, including `this._pendingState` and `this._rootNodeID`.

#### New Features

* Support for using ES6 classes to build React components; see the [v0.13.0 beta 1 notes](https://reactjs.org/blog/2015/01/27/react-v0.13.0-beta-1.html) for details.
* Added new top-level API `React.findDOMNode(component)`, which should be used in place of `component.getDOMNode()`. The base class for ES6-based components will not have `getDOMNode`. This change will enable some more patterns moving forward.
* Added a new top-level API `React.cloneElement(el, props)` for making copies of React elements – see the [v0.13 RC2 notes](https://reactjs.org/blog/2015/03/03/react-v0.13-rc2.html#react.cloneelement) for more details.
* New `ref` style, allowing a callback to be used in place of a name: `<Photo ref={(c) => this._photo = c} />` allows you to reference the component with `this._photo` (as opposed to `ref="photo"` which gives `this.refs.photo`).
* `this.setState()` can now take a function as the first argument for transactional state updates, such as `this.setState((state, props) => ({count: state.count + 1}));` – this means that you no longer need to use `this._pendingState`, which is now gone.
* Support for iterators and immutable-js sequences as children.

#### Deprecations

* `ComponentClass.type` is deprecated. Just use `ComponentClass` (usually as `element.type === ComponentClass`).
* Some methods that are available on `createClass`-based components are removed or deprecated from ES6 classes (`getDOMNode`, `replaceState`, `isMounted`, `setProps`, `replaceProps`).

### React with Add-Ons

#### New Features

* [`React.addons.createFragment` was added](https://reactjs.org/docs/create-fragment.html) for adding keys to entire sets of children.

#### Deprecations

* `React.addons.classSet` is now deprecated. This functionality can be replaced with several freely available modules. [classnames](https://www.npmjs.com/package/classnames) is one such module.
* Calls to `React.addons.cloneWithProps` can be migrated to use `React.cloneElement` instead – make sure to merge `style` and `className` manually if desired.

### React Tools

#### Breaking Changes

* When transforming ES6 syntax, `class` methods are no longer enumerable by default, which requires `Object.defineProperty`; if you support browsers such as IE8, you can pass `--target es3` to mirror the old behavior

#### New Features

* `--target` option is available on the jsx command, allowing users to specify and ECMAScript version to target.
  * `es5` is the default.
  * `es3` restores the previous default behavior. An additional transform is added here to ensure the use of reserved words as properties is safe (eg `this.static` will become `this['static']` for IE8 compatibility).
* The transform for the call spread operator has also been enabled.

### JSXTransformer

#### Breaking Changes

* The return value of `transform` now contains `sourceMap` as a JS object already, not an instance of `SourceMapGenerator`.

### JSX

#### Breaking Changes
* A change was made to how some JSX was parsed, specifically around the use of `>` or `}` when inside an element. Previously it would be treated as a string but now it will be treated as a parse error. The [`jsx_orphaned_brackets_transformer`](https://www.npmjs.com/package/jsx_orphaned_brackets_transformer) package on npm can be used to find and fix potential issues in your JSX code.


## 0.12.2 (December 18, 2014)

### React Core

* Added support for more HTML attributes: `formAction`, `formEncType`, `formMethod`, `formTarget`, `marginHeight`, `marginWidth`
* Added `strokeOpacity` to the list of unitless CSS properties
* Removed trailing commas (allows npm module to be bundled and used in IE8)
* Fixed bug resulting in error when passing `undefined` to `React.createElement` - now there is a useful warning

### React Tools

* JSX-related transforms now always use double quotes for props and `displayName`


## 0.12.1 (November 18, 2014)

### React Tools

* Types transform updated with latest support
* jstransform version updated with improved ES6 transforms
* Explicit Esprima dependency removed in favor of using Esprima information exported by jstransform


## 0.12.0 (October 28, 2014)

### React Core

#### Breaking Changes

* `key` and `ref` moved off props object, now accessible on the element directly
* React is now BSD licensed with accompanying Patents grant
* Default prop resolution has moved to Element creation time instead of mount time, making them effectively static
* `React.__internals` is removed - it was exposed for DevTools which no longer needs access
* Composite Component functions can no longer be called directly - they must be wrapped with `React.createFactory` first. This is handled for you when using JSX.

#### New Features

* Spread operator (`{...}`) introduced to deprecate `this.transferPropsTo`
* Added support for more HTML attributes: `acceptCharset`, `classID`, `manifest`

#### Deprecations

* `React.renderComponent` --> `React.render`
* `React.renderComponentToString` --> `React.renderToString`
* `React.renderComponentToStaticMarkup` --> `React.renderToStaticMarkup`
* `React.isValidComponent` --> `React.isValidElement`
* `React.PropTypes.component` --> `React.PropTypes.element`
* `React.PropTypes.renderable` --> `React.PropTypes.node`
* **DEPRECATED** `React.isValidClass`
* **DEPRECATED** `instance.transferPropsTo`
* **DEPRECATED** Returning `false` from event handlers to preventDefault
* **DEPRECATED** Convenience Constructor usage as function, instead wrap with `React.createFactory`
* **DEPRECATED** use of `key={null}` to assign implicit keys

#### Bug Fixes

* Better handling of events and updates in nested results, fixing value restoration in "layered" controlled components
* Correctly treat `event.getModifierState` as case sensitive
* Improved normalization of `event.charCode`
* Better error stacks when involving autobound methods
* Removed DevTools message when the DevTools are installed
* Correctly detect required language features across browsers
* Fixed support for some HTML attributes:
  * `list` updates correctly now
  * `scrollLeft`, `scrollTop` removed, these should not be specified as props
* Improved error messages

### React With Addons

#### New Features

* `React.addons.batchedUpdates` added to API for hooking into update cycle

#### Breaking Changes

* `React.addons.update` uses `assign` instead of `copyProperties` which does `hasOwnProperty` checks. Properties on prototypes will no longer be updated correctly.

#### Bug Fixes

* Fixed some issues with CSS Transitions

### JSX

#### Breaking Changes

* Enforced convention: lower case tag names are always treated as HTML tags, upper case tag names are always treated as composite components
* JSX no longer transforms to simple function calls

#### New Features

* `@jsx React.DOM` no longer required
* spread (`{...}`) operator introduced to allow easier use of props

#### Bug Fixes

* JSXTransformer: Make sourcemaps an option when using APIs directly (eg, for react-rails)


## 0.11.2 (September 16, 2014)

### React Core

#### New Features

* Added support for `<dialog>` element and associated `open` attribute
* Added support for `<picture>` element and associated `media` and `sizes` attributes
* Added `React.createElement` API in preparation for React v0.12
  * `React.createDescriptor` has been deprecated as a result

### JSX

* `<picture>` is now parsed into `React.DOM.picture`

### React Tools

* Update `esprima` and `jstransform` for correctness fixes
* The `jsx` executable now exposes a `--strip-types` flag which can be used to remove TypeScript-like type annotations
  * This option is also exposed to `require('react-tools').transform` as `stripTypes`

## 0.11.1 (July 24, 2014)

### React Core

#### Bug Fixes
* `setState` can be called inside `componentWillMount` in non-DOM environments
* `SyntheticMouseEvent.getEventModifierState` correctly renamed to `getModifierState`
* `getModifierState` correctly returns a `boolean`
* `getModifierState` is now correctly case sensitive
* Empty Text node used in IE8 `innerHTML` workaround is now removed, fixing rerendering in certain cases

### JSX
* Fix duplicate variable declaration in JSXTransformer (caused issues in some browsers)


## 0.11.0 (July 17, 2014)

### React Core

#### Breaking Changes
* `getDefaultProps()` is now called once per class and shared across all instances
* `MyComponent()` now returns a descriptor, not an instance
* `React.isValidComponent` and `React.PropTypes.component` validate *descriptors*, not component instances
* Custom `propType` validators should return an `Error` instead of logging directly

#### New Features
* Rendering to `null`
* Keyboard events include normalized `e.key` and `e.getModifierState()` properties
* New normalized `onBeforeInput` event
* `React.Children.count` has been added as a helper for counting the number of children

#### Bug Fixes

* Re-renders are batched in more cases
* Events: `e.view` properly normalized
* Added Support for more HTML attributes (`coords`, `crossOrigin`, `download`, `hrefLang`, `mediaGroup`, `muted`, `scrolling`, `shape`, `srcSet`, `start`, `useMap`)
* Improved SVG support
  * Changing `className` on a mounted SVG component now works correctly
  * Added support for elements `mask` and `tspan`
  * Added support for attributes `dx`, `dy`, `fillOpacity`, `fontFamily`, `fontSize`, `markerEnd`, `markerMid`, `markerStart`, `opacity`, `patternContentUnits`, `patternUnits`, `preserveAspectRatio`, `strokeDasharray`, `strokeOpacity`
* CSS property names with vendor prefixes (`Webkit`, `ms`, `Moz`, `O`) are now handled properly
* Duplicate keys no longer cause a hard error; now a warning is logged (and only one of the children with the same key is shown)
* `img` event listeners are now unbound properly, preventing the error "Two valid but unequal nodes with the same `data-reactid`"
* Added explicit warning when missing polyfills

### React With Addons
* PureRenderMixin: a mixin which helps optimize "pure" components
* Perf: a new set of tools to help with performance analysis
* Update: New `$apply` command to transform values
* TransitionGroup bug fixes with null elements, Android

### React NPM Module
* Now includes the pre-built packages under `dist/`.
* `envify` is properly listed as a dependency instead of a peer dependency

### JSX
* Added support for namespaces, eg `<Components.Checkbox />`
* JSXTransformer
  * Enable the same `harmony` features available in the command line with `<script type="text/jsx;harmony=true">`
  * Scripts are downloaded in parallel for more speed. They are still executed in order (as you would expect with normal script tags)
  * Fixed a bug preventing sourcemaps from working in Firefox

### React Tools Module
* Improved readme with usage and API information
* Improved ES6 transforms available with `--harmony` option
* Added `--source-map-inline` option to the `jsx` executable
* New `transformWithDetails` API which gives access to the raw sourcemap data


## 0.10.0 (March 21, 2014)

### React Core

#### New Features
* Added warnings to help migrate towards descriptors
* Made it possible to server render without React-related markup (`data-reactid`, `data-react-checksum`). This DOM will not be mountable by React. [Read the docs for `React.renderComponentToStaticMarkup`](https://reactjs.org/docs/top-level-api.html#react.rendercomponenttostaticmarkup)
* Added support for more attributes:
  * `srcSet` for `<img>` to specify images at different pixel ratios
  * `textAnchor` for SVG

#### Bug Fixes
* Ensure all void elements don’t insert a closing tag into the markup.
* Ensure `className={false}` behaves consistently
* Ensure `this.refs` is defined, even if no refs are specified.

### Addons

* `update` function to deal with immutable data. [Read the docs](https://reactjs.org/docs/update.html)

### react-tools
* Added an option argument to `transform` function. The only option supported is `harmony`, which behaves the same as `jsx --harmony` on the command line. This uses the ES6 transforms from [jstransform](https://github.com/facebook/jstransform).


## 0.9.0 (February 20, 2014)

### React Core

#### Breaking Changes

- The lifecycle methods `componentDidMount` and `componentDidUpdate` no longer receive the root node as a parameter; use `this.getDOMNode()` instead
- Whenever a prop is equal to `undefined`, the default value returned by `getDefaultProps` will now be used instead
- `React.unmountAndReleaseReactRootNode` was previously deprecated and has now been removed
- `React.renderComponentToString` is now synchronous and returns the generated HTML string
- Full-page rendering (that is, rendering the `<html>` tag using React) is now supported only when starting with server-rendered markup
- On mouse wheel events, `deltaY` is no longer negated
- When prop types validation fails, a warning is logged instead of an error thrown (with the production build of React, type checks are now skipped for performance)
- On `input`, `select`, and `textarea` elements, `.getValue()` is no longer supported; use `.getDOMNode().value` instead
- `this.context` on components is now reserved for internal use by React

#### New Features

- React now never rethrows errors, so stack traces are more accurate and Chrome's purple break-on-error stop sign now works properly
- Added support for SVG tags `defs`, `linearGradient`, `polygon`, `radialGradient`, `stop`
- Added support for more attributes:
  - `crossOrigin` for CORS requests
  - `download` and `hrefLang` for `<a>` tags
  - `mediaGroup` and `muted` for `<audio>` and `<video>` tags
  - `noValidate` and `formNoValidate` for forms
  - `property` for Open Graph `<meta>` tags
  - `sandbox`, `seamless`, and `srcDoc` for `<iframe>` tags
  - `scope` for screen readers
  - `span` for `<colgroup>` tags
- Added support for defining `propTypes` in mixins
- Added `any`, `arrayOf`, `component`, `oneOfType`, `renderable`, `shape` to `React.PropTypes`
- Added support for `statics` on component spec for static component methods
- On all events, `.currentTarget` is now properly set
- On keyboard events, `.key` is now polyfilled in all browsers for special (non-printable) keys
- On clipboard events, `.clipboardData` is now polyfilled in IE
- On drag events, `.dragTransfer` is now present
- Added support for `onMouseOver` and `onMouseOut` in addition to the existing `onMouseEnter` and `onMouseLeave` events
- Added support for `onLoad` and `onError` on `<img>` elements
- Added support for `onReset` on `<form>` elements
- The `autoFocus` attribute is now polyfilled consistently on `input`, `select`, and `textarea`

#### Bug Fixes

- React no longer adds an `__owner__` property to each component's `props` object; passed-in props are now never mutated
- When nesting top-level components (e.g., calling `React.renderComponent` within `componentDidMount`), events now properly bubble to the parent component
- Fixed a case where nesting top-level components would throw an error when updating
- Passing an invalid or misspelled propTypes type now throws an error
- On mouse enter/leave events, `.target`, `.relatedTarget`, and `.type` are now set properly
- On composition events, `.data` is now properly normalized in IE9 and IE10
- CSS property values no longer have `px` appended for the unitless properties `columnCount`, `flex`, `flexGrow`, `flexShrink`, `lineClamp`, `order`, `widows`
- Fixed a memory leak when unmounting children with a `componentWillUnmount` handler
- Fixed a memory leak when `renderComponentToString` would store event handlers
- Fixed an error that could be thrown when removing form elements during a click handler
- Boolean attributes such as `disabled` are rendered without a value (previously `disabled="true"`, now simply `disabled`)
- `key` values containing `.` are now supported
- Shortened `data-reactid` values for performance
- Components now always remount when the `key` property changes
- Event handlers are attached to `document` only when necessary, improving performance in some cases
- Events no longer use `.returnValue` in modern browsers, eliminating a warning in Chrome
- `scrollLeft` and `scrollTop` are no longer accessed on document.body, eliminating a warning in Chrome
- General performance fixes, memory optimizations, improvements to warnings and error messages

### React with Addons

- `React.addons.TestUtils` was added to help write unit tests
- `React.addons.TransitionGroup` was renamed to `React.addons.CSSTransitionGroup`
- `React.addons.TransitionGroup` was added as a more general animation wrapper
- `React.addons.cloneWithProps` was added for cloning components and modifying their props
- Bug fix for adding back nodes during an exit transition for CSSTransitionGroup
- Bug fix for changing `transitionLeave` in CSSTransitionGroup
- Performance optimizations for CSSTransitionGroup
- On checkbox `<input>` elements, `checkedLink` is now supported for two-way binding

### JSX Compiler and react-tools Package

- Whitespace normalization has changed; now space between two tags on the same line will be preserved, while newlines between two tags will be removed
- The `react-tools` npm package no longer includes the React core libraries; use the `react` package instead.
- `displayName` is now added in more cases, improving error messages and names in the React Dev Tools
- Fixed an issue where an invalid token error was thrown after a JSX closing tag
- `JSXTransformer` now uses source maps automatically in modern browsers
- `JSXTransformer` error messages now include the filename and problematic line contents when a file fails to parse

## 0.8.0 (December 19, 2013)

### React

* Added support for more attributes:
  * `rows` & `cols` for `<textarea>`
  * `defer` & `async` for `<script>`
  * `loop` for `<audio>` & `<video>`
  * `autoCorrect` for form fields (a non-standard attribute only supported by mobile WebKit)
* Improved error messages
* Fixed Selection events in IE11
* Added `onContextMenu` events

### React with Addons

* Fixed bugs with TransitionGroup when children were undefined
* Added support for `onTransition`

### react-tools

* Upgraded `jstransform` and `esprima-fb`

### JSXTransformer

* Added support for use in IE8
* Upgraded browserify, which reduced file size by ~65KB (16KB gzipped)


## 0.5.2, 0.4.2 (December 18, 2013)

### React

* Fixed a potential XSS vulnerability when using user content as a `key`: [CVE-2013-7035](https://groups.google.com/forum/#!topic/reactjs/OIqxlB2aGfU)


## 0.5.1 (October 29, 2013)

### React

* Fixed bug with `<input type="range">` and selection events.
* Fixed bug with selection and focus.
* Made it possible to unmount components from the document root.
* Fixed bug for `disabled` attribute handling on non-`<input>` elements.

### React with Addons

* Fixed bug with transition and animation event detection.


## 0.5.0 (October 16, 2013)

### React

* Memory usage improvements - reduced allocations in core which will help with GC pauses
* Performance improvements - in addition to speeding things up, we made some tweaks to stay out of slow path code in V8 and Nitro.
* Standardized prop -> DOM attribute process. This previously resulting in additional type checking and overhead as well as confusing cases for users. Now we will always convert your value to a string before inserting it into the DOM.
* Support for Selection events.
* Support for [Composition events](https://developer.mozilla.org/en-US/docs/Web/API/CompositionEvent).
* Support for additional DOM properties (`charSet`, `content`, `form`, `httpEquiv`, `rowSpan`, `autoCapitalize`).
* Support for additional SVG properties (`rx`, `ry`).
* Support for using `getInitialState` and `getDefaultProps` in mixins.
* Support mounting into iframes.
* Bug fixes for controlled form components.
* Bug fixes for SVG element creation.
* Added `React.version`.
* Added `React.isValidClass` - Used to determine if a value is a valid component constructor.
* Removed `React.autoBind` - This was deprecated in v0.4 and now properly removed.
* Renamed  `React.unmountAndReleaseReactRootNode` to `React.unmountComponentAtNode`.
* Began laying down work for refined performance analysis.
* Better support for server-side rendering - [react-page](https://github.com/facebook/react-page) has helped improve the stability for server-side rendering.
* Made it possible to use React in environments enforcing a strict [Content Security Policy](https://developer.mozilla.org/en-US/docs/Security/CSP/Introducing_Content_Security_Policy). This also makes it possible to use React to build Chrome extensions.

### React with Addons (New!)

* Introduced a separate build with several "addons" which we think can help improve the React experience. We plan to deprecate this in the long-term, instead shipping each as standalone pieces. [Read more in the docs](https://reactjs.org/docs/addons.html).

### JSX

* No longer transform `class` to `className` as part of the transform! This is a breaking change - if you were using `class`, you *must* change this to `className` or your components will be visually broken.
* Added warnings to the in-browser transformer to make it clear it is not intended for production use.
* Improved compatibility for Windows
* Improved support for maintaining line numbers when transforming.


## 0.4.1 (July 26, 2013)

### React

* `setState` callbacks are now executed in the scope of your component.
* `click` events now work on Mobile Safari.
* Prevent a potential error in event handling if `Object.prototype` is extended.
* Don't set DOM attributes to the string `"undefined"` on update when previously defined.
* Improved support for `<iframe>` attributes.
* Added checksums to detect and correct cases where server-side rendering markup mismatches what React expects client-side.

### JSXTransformer

* Improved environment detection so it can be run in a non-browser environment.


## 0.4.0 (July 17, 2013)

### React

* Switch from using `id` attribute to `data-reactid` to track DOM nodes. This allows you to integrate with other JS and CSS libraries more easily.
* Support for more DOM elements and attributes (e.g., `<canvas>`)
* Improved server-side rendering APIs. `React.renderComponentToString(<component>, callback)` allows you to use React on the server and generate markup which can be sent down to the browser.
* `prop` improvements: validation and default values. [Read our blog post for details...](https://reactjs.org/blog/2013/07/11/react-v0-4-prop-validation-and-default-values.html)
* Support for the `key` prop, which allows for finer control over reconciliation. [Read the docs for details...](https://reactjs.org/docs/multiple-components.html)
* Removed `React.autoBind`. [Read our blog post for details...](https://reactjs.org/blog/2013/07/02/react-v0-4-autobind-by-default.html)
* Improvements to forms. We've written wrappers around `<input>`, `<textarea>`, `<option>`, and `<select>` in order to standardize many inconsistencies in browser implementations. This includes support for `defaultValue`, and improved implementation of the `onChange` event, and circuit completion. [Read the docs for details...](https://reactjs.org/docs/forms.html)
* We've implemented an improved synthetic event system that conforms to the W3C spec.
* Updates to your component are batched now, which may result in a significantly faster re-render of components. `this.setState` now takes an optional callback as it's second parameter. If you were using `onClick={this.setState.bind(this, state)}` previously, you'll want to make sure you add a third parameter so that the event is not treated as the callback.

### JSX

* Support for comment nodes `<div>{/* this is a comment and won't be rendered */}</div>`
* Children are now transformed directly into arguments instead of being wrapped in an array
  E.g. `<div><Component1/><Component2/></div>` is transformed into `React.DOM.div(null, Component1(null), Component2(null))`.
  Previously this would be transformed into `React.DOM.div(null, [Component1(null), Component2(null)])`.
  If you were using React without JSX previously, your code should still work.

### react-tools

* Fixed a number of bugs when transforming directories
* No longer re-write `require()`s to be relative unless specified


## 0.3.3 (June 20, 2013)

### React

* Allow reusing the same DOM node to render different components. e.g. `React.renderComponent(<div/>, domNode); React.renderComponent(<span/>, domNode);` will work now.

### JSX

* Improved the in-browser transformer so that transformed scripts will execute in the expected scope. The allows components to be defined and used from separate files.

### react-tools

* Upgrade Commoner so `require` statements are no longer relativized when passing through the transformer. This was a feature needed when building React, but doesn't translate well for other consumers of `bin/jsx`.
* Upgraded our dependencies on Commoner and Recast so they use a different directory for their cache.
* Freeze our Esprima dependency.


## 0.3.2 (May 31, 2013)

### JSX

* Improved compatibility with other coding styles (specifically, multiple assignments with a single `var`).

### react-tools

* Switch from using the browserified build to shipping individual modules. This allows react-tools to be used with [browserify](https://github.com/substack/node-browserify).


## 0.3.1 (May 30, 2013)

### react-tools

* Fix bug in packaging resulting in broken module.


## 0.3.0 (May 29, 2013)

* Initial public release
```
## _fixtures_dom_src_components_fixtures_text_inputs_README_md
```# Text Inputs

There are a couple of important concepts to be aware of when working on text
inputs in React.

## `defaultValue` vs `value`

An input's value is drawn from two properties: `defaultValue` and `value`.

The `defaultValue` property directly maps to the value _attribute_, for example:

'''javascript
var input = document.createElement('input')
input.defaultValue = 'hello'

console.log(input.getAttribute('value')) // => "hello"
'''

The `value` property manipulates the _working value_ for the input. This property
changes whenever the user interacts with an input, or it is modified with JavaScript:

'''javascript
var input = document.createElement('input')
input.defaultValue = 'hello'
input.value = 'goodbye'

console.log(input.getAttribute('value')) // => "hello"
console.log(input.value) // => "goodbye"
'''

## value detachment

Until `value` is manipulated by a user or JavaScript, manipulating `defaultValue`
will also modify the `value` property:

'''javascript
var input = document.createElement('input')
// This will turn into 3
input.defaultValue = 3
// This will turn into 5
input.defaultValue = 5
// This will turn into 7
input.value = 7
// This will do nothing
input.defaultValue = 1
'''

**React detaches all inputs**. This prevents `value` from accidentally updating if
`defaultValue` changes.

## Form reset events

React does not support `form.reset()` for controlled inputs. This is a feature,
not a bug. `form.reset()` works by reverting an input's `value` _property_ to
that of the current `defaultValue`. Since React assigns the value `attribute`
every time a controlled input's value changes, controlled inputs will never
"revert" back to their original display value.

## Number inputs

Chrome (55) and Safari (10) attempt to "correct" the value of number inputs any
time the value property or attribute are changed. This leads to some edge documented
here:

https://github.com/facebook/react/pull/7359#issuecomment-256499693
```
## _scripts_eslint_rules_README_md
```# Custom ESLint Rules

This is a dummy npm package that allows us to treat it as an `eslint-plugin`. It's not actually published, nor are the rules here useful for users of React. If you want to lint your React code, try <https://github.com/yannickcr/eslint-plugin-react>.

**If you modify this rule, you must re-run `npm install ./eslint-rules` for it to take effect.**
```
## _packages_react_is_README_md
```# `react-is`

This package allows you to test arbitrary values and see if they're a particular React element type.

## Installation

'''sh
# Yarn
yarn add react-is

# NPM
npm install react-is
'''

## Usage

### Determining if a Component is Valid

'''js
import React from "react";
import * as ReactIs from "react-is";

class ClassComponent extends React.Component {
  render() {
    return React.createElement("div");
  }
}

const FunctionComponent = () => React.createElement("div");

const ForwardRefComponent = React.forwardRef((props, ref) =>
  React.createElement(Component, { forwardedRef: ref, ...props })
);

const Context = React.createContext(false);

ReactIs.isValidElementType("div"); // true
ReactIs.isValidElementType(ClassComponent); // true
ReactIs.isValidElementType(FunctionComponent); // true
ReactIs.isValidElementType(ForwardRefComponent); // true
ReactIs.isValidElementType(Context.Provider); // true
ReactIs.isValidElementType(Context.Consumer); // true
ReactIs.isValidElementType(React.createFactory("div")); // true
'''

### Determining an Element's Type

#### Context

'''js
import React from "react";
import * as ReactIs from 'react-is';

const ThemeContext = React.createContext("blue");

ReactIs.isContextConsumer(<ThemeContext.Consumer />); // true
ReactIs.isContextProvider(<ThemeContext.Provider />); // true
ReactIs.typeOf(<ThemeContext.Provider />) === ReactIs.ContextProvider; // true
ReactIs.typeOf(<ThemeContext.Consumer />) === ReactIs.ContextConsumer; // true
'''

#### Element

'''js
import React from "react";
import * as ReactIs from 'react-is';

ReactIs.isElement(<div />); // true
ReactIs.typeOf(<div />) === ReactIs.Element; // true
'''

#### Fragment

'''js
import React from "react";
import * as ReactIs from 'react-is';

ReactIs.isFragment(<></>); // true
ReactIs.typeOf(<></>) === ReactIs.Fragment; // true
'''

#### Portal

'''js
import React from "react";
import ReactDOM from "react-dom";
import * as ReactIs from 'react-is';

const div = document.createElement("div");
const portal = ReactDOM.createPortal(<div />, div);

ReactIs.isPortal(portal); // true
ReactIs.typeOf(portal) === ReactIs.Portal; // true
'''

#### StrictMode

'''js
import React from "react";
import * as ReactIs from 'react-is';

ReactIs.isStrictMode(<React.StrictMode />); // true
ReactIs.typeOf(<React.StrictMode />) === ReactIs.StrictMode; // true
'''
```
## _packages_react_dom_README_md
```# `react-dom`

This package serves as the entry point to the DOM and server renderers for React. It is intended to be paired with the generic React package, which is shipped as `react` to npm.

## Installation

'''sh
npm install react react-dom
'''

## Usage

### In the browser

'''js
var React = require('react');
var ReactDOM = require('react-dom');

class MyComponent extends React.Component {
  render() {
    return <div>Hello World</div>;
  }
}

ReactDOM.render(<MyComponent />, node);
'''

### On the server

'''js
var React = require('react');
var ReactDOMServer = require('react-dom/server');

class MyComponent extends React.Component {
  render() {
    return <div>Hello World</div>;
  }
}

ReactDOMServer.renderToString(<MyComponent />);
'''

## API

### `react-dom`

- `findDOMNode`
- `render`
- `unmountComponentAtNode`

### `react-dom/server`

- `renderToString`
- `renderToStaticMarkup`
```
## _packages_react_devtools_README_md
```# `react-devtools`

React DevTools is available as a built-in extension for Chrome and Firefox browsers. This package enables you to debug a React app elsewhere (e.g. a mobile browser, an embedded webview, Safari, inside an iframe).

It works both with React DOM and React Native.

![React DevTools screenshot](https://user-images.githubusercontent.com/29597/63811956-bdd9b580-c8dd-11e9-8962-c568e475c425.png)

## Installation
Install the `react-devtools` package. Because this is a development tool, a global install is often the most convenient:
'''sh
# Yarn
yarn global add react-devtools

# NPM
npm install -g react-devtools
'''

If you prefer to avoid global installations, you can add `react-devtools` as a project dependency. With Yarn, you can do this by running:
'''sh
yarn add --dev react-devtools
'''

With NPM you can just use [NPX](https://www.npmjs.com/package/npx):
'''sh
npx react-devtools
'''

## Usage with React Native
Run `react-devtools` from the terminal to launch the standalone DevTools app:
'''sh
react-devtools
'''

If you're not in a simulator then you also need to run the following in a command prompt:
'''sh
adb reverse tcp:8097 tcp:8097
'''

If you're using React Native 0.43 or higher, it should connect to your simulator within a few seconds.

### Integration with React Native Inspector

You can open the [in-app developer menu](https://facebook.github.io/react-native/docs/debugging.html#accessing-the-in-app-developer-menu) and choose "Show Inspector". It will bring up an overlay that lets you tap on any UI element and see information about it:

![React Native Inspector](http://i.imgur.com/ReFhREb.gif)

However, when `react-devtools` is running, Inspector will enter a special collapsed mode, and instead use the DevTools as primary UI. In this mode, clicking on something in the simulator will bring up the relevant components in the DevTools:

![React DevTools Inspector Integration](https://user-images.githubusercontent.com/29597/63811958-be724c00-c8dd-11e9-8587-37357334a0e1.gif)


You can choose "Hide Inspector" in the same menu to exit this mode.

### Inspecting Component Instances

When debugging JavaScript in Chrome, you can inspect the props and state of the React components in the browser console.

First, follow the [instructions for debugging in Chrome](https://facebook.github.io/react-native/docs/debugging.html#chrome-developer-tools) to open the Chrome console.

Make sure that the dropdown in the top left corner of the Chrome console says `debuggerWorker.js`. **This step is essential.**

Then select a React component in React DevTools. There is a search box at the top that helps you find one by name. As soon as you select it, it will be available as `$r` in the Chrome console, letting you inspect its props, state, and instance properties.

![React DevTools Chrome Console Integration](https://user-images.githubusercontent.com/29597/63811957-be724c00-c8dd-11e9-9d1d-8eba440ef948.gif)


## Usage with React DOM

The standalone shell can also be useful with React DOM (e.g. to debug apps in Safari or inside of an iframe).

Run `react-devtools` from the terminal to launch the standalone DevTools app:
'''sh
react-devtools
'''

Add `<script src="http://localhost:8097"></script>` as the very first `<script>` tag in the `<head>` of your page when developing:

'''html
<!doctype html>
<html lang="en">
  <head>
    <script src="http://localhost:8097"></script>
'''

This will ensure the developer tools are connected. **Don’t forget to remove it before deploying to production!**

>If you install `react-devtools` as a project dependency, you may also replace the `<script>` suggested above with a JavaScript import (`import 'react-devtools'`). It is important that this import comes before any other imports in your app (especially before `react-dom`). Make sure to remove the import before deploying to production, as it carries a large DevTools client with it. If you use Webpack and have control over its configuration, you could alternatively add `'react-devtools'` as the first item in the `entry` array of the development-only configuration, and then you wouldn’t need to deal either with `<script>` tags or `import` statements.

## Advanced

By default DevTools listen to port `8097` on `localhost`. If you need to customize host, port, or other settings, see the `react-devtools-core` package instead.

## FAQ

### The React Tab Doesn't Show Up

**If you are running your app from a local `file://` URL**, don't forget to check "Allow access to file URLs" on the Chrome Extensions settings page. You can find it by opening Settings > Extensions:

![Allow access to file URLs](https://user-images.githubusercontent.com/29597/64646784-95b58080-d3cc-11e9-943d-02474683398a.png)

Or you could develop with a local HTTP server [like `serve`](https://www.npmjs.com/package/serve).

**The React tab won't show up if the site doesn't use React**, or if React can't communicate with the devtools. When the page loads, the devtools sets a global named `__REACT_DEVTOOLS_GLOBAL_HOOK__`, then React communicates with that hook during initialization. You can test this on the [React website](http://facebook.github.io/react/) or by inspecting [Facebook](https://www.facebook.com/).

**If your app is inside of CodePen**, make sure you are registered. Then press Fork (if it's not your pen), and then choose Change View > Debug. The Debug view is inspectable with DevTools because it doesn't use an iframe.

**If your app is inside an iframe, a Chrome extension, React Native, or in another unusual environment**, try [the standalone version instead](https://github.com/facebook/react/tree/master/packages/react-devtools). Chrome apps are currently not inspectable.

**If you still have issues** please [report them](https://github.com/facebook/react/issues/new?labels=Component:%20Developer%20Tools). Don't forget to specify your OS, browser version, extension version, and the exact instructions to reproduce the issue with a screenshot.

## Development

* Run `yarn start:backend` and `yarn start:standalone` in `../react-devtools-core`
* Run `yarn start` in this folder
* Refresh the app after it has recompiled a change
* For React Native, copy `react-devtools-core` to its `node_modules` to test your changes.
```
## _packages_react_devtools_shared_src_node_modules_react_window_CHANGELOG_md
```Changelog
------------

### 1.8.0
* 🎉 Added new "smart" align option for grid and list scroll-to-item methods ([gaearon](https://github.com/gaearon) - [#209](https://github.com/bvaughn/react-window/pull/209))

### 1.7.2
* 🐛 Add guards to avoid invalid scroll offsets when `scrollTo()` is called with a negative offset or when `scrollToItem` is called with invalid indices (negative or too large).

### 1.7.1
* 🐛 Fix SSR regression introduced in 1.7.0 - ([Betree](https://github.com/Betree) - [#185](https://github.com/bvaughn/react-window/pull/185))

### 1.7.0
* 🎉 Grid `scrollToItem` supports optional `rowIndex` and `columnIndex` params ([jgoz](https://github.com/jgoz) - [#174](https://github.com/bvaughn/react-window/pull/174))
* DEV mode checks for `WeakSet` support before using it to avoid requiring a polyfill for IE11 - ([jgoz](https://github.com/jgoz) - [#167](https://github.com/bvaughn/react-window/pull/167))

### 1.6.2
* 🐛 Bugfix for RTL  when scrolling back towards the beginning (right) of the list.

### 1.6.1
* 🐛 Bugfix to account for differences between Chrome and non-Chrome browsers with regard to RTL and "scroll" events.

### 1.6.0
* 🎉 RTL support added for lists and grids. Special thanks to [davidgarsan](https://github.com/davidgarsan) for his support. - [#156](https://github.com/bvaughn/react-window/pull/156)
* 🐛 Grid `scrollToItem` methods take scrollbar size into account when aligning items - [#153](https://github.com/bvaughn/react-window/issues/153)

### 1.5.2
* 🐛 Edge case bug fix for `VariableSizeList` and `VariableSizeGrid` when the number of items decreases while a scroll is in progress. - ([iamsolankiamit](https://github.com/iamsolankiamit) - [#138](https://github.com/bvaughn/react-window/pull/138))

### 1.5.1
* 🐛 Updated `getDerivedState` Flow annotations to address a warning in a newer version of Flow.

### 1.5.0
* 🎉 Added advanced memoization helpers methods `areEqual` and `shouldComponentUpdate` for item renderers. - [#114](https://github.com/bvaughn/react-window/issues/114)

### 1.4.0
* 🎉 List and Grid components now "overscan" (pre-render) in both directions when scrolling is not active. When scrolling is in progress, cells are only pre-rendered in the direction being scrolled. This change has been made in an effort to reduce visible flicker when scrolling starts without adding additional overhead during scroll (which is the most performance sensitive time).
* 🎉 Grid components now support separate `overscanColumnsCount` and `overscanRowsCount` props. Legacy `overscanCount` prop will continue to work, but with a deprecation warning in DEV mode.
* 🐛 Replaced `setTimeout` with `requestAnimationFrame` based timer, to avoid starvation issue for `isScrolling` reset. - [#106](https://github.com/bvaughn/react-window/issues/106)
* 🎉 Renamed List and Grid `innerTagName` and `outerTagName` props to `innerElementType` and `outerElementType` to formalize support for attaching arbitrary props (e.g. test ids) to List and Grid inner and outer DOM elements. Legacy `innerTagName` and `outerTagName` props will continue to work, but with a deprecation warning in DEV mode.
* 🐛 List re-renders items if `direction` prop changes. - [#104](https://github.com/bvaughn/react-window/issues/104)

### 1.3.1
* 🎉 Pass `itemData` value to custom `itemKey` callbacks when present - [#90](https://github.com/bvaughn/react-window/issues/90))

### 1.3.0
* (Skipped)

### 1.2.4
* 🐛 Added Flow annotations to memoized methods to avoid a Flow warning for newer versions of Flow

### 1.2.3
* 🐛 Relaxed `children` validation checks. They were too strict and didn't support new React APIs like `memo`.

### 1.2.2
* 🐛 Improved Flow types for class component item renderers - ([nicholas-l](https://github.com/nicholas-l) - [#77](https://github.com/bvaughn/react-window/pull/77))

### 1.2.1
* 🎉 Improved Flow types to include optional `itemData` parameter. ([TrySound](https://github.com/TrySound) - [#66](https://github.com/bvaughn/react-window/pull/66))
* 🐛 `VariableSizeList` and `VariableSizeGrid` no longer call size getter functions with invalid index when item count is zero.

### 1.2.0
* 🎉 Flow types added to NPM package. ([TrySound](https://github.com/TrySound) - [#40](https://github.com/bvaughn/react-window/pull/40))
* 🎉 Relaxed grid `scrollTo` method to make `scrollLeft` and `scrollTop` params _optional_ (so you can only update one axis if desired). - [#63](https://github.com/bvaughn/react-window/pull/63))
* 🐛 Fixed invalid `this` pointer in `VariableSizeGrid` that broke the `resetAfter*` methods - [#58](https://github.com/bvaughn/react-window/pull/58))
* Upgraded to babel 7 and used shared runtime helpers to reduce package size slightly. ([TrySound](https://github.com/TrySound) - [#48](https://github.com/bvaughn/react-window/pull/48))
* Remove `overflow:hidden` from inner container ([souporserious](https://github.com/souporserious) - [#56](https://github.com/bvaughn/react-window/pull/56))

### 1.1.2
* 🐛 Fixed edge case `scrollToItem` bug that caused lists/grids with very few items to have negative scroll offsets.

### 1.1.1
* 🐛 `FixedSizeGrid` and `FixedSizeList` automatically clear style cache when item size props change.

### 1.1.0
* 🎉 Use explicit `constructor` and `super` to generate cleaner component code. ([Andarist](https://github.com/Andarist) - [#26](https://github.com/bvaughn/react-window/pull/26))
* 🎉 Add optional `shouldForceUpdate` param reset-index methods to specify `forceUpdate` behavior. ([nihgwu](https://github.com/nihgwu) - [#32](https://github.com/bvaughn/react-window/pull/32))

### 1.0.3
* 🐛 Avoid unnecessary scrollbars for lists (e.g. no horizontal scrollbar for a vertical list) unless content requires them.

### 1.0.2

* 🎉 Enable Babel `annotate-pure-calls` option so that classes compiled by "transform-es2015-classes" are annotated with `#__PURE__`. This enables [UglifyJS to remove them if they are not referenced](https://github.com/mishoo/UglifyJS2/pull/1448), improving dead code elimination in application code. ([Andarist](https://github.com/Andarist) - [#20](https://github.com/bvaughn/react-window/pull/20))
* 🎉 Update "rollup-plugin-peer-deps-external" and use new `includeDependencies` flag so that the "memoize-one" dependency does not get inlined into the Rollup bundle. ([Andarist](https://github.com/Andarist) - [#19](https://github.com/bvaughn/react-window/pull/19))
* 🎉 Enable [Babel "loose" mode](https://babeljs.io/docs/en/babel-preset-env#loose) to reduce package size (-8%). ([Andarist](https://github.com/Andarist) - [#18](https://github.com/bvaughn/react-window/pull/18))

### 1.0.1
Updated `README.md` file to remove `@alpha` tag from NPM installation instructions.

# 1.0.0
Initial release of library. Includes the following components:
* `FixedSizeGrid`
* `FixedSizeList`
* `VariableSizeGrid`
* `VariableSizeList`
```
## _packages_react_reconciler_README_md
```# react-reconciler

This is an experimental package for creating custom React renderers.

**Its API is not as stable as that of React, React Native, or React DOM, and does not follow the common versioning scheme.**

**Use it at your own risk.**

## API

'''js
const Reconciler = require('react-reconciler');

const HostConfig = {
  // You'll need to implement some methods here.
  // See below for more information and examples.
};

const MyRenderer = Reconciler(HostConfig);

const RendererPublicAPI = {
  render(element, container, callback) {
    // Call MyRenderer.updateContainer() to schedule changes on the roots.
    // See ReactDOM, React Native, or React ART for practical examples.
  }
};

module.exports = RendererPublicAPI;
'''

## Practical Examples

A "host config" is an object that you need to provide, and that describes how to make something happen in the "host" environment (e.g. DOM, canvas, console, or whatever your rendering target is). It looks like this:

'''js
const HostConfig = {
  createInstance(type, props) {
    // e.g. DOM renderer returns a DOM node
  },
  // ...
  supportsMutation: true, // it works by mutating nodes
  appendChild(parent, child) {
    // e.g. DOM renderer would call .appendChild() here
  },
  // ...
};
'''

**For an introduction to writing a very simple custom renderer, check out this article series:**

* **[Building a simple custom renderer to DOM](https://medium.com/@agent_hunt/hello-world-custom-react-renderer-9a95b7cd04bc)**
* **[Building a simple custom renderer to native](https://medium.com/@agent_hunt/introduction-to-react-native-renderers-aka-react-native-is-the-java-and-react-native-renderers-are-828a0022f433)**

The full list of supported methods [can be found here](https://github.com/facebook/react/blob/master/packages/react-reconciler/src/forks/ReactFiberHostConfig.custom.js). For their signatures, we recommend looking at specific examples below.

The React repository includes several renderers. Each of them has its own host config.

The examples in the React repository are declared a bit differently than a third-party renderer would be. In particular, the `HostConfig` object mentioned above is never explicitly declared, and instead is a *module* in our code. However, its exports correspond directly to properties on a `HostConfig` object you'd need to declare in your code:

* [React ART](https://github.com/facebook/react/blob/master/packages/react-art/src/ReactART.js) and its [host config](https://github.com/facebook/react/blob/master/packages/react-art/src/ReactARTHostConfig.js)
* [React DOM](https://github.com/facebook/react/blob/master/packages/react-dom/src/client/ReactDOM.js) and its [host config](https://github.com/facebook/react/blob/master/packages/react-dom/src/client/ReactDOMHostConfig.js)
* [React Native](https://github.com/facebook/react/blob/master/packages/react-native-renderer/src/ReactNativeRenderer.js) and its [host config](https://github.com/facebook/react/blob/master/packages/react-native-renderer/src/ReactNativeHostConfig.js)

If these links break please file an issue and we’ll fix them. They intentionally link to the latest versions since the API is still evolving. If you have more questions please file an issue and we’ll try to help!
```
## _packages_react_devtools_inline_README_md
```# `react-devtools-inline`

React DevTools implementation for embedding within a browser-based IDE (e.g. [CodeSandbox](https://codesandbox.io/), [StackBlitz](https://stackblitz.com/)).

This is a low-level package. If you're looking for the standalone DevTools app, **use the `react-devtools` package instead.**

## Usage

This package exports two entry points: a frontend (to be run in the main `window`) and a backend (to be installed and run within an `iframe`<sup>1</sup>).

The frontend and backend can be initialized in any order, but **the backend must not be activated until after the frontend has been initialized**. Because of this, the simplest sequence is:

1. Frontend (DevTools interface) initialized in the main `window`.
1. Backend initialized in an `iframe`.
1. Backend activated.

<sup>1</sup> Sandboxed iframes are supported.

## API

### `react-devtools-inline/backend`

* **`initialize(contentWindow)`** -
Installs the global hook on the window. This hook is how React and DevTools communicate. **This method must be called before React is loaded.**<sup>2</sup>
* **`activate(contentWindow)`** -
Lets the backend know when the frontend is ready. It should not be called until after the frontend has been initialized, else the frontend might miss important tree-initialization events.

'''js
import { activate, initialize } from 'react-devtools-inline/backend';

// This should be the iframe the React application is running in.
const iframe = document.getElementById(frameID);
const contentWindow = iframe.contentWindow;

// Call this before importing React (or any other packages that might import React).
initialize(contentWindow);

// Initialize the frontend...

// Call this only once the frontend has been initialized.
activate(contentWindow);
'''

<sup>2</sup> The backend must be initialized before React is loaded. (This means before any `import` or `require` statements or `<script>` tags that include React.)

### `react-devtools-inline/frontend`

* **`initialize(contentWindow)`** -
Configures the DevTools interface to listen to the `window` the backend was injected into. This method returns a React component that can be rendered directly<sup>3</sup>.

'''js
import { initialize } from 'react-devtools-inline/frontend';

// This should be the iframe the backend hook has been installed in.
const iframe = document.getElementById(frameID);
const contentWindow = iframe.contentWindow;

// This returns a React component that can be rendered into your app.
// <DevTools {...props} />
const DevTools = initialize(contentWindow);
'''

<sup>3</sup> Because the DevTools interface makes use of several new React APIs (e.g. suspense, concurrent mode) it should be rendered using either `ReactDOM.createRoot` or `ReactDOM.createSyncRoot`. **It should not be rendered with `ReactDOM.render`.**

## Examples

### Configuring a same-origin `iframe`

The simplest way to use this package is to install the hook from the parent `window`. This is possible if the `iframe` is not sandboxed and there are no cross-origin restrictions.

'''js
import {
  activate as activateBackend,
  initialize as initializeBackend
} from 'react-devtools-inline/backend';
import { initialize as initializeFrontend } from 'react-devtools-inline/frontend';

// The React app you want to inspect with DevTools is running within this iframe:
const iframe = document.getElementById('target');
const { contentWindow } = iframe;

// Installs the global hook into the iframe.
// This must be called before React is loaded into that frame.
initializeBackend(contentWindow);

// React application can be injected into <iframe> at any time now...
// Note that this would need to be done via <script> tag injection,
// as setting the src of the <iframe> would load a new page (withou the injected backend).

// Initialize DevTools UI to listen to the hook we just installed.
// This returns a React component we can render anywhere in the parent window.
const DevTools = initializeFrontend(contentWindow);

// <DevTools /> interface can be rendered in the parent window at any time now...
// Be sure to use either ReactDOM.createRoot()
// or ReactDOM.createSyncRoot() to render this component.

// Let the backend know the frontend is ready and listening.
activateBackend(contentWindow);
'''

### Configuring a sandboxed `iframe`

Sandboxed `iframe`s are also supported but require more complex initialization.

**`iframe.html`**
'''js
import { activate, initialize } from "react-devtools-inline/backend";

// The DevTooks hook needs to be installed before React is even required!
// The safest way to do this is probably to install it in a separate script tag.
initialize(window);

// Wait for the frontend to let us know that it's ready.
function onMessage({ data }) {
  switch (data.type) {
    case "activate-backend":
      window.removeEventListener("message", onMessage);

      activate(window);
      break;
    default:
      break;
  }
}

window.addEventListener("message", onMessage);
'''

**`main-window.html`**
'''js
import { initialize } from "react-devtools-inline/frontend";

const iframe = document.getElementById("target");
const { contentWindow } = iframe;

// Initialize DevTools UI to listen to the iframe.
// This returns a React component we can render anywhere in the main window.
// Be sure to use either ReactDOM.createRoot()
// or ReactDOM.createSyncRoot() to render this component.
const DevTools = initialize(contentWindow);

// Let the backend know to initialize itself.
// We can't do this directly because the iframe is sandboxed.
// Only initialize the backend once the DevTools frontend has been initialized.
iframe.onload = () => {
  contentWindow.postMessage(
    {
      type: "activate-backend"
    },
    "*"
  );
};
'''

## Development

Watch for changes made to the source code and rebuild:
'''sh
yarn start
'''```
## _fixtures_dom_README_md
```# DOM Fixtures

A set of DOM test cases for quickly identifying browser issues.

## Setup

To reference a local build of React, first run `yarn build` at the root
of the React project. Then:

'''
cd fixtures/dom
yarn
yarn start
'''

The `start` command runs a script that copies over the local build of react into
the public directory.
```
## _fixtures_ssr_README_md
```# SSR Fixtures

A set of test cases for quickly identifying issues with server-side rendering.

## Setup

To reference a local build of React, first run `npm run build` at the root
of the React project. Then:

'''
cd fixtures/ssr
yarn
yarn start
'''

The `start` command runs a webpack dev server and a server-side rendering server in development mode with hot reloading.

**Note: whenever you make changes to React and rebuild it, you need to re-run `yarn` in this folder:**

'''
yarn
'''

If you want to try the production mode instead run:

'''
yarn start:prod
'''

This will pre-build all static resources and then start a server-side rendering HTTP server that hosts the React app and service the static resources (without hot reloading).
```
## _packages_jest_mock_scheduler_README_md
```# `jest-mock-scheduler`

Jest matchers and utilities for testing the `scheduler` package.

This package is experimental. APIs may change between releases.```
## _scripts_release_README_md
```# React Release Scripts

The release process consists of several phases, each one represented by one of the scripts below.

A typical release goes like this:
1. When a commit is pushed to the React repo, [Circle CI](https://circleci.com/gh/facebook/react/) will build all release bundles and run unit tests against both the source code and the built bundles.
2. Next the release is [**published as a canary**](#publishing-a-canary) using the [`prepare-canary`](#prepare-canary) and [`publish`](#publish) scripts. (Currently this process is manual but might be automated in the future using [GitHub "actions"](https://github.com/features/actions).)
3. Finally, a canary releases can be [**promoted to stable**](#publishing-a-stable-release)<sup>1</sup> using the [`prepare-stable`](#prepare-stable) and [`publish`](#publish) scripts. (This process is always manual.)

The high level process of creating releases is [documented below](#process). Individual scripts are documented as well:
* [`create-canary`](#create-canary)
* [`prepare-canary`](#prepare-canary)
* [`prepare-stable`](#prepare-stable)
* [`publish`](#publish)

<sup>Note that [**creating a patch release**](creating-a-patch-release) has a slightly different process than a major/minor release.</sup>

# Process

If this is your first time running the release scripts, go to the `scripts/release` directory and run `yarn` to install the dependencies.

## Publishing a Canary

Canaries are meant to be lightweight and published often. In most cases, canaries can be published using artifacts built by Circle CI.

To prepare a canary for a particular commit:
1. Choose a commit from [the commit log](https://github.com/facebook/react/commits/master).
2. Click the "“✓" icon and click the Circle CI "Details" link.
3. Select the `build` job (**not** the `build_experimental` job; see the next section). If it's still pending, you'll need to wait for it to finish. (Note: This is the most awkward part of cutting a release right now. We have plans to improve it.)
4. Copy the build ID from the URL (e.g. the build ID for [circleci.com/gh/facebook/react/13471](https://circleci.com/gh/facebook/react/13471) is  **13471**).
5. Run the [`prepare-canary`](#prepare-canary) script with the build ID you found <sup>1</sup>:
'''sh
scripts/release/prepare-canary.js --build=13471
'''

Once the canary has been checked out and tested locally, you're ready to publish it:
'''sh
scripts/release/publish.js --tags canary
'''

<sup>1: You can omit the `build` param if you just want to release the latest commit as a canary.</sup>

## Publishing an Experimental Canary

Experimental canaries are special releases with additional features turned on.

The steps for publishing an experimental canary are almost the same as for publishing a normal canary, except in step 3 you should choose the `build_experimental` job instead of `build`. (I know this is awkward; we have plans to make it less so. Ideally these canaries would get published by a cron job.)

When publishing an experimental canary, use the `experimental` tag:

'''sh
scripts/release/publish.js --tags experimental
'''

## Publishing a Stable Release

Stable releases should always be created from a previously-released canary. This encourages better testing of the actual release artifacts and reduces the chance of unintended changes accidentally being included in a stable release.

To prepare a stable release, choose a canary version and  run the [`prepare-stable`](#prepare-stable) script <sup>1</sup>:

'''sh
scripts/release/prepare-stable.js --version=0.0.0-5bf84d292
'''

This script will prompt you to select stable version numbers for each of the packages. It will update the package JSON versions (and dependencies) based on the numbers you select.

Once this step is complete, you're ready to publish the release:

'''sh
scripts/release/publish.js --tags next latest
'''

After successfully publishing the release, follow the on-screen instructions to ensure that all of the appropriate post-release steps are executed.

<sup>1: You can omit the `version` param if you just want to promote the latest canary to stable.</sup>

## Creating a Patch Release

Patch releases should always be created by branching from a previous release. This reduces the likelihood of unstable changes being accidentally included in the release.

Begin by creating a branch from the previous git tag<sup>1</sup>:

'''sh
git checkout -b 16.8.3 v16.8.2
'''

Next cherry pick any changes from master that you want to include in the release:

'''sh
git cherry-pick <commit-hash>
'''

Once you have cherry picked all of the commits you want to include in the release, push your feature branch and create a Pull Request (so that Circle CI will create a canary):

'''sh
git push origin 16.8.3
'''

Once CI is complete, follow the regular [**canary**](#publishing-a-canary) and [**promote to stable**](#publishing-a-stable-release) processes.

<sup>1: The `build-info.json` artifact can also be used to identify the appropriate commit (e.g. [unpkg.com/react@16.8.3/build-info.json](https://unpkg.com/react@16.8.3/build-info.json) shows us that react version 16.8.3 was created from commit [`29b7b775f`](https://github.com/facebook/react/commit/29b7b775f)).</sup>

# Scripts

## `create-canary`
Creates a canary build from the current (local) Git revision.

**This script is an escape hatch.** It allows a canary release to be created without pushing a commit to be verified by Circle CI. **It does not run any automated unit tests.** Testing is solely the responsibility of the release engineer.

Note that this script git-archives the React repo (at the current revision) to a temporary directory before building, so **uncommitted changes are not included in the build**.

#### Example usage
To create a canary from the current branch and revision:
'''sh
scripts/release/create-canary.js
'''

## `prepare-canary`
Downloads build artifacts from Circle CI in preparation to be published to NPM as a canary release.

All artifacts built by Circle CI have already been unit-tested (both source and bundles) but canaries should **always be manually tested** before being published. Upon completion, this script prints manual testing instructions.

#### Example usage
To prepare the artifacts created by [Circle CI build 12677](https://circleci.com/gh/facebook/react/12677#artifacts/containers/0) you would run:
'''sh
scripts/release/prepare-canary.js --build=12677
'''

## `prepare-stable`
Checks out a canary release from NPM and prepares it to be published as a stable release.

This script prompts for new (stable) release versions for each public package and updates the package contents (both `package.json` and inline version numbers) to match. It also updates inter-package dependencies to account for the new versions.

Canary release have already been tested but it is still a good idea to **manually test and verify a release** before publishing to ensure that e.g. version numbers are correct. Upon completion, this script prints manual testing instructions.

#### Example usage
To promote the canary release `0.0.0-5bf84d292` (aka commit [5bf84d292](https://github.com/facebook/react/commit/5bf84d292)) to stable:
'''sh
scripts/release/prepare-stable.js --version=0.0.0-5bf84d292
'''

## `publish`
Publishes the current contents of `build/node_modules` to NPM.

This script publishes each public package to NPM and updates the specified tag(s) to match. **It does not test or verify the local package contents before publishing**. This should be done by the release engineer prior to running the script.

Upon completion, this script provides instructions for tagging the Git commit that the package was created from and updating the release CHANGELOG.

**Specify a `--dry` flag when running this script if you want to skip the NPM-publish step.** In this event, the script will print the NPM commands but it will not actually run them.

#### Example usage
To publish a release to NPM as both `next` and `latest`:
'''sh
scripts/release/publish.js --tags next latest
'''
```
## _scripts_error_codes_README_md
```The error code system substitutes React's error messages with error IDs to
provide a better debugging support in production. Check out the blog post
[here](https://reactjs.org/blog/2016/07/11/introducing-reacts-error-code-system.html).

- [`codes.json`](https://github.com/facebook/react/blob/master/scripts/error-codes/codes.json)
  contains the mapping from IDs to error messages. This file is generated by the
  Gulp plugin and is used by both the Babel plugin and the error decoder page in
  our documentation. This file is append-only, which means an existing code in
  the file will never be changed/removed.
- [`extract-errors.js`](https://github.com/facebook/react/blob/master/scripts/error-codes/extract-errors.js)
  is an node script that traverses our codebase and updates `codes.json`. You
  can test it by running `yarn extract-errors`.
- [`transform-error-messages`](https://github.com/facebook/react/blob/master/scripts/error-codes/transform-error-messages.js)
  is a Babel pass that rewrites error messages to IDs for a production
  (minified) build.
```
## _packages_react_interactions_events_README_md
```# `react-interactions/events`

*This package is experimental. It is intended for use with the experimental React
events API that is not available in open source builds.*

Event Responders attach to a host node. They listen to native browser events
dispatched on the host node of their child and transform those events into
high-level events for applications.

The core API is documented below. Documentation for individual Event Responders
can be found [here](./docs).

## Event Responder Interface

Note: React Responders require the internal React flag `enableFlareAPI`.

An Event Responder Interface is defined using an object. Each responder can define DOM
events to listen to, handle the synthetic responder events, dispatch custom
events, and implement a state machine.

'''js
// types
type ResponderEventType = string;

type ResponderEvent = {|
  nativeEvent: any,
  target: Element | Document,
  pointerType: string,
  type: string,
  passive: boolean,
  passiveSupported: boolean,
|};

type CustomEvent = {
  type: string,
  target: Element,
  ...
}
'''

### getInitialState?: (props: null | Object) => Object

The initial state of that the Event Responder is created with.

### onEvent?: (event: ResponderEvent, context: ResponderContext, props, state)

Called during the bubble phase of the `targetEventTypes` dispatched on DOM
elements within the Event Responder.

### onMount?: (context: ResponderContext, props, state)

Called after an Event Responder in mounted.

### onRootEvent?: (event: ResponderEvent, context: ResponderContext, props, state)

Called when any of the `rootEventTypes` are dispatched on the root of the app.

### onUnmount?: (context: ResponderContext, props, state)

Called before an Event Responder in unmounted.

### rootEventTypes?: Array<ResponderEventType>

Defines the DOM events to listen to on the root of the app.

### targetEventTypes?: Array<ResponderEventType>

Defines the DOM events to listen to within the Event Responder subtree.

## ResponderContext

The Event Responder Context is exposed via the `context` argument for certain methods
on the `EventResponder` object.

### addRootEventTypes(eventTypes: Array<ResponderEventType>)

This can be used to dynamically listen to events on the root of the app only
when it is necessary to do so.

### dispatchEvent(propName: string, event: CustomEvent, { discrete: boolean })

Dispatches a custom synthetic event. The `type` and `target` are required
fields if the event is an object, but any other fields can be defined on the `event` that will be passed
to the `listener`. You can also pass a value that is not an object, but a `boolean`. For example:

'''js
const event = { type: 'press', target, pointerType, x, y };
context.dispatchEvent('onPress', event, DiscreteEvent);
'''

### isTargetWithinNode(target: Element, element: Element): boolean

Returns `true` if `target` is a child of `element`.

### isTargetWithinResponder(target: Element): boolean

Returns `true` is the target element is within the subtree of the Event Responder.

### isTargetWithinResponderScope(target: Element): boolean

Returns `true` is the target element is within the current Event Responder's scope. If the target element
is within the scope of the same responder, but owned by another Event Responder instance, this will return `false`.

### removeRootEventTypes(eventTypes: Array<ResponderEventType>)

Remove the root event types added with `addRootEventTypes`.
```
## _fixtures_unstable_async_time_slicing_README_md
```# CPU async rendering demo

## What is this fixture?

This is a demo application based on [Dan Abramov's](https://github.com/gaearon) recent [JSConf Iceland talk](https://reactjs.org/blog/2018/03/01/sneak-peek-beyond-react-16.html) about React.

It depends on a local build of React and enables us to easily test async "time slicing" APIs in a more "real world app" like context.

## Can I use this code in production?

No. The APIs being tested here are unstable and some of them have still not been released to NPM. For now, this fixture is only a test harness.

There are also known bugs and inefficiencies in master so **don't use this fixture for demonstration purposes either yet**. Until they are fixed, this fixture is **not** indicative of React async rendering performance.

## How do I run this fixture?

'''shell
# 1: Build react from source
cd /path/to/react
yarn
yarn build react-dom/index,react/index,react-cache,scheduler --type=NODE

# 2: Install fixture dependencies
cd fixtures/unstable-async/time-slicing/
yarn

# 3: Run the app
yarn start
'''
```
## _CONTRIBUTING_md
```# Contributing to React

Want to contribute to React? There are a few things you need to know.  

We wrote a **[contribution guide](https://reactjs.org/contributing/how-to-contribute.html)** to help you get started.
```
## _packages_react_interactions_accessibility_docs_FocusManager_md
```# FocusManager

`FocusManager` is a module that exports a selection of helpful utility functions to be used
in conjunction with the `ref` from a React Scope, such as `TabbableScope`.

## Example

'''jsx
import {
  focusFirst,
  focusNext,
  focusPrevious,
  getNextScope,
  getPreviousScope,
} from 'react-interactions/accessibility/focus-manager';

function scopeQuery(type) {
  return type === 'div';
}

function KeyboardFocusMover(props) {
  const scopeRef = useRef(null);

  useEffect(() => {
    const scope = scopeRef.current;

    if (scope) {
      // Focus the first tabbable DOM node in my children
      focusFirst(scopeQuery, scope);
      // Then focus the next chilkd
      focusNext(scopeQuery, scope);
    }
  });
  
  return (
    <TabbableScope ref={scopeRef}>
      {props.children}
    </TabbableScope>
  );
}
'''

## FocusManager API

### `focusFirst`

Focus the first node that matches the given scope.

### `focusNext`

Focus the next sequential node that matches the given scope.

### `focusPrevious`

Focus the previous sequential node that matches the given scope.

### `getNextScope`

Focus the first node that matches the next sibling scope from the given scope.

### `getPreviousScope`

Focus the first node that matches the previous sibling scope from the given scope.
```
# Inline
## _packages_scheduler_src_TracingSubscriptions_js

## _packages_react_refresh_src_tests_ReactFresh_test_js
### Line 87-105
```
        }
        $RefreshReg$(Hello, 'Hello');
        return Hello;
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update.
      let HelloV2 = patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 110-150
```
        }
        $RefreshReg$(Hello, 'Hello');
        return Hello;
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Bump the state again.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Perform top-down renders with both fresh and stale types.
      // Neither should change the state or color.
      // They should always resolve to the latest version.
      render(() => HelloV1);
      render(() => HelloV2);
      render(() => HelloV1);
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Bump the state again.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('3');
      expect(el.style.color).toBe('red');

      // Finally, a render with incompatible type should reset it.
      render(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 151-161
```
            <p style={{color: 'blue'}} onClick={() => setVal(val + 1)}>
              {val}
            </p>
          );
        }
        // No register call.
        // This is considered a new type.
        return Hello;
      });
      expect(container.firstChild).not.toBe(el);
      const newEl = container.firstChild;
```
### Line 180-198
```
        const Outer = React.forwardRef(() => <Hello />);
        $RefreshReg$(Outer, 'Outer');
        return Outer;
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update.
      let OuterV2 = patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 206-238
```
        const Outer = React.forwardRef(() => <Hello />);
        $RefreshReg$(Outer, 'Outer');
        return Outer;
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Bump the state again.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Perform top-down renders with both fresh and stale types.
      // Neither should change the state or color.
      // They should always resolve to the latest version.
      render(() => OuterV1);
      render(() => OuterV2);
      render(() => OuterV1);
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Finally, a render with incompatible type should reset it.
      render(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 241-250
```
            </p>
          );
        }
        $RefreshReg$(Hello, 'Hello');

        // Note: no forwardRef wrapper this time.
        return Hello;
      });

      expect(container.firstChild).not.toBe(el);
```
### Line 269-279
```
          $RefreshReg$(Hello, 'Hello');

          function renderInner() {
            return <Hello />;
          }
          // Both of these are wrappers around the same inner function.
          // They should be treated as distinct types across reloads.
          let ForwardRefA = React.forwardRef(renderInner);
          $RefreshReg$(ForwardRefA, 'ForwardRefA');
          let ForwardRefB = React.forwardRef(renderInner);
          $RefreshReg$(ForwardRefB, 'ForwardRefB');
```
### Line 286-304
```
          return Parent;
        },
        {cond: true},
      );

      // Bump the state before switching up types.
      let el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Switching up the inner types should reset the state.
      render(() => ParentV1, {cond: false});
      expect(el).not.toBe(container.firstChild);
      el = container.firstChild;
      expect(el.textContent).toBe('0');
```
### Line 307-329
```
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Switch them up back again.
      render(() => ParentV1, {cond: true});
      expect(el).not.toBe(container.firstChild);
      el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');

      // Now bump up the state to prepare for patching.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Patch to change the color.
      let ParentV2 = patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 335-345
```
        $RefreshReg$(Hello, 'Hello');

        function renderInner() {
          return <Hello />;
        }
        // Both of these are wrappers around the same inner function.
        // They should be treated as distinct types across reloads.
        let ForwardRefA = React.forwardRef(renderInner);
        $RefreshReg$(ForwardRefA, 'ForwardRefA');
        let ForwardRefB = React.forwardRef(renderInner);
        $RefreshReg$(ForwardRefB, 'ForwardRefB');
```
### Line 350-379
```
        $RefreshReg$(Parent, 'Parent');

        return Parent;
      });

      // The state should be intact; the color should change.
      expect(el).toBe(container.firstChild);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Switching up the condition should still reset the state.
      render(() => ParentV2, {cond: false});
      expect(el).not.toBe(container.firstChild);
      el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('red');

      // Now bump up the state to prepare for top-level renders.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el).toBe(container.firstChild);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Finally, verify using top-level render with stale type keeps state.
      render(() => ParentV1);
      render(() => ParentV2);
      render(() => ParentV1);
      expect(container.firstChild).toBe(el);
```
### Line 398-416
```
        const Outer = React.forwardRef(() => <Hello color="blue" />);
        $RefreshReg$(Outer, 'Outer');
        return Outer;
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update.
      patch(() => {
        function Hello({color}) {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 424-433
```
        const Outer = React.forwardRef(() => <Hello color="red" />);
        $RefreshReg$(Outer, 'Outer');
        return Outer;
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');
    }
```
### Line 452-470
```
        $RefreshReg$(renderHello, 'renderHello');

        return React.forwardRef(renderHello);
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update of just the rendering function.
      patch(() => {
        function Hello({color}) {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 478-490
```
        function renderHello() {
          return <Hello color="red" />;
        }
        $RefreshReg$(renderHello, 'renderHello');

        // Not updating the wrapper.
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');
    }
```
### Line 506-524
```
        const Outer = React.memo(Hello);
        $RefreshReg$(Outer, 'Outer');
        return Outer;
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update.
      let OuterV2 = patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 532-564
```
        const Outer = React.memo(Hello);
        $RefreshReg$(Outer, 'Outer');
        return Outer;
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Bump the state again.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Perform top-down renders with both fresh and stale types.
      // Neither should change the state or color.
      // They should always resolve to the latest version.
      render(() => OuterV1);
      render(() => OuterV2);
      render(() => OuterV1);
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Finally, a render with incompatible type should reset it.
      render(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 567-576
```
            </p>
          );
        }
        $RefreshReg$(Hello, 'Hello');

        // Note: no wrapper this time.
        return Hello;
      });

      expect(container.firstChild).not.toBe(el);
```
### Line 595-613
```
        const Outer = React.memo(Hello, () => true);
        $RefreshReg$(Outer, 'Outer');
        return Outer;
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update.
      let OuterV2 = patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 620-652
```
        const Outer = React.memo(Hello, () => true);
        $RefreshReg$(Outer, 'Outer');
        return Outer;
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Bump the state again.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Perform top-down renders with both fresh and stale types.
      // Neither should change the state or color.
      // They should always resolve to the latest version.
      render(() => OuterV1);
      render(() => OuterV2);
      render(() => OuterV1);
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Finally, a render with incompatible type should reset it.
      render(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 655-664
```
            </p>
          );
        }
        $RefreshReg$(Hello, 'Hello');

        // Note: no wrapper this time.
        return Hello;
      });

      expect(container.firstChild).not.toBe(el);
```
### Line 682-700
```
        $RefreshReg$(Hello, 'Hello');

        return React.memo(Hello);
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update of just the rendering function.
      patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 703-715
```
            </p>
          );
        }
        $RefreshReg$(Hello, 'Hello');

        // Not updating the wrapper.
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');
    }
```
### Line 731-749
```
        const Outer = React.memo(React.forwardRef(() => <Hello />));
        $RefreshReg$(Outer, 'Outer');
        return Outer;
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update.
      let OuterV2 = patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 757-789
```
        const Outer = React.memo(React.forwardRef(() => <Hello />));
        $RefreshReg$(Outer, 'Outer');
        return Outer;
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Bump the state again.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Perform top-down renders with both fresh and stale types.
      // Neither should change the state or color.
      // They should always resolve to the latest version.
      render(() => OuterV1);
      render(() => OuterV2);
      render(() => OuterV1);
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Finally, a render with incompatible type should reset it.
      render(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 792-801
```
            </p>
          );
        }
        $RefreshReg$(Hello, 'Hello');

        // Note: no wrapper this time.
        return Hello;
      });

      expect(container.firstChild).not.toBe(el);
```
### Line 842-860
```
      await act(async () => {
        jest.runAllTimers();
      });
      expect(container.textContent).toBe('0');

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update.
      let AppV2 = patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 883-915
```
        $RefreshReg$(App, 'App');

        return App;
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Bump the state again.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Perform top-down renders with both fresh and stale types.
      // Neither should change the state or color.
      // They should always resolve to the latest version.
      render(() => AppV1);
      render(() => AppV2);
      render(() => AppV1);
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('2');
      expect(el.style.color).toBe('red');

      // Finally, a render with incompatible type should reset it.
      render(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 918-927
```
            </p>
          );
        }
        $RefreshReg$(Hello, 'Hello');

        // Note: no lazy wrapper this time.

        function App() {
          return (
            <React.Suspense fallback={<p>Loading</p>}>
```
### Line 973-982
```
        return App;
      });

      expect(container.textContent).toBe('Loading');

      // Perform a hot update.
      patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 990-1012
```

      await act(async () => {
        jest.runAllTimers();
      });

      // Expect different color on initial mount.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('red');

      // Bump state.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Test another reload.
      patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1056-1065
```
        return App;
      });

      expect(container.textContent).toBe('Loading');

      // Perform a hot update.
      patch(() => {
        function renderHello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1074-1096
```

      await act(async () => {
        jest.runAllTimers();
      });

      // Expect different color on initial mount.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('red');

      // Bump state.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Test another reload.
      patch(() => {
        function renderHello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1141-1150
```
        return App;
      });

      expect(container.textContent).toBe('Loading');

      // Perform a hot update.
      patch(() => {
        function renderHello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1159-1181
```

      await act(async () => {
        jest.runAllTimers();
      });

      // Expect different color on initial mount.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('red');

      // Bump state.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Test another reload.
      patch(() => {
        function renderHello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1226-1235
```
        return App;
      });

      expect(container.textContent).toBe('Loading');

      // Perform a hot update.
      patch(() => {
        function renderHello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1244-1266
```

      await act(async () => {
        jest.runAllTimers();
      });

      // Expect different color on initial mount.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('red');

      // Bump state.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Test another reload.
      patch(() => {
        function renderHello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1308-1324
```
          return App;
        },
        {shouldSuspend: false},
      );

      // We start with just the primary tree.
      expect(container.childNodes.length).toBe(1);
      const primaryChild = container.firstChild;
      expect(primaryChild.textContent).toBe('Content 0');
      expect(primaryChild.style.color).toBe('blue');
      expect(primaryChild.style.display).toBe('');

      // Bump primary content state.
      act(() => {
        primaryChild.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.childNodes.length).toBe(1);
```
### Line 1325-1334
```
      expect(container.childNodes[0]).toBe(primaryChild);
      expect(primaryChild.textContent).toBe('Content 1');
      expect(primaryChild.style.color).toBe('blue');
      expect(primaryChild.style.display).toBe('');

      // Perform a hot update.
      patch(() => {
        function Hello({children}) {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1343-1355
```
      expect(container.childNodes[0]).toBe(primaryChild);
      expect(primaryChild.textContent).toBe('Content 1');
      expect(primaryChild.style.color).toBe('green');
      expect(primaryChild.style.display).toBe('');

      // Now force the tree to suspend.
      render(() => AppV1, {shouldSuspend: true});

      // Expect to see two trees, one of them is hidden.
      expect(container.childNodes.length).toBe(2);
      expect(container.childNodes[0]).toBe(primaryChild);
      const fallbackChild = container.childNodes[1];
      expect(primaryChild.textContent).toBe('Content 1');
```
### Line 1357-1366
```
      expect(primaryChild.style.display).toBe('none');
      expect(fallbackChild.textContent).toBe('Fallback 0');
      expect(fallbackChild.style.color).toBe('green');
      expect(fallbackChild.style.display).toBe('');

      // Bump fallback state.
      act(() => {
        fallbackChild.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(container.childNodes.length).toBe(2);
```
### Line 1371-1380
```
      expect(primaryChild.style.display).toBe('none');
      expect(fallbackChild.textContent).toBe('Fallback 1');
      expect(fallbackChild.style.color).toBe('green');
      expect(fallbackChild.style.display).toBe('');

      // Perform a hot update.
      patch(() => {
        function Hello({children}) {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1384-1393
```
          );
        }
        $RefreshReg$(Hello, 'Hello');
      });

      // Colors inside both trees should change:
      expect(container.childNodes.length).toBe(2);
      expect(container.childNodes[0]).toBe(primaryChild);
      expect(container.childNodes[1]).toBe(fallbackChild);
      expect(primaryChild.textContent).toBe('Content 1');
```
### Line 1395-1412
```
      expect(primaryChild.style.display).toBe('none');
      expect(fallbackChild.textContent).toBe('Fallback 1');
      expect(fallbackChild.style.color).toBe('red');
      expect(fallbackChild.style.display).toBe('');

      // Only primary tree should exist now:
      render(() => AppV1, {shouldSuspend: false});
      expect(container.childNodes.length).toBe(1);
      expect(container.childNodes[0]).toBe(primaryChild);
      expect(primaryChild.textContent).toBe('Content 1');
      expect(primaryChild.style.color).toBe('red');
      expect(primaryChild.style.display).toBe('');

      // Perform a hot update.
      patch(() => {
        function Hello({children}) {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1447-1468
```
        return App;
      });

      expect(appRenders).toBe(1);

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // No re-renders from the top.
      expect(appRenders).toBe(1);

      // Perform a hot update for Hello only.
      patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1472-1495
```
          );
        }
        $RefreshReg$(Hello, 'Hello');
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Still no re-renders from the top.
      expect(appRenders).toBe(1);

      // Bump the state.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('2');

      // Still no re-renders from the top.
      expect(appRenders).toBe(1);
    }
  });

```
### Line 1563-1595
```
          return App;
        },
        {cond: false},
      );

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Switch the condition, flipping inner content.
      // This should reset the state.
      render(() => AppV1, {cond: true});
      const el2 = container.firstChild;
      expect(el2).not.toBe(el);
      expect(el2.textContent).toBe('0');
      expect(el2.style.color).toBe('blue');

      // Bump it again.
      act(() => {
        el2.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el2.textContent).toBe('1');

      // Perform a hot update for both inner components.
      patch(() => {
        function Hello1() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1608-1622
```
          );
        }
        $RefreshReg$(Hello2, 'Hello2');
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el2);
      expect(el2.textContent).toBe('1');
      expect(el2.style.color).toBe('red');

      // Flip the condition again.
      render(() => AppV1, {cond: false});
      const el3 = container.firstChild;
      expect(el3).not.toBe(el2);
      expect(el3.textContent).toBe('0');
```
### Line 1634-1657
```
              {val}
            </p>
          );
        }
        $RefreshReg$(Hello, 'Hello');
        // When this changes, we'll expect a remount:
        $RefreshSig$(Hello, '1');
        return Hello;
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update.
      let HelloV2 = patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1659-1678
```
              {val}
            </p>
          );
        }
        $RefreshReg$(Hello, 'Hello');
        // The signature hasn't changed since the last time:
        $RefreshSig$(Hello, '1');
        return Hello;
      });

      // Assert the state was preserved but color changed.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('1');
      expect(el.style.color).toBe('red');

      // Perform a hot update.
      let HelloV3 = patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1679-1709
```
            <p style={{color: 'yellow'}} onClick={() => setVal(val + 1)}>
              {val}
            </p>
          );
        }
        // We're changing the signature now so it will remount:
        $RefreshReg$(Hello, 'Hello');
        $RefreshSig$(Hello, '2');
        return Hello;
      });

      // Expect a remount.
      expect(container.firstChild).not.toBe(el);
      const newEl = container.firstChild;
      expect(newEl.textContent).toBe('0');
      expect(newEl.style.color).toBe('yellow');

      // Bump state again.
      act(() => {
        newEl.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(newEl.textContent).toBe('1');
      expect(newEl.style.color).toBe('yellow');

      // Perform top-down renders with both fresh and stale types.
      // Neither should change the state or color.
      // They should always resolve to the latest version.
      render(() => HelloV1);
      render(() => HelloV2);
      render(() => HelloV3);
      render(() => HelloV2);
```
### Line 1710-1719
```
      render(() => HelloV1);
      expect(container.firstChild).toBe(newEl);
      expect(newEl.textContent).toBe('1');
      expect(newEl.style.color).toBe('yellow');

      // Verify we can patch again while preserving the signature.
      patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1720-1729
```
            <p style={{color: 'purple'}} onClick={() => setVal(val + 1)}>
              {val}
            </p>
          );
        }
        // Same signature as last time.
        $RefreshReg$(Hello, 'Hello');
        $RefreshSig$(Hello, '2');
        return Hello;
      });
```
### Line 1730-1739
```

      expect(container.firstChild).toBe(newEl);
      expect(newEl.textContent).toBe('1');
      expect(newEl.style.color).toBe('purple');

      // Check removing the signature also causes a remount.
      patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 1740-1754
```
            <p style={{color: 'orange'}} onClick={() => setVal(val + 1)}>
              {val}
            </p>
          );
        }
        // No signature this time.
        $RefreshReg$(Hello, 'Hello');
        return Hello;
      });

      // Expect a remount.
      expect(container.firstChild).not.toBe(newEl);
      const finalEl = container.firstChild;
      expect(finalEl.textContent).toBe('0');
      expect(finalEl.style.color).toBe('orange');
```
### Line 1768-1778
```

      const Bailout = React.memo(({children}) => {
        return children;
      });

      // Each of those renders three instances of HelloV1,
      // but in different ways.
      let trees = [
        <div>
          <HelloV1 />
          <div>
```
### Line 1881-1900
```
            </Bailout>
          </HelloV1>
        </HelloV1>,
      ];

      // First, check that each tree handles remounts in isolation.
      ReactDOM.render(null, container);
      for (let i = 0; i < trees.length; i++) {
        runRemountingStressTest(trees[i]);
      }

      // Then check that each tree is resilient to updates from another tree.
      for (let i = 0; i < trees.length; i++) {
        for (let j = 0; j < trees.length; j++) {
          ReactDOM.render(null, container);
          // Intentionally don't clean up between the tests:
          runRemountingStressTest(trees[i]);
          runRemountingStressTest(trees[j]);
          runRemountingStressTest(trees[i]);
        }
```
### Line 1912-1927
```
      return Hello;
    });

    ReactDOM.render(tree, container);
    const elements = container.querySelectorAll('section');
    // Each tree above produces exactly three <section> elements:
    expect(elements.length).toBe(3);
    elements.forEach(el => {
      expect(el.dataset.color).toBe('blue');
    });

    // Patch color without changing the signature.
    patch(() => {
      function Hello({children}) {
        return <section data-color="red">{children}</section>;
      }
```
### Line 1931-1946
```
    });

    const elementsAfterPatch = container.querySelectorAll('section');
    expect(elementsAfterPatch.length).toBe(3);
    elementsAfterPatch.forEach((el, index) => {
      // The signature hasn't changed so we expect DOM nodes to stay the same.
      expect(el).toBe(elements[index]);
      // However, the color should have changed:
      expect(el.dataset.color).toBe('red');
    });

    // Patch color *and* change the signature.
    patch(() => {
      function Hello({children}) {
        return <section data-color="orange">{children}</section>;
      }
```
### Line 1950-1965
```
    });

    const elementsAfterRemount = container.querySelectorAll('section');
    expect(elementsAfterRemount.length).toBe(3);
    elementsAfterRemount.forEach((el, index) => {
      // The signature changed so we expect DOM nodes to be different.
      expect(el).not.toBe(elements[index]);
      // They should all be using the new color:
      expect(el.dataset.color).toBe('orange');
    });

    // Now patch color but *don't* change the signature.
    patch(() => {
      function Hello({children}) {
        return <section data-color="black">{children}</section>;
      }
```
### Line 1968-1983
```
      return Hello;
    });

    expect(container.querySelectorAll('section').length).toBe(3);
    container.querySelectorAll('section').forEach((el, index) => {
      // The signature didn't change so DOM nodes should stay the same.
      expect(el).toBe(elementsAfterRemount[index]);
      // They should all be using the new color:
      expect(el.dataset.color).toBe('black');
    });

    // Do another render just in case.
    ReactDOM.render(tree, container);
    expect(container.querySelectorAll('section').length).toBe(3);
    container.querySelectorAll('section').forEach((el, index) => {
      expect(el).toBe(elementsAfterRemount[index]);
```
### Line 2077-2086
```
  });

  it('can remount on signature change within a suspense node', () => {
    if (__DEV__) {
      testRemountingWithWrapper(Hello => {
        // TODO: we'll probably want to test fallback trees too.
        const child = (
          <React.Suspense>
            <Hello />
          </React.Suspense>
```
### Line 2165-2191
```
            {val}
          </p>
        );
      }
      $RefreshReg$(Hello, 'Hello');
      // When this changes, we'll expect a remount:
      $RefreshSig$(Hello, '1');

      // Use the passed wrapper.
      // This will be different in every test.
      return wrap(Hello);
    });

    // Bump the state before patching.
    const el = container.firstChild;
    expect(el.textContent).toBe('0');
    expect(el.style.color).toBe('blue');
    act(() => {
      el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
    });
    expect(el.textContent).toBe('1');

    // Perform a hot update that doesn't remount.
    patch(() => {
      function Hello() {
        const [val, setVal] = React.useState(0);
        return (
```
### Line 2193-2212
```
            {val}
          </p>
        );
      }
      $RefreshReg$(Hello, 'Hello');
      // The signature hasn't changed since the last time:
      $RefreshSig$(Hello, '1');
      return Hello;
    });

    // Assert the state was preserved but color changed.
    expect(container.firstChild).toBe(el);
    expect(el.textContent).toBe('1');
    expect(el.style.color).toBe('red');

    // Perform a hot update that remounts.
    patch(() => {
      function Hello() {
        const [val, setVal] = React.useState(0);
        return (
```
### Line 2213-2241
```
          <p style={{color: 'yellow'}} onClick={() => setVal(val + 1)}>
            {val}
          </p>
        );
      }
      // We're changing the signature now so it will remount:
      $RefreshReg$(Hello, 'Hello');
      $RefreshSig$(Hello, '2');
      return Hello;
    });

    // Expect a remount.
    expect(container.firstChild).not.toBe(el);
    const newEl = container.firstChild;
    expect(newEl.textContent).toBe('0');
    expect(newEl.style.color).toBe('yellow');

    // Bump state again.
    act(() => {
      newEl.dispatchEvent(new MouseEvent('click', {bubbles: true}));
    });
    expect(newEl.textContent).toBe('1');
    expect(newEl.style.color).toBe('yellow');

    // Verify we can patch again while preserving the signature.
    patch(() => {
      function Hello() {
        const [val, setVal] = React.useState(0);
        return (
```
### Line 2242-2251
```
          <p style={{color: 'purple'}} onClick={() => setVal(val + 1)}>
            {val}
          </p>
        );
      }
      // Same signature as last time.
      $RefreshReg$(Hello, 'Hello');
      $RefreshSig$(Hello, '2');
      return Hello;
    });
```
### Line 2252-2261
```

    expect(container.firstChild).toBe(newEl);
    expect(newEl.textContent).toBe('1');
    expect(newEl.style.color).toBe('purple');

    // Check removing the signature also causes a remount.
    patch(() => {
      function Hello() {
        const [val, setVal] = React.useState(0);
        return (
```
### Line 2262-2276
```
          <p style={{color: 'orange'}} onClick={() => setVal(val + 1)}>
            {val}
          </p>
        );
      }
      // No signature this time.
      $RefreshReg$(Hello, 'Hello');
      return Hello;
    });

    // Expect a remount.
    expect(container.firstChild).not.toBe(newEl);
    const finalEl = container.firstChild;
    expect(finalEl.textContent).toBe('0');
    expect(finalEl.style.color).toBe('orange');
```
### Line 2298-2307
```
        }
        $RefreshReg$(Hello, 'Hello');
        return Hello;
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      expect(useEffectWithEmptyArrayCalls).toBe(1); // useEffect ran
```
### Line 2309-2318
```
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('2'); // val * 2
      expect(useEffectWithEmptyArrayCalls).toBe(1); // useEffect didn't re-run

      // Perform a hot update.
      act(() => {
        patch(() => {
          function Hello() {
            const [val, setVal] = React.useState(0);
```
### Line 2332-2347
```
          $RefreshReg$(Hello, 'Hello');
          return Hello;
        });
      });

      // Assert the state was preserved but memo was evicted.
      expect(container.firstChild).toBe(el);
      expect(el.textContent).toBe('10'); // val * 10
      expect(el.style.color).toBe('red');
      expect(useEffectWithEmptyArrayCalls).toBe(2); // useEffect re-ran

      // This should fire the new callback which decreases the counter.
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('0');
```
### Line 2348-2357
```
      expect(el.style.color).toBe('red');
      expect(useEffectWithEmptyArrayCalls).toBe(2); // useEffect didn't re-run
    }
  });

  // This pattern is inspired by useSubscription and similar mechanisms.
  it('does not get into infinite loops during render phase updates', () => {
    if (__DEV__) {
      render(() => {
        function Hello() {
```
### Line 2368-2384
```

      const el = container.firstChild;
      expect(el.textContent).toBe('10');
      expect(el.style.color).toBe('blue');

      // Perform a hot update.
      act(() => {
        patch(() => {
          function Hello() {
            const source = React.useMemo(() => ({value: 20}), []);
            const [state, setState] = React.useState({value: null});
            if (state !== source) {
              // This should perform a single render-phase update.
              setState(source);
            }
            return <p style={{color: 'red'}}>{state.value}</p>;
          }
```
### Line 2426-2435
```
      expect(Scheduler).toFlushAndYieldThrough(['App#layout']);
      const el = container.firstChild;
      expect(el.hidden).toBe(true);
      expect(el.firstChild).toBe(null); // Offscreen content not flushed yet.

      // Perform a hot update.
      patch(() => {
        function Hello() {
          React.useLayoutEffect(() => {
            Scheduler.unstable_yieldValue('Hello#layout');
```
### Line 2442-2456
```
          );
        }
        $RefreshReg$(Hello, 'Hello');
      });

      // It's still offscreen so we don't see anything.
      expect(container.firstChild).toBe(el);
      expect(el.hidden).toBe(true);
      expect(el.firstChild).toBe(null);

      // Process the offscreen updates.
      expect(Scheduler).toFlushAndYieldThrough(['Hello#layout']);
      expect(container.firstChild).toBe(el);
      expect(el.firstChild.textContent).toBe('0');
      expect(el.firstChild.style.color).toBe('red');
```
### Line 2460-2469
```
      expect(el.firstChild.style.color).toBe('red');
      expect(Scheduler).toFlushAndYieldThrough(['Hello#layout']);
      expect(el.firstChild.textContent).toBe('1');
      expect(el.firstChild.style.color).toBe('red');

      // Hot reload while we're offscreen.
      patch(() => {
        function Hello() {
          React.useLayoutEffect(() => {
            Scheduler.unstable_yieldValue('Hello#layout');
```
### Line 2476-2490
```
          );
        }
        $RefreshReg$(Hello, 'Hello');
      });

      // It's still offscreen so we don't see the updates.
      expect(container.firstChild).toBe(el);
      expect(el.firstChild.textContent).toBe('1');
      expect(el.firstChild.style.color).toBe('red');

      // Process the offscreen updates.
      expect(Scheduler).toFlushAndYieldThrough(['Hello#layout']);
      expect(container.firstChild).toBe(el);
      expect(el.firstChild.textContent).toBe('1');
      expect(el.firstChild.style.color).toBe('orange');
```
### Line 2529-2538
```

      expect(container.innerHTML).toBe('<p>A</p><h1>Hi</h1><p>B</p>');
      const firstP = container.firstChild;
      const secondP = firstP.nextSibling.nextSibling;

      // Perform a hot update that fails.
      patch(() => {
        function Hello() {
          throw new Error('No');
        }
```
### Line 2541-2563
```

      expect(container.innerHTML).toBe('<p>A</p><h1>Oops: No</h1><p>B</p>');
      expect(container.firstChild).toBe(firstP);
      expect(container.firstChild.nextSibling.nextSibling).toBe(secondP);

      // Perform a hot update that fixes the error.
      patch(() => {
        function Hello() {
          return <h1>Fixed!</h1>;
        }
        $RefreshReg$(Hello, 'Hello');
      });

      // This should remount the error boundary (but not anything above it).
      expect(container.innerHTML).toBe('<p>A</p><h1>Fixed!</h1><p>B</p>');
      expect(container.firstChild).toBe(firstP);
      expect(container.firstChild.nextSibling.nextSibling).toBe(secondP);

      // Verify next hot reload doesn't remount anything.
      const helloNode = container.firstChild.nextSibling;
      patch(() => {
        function Hello() {
          return <h1>Nice.</h1>;
```
### Line 2607-2616
```

      expect(container.innerHTML).toBe('<p>A</p><h1>Hi</h1><p>B</p>');
      const firstP = container.firstChild;
      const secondP = firstP.nextSibling.nextSibling;

      // Perform a hot update that fails.
      patch(() => {
        function Hello() {
          throw new Error('No');
        }
```
### Line 2619-2641
```

      expect(container.innerHTML).toBe('<p>A</p><h1>Oops: No</h1><p>B</p>');
      expect(container.firstChild).toBe(firstP);
      expect(container.firstChild.nextSibling.nextSibling).toBe(secondP);

      // Perform a hot update that fixes the error.
      patch(() => {
        function Hello() {
          return <h1>Fixed!</h1>;
        }
        $RefreshReg$(Hello, 'Hello');
      });

      // This should remount the error boundary (but not anything above it).
      expect(container.innerHTML).toBe('<p>A</p><h1>Fixed!</h1><p>B</p>');
      expect(container.firstChild).toBe(firstP);
      expect(container.firstChild.nextSibling.nextSibling).toBe(secondP);

      // Verify next hot reload doesn't remount anything.
      const helloNode = container.firstChild.nextSibling;
      patch(() => {
        function Hello() {
          return <h1>Nice.</h1>;
```
### Line 2688-2697
```

      expect(container.innerHTML).toBe('<p>A</p><h1>Hi</h1><p>B</p>');
      const firstP = container.firstChild;
      const secondP = firstP.nextSibling.nextSibling;

      // Perform a hot update that fails.
      act(() => {
        patch(() => {
          function Hello() {
            const [x, setX] = React.useState('');
```
### Line 2706-2715
```
          $RefreshReg$(Hello, 'Hello');
        });
      });

      expect(container.innerHTML).toBe('<p>A</p><h1>Hi</h1><p>B</p>');
      // Run timeout inside effect:
      act(() => {
        jest.runAllTimers();
      });
      expect(container.innerHTML).toBe(
```
### Line 2716-2725
```
        '<p>A</p><h1>Oops: x.slice is not a function</h1><p>B</p>',
      );
      expect(container.firstChild).toBe(firstP);
      expect(container.firstChild.nextSibling.nextSibling).toBe(secondP);

      // Perform a hot update that fixes the error.
      act(() => {
        patch(() => {
          function Hello() {
            const [x] = React.useState('');
```
### Line 2729-2743
```
          }
          $RefreshReg$(Hello, 'Hello');
        });
      });

      // This should remount the error boundary (but not anything above it).
      expect(container.innerHTML).toBe('<p>A</p><h1>Fixed!</h1><p>B</p>');
      expect(container.firstChild).toBe(firstP);
      expect(container.firstChild.nextSibling.nextSibling).toBe(secondP);

      // Verify next hot reload doesn't remount anything.
      const helloNode = container.firstChild.nextSibling;
      act(() => {
        patch(() => {
          function Hello() {
```
### Line 2753-2763
```
      expect(container.firstChild.nextSibling).toBe(helloNode);
      expect(helloNode.textContent).toBe('Nice.');
    }
  });

  // TODO: we can make this recoverable in the future
  // if we add a way to track the last attempted element.
  it('records an unrecoverable error if a root fails on mount', () => {
    if (__DEV__) {
      expect(ReactFreshRuntime.hasUnrecoverableErrors()).toBe(false);
      expect(() => {
```
### Line 2786-2796
```
        return Hello;
      });
      expect(container.innerHTML).toBe('<h1>Hi</h1>');
      expect(ReactFreshRuntime.hasUnrecoverableErrors()).toBe(false);

      // Perform a hot update that fails.
      // This removes the root.
      expect(() => {
        patch(() => {
          function Hello() {
            throw new Error('No');
```
### Line 2799-2808
```
        });
      }).toThrow('No');
      expect(container.innerHTML).toBe('');
      expect(ReactFreshRuntime.hasUnrecoverableErrors()).toBe(false);

      // A bad retry
      expect(() => {
        patch(() => {
          function Hello() {
            throw new Error('Not yet');
```
### Line 2811-2831
```
        });
      }).toThrow('Not yet');
      expect(container.innerHTML).toBe('');
      expect(ReactFreshRuntime.hasUnrecoverableErrors()).toBe(false);

      // Perform a hot update that fixes the error.
      patch(() => {
        function Hello() {
          return <h1>Fixed!</h1>;
        }
        $RefreshReg$(Hello, 'Hello');
      });
      // This should remount the root.
      expect(container.innerHTML).toBe('<h1>Fixed!</h1>');
      expect(ReactFreshRuntime.hasUnrecoverableErrors()).toBe(false);

      // Verify next hot reload doesn't remount anything.
      let helloNode = container.firstChild;
      patch(() => {
        function Hello() {
          return <h1>Nice.</h1>;
```
### Line 2834-2843
```
      });
      expect(container.firstChild).toBe(helloNode);
      expect(helloNode.textContent).toBe('Nice.');
      expect(ReactFreshRuntime.hasUnrecoverableErrors()).toBe(false);

      // Break again.
      expect(() => {
        patch(() => {
          function Hello() {
            throw new Error('Oops');
```
### Line 2846-2866
```
        });
      }).toThrow('Oops');
      expect(container.innerHTML).toBe('');
      expect(ReactFreshRuntime.hasUnrecoverableErrors()).toBe(false);

      // Perform a hot update that fixes the error.
      patch(() => {
        function Hello() {
          return <h1>At last.</h1>;
        }
        $RefreshReg$(Hello, 'Hello');
      });
      // This should remount the root.
      expect(container.innerHTML).toBe('<h1>At last.</h1>');
      expect(ReactFreshRuntime.hasUnrecoverableErrors()).toBe(false);

      // Check we don't attempt to reverse an intentional unmount.
      ReactDOM.unmountComponentAtNode(container);
      expect(container.innerHTML).toBe('');
      patch(() => {
        function Hello() {
```
### Line 2889-2916
```
                {this.state.count}
              </p>
            );
          }
        }
        // For classes, we wouldn't do this call via Babel plugin.
        // Instead, we'd do it at module boundaries.
        // Normally classes would get a different type and remount anyway,
        // but at module boundaries we may want to prevent propagation.
        // However we still want to force a remount and use latest version.
        $RefreshReg$(Hello, 'Hello');
        return Hello;
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update.
      let HelloV2 = patch(() => {
        class Hello extends React.Component {
          state = {count: 0};
          handleClick = () => {
```
### Line 2928-2937
```
        }
        $RefreshReg$(Hello, 'Hello');
        return Hello;
      });

      // It should have remounted the class.
      expect(container.firstChild).not.toBe(el);
      const newEl = container.firstChild;
      expect(newEl.textContent).toBe('0');
      expect(newEl.style.color).toBe('red');
```
### Line 2938-2947
```
      act(() => {
        newEl.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(newEl.textContent).toBe('1');

      // Now top-level renders of both types resolve to latest.
      render(() => HelloV1);
      render(() => HelloV2);
      expect(container.firstChild).toBe(newEl);
      expect(newEl.style.color).toBe('red');
```
### Line 2965-2974
```
        }
        $RefreshReg$(Hello, 'Hello');
        return Hello;
      });

      // It should have remounted the class again.
      expect(container.firstChild).not.toBe(el);
      const finalEl = container.firstChild;
      expect(finalEl.textContent).toBe('0');
      expect(finalEl.style.color).toBe('orange');
```
### Line 3073-3091
```
        }
        $RefreshReg$(Hello, 'Hello');
        return Hello;
      });

      // Bump the state before patching.
      const el = container.firstChild;
      expect(el.textContent).toBe('0');
      expect(el.style.color).toBe('blue');
      act(() => {
        el.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(el.textContent).toBe('1');

      // Perform a hot update that turns it into a class.
      let HelloV2 = patch(() => {
        class Hello extends React.Component {
          state = {count: 0};
          handleClick = () => {
```
### Line 3103-3112
```
        }
        $RefreshReg$(Hello, 'Hello');
        return Hello;
      });

      // It should have remounted.
      expect(container.firstChild).not.toBe(el);
      const newEl = container.firstChild;
      expect(newEl.textContent).toBe('0');
      expect(newEl.style.color).toBe('red');
```
### Line 3113-3129
```
      act(() => {
        newEl.dispatchEvent(new MouseEvent('click', {bubbles: true}));
      });
      expect(newEl.textContent).toBe('1');

      // Now top-level renders of both types resolve to latest.
      render(() => HelloV1);
      render(() => HelloV2);
      expect(container.firstChild).toBe(newEl);
      expect(newEl.style.color).toBe('red');
      expect(newEl.textContent).toBe('1');

      // Now convert it back to a function.
      let HelloV3 = patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 3134-3143
```
        }
        $RefreshReg$(Hello, 'Hello');
        return Hello;
      });

      // It should have remounted again.
      expect(container.firstChild).not.toBe(el);
      const finalEl = container.firstChild;
      expect(finalEl.textContent).toBe('0');
      expect(finalEl.style.color).toBe('orange');
```
### Line 3151-3160
```
      render(() => HelloV1);
      expect(container.firstChild).toBe(finalEl);
      expect(finalEl.style.color).toBe('orange');
      expect(finalEl.textContent).toBe('1');

      // Now that it's a function, verify edits keep state.
      patch(() => {
        function Hello() {
          const [val, setVal] = React.useState(0);
          return (
```
### Line 3253-3269
```
      testFindHostInstancesForFamilies(
        [childFamily],
        container.querySelectorAll('.Child'),
      );

      // When searching for both Parent and Child,
      // we'll stop visual highlighting at the Parent.
      testFindHostInstancesForFamilies(
        [parentFamily, childFamily],
        container.querySelectorAll('.Parent'),
      );

      // When we can't find host nodes, use the closest parent.
      testFindHostInstancesForFamilies(
        [emptyFamily],
        container.querySelectorAll('.App'),
      );
```
### Line 3280-3289
```
    });
  }

  it('can update multiple roots independently', () => {
    if (__DEV__) {
      // Declare the first version.
      const HelloV1 = () => {
        const [val, setVal] = React.useState(0);
        return (
          <p style={{color: 'blue'}} onClick={() => setVal(val + 1)}>
```
### Line 3291-3300
```
          </p>
        );
      };
      $RefreshReg$(HelloV1, 'Hello');

      // Perform a hot update before any roots exist.
      const HelloV2 = () => {
        const [val, setVal] = React.useState(0);
        return (
          <p style={{color: 'red'}} onClick={() => setVal(val + 1)}>
```
### Line 3303-3312
```
        );
      };
      $RefreshReg$(HelloV2, 'Hello');
      ReactFreshRuntime.performReactRefresh();

      // Mount three roots.
      let cont1 = document.createElement('div');
      let cont2 = document.createElement('div');
      let cont3 = document.createElement('div');
      document.body.appendChild(cont1);
```
### Line 3315-3332
```
      try {
        ReactDOM.render(<HelloV1 id={1} />, cont1);
        ReactDOM.render(<HelloV2 id={2} />, cont2);
        ReactDOM.render(<HelloV1 id={3} />, cont3);

        // Expect we see the V2 color.
        expect(cont1.firstChild.style.color).toBe('red');
        expect(cont2.firstChild.style.color).toBe('red');
        expect(cont3.firstChild.style.color).toBe('red');
        expect(cont1.firstChild.textContent).toBe('0');
        expect(cont2.firstChild.textContent).toBe('0');
        expect(cont3.firstChild.textContent).toBe('0');

        // Bump the state for each of them.
        act(() => {
          cont1.firstChild.dispatchEvent(
            new MouseEvent('click', {bubbles: true}),
          );
```
### Line 3342-3351
```
        expect(cont3.firstChild.style.color).toBe('red');
        expect(cont1.firstChild.textContent).toBe('1');
        expect(cont2.firstChild.textContent).toBe('1');
        expect(cont3.firstChild.textContent).toBe('1');

        // Perform another hot update.
        const HelloV3 = () => {
          const [val, setVal] = React.useState(0);
          return (
            <p style={{color: 'green'}} onClick={() => setVal(val + 1)}>
```
### Line 3354-3373
```
          );
        };
        $RefreshReg$(HelloV3, 'Hello');
        ReactFreshRuntime.performReactRefresh();

        // It should affect all roots.
        expect(cont1.firstChild.style.color).toBe('green');
        expect(cont2.firstChild.style.color).toBe('green');
        expect(cont3.firstChild.style.color).toBe('green');
        expect(cont1.firstChild.textContent).toBe('1');
        expect(cont2.firstChild.textContent).toBe('1');
        expect(cont3.firstChild.textContent).toBe('1');

        // Unmount the second root.
        ReactDOM.unmountComponentAtNode(cont2);
        // Make the first root throw and unmount on hot update.
        const HelloV4 = ({id}) => {
          if (id === 1) {
            throw new Error('Oops.');
          }
```
### Line 3381-3390
```
        $RefreshReg$(HelloV4, 'Hello');
        expect(() => {
          ReactFreshRuntime.performReactRefresh();
        }).toThrow('Oops.');

        // Still, we expect the last root to be updated.
        expect(cont1.innerHTML).toBe('');
        expect(cont2.innerHTML).toBe('');
        expect(cont3.firstChild.style.color).toBe('orange');
        expect(cont3.firstChild.textContent).toBe('1');
```
### Line 3394-3406
```
        document.body.removeChild(cont3);
      }
    }
  });

  // Module runtimes can use this to decide whether
  // to propagate an update up to the modules that imported it,
  // or to stop at the current module because it's a component.
  // This can't and doesn't need to be 100% precise.
  it('can detect likely component types', () => {
    function useTheme() {}
    function Widget() {}

```
### Line 3407-3420
```
    if (__DEV__) {
      expect(ReactFreshRuntime.isLikelyComponentType(false)).toBe(false);
      expect(ReactFreshRuntime.isLikelyComponentType(null)).toBe(false);
      expect(ReactFreshRuntime.isLikelyComponentType('foo')).toBe(false);

      // We need to hit a balance here.
      // If we lean towards assuming everything is a component,
      // editing modules that export plain functions won't trigger
      // a proper reload because we will bottle up the update.
      // So we're being somewhat conservative.
      expect(ReactFreshRuntime.isLikelyComponentType(() => {})).toBe(false);
      expect(ReactFreshRuntime.isLikelyComponentType(function() {})).toBe(
        false,
      );
```
### Line 3425-3442
```
      expect(ReactFreshRuntime.isLikelyComponentType(loadUser)).toBe(false);
      const useStore = () => {};
      expect(ReactFreshRuntime.isLikelyComponentType(useStore)).toBe(false);
      expect(ReactFreshRuntime.isLikelyComponentType(useTheme)).toBe(false);

      // These seem like function components.
      let Button = () => {};
      expect(ReactFreshRuntime.isLikelyComponentType(Button)).toBe(true);
      expect(ReactFreshRuntime.isLikelyComponentType(Widget)).toBe(true);
      let anon = (() => () => {})();
      anon.displayName = 'Foo';
      expect(ReactFreshRuntime.isLikelyComponentType(anon)).toBe(true);

      // These seem like class components.
      class Btn extends React.Component {}
      class PureBtn extends React.PureComponent {}
      expect(ReactFreshRuntime.isLikelyComponentType(Btn)).toBe(true);
      expect(ReactFreshRuntime.isLikelyComponentType(PureBtn)).toBe(true);
```
### Line 3444-3464
```
        ReactFreshRuntime.isLikelyComponentType(
          createReactClass({render() {}}),
        ),
      ).toBe(true);

      // These don't.
      class Figure {
        move() {}
      }
      expect(ReactFreshRuntime.isLikelyComponentType(Figure)).toBe(false);
      class Point extends Figure {}
      expect(ReactFreshRuntime.isLikelyComponentType(Point)).toBe(false);

      // Run the same tests without Babel.
      // This tests real arrow functions and classes, as implemented in Node.

      // eslint-disable-next-line no-new-func
      new Function(
        'global',
        'React',
        'ReactFreshRuntime',
```
### Line 3475-3502
```
        const useStore = () => {};
        expect(ReactFreshRuntime.isLikelyComponentType(useStore)).toBe(false);
        function useTheme() {}
        expect(ReactFreshRuntime.isLikelyComponentType(useTheme)).toBe(false);

        // These seem like function components.
        let Button = () => {};
        expect(ReactFreshRuntime.isLikelyComponentType(Button)).toBe(true);
        function Widget() {}
        expect(ReactFreshRuntime.isLikelyComponentType(Widget)).toBe(true);
        let anon = (() => () => {})();
        anon.displayName = 'Foo';
        expect(ReactFreshRuntime.isLikelyComponentType(anon)).toBe(true);

        // These seem like class components.
        class Btn extends React.Component {}
        class PureBtn extends React.PureComponent {}
        expect(ReactFreshRuntime.isLikelyComponentType(Btn)).toBe(true);
        expect(ReactFreshRuntime.isLikelyComponentType(PureBtn)).toBe(true);
        expect(
          ReactFreshRuntime.isLikelyComponentType(createReactClass({render() {}})),
        ).toBe(true);

        // These don't.
        class Figure {
          move() {}
        }
        expect(ReactFreshRuntime.isLikelyComponentType(Figure)).toBe(false);
```
### Line 3532-3540
```
      const update = ReactFreshRuntime.performReactRefresh();
      expect(update.updatedFamilies.size).toBe(1);
      expect(update.staleFamilies.size).toBe(0);
      const family = update.updatedFamilies.values().next().value;
      expect(family.current.name).toBe('HelloV2');
      // For example, we can use this to print a log of what was updated.
    }
  });
});
```

## _packages_react_devtools_shared_src_devtools_views_Profiler_SidebarInteractions_js

## _fixtures_dom_src_components_fixtures_number_inputs_index_js

## _packages_react_is_npm_index_js

## _scripts_bench_stats_js
### Line 18-27
```
  if (pctChange + ci95 < 0) {
    return chalk.green(text);
  } else if (pctChange - ci95 > 0) {
    return chalk.red(text);
  } else {
    // Statistically insignificant.
    return text;
  }
}

```
### Line 67-76
```
      let remoteMean;
      let remoteSem;
      if (remoteMasterResults) {
        remoteMean = remoteMasterResults.benchmarks[benchmark].averages[i].mean;
        remoteSem = remoteMasterResults.benchmarks[benchmark].averages[i].sem;
        // https://en.wikipedia.org/wiki/1.96 gives a 99% confidence interval.
        const ci95 = remoteSem * 1.96;
        row.push(
          chalk.white(+remoteMean.toFixed(2) + ' ms +- ' + ci95.toFixed(2))
        );
```

## _packages_react_reconciler_src_tests_ReactLazy_test_internal_js
### Line 51-60
```
    await Promise.resolve();

    expect(Scheduler).toFlushAndYield(['Hi']);
    expect(root).toMatchRenderedOutput('Hi');

    // Should not suspend on update
    root.update(
      <Suspense fallback={<Text text="Loading..." />}>
        <LazyText text="Hi again" />
      </Suspense>,
```
### Line 250-259
```
      'Did mount: A',
      'Did mount: B',
    ]);
    expect(root).toMatchRenderedOutput('AB');

    // Swap the position of A and B
    root.update(<Parent swap={true} />);
    expect(Scheduler).toFlushAndYield([
      'B',
      'A',
```
### Line 335-344
```
    await Promise.resolve();

    expect(Scheduler).toFlushAndYield(['Lazy', 'Sibling', 'A']);
    expect(root).toMatchRenderedOutput('SiblingA');

    // Lazy should not re-render
    stateful.current.setState({text: 'B'});
    expect(Scheduler).toFlushAndYield(['B']);
    expect(root).toMatchRenderedOutput('SiblingB');
  });
```
### Line 655-673
```
    );

    expect(Scheduler).toFlushAndYield(['Loading...']);
    expect(root).not.toMatchRenderedOutput('22');

    // Mount
    await Promise.resolve();
    expect(() => {
      Scheduler.unstable_flushAll();
    }).toWarnDev([
      'Invalid prop `inner` of type `string` supplied to `Add`, expected `number`.',
    ]);
    expect(root).toMatchRenderedOutput('22');

    // Update
    expect(() => {
      root.update(
        <Suspense fallback={<Text text="Loading..." />}>
          <LazyAdd inner={false} outer={false} />
```
### Line 678-688
```
      'Invalid prop `inner` of type `boolean` supplied to `Add`, expected `number`.',
    );
    expect(root).toMatchRenderedOutput('0');
  }

  // Note: all "with defaultProps" tests below also verify defaultProps works as expected.
  // If we ever delete or move propTypes-related tests, make sure not to delete these.
  it('respects propTypes on function component with defaultProps', async () => {
    function Add(props) {
      expect(props.innerWithDefault).toBe(42);
      return props.inner + props.outer;
```
### Line 824-833
```
    T.defaultProps = {
      text: 'Inner default text',
    };
    T = React.memo(T);
    T.propTypes = {
      // Should not be satisfied by the *inner* defaultProps.
      text: PropTypes.string.isRequired,
    };
    const LazyText = lazy(() => fakeImport(T));
    const root = ReactTestRenderer.create(
```
### Line 840-858
```
    );

    expect(Scheduler).toFlushAndYield(['Loading...']);
    expect(root).not.toMatchRenderedOutput('Inner default text');

    // Mount
    await Promise.resolve();
    expect(() => {
      expect(Scheduler).toFlushAndYield(['Inner default text']);
    }).toWarnDev(
      'The prop `text` is marked as required in `T`, but its value is `undefined`',
    );
    expect(root).toMatchRenderedOutput('Inner default text');

    // Update
    expect(() => {
      root.update(
        <Suspense fallback={<Text text="Loading..." />}>
          <LazyText text={null} />
```
### Line 936-945
```
    expect(Scheduler).toFlushAndYield(['Foo', 'forwardRef', 'Bar']);
    expect(root).toMatchRenderedOutput('FooBar');
    expect(ref.current).not.toBe(null);
  });

  // Regression test for #14310
  it('supports defaultProps defined on the memo() return value', async () => {
    const Add = React.memo(props => {
      return props.inner + props.outer;
    });
```
### Line 956-1015
```
      },
    );
    expect(Scheduler).toFlushAndYield(['Loading...']);
    expect(root).not.toMatchRenderedOutput('4');

    // Mount
    await Promise.resolve();
    expect(Scheduler).toFlushWithoutYielding();
    expect(root).toMatchRenderedOutput('4');

    // Update (shallowly equal)
    root.update(
      <Suspense fallback={<Text text="Loading..." />}>
        <LazyAdd outer={2} />
      </Suspense>,
    );
    expect(Scheduler).toFlushWithoutYielding();
    expect(root).toMatchRenderedOutput('4');

    // Update
    root.update(
      <Suspense fallback={<Text text="Loading..." />}>
        <LazyAdd outer={3} />
      </Suspense>,
    );
    expect(Scheduler).toFlushWithoutYielding();
    expect(root).toMatchRenderedOutput('5');

    // Update (shallowly equal)
    root.update(
      <Suspense fallback={<Text text="Loading..." />}>
        <LazyAdd outer={3} />
      </Suspense>,
    );
    expect(Scheduler).toFlushWithoutYielding();
    expect(root).toMatchRenderedOutput('5');

    // Update (explicit props)
    root.update(
      <Suspense fallback={<Text text="Loading..." />}>
        <LazyAdd outer={1} inner={1} />
      </Suspense>,
    );
    expect(Scheduler).toFlushWithoutYielding();
    expect(root).toMatchRenderedOutput('2');

    // Update (explicit props, shallowly equal)
    root.update(
      <Suspense fallback={<Text text="Loading..." />}>
        <LazyAdd outer={1} inner={1} />
      </Suspense>,
    );
    expect(Scheduler).toFlushWithoutYielding();
    expect(root).toMatchRenderedOutput('2');

    // Update
    root.update(
      <Suspense fallback={<Text text="Loading..." />}>
        <LazyAdd outer={1} />
      </Suspense>,
```
### Line 1040-1063
```
      },
    );
    expect(Scheduler).toFlushAndYield(['Loading...']);
    expect(root).not.toMatchRenderedOutput('4');

    // Mount
    await Promise.resolve();
    expect(Scheduler).toFlushWithoutYielding();
    expect(root).toMatchRenderedOutput('4');

    // Update
    root.update(
      <Suspense fallback={<Text text="Loading..." />}>
        <LazyAdd outer={3} />
      </Suspense>,
    );
    expect(Scheduler).toFlushWithoutYielding();
    expect(root).toMatchRenderedOutput('5');

    // Update
    root.update(
      <Suspense fallback={<Text text="Loading..." />}>
        <LazyAdd />
      </Suspense>,
```

## _scripts_rollup_shims_facebook_www_renderSubtreeIntoContainer_DO_NOT_USE_js

## _packages_react_dom_src_events_tests_SyntheticClipboardEvent_test_js
### Line 17-26
```

  beforeEach(() => {
    React = require('react');
    ReactDOM = require('react-dom');

    // The container has to be attached for events to fire.
    container = document.createElement('div');
    document.body.appendChild(container);
  });

```
### Line 33-42
```
    describe('clipboardData', () => {
      describe('when event has clipboardData', () => {
        it("returns event's clipboardData", () => {
          let expectedCount = 0;

          // Mock clipboardData since jsdom implementation doesn't have a constructor
          const clipboardData = {
            dropEffect: null,
            effectAllowed: null,
            files: null,
```

## _scripts_jest_matchers_reactTestMatchers_js
### Line 2-14
```

const JestReact = require('jest-react');
const SchedulerMatchers = require('./schedulerTestMatchers');

function captureAssertion(fn) {
  // Trick to use a Jest matcher inside another Jest matcher. `fn` contains an
  // assertion; if it throws, we capture the error and return it, so the stack
  // trace presented to the user points to the original assertion in the
  // test file.
  try {
    fn();
  } catch (error) {
    return {
```

## _packages_react_devtools_shared_src_tests_profilerContext_test_js
### Line 121-130
```
    function ContextReader() {
      context = React.useContext(ProfilerContext);
      return null;
    }

    // Profile but don't record any updates.
    await utils.actAsync(() => store.profilerStore.startProfiling());
    await utils.actAsync(() => {
      TestRenderer.create(
        <Contexts>
```
### Line 156-165
```
    const containerTwo = document.createElement('div');
    utils.act(() => ReactDOM.render(<Parent />, containerOne));
    utils.act(() => ReactDOM.render(<Parent />, containerTwo));
    expect(store).toMatchSnapshot('mounted');

    // Profile and record updates to both roots.
    await utils.actAsync(() => store.profilerStore.startProfiling());
    await utils.actAsync(() => ReactDOM.render(<Parent />, containerOne));
    await utils.actAsync(() => ReactDOM.render(<Parent />, containerTwo));
    await utils.actAsync(() => store.profilerStore.stopProfiling());
```
### Line 168-177
```
    function ContextReader() {
      context = React.useContext(ProfilerContext);
      return null;
    }

    // Select an element within the second root.
    await utils.actAsync(() =>
      TestRenderer.create(
        <Contexts
          defaultSelectedElementID={store.getElementIDAtIndex(3)}
```
### Line 197-206
```
    const containerTwo = document.createElement('div');
    utils.act(() => ReactDOM.render(<Parent />, containerOne));
    utils.act(() => ReactDOM.render(<Parent />, containerTwo));
    expect(store).toMatchSnapshot('mounted');

    // Profile and record updates to only the first root.
    await utils.actAsync(() => store.profilerStore.startProfiling());
    await utils.actAsync(() => ReactDOM.render(<Parent />, containerOne));
    await utils.actAsync(() => store.profilerStore.stopProfiling());

```
### Line 208-217
```
    function ContextReader() {
      context = React.useContext(ProfilerContext);
      return null;
    }

    // Select an element within the second root.
    await utils.actAsync(() =>
      TestRenderer.create(
        <Contexts
          defaultSelectedElementID={store.getElementIDAtIndex(3)}
```
### Line 219-228
```
          <ContextReader />
        </Contexts>,
      ),
    );

    // Verify the default profiling root is the first one.
    expect(context).not.toBeNull();
    expect(context.rootID).toBe(
      store.getRootIDForElement(((store.getElementIDAtIndex(0): any): number)),
    );
```
### Line 238-247
```
    const containerB = document.createElement('div');
    utils.act(() => ReactDOM.render(<Parent />, containerA));
    utils.act(() => ReactDOM.render(<Parent />, containerB));
    expect(store).toMatchSnapshot('mounted');

    // Profile and record updates.
    await utils.actAsync(() => store.profilerStore.startProfiling());
    await utils.actAsync(() => ReactDOM.render(<Parent />, containerA));
    await utils.actAsync(() => ReactDOM.render(<Parent />, containerB));
    await utils.actAsync(() => store.profilerStore.stopProfiling());
```
### Line 256-265
```
      return null;
    }

    const id = ((store.getElementIDAtIndex(3): any): number);

    // Select an element within the second root.
    await utils.actAsync(() =>
      TestRenderer.create(
        <Contexts defaultSelectedElementID={id} defaultSelectedElementIndex={3}>
          <ContextReader />
```
### Line 267-287
```
      ),
    );

    expect(selectedElementID).toBe(id);

    // Profile and record more updates to both roots
    await utils.actAsync(() => store.profilerStore.startProfiling());
    await utils.actAsync(() => ReactDOM.render(<Parent />, containerA));
    await utils.actAsync(() => ReactDOM.render(<Parent />, containerB));
    await utils.actAsync(() => store.profilerStore.stopProfiling());

    const otherID = ((store.getElementIDAtIndex(0): any): number);

    // Change the selected element within a the Components tab.
    utils.act(() => dispatch({type: 'SELECT_ELEMENT_AT_INDEX', payload: 0}));

    // Verify that the initial Profiler root selection is maintained.
    expect(selectedElementID).toBe(otherID);
    expect(context).not.toBeNull();
    expect(context.rootID).toBe(store.getRootIDForElement(id));

```
### Line 302-311
```
    expect(store).toMatchSnapshot('mounted');

    const parentID = ((store.getElementIDAtIndex(1): any): number);
    const childID = ((store.getElementIDAtIndex(2): any): number);

    // Profile and record updates.
    await utils.actAsync(() => store.profilerStore.startProfiling());
    await utils.actAsync(() =>
      ReactDOM.render(<GrandParent includeChild={true} />, container),
    );
```
### Line 331-348
```
        </Contexts>,
      ),
    );
    expect(selectedElementID).toBeNull();

    // Select an element in the Profiler tab and verify that the selection is synced to the Components tab.
    await utils.actAsync(() => context.selectFiber(parentID, 'Parent'));
    expect(selectedElementID).toBe(parentID);

    // We expect a "no element found" warning.
    // Let's hide it from the test console though.
    spyOn(console, 'warn');

    // Select an unmounted element and verify no Components tab selection doesn't change.
    await utils.actAsync(() => context.selectFiber(childID, 'Child'));
    expect(selectedElementID).toBe(parentID);

    expect(console.warn).toHaveBeenCalledWith(
```

## _packages_react_devtools_shared_src_devtools_views_TabBar_js

## _packages_react_dom_src_tests_ReactIdentity_test_js
### Line 85-95
```
    const detachedContainer = document.createElement('div');
    renderAComponentWithKeyIntoContainer("<'WEIRD/&\\key'>", detachedContainer);
  });

  it('should allow any character as a key, in an attached parent', () => {
    // This test exists to protect against implementation details that
    // incorrectly query escaped IDs using DOM tools like getElementById.
    const attachedContainer = document.createElement('div');
    document.body.appendChild(attachedContainer);

    renderAComponentWithKeyIntoContainer("<'WEIRD/&\\key'>", attachedContainer);
```
### Line 106-115
```

    renderAComponentWithKeyIntoContainer(h4x0rKey, attachedContainer);

    document.body.removeChild(attachedContainer);

    // If we get this far, make sure we haven't executed the code
    expect(window.YOUVEBEENH4X0RED).toBe(undefined);
  });

  it('should let restructured components retain their uniqueness', () => {
```

## _packages_react_reconciler_src_ReactFiberInstrumentation_js
### Line 5-17
```
 * LICENSE file in the root directory of this source tree.
 *
 * @flow
 */

// This lets us hook into Fiber to debug what it's doing.
// See https://github.com/facebook/react/pull/8033.
// This is not part of the public API, not even for React DevTools.
// You may only inject a debugTool if you work on React Fiber itself.
const ReactFiberInstrumentation = {
  debugTool: null,
};

```

## _packages_react_src_ReactCreateRef_js
### Line 6-15
```
 * @flow
 */

import type {RefObject} from 'shared/ReactTypes';

// an immutable object with a single mutable value
export function createRef(): RefObject {
  const refObject = {
    current: null,
  };
```

## _packages_react_dom_src_shared_CSSShorthandProperty_js
### Line 3-13
```
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// List derived from Gecko source code:
// https://github.com/mozilla/gecko-dev/blob/4e638efc71/layout/style/test/property_database.js
export const shorthandToLonghand = {
  animation: [
    'animationDelay',
    'animationDirection',
```

## _packages_scheduler_npm_umd_scheduler_development_js
### Line 10-19
```
/* eslint-disable max-len */

'use strict';

(function(global, factory) {
  // eslint-disable-next-line no-unused-expressions
  typeof exports === 'object' && typeof module !== 'undefined'
    ? (module.exports = factory(require('react')))
    : typeof define === 'function' && define.amd // eslint-disable-line no-undef
      ? define(['react'], factory) // eslint-disable-line no-undef
```

## _packages_react_stream_inline_typed_js
### Line 5-24
```
 * LICENSE file in the root directory of this source tree.
 *
 * @flow
 */

// This file must have the Flow annotation.
//
// This is the Flow-typed entry point for the renderer. It should not be
// imported directly in code. Instead, our Flow configuration uses this entry
// point for the currently checked renderer (the one you passed to `yarn flow`).
//
// For example, if you run `yarn flow dom`, `react-stream/inline.dom` points
// to this module (and thus will be considered Flow-typed). But other renderers
// (e.g. `react-test-renderer`) will see stream as untyped during the check.
//
// We can't make all entry points typed at the same time because different
// renderers have different host config types. So we check them one by one.
// We run Flow on all renderers on CI.

export * from './src/ReactFizzStreamer';
```

## _fixtures_ssr_src_components_Suspend_js
### Line 1-10
```
let promise = null;
let isResolved = false;

export default function Suspend({children}) {
  // This will suspend the content from rendering but only on the client.
  // This is used to demo a slow loading app.
  if (typeof window === 'object') {
    if (!isResolved) {
      if (promise === null) {
        promise = new Promise(resolve => {
```

## _packages_react_dom_src_tests_ReactLegacyErrorBoundaries_test_internal_js
### Line 12-21
```
let PropTypes;
let React;
let ReactDOM;
let ReactFeatureFlags;

// TODO: Refactor this test once componentDidCatch setState is deprecated.
describe('ReactLegacyErrorBoundaries', () => {
  let log;

  let BrokenConstructor;
```
### Line 556-565
```
      componentWillUnmount() {
        log.push('RetryErrorBoundary componentWillUnmount');
      }
      componentDidCatch(error) {
        log.push('RetryErrorBoundary componentDidCatch [!]');
        // In Fiber, calling setState() (and failing) is treated as a rethrow.
        this.setState({});
      }
    };

```
### Line 685-700
```
      'BothErrorBoundaries componentWillMount',
      'BothErrorBoundaries render success',
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // Both getDerivedStateFromError and componentDidCatch should be called
      'BothErrorBoundaries static getDerivedStateFromError',
      'BothErrorBoundaries componentWillMount',
      'BothErrorBoundaries render error',
      // Fiber mounts with null children before capturing error
      'BothErrorBoundaries componentDidMount',
      // Catch and render an error message
      'BothErrorBoundaries componentDidCatch',
      'BothErrorBoundaries componentWillUpdate',
      'BothErrorBoundaries render error',
      'BothErrorBoundaries componentDidUpdate',
```
### Line 719-730
```
      'ErrorBoundary componentWillMount',
      'ErrorBoundary render success',
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // Fiber mounts with null children before capturing error
      'ErrorBoundary componentDidMount',
      // Catch and render an error message
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
```
### Line 747-758
```
    expect(log).toEqual([
      'ErrorBoundary constructor',
      'ErrorBoundary componentWillMount',
      'ErrorBoundary render success',
      'BrokenConstructor constructor [!]',
      // Fiber mounts with null children before capturing error
      'ErrorBoundary componentDidMount',
      // Catch and render an error message
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
```
### Line 909-930
```
      'RetryErrorBoundary componentWillMount',
      'RetryErrorBoundary render',
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // In Fiber, failed error boundaries render null before attempting to recover
      'RetryErrorBoundary componentDidMount',
      'RetryErrorBoundary componentDidCatch [!]',
      'ErrorBoundary componentDidMount',
      // Retry
      'RetryErrorBoundary render',
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // This time, the error propagates to the higher boundary
      'RetryErrorBoundary componentWillUnmount',
      'ErrorBoundary componentDidCatch',
      // Render the error
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
    ]);
```
### Line 947-956
```
      'ErrorBoundary constructor',
      'ErrorBoundary componentWillMount',
      'ErrorBoundary render success',
      'BrokenComponentWillMountErrorBoundary constructor',
      'BrokenComponentWillMountErrorBoundary componentWillMount [!]',
      // The error propagates to the higher boundary
      'ErrorBoundary componentDidMount',
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
```
### Line 981-1000
```
      'BrokenRenderErrorBoundary componentWillMount',
      'BrokenRenderErrorBoundary render success',
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // The first error boundary catches the error
      // It adjusts state but throws displaying the message
      // Finish mounting with null children
      'BrokenRenderErrorBoundary componentDidMount',
      // Attempt to handle the error
      'BrokenRenderErrorBoundary componentDidCatch',
      'ErrorBoundary componentDidMount',
      'BrokenRenderErrorBoundary render error [!]',
      // Boundary fails with new error, propagate to next boundary
      'BrokenRenderErrorBoundary componentWillUnmount',
      // Attempt to handle the error again
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
```
### Line 1018-1043
```
    expect(container.firstChild.textContent).toBe('Caught an error: Hello.');
    expect(log).toEqual([
      'ErrorBoundary constructor',
      'ErrorBoundary componentWillMount',
      'ErrorBoundary render success',
      // Render first child
      'Normal constructor',
      'Normal componentWillMount',
      'Normal render',
      // Render second child (it throws)
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // Render third child, even though an earlier sibling threw.
      'Normal constructor',
      'Normal componentWillMount',
      'Normal render',
      // Finish mounting with null children
      'ErrorBoundary componentDidMount',
      // Handle the error
      'ErrorBoundary componentDidCatch',
      // Render the error message
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
    ]);
```
### Line 1069-1083
```
      'ErrorBoundary componentWillMount',
      'ErrorBoundary render success',
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // Handle error:
      // Finish mounting with null children
      'ErrorBoundary componentDidMount',
      // Handle the error
      'ErrorBoundary componentDidCatch',
      // Render the error message
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'Error message ref is set to [object HTMLDivElement]',
      'ErrorBoundary componentDidUpdate',
```
### Line 1109-1123
```
      'ErrorBoundary componentWillMount',
      'ErrorBoundary render success',
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // Handle error:
      // Finish mounting with null children
      'ErrorBoundary componentDidMount',
      // Handle the error
      'ErrorBoundary componentDidCatch',
      // Render the error message
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
    ]);
```
### Line 1176-1196
```
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render success',
      'Normal componentWillReceiveProps',
      'Normal componentWillUpdate',
      'Normal render',
      // Normal2 will attempt to mount:
      'Normal2 constructor',
      'Normal2 componentWillMount',
      'Normal2 render',
      // BrokenConstructor will abort rendering:
      'BrokenConstructor constructor [!]',
      // Finish updating with null children
      'Normal componentWillUnmount',
      'ErrorBoundary componentDidUpdate',
      // Handle the error
      'ErrorBoundary componentDidCatch',
      // Render the error message
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
    ]);
```
### Line 1224-1245
```
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render success',
      'Normal componentWillReceiveProps',
      'Normal componentWillUpdate',
      'Normal render',
      // Normal2 will attempt to mount:
      'Normal2 constructor',
      'Normal2 componentWillMount',
      'Normal2 render',
      // BrokenComponentWillMount will abort rendering:
      'BrokenComponentWillMount constructor',
      'BrokenComponentWillMount componentWillMount [!]',
      // Finish updating with null children
      'Normal componentWillUnmount',
      'ErrorBoundary componentDidUpdate',
      // Handle the error
      'ErrorBoundary componentDidCatch',
      // Render the error message
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
    ]);
```
### Line 1273-1288
```
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render success',
      'Normal componentWillReceiveProps',
      'Normal componentWillUpdate',
      'Normal render',
      // BrokenComponentWillReceiveProps will abort rendering:
      'BrokenComponentWillReceiveProps componentWillReceiveProps [!]',
      // Finish updating with null children
      'Normal componentWillUnmount',
      'BrokenComponentWillReceiveProps componentWillUnmount',
      'ErrorBoundary componentDidUpdate',
      // Handle the error
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
```
### Line 1317-1333
```
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render success',
      'Normal componentWillReceiveProps',
      'Normal componentWillUpdate',
      'Normal render',
      // BrokenComponentWillUpdate will abort rendering:
      'BrokenComponentWillUpdate componentWillReceiveProps',
      'BrokenComponentWillUpdate componentWillUpdate [!]',
      // Finish updating with null children
      'Normal componentWillUnmount',
      'BrokenComponentWillUpdate componentWillUnmount',
      'ErrorBoundary componentDidUpdate',
      // Handle the error
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
```
### Line 1362-1382
```
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render success',
      'Normal componentWillReceiveProps',
      'Normal componentWillUpdate',
      'Normal render',
      // Normal2 will attempt to mount:
      'Normal2 constructor',
      'Normal2 componentWillMount',
      'Normal2 render',
      // BrokenRender will abort rendering:
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // Finish updating with null children
      'Normal componentWillUnmount',
      'ErrorBoundary componentDidUpdate',
      // Handle the error
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
```
### Line 1425-1446
```
    expect(container.textContent).toBe('Caught an error: Hello.');
    expect(log).toEqual([
      'ErrorBoundary componentWillReceiveProps',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render success',
      // BrokenRender will abort rendering:
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // Finish updating with null children
      'Child1 ref is set to null',
      'ErrorBoundary componentDidUpdate',
      // Handle the error
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'Error message ref is set to [object HTMLDivElement]',
      // Child2 ref is never set because its mounting aborted
      'ErrorBoundary componentDidUpdate',
    ]);

    log.length = 0;
```
### Line 1472-1505
```
    expect(container.textContent).toBe('Caught an error: Hello.');
    expect(log).toEqual([
      'ErrorBoundary componentWillReceiveProps',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render success',
      // Update existing child:
      'BrokenComponentWillUnmount componentWillReceiveProps',
      'BrokenComponentWillUnmount componentWillUpdate',
      'BrokenComponentWillUnmount render',
      // Unmounting throws:
      'BrokenComponentWillUnmount componentWillUnmount [!]',
      // Fiber proceeds with lifecycles despite errors
      'Normal componentWillUnmount',
      // The components have updated in this phase
      'BrokenComponentWillUnmount componentDidUpdate',
      'ErrorBoundary componentDidUpdate',
      // Now that commit phase is done, Fiber unmounts the boundary's children
      'BrokenComponentWillUnmount componentWillUnmount [!]',
      'ErrorBoundary componentDidCatch',
      // The initial render was aborted, so
      // Fiber retries from the root.
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary componentDidUpdate',
      // The second willUnmount error should be captured and logged, too.
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      // Render an error now (stack will do it later)
      'ErrorBoundary render error',
      // Attempt to unmount previous child:
      // Done
      'ErrorBoundary componentDidUpdate',
    ]);

    log.length = 0;
```
### Line 1531-1566
```
    expect(container.textContent).toBe('Caught an error: Hello.');
    expect(log).toEqual([
      'ErrorBoundary componentWillReceiveProps',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render success',
      // Update existing children:
      'Normal componentWillReceiveProps',
      'Normal componentWillUpdate',
      'Normal render',
      'BrokenComponentWillUnmount componentWillReceiveProps',
      'BrokenComponentWillUnmount componentWillUpdate',
      'BrokenComponentWillUnmount render',
      // Unmounting throws:
      'BrokenComponentWillUnmount componentWillUnmount [!]',
      // Fiber proceeds with lifecycles despite errors
      'BrokenComponentWillUnmount componentDidUpdate',
      'Normal componentDidUpdate',
      'ErrorBoundary componentDidUpdate',
      'Normal componentWillUnmount',
      'BrokenComponentWillUnmount componentWillUnmount [!]',
      // Now that commit phase is done, Fiber handles errors
      'ErrorBoundary componentDidCatch',
      // The initial render was aborted, so
      // Fiber retries from the root.
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary componentDidUpdate',
      // The second willUnmount error should be captured and logged, too.
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      // Render an error now (stack will do it later)
      'ErrorBoundary render error',
      // Done
      'ErrorBoundary componentDidUpdate',
    ]);

    log.length = 0;
```
### Line 1602-1632
```
      </ErrorBoundary>,
      container,
    );
    expect(container.textContent).toBe('Caught an inner error: Hello.');
    expect(log).toEqual([
      // Update outer boundary
      'OuterErrorBoundary componentWillReceiveProps',
      'OuterErrorBoundary componentWillUpdate',
      'OuterErrorBoundary render success',
      // Update inner boundary
      'InnerErrorBoundary componentWillReceiveProps',
      'InnerErrorBoundary componentWillUpdate',
      'InnerErrorBoundary render success',
      // Try unmounting child
      'BrokenComponentWillUnmount componentWillUnmount [!]',
      // Fiber proceeds with lifecycles despite errors
      // Inner and outer boundaries have updated in this phase
      'InnerErrorBoundary componentDidUpdate',
      'OuterErrorBoundary componentDidUpdate',
      // Now that commit phase is done, Fiber handles errors
      // Only inner boundary receives the error:
      'InnerErrorBoundary componentDidCatch',
      'InnerErrorBoundary componentWillUpdate',
      // Render an error now
      'InnerErrorBoundary render error',
      // In Fiber, this was a local update to the
      // inner boundary so only its hook fires
      'InnerErrorBoundary componentDidUpdate',
    ]);

    log.length = 0;
```
### Line 1650-1662
```
      <ErrorBoundary>
        <Normal />
      </ErrorBoundary>,
      container,
    );
    // Error boundary doesn't retry by itself:
    expect(container.textContent).toBe('Caught an error: Hello.');

    // Force the success path:
    log.length = 0;
    ReactDOM.render(
      <ErrorBoundary forceRetry={true}>
        <Normal />
```
### Line 1666-1679
```
    expect(container.textContent).not.toContain('Caught an error');
    expect(log).toEqual([
      'ErrorBoundary componentWillReceiveProps',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render success',
      // Mount children:
      'Normal constructor',
      'Normal componentWillMount',
      'Normal render',
      // Finalize updates:
      'Normal componentDidMount',
      'ErrorBoundary componentDidUpdate',
    ]);

```
### Line 1862-1893
```
      'BrokenComponentDidMount componentWillMount',
      'BrokenComponentDidMount render',
      'LastChild constructor',
      'LastChild componentWillMount',
      'LastChild render',
      // Start flushing didMount queue
      'Normal componentDidMount',
      'BrokenComponentWillUnmount componentDidMount',
      'BrokenComponentDidMount componentDidMount [!]',
      // Continue despite the error
      'LastChild componentDidMount',
      'ErrorBoundary componentDidMount',
      // Now we are ready to handle the error
      // Safely unmount every child
      'BrokenComponentWillUnmount componentWillUnmount [!]',
      // Continue unmounting safely despite any errors
      'Normal componentWillUnmount',
      'BrokenComponentDidMount componentWillUnmount',
      'LastChild componentWillUnmount',
      // Handle the error
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      // The willUnmount error should be captured and logged, too.
      'ErrorBoundary componentDidUpdate',
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      // The update has finished
      'ErrorBoundary componentDidUpdate',
    ]);

    log.length = 0;
```
### Line 1916-1929
```
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render success',
      'BrokenComponentDidUpdate componentWillReceiveProps',
      'BrokenComponentDidUpdate componentWillUpdate',
      'BrokenComponentDidUpdate render',
      // All lifecycles run
      'BrokenComponentDidUpdate componentDidUpdate [!]',
      'ErrorBoundary componentDidUpdate',
      'BrokenComponentDidUpdate componentWillUnmount',
      // Then, error is handled
      'ErrorBoundary componentDidCatch',
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
```
### Line 1953-1967
```
      'ErrorBoundary render success',
      'BrokenComponentDidMountErrorBoundary constructor',
      'BrokenComponentDidMountErrorBoundary componentWillMount',
      'BrokenComponentDidMountErrorBoundary render success',
      'BrokenComponentDidMountErrorBoundary componentDidMount [!]',
      // Fiber proceeds with the hooks
      'ErrorBoundary componentDidMount',
      'BrokenComponentDidMountErrorBoundary componentWillUnmount',
      // The error propagates to the higher boundary
      'ErrorBoundary componentDidCatch',
      // Fiber retries from the root
      'ErrorBoundary componentWillUpdate',
      'ErrorBoundary render error',
      'ErrorBoundary componentDidUpdate',
    ]);
```
### Line 2017-2026
```

    expect(container.firstChild.textContent).toBe(
      'Caught an unmounting error: E2.' + 'Caught an updating error: E4.',
    );
    expect(log).toEqual([
      // Begin update phase
      'OuterErrorBoundary componentWillReceiveProps',
      'OuterErrorBoundary componentWillUpdate',
      'OuterErrorBoundary render success',
      'InnerUnmountBoundary componentWillReceiveProps',
```
### Line 2027-2055
```
      'InnerUnmountBoundary componentWillUpdate',
      'InnerUnmountBoundary render success',
      'InnerUpdateBoundary componentWillReceiveProps',
      'InnerUpdateBoundary componentWillUpdate',
      'InnerUpdateBoundary render success',
      // First come the updates
      'BrokenComponentDidUpdate componentWillReceiveProps',
      'BrokenComponentDidUpdate componentWillUpdate',
      'BrokenComponentDidUpdate render',
      'BrokenComponentDidUpdate componentWillReceiveProps',
      'BrokenComponentDidUpdate componentWillUpdate',
      'BrokenComponentDidUpdate render',
      // We're in commit phase now, deleting
      'BrokenComponentWillUnmount componentWillUnmount [!]',
      'BrokenComponentWillUnmount componentWillUnmount [!]',
      // Continue despite errors, handle them after commit is done
      'InnerUnmountBoundary componentDidUpdate',
      // We're still in commit phase, now calling update lifecycles
      'BrokenComponentDidUpdate componentDidUpdate [!]',
      // Again, continue despite errors, we'll handle them later
      'BrokenComponentDidUpdate componentDidUpdate [!]',
      'InnerUpdateBoundary componentDidUpdate',
      'OuterErrorBoundary componentDidUpdate',
      // After the commit phase, attempt to recover from any errors that
      // were captured
      'BrokenComponentDidUpdate componentWillUnmount',
      'BrokenComponentDidUpdate componentWillUnmount',
      'InnerUnmountBoundary componentDidCatch',
      'InnerUnmountBoundary componentDidCatch',
```
### Line 2125-2137
```
      'NoopErrorBoundary componentWillMount',
      'NoopErrorBoundary render',
      'BrokenRender constructor',
      'BrokenRender componentWillMount',
      'BrokenRender render [!]',
      // In Fiber, noop error boundaries render null
      'NoopErrorBoundary componentDidMount',
      'NoopErrorBoundary componentDidCatch',
      // Nothing happens.
    ]);

    log.length = 0;
    ReactDOM.unmountComponentAtNode(container);
```
### Line 2160-2170
```
      }
    }

    const container = document.createElement('div');
    try {
      // Here, we test the behavior where there is no error boundary and we
      // delegate to the host root.
      ReactDOM.render(<Parent />, container);
    } catch (e) {
      if (e.message !== 'parent sad' && e.message !== 'child sad') {
        throw e;
```
### Line 2171-2180
```
      }
      caughtError = e;
    }

    expect(errors).toEqual(['child sad', 'parent sad']);
    // Error should be the first thrown
    expect(caughtError.message).toBe('child sad');
  });

  it('propagates uncaught error inside unbatched initial mount', () => {
```
### Line 2223-2231
```
      }
      caughtError = e;
    }

    expect(errors).toEqual(['child sad', 'parent sad']);
    // Error should be the first thrown
    expect(caughtError.message).toBe('child sad');
  });
});
```

# Issues
## 1580
Title:
```

        setState() in componentWillReceiveProps() does NOT update the state in callback
      
```
Author:
```
velsa
```
Text:
```

The example jsfiddle is here: http://jsfiddle.net/kka99/
As far as I understand this is not a proper behavior.

```
Author:
```
syranide
```
Text:
```

So the problem seems to be that componentWillReceiveProps is called with batchingStrategy.isBatchingUpdates = false which means that the callback is executed immediately, rather than queued as the new state is.

```
Author:
```
sophiebits
```
Text:
```

#1363 fixes this.

```
Author:
```
sophiebits
```
Text:
```

It was merged! This should work now in master.

```
Author:
```
spudly
```
Text:
```

Just spent hours trying to figure out why my code doesn't work. Thanks for the fix! Hope it makes it into a release soon.

```

## 2400
Title:
```

        ReactDOMInput will throw error when use mootools together
      
```
Author:
```
oceanjack
```
Text:
```

error stack




first it in react-with-addon.js

function checkPropTypes(componentName, propTypes, props, location) {
  for (var propName in propTypes) {
    if (propTypes.hasOwnProperty(propName)) {
      var error;
      // Prop type validation may throw. In case they do, we don't want to
      // fail the render phase where it didn't fail before. So we log it.
      // After these have been cleaned up, we'll let them throw.
      try {
        error = propTypes\[propName\](props, propName, componentName, location);


componentName is ReactDOMInput
propName is 'onChange'





and then it jump to this func in mootools

Function.implement({create: function(b) {
    var a = this;
    b = b || {};
    return function(d) {
      var c = b.arguments;
      c = (c != null) ? Array.from(c) : Array.slice(arguments, (b.event) ? 1 : 0);
      if (b.event) {
        c = [d || window.event].extend(c)
      }
      var e = function() {
        return a.apply(b.bind || null, c)
      };
      if (b.delay) {
        return setTimeout(e, b.delay)
      }
      if (b.periodical) {
        return setInterval(e, b.periodical)
      }
      if (b.attempt) {
        return Function.attempt(e)
      }
      return e()
    }
  },bind: function(c, b) {
    var a = this;
    if (b != null) {
      b = Array.from(b)
    }
    return function() {
      return a.apply(c, b || arguments)
    }


c is null here and arguments are from propTypes[propName](props, propName, componentName, location);





and then it jump to react-with-addon.js

function createChainableTypeChecker(validate) {
  function checkType(isRequired, props, propName, componentName, location) {
    componentName = componentName || ANONYMOUS;
    if (props[propName] == null) {


props are undefined here ...





what should I do...


```
Author:
```
bloodyowl
```
Text:
```


mootools

here is your problem

```
Author:
```
oceanjack
```
Text:
```

but mootools is using by the old webpage, I can't remove it now @bloodyowl

```
Author:
```
asuth
```
Text:
```

It sounds like you're on mootools 1.2, which implements bind differently than the ES5 standard. mootools 1.3 corrected that.
An easier path than getting rid of mootools if that's not feasible would be to upgrade mootools

```
Author:
```
sebmarkbage
```
Text:
```

I personally made sure that was changed in MooTools 1.3 back in the day. You're going to have a bad time with anything before that. Sorry. Upgrade. :/

```
Author:
```
oceanjack
```
Text:
```

I made a chrome plug-in, inject js into the webpage. so, I can't change the js lib on that webpage. It's js lib change Function.prototype.bind first, and then, the page loading react. So, problem happened.
May be I should fix Function.prototype.bind by myself before I using react ? @sebmarkbage

```
Author:
```
zpao
```
Text:
```

This is the same as #2404 where I suggested using a better polyfill.

```
Author:
```
sebmarkbage
```
Text:
```

Chrome extensions can execute code in an isolated DOM environment using content scripts. That way you can execute in an environment completely isolated from the web page's realm. You can still touch the DOM, just not scripts on the page. You'd have to interact with them through message passing, if you need to.

```

## 2886
Title:
```

        Missing closing brace gives misleading warning...
      
```
Author:
```
Dakuan
```
Text:
```

heres some jsx code:
        return (
            <div className="form-group">
                <label className={"control-label " + this.props.labelClass}>
                    {this.props.label || this.props.name}
                </label>
                <div className={this.props.inputClass>
                    <select name={this.props.name} className="form-control">
                        {this.props.options.map(this._renderOption)}
                    </select>
                </div>
            </div>
        )
which gives the following error:
Line 19: Adjacent XJS elements must be wrapped in an enclosing tag

Spent a bit of time wondering which tag wasn't closed or some such before noticing that this line wasn't right:
<div className={this.props.inputClass>
It's missing the closing brace. I wonder if the error could be more descriptive in this case, as when I have had this error before its been the pointy rather than curly brackets that have been the problem.

```
Author:
```
brigand
```
Text:
```

So.. the problem is that this.props.inputClass> is a valid start of an expression in JS, and the > is interpreted as the greater than operator.  The code isn't actually invalid until the first </div> – and if you replaced that with }/> it'd compile.
It's a bit of a tricky problem to solve and get the correct line number.
Side note: you forgot the curlies around this.props.options.map(...

```
Author:
```
Dakuan
```
Text:
```

@brigand Indeed, didn't think it was going to be an easy one. Maybe worth adding to a list of gotchas? It's the sort of silly thing that's easy to lose quite a bit of time to!

```
Author:
```
gpbl
```
Text:
```

@Dakuan you could use a lint tool like jsxhint or islint, they help a lot for catching such errors.

```
Author:
```
brigand
```
Text:
```

@gpbl you'd get the same error with jsxhint.  All it does is jsx -> js and give the resulting js to jshint.

```
Author:
```
zpao
```
Text:
```

I'm going to send you over to https://github.com/facebook/esprima/issues/34 since that's where this error is actually coming from, it's part of the parse step. This specific message is different than the one mentioned in that issue but it's in the same class of problems. I think we're definitely up for making the messages as helpful as possible, just want to make sure we solve the problem in the right way.

```

## 13104
Title:
```

        add support for SyntheticKeyboardEvent#isComposing
      
```
Author:
```
mattkrick
```
Text:
```

Do you want to request a feature or report a bug?
Bug
What is the current behavior?
Synthetic keyboard events do not contain isComposing.
They should if the value is true, per the w3 spec 4.7.5: https://www.w3.org/TR/uievents/#events-compositionevents
What is the expected behavior?
event.isComposing === event.nativeEvent.isComposing
SyntheticKeyboardEvent#isComposing is true when a keydown even is fired after compositionstart and before compositionend.
Which versions of React, and which browser / OS are affected by this issue? Did this work in previous versions of React?
all versions, up through at least 16.4.1

```
Author:
```
gaearon
```
Text:
```

Want to send a PR?

```
Author:
```
craigkovatch
```
Text:
```

This is native-unsupported on IE and Safari < 10.1. Would need to be polyfilled, although it is an extremely simple polyfill: true if seen after compositionStart but before compositionEnd, otherwise false.

```
Author:
```
craigkovatch
```
Text:
```

@gaearon I would like to work on a PR for this. Copying the field from the nativeEvent is easy, polyfilling for IE11 (+old Safari) is not as would need to listen for compositionstart and compositionend events on relevant event targets and save that state somewhere for the KeyboardEvent to read. Do you have any pointers on existing features in React that might follow this pattern of "save data from some native event and use it to polyfill a field in another (synthetic) event"?

```

## 14408
Title:
```

        SSR context issue: Warning: Rendering <Context.Consumer.Provider> is not supported and will be removed in a future major release
      
```
Author:
```
antonybudianto
```
Text:
```

Do you want to request a feature or report a bug?
Bug, probably related https://github.com/facebook/react/pull/13829/files#diff-0ec201d2f87127ead696e6f5681e6830R1645
What is the current behavior?
Warning: Rendering <Context.Consumer.Provider> is not supported and will be removed in a future major release. Did you mean to render <Context.Provider> instead?

If the current behavior is a bug, please provide the steps to reproduce and if possible a minimal demo of the problem. Your bug will get fixed much faster if we can run your code and it doesn't have dependencies other than React. Paste the link to your JSFiddle (https://jsfiddle.net/Luktwrdm/) or CodeSandbox (https://codesandbox.io/s/new) example below:
https://github.com/antonybudianto/react-context-issue
master -> working branch (React 16.4.2)
repro-issue -> branch with warning/issue (React 16.6.3)

npm install
npm start
open localhost:3000, and you can see the warning on the terminal where you run npm start (not dev console)
I think it's SSR issue since no warning shown on client side

Here is the React context API usage:
https://github.com/antonybudianto/react-ua/blob/master/src/react-ua.js
Here is the library usage:

client side Provider (https://github.com/antonybudianto/react-context-issue/blob/master/src/renderer/client.js#L22)
server side Provider (https://github.com/antonybudianto/react-context-issue/blob/master/src/renderer/app.js#L43)
Consumer (https://github.com/antonybudianto/react-context-issue/blob/master/src/routes/Home/HomeView.js#L59)

I'm sure I don't use <MyContext> as a Customer/Provider as you see in the source.
What is the expected behavior?
It should work without warning
Which versions of React, and which browser / OS are affected by this issue? Did this work in previous versions of React?
Warning on React 16.6.3
Working well (no warning) on React 16.4.2

```
Author:
```
antonybudianto
```
Text:
```

FYI, This is still happening in latest release (16.8.0) @aweary

```
Author:
```
gaearon
```
Text:
```

This is triggered by loadable-components which "walk the React tree" (not something we support or recommend to do) and attempt to access context Consumer's Provider property (which exists solely for the purpose of this warning). Printing the warning stack trace would tell you that:
   at walkTree (/Users/gaearon/p/react-context-issue/node_modules/loadable-components/dist/loadable-components.server.cjs.js:149:51)
    at /Users/gaearon/p/react-context-issue/node_modules/loadable-components/dist/loadable-components.server.cjs.js:159:13
    at forEachSingleChild (/Users/gaearon/p/react-context-issue/node_modules/react/cjs/react.development.js:1113:8)
    at traverseAllChildrenImpl (/Users/gaearon/p/react-context-issue/node_modules/react/cjs/react.development.js:1017:5)
    at traverseAllChildrenImpl (/Users/gaearon/p/react-context-issue/node_modules/react/cjs/react.development.js:1033:23)
    at traverseAllChildren (/Users/gaearon/p/react-context-issue/node_modules/react/cjs/react.development.js:1088:10)

Please file an issue in loadable-components so that this library can be fixed to not attempt to read .Consumer.Provider. Thanks!

```

## 9085
Title:
```

        Why Value of Array is lost after setting Timeout
      
```
Author:
```
Ghayyas
```
Text:
```

Hello All, I'm getting Issue regarding Timeout in React.
My code.
submit()  { this.id1++; this.array.push(this.state); this.setState({value:""}); setTimeout(function() { console.log(this.array);   }, 2000); } 
The Issue is.
When user clicks on submit state value has been push in array. But If I set Set timout to get Array list after 2 to 3 sec. It shows me Undefined.
Why is its saying that array is undefined.  If I remove the timeout code then it works fine.
I dont know weather its my issue? Am I doing wrong?
Please help me out.
Thank you.

```
Author:
```
fdaciuk
```
Text:
```

Why not just use this.state instead to push in this.array?

```
Author:
```
Ghayyas
```
Text:
```

Because Im pushing the value in array.
this.array=  []
 this.state= { id: 0, value: ""  }
this.array.push(this.state)

```
Author:
```
fdaciuk
```
Text:
```

I mean, why you don't leave this.array and use just this.state?
this.state is your source of truth. You don't need to pass its values to another object, got it? =)

```
Author:
```
gaearon
```
Text:
```

I'm not sure what you're trying to do by pushing this.state into this.array as this doesn't look like idiomatic React code.
Your particular problem is because of how this works in JavaScript. If you're just calling setTimeout(function() { /* code here */ }), this inside the function will be different than your component. You can either capture it in a variable, bind the function, or you can use the arrow function syntax to preserve this. This article explains how this works in JavaScript.
I'm closing because it's not a bug in React, but a question about JavaScript. We recommend asking those on StackOverflow or support forums, as we use GitHub issues for tracking bugs in React.
Cheers!

```
Author:
```
Ghayyas
```
Text:
```

Im very new to React So Dont know what is state why we use it. I just used it for making single object. Please let me know about State and props in React.

```
Author:
```
fdaciuk
```
Text:
```

@Ghayyas follow the documentation =)

```
Author:
```
Ghayyas
```
Text:
```

Alright So I got Resolved it By..
setTimeout(()=>{
 console.log("Working :D ");
},3000);

Instead of:
 setTimeout(function(){
   console.log("Not Working  BC :( ");
  },3000);

Question is WHY?? :/

```
Author:
```
gaearon
```
Text:
```

I explained why here: #9085 (comment).
You are using an arrow function to capture the value of this.
Please read about arrow functions on a resource like MDN. Cheers!

```

## 10204
Title:
```

        Components rendering order
      
```
Author:
```
DavidHe1127
```
Text:
```

I have a composite component like below
const a = <A></A>;
const b = <B></B>;
const c = <C></C>;

return (
   <div>
     {a}
     {b}
     {c}
    </div>
);
I wonder if it is ok to write it like that and hope JSX will render them in the correct order I embed?
thanks

```
Author:
```
gaearon
```
Text:
```

Yes.

```
Author:
```
gaearon
```
Text:
```

To be clear, it is up to React to decide in which order to actually call their render functions. You shouldn’t need to rely on this. But they will be displayed in the order you specify.

```

## 1107
Title:
```

        Changing node type breaks invariant
      
```
Author:
```
vsolovyov
```
Text:
```

This example:
<html>
  <head>
    <script type="text/javascript" src="http://fb.me/react-0.9.0-rc1.js"></script>
  </head>
  <body>
    <div id="example"></div>
    <script type="text/javascript">
var FailingComponent = React.createClass({
    getInitialState: function() {
        return {selecting: false}
    },
    handleAddClick: function(e) {
        this.setState({selecting: true});
    },
    render: function() {
        if (this.state.selecting) {
            // This will cause Invariant violation
            return React.DOM.input(null, '')
        } else {
            return React.DOM.div({onClick: this.handleAddClick}, "Press me");
        }
    }
});

React.renderComponent(FailingComponent(), document.getElementById('example'))
    </script>
  </body>
</html>

When one tries to click on a div an error will be raised:
Invariant Violation: ReactMount: Two valid but unequal nodes with the same data-reactid: .0
Does break with select/option pair instead of input tag as well (maybe some other tags as well, haven't checked them). Doesn't break with button tag and others.
Works flawlessly on React 0.8.0, doesn't work on master.

```
Author:
```
syranide
```
Text:
```

Can just chime in and say that's something is definitely funky here. Also, it breaks even if wrapped in one or more divs, so it's not specific to the root (although the bad reactid will never go "higher" than .0.0 for me at least).

```
Author:
```
syranide
```
Text:
```

cc @zpao This seems (to me) like a showstopper for 0.9.0.

```
Author:
```
plievone
```
Text:
```

Is this exactly the same as #1105?

```
Author:
```
syranide
```
Text:
```

@plievone It seems so, but it's weird, I did try it with span and div and it worked. Oh well, but yeah, probably same root cause.

```
Author:
```
plievone
```
Text:
```

@syranide Without keys it may reuse the same instance or id or something in some cases, so not unmounting the event target and thus not erroring, I guess?

```
Author:
```
syranide
```
Text:
```

@plievone I think I tried that, but span != div so I think it should anyway. But this whole issue seems magically weird.

```
Author:
```
vsolovyov
```
Text:
```

@syranide Problem occurs for me with reactid=.0.0.3.0:0.3.1 as well

```
Author:
```
petehunt
```
Text:
```

Yeah. Definitely a launch blocker.

```
Author:
```
sophiebits
```
Text:
```

Dupe of #1105. It breaks only with input because ReactMount's node cache doesn't get populated if you just render a span without ever calling getDOMNode().

```
Author:
```
dlindahl
```
Text:
```

I am still seeing this error even on 0.9 with select and checkbox inputs. The catch is that the component is rendered inside an unwrapped Polymer element (unwrap(el))
I am not sure if this is a bug with React or not, but it is entirely unclear to me how to resolve the problem.
Can anyone help nudge me in the right direction?

```
Author:
```
sophiebits
```
Text:
```

@dlindahl Can you post a minimal jsbin or jsfiddle showing the problem in a new issue?

```
Author:
```
dlindahl
```
Text:
```

@spicyj Done: #1263

```

## 847
Title:
```

        TransitionGroup leave animation doesn't get non-active style
      
```
Author:
```
matthewwithanm
```
Text:
```

I think I've come across a bug with TransitionGroup which basically causes properties of the "leave" styles to be ignored. Here's a fiddle demonstrating the problem.
As you can see, the "leave" animation doesn't use the correct origin or transition (in the latest Chrome or FF). If those properties are moved to an always-matching selector (".bluebox"), it works fine.
My only guess as to why this would happen is that the active leave class is being added in the same tick as the leave.

```
Author:
```
matthewwithanm
```
Text:
```

Alright, I dug into the source today to see what was going on. This isn't a bug with TransitionGroup (all of the classes are being applied correctly) but a bug in the CSS. (In other words, my fault!)
However, I do think it highlights a problem with the current animation approach. Let me back up a little to explain why:
The reason that my fiddle doesn't work as I (incorrectly) expected is because the starting value of my transform-origin doesn't match the default value of the element. In addition, the transition specifies that that property should be animated (since it uses "all"). So when the "-leave" class is added, the origin is animated to the "starting" value (right center).
In other words, it's not currently possible to specify a starting point for a leave animation that doesn't match the default value. Of course, I could set the transform-origin for every element that uses the transition but that's clearly brittle and difficult to maintain.
One possible solution would be for React to add an idle class when the transition is idle. Alternatively, users could put the transition property in the "-active" classes instead, but I think that has the potential to screw up switching from enter to leave before enter has completed (or vise versa). (Then again, I'm not sure that's working anyway.)
I realize that this behavior is all taken from ngAnimate, so maybe this isn't the best place to discuss the issue. On the other hand, the React project is much younger and there's probably more of an opportunity to correct it here without worrying about legacy. Let me know!

```
Author:
```
plievone
```
Text:
```


there's probably more of an opportunity to correct it here without worrying about legacy.

I collected a few TransitionGroup issues here #587 . There are race conditions, for example repaints due to some other component's componentDidMount on same tick can cause flash of misstyled content, so perhaps initial render should be affected via setStates in componentWillMount instead.
I guess I would not count on TransitionGroup but go for some custom solution, setting some visible/hidden props, tracking the states in some container, and triggering transitions based on comparing those props in components, notifying the container for completion.. Of course it will be a mess, but there are so many complicated interactions here...

```
Author:
```
sophiebits
```
Text:
```

This isn't super actionable so I'm going to close it out. Thanks for your thoughts though! CSS transitions seem to be surprisingly tricky.

```
Author:
```
tannerlinsley
```
Text:
```

I know this is close, but I thought I would also let people know that this problem snuck up on me to the point that I also dug through the source code only to find that I needed to move the transition property to the -active classes, instead of having it defined by default on the idle or default class of the element.  This is not a bug.  It will feel like one though if you have moved from angular to react.  Ng-Animate goes into great detail to avoid strange edge cases like this one, and since this library is still young (and in my opinion, getting a bit neglected), so don't expect all the edge cases to be covered ;) Great addon nonetheless.  Thanks React team!

```

# Pull
## 6133
Title:
```

        support standard "cssFloat" css property
      
```
Author:
```
stevenvachon
```
Text:
```

For tools that compile CSS may have already converted the name.
More info:
https://npmjs.com/camelcase-css
https://npmjs.com/postcss-js

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for your pull request and welcome to our community. We require contributors to sign our Contributor License Agreement, and we don't seem to have you on file. In order for us to review and merge your code, please sign up at https://code.facebook.com/cla - and if you have received this in error or have any questions, please drop us a line at cla@fb.com. Thanks!

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for signing our Contributor License Agreement. We can now accept your code for this (and any) Facebook open source project. Thanks!

```
Author:
```
zpao
```
Text:
```

Ah true, that's what I get for trying to review from my phone 😬

```
Author:
```
stevenvachon
```
Text:
```

:) np

```
Author:
```
zpao
```
Text:
```

Thanks!

```

## 2512
Title:
```

        Adding "appear" phase to ReactTransitionGroup and ReactCSSTransitionGroup
      
```
Author:
```
leebyron
```
Text:
```

"appear" differs from "enter" in that all children of a transition group at mount time will "appear" but will not "enter". All children later added to an existing transition group will "enter" but not "appear".
This extra transition phase allows for animation-on-mount effects.
A mirroring "appear" prop has been added to ReactCSSTransitionGroup, however for reverse-compatibility (and because "appear" is less common) it defaults to false.
Thanks to @appsforartists for his work investigating the possible ways to implement this.

```
Author:
```
leebyron
```
Text:
```

cc @petehunt

```
Author:
```
leebyron
```
Text:
```

also cc @zpao and @sebmarkbage - just want another set of eyes before merging this.

```
Author:
```
sebmarkbage
```
Text:
```

Just FYI, I think that we'll want to build in some native support hooks for transition groups that works better with composition. Which will later replace ReactTransitionGroup.
This doesn't "appear" to use any additional internal APIs so I don't think this could be harmful.
Thanks.

On Nov 13, 2014, at 9:34 AM, Lee Byron notifications@github.com wrote:
also cc @zpao and @sebmarkbage - just want another set of eyes before merging this.
—
Reply to this email directly or view it on GitHub.


```
Author:
```
appsforartists
```
Text:
```

Other options:

arrive
debut
inauguration (too wordy to actually use, but a short synonym could work)

Might just be 🚲🚲 at this point, but food for thought.

```
Author:
```
leebyron
```
Text:
```

Agreed, @sebmarkbage. The mixing of parent and child lifecycles is a bit confusing and incorporating transitions into the component lifecycle directly will be much clearer and more powerful when we get that worked out.

```

## 8279
Title:
```

        Have jest check for window errors in a similar to console.error logs. Fix for #8260
      
```
Author:
```
franciscofsales
```
Text:
```

Fixes #8260

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for your pull request and welcome to our community. We require contributors to sign our Contributor License Agreement, and we don't seem to have you on file. In order for us to review and merge your code, please sign up at https://code.facebook.com/cla - and if you have received this in error or have any questions, please drop us a line at cla@fb.com. Thanks!
If you are contributing on behalf of someone else (eg your employer): the individual CLA is not sufficient - use https://developers.facebook.com/opensource/cla?type=company instead. Contact cla@fb.com if you have any questions.

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for signing our Contributor License Agreement. We can now accept your code for this (and any) Facebook open source project. Thanks!

```
Author:
```
aweary
```
Text:
```

@cpojer does this look right to you?

```
Author:
```
cpojer
```
Text:
```

sure

```
Author:
```
aweary
```
Text:
```

@franciscofsales can you resolve the conflicts when you get a chance?

```
Author:
```
franciscofsales
```
Text:
```

@aweary I synced and added the spyOn for window errors on a few tests. Hope all it's good now. Let me know if I can help any further.

```
Author:
```
ttsui
```
Text:
```

Any progress on getting this merged?
Was caught out by this problem yesterday and wasted a good half day over it.

```
Author:
```
gaearon
```
Text:
```

@ttsui I don't understand. This PR is for the React repo infrastructure. It won't affect you as a Jest or React user.

```
Author:
```
gaearon
```
Text:
```

I'm going to close since we didn't do a good job reviewing and it got stale. The issue still exists but it seems like it's worth solving together with #11098 (comment). Thanks for the PR!

```

## 4114
Title:
```

        Add owner to void element children warning
      
```
Author:
```
sophiebits
```
Text:
```


No description provided.


```

## 821
Title:
```

        benchmark runner & comparison tool with grunt commands and travis integration
      
```
Author:
```
subtleGradient
```
Text:
```


No description provided.


```
Author:
```
plievone
```
Text:
```

Do you know if there's any possibility to also benchmark memory use? Perf might increase by adding caches etc., which might be sad for e.g. memory-constrained mobile browsers. Possibly an overkill though.

```
Author:
```
subtleGradient
```
Text:
```

Yes. I plan to add some memory profiling stuff soon. That'll be a bit tricky though since it requires passing command line flags to chrome. I'm not sure if sauce labs supports that yet.

```
Author:
```
subtleGradient
```
Text:
```

Current output example: https://travis-ci.org/facebook/react/jobs/16476932
SauceLabs example: https://saucelabs.com/tests/3161fd82969e422a9e05c6f0bd2dd9ee

```
Author:
```
subtleGradient
```
Text:
```

The unit tests are currently failing on master, this diff contains no changes to any React source.

```
Author:
```
petehunt
```
Text:
```

i tested it and it printed json to stdout. and running regular grunt still works

```

## 15346
Title:
```

        Experimental event API: Focus module
      
```
Author:
```
behzad888
```
Text:
```

Note:
determine eventData and pointerType
{
  pointerType: 'mouse' | 'pen' | 'touch' | 'keyboard'
}

Ref #15257

```
Author:
```
sizebot
```
Text:
```


Details of bundled changes.
Comparing: 81a61b1...e948baa
react-events



File
Filesize Diff
Gzip Diff
Prev Size
Current Size
Prev Gzip
Current Gzip
ENV




react-events.development.js
0.0%
-0.2%
1.16 KB
1.16 KB
617 B
616 B
UMD_DEV


react-events.production.min.js
0.0%
🔺+0.3%
512 B
512 B
352 B
353 B
NODE_PROD


react-events-press.development.js
0.0%
0.0%
12.88 KB
12.88 KB
3.02 KB
3.02 KB
UMD_DEV


react-events-hover.development.js
0.0%
+0.1%
6.74 KB
6.74 KB
1.79 KB
1.79 KB
UMD_DEV


react-events-hover.production.min.js
0.0%
🔺+0.1%
3.02 KB
3.02 KB
1.15 KB
1.15 KB
UMD_PROD


react-events-hover.production.min.js
0.0%
🔺+0.1%
2.85 KB
2.85 KB
1.1 KB
1.1 KB
NODE_PROD


react-events-focus.development.js
+68.6%
+73.4%
3.29 KB
5.54 KB
1.11 KB
1.92 KB
UMD_DEV


react-events-focus.production.min.js
🔺+64.2%
🔺+61.6%
1.52 KB
2.49 KB
740 B
1.17 KB
UMD_PROD


react-events-focus.development.js
+72.4%
+78.0%
3.12 KB
5.37 KB
1.06 KB
1.89 KB
NODE_DEV


react-events-focus.production.min.js
🔺+72.4%
🔺+68.7%
1.35 KB
2.33 KB
670 B
1.1 KB
NODE_PROD


ReactEventsFocus-dev.js
+11.4%
+5.9%
3.04 KB
3.38 KB
1.03 KB
1.1 KB
FB_WWW_DEV


ReactEventsFocus-prod.js
🔺+21.0%
🔺+10.4%
2.36 KB
2.85 KB
809 B
893 B
FB_WWW_PROD


react-events-swipe.development.js
0.0%
-0.0%
8.29 KB
8.29 KB
2.57 KB
2.57 KB
UMD_DEV


react-events-swipe.production.min.js
0.0%
-0.1%
3.46 KB
3.46 KB
1.61 KB
1.61 KB
UMD_PROD


react-events-swipe.production.min.js
0.0%
-0.1%
3.29 KB
3.29 KB
1.55 KB
1.55 KB
NODE_PROD


react-events-drag.production.min.js
0.0%
-0.1%
3.3 KB
3.3 KB
1.5 KB
1.5 KB
UMD_PROD


react-events-drag.production.min.js
0.0%
-0.1%
3.14 KB
3.14 KB
1.44 KB
1.44 KB
NODE_PROD





  Generated by 🚫 dangerJS


```
Author:
```
matthargett
```
Text:
```

What about ‘gaze’ for AR/VR?l, and directional pad for TV remote/game controller?

```
Author:
```
necolas
```
Text:
```

We're still figuring things out. Not sure it's worth your time submitting PRs for experimental APIs that are in flux.

```
Author:
```
jhampton
```
Text:
```


What about ‘gaze’ for AR/VR?l, and directional pad for TV remote/game controller?

Agreed @matthargett .  At the risk of being a pedant, perhaps a dwell or hover could be an analog for the same intent?

```
Author:
```
necolas
```
Text:
```

Thanks for taking interest in this work. But I'm closing this PR as master has diverged quite a lot and we're still figuring out event data internally. This approach doesn't work either as native focus/blur events do not contain pointerType information on the event object.

```

## 14673
Title:
```

        Put DEV-only code into DEV blocks
      
```
Author:
```
gaearon
```
Text:
```

This confused me a bit. I think it's sometimes dangerous to leave these assignments without DEV blocks because one might think the variable itself is legit to use outside of DEV, and have a prod error.
In practice the name already codifies it's DEV only but I added guards for consistency with other code.

```
Author:
```
bvaughn
```
Text:
```

Too bad we can't use Flow for this somehow.

```
Author:
```
threepointone
```
Text:
```

that's fair, I'm happy with being more explicit. thanks!

```

## 9881
Title:
```

        Update CHANGELOG.md 0.14.9
      
```
Author:
```
bam
```
Text:
```

Update CHANGELOG.md 0.14.9

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for your pull request and welcome to our community. We require contributors to sign our Contributor License Agreement, and we don't seem to have you on file. In order for us to review and merge your code, please sign up at https://code.facebook.com/cla - and if you have received this in error or have any questions, please drop us a line at cla@fb.com. Thanks!
If you are contributing on behalf of someone else (eg your employer): the individual CLA is not sufficient - use https://developers.facebook.com/opensource/cla?type=company instead. Contact cla@fb.com if you have any questions.

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for signing our Contributor License Agreement. We can now accept your code for this (and any) Facebook open source project. Thanks!

```
Author:
```
aweary
```
Text:
```

Thanks for thinking of this @bam, but this changelog is woefully out of date (last updated over a year ago). We should probably just delete it cc @gaearon
You can get a better idea of what's changed between versions on the release page: https://github.com/facebook/react/releases

```
Author:
```
bam
```
Text:
```

Well @aweary should I add v.0.14.9 to the changelog you mentioned?
I did it just because I've found recently we're using 0.14.9 but I couldn't find any notes on this version in repo (your link too - there is only 0.14.8). And I thought it would be useful to someone who will be in the same situation like me...

```
Author:
```
aweary
```
Text:
```

0.14.9 is a very old version. If you refer to the releases page you'll see that the latest release was 15.5.4. If you're looking to see what changed between versions I recommend looking at the releases page, as it's kept up to date.

```
Author:
```
bam
```
Text:
```

so on that releases page there is no 0.14.9
and AFAIK 0.14.9 has been released less than two months ago...
but as you wish... I already know all information I had to have. just worried about other people.

```
Author:
```
blling
```
Text:
```

who published 0.14.9? there is no tag nor change log :(

```
Author:
```
bam
```
Text:
```

@blling I don't know who was published it, but if you check npm package there is

'0.14.9': '2017-04-12T15:45:16.662Z',

further more you can read Dan's post. Especially look at Dan's answer to comment about absence of git tag 0.14.9…

```

## 9634
Title:
```

        [Fiber] Fix to call deferred callbackQueue even if updates are aborted
      
```
Author:
```
koba04
```
Text:
```

Currently, setState callback has never been called when the update is interrupted.
This PR is fixed it and added a test for reproducing it.

```
Author:
```
acdlite
```
Text:
```

Thanks! The fix looks good. Fix the test and I'll merge.

```
Author:
```
koba04
```
Text:
```

@acdlite Thanks! I've added an assertion for that.

```
Author:
```
sebmarkbage
```
Text:
```

What happens if this gets aborted and begins many times?
This mutation of something that we received from the outside looks suspicious to me: https://github.com/facebook/react/pull/9634/files#diff-58ab36183b601ad6f7c27ed4c7d96278R468
It just to be ok because knew we always started with a fresh array but now we don't. Won't we just keep adding things to it?

```
Author:
```
acdlite
```
Text:
```


Won't we just keep adding things to it?

Hmm I don't think so. When we begin work on a queue, we advance the first update in the list. If we begin the queue again, we start at first. So the only time we process the same update twice is if we clone from current, and the callbackList is reset whenever we clone.
But I agree this is a bit confusing now. I've cleaned this up a bit in the branch I'm working on.

```
Author:
```
koba04
```
Text:
```

Thanks!!

This mutation of something that we received from the outside looks suspicious to me

I'll add a test for this if necessary.

```

## 3129
Title:
```

        Put comma after any non-whitespace non-comment characters in XJSExpression
      
```
Author:
```
jasom
```
Text:
```

For some reason the comma was emitted in renderXJSExpressionContainer if
it was an XJSExpressionContainer, and in the caller of the function
otherwise.  This made getting things like <Foo bar=(baz) quux={biff} />
hard.
This should fix issue #1673

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for your pull request and welcome to our community. We require contributors to sign our Contributor License Agreement, and we don't seem to have you on file. In order for us to review and merge your code, please sign up at https://code.facebook.com/cla - and if you have received this in error or have any questions, please drop us a line at cla@fb.com. Thanks!

```
Author:
```
jasom
```
Text:
```

Re: the TravisCI failure:
Hmm; that test passed locally; I'll check if I'm missing anything from the commit, and update.

```
Author:
```
jasom
```
Text:
```

Added in the missing change, and signed cla.

```
Author:
```
zpao
```
Text:
```

Hmm, can you run npm test locally - it looks like that might not be working on Travis (the grunt jest task doesn't seem to be outputting anything and is passing but running locally it fails). This will run our transform tests (we should also add one for whatever changes we have here, looks like there was a test case in the linked issue).

```
Author:
```
jasom
```
Text:
```

Ah, npm test is much better; I was doing a grunt test previously to test it, per the readme.  It looks like it wants the comma before the following whitespace.  Is this a correctness issue with ASI in the event of a newline, or just an aesthetic thing?

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for signing our Contributor License Agreement. We can now accept your code for this (and any) Facebook open source project. Thanks!

```
Author:
```
jasom
```
Text:
```

The tests seem to think that for:
<foo> {
 bar
//comment
}
{ baz}
</foo>

The comma ought go immediately after bar.  That surprises me; does anyone happen to know why this is the case?  I can sort-of see putting the comma after the last non-whitespace item in the braces, but putting it before comments seems rather odd to me.

```
Author:
```
syranide
```
Text:
```

The reason for them being inlined into the sub visitors is to have control over where they end up. Moving it out like that works, but you then end up with commas after newlines/whitespace rather than before as you would write yourself.

```
Author:
```
jasom
```
Text:
```

@syranide Starting to get a bit off topic, but as far as "as you would write yourself." you probably wouldn't put a space right before a newline, so that becomes a question of how far you want to take it.  I'm testing a patch that fixes #1673 without changing any existing output; it's a lot more complicated than this one though.

```
Author:
```
syranide
```
Text:
```

@jasom I don't see how this is off-topic, the current output by JSX (except for whitespace before newline) was agreed on in #970 and follows common style-guides/lints and the way you would write it yourself, this PR seems to undo just that?
, \n is a deficiency in the current implementation due to the complexity of solving it (it seems).

```
Author:
```
jasom
```
Text:
```

@syranide I meant the , \n nitpick was off topic, not your comment.

```
Author:
```
syranide
```
Text:
```

@jasom Ah :)

```
Author:
```
jasom
```
Text:
```

Okay, I fixed the same issue in a completely different way; it should change not at all any whitespace placement.  I also added a unit test for the issue I fixed.

```
Author:
```
syranide
```
Text:
```

@jasom Your commit is broken (it includes git comments).

```
Author:
```
jasom
```
Text:
```

@syranide Sorry, I pushed the wrong branch

```
Author:
```
jasom
```
Text:
```

@syranide Fixed up git garbage, converted switch to if/else.  I have to go to work now so any other changes will have to wait until tonight.

```
Author:
```
zpao
```
Text:
```

cc @jeffmo

```
Author:
```
jasom
```
Text:
```

Is there anything else I need do to get this PR ready for merge?

```
Author:
```
zpao
```
Text:
```

There are still a few stylistic things. I'm in the process of enabling eslint here so that these files get linted and can tell you what's going on (namely use single quotes, match other styles with indentation, else bracing). If you rebase on top of #3206 (or it will be in master shortly I think) then you can see this yourself with grunt lint (that grunt task doesn't take params and is actually a bit noisy about long lines in other code so you could also run ./node_modules/.bin/eslint vendor/fbtransform directly)

```
Author:
```
jasom
```
Text:
```

The changes I made should be clean to eslint now (I ran it directly on
the file last night).  Do you want me to clean up the entire jsx.js?
-Jason
On 15:34 Thu 19 Feb     , Paul O’Shannessy wrote:

There are still a few stylistic things. I'm in the process of enabling
eslint here so that these files get linted and can tell you what's
going on (namely use single quotes, match other styles with
indentation, else bracing). If you rebase on top of [1]#3206 (or it
will be in master shortly I think) then you can see this yourself with
grunt lint (that grunt task doesn't take params and is actually a bit
noisy about long lines in other code so you could also run
./node_modules/.bin/eslint vendor/fbtransform directly)
—
Reply to this email directly or [2]view it on GitHub.
References

#3206
#3129 (comment)



```
Author:
```
zpao
```
Text:
```

Please rebase and re-run. If you were running eslint from your branch point, it wasn't configured correctly. It has since been configured appropriately and I cleaned up everything else in the above PR. The remaining errors and warnings are a result of your changes (image below is with your branch rebased on master).


```
Author:
```
jasom
```
Text:
```

Thanks @zpao after rebase fixing the lint issues was easy.

```
Author:
```
jasom
```
Text:
```

Let me know if you want me to squash some of these cleanup commits together

```
Author:
```
jasom
```
Text:
```

Any other changes needed?

```
Author:
```
jasom
```
Text:
```

Just checking in on the status of this.

```
Author:
```
jasom
```
Text:
```

Just checking in to see if any action is needed by me on this.

```
Author:
```
zpao
```
Text:
```

Sorry, been focused on shipping 0.13. This won't make that cut but I'll come back to it after. In the mean time, this doesn't merge cleanly (probably mostly just because xjs.js is now jsx.js) so getting it back into a mergable state will help.

```
Author:
```
jasom
```
Text:
```

Now rebased on top of master

```
Author:
```
jasom
```
Text:
```

0.13 is out now.  @zpao: Let me know if I'm being too annoying.

```
Author:
```
zpao
```
Text:
```

Squashed and landed as ef79679. Thanks and I'm sorry it took as long as it did!

```

## 5287
Title:
```

        Updated conference page
      
```
Author:
```
benhalpern
```
Text:
```

Added Reactive 2015 and React Europe 2016 so that there are some upcoming conferences on the page.

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for your pull request and welcome to our community. We require contributors to sign our Contributor License Agreement, and we don't seem to have you on file. In order for us to review and merge your code, please sign up at https://code.facebook.com/cla - and if you have received this in error or have any questions, please drop us a line at cla@fb.com. Thanks!

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for signing our Contributor License Agreement. We can now accept your code for this (and any) Facebook open source project. Thanks!

```
Author:
```
zpao
```
Text:
```

We actually aren't affiliated with Reactive, could you drop that? (As much as we'd like to have every conference with React content on here, it's not something we want to maintain right now)
And for ReactEurope, it looks like they have their dates nailed down to June 2 & 3, can you update that?

```
Author:
```
sophiebits
```
Text:
```

Talked with @zpao, let's keep Reactive – mind updating the dates for React Europe though?

```
Author:
```
facebook-github-bot
```
Text:
```

@benhalpern updated the pull request.

```
Author:
```
sophiebits
```
Text:
```

Thanks!

```

