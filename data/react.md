# facebook/react
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_packages_react_interactions_accessibility_docs_TabbableScopeQuery_md](#_packages_react_interactions_accessibility_docs_TabbableScopeQuery_md)

* [_packages_react_interactions_events_docs_Focus_md](#_packages_react_interactions_events_docs_Focus_md)

* [_fixtures_packaging_README_md](#_fixtures_packaging_README_md)

* [_CONTRIBUTING_md](#_CONTRIBUTING_md)

* [_packages_react_test_renderer_README_md](#_packages_react_test_renderer_README_md)

* [_fixtures_art_README_md](#_fixtures_art_README_md)

* [_packages_react_README_md](#_packages_react_README_md)

* [_fixtures_dom_src_components_fixtures_text_inputs_README_md](#_fixtures_dom_src_components_fixtures_text_inputs_README_md)

* [_fixtures_fiber_debugger_README_md](#_fixtures_fiber_debugger_README_md)

* [_packages_react_devtools_OVERVIEW_md](#_packages_react_devtools_OVERVIEW_md)

* [_github_ISSUE_TEMPLATE_md](#_github_ISSUE_TEMPLATE_md)

* [_packages_react_devtools_CHANGELOG_md](#_packages_react_devtools_CHANGELOG_md)

* [_packages_react_devtools_shared_src_node_modules_react_window_README_md](#_packages_react_devtools_shared_src_node_modules_react_window_README_md)

* [_packages_react_interactions_events_docs_ContextMenu_md](#_packages_react_interactions_events_docs_ContextMenu_md)

* [_packages_react_devtools_shared_src_node_modules_react_window_LICENSE_md](#_packages_react_devtools_shared_src_node_modules_react_window_LICENSE_md)

* [_packages_react_devtools_extensions_README_md](#_packages_react_devtools_extensions_README_md)

* [_packages_react_noop_renderer_README_md](#_packages_react_noop_renderer_README_md)

* [_scripts_error_codes_README_md](#_scripts_error_codes_README_md)

* [_packages_react_cache_README_md](#_packages_react_cache_README_md)

* [_fixtures_unstable_async_time_slicing_README_md](#_fixtures_unstable_async_time_slicing_README_md)

* [_README_md](#_README_md)

[- Inline](#Inline)

* [_scripts_perf_counters_src_jsc_perf_cpp](#_scripts_perf_counters_src_jsc_perf_cpp)

* [_packages_react_dom_npm_unstable_fizz_node_js](#_packages_react_dom_npm_unstable_fizz_node_js)

* [_packages_shared_forks_Scheduler_umd_js](#_packages_shared_forks_Scheduler_umd_js)

* [_scripts_rollup_shims_react_native_NativeMethodsMixin_js](#_scripts_rollup_shims_react_native_NativeMethodsMixin_js)

* [_packages_react_stream_inline_dom_browser_js](#_packages_react_stream_inline_dom_browser_js)

* [_packages_scheduler_src_forks_SchedulerFeatureFlags_www_js](#_packages_scheduler_src_forks_SchedulerFeatureFlags_www_js)

* [_scripts_bench_benchmarks_pe_class_components_benchmark_js](#_scripts_bench_benchmarks_pe_class_components_benchmark_js)

* [_packages_react_native_renderer_src_ReactNativeEventPluginOrder_js](#_packages_react_native_renderer_src_ReactNativeEventPluginOrder_js)

* [_scripts_babel_transform_object_assign_require_js](#_scripts_babel_transform_object_assign_require_js)

* [_packages_react_devtools_shell_src_app_InteractionTracing_index_js](#_packages_react_devtools_shell_src_app_InteractionTracing_index_js)

* [_packages_react_devtools_shared_src_devtools_views_ButtonIcon_js](#_packages_react_devtools_shared_src_devtools_views_ButtonIcon_js)

* [_packages_react_devtools_extensions_webpack_config_js](#_packages_react_devtools_extensions_webpack_config_js)

* [_packages_react_devtools_shared_src_node_modules_react_window_src_FixedSizeGrid_js](#_packages_react_devtools_shared_src_node_modules_react_window_src_FixedSizeGrid_js)

* [_packages_react_reconciler_src_ReactFiberWorkLoop_js](#_packages_react_reconciler_src_ReactFiberWorkLoop_js)

* [_packages_react_devtools_shared_src_tests_profilerStore_test_js](#_packages_react_devtools_shared_src_tests_profilerStore_test_js)

* [_packages_react_dom_src_tests_ReactTestUtils_test_js](#_packages_react_dom_src_tests_ReactTestUtils_test_js)

* [_packages_react_dom_src_events_SyntheticWheelEvent_js](#_packages_react_dom_src_events_SyntheticWheelEvent_js)

* [_packages_react_art_npm_Rectangle_js](#_packages_react_art_npm_Rectangle_js)

* [_packages_react_devtools_shared_src_devtools_views_Profiler_CommitFlamegraphListItem_js](#_packages_react_devtools_shared_src_devtools_views_Profiler_CommitFlamegraphListItem_js)

* [_packages_react_dom_src_tests_ReactErrorLoggingRecovery_test_js](#_packages_react_dom_src_tests_ReactErrorLoggingRecovery_test_js)

[- Issues](#Issues)

* [16193](#16193)

* [2976](#2976)

* [2569](#2569)

* [8295](#8295)

* [8847](#8847)

* [15052](#15052)

* [3743](#3743)

* [3070](#3070)

* [7399](#7399)

* [1029](#1029)

* [8692](#8692)

[- Pull](#Pull)

* [11243](#11243)

* [8562](#8562)

* [6763](#6763)

* [8777](#8777)

* [8538](#8538)

* [4231](#4231)

* [15631](#15631)

* [1747](#1747)

* [16565](#16565)

<!-- toc -->

# Info
## description
A declarative, efficient, and flexible JavaScript library for building user interfaces.

# Markdown
## _packages_react_interactions_accessibility_docs_TabbableScopeQuery_md
```# TabbableScopeQuery

`TabbableScopeQuery` is a custom scope implementation that can be used with
`FocusContain`, `FocusGroup`, `FocusTable` and `FocusManager` modules.

## Usage

'''jsx
import tabbableScopeQuery from 'react-interactions/accessibility/tabbable-scope-query';

function FocusableNodeCollector(props) {
  const scopeRef = useRef(null);

  useEffect(() => {
    const scope = scopeRef.current;

    if (scope) {
      const tabFocusableNodes = scope.queryAllNodes(tabbableScopeQuery);
      if (tabFocusableNodes && props.onFocusableNodes) {
        props.onFocusableNodes(tabFocusableNodes);
      }
    }
  });
  
  return (
    <TabbableScope ref={scopeRef}>
      {props.children}
    </TabbableScope>
  );
}
'''
```
## _packages_react_interactions_events_docs_Focus_md
```# Focus

The `useFocus` hook responds to focus and blur events on its child. Focus events
are dispatched for all input types, with the exception of `onFocusVisibleChange`
which is only dispatched when focusing with a keyboard.

Focus events do not propagate between `useFocus` event responders.

'''js
// Example
const Button = (props) => {
  const [ isFocusVisible, setFocusVisible ] = useState(false);
  const focus = useFocus({
    onBlur={props.onBlur}
    onFocus={props.onFocus}
    onFocusVisibleChange={setFocusVisible}
  });

  return (
    <button
      children={props.children}
      listeners={focus}
      style={{
        ...(isFocusVisible && focusVisibleStyles)
      }}
    >
  );
};
'''

## Types

'''js
type FocusEvent = {
  target: Element,
  pointerType: 'mouse' | 'touch' | 'pen' | 'keyboard',
  timeStamp: number,
  type: 'blur' | 'focus' | 'focuschange' | 'focusvisiblechange'
}
'''

## Props

### disabled: boolean = false

Disables the responder.

### onBlur: (e: FocusEvent) => void

Called when the element loses focus.

### onFocus: (e: FocusEvent) => void

Called when the element gains focus.

### onFocusChange: boolean => void

Called when the element changes focus state (i.e., after `onBlur` and
`onFocus`).

### onFocusVisibleChange: boolean => void

Called when the element receives or loses focus following keyboard navigation.
This can be used to display focus styles only for keyboard interactions.
```
## _fixtures_packaging_README_md
```# Manual Testing Fixtures

This folder exists for **React contributors** only.  
If you use React, you don't need to worry about it.

These fixtures verify that the built React distributions are usable in different environments.  
**They are not running automatically.** (At least not yet. Feel free to contribute to automate them.)

Run them when you make changes to how we package React and ReactDOM.

## How to Run

First, build React and the fixtures:

'''
cd react
npm run build
node fixtures/packaging/build-all.js
'''

Then run a local server, e.g.

'''
npx pushstate-server .
'''

and open the following URL in your browser: [http://localhost:9000/fixtures/packaging/index.html](http://localhost:9000/fixtures/packaging/index.html)

You should see two things:

* A number of iframes (corresponding to various builds), with "Hello World" rendered in each iframe.
* No errors in the console.
```
## _CONTRIBUTING_md
```# Contributing to React

Want to contribute to React? There are a few things you need to know.  

We wrote a **[contribution guide](https://reactjs.org/contributing/how-to-contribute.html)** to help you get started.
```
## _packages_react_test_renderer_README_md
```# `react-test-renderer`

This package provides an experimental React renderer that can be used to render React components to pure JavaScript objects, without depending on the DOM or a native mobile environment.

Essentially, this package makes it easy to grab a snapshot of the "DOM tree" rendered by a React DOM or React Native component without using a browser or jsdom.

Documentation:

[https://reactjs.org/docs/test-renderer.html](https://reactjs.org/docs/test-renderer.html)

Usage:

'''jsx
const ReactTestRenderer = require('react-test-renderer');

const renderer = ReactTestRenderer.create(
  <Link page="https://www.facebook.com/">Facebook</Link>
);

console.log(renderer.toJSON());
// { type: 'a',
//   props: { href: 'https://www.facebook.com/' },
//   children: [ 'Facebook' ] }
'''

You can also use Jest's snapshot testing feature to automatically save a copy of the JSON tree to a file and check in your tests that it hasn't changed: https://facebook.github.io/jest/blog/2016/07/27/jest-14.html.
```
## _fixtures_art_README_md
```# VectorWidget example

To try this example, run:

'''
yarn
yarn build
'''

in this directory, then open index.html in your browser.
```
## _packages_react_README_md
```# `react`

React is a JavaScript library for creating user interfaces.

The `react` package contains only the functionality necessary to define React components. It is typically used together with a React renderer like `react-dom` for the web, or `react-native` for the native environments.

**Note:** by default, React will be in development mode. The development version includes extra warnings about common mistakes, whereas the production version includes extra performance optimizations and strips all error messages. Don't forget to use the [production build](https://reactjs.org/docs/optimizing-performance.html#use-the-production-build) when deploying your application.

## Example Usage

'''js
var React = require('react');
'''
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
## _fixtures_fiber_debugger_README_md
```# Fiber Debugger

This is a debugger handy for visualizing how [Fiber](https://github.com/facebook/react/issues/6170) works internally.

**It is only meant to be used by React contributors, and not by React users.**

It is likely that it might get broken at some point. If it's broken, ping [Dan](https://twitter.com/dan_abramov).

### Running

First, `npm run build` in React root repo folder.

Then `npm install` and `npm start` in this folder.

Open `http://localhost:3000` in Chrome.

### Features

* Edit code that uses `ReactNoop` renderer
* Visualize how relationships between fibers change over time
* Current tree is displayed in green

![fiber debugger](https://d17oy1vhnax1f7.cloudfront.net/items/3R2W1H2M3a0h3p1l133r/Screen%20Recording%202016-10-21%20at%2020.41.gif?v=e4323e51)


```
## _packages_react_devtools_OVERVIEW_md
```# Overview

The React DevTools extension consists of multiple pieces:
* The **frontend** portion is the extension you see (the Components tree, the Profiler, etc.).
* The **backend** portion is invisible. It runs in the same context as React itself. When React commits changes to e.g. the DOM, the backend is responsible for notifying the frontend by sending a message through the **bridge** (an abstraction around e.g. `postMessage`).

One of the largest performance bottlenecks of the old React DevTools was the amount of bridge traffic. Each time React commits an update, the backend sends every fiber that changed across the bridge, resulting in a lot of (JSON) serialization. The primary goal for the DevTools rewrite was to reduce this traffic. Instead of sending everything across the bridge, **the backend should only send the minimum amount required to render the Components tree**. The frontend can request more information (e.g. an element's props) on demand, only as needed.

The old DevTools also rendered the entire application tree in the form of a large DOM structure of nested nodes. A secondary goal of the rewrite was to avoid rendering unnecessary nodes by using a windowing library (specifically [react-window](https://github.com/bvaughn/react-window)).

## Components panel

### Serializing the tree

Every React commit that changes the tree in a way DevTools cares about results in an "_operations_" message being sent across the bridge. These messages are lightweight patches that describe the changes that were made. (We don't resend the full tree structure like in legacy DevTools.)

The payload for each message is a typed array. The first two entries are numbers that identify which renderer and root the update belongs to (for multi-root support). Then the strings are encoded in a [string table](#string-table). The rest of the array depends on the operations being made to the tree.

No updates are required for most commits because we only send the following bits of information: element type, id, parent id, owner id, name, and key. Additional information (e.g. props, state) requires a separate ["_inspectElement_" message](#inspecting-an-element).

#### String table

The string table is encoded right after the first two numbers.

It consists of:

1. the total length of next items that belong to string table
2. for each string in a table:
  1. encoded size
  2. a list of its UTF encoded codepoints

For example, for `Foo` and `Bar` we would see:

'''
[
  8,   // string table length
  3,   // encoded display name size
  70,  // "F"
  111, // "o"
  111, // "o"
  3,   // encoded display name size
  66,  // "B"
  97,  // "a"
  114, // "r"
]
'''

Later operations will reference strings by a one-based index. For example, `1` would mean `"Foo"`, and `2` would mean `"Bar"`. The `0` string id always represents `null` and isn't explicitly encoded in the table.

#### Adding a root node

Adding a root to the tree requires sending 4 numbers:

1. add operation constant (`1`)
1. fiber id
1. element type constant (`8 === ElementTypeRoot`)
1. profiling supported flag

For example, adding a root fiber with an id of 1:
'''js
[
  1, // add operation
  1, // fiber id
  8, // ElementTypeRoot
  1, // this root's renderer supports profiling
]
'''

#### Adding a leaf node

Adding a leaf node takes a variable number of numbers since we need to decode the name (and potentially the key):

1. add operation constant (`1`)
1. fiber id
1. element type constant (e.g. `1 === ElementTypeClass`)
1. parent fiber id
1. owner fiber id
1. string table id for `displayName`
1. string table id for `key`

For example, adding a function component `<Foo>` with an id 2:
'''js
[
  1,   // add operation
  2,   // fiber id
  1,   // ElementTypeClass
  1,   // parent id
  0,   // owner id
  3,   // encoded display name size
  1,   // id of "Foo" displayName in the string table
  0,   // id of null key in the string table (always zero for null)
]
'''

#### Removing a node

Removing a fiber from the tree (a root or a leaf) requires sending:

1. remove operation constant (`2`)
1. how many items were removed
1. number of children
   * (followed by a children-first list of removed fiber ids)

For example, removing fibers with ids of 35 and 21:
'''js
[
  2, // remove operation
  2, // number of removed fibers
  35, // first removed id
  21, // second removed id
]
'''

#### Re-ordering children

1. re-order children constant (`3`)
1. fiber id
1. number of children
   * (followed by an ordered list of child fiber ids)

For example:
'''js
[
  3,  // re-order operation
  15, // fiber id
  2,  // number of children
  35, // first child id
  21, // second child id
]
'''

#### Updating tree base duration

While profiling is in progress, we send an extra operation any time a fiber is added or a updated in a way that affects its tree base duration. This information is needed by the Profiler UI in order to render the "snapshot" and "ranked" chart views.

1. tree base duration constant (`4`)
1. fiber id
1. tree base duration

For example, updating the base duration for a fiber with an id of 1:
'''js
[
  4,  // tree base duration operation
  1,  // fiber id
  32, // new tree base duration value
]
'''

## Reconstructing the tree

The frontend stores its information about the tree in a map of id to objects with the following keys:

* id: `number`
* parentID: `number`
* children: `Array<number>`
* type: `number` (constant)
* displayName: `string | null`
* key: `number | string | null`
* ownerID: `number`
* depth: `number` <sup>1</sup>
* weight: `number` <sup>2</sup>

<sup>1</sup> The `depth` value determines how much padding/indentation to use for the element when rendering it in the Components panel. (This preserves the appearance of a nested tree, even though the view is a flat list.)

<sup>2</sup> The `weight` of an element is the number of elements (including itself) below it in the tree. We cache this property so that we can quickly determine the total number of Components as well as to find the Nth element within that set. (This enables us to use windowing.) This value needs to be adjusted each time elements are added or removed from the tree, but we amortize this over time to avoid any big performance hits when rendering the tree.

#### Finding the element at index N

The tree data structure lets us impose an order on elements and "quickly" find the Nth one using the `weight` attribute.

First we find which root contains the index:
'''js
let rootID;
let root;
let rootWeight = 0;
for (let i = 0; i < this._roots.length; i++) {
  rootID = this._roots[i];
  root = this._idToElement.get(rootID);
  if (root.children.length === 0) {
    continue;
  } else if (rootWeight + root.weight > index) {
    break;
  } else {
    rootWeight += root.weight;
  }
}
'''

We skip the root itself because don't display them in the tree:
'''js
const firstChildID = root.children[0];
'''

Then we traverse the tree to find the element:
'''js
let currentElement = this._idToElement.get(firstChildID);
let currentWeight = rootWeight;
while (index !== currentWeight) {
  for (let i = 0; i < currentElement.children.length; i++) {
    const childID = currentElement.children[i];
    const child = this._idToElement.get(childID);
    const { weight } = child;
    if (index <= currentWeight + weight) {
      currentWeight++;
      currentElement = child;
      break;
    } else {
      currentWeight += weight;
    }
  }
}
'''

## Inspecting an element

When an element is mounted in the tree, DevTools sends a minimal amount of information about it across the bridge. This information includes its display name, type, and key- but does _not_ include things like props or state. (These values are often expensive to serialize and change frequently, which would add a significant amount of load to the bridge.)

Instead DevTools lazily requests additional information about an element only when it is selected in the "Components" tab. At that point, the frontend requests this information by sending a special "_inspectElement_" message containing the id of the element being inspected. The backend then responds with an "_inspectedElement_" message containing the additional details.

### Polling strategy

Elements can update frequently, especially in response to things like scrolling events. Since props and state can be large, we avoid sending this information across the bridge every time the selected element is updated. Instead, the frontend polls the backend for updates about once a second. The backend tracks when the element was last "inspected" and sends a special no-op response if it has not re-rendered since then.

### Deeply nested properties

Even when dealing with a single component, serializing deeply nested properties can be expensive. Because of this, DevTools uses a technique referred to as "dehyration" to only send a shallow copy of the data on initial inspection. DevTools then fills in the missing data on demand as a user expands nested objects or arrays. Filled in paths are remembered (for the currently inspected element) so they are not "dehyrated" again as part of a polling update.

### Inspecting hooks

Hooks present a unique challenge for the DevTools because of the concept of _custom_ hooks. (A custom hook is essentially any function that calls at least one of the built-in hooks. By convention custom hooks also have names that begin with "use".)

So how does DevTools identify custom functions called from within third party components? It does this by temporarily overriding React's built-in hooks and shallow rendering the component in question. Whenever one of the (overridden) built-in hooks are called, it parses the call stack to spot potential custom hooks (functions between the component itself and the built-in hook). This approach enables it to build a tree structure describing all of the calls to both the built-in _and_ custom hooks, along with the values passed to those hooks. (If you're interested in learning more about this, [here is the source code](https://github.com/facebook/react/blob/master/packages/react-debug-tools/src/ReactDebugHooks.js).)

> **Note**: DevTools obtains hooks info by re-rendering a component.
> Breakpoints will be invoked during this additional (shallow) render,
> but DevTools temporarily overrides `console` methods to suppress logging.

### Performance implications

To mitigate the performance impact of re-rendering a component, DevTools does the following:
* Only function components that use _at least one hook_ are rendered. (Props and state can be analyzed without rendering.)
* Rendering is always shallow.
* Rendering is throttled to occur, at most, once per second.
* Rendering is skipped if the component has not updated since the last time its properties were inspected.

## Profiler

The Profiler UI is a powerful tool for identifying and fixing performance problems. The primary goal of the new profiler is to minimize its impact (CPU usage) while profiling is active. This can be accomplished by:
* Minimizing bridge traffic.
* Making expensive computations lazy.

The majority of profiling information is stored on the backend. The backend push-notifies the frontend of when profiling starts or stops by sending a "_profilingStatus_" message. The frontend also asks for the current status after mounting by sending a "_getProfilingStatus_" message. (This is done to support the reload-and-profile functionality.)

When profiling begins, the frontend takes a snapshot/copy of each root. This snapshot includes the id, name, key, and child IDs for each node in the tree. (This information is already present on the frontend, so it does not require any additional bridge traffic.) While profiling is active, each time React commits– the frontend also stores a copy of the "_operations_" message (described above). Once profiling has finished, the frontend can use the original snapshot along with each of the stored "_operations_" messages to reconstruct the tree for each of the profiled commits.

When profiling begins, the backend records the base durations of each fiber currently in the tree. While profiling is in progress, the backend also stores some information about each commit, including:
* Commit time and duration
* Which elements were rendered during that commit
* Which interactions (if any) were part of the commit
* Which props and state changed (if enabled in profiler settings)

This information will eventually be required by the frontend in order to render its profiling graphs, but it will not be sent across the bridge until profiling has completed (to minimize the performance impact of profiling).

### Combining profiling data

Once profiling is finished, the frontend requests profiling data from the backend one renderer at a time by sending a "_getProfilingData_" message. The backend responds with a "_profilingData_" message that contains per-root commit timing and duration information. The frontend then combines this information with its own snapshots to form a complete picture of the profiling session. Using this data, charts and graphs are lazily computed (and incrementally cached) on demand, based on which commits and views are selected in the Profiler UI.

### Importing/exporting data

Because all of the data is merged in the frontend after a profiling session is completed, it can be exported and imported (as a single JSON object), enabling profiling sessions to be shared between users.```
## _github_ISSUE_TEMPLATE_md
```<!--
  Note: if the issue is about documentation or the website, please file it at:
  https://github.com/reactjs/reactjs.org/issues/new
-->

**Do you want to request a *feature* or report a *bug*?**

**What is the current behavior?**

**If the current behavior is a bug, please provide the steps to reproduce and if possible a minimal demo of the problem. Your bug will get fixed much faster if we can run your code and it doesn't have dependencies other than React. Paste the link to your JSFiddle (https://jsfiddle.net/Luktwrdm/) or CodeSandbox (https://codesandbox.io/s/new) example below:**

**What is the expected behavior?**

**Which versions of React, and which browser / OS are affected by this issue? Did this work in previous versions of React?**
```
## _packages_react_devtools_CHANGELOG_md
```# React DevTools changelog

<details>
  <summary>
    Changes that have landed in master but are not yet released.
    Click to see more.
  </summary>
  
  <!-- Upcoming changes go here -->

</details>

## 4.2.0 (October 3, 2019)
#### Features
* "Highlight updates" feature added for browser extensions and `react-devtools-inline` NPM package. ([bvaughn](https://github.com/bvaughn) in [#16989](https://github.com/facebook/react/pull/16989))

## 4.1.3 (September 30, 2019)
#### Bug fixes
* Fixed regression where DevTools wouldn't properly connect with apps when using the `file://` protocol. ([linshunghuang](https://github.com/linshunghuang) in [#16953](https://github.com/facebook/react/pull/16953))

## 4.1.2 (September 27, 2019)
#### Bug fixes
* Fixed an infinite loop that occurred in some cases with prop values of `NaN`. ([bvaughn](https://github.com/bvaughn) in [#16934](https://github.com/facebook/react/pull/16934))

## 4.1.1 (September 26, 2019)
#### Bug fixes
* Fixed bug where Components panel was always empty for certain users. ([linshunghuang](https://github.com/linshunghuang) in [#16900](https://github.com/facebook/react/pull/16900))
* Fixed regression in DevTools editable hooks interface that caused primitive values to be shown as `undefined`. ([bvaughn](https://github.com/bvaughn) in [#16867](https://github.com/facebook/react/pull/16867))
* Fixed bug where DevTools showed stale values in props/state/hooks editing interface. ([bvaughn](https://github.com/bvaughn) in [#16878](https://github.com/facebook/react/pull/16878))
* Show unsupported version dialog with downgrade instructions. ([bvaughn](https://github.com/bvaughn) in [#16897](https://github.com/facebook/react/pull/16897))

## 4.1.0 (September 19, 2019)
#### Features
* Props/state editor supports adding new values and changing value types. ([hristo-kanchev](https://github.com/hristo-kanchev) in [#16700](https://github.com/facebook/react/pull/16700))
#### Bug fixes
* Profiler correctly saves/exports profiling data in Firefox now. ([hristo-kanchev](https://github.com/hristo-kanchev) in [#16612](https://github.com/facebook/react/pull/16612))
* Class components now show "legacy context" header (rather than "context") for legacy API. ([hristo-kanchev](https://github.com/hristo-kanchev) in [#16617](https://github.com/facebook/react/pull/16617))
* Show component source button ("<>") now highlights the `render` method for class components. ([theKashey](https://github.com/theKashey) in [#16759](https://github.com/facebook/react/pull/16759))
* Bugfix for components with non-standard object values for `function.name`. ([LetItRock](https://github.com/LetItRock) in [#16798](https://github.com/facebook/react/pull/16798))

## 4.0.6 (August 26, 2019)
#### Bug fixes
* Remove ⚛️ emoji prefix from Firefox extension tab labels
* Standalone polyfills `Symbol` usage

## 4.0.5 (August 19, 2019)
#### Bug fixes
* Props, state, and context values are alpha sorted.
* Standalone DevTools properly serves backend script over localhost:8097

## 4.0.4 (August 18, 2019)
#### Bug fixes
* Bugfix for potential error if a min-duration commit filter is applied after selecting a fiber in the Profiler UI.

## 4.0.3 (August 17, 2019)
#### Bug fixes
* ES6 `Map` and `Set`, typed arrays, and other unserializable types (e.g. Immutable JS) can now be inspected.
* Empty objects and arrays now display an "(empty)" label to the right to reduce confusion.
* Components that use only the `useContext` hook now properly display hooks values in side panel.
* Style editor now supports single quotes around string values (e.g. both `"red"` and `'red'`).
* Fixed edge case bug that prevented profiling when both React v16 and v15 were present on a page.

## 4.0.2 (August 15, 2019)
#### Permissions cleanup
* Removed unnecessary `webNavigation ` permission from Chrome and Firefox extensions.

## 4.0.1 (August 15, 2019)
#### Permissions cleanup
* Removed unnecessary `<all_urls>`, `background`, and `tabs` permissions from Chrome and Firefox extensions.

## 4.0.0 (August 15, 2019)

### General changes

#### Improved performance
The legacy DevTools extension used to add significant performance overhead, making it unusable for some larger React applications. That overhead has been effectively eliminated in version 4.

[Learn more](https://github.com/facebook/react/blob/master/packages/react-devtools/OVERVIEW.md) about the performance optimizations that made this possible.

#### Component stacks

React component authors have often requested a way to log warnings that include the React ["component stack"](https://reactjs.org/docs/error-boundaries.html#component-stack-traces). DevTools now provides an option to automatically append this information to warnings (`console.warn`) and errors (`console.error`).

![Example console warning with component stack added](https://user-images.githubusercontent.com/29597/62228120-eec3da80-b371-11e9-81bb-018c1e577389.png)

It can be disabled in the general settings panel:

![Settings panel showing "component stacks" option](https://user-images.githubusercontent.com/29597/62227882-8f65ca80-b371-11e9-8a4e-5d27011ad1aa.png)

### Components tree changes

#### Component filters

Large component trees can sometimes be hard to navigate. DevTools now provides a way to filter components so that you can hide ones you're not interested in seeing.

![Component filter demo video](https://user-images.githubusercontent.com/29597/62229209-0bf9a880-b374-11e9-8f84-cebd6c1a016b.gif)

Host nodes (e.g. HTML `<div>`, React Native `View`) are now hidden by default, but you can see them by disabling that filter.

Filter preferences are remembered between sessions.

#### No more inline props

Components in the tree no longer show inline props. This was done to [make DevTools faster](https://github.com/facebook/react/blob/master/packages/react-devtools/OVERVIEW.md) and to make it easier to browse larger component trees.

You can view a component's props, state, and hooks by selecting it:

![Inspecting props](https://user-images.githubusercontent.com/29597/62303001-37da6400-b430-11e9-87fd-10a94df88efa.png)

#### "Rendered by" list

In React, an element's "owner" refers to the thing that rendered it. Sometimes an element's parent is also its owner, but usually they're different. This distinction is important because props come from owners.

![Example code](https://user-images.githubusercontent.com/29597/62229551-bbcf1600-b374-11e9-8411-8ff411f4f847.png)

When you are debugging an unexpected prop value, you can save time if you skip over the parents.

DevTools v4 adds a new "rendered by" list in the right hand pane that allows you to quickly step through the list of owners to speed up your debugging.

![Example video showing the "rendered by" list](https://user-images.githubusercontent.com/29597/62229747-4152c600-b375-11e9-9930-3f6b3b92be7a.gif)

#### Owners tree

The inverse of the "rendered by" list is called the "owners tree". It is the list of things rendered by a particular component- (the things it "owns"). This view is kind of like looking at the source of the component's render method, and can be a helpful way to explore large, unfamiliar React applications.

Double click a component to view the owners tree and click the "x" button to return to the full component tree:

![Demo showing "owners tree" feature](https://user-images.githubusercontent.com/29597/62229452-84f90000-b374-11e9-818a-61eec6be0bb4.gif)

#### No more horizontal scrolling

Deeply nested components used to require both vertical and horizontal scrolling to see, making it easy to "get lost" within large component trees. DevTools now dynamically adjusts nesting indentation to eliminate horizontal scrolling.

![Video demonstration dynamic indentation to eliminate horizontal scrolling](https://user-images.githubusercontent.com/29597/62246661-f8ad0400-b398-11e9-885f-284f150a6d76.gif)

#### Improved hooks support

Hooks now have the same level of support as props and state: values can be edited, arrays and objects can be drilled into, etc.

![Video demonstrating hooks support](https://user-images.githubusercontent.com/29597/62230532-d86c4d80-b376-11e9-8629-1b2129b210d6.gif)

#### Improved search UX

Legacy DevTools search filtered the components tree to show matching nodes as roots. This made the overall structure of the application harder to reason about, because it displayed ancestors as siblings.

Search results are now shown inline similar to the browser's find-in-page search.

![Video demonstrating the search UX](https://user-images.githubusercontent.com/29597/62230923-c63edf00-b377-11e9-9f95-aa62ddc8f62c.gif)

#### Higher order components

[Higher order components](https://reactjs.org/docs/higher-order-components.html) (or HOCs) often provide a [custom `displayName`](https://reactjs.org/docs/higher-order-components.html#convention-wrap-the-display-name-for-easy-debugging) following a convention of `withHOC(InnerComponentName)` in order to make it easier to identify components in React warnings and in DevTools.

The new Components tree formats these HOC names (along with several built-in utilities like `React.memo` and `React.forwardRef`) as a special badge to the right of the decorated component name.

![Screenshot showing HOC badges](https://user-images.githubusercontent.com/29597/62302774-c4385700-b42f-11e9-9ef4-49c5f18d6276.png)

Components decorated with multiple HOCs show the topmost badge and a count. Selecting the component shows all of the HOCs badges in the properties panel.

![Screenshot showing a component with multiple HOC badges](https://user-images.githubusercontent.com/29597/62303729-7fadbb00-b431-11e9-8685-45f5ab52b30b.png)

#### Restoring selection between reloads

DevTools now attempts to restore the previously selected element when you reload the page.

![Video demonstrating selection persistence](https://user-images.githubusercontent.com/810438/63130054-2c02ac00-bfb1-11e9-92fa-382e9e433638.gif)

#### Suspense toggle

React's experimental [Suspense API](https://reactjs.org/docs/react-api.html#suspense) lets components "wait" for something before rendering. `<Suspense>` components can be used to specify loading states when components deeper in the tree are waiting to render.

DevTools lets you test these loading states with a new toggle:

![Video demonstrating suspense toggle UI](https://user-images.githubusercontent.com/29597/62231446-e15e1e80-b378-11e9-92d4-086751dc65fc.gif)

### Profiler changes

#### Reload and profile

The profiler is a powerful tool for performance tuning React components. Legacy DevTools supported profiling, but only after it detected a profiling-capable version of React. Because of this there was no way to profile the initial _mount_ (one of the most performance sensitive parts) of an application.

This feature is now supported with a "reload and profile" action:

![Video demonstrating the reload-and-profile feature](https://user-images.githubusercontent.com/29597/62233455-7a8f3400-b37d-11e9-9563-ec334bfb2572.gif)

#### Import/export

Profiler data can now be exported and shared with other developers to enable easier collaboration.

![Video demonstrating exporting and importing profiler data](https://user-images.githubusercontent.com/29597/62233911-6566d500-b37e-11e9-9052-692378c92538.gif)

Exports include all commits, timings, interactions, etc.

#### "Why did this render?"

"Why did this render?" is a common question when profiling. The profiler now helps answer this question by recording which props and state change between renders.

![Video demonstrating profiler "why did this render?" feature](https://user-images.githubusercontent.com/29597/62234698-0f932c80-b380-11e9-8cf3-a5183af0c388.gif)

Because this feature adds a small amount of overhead, it can be disabled in the profiler settings panel.

#### Component renders list

The profiler now displays a list of each time the selected component rendered during a profiling session, along with the duration of each render. This list can be used to quickly jump between commits when analyzing the performance of a specific component.

![Video demonstrating profiler's component renders list](https://user-images.githubusercontent.com/29597/62234547-bcb97500-b37f-11e9-9615-54fba8b574b9.gif)
```
## _packages_react_devtools_shared_src_node_modules_react_window_README_md
```# react-window

> React components for efficiently rendering large lists and tabular data

[![NPM registry](https://img.shields.io/npm/v/react-window.svg?style=for-the-badge)](https://yarnpkg.com/en/package/react-window) [![Travis](https://img.shields.io/badge/ci-travis-green.svg?style=for-the-badge)](https://travis-ci.org/bvaughn/react-window) [![NPM license](https://img.shields.io/badge/license-mit-red.svg?style=for-the-badge)](LICENSE.md)

## Install

'''bash
# Yarn
yarn add react-window

# NPM
npm install --save react-window
'''

## Usage

Learn more at [react-window.now.sh](https://react-window.now.sh/):

## Related libraries

* [`react-virtualized-auto-sizer`](https://npmjs.com/package/react-virtualized-auto-sizer): HOC that grows to fit all of the available space and passes the width and height values to its child.
* [`react-window-infinite-loader`](https://npmjs.com/package/react-window-infinite-loader): Helps break large data sets down into chunks that can be just-in-time loaded as they are scrolled into view. It can also be used to create infinite loading lists (e.g. Facebook or Twitter).

## Frequently asked questions

### How is `react-window` different from `react-virtualized`?
I wrote `react-virtualized` several years ago. At the time, I was new to both React and the concept of windowing. Because of this, I made a few API decisions that I later came to regret. One of these was adding too many non-essential features and components. Once you add something to an open source project, removing it is pretty painful for users.

`react-window` is a complete rewrite of `react-virtualized`. I didn't try to solve as many problems or support as many use cases. Instead I focused on making the package **smaller**<sup>1</sup> and **faster**. I also put a lot of thought into making the API (and documentation) as beginner-friendly as possible (with the caveat that windowing is still kind of an advanced use case).

If `react-window` provides the functionality your project needs, I would strongly recommend using it instead of `react-virtualized`. However if you need features that only `react-virtualized` provides, you have two options:

1. Use `react-virtualized`. (It's still widely used by a lot of successful projects!)
2. Create a component that decorates one of the `react-window` primitives and adds the functionality you need. You may even want to release this component to NPM (as its own, standalone package)! 🙂

<sup>1 - Adding a `react-virtualized` list to a CRA project increases the (gzipped) build size by ~33.5 KB. Adding a `react-window` list to a CRA project increases the (gzipped) build size by &lt;2 KB.</sup>

### Can a list or a grid fill 100% the width or height of a page?

Yes. I recommend using the [`react-virtualized-auto-sizer` package](https://npmjs.com/package/react-virtualized-auto-sizer):

<img width="336" alt="screen shot 2019-03-07 at 7 29 08 pm" src="https://user-images.githubusercontent.com/29597/54005716-50f41880-410f-11e9-864f-a65bbdf49e07.png">

Here's a [Code Sandbox demo](https://codesandbox.io/s/3vnx878jk5).

### Why is my list blank when I scroll?

If your list looks something like this...

<img src="https://user-images.githubusercontent.com/29597/54005352-eb535c80-410d-11e9-80b2-d3d02db1f599.gif" width="302" height="152">

...then you probably forgot to use the `style` parameter! Libraries like react-window work by absolutely positioning the list items (via an inline style), so don't forget to attach it to the DOM element you render!

<img width="257" alt="screen shot 2019-03-07 at 7 21 48 pm" src="https://user-images.githubusercontent.com/29597/54005433-45ecb880-410e-11e9-8721-420ff1a153da.png">

### Can I lazy load data for my list?

Yes. I recommend using the [`react-window-infinite-loader` package](https://npmjs.com/package/react-window-infinite-loader):

<img width="368" alt="screen shot 2019-03-07 at 7 32 32 pm" src="https://user-images.githubusercontent.com/29597/54006733-653a1480-4113-11e9-907b-08ca5e27b3f9.png">

Here's a [Code Sandbox demo](https://codesandbox.io/s/5wqo7z2np4).

### Can I attach custom properties or event handlers?

Yes, using the `outerElementType` prop.

<img width="412" alt="Screen Shot 2019-03-12 at 8 58 09 AM" src="https://user-images.githubusercontent.com/29597/54215333-f9ee9a80-44a4-11e9-9142-34c67026d950.png">

Here's a [Code Sandbox demo](https://codesandbox.io/s/4zqx79nww0).

### Can I add gutter or padding between items?

Yes, although it requires a bit of inline styling.

<img width="416" alt="Screen Shot 2019-03-26 at 6 33 56 PM" src="https://user-images.githubusercontent.com/29597/55043972-c14ad700-4ff5-11e9-9caa-2e9f4d85f96c.png">

Here's a [Code Sandbox demo](https://codesandbox.io/s/2w8wmlm89p).

### Does this library support "sticky" items?

Yes, although it requires a small amount of user code. Here's a [Code Sandbox demo](https://codesandbox.io/s/0mk3qwpl4l).

## License

MIT © [bvaughn](https://github.com/bvaughn)
```
## _packages_react_interactions_events_docs_ContextMenu_md
```# ContextMenu

The `useContextMenu` hooks responds to context-menu events.

'''js
// Example
const Button = (props) => {
  const contextmenu = useContextMenu({
    disabled,
    onContextMenu,
    preventDefault
  });

  return (
    <div listeners={contextmenu}>
      {props.children}
    </div>
  );
};
'''

## Types

'''js
type ContextMenuEvent = {
  altKey: boolean,
  buttons: 0 | 1 | 2,
  ctrlKey: boolean,
  metaKey: boolean,
  pageX: number,
  pageY: number,
  pointerType: PointerType,
  shiftKey: boolean,
  target: Element,
  timeStamp: number,
  type: 'contextmenu',
  x: number,
  y: number,
}
'''

## Props

### disabled: boolean = false

Disables the responder.

### onContextMenu: (e: ContextMenuEvent) => void

Called when the user performs a gesture to display a context menu.

### preventDefault: boolean = true

Prevents the native behavior (i.e., context menu).
```
## _packages_react_devtools_shared_src_node_modules_react_window_LICENSE_md
```The MIT License (MIT)

Copyright (c) 2018 Brian Vaughn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
## _packages_react_devtools_extensions_README_md
```This is the source code for the React DevTools browser extension.

## Installation

The easiest way to install this extension is as a browser add-on:
* [Chrome web store](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)
* [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/)

## Development

You can also build and install this extension from source.

DevTools embeds local versions of several NPM packages also in this workspae. If you have not already built them, you'll need to do that before getting started by running the following command in the root directory of this repository:
'''sh
yarn build -- react,react-dom,react-is,scheduler --type=NODE
'''

Once the above packages have been built, you can build the extension by running:
'''sh
cd packages/react-devtools-extensions/

yarn build:chrome # => packages/react-devtools-extensions/chrome/build
yarn run test:chrome # Test Chrome extension

yarn build:firefox # => packages/react-devtools-extensions/firefox/build
yarn run test:firefox # Test Firefox extension
'''
```
## _packages_react_noop_renderer_README_md
```# `react-noop-renderer`

This package is the renderer we use for debugging [Fiber](https://github.com/facebook/react/issues/6170).
It is not intended to be used directly.
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
## _packages_react_cache_README_md
```# react-cache

A basic cache for React applications. It also serves as a reference for more
advanced caching implementations.

This package is meant to be used alongside yet-to-be-released, experimental
React features. It's unlikely to be useful in any other context.

**Do not use in a real application.** We're publishing this early for
demonstration purposes.

**Use it at your own risk.**

# No, Really, It Is Unstable

The API ~~may~~ will change wildly between versions.
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
## _README_md
```# [React](https://reactjs.org/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/master/LICENSE) [![npm version](https://img.shields.io/npm/v/react.svg?style=flat)](https://www.npmjs.com/package/react) [![CircleCI Status](https://circleci.com/gh/facebook/react.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/facebook/react) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://reactjs.org/docs/how-to-contribute.html#your-first-pull-request)

React is a JavaScript library for building user interfaces.

* **Declarative:** React makes it painless to create interactive UIs. Design simple views for each state in your application, and React will efficiently update and render just the right components when your data changes. Declarative views make your code more predictable, simpler to understand, and easier to debug.
* **Component-Based:** Build encapsulated components that manage their own state, then compose them to make complex UIs. Since component logic is written in JavaScript instead of templates, you can easily pass rich data through your app and keep state out of the DOM.
* **Learn Once, Write Anywhere:** We don't make assumptions about the rest of your technology stack, so you can develop new features in React without rewriting existing code. React can also render on the server using Node and power mobile apps using [React Native](https://facebook.github.io/react-native/).

[Learn how to use React in your own project](https://reactjs.org/docs/getting-started.html).

## Installation

React has been designed for gradual adoption from the start, and **you can use as little or as much React as you need**:

* Use [Online Playgrounds](https://reactjs.org/docs/getting-started.html#online-playgrounds) to get a taste of React.
* [Add React to a Website](https://reactjs.org/docs/add-react-to-a-website.html) as a `<script>` tag in one minute.
* [Create a New React App](https://reactjs.org/docs/create-a-new-react-app.html) if you're looking for a powerful JavaScript toolchain.

You can use React as a `<script>` tag from a [CDN](https://reactjs.org/docs/cdn-links.html), or as a `react` package on [npm](https://www.npmjs.com/).

## Documentation

You can find the React documentation [on the website](https://reactjs.org/docs).  

Check out the [Getting Started](https://reactjs.org/docs/getting-started.html) page for a quick overview.

The documentation is divided into several sections:

* [Tutorial](https://reactjs.org/tutorial/tutorial.html)
* [Main Concepts](https://reactjs.org/docs/hello-world.html)
* [Advanced Guides](https://reactjs.org/docs/jsx-in-depth.html)
* [API Reference](https://reactjs.org/docs/react-api.html)
* [Where to Get Support](https://reactjs.org/community/support.html)
* [Contributing Guide](https://reactjs.org/docs/how-to-contribute.html)

You can improve it by sending pull requests to [this repository](https://github.com/reactjs/reactjs.org).

## Examples

We have several examples [on the website](https://reactjs.org/). Here is the first one to get you started:

'''jsx
function HelloMessage({ name }) {
  return <div>Hello {name}</div>;
}

ReactDOM.render(
  <HelloMessage name="Taylor" />,
  document.getElementById('container')
);
'''

This example will render "Hello Taylor" into a container on the page.

You'll notice that we used an HTML-like syntax; [we call it JSX](https://reactjs.org/docs/introducing-jsx.html). JSX is not required to use React, but it makes code more readable, and writing it feels like writing HTML. If you're using React as a `<script>` tag, read [this section](https://reactjs.org/docs/add-react-to-a-website.html#optional-try-react-with-jsx) on integrating JSX; otherwise, the [recommended JavaScript toolchains](https://reactjs.org/docs/create-a-new-react-app.html) handle it automatically.

## Contributing

The main purpose of this repository is to continue to evolve React core, making it faster and easier to use. Development of React happens in the open on GitHub, and we are grateful to the community for contributing bugfixes and improvements. Read below to learn how you can take part in improving React.

### [Code of Conduct](https://code.fb.com/codeofconduct)

Facebook has adopted a Code of Conduct that we expect project participants to adhere to. Please read [the full text](https://code.fb.com/codeofconduct) so that you can understand what actions will and will not be tolerated.

### [Contributing Guide](https://reactjs.org/contributing/how-to-contribute.html)

Read our [contributing guide](https://reactjs.org/contributing/how-to-contribute.html) to learn about our development process, how to propose bugfixes and improvements, and how to build and test your changes to React.

### Good First Issues

To help you get your feet wet and get you familiar with our contribution process, we have a list of [good first issues](https://github.com/facebook/react/labels/good%20first%20issue) that contain bugs which have a relatively limited scope. This is a great place to get started.

### License

React is [MIT licensed](./LICENSE).
```
# Inline
## _scripts_perf_counters_src_jsc_perf_cpp
### Line 3-22
```
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#include <errno.h>
#include <stdlib.h>
#include <string.h>

#include <fstream>
#include <iostream>
#include <string>

#include <JavaScriptCore/JavaScript.h>

#include "hardware-counter.h"

using HPHP::HardwareCounter;

void add_native_hook(

```
### Line 82-91
```
  JSObjectRef thisObject,
  size_t argumentCount,
  const JSValueRef arguments[],
  JSValueRef *exception
) {
  // TODO: Allow customizing recorded events
  bool enable = true;
  std::string events = "";
  bool recordSubprocesses = false;
  HardwareCounter::Init(enable, events, recordSubprocesses);

```

## _packages_react_dom_npm_unstable_fizz_node_js

## _packages_shared_forks_Scheduler_umd_js
### Line 28-38
```
  unstable_NormalPriority,
  unstable_LowPriority,
  unstable_IdlePriority,
  unstable_forceFrameRate,

  // this doesn't actually exist on the scheduler, but it *does*
  // on scheduler/unstable_mock, which we'll need inside act().
  unstable_flushAllWithoutAsserting,
} = ReactInternals.Scheduler;

export {

```

## _scripts_rollup_shims_react_native_NativeMethodsMixin_js

## _packages_react_stream_inline_dom_browser_js
### Line 3-11
```
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// This file intentionally does *not* have the Flow annotation.
// Don't add it. See `./inline-typed.js` for an explanation.

export * from './src/ReactFizzStreamer';

```

## _packages_scheduler_src_forks_SchedulerFeatureFlags_www_js

## _scripts_bench_benchmarks_pe_class_components_benchmark_js

## _packages_react_native_renderer_src_ReactNativeEventPluginOrder_js

## _scripts_babel_transform_object_assign_require_js
### Line 20-36
```
    return state.id;
  }

  return {
    pre: function() {
      // map from module to generated identifier
      this.id = null;
    },

    visitor: {
      CallExpression: function(path, file) {
        if (path.get('callee').matchesPattern('Object.assign')) {
          // generate identifier and require if it hasn't been already
          const id = getAssignIdent(path, file, this);
          path.node.callee = id;
        }
      },

```

## _packages_react_devtools_shell_src_app_InteractionTracing_index_js

## _packages_react_devtools_shared_src_devtools_views_ButtonIcon_js

## _packages_react_devtools_extensions_webpack_config_js

## _packages_react_devtools_shared_src_node_modules_react_window_src_FixedSizeGrid_js
### Line 1-5
```
// @flow

import createGridComponent from './createGridComponent';

import type { Props, ScrollToAlign } from './createGridComponent';

```
### Line 59-69
```
      case 'start':
        return maxOffset;
      case 'end':
        return minOffset;
      case 'center':
        // "Centered" offset is usually the average of the min and max.
        // But near the edges of the list, this doesn't hold true.
        const middleOffset = Math.round(
          minOffset + (maxOffset - minOffset) / 2
        );
        if (middleOffset < Math.ceil(width / 2)) {

```
### Line 76-86
```
      case 'auto':
      default:
        if (scrollLeft >= minOffset && scrollLeft <= maxOffset) {
          return scrollLeft;
        } else if (minOffset > maxOffset) {
          // Because we only take into account the scrollbar size when calculating minOffset
          // this value can be larger than maxOffset when at the end of the list
          return minOffset;
        } else if (scrollLeft < minOffset) {
          return minOffset;
        } else {

```
### Line 125-135
```
      case 'start':
        return maxOffset;
      case 'end':
        return minOffset;
      case 'center':
        // "Centered" offset is usually the average of the min and max.
        // But near the edges of the list, this doesn't hold true.
        const middleOffset = Math.round(
          minOffset + (maxOffset - minOffset) / 2
        );
        if (middleOffset < Math.ceil(height / 2)) {

```
### Line 142-152
```
      case 'auto':
      default:
        if (scrollTop >= minOffset && scrollTop <= maxOffset) {
          return scrollTop;
        } else if (minOffset > maxOffset) {
          // Because we only take into account the scrollbar size when calculating minOffset
          // this value can be larger than maxOffset when at the end of the list
          return minOffset;
        } else if (scrollTop < minOffset) {
          return minOffset;
        } else {

```
### Line 211-220
```
      )
    );
  },

  initInstanceProps(props: Props<any>): any {
    // Noop
  },

  shouldResetStyleCacheOnItemSizeChange: true,


```

## _packages_react_reconciler_src_ReactFiberWorkLoop_js
### Line 46-55
```
  IdlePriority,
  flushSyncCallbackQueue,
  scheduleSyncCallback,
} from './SchedulerWithReactIntegration';

// The scheduler is imported here *only* to detect whether it's been mocked
import * as Scheduler from 'scheduler';

import {__interactionsRef, __subscriberRef} from 'scheduler/tracing';


```
### Line 146-155
```
  recordCommitTime,
  startProfilerTimer,
  stopProfilerTimerIfRunningAndRecordDelta,
} from './ReactProfilerTimer';

// DEV stuff
import warningWithoutStack from 'shared/warningWithoutStack';
import getComponentName from 'shared/getComponentName';
import ReactStrictModeWarnings from './ReactStrictModeWarnings';
import {

```
### Line 209-250
```
const RootCompleted = 5;

export type Thenable = {
  then(resolve: () => mixed, reject?: () => mixed): Thenable | void,

  // Special flag to opt out of tracing interactions across a Suspense boundary.
  __reactDoNotTraceInteractions?: boolean,
};

// Describes where we are in the React execution stack
let executionContext: ExecutionContext = NoContext;
// The root we're working on
let workInProgressRoot: FiberRoot | null = null;
// The fiber we're working on
let workInProgress: Fiber | null = null;
// The expiration time we're rendering
let renderExpirationTime: ExpirationTime = NoWork;
// Whether to root completed, errored, suspended, etc.
let workInProgressRootExitStatus: RootExitStatus = RootIncomplete;
// A fatal error, if one is thrown
let workInProgressRootFatalError: mixed = null;
// Most recent event time among processed updates during this render.
// This is conceptually a time stamp but expressed in terms of an ExpirationTime
// because we deal mostly with expiration times in the hot path, so this avoids
// the conversion happening in the hot path.
let workInProgressRootLatestProcessedExpirationTime: ExpirationTime = Sync;
let workInProgressRootLatestSuspenseTimeout: ExpirationTime = Sync;
let workInProgressRootCanSuspendUsingConfig: null | SuspenseConfig = null;
// The work left over by components that were visited during this render. Only
// includes unprocessed updates, not work in bailed out children.
let workInProgressRootNextUnprocessedUpdateTime: ExpirationTime = NoWork;

// If we're pinged while rendering we don't always restart immediately.
// This flag determines if it might be worthwhile to restart if an opportunity
// happens latere.
let workInProgressRootHasPendingPing: boolean = false;
// The most recent time we committed a fallback. This lets us ensure a train
// model where we don't commit new loading states in too quick succession.
let globalMostRecentFallbackTime: number = 0;
const FALLBACK_THROTTLE_MS: number = 500;

let nextEffect: Fiber | null = null;

```
### Line 260-269
```
let rootsWithPendingDiscreteUpdates: Map<
  FiberRoot,
  ExpirationTime,
> | null = null;

// Use these to prevent an infinite loop of nested updates
const NESTED_UPDATE_LIMIT = 50;
let nestedUpdateCount: number = 0;
let rootWithNestedUpdates: FiberRoot | null = null;


```
### Line 270-305
```
const NESTED_PASSIVE_UPDATE_LIMIT = 50;
let nestedPassiveUpdateCount: number = 0;

let interruptedBy: Fiber | null = null;

// Marks the need to reschedule pending interactions at these expiration times
// during the commit phase. This enables them to be traced across components
// that spawn new work during render. E.g. hidden boundaries, suspended SSR
// hydration or SuspenseList.
let spawnedWorkDuringRender: null | Array<ExpirationTime> = null;

// Expiration times are computed by adding to the current time (the start
// time). However, if two updates are scheduled within the same event, we
// should treat their start times as simultaneous, even if the actual clock
// time has advanced between the first and second call.

// In other words, because expiration times determine how updates are batched,
// we want all updates of like priority that occur within the same event to
// receive the same expiration time. Otherwise we get tearing.
let currentEventTime: ExpirationTime = NoWork;

export function requestCurrentTimeForUpdate() {
  if ((executionContext & (RenderContext | CommitContext)) !== NoContext) {
    // We're inside React, so it's fine to read the actual time.
    return msToExpirationTime(now());
  }
  // We're not inside React, so we may be in the middle of a browser event.
  if (currentEventTime !== NoWork) {
    // Use the same start time for all updates until we enter React again.
    return currentEventTime;
  }
  // This is the first update since React yielded. Compute a new start time.
  currentEventTime = msToExpirationTime(now());
  return currentEventTime;
}


```
### Line 321-354
```
  if ((mode & ConcurrentMode) === NoMode) {
    return priorityLevel === ImmediatePriority ? Sync : Batched;
  }

  if ((executionContext & RenderContext) !== NoContext) {
    // Use whatever time we're already rendering
    // TODO: Should there be a way to opt out, like with `runWithPriority`?
    return renderExpirationTime;
  }

  let expirationTime;
  if (suspenseConfig !== null) {
    // Compute an expiration time based on the Suspense timeout.
    expirationTime = computeSuspenseExpiration(
      currentTime,
      suspenseConfig.timeoutMs | 0 || LOW_PRIORITY_EXPIRATION,
    );
  } else {
    // Compute an expiration time based on the Scheduler priority.
    switch (priorityLevel) {
      case ImmediatePriority:
        expirationTime = Sync;
        break;
      case UserBlockingPriority:
        // TODO: Rename this to computeUserBlockingExpiration
        expirationTime = computeInteractiveExpiration(currentTime);
        break;
      case NormalPriority:
      case LowPriority: // TODO: Handle LowPriority
        // TODO: Rename this to... something better.
        expirationTime = computeAsyncExpiration(currentTime);
        break;
      case IdlePriority:
        expirationTime = Idle;

```
### Line 356-371
```
      default:
        invariant(false, 'Expected a valid priority level');
    }
  }

  // If we're in the middle of rendering a tree, do not update at the same
  // expiration time that is already rendering.
  // TODO: We shouldn't have to do this if the update is on a different root.
  // Refactor computeExpirationForFiber + scheduleUpdate so we have access to
  // the root when we check for this condition.
  if (workInProgressRoot !== null && expirationTime === renderExpirationTime) {
    // This is a trick to move this update into a separate batch
    expirationTime -= 1;
  }

  return expirationTime;

```
### Line 385-420
```
  }

  checkForInterruption(fiber, expirationTime);
  recordScheduleUpdate();

  // TODO: computeExpirationForFiber also reads the priority. Pass the
  // priority as an argument to that function and this one.
  const priorityLevel = getCurrentPriorityLevel();

  if (expirationTime === Sync) {
    if (
      // Check if we're inside unbatchedUpdates
      (executionContext & LegacyUnbatchedContext) !== NoContext &&
      // Check if we're not already rendering
      (executionContext & (RenderContext | CommitContext)) === NoContext
    ) {
      // Register pending interactions on the root to avoid losing traced interaction data.
      schedulePendingInteractions(root, expirationTime);

      // This is a legacy edge case. The initial mount of a ReactDOM.render-ed
      // root inside of batchedUpdates should be synchronous, but layout updates
      // should be deferred until the end of the batch.
      performSyncWorkOnRoot(root);
    } else {
      ensureRootIsScheduled(root);
      schedulePendingInteractions(root, expirationTime);
      if (executionContext === NoContext) {
        // Flush the synchronous work now, unless we're already working or inside
        // a batch. This is intentionally inside scheduleUpdateOnFiber instead of
        // scheduleCallbackForFiber to preserve the ability to schedule a callback
        // without immediately flushing it. We only do this for user-initiated
        // updates, to preserve historical behavior of sync mode.
        flushSyncCallbackQueue();
      }
    }
  } else {

```
### Line 422-437
```
    schedulePendingInteractions(root, expirationTime);
  }

  if (
    (executionContext & DiscreteEventContext) !== NoContext &&
    // Only updates at user-blocking priority or greater are considered
    // discrete, even inside a discrete event.
    (priorityLevel === UserBlockingPriority ||
      priorityLevel === ImmediatePriority)
  ) {
    // This is the result of a discrete event. Track the lowest priority
    // discrete update per root so we can flush them early, if needed.
    if (rootsWithPendingDiscreteUpdates === null) {
      rootsWithPendingDiscreteUpdates = new Map([[root, expirationTime]]);
    } else {
      const lastDiscreteTime = rootsWithPendingDiscreteUpdates.get(root);

```
### Line 441-463
```
    }
  }
}
export const scheduleWork = scheduleUpdateOnFiber;

// This is split into a separate function so we can mark a fiber with pending
// work without treating it as a typical update that originates from an event;
// e.g. retrying a Suspense boundary isn't an update, but it does schedule work
// on a fiber.
function markUpdateTimeFromFiberToRoot(fiber, expirationTime) {
  // Update the source fiber's expiration time
  if (fiber.expirationTime < expirationTime) {
    fiber.expirationTime = expirationTime;
  }
  let alternate = fiber.alternate;
  if (alternate !== null && alternate.expirationTime < expirationTime) {
    alternate.expirationTime = expirationTime;
  }
  // Walk the parent path to the root and update the child expiration time.
  let node = fiber.return;
  let root = null;
  if (node === null && fiber.tag === HostRoot) {
    root = fiber.stateNode;

```
### Line 486-559
```
    }
  }

  if (root !== null) {
    if (workInProgressRoot === root) {
      // Received an update to a tree that's in the middle of rendering. Mark
      // that's unprocessed work on this root.
      markUnprocessedUpdateTime(expirationTime);

      if (workInProgressRootExitStatus === RootSuspendedWithDelay) {
        // The root already suspended with a delay, which means this render
        // definitely won't finish. Since we have a new update, let's mark it as
        // suspended now, right before marking the incoming update. This has the
        // effect of interrupting the current render and switching to the update.
        // TODO: This happens to work when receiving an update during the render
        // phase, because of the trick inside computeExpirationForFiber to
        // subtract 1 from `renderExpirationTime` to move it into a
        // separate bucket. But we should probably model it with an exception,
        // using the same mechanism we use to force hydration of a subtree.
        // TODO: This does not account for low pri updates that were already
        // scheduled before the root started rendering. Need to track the next
        // pending expiration time (perhaps by backtracking the return path) and
        // then trigger a restart in the `renderDidSuspendDelayIfPossible` path.
        markRootSuspendedAtTime(root, renderExpirationTime);
      }
    }
    // Mark that the root has a pending update.
    markRootUpdatedAtTime(root, expirationTime);
  }

  return root;
}

function getNextRootExpirationTimeToWorkOn(root: FiberRoot): ExpirationTime {
  // Determines the next expiration time that the root should render, taking
  // into account levels that may be suspended, or levels that may have
  // received a ping.

  const lastExpiredTime = root.lastExpiredTime;
  if (lastExpiredTime !== NoWork) {
    return lastExpiredTime;
  }

  // "Pending" refers to any update that hasn't committed yet, including if it
  // suspended. The "suspended" range is therefore a subset.
  const firstPendingTime = root.firstPendingTime;
  if (!isRootSuspendedAtTime(root, firstPendingTime)) {
    // The highest priority pending time is not suspended. Let's work on that.
    return firstPendingTime;
  }

  // If the first pending time is suspended, check if there's a lower priority
  // pending level that we know about. Or check if we received a ping. Work
  // on whichever is higher priority.
  const lastPingedTime = root.lastPingedTime;
  const nextKnownPendingLevel = root.nextKnownPendingLevel;
  return lastPingedTime > nextKnownPendingLevel
    ? lastPingedTime
    : nextKnownPendingLevel;
}

// Use this function to schedule a task for a root. There's only one task per
// root; if a task was already scheduled, we'll check to make sure the
// expiration time of the existing task is the same as the expiration time of
// the next level that the root has work on. This function is called on every
// update, and right before exiting a task.
function ensureRootIsScheduled(root: FiberRoot) {
  const lastExpiredTime = root.lastExpiredTime;
  if (lastExpiredTime !== NoWork) {
    // Special case: Expired work should flush synchronously.
    root.callbackExpirationTime = Sync;
    root.callbackPriority = ImmediatePriority;
    root.callbackNode = scheduleSyncCallback(
      performSyncWorkOnRoot.bind(null, root),

```
### Line 562-613
```
  }

  const expirationTime = getNextRootExpirationTimeToWorkOn(root);
  const existingCallbackNode = root.callbackNode;
  if (expirationTime === NoWork) {
    // There's nothing to work on.
    if (existingCallbackNode !== null) {
      root.callbackNode = null;
      root.callbackExpirationTime = NoWork;
      root.callbackPriority = NoPriority;
    }
    return;
  }

  // TODO: If this is an update, we already read the current time. Pass the
  // time as an argument.
  const currentTime = requestCurrentTimeForUpdate();
  const priorityLevel = inferPriorityFromExpirationTime(
    currentTime,
    expirationTime,
  );

  // If there's an existing render task, confirm it has the correct priority and
  // expiration time. Otherwise, we'll cancel it and schedule a new one.
  if (existingCallbackNode !== null) {
    const existingCallbackPriority = root.callbackPriority;
    const existingCallbackExpirationTime = root.callbackExpirationTime;
    if (
      // Callback must have the exact same expiration time.
      existingCallbackExpirationTime === expirationTime &&
      // Callback must have greater or equal priority.
      existingCallbackPriority >= priorityLevel
    ) {
      // Existing callback is sufficient.
      return;
    }
    // Need to schedule a new task.
    // TODO: Instead of scheduling a new task, we should be able to change the
    // priority of the existing one.
    cancelCallback(existingCallbackNode);
  }

  root.callbackExpirationTime = expirationTime;
  root.callbackPriority = priorityLevel;

  let callbackNode;
  if (expirationTime === Sync) {
    // Sync React callbacks are scheduled on a special internal queue
    callbackNode = scheduleSyncCallback(performSyncWorkOnRoot.bind(null, root));
  } else if (disableSchedulerTimeoutBasedOnReactExpirationTime) {
    callbackNode = scheduleCallback(
      priorityLevel,

```
### Line 615-651
```
    );
  } else {
    callbackNode = scheduleCallback(
      priorityLevel,
      performConcurrentWorkOnRoot.bind(null, root),
      // Compute a task timeout based on the expiration time. This also affects
      // ordering because tasks are processed in timeout order.
      {timeout: expirationTimeToMs(expirationTime) - now()},
    );
  }

  root.callbackNode = callbackNode;
}

// This is the entry point for every concurrent task, i.e. anything that
// goes through Scheduler.
function performConcurrentWorkOnRoot(root, didTimeout) {
  // Since we know we're in a React event, we can clear the current
  // event time. The next update will compute a new event time.
  currentEventTime = NoWork;

  if (didTimeout) {
    // The render task took too long to complete. Mark the current time as
    // expired to synchronously render all expired work in a single batch.
    const currentTime = requestCurrentTimeForUpdate();
    markRootExpiredAtTime(root, currentTime);
    // This will schedule a synchronous callback.
    ensureRootIsScheduled(root);
    return null;
  }

  // Determine the next expiration time to work on, using the fields stored
  // on the root.
  const expirationTime = getNextRootExpirationTimeToWorkOn(root);
  if (expirationTime !== NoWork) {
    const originalCallbackNode = root.callbackNode;
    invariant(

```
### Line 653-673
```
      'Should not already be working.',
    );

    flushPassiveEffects();

    // If the root or expiration time have changed, throw out the existing stack
    // and prepare a fresh one. Otherwise we'll continue where we left off.
    if (
      root !== workInProgressRoot ||
      expirationTime !== renderExpirationTime
    ) {
      prepareFreshStack(root, expirationTime);
      startWorkOnPendingInteractions(root, expirationTime);
    }

    // If we have a work-in-progress fiber, it means there's still work to do
    // in this root.
    if (workInProgress !== null) {
      const prevExecutionContext = executionContext;
      executionContext |= RenderContext;
      const prevDispatcher = pushDispatcher(root);

```
### Line 696-709
```
        ensureRootIsScheduled(root);
        throw fatalError;
      }

      if (workInProgress !== null) {
        // There's still work left over. Exit without committing.
        stopInterruptedWorkLoopTimer();
      } else {
        // We now have a consistent tree. The next step is either to commit it,
        // or, if something suspended, wait to commit it after a timeout.
        stopFinishedWorkLoopTimer();

        const finishedWork: Fiber = ((root.finishedWork =
          root.current.alternate): any);

```
### Line 716-726
```
        );
      }

      ensureRootIsScheduled(root);
      if (root.callbackNode === originalCallbackNode) {
        // The task node scheduled for this root is the same one that's
        // currently executed. Need to return a continuation.
        return performConcurrentWorkOnRoot.bind(null, root);
      }
    }
  }

```
### Line 731-764
```
  root,
  finishedWork,
  exitStatus,
  expirationTime,
) {
  // Set this to null to indicate there's no in-progress render.
  workInProgressRoot = null;

  switch (exitStatus) {
    case RootIncomplete:
    case RootFatalErrored: {
      invariant(false, 'Root did not complete. This is a bug in React.');
    }
    // Flow knows about invariant, so it complains if I add a break
    // statement, but eslint doesn't know about invariant, so it complains
    // if I do. eslint-disable-next-line no-fallthrough
    case RootErrored: {
      // If this was an async render, the error may have happened due to
      // a mutation in a concurrent event. Try rendering one more time,
      // synchronously, to see if the error goes away. If there are
      // lower priority updates, let's include those, too, in case they
      // fix the inconsistency. Render at Idle to include all updates.
      // If it was Idle or Never or some not-yet-invented time, render
      // at that time.
      markRootExpiredAtTime(
        root,
        expirationTime > Idle ? Idle : expirationTime,
      );
      // We assume that this second render pass will be synchronous
      // and therefore not hit this path again.
      break;
    }
    case RootSuspended: {
      markRootSuspendedAtTime(root, expirationTime);

```
### Line 766-839
```
      if (expirationTime === lastSuspendedTime) {
        root.nextKnownPendingLevel = getRemainingExpirationTime(finishedWork);
      }
      flushSuspensePriorityWarningInDEV();

      // We have an acceptable loading state. We need to figure out if we
      // should immediately commit it or wait a bit.

      // If we have processed new updates during this render, we may now
      // have a new loading state ready. We want to ensure that we commit
      // that as soon as possible.
      const hasNotProcessedNewUpdates =
        workInProgressRootLatestProcessedExpirationTime === Sync;
      if (
        hasNotProcessedNewUpdates &&
        // do not delay if we're inside an act() scope
        !(
          __DEV__ &&
          flushSuspenseFallbacksInTests &&
          IsThisRendererActing.current
        )
      ) {
        // If we have not processed any new updates during this pass, then
        // this is either a retry of an existing fallback state or a
        // hidden tree. Hidden trees shouldn't be batched with other work
        // and after that's fixed it can only be a retry. We're going to
        // throttle committing retries so that we don't show too many
        // loading states too quickly.
        let msUntilTimeout =
          globalMostRecentFallbackTime + FALLBACK_THROTTLE_MS - now();
        // Don't bother with a very short suspense time.
        if (msUntilTimeout > 10) {
          if (workInProgressRootHasPendingPing) {
            const lastPingedTime = root.lastPingedTime;
            if (lastPingedTime === NoWork || lastPingedTime >= expirationTime) {
              // This render was pinged but we didn't get to restart
              // earlier so try restarting now instead.
              root.lastPingedTime = expirationTime;
              prepareFreshStack(root, expirationTime);
              break;
            }
          }

          const nextTime = getNextRootExpirationTimeToWorkOn(root);
          if (nextTime !== NoWork && nextTime !== expirationTime) {
            // There's additional work on this root.
            break;
          }
          if (
            lastSuspendedTime !== NoWork &&
            lastSuspendedTime !== expirationTime
          ) {
            // We should prefer to render the fallback of at the last
            // suspended level. Ping the last suspended level to try
            // rendering it again.
            root.lastPingedTime = lastSuspendedTime;
            break;
          }

          // The render is suspended, it hasn't timed out, and there's no
          // lower priority work to do. Instead of committing the fallback
          // immediately, wait for more data to arrive.
          root.timeoutHandle = scheduleTimeout(
            commitRoot.bind(null, root),
            msUntilTimeout,
          );
          break;
        }
      }
      // The work expired. Commit immediately.
      commitRoot(root);
      break;
    }
    case RootSuspendedWithDelay: {

```
### Line 843-955
```
        root.nextKnownPendingLevel = getRemainingExpirationTime(finishedWork);
      }
      flushSuspensePriorityWarningInDEV();

      if (
        // do not delay if we're inside an act() scope
        !(
          __DEV__ &&
          flushSuspenseFallbacksInTests &&
          IsThisRendererActing.current
        )
      ) {
        // We're suspended in a state that should be avoided. We'll try to
        // avoid committing it for as long as the timeouts let us.
        if (workInProgressRootHasPendingPing) {
          const lastPingedTime = root.lastPingedTime;
          if (lastPingedTime === NoWork || lastPingedTime >= expirationTime) {
            // This render was pinged but we didn't get to restart earlier
            // so try restarting now instead.
            root.lastPingedTime = expirationTime;
            prepareFreshStack(root, expirationTime);
            break;
          }
        }

        const nextTime = getNextRootExpirationTimeToWorkOn(root);
        if (nextTime !== NoWork && nextTime !== expirationTime) {
          // There's additional work on this root.
          break;
        }
        if (
          lastSuspendedTime !== NoWork &&
          lastSuspendedTime !== expirationTime
        ) {
          // We should prefer to render the fallback of at the last
          // suspended level. Ping the last suspended level to try
          // rendering it again.
          root.lastPingedTime = lastSuspendedTime;
          break;
        }

        let msUntilTimeout;
        if (workInProgressRootLatestSuspenseTimeout !== Sync) {
          // We have processed a suspense config whose expiration time we
          // can use as the timeout.
          msUntilTimeout =
            expirationTimeToMs(workInProgressRootLatestSuspenseTimeout) - now();
        } else if (workInProgressRootLatestProcessedExpirationTime === Sync) {
          // This should never normally happen because only new updates
          // cause delayed states, so we should have processed something.
          // However, this could also happen in an offscreen tree.
          msUntilTimeout = 0;
        } else {
          // If we don't have a suspense config, we're going to use a
          // heuristic to determine how long we can suspend.
          const eventTimeMs: number = inferTimeFromExpirationTime(
            workInProgressRootLatestProcessedExpirationTime,
          );
          const currentTimeMs = now();
          const timeUntilExpirationMs =
            expirationTimeToMs(expirationTime) - currentTimeMs;
          let timeElapsed = currentTimeMs - eventTimeMs;
          if (timeElapsed < 0) {
            // We get this wrong some time since we estimate the time.
            timeElapsed = 0;
          }

          msUntilTimeout = jnd(timeElapsed) - timeElapsed;

          // Clamp the timeout to the expiration time. TODO: Once the
          // event time is exact instead of inferred from expiration time
          // we don't need this.
          if (timeUntilExpirationMs < msUntilTimeout) {
            msUntilTimeout = timeUntilExpirationMs;
          }
        }

        // Don't bother with a very short suspense time.
        if (msUntilTimeout > 10) {
          // The render is suspended, it hasn't timed out, and there's no
          // lower priority work to do. Instead of committing the fallback
          // immediately, wait for more data to arrive.
          root.timeoutHandle = scheduleTimeout(
            commitRoot.bind(null, root),
            msUntilTimeout,
          );
          break;
        }
      }
      // The work expired. Commit immediately.
      commitRoot(root);
      break;
    }
    case RootCompleted: {
      // The work completed. Ready to commit.
      if (
        // do not delay if we're inside an act() scope
        !(
          __DEV__ &&
          flushSuspenseFallbacksInTests &&
          IsThisRendererActing.current
        ) &&
        workInProgressRootLatestProcessedExpirationTime !== Sync &&
        workInProgressRootCanSuspendUsingConfig !== null
      ) {
        // If we have exceeded the minimum loading delay, which probably
        // means we have shown a spinner already, we might have to suspend
        // a bit longer to ensure that the spinner is shown for
        // enough time.
        const msUntilTimeout = computeMsUntilSuspenseLoadingDelay(
          workInProgressRootLatestProcessedExpirationTime,
          expirationTime,
          workInProgressRootCanSuspendUsingConfig,

```
### Line 970-988
```
      invariant(false, 'Unknown root exit status.');
    }
  }
}

// This is the entry point for synchronous tasks that don't go
// through Scheduler
function performSyncWorkOnRoot(root) {
  // Check if there's expired work on this root. Otherwise, render at Sync.
  const lastExpiredTime = root.lastExpiredTime;
  const expirationTime = lastExpiredTime !== NoWork ? lastExpiredTime : Sync;
  if (root.finishedExpirationTime === expirationTime) {
    // There's already a pending commit at this expiration time.
    // TODO: This is poorly factored. This case only exists for the
    // batch.commit() API.
    commitRoot(root);
  } else {
    invariant(
      (executionContext & (RenderContext | CommitContext)) === NoContext,

```
### Line 989-1009
```
      'Should not already be working.',
    );

    flushPassiveEffects();

    // If the root or expiration time have changed, throw out the existing stack
    // and prepare a fresh one. Otherwise we'll continue where we left off.
    if (
      root !== workInProgressRoot ||
      expirationTime !== renderExpirationTime
    ) {
      prepareFreshStack(root, expirationTime);
      startWorkOnPendingInteractions(root, expirationTime);
    }

    // If we have a work-in-progress fiber, it means there's still work to do
    // in this root.
    if (workInProgress !== null) {
      const prevExecutionContext = executionContext;
      executionContext |= RenderContext;
      const prevDispatcher = pushDispatcher(root);

```
### Line 1033-1067
```
        ensureRootIsScheduled(root);
        throw fatalError;
      }

      if (workInProgress !== null) {
        // This is a sync render, so we should have finished the whole tree.
        invariant(
          false,
          'Cannot commit an incomplete root. This error is likely caused by a ' +
            'bug in React. Please file an issue.',
        );
      } else {
        // We now have a consistent tree. Because this is a sync render, we
        // will commit it even if something suspended.
        stopFinishedWorkLoopTimer();
        root.finishedWork = (root.current.alternate: any);
        root.finishedExpirationTime = expirationTime;
        finishSyncRender(root, workInProgressRootExitStatus, expirationTime);
      }

      // Before exiting, make sure there's a callback scheduled for the next
      // pending level.
      ensureRootIsScheduled(root);
    }
  }

  return null;
}

function finishSyncRender(root, exitStatus, expirationTime) {
  // Set this to null to indicate there's no in-progress render.
  workInProgressRoot = null;

  if (__DEV__) {
    if (exitStatus === RootSuspended || exitStatus === RootSuspendedWithDelay) {

```
### Line 1078-1090
```
    flushSyncCallbackQueue();
  }
}

export function flushDiscreteUpdates() {
  // TODO: Should be able to flush inside batchedUpdates, but not inside `act`.
  // However, `act` uses `batchedUpdates`, so there's no way to distinguish
  // those two cases. Need to fix this before exposing flushDiscreteUpdates
  // as a public API.
  if (
    (executionContext & (BatchedContext | RenderContext | CommitContext)) !==
    NoContext
  ) {

```
### Line 1093-1114
```
        false,
        'unstable_flushDiscreteUpdates: Cannot flush updates when React is ' +
          'already rendering.',
      );
    }
    // We're already rendering, so we can't synchronously flush pending work.
    // This is probably a nested event dispatch triggered by a lifecycle/effect,
    // like `el.focus()`. Exit.
    return;
  }
  flushPendingDiscreteUpdates();
  // If the discrete updates scheduled passive effects, flush them now so that
  // they fire before the next serial event.
  flushPassiveEffects();
}

export function deferredUpdates<A>(fn: () => A): A {
  // TODO: Remove in favor of Scheduler.next
  return runWithPriority(NormalPriority, fn);
}

export function syncUpdates<A, B, C, R>(

```
### Line 1120-1137
```
  return runWithPriority(ImmediatePriority, fn.bind(null, a, b, c));
}

function flushPendingDiscreteUpdates() {
  if (rootsWithPendingDiscreteUpdates !== null) {
    // For each root with pending discrete updates, schedule a callback to
    // immediately flush them.
    const roots = rootsWithPendingDiscreteUpdates;
    rootsWithPendingDiscreteUpdates = null;
    roots.forEach((expirationTime, root) => {
      markRootExpiredAtTime(root, expirationTime);
      ensureRootIsScheduled(root);
    });
    // Now flush the immediate queue.
    flushSyncCallbackQueue();
  }
}


```
### Line 1141-1150
```
  try {
    return fn(a);
  } finally {
    executionContext = prevExecutionContext;
    if (executionContext === NoContext) {
      // Flush the immediate callbacks that were scheduled during this batch
      flushSyncCallbackQueue();
    }
  }
}

```
### Line 1155-1164
```
  try {
    return fn(a);
  } finally {
    executionContext = prevExecutionContext;
    if (executionContext === NoContext) {
      // Flush the immediate callbacks that were scheduled during this batch
      flushSyncCallbackQueue();
    }
  }
}

```
### Line 1170-1184
```
  c: C,
): R {
  const prevExecutionContext = executionContext;
  executionContext |= DiscreteEventContext;
  try {
    // Should this
    return runWithPriority(UserBlockingPriority, fn.bind(null, a, b, c));
  } finally {
    executionContext = prevExecutionContext;
    if (executionContext === NoContext) {
      // Flush the immediate callbacks that were scheduled during this batch
      flushSyncCallbackQueue();
    }
  }
}

```
### Line 1190-1199
```
  try {
    return fn(a);
  } finally {
    executionContext = prevExecutionContext;
    if (executionContext === NoContext) {
      // Flush the immediate callbacks that were scheduled during this batch
      flushSyncCallbackQueue();
    }
  }
}

```
### Line 1210-1221
```
  executionContext |= BatchedContext;
  try {
    return runWithPriority(ImmediatePriority, fn.bind(null, a));
  } finally {
    executionContext = prevExecutionContext;
    // Flush the immediate callbacks that were scheduled during this batch.
    // Note that this will happen even if batchedUpdates is higher up
    // the stack.
    flushSyncCallbackQueue();
  }
}


```
### Line 1225-1234
```
  try {
    runWithPriority(ImmediatePriority, fn);
  } finally {
    executionContext = prevExecutionContext;
    if (executionContext === NoContext) {
      // Flush the immediate callbacks that were scheduled during this batch
      flushSyncCallbackQueue();
    }
  }
}

```
### Line 1237-1249
```
  root.finishedWork = null;
  root.finishedExpirationTime = NoWork;

  const timeoutHandle = root.timeoutHandle;
  if (timeoutHandle !== noTimeout) {
    // The root previous suspended and scheduled a timeout to commit a fallback
    // state. Now that we have additional work, cancel the timeout.
    root.timeoutHandle = noTimeout;
    // $FlowFixMe Complains noTimeout is not a TimeoutID, despite the check above
    cancelTimeout(timeoutHandle);
  }

  if (workInProgress !== null) {

```
### Line 1275-1302
```
}

function handleError(root, thrownValue) {
  do {
    try {
      // Reset module-level state that was set during the render phase.
      resetContextDependencies();
      resetHooks();
      resetCurrentDebugFiberInDEV();

      if (workInProgress === null || workInProgress.return === null) {
        // Expected to be working on a non-root fiber. This is a fatal error
        // because there's no ancestor that can handle it; the root is
        // supposed to capture all errors that weren't caught by an error
        // boundary.
        workInProgressRootExitStatus = RootFatalErrored;
        workInProgressRootFatalError = thrownValue;
        return null;
      }

      if (enableProfilerTimer && workInProgress.mode & ProfileMode) {
        // Record the time spent rendering before an error was thrown. This
        // avoids inaccurate Profiler durations in the case of a
        // suspended render.
        stopProfilerTimerIfRunningAndRecordDelta(workInProgress, true);
      }

      throwException(

```
### Line 1306-1330
```
        thrownValue,
        renderExpirationTime,
      );
      workInProgress = completeUnitOfWork(workInProgress);
    } catch (yetAnotherThrownValue) {
      // Something in the return path also threw.
      thrownValue = yetAnotherThrownValue;
      continue;
    }
    // Return to the normal work loop.
    return;
  } while (true);
}

function pushDispatcher(root) {
  const prevDispatcher = ReactCurrentDispatcher.current;
  ReactCurrentDispatcher.current = ContextOnlyDispatcher;
  if (prevDispatcher === null) {
    // The React isomorphic package does not include a default dispatcher.
    // Instead the first renderer will lazily attach one, in order to give
    // nicer error messages.
    return ContextOnlyDispatcher;
  } else {
    return prevDispatcher;
  }

```
### Line 1367-1376
```
    if (
      expirationTime < workInProgressRootLatestSuspenseTimeout &&
      expirationTime > Idle
    ) {
      workInProgressRootLatestSuspenseTimeout = expirationTime;
      // Most of the time we only have one config and getting wrong is not bad.
      workInProgressRootCanSuspendUsingConfig = suspenseConfig;
    }
  }
}

```
### Line 1395-1412
```
    workInProgressRootExitStatus === RootSuspended
  ) {
    workInProgressRootExitStatus = RootSuspendedWithDelay;
  }

  // Check if there's a lower priority update somewhere else in the tree.
  if (
    workInProgressRootNextUnprocessedUpdateTime !== NoWork &&
    workInProgressRoot !== null
  ) {
    // Mark the current render as suspended, and then mark that there's a
    // pending update.
    // TODO: This should immediately interrupt the current render, instead
    // of waiting until the next time we yield.
    markRootSuspendedAtTime(workInProgressRoot, renderExpirationTime);
    markRootUpdatedAtTime(
      workInProgressRoot,
      workInProgressRootNextUnprocessedUpdateTime,

```
### Line 1418-1476
```
  if (workInProgressRootExitStatus !== RootCompleted) {
    workInProgressRootExitStatus = RootErrored;
  }
}

// Called during render to determine if anything has suspended.
// Returns false if we're not sure.
export function renderHasNotSuspendedYet(): boolean {
  // If something errored or completed, we can't really be sure,
  // so those are false.
  return workInProgressRootExitStatus === RootIncomplete;
}

function inferTimeFromExpirationTime(expirationTime: ExpirationTime): number {
  // We don't know exactly when the update was scheduled, but we can infer an
  // approximate start time from the expiration time.
  const earliestExpirationTimeMs = expirationTimeToMs(expirationTime);
  return earliestExpirationTimeMs - LOW_PRIORITY_EXPIRATION;
}

function inferTimeFromExpirationTimeWithSuspenseConfig(
  expirationTime: ExpirationTime,
  suspenseConfig: SuspenseConfig,
): number {
  // We don't know exactly when the update was scheduled, but we can infer an
  // approximate start time from the expiration time by subtracting the timeout
  // that was added to the event time.
  const earliestExpirationTimeMs = expirationTimeToMs(expirationTime);
  return (
    earliestExpirationTimeMs -
    (suspenseConfig.timeoutMs | 0 || LOW_PRIORITY_EXPIRATION)
  );
}

// The work loop is an extremely hot path. Tell Closure not to inline it.
/** @noinline */
function workLoopSync() {
  // Already timed out, so perform work without checking if we need to yield.
  while (workInProgress !== null) {
    workInProgress = performUnitOfWork(workInProgress);
  }
}

/** @noinline */
function workLoopConcurrent() {
  // Perform work until Scheduler asks us to yield
  while (workInProgress !== null && !shouldYield()) {
    workInProgress = performUnitOfWork(workInProgress);
  }
}

function performUnitOfWork(unitOfWork: Fiber): Fiber | null {
  // The current, flushed, state of this fiber is the alternate. Ideally
  // nothing should rely on this, but relying on it here means that we don't
  // need an additional field on the work in progress.
  const current = unitOfWork.alternate;

  startWorkTimer(unitOfWork);
  setCurrentDebugFiberInDEV(unitOfWork);

```
### Line 1485-1513
```
  }

  resetCurrentDebugFiberInDEV();
  unitOfWork.memoizedProps = unitOfWork.pendingProps;
  if (next === null) {
    // If this doesn't spawn new work, complete the current work.
    next = completeUnitOfWork(unitOfWork);
  }

  ReactCurrentOwner.current = null;
  return next;
}

function completeUnitOfWork(unitOfWork: Fiber): Fiber | null {
  // Attempt to complete the current unit of work, then move to the next
  // sibling. If there are no more siblings, return to the parent fiber.
  workInProgress = unitOfWork;
  do {
    // The current, flushed, state of this fiber is the alternate. Ideally
    // nothing should rely on this, but relying on it here means that we don't
    // need an additional field on the work in progress.
    const current = workInProgress.alternate;
    const returnFiber = workInProgress.return;

    // Check if the work completed or if something threw.
    if ((workInProgress.effectTag & Incomplete) === NoEffect) {
      setCurrentDebugFiberInDEV(workInProgress);
      let next;
      if (

```
### Line 1516-1544
```
      ) {
        next = completeWork(current, workInProgress, renderExpirationTime);
      } else {
        startProfilerTimer(workInProgress);
        next = completeWork(current, workInProgress, renderExpirationTime);
        // Update render duration assuming we didn't error.
        stopProfilerTimerIfRunningAndRecordDelta(workInProgress, false);
      }
      stopWorkTimer(workInProgress);
      resetCurrentDebugFiberInDEV();
      resetChildExpirationTime(workInProgress);

      if (next !== null) {
        // Completing this fiber spawned new work. Work on that next.
        return next;
      }

      if (
        returnFiber !== null &&
        // Do not append effects to parents if a sibling failed to complete
        (returnFiber.effectTag & Incomplete) === NoEffect
      ) {
        // Append all the effects of the subtree and this fiber onto the effect
        // list of the parent. The completion order of the children affects the
        // side-effect order.
        if (returnFiber.firstEffect === null) {
          returnFiber.firstEffect = workInProgress.firstEffect;
        }
        if (workInProgress.lastEffect !== null) {

```
### Line 1546-1565
```
            returnFiber.lastEffect.nextEffect = workInProgress.firstEffect;
          }
          returnFiber.lastEffect = workInProgress.lastEffect;
        }

        // If this fiber had side-effects, we append it AFTER the children's
        // side-effects. We can perform certain side-effects earlier if needed,
        // by doing multiple passes over the effect list. We don't want to
        // schedule our own side-effect on our own list because if end up
        // reusing children we'll schedule this effect onto itself since we're
        // at the end.
        const effectTag = workInProgress.effectTag;

        // Skip both NoWork and PerformedWork tags when creating the effect
        // list. PerformedWork effect is read by React DevTools but shouldn't be
        // committed.
        if (effectTag > PerformedWork) {
          if (returnFiber.lastEffect !== null) {
            returnFiber.lastEffect.nextEffect = workInProgress;
          } else {

```
### Line 1567-1590
```
          }
          returnFiber.lastEffect = workInProgress;
        }
      }
    } else {
      // This fiber did not complete because something threw. Pop values off
      // the stack without entering the complete phase. If this is a boundary,
      // capture values if possible.
      const next = unwindWork(workInProgress, renderExpirationTime);

      // Because this fiber did not complete, don't reset its expiration time.

      if (
        enableProfilerTimer &&
        (workInProgress.mode & ProfileMode) !== NoMode
      ) {
        // Record the render duration for the fiber that errored.
        stopProfilerTimerIfRunningAndRecordDelta(workInProgress, false);

        // Include the time spent working on failed children before continuing.
        let actualDuration = workInProgress.actualDuration;
        let child = workInProgress.child;
        while (child !== null) {
          actualDuration += child.actualDuration;

```
### Line 1592-1629
```
        }
        workInProgress.actualDuration = actualDuration;
      }

      if (next !== null) {
        // If completing this work spawned new work, do that next. We'll come
        // back here again.
        // Since we're restarting, remove anything that is not a host effect
        // from the effect tag.
        // TODO: The name stopFailedWorkTimer is misleading because Suspense
        // also captures and restarts.
        stopFailedWorkTimer(workInProgress);
        next.effectTag &= HostEffectMask;
        return next;
      }
      stopWorkTimer(workInProgress);

      if (returnFiber !== null) {
        // Mark the parent fiber as incomplete and clear its effect list.
        returnFiber.firstEffect = returnFiber.lastEffect = null;
        returnFiber.effectTag |= Incomplete;
      }
    }

    const siblingFiber = workInProgress.sibling;
    if (siblingFiber !== null) {
      // If there is more work to do in this returnFiber, do that next.
      return siblingFiber;
    }
    // Otherwise, return to the parent
    workInProgress = returnFiber;
  } while (workInProgress !== null);

  // We've reached the root.
  if (workInProgressRootExitStatus === RootIncomplete) {
    workInProgressRootExitStatus = RootCompleted;
  }
  return null;

```
### Line 1640-1669
```
function resetChildExpirationTime(completedWork: Fiber) {
  if (
    renderExpirationTime !== Never &&
    completedWork.childExpirationTime === Never
  ) {
    // The children of this component are hidden. Don't bubble their
    // expiration times.
    return;
  }

  let newChildExpirationTime = NoWork;

  // Bubble up the earliest expiration time.
  if (enableProfilerTimer && (completedWork.mode & ProfileMode) !== NoMode) {
    // In profiling mode, resetChildExpirationTime is also used to reset
    // profiler durations.
    let actualDuration = completedWork.actualDuration;
    let treeBaseDuration = completedWork.selfBaseDuration;

    // When a fiber is cloned, its actualDuration is reset to 0. This value will
    // only be updated if work is done on the fiber (i.e. it doesn't bailout).
    // When work is done, it should bubble to the parent's actualDuration. If
    // the fiber has not been cloned though, (meaning no work was done), then
    // this value will reflect the amount of time spent working on a previous
    // render. In that case it should not bubble. We determine whether it was
    // cloned by comparing the child pointer.
    const shouldBubbleActualDurations =
      completedWork.alternate === null ||
      completedWork.child !== completedWork.alternate.child;


```
### Line 1733-1752
```
    finishedWork !== root.current,
    'Cannot commit the same tree as before. This error is likely caused by ' +
      'a bug in React. Please file an issue.',
  );

  // commitRoot never returns a continuation; it always finishes synchronously.
  // So we can clear these now to allow a new callback to be scheduled.
  root.callbackNode = null;
  root.callbackExpirationTime = NoWork;
  root.callbackPriority = NoPriority;
  root.nextKnownPendingLevel = NoWork;

  startCommitTimer();

  // Update the first and last pending times on this root. The new first
  // pending time is whatever is left on the root fiber.
  const remainingExpirationTimeBeforeCommit = getRemainingExpirationTime(
    finishedWork,
  );
  markRootFinishedAtTime(

```
### Line 1754-1805
```
    expirationTime,
    remainingExpirationTimeBeforeCommit,
  );

  if (root === workInProgressRoot) {
    // We can reset these now that they are finished.
    workInProgressRoot = null;
    workInProgress = null;
    renderExpirationTime = NoWork;
  } else {
    // This indicates that the last root we worked on is not the same one that
    // we're committing now. This most commonly happens when a suspended root
    // times out.
  }

  // Get the list of effects.
  let firstEffect;
  if (finishedWork.effectTag > PerformedWork) {
    // A fiber's effect list consists only of its children, not itself. So if
    // the root has an effect, we need to add it to the end of the list. The
    // resulting list is the set that would belong to the root's parent, if it
    // had one; that is, all the effects in the tree including the root.
    if (finishedWork.lastEffect !== null) {
      finishedWork.lastEffect.nextEffect = finishedWork;
      firstEffect = finishedWork.firstEffect;
    } else {
      firstEffect = finishedWork;
    }
  } else {
    // There is no effect on the root.
    firstEffect = finishedWork.firstEffect;
  }

  if (firstEffect !== null) {
    const prevExecutionContext = executionContext;
    executionContext |= CommitContext;
    const prevInteractions = pushInteractions(root);

    // Reset this to null before calling lifecycles
    ReactCurrentOwner.current = null;

    // The commit phase is broken into several sub-phases. We do a separate pass
    // of the effect list for each phase: all mutation effects come before all
    // layout effects, and so on.

    // The first phase a "before mutation" phase. We use this phase to read the
    // state of the host tree right before we mutate it. This is where
    // getSnapshotBeforeUpdate is called.
    startCommitSnapshotEffectsTimer();
    prepareForCommit(root.containerInfo);
    nextEffect = firstEffect;
    do {

```
### Line 1822-1836
```
      }
    } while (nextEffect !== null);
    stopCommitSnapshotEffectsTimer();

    if (enableProfilerTimer) {
      // Mark the current commit time to be shared by all Profilers in this
      // batch. This enables them to be grouped later.
      recordCommitTime();
    }

    // The next phase is the mutation phase, where we mutate the host tree.
    startCommitHostEffectsTimer();
    nextEffect = firstEffect;
    do {
      if (__DEV__) {

```
### Line 1858-1875
```
      }
    } while (nextEffect !== null);
    stopCommitHostEffectsTimer();
    resetAfterCommit(root.containerInfo);

    // The work-in-progress tree is now the current tree. This must come after
    // the mutation phase, so that the previous tree is still current during
    // componentWillUnmount, but before the layout phase, so that the finished
    // work is current during componentDidMount/Update.
    root.current = finishedWork;

    // The next phase is the layout phase, where we call effects that read
    // the host tree after it's been mutated. The idiomatic use case for this is
    // layout, but class component lifecycles also fire here for legacy reasons.
    startCommitLifeCyclesTimer();
    nextEffect = firstEffect;
    do {
      if (__DEV__) {

```
### Line 1898-1920
```
    } while (nextEffect !== null);
    stopCommitLifeCyclesTimer();

    nextEffect = null;

    // Tell Scheduler to yield at the end of the frame, so the browser has an
    // opportunity to paint.
    requestPaint();

    if (enableSchedulerTracing) {
      popInteractions(((prevInteractions: any): Set<Interaction>));
    }
    executionContext = prevExecutionContext;
  } else {
    // No effects.
    root.current = finishedWork;
    // Measure these anyway so the flamegraph explicitly shows that there were
    // no effects.
    // TODO: Maybe there's a better way to report this.
    startCommitSnapshotEffectsTimer();
    stopCommitSnapshotEffectsTimer();
    if (enableProfilerTimer) {
      recordCommitTime();

```
### Line 1928-1955
```
  stopCommitTimer();

  const rootDidHavePassiveEffects = rootDoesHavePassiveEffects;

  if (rootDoesHavePassiveEffects) {
    // This commit has passive effects. Stash a reference to them. But don't
    // schedule a callback until after flushing layout work.
    rootDoesHavePassiveEffects = false;
    rootWithPendingPassiveEffects = root;
    pendingPassiveEffectsExpirationTime = expirationTime;
    pendingPassiveEffectsRenderPriority = renderPriorityLevel;
  } else {
    // We are done with the effect chain at this point so let's clear the
    // nextEffect pointers to assist with GC. If we have passive effects, we'll
    // clear this in flushPassiveEffects.
    nextEffect = firstEffect;
    while (nextEffect !== null) {
      const nextNextEffect = nextEffect.nextEffect;
      nextEffect.nextEffect = null;
      nextEffect = nextNextEffect;
    }
  }

  // Check if there's remaining work on this root
  const remainingExpirationTime = root.firstPendingTime;
  if (remainingExpirationTime !== NoWork) {
    if (enableSchedulerTracing) {
      if (spawnedWorkDuringRender !== null) {

```
### Line 1964-1990
```
        }
      }
      schedulePendingInteractions(root, remainingExpirationTime);
    }
  } else {
    // If there's no remaining work, we can clear the set of already failed
    // error boundaries.
    legacyErrorBoundariesThatAlreadyFailed = null;
  }

  if (enableSchedulerTracing) {
    if (!rootDidHavePassiveEffects) {
      // If there are no passive effects, then we can complete the pending interactions.
      // Otherwise, we'll wait until after the passive effects are flushed.
      // Wait to do this until after remaining work has been scheduled,
      // so that we don't prematurely signal complete for interactions when there's e.g. hidden work.
      finishPendingInteractions(root, expirationTime);
    }
  }

  if (remainingExpirationTime === Sync) {
    // Count the number of times the root synchronously re-renders without
    // finishing. If there are too many, it indicates an infinite update loop.
    if (root === rootWithNestedUpdates) {
      nestedUpdateCount++;
    } else {
      nestedUpdateCount = 0;

```
### Line 1994-2004
```
    nestedUpdateCount = 0;
  }

  onCommitRoot(finishedWork.stateNode, expirationTime);

  // Always call this before exiting `commitRoot`, to ensure that any
  // additional work on this root is scheduled.
  ensureRootIsScheduled(root);

  if (hasUncaughtError) {
    hasUncaughtError = false;

```
### Line 2006-2022
```
    firstUncaughtError = null;
    throw error;
  }

  if ((executionContext & LegacyUnbatchedContext) !== NoContext) {
    // This is a legacy edge case. We just committed the initial mount of
    // a ReactDOM.render-ed root inside of batchedUpdates. The commit fired
    // synchronously, but layout updates should be deferred until the end
    // of the batch.
    return null;
  }

  // If layout work was scheduled, flush it now.
  flushSyncCallbackQueue();
  return null;
}


```
### Line 2031-2041
```
      commitBeforeMutationEffectOnFiber(current, nextEffect);

      resetCurrentDebugFiberInDEV();
    }
    if ((effectTag & Passive) !== NoEffect) {
      // If there are passive effects, schedule a callback to flush at
      // the earliest opportunity.
      if (!rootDoesHavePassiveEffects) {
        rootDoesHavePassiveEffects = true;
        scheduleCallback(NormalPriority, () => {
          flushPassiveEffects();

```
### Line 2046-2055
```
    nextEffect = nextEffect.nextEffect;
  }
}

function commitMutationEffects(root: FiberRoot, renderPriorityLevel) {
  // TODO: Should probably move the bulk of this function to commitWork.
  while (nextEffect !== null) {
    setCurrentDebugFiberInDEV(nextEffect);

    const effectTag = nextEffect.effectTag;

```
### Line 2063-2095
```
      if (current !== null) {
        commitDetachRef(current);
      }
    }

    // The following switch statement is only concerned about placement,
    // updates, and deletions. To avoid needing to add a case for every possible
    // bitmap value, we remove the secondary effects from the effect tag and
    // switch on that value.
    let primaryEffectTag =
      effectTag & (Placement | Update | Deletion | Hydrating);
    switch (primaryEffectTag) {
      case Placement: {
        commitPlacement(nextEffect);
        // Clear the "placement" from effect tag so that we know that this is
        // inserted, before any life-cycles like componentDidMount gets called.
        // TODO: findDOMNode doesn't rely on this any more but isMounted does
        // and isMounted is deprecated anyway so we should be able to kill this.
        nextEffect.effectTag &= ~Placement;
        break;
      }
      case PlacementAndUpdate: {
        // Placement
        commitPlacement(nextEffect);
        // Clear the "placement" from effect tag so that we know that this is
        // inserted, before any life-cycles like componentDidMount gets called.
        nextEffect.effectTag &= ~Placement;

        // Update
        const current = nextEffect.alternate;
        commitWork(current, nextEffect);
        break;
      }

```
### Line 2098-2107
```
        break;
      }
      case HydratingAndUpdate: {
        nextEffect.effectTag &= ~Hydrating;

        // Update
        const current = nextEffect.alternate;
        commitWork(current, nextEffect);
        break;
      }

```
### Line 2114-2123
```
        commitDeletion(root, nextEffect, renderPriorityLevel);
        break;
      }
    }

    // TODO: Only record a mutation effect if primaryEffectTag is non-zero.
    recordEffect();

    resetCurrentDebugFiberInDEV();
    nextEffect = nextEffect.nextEffect;

```
### Line 2126-2135
```

function commitLayoutEffects(
  root: FiberRoot,
  committedExpirationTime: ExpirationTime,
) {
  // TODO: Should probably move the bulk of this function to commitWork.
  while (nextEffect !== null) {
    setCurrentDebugFiberInDEV(nextEffect);

    const effectTag = nextEffect.effectTag;

```
### Line 2181-2192
```
  );
  const prevExecutionContext = executionContext;
  executionContext |= CommitContext;
  const prevInteractions = pushInteractions(root);

  // Note: This currently assumes there are no passive effects on the root
  // fiber, because the root is not part of its own effect list. This could
  // change in the future.
  let effect = root.current.firstEffect;
  while (effect !== null) {
    if (__DEV__) {
      setCurrentDebugFiberInDEV(effect);

```
### Line 2204-2213
```
        invariant(effect !== null, 'Should be working on an effect.');
        captureCommitPhaseError(effect, error);
      }
    }
    const nextNextEffect = effect.nextEffect;
    // Remove nextEffect pointer to assist GC
    effect.nextEffect = null;
    effect = nextNextEffect;
  }


```
### Line 2218-2228
```

  executionContext = prevExecutionContext;

  flushSyncCallbackQueue();

  // If additional passive effects were scheduled, increment a counter. If this
  // exceeds the limit, we'll fire a warning.
  nestedPassiveUpdateCount =
    rootWithPendingPassiveEffects === null ? 0 : nestedPassiveUpdateCount + 1;

  return true;

```
### Line 2266-2276
```
  }
}

export function captureCommitPhaseError(sourceFiber: Fiber, error: mixed) {
  if (sourceFiber.tag === HostRoot) {
    // Error was thrown at the root. There is no parent, so the root
    // itself should capture it.
    captureCommitPhaseErrorOnRoot(sourceFiber, sourceFiber, error);
    return;
  }


```
### Line 2289-2298
```
      ) {
        const errorInfo = createCapturedValue(error, sourceFiber);
        const update = createClassErrorUpdate(
          fiber,
          errorInfo,
          // TODO: This is always sync
          Sync,
        );
        enqueueUpdate(fiber, update);
        const root = markUpdateTimeFromFiberToRoot(fiber, Sync);

```
### Line 2312-2372
```
  thenable: Thenable,
  suspendedTime: ExpirationTime,
) {
  const pingCache = root.pingCache;
  if (pingCache !== null) {
    // The thenable resolved, so we no longer need to memoize, because it will
    // never be thrown again.
    pingCache.delete(thenable);
  }

  if (workInProgressRoot === root && renderExpirationTime === suspendedTime) {
    // Received a ping at the same priority level at which we're currently
    // rendering. We might want to restart this render. This should mirror
    // the logic of whether or not a root suspends once it completes.

    // TODO: If we're rendering sync either due to Sync, Batched or expired,
    // we should probably never restart.

    // If we're suspended with delay, we'll always suspend so we can always
    // restart. If we're suspended without any updates, it might be a retry.
    // If it's early in the retry we can restart. We can't know for sure
    // whether we'll eventually process an update during this render pass,
    // but it's somewhat unlikely that we get to a ping before that, since
    // getting to the root most update is usually very fast.
    if (
      workInProgressRootExitStatus === RootSuspendedWithDelay ||
      (workInProgressRootExitStatus === RootSuspended &&
        workInProgressRootLatestProcessedExpirationTime === Sync &&
        now() - globalMostRecentFallbackTime < FALLBACK_THROTTLE_MS)
    ) {
      // Restart from the root. Don't need to schedule a ping because
      // we're already working on this tree.
      prepareFreshStack(root, renderExpirationTime);
    } else {
      // Even though we can't restart right now, we might get an
      // opportunity later. So we mark this render as having a ping.
      workInProgressRootHasPendingPing = true;
    }
    return;
  }

  if (!isRootSuspendedAtTime(root, suspendedTime)) {
    // The root is no longer suspended at this time.
    return;
  }

  const lastPingedTime = root.lastPingedTime;
  if (lastPingedTime !== NoWork && lastPingedTime < suspendedTime) {
    // There's already a lower priority ping scheduled.
    return;
  }

  // Mark the time at which this ping was scheduled.
  root.lastPingedTime = suspendedTime;

  if (root.finishedExpirationTime === suspendedTime) {
    // If there's a pending fallback waiting to commit, throw it away.
    root.finishedExpirationTime = NoWork;
    root.finishedWork = null;
  }


```
### Line 2376-2388
```

function retryTimedOutBoundary(
  boundaryFiber: Fiber,
  retryTime: ExpirationTime,
) {
  // The boundary fiber (a Suspense component or SuspenseList component)
  // previously was rendered in its fallback state. One of the promises that
  // suspended it has resolved, which means at least part of the tree was
  // likely unblocked. Try rendering again, at a new expiration time.
  if (retryTime === NoWork) {
    const suspenseConfig = null; // Retries don't carry over the already committed update.
    const currentTime = requestCurrentTimeForUpdate();
    retryTime = computeExpirationForFiber(

```
### Line 2389-2398
```
      currentTime,
      boundaryFiber,
      suspenseConfig,
    );
  }
  // TODO: Special case idle priority?
  const root = markUpdateTimeFromFiberToRoot(boundaryFiber, retryTime);
  if (root !== null) {
    ensureRootIsScheduled(root);
    schedulePendingInteractions(root, retryTime);

```
### Line 2433-2458
```
  } else {
    retryCache = boundaryFiber.stateNode;
  }

  if (retryCache !== null) {
    // The thenable resolved, so we no longer need to memoize, because it will
    // never be thrown again.
    retryCache.delete(thenable);
  }

  retryTimedOutBoundary(boundaryFiber, retryTime);
}

// Computes the next Just Noticeable Difference (JND) boundary.
// The theory is that a person can't tell the difference between small differences in time.
// Therefore, if we wait a bit longer than necessary that won't translate to a noticeable
// difference in the experience. However, waiting for longer might mean that we can avoid
// showing an intermediate loading state. The longer we have already waited, the harder it
// is to tell small differences in time. Therefore, the longer we've already waited,
// the longer we can wait additionally. At some point we have to give up though.
// We pick a train model where the next boundary commits at a consistent schedule.
// These particular numbers are vague estimates. We expect to adjust them based on research.
function jnd(timeElapsed: number) {
  return timeElapsed < 120
    ? 120
    : timeElapsed < 480

```
### Line 2477-2499
```
  if (busyMinDurationMs <= 0) {
    return 0;
  }
  const busyDelayMs = (suspenseConfig.busyDelayMs: any) | 0;

  // Compute the time until this render pass would expire.
  const currentTimeMs: number = now();
  const eventTimeMs: number = inferTimeFromExpirationTimeWithSuspenseConfig(
    mostRecentEventTime,
    suspenseConfig,
  );
  const timeElapsed = currentTimeMs - eventTimeMs;
  if (timeElapsed <= busyDelayMs) {
    // If we haven't yet waited longer than the initial delay, we don't
    // have to wait any additional time.
    return 0;
  }
  const msUntilTimeout = busyDelayMs + busyMinDurationMs - timeElapsed;
  // This is the value that is passed to `setTimeout`.
  return msUntilTimeout;
}

function checkForNestedUpdates() {

```
### Line 2538-2547
```
  stopWorkLoopTimer(interruptedBy, didCompleteRoot);
  interruptedBy = null;
}

function stopInterruptedWorkLoopTimer() {
  // TODO: Track which fiber caused the interruption.
  const didCompleteRoot = false;
  stopWorkLoopTimer(interruptedBy, didCompleteRoot);
  interruptedBy = null;
}

```
### Line 2569-2582
```
      tag !== FunctionComponent &&
      tag !== ForwardRef &&
      tag !== MemoComponent &&
      tag !== SimpleMemoComponent
    ) {
      // Only warn for user-defined components, not internal ones like Suspense.
      return;
    }
    // We show the whole stack but dedupe on the top component's name because
    // the problematic code almost always lies inside that component.
    const componentName = getComponentName(fiber.type) || 'ReactComponent';
    if (didWarnStateUpdateForUnmountedComponent !== null) {
      if (didWarnStateUpdateForUnmountedComponent.has(componentName)) {
        return;

```
### Line 2600-2614
```

let beginWork;
if (__DEV__ && replayFailedUnitOfWorkWithInvokeGuardedCallback) {
  let dummyFiber = null;
  beginWork = (current, unitOfWork, expirationTime) => {
    // If a component throws an error, we replay it again in a synchronously
    // dispatched event, so that the debugger will treat it as an uncaught
    // error See ReactErrorUtils for more information.

    // Before entering the begin phase, copy the work-in-progress onto a dummy
    // fiber. If beginWork throws, we'll use this to reset the state.
    const originalWorkInProgressCopy = assignFiberPropertiesInDEV(
      dummyFiber,
      unitOfWork,
    );

```
### Line 2618-2649
```
      if (
        originalError !== null &&
        typeof originalError === 'object' &&
        typeof originalError.then === 'function'
      ) {
        // Don't replay promises. Treat everything else like an error.
        throw originalError;
      }

      // Keep this code in sync with handleError; any changes here must have
      // corresponding changes there.
      resetContextDependencies();
      resetHooks();
      // Don't reset current debug fiber, since we're about to work on the
      // same fiber again.

      // Unwind the failed stack frame
      unwindInterruptedWork(unitOfWork);

      // Restore the original properties of the fiber.
      assignFiberPropertiesInDEV(unitOfWork, originalWorkInProgressCopy);

      if (enableProfilerTimer && unitOfWork.mode & ProfileMode) {
        // Reset the profiler timer.
        startProfilerTimer(unitOfWork);
      }

      // Run beginWork again.
      invokeGuardedCallback(
        null,
        originalBeginWork,
        null,

```
### Line 2652-2665
```
        expirationTime,
      );

      if (hasCaughtError()) {
        const replayError = clearCaughtError();
        // `invokeGuardedCallback` sometimes sets an expando `_suppressLogging`.
        // Rethrow this error instead of the original one.
        throw replayError;
      } else {
        // This branch is reachable if the render phase is impure.
        throw originalError;
      }
    }
  };

```
### Line 2698-2707
```
      }
    }
  }
}

// a 'shared' variable that changes when act() opens/closes in tests.
export const IsThisRendererActing = {current: (false: boolean)};

export function warnIfNotScopedWithMatchingAct(fiber: Fiber): void {
  if (__DEV__) {

```
### Line 2786-2800
```
  }
}

export const warnIfNotCurrentlyActingUpdatesInDev = warnIfNotCurrentlyActingUpdatesInDEV;

// In tests, we want to enforce a mocked scheduler.
let didWarnAboutUnmockedScheduler = false;
// TODO Before we release concurrent mode, revisit this and decide whether a mocked
// scheduler is the actual recommendation. The alternative could be a testing build,
// a new lib, or whatever; we dunno just yet. This message is for early adopters
// to get their tests right.

export function warnIfUnmockedScheduler(fiber: Fiber) {
  if (__DEV__) {
    if (

```
### Line 2835-2852
```
      (currentPriorityLevel === UserBlockingPriority ||
        currentPriorityLevel === ImmediatePriority)
    ) {
      let workInProgressNode = sourceFiber;
      while (workInProgressNode !== null) {
        // Add the component that triggered the suspense
        const current = workInProgressNode.alternate;
        if (current !== null) {
          // TODO: warn component that triggers the high priority
          // suspend is the HostRoot
          switch (workInProgressNode.tag) {
            case ClassComponent:
              // Loop through the component's update queue and see whether the component
              // has triggered any high priority updates
              const updateQueue = current.updateQueue;
              if (updateQueue !== null) {
                let update = updateQueue.firstUpdate;
                while (update !== null) {

```
### Line 2876-2886
```
              if (
                workInProgressNode.memoizedState !== null &&
                workInProgressNode.memoizedState.baseUpdate !== null
              ) {
                let update = workInProgressNode.memoizedState.baseUpdate;
                // Loop through the functional component's memoized state to see whether
                // the component has triggered any high pri updates
                while (update !== null) {
                  const priority = update.priority;
                  if (
                    priority === UserBlockingPriority ||

```
### Line 2934-2952
```
            'update to provide immediate feedback, and another update that ' +
            'triggers the bulk of the changes.' +
            '\n\n' +
            'Refer to the documentation for useTransition to learn how ' +
            'to implement this pattern.',
          // TODO: Add link to React docs with more information, once it exists
          componentNames.sort().join(', '),
        );
      }
    }
  }
}

function computeThreadID(root, expirationTime) {
  // Interaction threads are unique per root and expiration time.
  return expirationTime * 1000 + root.interactionThreadID;
}

export function markSpawnedWork(expirationTime: ExpirationTime) {

```
### Line 2969-2987
```
    const pendingInteractionMap = root.pendingInteractionMap;
    const pendingInteractions = pendingInteractionMap.get(expirationTime);
    if (pendingInteractions != null) {
      interactions.forEach(interaction => {
        if (!pendingInteractions.has(interaction)) {
          // Update the pending async work count for previously unscheduled interaction.
          interaction.__count++;
        }

        pendingInteractions.add(interaction);
      });
    } else {
      pendingInteractionMap.set(expirationTime, new Set(interactions));

      // Update the pending async work count for the current interactions.
      interactions.forEach(interaction => {
        interaction.__count++;
      });
    }

```
### Line 2993-3020
```
    }
  }
}

function schedulePendingInteractions(root, expirationTime) {
  // This is called when work is scheduled on a root.
  // It associates the current interactions with the newly-scheduled expiration.
  // They will be restored when that expiration is later committed.
  if (!enableSchedulerTracing) {
    return;
  }

  scheduleInteractions(root, expirationTime, __interactionsRef.current);
}

function startWorkOnPendingInteractions(root, expirationTime) {
  // This is called when new work is started on a root.
  if (!enableSchedulerTracing) {
    return;
  }

  // Determine which interactions this batch of work currently includes, So that
  // we can accurately attribute time spent working on it, And so that cascading
  // work triggered during the render phase will be associated with it.
  const interactions: Set<Interaction> = new Set();
  root.pendingInteractionMap.forEach(
    (scheduledInteractions, scheduledExpirationTime) => {
      if (scheduledExpirationTime >= expirationTime) {

```
### Line 3023-3036
```
        );
      }
    },
  );

  // Store the current set of interactions on the FiberRoot for a few reasons:
  // We can re-use it in hot functions like performConcurrentWorkOnRoot()
  // without having to recalculate it. We will also use it in commitWork() to
  // pass to any Profiler onRender() hooks. This also provides DevTools with a
  // way to access it when the onCommitRoot() hook is called.
  root.memoizedInteractions = interactions;

  if (interactions.size > 0) {
    const subscriber = __subscriberRef.current;

```
### Line 3037-3046
```
    if (subscriber !== null) {
      const threadID = computeThreadID(root, expirationTime);
      try {
        subscriber.onWorkStarted(interactions, threadID);
      } catch (error) {
        // If the subscriber throws, rethrow it in a separate task
        scheduleCallback(ImmediatePriority, () => {
          throw error;
        });
      }

```
### Line 3062-3084
```
    if (subscriber !== null && root.memoizedInteractions.size > 0) {
      const threadID = computeThreadID(root, committedExpirationTime);
      subscriber.onWorkStopped(root.memoizedInteractions, threadID);
    }
  } catch (error) {
    // If the subscriber throws, rethrow it in a separate task
    scheduleCallback(ImmediatePriority, () => {
      throw error;
    });
  } finally {
    // Clear completed interactions from the pending Map.
    // Unless the render was suspended or cascading work was scheduled,
    // In which caseâ€“ leave pending interactions until the subsequent render.
    const pendingInteractionMap = root.pendingInteractionMap;
    pendingInteractionMap.forEach(
      (scheduledInteractions, scheduledExpirationTime) => {
        // Only decrement the pending interaction count if we're done.
        // If there's still work at the current priority,
        // That indicates that we are waiting for suspense data.
        if (scheduledExpirationTime > earliestRemainingTimeAfterCommit) {
          pendingInteractionMap.delete(scheduledExpirationTime);

          scheduledInteractions.forEach(interaction => {

```
### Line 3086-3095
```

            if (subscriber !== null && interaction.__count === 0) {
              try {
                subscriber.onInteractionScheduledWorkCompleted(interaction);
              } catch (error) {
                // If the subscriber throws, rethrow it in a separate task
                scheduleCallback(ImmediatePriority, () => {
                  throw error;
                });
              }

```

## _packages_react_devtools_shared_src_tests_profilerStore_test_js

## _packages_react_dom_src_tests_ReactTestUtils_test_js
### Line 47-59
```
    class MockedComponent extends React.Component {
      render() {
        throw new Error('Should not get here.');
      }
    }
    // This is close enough to what a Jest mock would give us.
    MockedComponent.prototype.render = jest.fn();

    // Patch it up so it returns its children.
    expect(() =>
      ReactTestUtils.mockComponent(MockedComponent),
    ).toLowPriorityWarnDev(
      'ReactTestUtils.mockComponent() is deprecated. ' +

```
### Line 60-69
```
        'Use shallow rendering or jest.mock() instead.\n\n' +
        'See https://fb.me/test-utils-mock-component for more information.',
      {withoutStack: true},
    );

    // De-duplication check
    ReactTestUtils.mockComponent(MockedComponent);

    const container = document.createElement('div');
    ReactDOM.render(<MockedComponent>Hello</MockedComponent>, container);

```
### Line 205-214
```
      if (ReactTestUtils.isDOMComponent(child)) {
        log.push(ReactDOM.findDOMNode(child).textContent);
      }
    });

    // Should be document order, not mount order (which would be purple, orange)
    expect(log).toEqual(['orangepurple', 'orange', 'purple']);
  });

  it('should support injected wrapper components as DOM components', () => {

```
### Line 229-239
```
      );
      expect(testComponent.tagName).toBe(type.toUpperCase());
      expect(ReactTestUtils.isDOMComponent(testComponent)).toBe(true);
    });

    // Full-page components (html, head, body) can't be rendered into a div
    // directly...
    class Root extends React.Component {
      render() {
        return (
          <html ref="html">

```
### Line 280-289
```
    const hrs = ReactTestUtils.scryRenderedDOMComponentsWithTag(inst, 'hr');
    expect(hrs.length).toBe(2);
  });

  it('provides a clear error when passing invalid objects to scry', () => {
    // This is probably too relaxed but it's existing behavior.
    ReactTestUtils.findAllInRenderedTree(null, 'span');
    ReactTestUtils.findAllInRenderedTree(undefined, 'span');
    ReactTestUtils.findAllInRenderedTree('', 'span');
    ReactTestUtils.findAllInRenderedTree(0, 'span');

```

## _packages_react_dom_src_events_SyntheticWheelEvent_js
### Line 31-43
```
          ? -event.wheelDelta
          : 0;
  },
  deltaZ: null,

  // Browsers without "deltaMode" is reporting in raw wheel delta where one
  // notch on the scroll is always +/- 120, roughly equivalent to pixels.
  // A good approximation of DOM_DELTA_LINE (1) is 5% of viewport size or
  // ~40 pixels, for DOM_DELTA_SCREEN (2) it is 87.5% of viewport size.
  deltaMode: null,
});

export default SyntheticWheelEvent;

```

## _packages_react_art_npm_Rectangle_js
### Line 54-64
```
  render: function render() {
    var width = this.props.width;
    var height = this.props.height;
    var radius = this.props.radius ? this.props.radius : 0;

    // if unspecified, radius(Top|Bottom)(Left|Right) defaults to the radius
    // property
    var tl = this.props.radiusTopLeft ? this.props.radiusTopLeft : radius;
    var tr = this.props.radiusTopRight ? this.props.radiusTopRight : radius;
    var br = this.props.radiusBottomRight
      ? this.props.radiusBottomRight

```
### Line 65-75
```
      : radius;
    var bl = this.props.radiusBottomLeft ? this.props.radiusBottomLeft : radius;

    var path = Path();

    // for negative width/height, offset the rectangle in the negative x/y
    // direction. for negative radius, just default to 0.
    if (width < 0) {
      path.move(width, 0);
      width = -width;
    }

```
### Line 88-98
```
    }
    if (bl < 0) {
      bl = 0;
    }

    // disable border radius if it doesn't fit within the specified
    // width/height
    if (tl + tr > width) {
      tl = 0;
      tr = 0;
    }

```

## _packages_react_devtools_shared_src_devtools_views_Profiler_CommitFlamegraphListItem_js
### Line 40-52
```
      selectFiber(id, name);
    },
    [selectFiber],
  );

  // List items are absolutely positioned using the CSS "top" attribute.
  // The "left" value will always be 0.
  // Since height is fixed, and width is based on the node's duration,
  // We can ignore those values as well.
  const top = parseInt(style.top, 10);

  const row = rows[index];


```
### Line 69-84
```
        } = chartNode;

        const nodeOffset = scaleX(offset, width);
        const nodeWidth = scaleX(treeBaseDuration, width);

        // Filter out nodes that are too small to see or click.
        // This also helps render large trees faster.
        if (nodeWidth < barWidthThreshold) {
          return null;
        }

        // Filter out nodes that are outside of the horizontal window.
        if (
          nodeOffset + nodeWidth < selectedNodeOffset ||
          nodeOffset > selectedNodeOffset + width
        ) {

```

## _packages_react_dom_src_tests_ReactErrorLoggingRecovery_test_js
### Line 6-27
```
 *
 * @emails react-core
 * @jest-environment node
 */

// This is a regression test for https://github.com/facebook/react/issues/13188.
// It reproduces a combination of conditions that led to a problem.

if (global.window) {
  throw new Error('This test must run in a Node environment.');
}

// The issue only reproduced when React was loaded before JSDOM.
const React = require('react');
const ReactDOM = require('react-dom');

// Initialize JSDOM separately.
// We don't use our normal JSDOM setup because we want to load React first.
const {JSDOM} = require('jsdom');
global.requestAnimationFrame = setTimeout;
global.cancelAnimationFrame = clearTimeout;
const jsdom = new JSDOM(`<div id="app-root"></div>`);

```
### Line 63-72
```
    }
    expect(didCatch).toBe(true);
    ReactDOM.render(<span>Hello</span>, div);
    expect(div.firstChild.textContent).toBe('Hello');

    // Verify the console.error bug is surfaced
    expect(() => {
      jest.runAllTimers();
    }).toThrow('Buggy console.error');
  });

```

# Issues
## 16193
Title:
```

        Bug: Environment variables with '$' are modified on Linux
      
```
Author:
```
thebananeman
```
Text:
```

I report this issue here since I didn't find any occurence of it anywhere else.
What is the current behavior?
Right now whenever I want to read an env variable in the process.env object whose value contains a dollar sign '$'. The value is modified once passed to react and replaced by the corresponding env variable.
For example: If I type the following in my terminal :
export REACT_APP_EXAMPLE="my\$value"
If I check again in the terminal I have :
echo $REACT_APP_EXAMPLE 
my$value

But once my app is launched, React replace the portion followed by the '$' by the content of the 'value' environment variable (empty by default). So if for example I want to log it, I will have :
console.log(process.env.REACT_APP_EXAMPLE);
-> my

And if my 'value' variable is set :
export value=something
console.log(process.env.REACT_APP_EXAMPLE);
-> mysomething

What is the expected behavior?
React should give the proper value and not overriding its content because of special characters. Especially since I used double quotes and backslash expression to avoid the confusion when setting the variables.
This seems to be an issue with React when it redefines and filters the process.env object since I don't have this issue with plain JS or when running a node console.
For now I use dotenv to avoid that behaviour but it is still an issue worthy of note.
Which versions of React, and which browser / OS are affected by this issue?
React v.16.8.6
OS: Ubuntu 16.04

```
Author:
```
threepointone
```
Text:
```

You should file this issue at https://github.com/facebook/create-react-app/issues

```

## 2976
Title:
```

        style expecting an object has unfortunate consequences. 
      
```
Author:
```
aronallen
```
Text:
```

Hi,
I am pretty new to react, and I am trying to build a DIV that requests an image-scaling service on the backend for images in specific resolutions, to do this I need to use CSS image-set, this CSS value need vendor prefixes, but the CSS key does not, my problem is that I can't have duplicate keys in the style object. I ended up manually setting the style attribute in componentDidUpdate, but it is a hack to get around the system. I suggest that you could perhaps also expect an array of key value pairs, then I could do like this:
[{backgroundImage : 'value1'}, {backgroundImage : 'value 2'}]

a specific example of the css I am trying to modify can be found here.
height : 818px;
width : 1440px;
background-size : cover;
background-image : url(https://images.blockbuster.dk/movie/divergent?width=1440&height=818);
background-image : -webkit-image-set(url(https://images.blockbuster.dk/movie/divergent?width=1440&height=818) 1.0x, url(https://images.blockbuster.dk/movie/divergent?width=2880&height=1636) 2.0x);
background-image : -moz-image-set(url(https://images.blockbuster.dk/movie/divergent?width=1440&height=818) 1.0x, url(https://images.blockbuster.dk/movie/divergent?width=2880&height=1636) 2.0x);
background-image : -ms-image-set(url(https://images.blockbuster.dk/movie/divergent?width=1440&height=818) 1.0x, url(https://images.blockbuster.dk/movie/divergent?width=2880&height=1636) 2.0x);
background-image : -o-image-set(url(https://images.blockbuster.dk/movie/divergent?width=1440&height=818) 1.0x, url(https://images.blockbuster.dk/movie/divergent?width=2880&height=1636) 2.0x)


```
Author:
```
aronallen
```
Text:
```

I also tried to add spaces to the backgroundImage key, but react reacted and didn't let me.

```
Author:
```
syranide
```
Text:
```

Feature detection is the go-to solution (at least for now) I believe.
EDIT: Supplying an array of rules is complicated because updating any of them would require reapplying all of them in order, which could be quite costly. But this is an area where nothing is really decided yet I believe, but feature detection is the solution for now (or use CSS which is probably preferable unless it's dynamic, which it seems it is).

```
Author:
```
zpao
```
Text:
```

Yea, we've suggested feature detection for this case. It's not bullet-proof (eg, won't work for server-rendering).
Otherwise yes, this is an area where unfortunately using objects doesn't work out perfectly. But there isn't really anything we can do, we're not going to change style to a string.

```

## 2569
Title:
```

        [EDIT]: No error thrown on missing mixin (Formerly named "Mixin lifecycle methods not called server-side")
      
```
Author:
```
jwietelmann
```
Text:
```

MyComponentWithMyMixin.componentWillMount gets called, but MyMixin.componentWillMount never does.
Granted I'm using an older version and didn't dig into latest source too hard, but I didn't see this pop up in an issues search.

```
Author:
```
cody
```
Text:
```

It works for me: http://jsfiddle.net/kb3gN/7874/
Can you make a small example that shows your problem?

```
Author:
```
aackerman
```
Text:
```

This doesn't appear to be reproducible with 0.12.1 react or react with addons, gist here. At least on node v0.10.28.
What is your version of React, Node, and are you using React with addons?

```
Author:
```
jwietelmann
```
Text:
```

Hmmm, I'll dig into it a bit more. I'm using react-rails latest master which has 0.12.2 and digging through its code, it seemed like the problem was coming from react itself. But I could certainly be wrong.

```
Author:
```
jwietelmann
```
Text:
```

Pinned it down. The mixin was undefined in a server-side context, but React did not throw an error to indicate that fact.

```
Author:
```
aackerman
```
Text:
```

undefined or null mixins are simply ignored right now. Referenced here. You're looking for an early error or a warning?

```
Author:
```
jwietelmann
```
Text:
```

I mean, I can always do something like mixins: [assertDefined(myMixin)] but it seems like an odd choice to silently ignore an undefined mixin. At the very least, the fact that this is the default behavior should feature pretty prominently in the mixin docs if there is a good reason.

```
Author:
```
sophiebits
```
Text:
```

Thanks for tracking this down – going to close this as a dupe of #1302.

```

## 8295
Title:
```

        Is there a way to judge if an instance of a component is a child of another?
      
```
Author:
```
vifird
```
Text:
```

Hello, our team is writing a framework of React' system, and now we are facing a problem: To judge if an instance of a component is a child of another( It may in deep layer of the parent instance ). We think there should be a function to resolve these problems, but we cound not find it out.
We need your help.
Thanks a lot.

```
Author:
```
probablyup
```
Text:
```

I usually just do that type of comparison by tagging things with IDs and using the DOM .contains() API. A little inelegant, but I'm not aware of non-test tooling for the use case.

```
Author:
```
gaearon
```
Text:
```

Could you explain your use case in more detail?

```
Author:
```
vifird
```
Text:
```

@yaycmyk Yeah, we finally find a way that may probably effect, it's the _owner property , we are trying on it.

```
Author:
```
gaearon
```
Text:
```

Please don't rely on _owner, it's an implementation detail and might change behavior in future releases. Generally anything with underscores that isn't documented in public API docs isn't a public API ;-)

```
Author:
```
vifird
```
Text:
```

@gaearon Hello. We defined a component (instance of React.Component), and it's used merging with other components or HTML tag.  Such as(named Group):
<div>
  <Group key={1} name="group1">
    <div>
      <Group/>
      <div>
        <Group name="group2"/>
      </div>
    </div>
  </Group>
  <Group key={2}>
    <Department/>
  </Group>
</div>

class Department extends React.Component {
  render() {
    return (
      <div>
        <Group key={1} name="group3"/>
        <Group key={2}/>
      </div>
    )
  }
}

We want to find if the Group instance named 'group3' (or 'group2') is a chind of that named 'group1' (Obviously, 'group2' is while 'group3' isnot) .

```
Author:
```
vifird
```
Text:
```

@gaearon Yeah, thanks for your reply, but we couldn't find out another way to resolve these problems.

```
Author:
```
eliseumds
```
Text:
```

@vifird have you seen the Context feature?
class Group extends Component {
  getChildContext() {
    return { group: this.props.name };
  }

  render() {
    const parentGroup = this.context.group; // it will be undefined in the roots
    console.log('parentGroup', parentGroup);

    return (
      <div className="group">
        {this.props.children}
      </div>
    );
  }
}

Group.contextTypes = {
  group: PropTypes.string
};

Group.childContextTypes = {
  group: PropTypes.string
};

```
Author:
```
vifird
```
Text:
```

@eliseumds
Thanks for your advice. It's really a good idea for this scene.

```
Author:
```
vifird
```
Text:
```

@yaycmyk @gaearon @eliseumds
Thanks for all of you. We found a way out finally. It's used by _owner and props.children. It's a common solution for these problems. and it's not resolved by open APIs, but it doesn't matter for us.
Here we share our code (the reactContains is the main function):
/**
 * judg if parentComponent contains childComponent
 */
export function reactContains(parentComponent, childComponent) {
  if(!parentComponent || !childComponent
      || !(parentComponent instanceof React.Component)
      || !(childComponent instanceof React.Component)) {
    return false
  }
  const parentSelf = parentComponent._reactInternalInstance
  const childSelf = childComponent._reactInternalInstance

  const parentOwner = parentSelf._currentElement._owner
  let childOwner = childSelf._currentElement._owner

  while(childOwner
      && childOwner !== parentSelf
      && childOwner !== parentOwner) {
    childOwner = childOwner._currentElement._owner
  }

  if(!childOwner) {
    return false
  }

  if(childOwner === parentSelf) {
    return true
  }

  if(childOwner === parentOwner) {
    return isChild(parentSelf._currentElement, childSelf._currentElement)
  }
}
/**
 * judge if childElement is a child of parentElement
 */
export const isChild = (parentElement, childElement)=> {
  if(!parentElement || !childElement) {
    return false
  }
  if(parentElement === childElement) {
    return true
  }
  if(!parentElement.props
      || !parentElement.props.children
      || (typeof parentElement.props.children === 'string')) {
    return false
  }
  
  let children = parentElement.props.children instanceof Array ? parentElement.props.children : [ parentElement.props.children ]
  // React.Children.toArray(parentElement.props.children)
  for(let i=0; i<children.length; i++) {
    if(React.isValidElement(children[i])
        && isChild(children[i], childElement)) {
      return true
    }
  }

  return false
}

```
Author:
```
gaearon
```
Text:
```

Note that this code is extremely fragile and can (and likely will) break in any patch version of React without warning. It will also be very confusing to anyone who used React but haven't seen your project so please consider the longer term maintainability of this.

```

## 8847
Title:
```

        DOM element rendered with same props is not detected as wasted
      
```
Author:
```
mocheng
```
Text:
```

I found this issue when  #trying to demo React Perf in Chrome which basically utilizing react-addons-perf. When input DOM element is rendered with same checked={true} or checked="checked" prop, it is not detected as wasted.
Code below cannot not be detected as wasted even onClick is new function for every render.
const DumbCompnent = ({onClick, text, completed}) => {
  return (
    <div>
      <input type="checkbox" checked={completed} readOnly onClick={onClick} /><label>{text}</label>
    </div>
  );
}

Interestingly, if the code just exempt checked prop if the value is false, it can detect it as wasted properly. Code as below
const DumbCompnent = ({onClick, text, completed}) => {
  const checkedProp = completed ? {checked: true} : {};
  return (
    <div>
      <input type="checkbox" {...checkedProp} readOnly onClick={onClick} /><label>{text}</label>
    </div>
  );
}

I have created minimal TODO-like project to reproduce this issue https://github.com/mocheng/sample-wasted
Repro Steps:

Click "Start" on Perf Tab;
Check one item in web page;
Click "Stop" on Perf Tab;

Expected Result: It should detect wasted render .
Actual Result: No wasted is detected.
This can be reproduced In React v15.4.2.

```
Author:
```
gaearon
```
Text:
```

React Perf does not work in React 16. We might resurrect it at some point, but for now it's not very clear how it should work with the new algorithm. In any case, we can close this now.

```

## 15052
Title:
```

        setState has wrong type
      
```
Author:
```
laxip
```
Text:
```

We have interface:
interface State {
  condition: boolean;
  left: number;
  right: number;
}

and defined state:
  public state: State = {
    condition: true,
    left: 0,
    right: 0,
  };

Consider method:
  public change= (value: number) => {
    this.setState((state) => {
      if(state.condition) {
        return {
          left: value,
        }
      } else {
        return {
          right: value,
        }
      }
    });
  };

This cause an error during compilation.
TS:
...
        Type '{ left: number; right?: undefined; }' is not assignable to type 'Pick<State, "left" | "right">'.
          Types of property 'right' are incompatible.
            Type 'undefined' is not assignable to type 'number'.

Posible Solution:
       setState<K extends keyof S>(
            state: ((prevState: Readonly<S>, props: Readonly<P>) => (Partial<Pick<S, K>> | S | null)) | (Pick<S, K> | S | null),
            callback?: () => void
        ): void;


```
Author:
```
brookslybrand
```
Text:
```

This doesn't seem to be a problem with React and might be better suited for Stack Overflow. Regardless, the issues lies in your this.setState statement. The logic should be something more like:
if(state.condition) {
  return { ...state, left: value }
} else {
  return { ...state, right: value }
}

The reason is because when you call setState you need to return what the whole state will look like, hence the spread operator in ...state.

```
Author:
```
laxip
```
Text:
```

I dont agree with you. Look at
https://reactjs.org/docs/state-and-lifecycle.html#state-updates-are-merged

```
Author:
```
brookslybrand
```
Text:
```

Ah, you're right, it's been a while since I've used setState (been using hooks more recently). I would still say this is a better question to ask on Stack Overflow. At the least can you setup a codepen to show the issue?

```
Author:
```
laxip
```
Text:
```

https://stackblitz.com/edit/react-ts-nprphh

```
Author:
```
laxip
```
Text:
```

Im not sure, maybe I should add this issue to DefinitelyTyped/DefinitelyTyped/tree/master/types/react

```
Author:
```
brookslybrand
```
Text:
```

If you do what I originally suggested, there's no error:
https://stackblitz.com/edit/react-ts-bcuxfq?file=index.tsx
But yeah, this is not an issue with React. I would post a question on Stack Overflow, since this is really regarding typescript, not react.

```
Author:
```
aweary
```
Text:
```

The React team doesn't maintain these TypeScript definitions. Please file this issue in the DefinitelyTyped repo. Thanks!

```

## 3743
Title:
```

        Kill react-tools in it's current form
      
```
Author:
```
zpao
```
Text:
```

I shipped jstransform 0.11, which now has the CLI and API from react-tools. The intention was to deprecate react-tools entirely so we have 1 less thing to support (and it lets us ship transform updates outside the React release cycle). I'm not sure if we just won't ship react-tools 0.14 at all or if it'll basically re-ship jstransform.
If you're a hawk and watching this repo, and wondering what that means for you, here are your options:

Switch to jstranform. I wrote a migration guide for you.
Switch to babel. It supports many of the same things jstransform does and more.
Do nothing. We don't really suggest this but it's an option. We won't un-ship react-tools from npm so as long as you used versions correctly, you should be able to keep chugging along.
 remove transforms from here
 make sure our build still works
 make a react-tools that still works like the one we have
 make sure JSXTransformer still works (did not make a new one of these for jstranform).


```
Author:
```
gaearon
```
Text:
```

I'm a bit frustrated that npm install facebook/react installs react-tools instead. It would have been nice if it installed React master, as expected. Will deprecation of RT has a side effect of fixing this?

```
Author:
```
zpao
```
Text:
```

It probably won't fix it since we have a build process. The better fix for that (which we'll get back on track with) is to have us publish alphas to npm.

```
Author:
```
zpao
```
Text:
```

Ok, we'll still need to add a proper deprecation notice on npm and probably write a blog post, but otherwise we're all done here.

```
Author:
```
jimfb
```
Text:
```

Deprecation notice applied to npm, blog post posted, I think we're done here.

```
Author:
```
zpao
```
Text:
```

Heh, thanks for coming back and closing. We're long done.

```

## 3070
Title:
```

        False warnings for controlled components
      
```
Author:
```
RileyTomasek
```
Text:
```

If you have a controlled component that doesn't have an onChange listener, but is being listened to by a parent component, the following warning should not be logged, but currently is:
'Warning: You provided a value prop to a form field without an onChange handler. This will render a read-only field. If the field should be mutable use defaultValue. Otherwise, set either onChange or readOnly. Check the render method of Input.'
Here is an example: http://jsfiddle.net/cgj0haLc/

```
Author:
```
jimfb
```
Text:
```

In your case, that makes sense.  But suppose someone attaches an onChange listener to the root of their document (for hotkey navigation, or whatever).  It would be easy for a developer to create a form under that top-level component and forget to attach an onChange handler.  If they're using other components, they may not even be aware that some ancestor attached a change handler.  Also, in your example, the form is an immediate parent, but if you have formatting code in there, it might be a lot less obvious where the event is being handled.  For these reasons, the warning makes sense.  (It is a dev warning, not a fatal).
There is an easy workaround.  Just attach a no-op change handler that documents what you're doing.  Example:  onChange={function(){/* no-op, change handled by the parent component (Form) */}}
Because the warning is still useful even when the change event is being handled by the parent, and there is an easy workaround that also helps give the developer a nice place to document what they're doing, I'm going to close this as desired/expected behavior.

```
Author:
```
RileyTomasek
```
Text:
```

That makes sense. Thanks for suggesting a workaround. I just have a really big form and the warnings were drowning out any real warnings.

```

## 7399
Title:
```

        [Question] How to update context from the descendant component
      
```
Author:
```
anianj
```
Text:
```

I want to use context to pass down some data from parent to some descendant components.
But i also need to update that context from the descendant component(like when clicking on descendant component).
I find there is no document to tell how to do this. so i am wondering that if this is a anti-pattern?

```
Author:
```
gaearon
```
Text:
```

We encourage you to avoid using context in the app code. It’s advanced feature and not fully supported. What you’re trying to do seems like an anti-pattern.
I think this guide describes what you’re trying to do: https://facebook.github.io/react/docs/thinking-in-react.html. I hope this helps!
In general, we encourage you to post usage questions on StackOverflow. We use the issue tracker for tracking bugs in React, not for usage questions. Cheers!

```

## 1029
Title:
```

        Behavior differs between IE10 and Chrome when manually removing component from DOM
      
```
Author:
```
sophiebits
```
Text:
```

Recently we came across the following:
/** @jsx React.DOM */

var CountdownView = React.createClass({
    componentDidMount: function() {
        this.timeout = setInterval(this.forceUpdate.bind(this), 1000);
    },

    componentWillUnmount: function() {
        clearTimeout(this.timeout);
    },

    render: function() {
        return <div onClick={rerender}>{Date.now()}</div>;
    }
});

function rerender() {
  document.body.innerHTML = '<div id="container"></div>';

  React.renderComponent(
    <CountdownView />,
    document.getElementById('container')
  );
}

rerender();
Live demo: http://jsfiddle.net/spicyj/EGmvT/
Note that I'm manually removing the component element from the DOM here (when I should be using unmountComponentAtNode instead). In IE10, clicking the timestamp once will thereafter cause a JS error from findComponentRoot every second, but in Chrome and Firefox no errors are thrown. Why?
(In addition, it would be nice if we could give some useful message here. If you instead clear document.body completely and render into document.body, you get a somewhat-helpful warning: "ReactMount: Root element has been removed from its original container.".)

```
Author:
```
plievone
```
Text:
```

It seems that IE's node.innerHTML= (as in your example) clears all DOM nodes in the whole subtree, so that their .childElementCount is zero and also their .parentNode is null. As the "old" component instance is still attached as a child to the container element when you replace the whole tree with that innerHTML call, all of its DOM elements, including the rootNode, are now detached from each other (so they won't be anymore in the detached old container DOM node, as is usual in other browsers) and traversal to root node is impossible. This causes containsNode() to return false in isValid() used by getNode(), when processing old component DOM node in old container (now all elements detached from each other), and that is when behavior starts to differ and error happens.
In other browsers perhaps the "old" component instance runs happily in its detached container DOM element, without knowing about the problem. There might be something one could do to get a better view of the problem there too and enable that helpful warning.

```
Author:
```
plievone
```
Text:
```

Curious: is containsNode called many times, it will query the DOM?

```
Author:
```
sophiebits
```
Text:
```

Yeah, it queries the DOM each time.

```
Author:
```
sophiebits
```
Text:
```

Wontfixing this.

```
Author:
```
klouskingsley
```
Text:
```

just use unmountComponentAtNode  before document.body.innerHTML = ''.
fixed in IE

```

## 8692
Title:
```

        Expected onBeforeMountComponent() parent and onSetChildren() to be consistent
      
```
Author:
```
MicheleBertoli
```
Text:
```

Do you want to request a feature or report a bug?
It looks like a bug.
What is the current behavior?
Setting the state before rendering a component with the test renderer, shows a warning in the console:

Warning: Exception thrown by hook while handling onSetChildren: Invariant Violation: Expected onBeforeMountComponent() parent and onSetChildren() to be consistent (3 has parents 0 and 2).
Invariant Violation: Expected onBeforeMountComponent() parent and onSetChildren() to be consistent (3 has parents 0 and 2).

In the following example, it weirdly happens consistently the third time you run it, while in other more complex scenarios it does it earlier.
The steps to reproduce the issue are the following:

first of all, create an app and install the renderer

create-react-app my-app
cd my-app
yarn add react-test-renderer

then, add the following button to the App

import renderer from 'react-test-renderer'

// ...

<button
  onClick={() => {
    this.setState({})
    renderer.create(<div />).toJSON()
  }}
>💥</button>
Here is a demo:

⚠️ I understand this is not a common way of using React and the Test Renderer.
I'm more interested in knowing the reasons behind the problem and eventually see if there are some workarounds to apply.
What I'm trying to do is to serialize components and send them to an endpoint (see snapguidist).
What is the expected behavior?
Ideally, there should not be any warning.
Which versions of React, and which browser / OS are affected by this issue? Did this work in previous versions of React?
react v15.4.1
react-test-renderer v15.4.1
I have been able to reproduce the issue on the latest versions of Chrome, Firefox and Safari on MacOS.

```
Author:
```
etiennedi
```
Text:
```

I'm having the same Issue wihtout using react-test-renderer. I'm getting the same error after randomly clicking inside a Modal component (I've tested with both react-modal and react-responsive-modal). Rendering the same content inline (instead of inside a modal) does not produce any errors.
I'm using react@15.4.2 and react-dom@15.4.2 The only scenario where I don't see the error above is when downgrading to 15.3.2.

```
Author:
```
gaearon
```
Text:
```

As for OP post, I don't think we explicitly support this use case. It's a bit unexpected but we probably won't be looking into it soon. Feel free to investigate a fix (I think it might have to do with needing to call onBeforeMountComponent and onSetChildren from the test renderer, just like ReactDOM renderer does it. You can search the code for these calls.)
@etiennedi
Your case sounds more like a bug. However we can't investigate it without a minimal reproducing case.

```
Author:
```
alvov
```
Text:
```

@MicheleBertoli We're also having a similar issue (well, kind of). In our tests we render components both with react-test-renderer (create()) and react-addons-test-utils (renderIntoDocument()) which use different_debugID generators. Therefore we get the ids conflicts which are reported by ReactComponentTreeHook.js.
Funny thing is, we get a conflict even if we render the same component by these two utils as there's a difference in how _debugID is generated for text elements: react-test-renderer generates them incrementally (getNextDebugID.js) while ReactDOMComponent.js uses the parent id with an opposite sign (still not sure I got that whole thing right though).
Anyway, I have to agree that this case is pretty edgy.

```
Author:
```
gaearon
```
Text:
```

We’re probably not going to fix this in React 15.
React 16 won’t have the onBeforeMount* and similar hooks altogether so I’m closing this.

```

# Pull
## 11243
Title:
```

        Simplify Jest-specific tests
      
```
Author:
```
gaearon
```
Text:
```

It was a bit hard to say what's being tested there.
This was relevant in the past but today the only special case we have for Jest is here:



react/src/renderers/shared/fiber/ReactChildFiber.js


        Lines 1450 to 1452
      in
      49d4381






 if (instance.render._isMockFunction) { 



 // We allow auto-mocks to proceed as if they're returning null. 



 break; 





and here:



react/src/renderers/shared/server/ReactPartialRenderer.js


        Lines 412 to 415
      in
      49d4381






 if (child === undefined && inst.render._isMockFunction) { 



 // This is probably bad practice. Consider warning here and 



 // deprecating this convenience. 



   child = null; 





So I just test those specifically instead now.
The automock system is also legacy, and has been disabled by default on www this year. The other things these tests were testing are related to Jest mocking itself but it doesn’t make sense for me that we should test Jest. Especially since we don’t necessarily use the same version as www. If Jest breaks any of this behavior, they will notice it during their www sync so it shouldn’t be on our plate.
See individual commits for details.

```
Author:
```
trueadm
```
Text:
```

This looks good to me, as it removes much of the testing of Jest auto-mocking that I never really understand was in our codebase. :)

```

## 8562
Title:
```

        [Fiber][WIP] Include component stack in Fiber
      
```
Author:
```
gaearon
```
Text:
```

This gets some tests passing.
Still needs work—for example I never clean up that data right now.
I want to get feedback on initial approach.
Do Flow hacks make sense here?

```
Author:
```
sebmarkbage
```
Text:
```

So what's the plan for handling incremental and errors? Since these mounts can be terminated, restarted and resumed you can end with all kinds of inconsistent states. At the very least this will cause leaks because ReactComponentTreeHook stores everything in a map and won't get an unmount call.
Would it be better to track changes in the commit phase?

```
Author:
```
gaearon
```
Text:
```

I haven't really thought about this yet.
For stacks incrementalness shouldn't matter since we only use the immutable data (type and parent).
Leaks might be an issue yes.
For other cases, dunno, I’ll figure something out when I get closer to other cases.

```
Author:
```
sebmarkbage
```
Text:
```

At the very least I'm hesitant to land this while it is leaking.

```
Author:
```
gaearon
```
Text:
```

For sure, me too. I put up the PR mostly for discussing Flow. I’ll definitely want to solve leaks somehow.

```
Author:
```
gaearon
```
Text:
```

Closing in favor of #8570.

```

## 6763
Title:
```

        added isProfiling() to ReactDebugTool and isRunning() to PerfTools
      
```
Author:
```
nfcampos
```
Text:
```

I'm not sure the tests are added are worth it,
closes #6762

```
Author:
```
nfcampos
```
Text:
```

should I add isRunning to the docs? is it this file?
https://github.com/facebook/react/blob/master/docs/docs/10.9-perf.md

```
Author:
```
nfcampos
```
Text:
```

the build timed out for some reason, not really sure why

```
Author:
```
ghost
```
Text:
```

@nfcampos updated the pull request.

```
Author:
```
gaearon
```
Text:
```

Let’s add extra tests that verify that running begin/start or end/stop twice has no effect.

```
Author:
```
nfcampos
```
Text:
```

separate tests right? because they're testing start etc. instead of isRunning

```
Author:
```
gaearon
```
Text:
```


separate tests right? because they're testing start etc. instead of isRunning

Yeah. I’d probably just test the public API here (ReactPerf). Basically to verify that it doesn’t crash when you try to start() or stop() it twice, and that isRunning() returns a sensible value.

```
Author:
```
nfcampos
```
Text:
```

@gaearon I've added those two tests to ReactPerf

```
Author:
```
ghost
```
Text:
```

@nfcampos updated the pull request.

```
Author:
```
gaearon
```
Text:
```

Thanks!

```

## 8777
Title:
```

                Added double newline delimiters to the following functions/files:
      
```
Author:
```
richiethomas
```
Text:
```

Added double newline delimiters to the following functions/files:
        * 'beginLifeCycleTimer' function of ReactDebugTool.js
        * 'bindAutoBindMethod' function of ReactClass.js
        * 'warnNoop' function of ReactServerUpdateQueue.js
        * 'getInternalInstanceReadyForUpdate' function of ReactUpdateQueue.js
        * 'warnNoop' function of ReactNoopUpdateQueue.js
        * 'getDeclarationErrorAddendum' function of ReactDOMComponent.js
        * 'getSourceInfoErrorAddendum' function of ReactElementValidator.js
        * 'getDeclarationErrorAddendum' function of instantiateReactComponent.js and ReactElementValidator.js
        * 'traverseAllChildrenImpl' function of traverseAllChildren.js
        * 'attachRef' function of ReactRef.js
        * 'mountIndeterminateComponent' function of ReactFiberBeginWork.js
        * 'createFiberFromElementType' function of ReactFiber.js
        * 'getDeclarationErrorAddendum' function of ReactDOMSelect.js
        * 'unmountComponentAtNode' function of ReactMount.js
        * 'getDeclarationErrorAddendum' function of ReactControlledValuePropTypes.js
        * 'checkRenderMessage' function of CSSPropertyOperations.js
        * 'getDeclarationErrorAddendum' function of ReactDomFiberSelect.js
        * 'getCurrentComponentErrorInfo' function in 'ReactElementValidator'
        * 'getDeclarationErrorAddendum' function in ReactDOMFiberComponent.js

Fixes #8719

```
Author:
```
richiethomas
```
Text:
```

@gaearon what's the procedure for requesting code reviews if no one has offered one in awhile?  Should I continue to be patient or is there a way to bump this?

```
Author:
```
gaearon
```
Text:
```

Sorry I left it hanging, I’ll jump on it next week.

```
Author:
```
aweary
```
Text:
```

@gaearon I can give it a review if you're busy with other stuff right now

```
Author:
```
gaearon
```
Text:
```

That would be cool, thanks.

```
Author:
```
aweary
```
Text:
```

LGTM!

```
Author:
```
gaearon
```
Text:
```

@aweary Thanks for getting this in!
@richiethomas Thanks for the PR!

```

## 8538
Title:
```

        [Fiber] Separate priority for updates
      
```
Author:
```
acdlite
```
Text:
```

Fixes a few issues with the way updates currently work.
Right now we reset the work-in-progress's update queue during the complete phase, which means updates that occur during render or in a child's begin phase (constructor, cWM, cWRP, render) are completely dropped. This isn't an ideal pattern but Stack supports it and it's fairly common. The lack of support in Fiber today is causing a nasty infinite loop bug for some components at Facebook.
To fix this, the update queue maintains a pointer to the first pending update. When an update is used during reconciliation, the pointer is set to null to indicate that the entire queue has been processed. If new updates come in before the component is committed, the pointer points to the first new update. Then in the commit phase, the processed updates are dropped, but the pending updates are kept in the queue.
Another problem is that we use the same priority field for both props and updates, and when we reset the priority field during the complete phase, we don't have a way to read the priority of the pending updates. In the first pass, I'll add a priority field to the update queue to solve this. What we really want, though, is for each individual update to have its own priority, so that when we render a component, we only process the updates that match the current priority level.

 Don't clear pending updates from the queue.
 Move scheduling of update/callback side-effects to the begin phase.
 Add priority field to the update queue so that pending priority isn't dropped.

May do in a follow-up; not needed to fix the infinite loop bug, but necessary to get the Fiber triangle demo working:

 Sort the queue by priority and only render updates that match the current priority.


```
Author:
```
acdlite
```
Text:
```

@sebmarkbage This is ready for review now. I updated it using the algorithm we discussed yesterday.

```
Author:
```
acdlite
```
Text:
```

@sebmarkbage Updating the example now but I believe I addressed the rest of your feedback

```
Author:
```
sebmarkbage
```
Text:
```

There's a lot to go through here. Will have to continue tomorrow. It's a skill but it might be worth while working on techniques for breaking these PRs apart. Even if you have to build on top of the base refactor, it would be quicker to review the base refactor if you excluded things like the new dev warnings, and the solutions to componentDidUpdate/refs/etc. We're still behind a flag but we're getting to a point where we need to keep the code base pretty stable so that others don't get blocked. So whatever you can do to minimize the risk of a PR is helpful even if it slows you down since it might be the thing that avoids someone being blocked on a bug - which helps parallelism.

```
Author:
```
acdlite
```
Text:
```

Yup that's fair. I'll work on that in the future. Happy to pull things out to help the main bit land. Usually I've tried to avoid any extra stuff unless it's needed to get the tests to pass, or to fix a new bug that surfaced, but some of these commits can indeed be moved to separate PRs.

```
Author:
```
acdlite
```
Text:
```

Just rebased, didn't change anything

```
Author:
```
acdlite
```
Text:
```

Review feedback:

 Replace console.error with warning module.
 Remove ForceUpdate effect and put the flag back on the queue.
 Don't need to track isEmpty
 Don't drop updates from the queue in replaceState and always pass the accumulated state.
 Inline insertUpdateIntoQueue, maybe. Make the logic easier to follow when an incoming update is cloned versus when it is not.
 Don't update memoizedState in begin phase. Later, we'll move all memoization from complete to begin.
 Get rid of weird for-loops. Either explode or use a helper function so it can be inlined.
 Clone update before transferring to callbackList


```
Author:
```
sebmarkbage
```
Text:
```

I have some concerns about the code style that we should address in follow ups but I think this works.
Let's just undo the effect tag thing and then we can land.

```
Author:
```
acdlite
```
Text:
```

Okay I'll remove the effect tag thing and then do the rest of the follow-up in a separate PR.

```
Author:
```
vjeux
```
Text:
```

I'm curious, why not Number.MAX_SAFE_INTEGER ?

```
Author:
```
aweary
```
Text:
```

Maybe so that the JS engine can store it as an unsigned 8-bit integer? I'm not actually sure if any actually do that, but that's my guess

```
Author:
```
syranide
```
Text:
```

@aweary AFAIK only 31bit signed integers have special treatment. https://www.html5rocks.com/en/tutorials/speed/v8/#toc-topic-numbers

```

## 4231
Title:
```

        Click counter example
      
```
Author:
```
DarkScorpion
```
Text:
```

Atomic example counter clicks on react.

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
jimfb
```
Text:
```

Seems reasonable to me.  I think it does make sense to add an example that demonstrates a click/event handler, since it's a very reasonable thing for someone to want to know how to do.  Rather than creating elements manually, we should probably use jsx, since it's more idiomatic.  And we should squash the commits into a single commit.  cc @spicyj.
On a side note: Can you sign the CLA so we're allowed to merge?  You know, lawyers :/

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
DarkScorpion
```
Text:
```

Translate to jsx and lowercase.
If jsx standard, why hi not included in react? A lot of confusion, people read examples, not for a single framework, but for almost 2 identical frameworks

```
Author:
```
jimfb
```
Text:
```

Looks good, thanks @DarkScorpion!

```

## 15631
Title:
```

        warn if passive effects get queued outside of an act() call.
      
```
Author:
```
threepointone
```
Text:
```

This version uses a feature flag to disable the warning in tests. It isn't a viable options since we'd have to disable a whole lot of tests that run in yarn test-build See #15763 instead

based on #15591. this might be a bit controversial, but I agree with the reasoning. of note, we don't modify our own tests to satisfy this warning, instead using a feature flag to disable the warning for some tests. this is because we're testing the actual sequencing of work in these tests, and don't want to flush everything with act().
you probably want to see just this commit - 9f7a346

```
Author:
```
sizebot
```
Text:
```

React: size: 0.0%, gzip: -0.0%

Details of bundled changes.
Comparing: c7398f3...9f7a346
react



File
Filesize Diff
Gzip Diff
Prev Size
Current Size
Prev Gzip
Current Gzip
ENV




react.development.js
+0.4%
+0.6%
107.92 KB
108.33 KB
27.39 KB
27.54 KB
UMD_DEV


react.production.min.js
0.0%
-0.0%
12.33 KB
12.33 KB
4.8 KB
4.8 KB
UMD_PROD


react.profiling.min.js
0.0%
-0.0%
14.48 KB
14.48 KB
5.32 KB
5.32 KB
UMD_PROFILING


react.development.js
+0.6%
+0.9%
70.09 KB
70.5 KB
18.04 KB
18.21 KB
NODE_DEV


react.production.min.js
0.0%
-0.0%
6.48 KB
6.48 KB
2.69 KB
2.69 KB
NODE_PROD


React-dev.js
0.0%
-0.0%
68.36 KB
68.36 KB
17.38 KB
17.38 KB
FB_WWW_DEV


React-prod.js
0.0%
-0.0%
16.32 KB
16.32 KB
4.31 KB
4.31 KB
FB_WWW_PROD


React-profiling.js
0.0%
-0.0%
16.32 KB
16.32 KB
4.31 KB
4.31 KB
FB_WWW_PROFILING



react-dom



File
Filesize Diff
Gzip Diff
Prev Size
Current Size
Prev Gzip
Current Gzip
ENV




react-dom.development.js
+0.2%
+0.2%
825.72 KB
827.61 KB
188.5 KB
188.79 KB
UMD_DEV


react-dom.profiling.min.js
0.0%
-0.0%
107.15 KB
107.15 KB
34.8 KB
34.8 KB
UMD_PROFILING


react-dom.development.js
+0.2%
+0.1%
820.13 KB
821.93 KB
186.95 KB
187.22 KB
NODE_DEV


react-dom.production.min.js
0.0%
-0.0%
103.98 KB
103.98 KB
33.25 KB
33.25 KB
NODE_PROD


react-dom.profiling.min.js
0.0%
-0.0%
107.33 KB
107.33 KB
34.14 KB
34.14 KB
NODE_PROFILING


ReactDOM-dev.js
+0.2%
+0.1%
844.85 KB
846.4 KB
188.48 KB
188.61 KB
FB_WWW_DEV


ReactDOM-profiling.js
0.0%
0.0%
351.45 KB
351.45 KB
65.08 KB
65.08 KB
FB_WWW_PROFILING


react-dom-unstable-fire.development.js
+0.2%
+0.2%
826.05 KB
827.93 KB
188.65 KB
188.93 KB
UMD_DEV


react-dom-unstable-fire.production.min.js
0.0%
-0.0%
104.01 KB
104.01 KB
33.82 KB
33.82 KB
UMD_PROD


react-dom-unstable-fire.profiling.min.js
0.0%
-0.0%
107.16 KB
107.16 KB
34.81 KB
34.81 KB
UMD_PROFILING


react-dom-unstable-fire.development.js
+0.2%
+0.1%
820.45 KB
822.25 KB
187.09 KB
187.36 KB
NODE_DEV


react-dom-unstable-fire.production.min.js
0.0%
-0.0%
104 KB
104 KB
33.26 KB
33.26 KB
NODE_PROD


react-dom-unstable-fire.profiling.min.js
0.0%
-0.0%
107.34 KB
107.34 KB
34.15 KB
34.15 KB
NODE_PROFILING


ReactFire-dev.js
+0.2%
+0.1%
844.04 KB
845.59 KB
188.47 KB
188.61 KB
FB_WWW_DEV


ReactFire-prod.js
0.0%
0.0%
334.22 KB
334.22 KB
61.68 KB
61.68 KB
FB_WWW_PROD


ReactFire-profiling.js
0.0%
0.0%
339.41 KB
339.41 KB
62.63 KB
62.63 KB
FB_WWW_PROFILING


react-dom-test-utils.development.js
+4.8%
+4.6%
54.23 KB
56.82 KB
14.98 KB
15.67 KB
UMD_DEV


react-dom-test-utils.production.min.js
🔺+1.1%
🔺+0.8%
10.56 KB
10.67 KB
3.9 KB
3.93 KB
UMD_PROD


react-dom-test-utils.development.js
+2.2%
+2.9%
53.95 KB
55.16 KB
14.91 KB
15.35 KB
NODE_DEV


react-dom-test-utils.production.min.js
🔺+0.7%
🔺+0.9%
10.35 KB
10.43 KB
3.82 KB
3.85 KB
NODE_PROD


ReactTestUtils-dev.js
+1.8%
+2.0%
51.44 KB
52.34 KB
13.83 KB
14.11 KB
FB_WWW_DEV


react-dom-unstable-native-dependencies.development.js
0.0%
-0.0%
60.76 KB
60.76 KB
15.85 KB
15.85 KB
UMD_DEV


react-dom-unstable-native-dependencies.development.js
0.0%
-0.0%
60.43 KB
60.43 KB
15.72 KB
15.72 KB
NODE_DEV


react-dom-server.browser.development.js
+0.3%
+0.5%
136.73 KB
137.14 KB
35.99 KB
36.17 KB
UMD_DEV


react-dom-server.browser.production.min.js
0.0%
-0.0%
19.14 KB
19.14 KB
7.22 KB
7.22 KB
UMD_PROD


react-dom-server.browser.development.js
+0.3%
+0.5%
132.86 KB
133.27 KB
35.05 KB
35.22 KB
NODE_DEV


react-dom-server.browser.production.min.js
0.0%
-0.0%
19.07 KB
19.07 KB
7.21 KB
7.21 KB
NODE_PROD


ReactDOMServer-dev.js
0.0%
-0.0%
135.21 KB
135.21 KB
34.71 KB
34.71 KB
FB_WWW_DEV


react-dom-server.node.development.js
+0.3%
+0.5%
134.81 KB
135.22 KB
35.6 KB
35.77 KB
NODE_DEV


react-dom-server.node.production.min.js
0.0%
-0.0%
19.93 KB
19.93 KB
7.51 KB
7.51 KB
NODE_PROD


react-dom-unstable-fizz.browser.development.js
0.0%
-0.1%
3.66 KB
3.66 KB
1.45 KB
1.45 KB
UMD_DEV


react-dom-unstable-fizz.browser.development.js
0.0%
-0.1%
3.49 KB
3.49 KB
1.41 KB
1.41 KB
NODE_DEV


react-dom-unstable-fizz.browser.production.min.js
0.0%
-0.2%
1.05 KB
1.05 KB
638 B
637 B
NODE_PROD


react-dom-unstable-fizz.node.production.min.js
0.0%
-0.1%
1.1 KB
1.1 KB
668 B
667 B
NODE_PROD



react-art



File
Filesize Diff
Gzip Diff
Prev Size
Current Size
Prev Gzip
Current Gzip
ENV




react-art.development.js
+0.3%
+0.3%
564.3 KB
566.19 KB
123.66 KB
123.97 KB
UMD_DEV


react-art.production.min.js
0.0%
-0.0%
95.8 KB
95.8 KB
29.41 KB
29.41 KB
UMD_PROD


react-art.development.js
+0.4%
+0.3%
495.26 KB
497.06 KB
106.24 KB
106.52 KB
NODE_DEV


react-art.production.min.js
0.0%
-0.0%
60.77 KB
60.77 KB
18.73 KB
18.73 KB
NODE_PROD


ReactART-dev.js
+0.3%
+0.1%
504.77 KB
506.33 KB
105.38 KB
105.51 KB
FB_WWW_DEV


ReactART-prod.js
0.0%
-0.0%
196.74 KB
196.74 KB
33.43 KB
33.43 KB
FB_WWW_PROD



react-native-renderer



File
Filesize Diff
Gzip Diff
Prev Size
Current Size
Prev Gzip
Current Gzip
ENV




ReactNativeRenderer-dev.js
+0.2%
+0.1%
636.83 KB
638.39 KB
135.64 KB
135.78 KB
RN_FB_DEV


ReactNativeRenderer-prod.js
0.0%
-0.0%
245.19 KB
245.19 KB
42.55 KB
42.55 KB
RN_FB_PROD


ReactNativeRenderer-profiling.js
0.0%
-0.0%
253.14 KB
253.14 KB
44.17 KB
44.17 KB
RN_FB_PROFILING


ReactNativeRenderer-dev.js
+0.2%
+0.1%
636.75 KB
638.31 KB
135.61 KB
135.74 KB
RN_OSS_DEV


ReactNativeRenderer-prod.js
0.0%
-0.0%
245.2 KB
245.2 KB
42.55 KB
42.55 KB
RN_OSS_PROD


ReactNativeRenderer-profiling.js
0.0%
-0.0%
253.16 KB
253.16 KB
44.17 KB
44.17 KB
RN_OSS_PROFILING


ReactFabric-dev.js
+0.2%
+0.1%
625.59 KB
627.15 KB
132.88 KB
133.02 KB
RN_FB_DEV


ReactFabric-prod.js
0.0%
-0.0%
238.35 KB
238.35 KB
41.22 KB
41.22 KB
RN_FB_PROD


ReactFabric-profiling.js
0.0%
-0.0%
246.3 KB
246.3 KB
42.91 KB
42.91 KB
RN_FB_PROFILING


ReactFabric-dev.js
+0.2%
+0.1%
625.49 KB
627.05 KB
132.85 KB
132.98 KB
RN_OSS_DEV


ReactFabric-prod.js
0.0%
-0.0%
238.36 KB
238.36 KB
41.22 KB
41.22 KB
RN_OSS_PROD


ReactFabric-profiling.js
0.0%
-0.0%
246.31 KB
246.31 KB
42.91 KB
42.91 KB
RN_OSS_PROFILING



react-test-renderer



File
Filesize Diff
Gzip Diff
Prev Size
Current Size
Prev Gzip
Current Gzip
ENV




react-test-renderer.development.js
+0.4%
+0.3%
508.77 KB
510.93 KB
108.96 KB
109.32 KB
UMD_DEV


react-test-renderer.production.min.js
🔺+0.1%
🔺+0.1%
61.99 KB
62.04 KB
19.05 KB
19.07 KB
UMD_PROD


react-test-renderer.development.js
+0.4%
+0.3%
504.31 KB
506.47 KB
107.86 KB
108.22 KB
NODE_DEV


react-test-renderer.production.min.js
🔺+0.1%
🔺+0.1%
61.68 KB
61.73 KB
18.9 KB
18.93 KB
NODE_PROD


ReactTestRenderer-dev.js
+0.5%
+0.4%
515.46 KB
517.89 KB
107.64 KB
108.04 KB
FB_WWW_DEV


react-test-renderer-shallow.development.js
+1.0%
+1.7%
41.49 KB
41.9 KB
10.64 KB
10.82 KB
UMD_DEV


react-test-renderer-shallow.development.js
+1.1%
+1.9%
35.72 KB
36.13 KB
9.3 KB
9.48 KB
NODE_DEV


react-test-renderer-shallow.production.min.js
0.0%
-0.0%
11.73 KB
11.73 KB
3.66 KB
3.66 KB
NODE_PROD



react-noop-renderer



File
Filesize Diff
Gzip Diff
Prev Size
Current Size
Prev Gzip
Current Gzip
ENV




react-noop-renderer.development.js
+3.8%
+5.8%
35.15 KB
36.47 KB
8.71 KB
9.22 KB
NODE_DEV


react-noop-renderer.production.min.js
🔺+0.5%
🔺+0.3%
10.49 KB
10.54 KB
3.45 KB
3.46 KB
NODE_PROD


react-noop-renderer-persistent.development.js
+3.8%
+5.8%
35.26 KB
36.59 KB
8.73 KB
9.23 KB
NODE_DEV


react-noop-renderer-persistent.production.min.js
🔺+0.5%
🔺+0.3%
10.51 KB
10.56 KB
3.46 KB
3.47 KB
NODE_PROD


react-noop-renderer-server.development.js
0.0%
-0.1%
1.83 KB
1.83 KB
877 B
876 B
NODE_DEV


react-noop-renderer-server.production.min.js
0.0%
-0.2%
813 B
813 B
491 B
490 B
NODE_PROD



react-reconciler



File
Filesize Diff
Gzip Diff
Prev Size
Current Size
Prev Gzip
Current Gzip
ENV




react-reconciler.development.js
+0.4%
+0.2%
492.79 KB
494.59 KB
104.68 KB
104.94 KB
NODE_DEV


react-reconciler.production.min.js
0.0%
-0.0%
61.71 KB
61.71 KB
18.48 KB
18.48 KB
NODE_PROD


react-reconciler-persistent.development.js
+0.3%
+0.1%
490.7 KB
492.09 KB
103.81 KB
103.89 KB
NODE_DEV


react-reconciler-persistent.production.min.js
0.0%
-0.0%
61.72 KB
61.72 KB
18.49 KB
18.49 KB
NODE_PROD


react-reconciler-reflection.development.js
+2.2%
+3.0%
18.79 KB
19.2 KB
5.92 KB
6.1 KB
NODE_DEV



scheduler



File
Filesize Diff
Gzip Diff
Prev Size
Current Size
Prev Gzip
Current Gzip
ENV




scheduler.development.js
0.0%
-0.0%
23.32 KB
23.32 KB
5.98 KB
5.98 KB
NODE_DEV


scheduler.production.min.js
0.0%
-0.1%
5.03 KB
5.03 KB
1.92 KB
1.92 KB
NODE_PROD


scheduler-unstable_mock.development.js
n/a
n/a
0 B
17.66 KB
0 B
4.08 KB
UMD_DEV


scheduler-unstable_mock.production.min.js
n/a
n/a
0 B
4.12 KB
0 B
1.7 KB
UMD_PROD


scheduler-unstable_mock.development.js
+0.5%
+0.3%
17.39 KB
17.47 KB
4.01 KB
4.02 KB
NODE_DEV


scheduler-unstable_mock.production.min.js
🔺+0.7%
🔺+0.7%
4.06 KB
4.09 KB
1.6 KB
1.61 KB
NODE_PROD


SchedulerMock-dev.js
+0.4%
+0.3%
17.61 KB
17.69 KB
4.05 KB
4.06 KB
FB_WWW_DEV


SchedulerMock-prod.js
🔺+0.5%
🔺+0.6%
11.91 KB
11.97 KB
2.45 KB
2.46 KB
FB_WWW_PROD


scheduler-tracing.development.js
+3.8%
+7.1%
10.79 KB
11.2 KB
2.62 KB
2.81 KB
NODE_DEV


scheduler-tracing.production.min.js
0.0%
🔺+0.8%
728 B
728 B
383 B
386 B
NODE_PROD


scheduler-tracing.profiling.min.js
0.0%
-0.1%
3.26 KB
3.26 KB
1000 B
999 B
NODE_PROFILING





  Generated by 🚫 dangerJS


```
Author:
```
acdlite
```
Text:
```

^ approved once base PR is merged

```
Author:
```
threepointone
```
Text:
```

I'm rewriting this to (hopefully) not need the feature flag. it'll mean rewriting a lot  of the tests.

```
Author:
```
acdlite
```
Text:
```

@threepointone Let's land the change before updating a bunch of tests? I would prefer not to couple those.

```
Author:
```
threepointone
```
Text:
```

made an attempt at doing this without the feature flag here - #15763

```
Author:
```
threepointone
```
Text:
```

abandoning this for #15763

```

## 1747
Title:
```

        {Blog] Community Round-up #19
      
```
Author:
```
chenglou
```
Text:
```


No description provided.


```
Author:
```
vjeux
```
Text:
```

Sick!

```

## 16565
Title:
```

        createElement() decorators.
      
```
Author:
```
mshoho
```
Text:
```

Please, let's consider the following change. So far it's just a proof of concept, I'll do all other necessary steps (tests, typings, docs) if it has a chance to land.
I've seen people monkey-patching React.createElement() from their frameworks before. I need to monkey-patch it myself now in order to be able to automatically add some accessibility related attributes (which in my case are needed in the majority of DOM elements, could be added automatically, so adding them manually and teaching every dev on the project to add them is too much of a hustle). Some might suggest using custom jsxFactory in the project's config, which is a semi-option, it requires to import that custom createElement in all 100500 tsx files of the project and educate all the devs about it. And it won't help with the components which are built without JSX.
So, I'd like to be able to augment React.createElement() in a convenient way (you import a module, call a setup function — and it's working). And monkey-patching currently gives that convenience, but it's a hack and it's not future-proof (React.createElement might become read-only in some environment).
I propose to add Decorators API. The example of which is reflected in this PR's code change. The way of defining a decorator is similar to how Python decorators are being defined. Plus a few methods to add/remove them. And the React.Decorators namespace could also be extended with some methods like React.Decorators.disable() (so that people are able to have that API consumption under their control from the application code).
A code example (inside of my module's setup function):
React.Decorators.createElement.add(function(createElement) {
    // createElement is a reference to the parent createElement
    // (can be already decorated by something else).

    // Should return a function with the same signature as the original createElement().
    return function(type, config, children) {
        if (type === 'h1') {
            arguments[0] = 'h6'; // Instead of all h1's create h6's (just an example).
        }
        return createElement.apply(this, arguments);
    };
});
What do you think?

```
Author:
```
facebook-github-bot
```
Text:
```

Thank you for your pull request and welcome to our community. We require contributors to sign our Contributor License Agreement, and we don't seem to have you on file. In order for us to review and merge your code, please sign up at https://code.facebook.com/cla. If you are contributing on behalf of someone else (eg your employer), the individual CLA may not be sufficient and your employer may need the corporate CLA signed.
If you have received this in error or have any questions, please contact us at cla@fb.com. Thanks!

```
Author:
```
sizebot
```
Text:
```

React: size: 🔺+2.4%, gzip: 🔺+2.6%

Details of bundled changes.
Comparing: 2f03aa6...4e2009e
react



File
Filesize Diff
Gzip Diff
Prev Size
Current Size
Prev Gzip
Current Gzip
ENV




react.development.js
+1.1%
+0.9%
112.69 KB
113.91 KB
28.86 KB
29.13 KB
UMD_DEV


react.production.min.js
🔺+2.4%
🔺+2.6%
12.64 KB
12.94 KB
5.02 KB
5.14 KB
UMD_PROD


react.profiling.min.js
+2.0%
+2.4%
14.82 KB
15.12 KB
5.56 KB
5.69 KB
UMD_PROFILING


react.development.js
+1.7%
+1.5%
71.99 KB
73.21 KB
18.95 KB
19.23 KB
NODE_DEV


react.production.min.js
🔺+4.5%
🔺+5.0%
6.66 KB
6.96 KB
2.77 KB
2.91 KB
NODE_PROD


React-dev.js
+1.8%
+1.5%
69.86 KB
71.09 KB
17.99 KB
18.26 KB
FB_WWW_DEV


React-prod.js
🔺+7.3%
🔺+5.5%
17.25 KB
18.52 KB
4.52 KB
4.76 KB
FB_WWW_PROD


React-profiling.js
+7.3%
+5.5%
17.25 KB
18.52 KB
4.52 KB
4.76 KB
FB_WWW_PROFILING





  Generated by 🚫 dangerJS


```
Author:
```
trueadm
```
Text:
```

This isn't something we plan on adding. In the future, it is likely we will be moving from React.createElement to React.jsx too, so I'm not sure how that fits with this. Thanks for your investigation into this though :)

```
Author:
```
mshoho
```
Text:
```

@trueadm just to clarify (for the future): only things you plan on adding have a chance to be added and the acceptable contributions are limited to your plan?

```
Author:
```
trueadm
```
Text:
```

We have a RFC process for proposing changes and new features, especially ones (like this) that affect a major API in React. I hope that makes sense as I didn’t intend to cause any negative feelings.

```

