# twbs/bootstrap
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_site_content_docs_4_3_components_close_button_md](#_site_content_docs_4_3_components_close_button_md)

* [_site_content_docs_4_3_forms_checks_md](#_site_content_docs_4_3_forms_checks_md)

* [_site_content_docs_4_3_migration_md](#_site_content_docs_4_3_migration_md)

* [_github_CONTRIBUTING_md](#_github_CONTRIBUTING_md)

* [_site_content_docs_4_3_components_pagination_md](#_site_content_docs_4_3_components_pagination_md)

* [_site_content_docs_4_3_components_button_group_md](#_site_content_docs_4_3_components_button_group_md)

* [_site_content_docs_4_3_helpers_stretched_link_md](#_site_content_docs_4_3_helpers_stretched_link_md)

* [_site_content_docs_4_3_content_typography_md](#_site_content_docs_4_3_content_typography_md)

* [_site_content_docs_4_3_components_breadcrumb_md](#_site_content_docs_4_3_components_breadcrumb_md)

* [_site_content_docs_4_3_helpers_clearfix_md](#_site_content_docs_4_3_helpers_clearfix_md)

* [_site_layouts_partials_callout_info_prefersreducedmotion_md](#_site_layouts_partials_callout_info_prefersreducedmotion_md)

* [_site_content_docs_4_3_getting_started_build_tools_md](#_site_content_docs_4_3_getting_started_build_tools_md)

* [_site_content_docs_4_3_layout_overview_md](#_site_content_docs_4_3_layout_overview_md)

* [_site_content_docs_4_3_helpers_embed_md](#_site_content_docs_4_3_helpers_embed_md)

* [_SECURITY_md](#_SECURITY_md)

* [_site_content_docs_4_3_components_progress_md](#_site_content_docs_4_3_components_progress_md)

* [_site_content_docs_4_3_utilities_api_md](#_site_content_docs_4_3_utilities_api_md)

* [_site_layouts_partials_callout_warning_input_support_md](#_site_layouts_partials_callout_warning_input_support_md)

* [_site_layouts_partials_callout_danger_async_methods_md](#_site_layouts_partials_callout_danger_async_methods_md)

* [_site_content_docs_4_3_utilities_visibility_md](#_site_content_docs_4_3_utilities_visibility_md)

* [_README_md](#_README_md)

[- Inline](#Inline)

* [_site_assets_js_vendor_clipboard_min_js](#_site_assets_js_vendor_clipboard_min_js)

* [_js_dist_dom_selector_engine_js](#_js_dist_dom_selector_engine_js)

* [_js_tests_unit_dom_data_spec_js](#_js_tests_unit_dom_data_spec_js)

* [_build_postcss_config_js](#_build_postcss_config_js)

* [_site_content_docs_4_3_examples_offcanvas_offcanvas_js](#_site_content_docs_4_3_examples_offcanvas_offcanvas_js)

* [_js_src_dropdown_js](#_js_src_dropdown_js)

* [_js_src_carousel_js](#_js_src_carousel_js)

* [_js_tests_unit_util_sanitizer_spec_js](#_js_tests_unit_util_sanitizer_spec_js)

* [_build_change_version_js](#_build_change_version_js)

* [_js_src_button_js](#_js_src_button_js)

* [_js_src_toast_js](#_js_src_toast_js)

* [_js_dist_collapse_js](#_js_dist_collapse_js)

* [_babelrc_js](#_babelrc_js)

* [_js_tests_unit_toast_spec_js](#_js_tests_unit_toast_spec_js)

* [_js_dist_alert_js](#_js_dist_alert_js)

* [_js_dist_modal_js](#_js_dist_modal_js)

* [_site_content_docs_4_3_examples_checkout_form_validation_js](#_site_content_docs_4_3_examples_checkout_form_validation_js)

* [_js_src_tooltip_js](#_js_src_tooltip_js)

* [_js_src_util_index_js](#_js_src_util_index_js)

* [_js_src_scrollspy_js](#_js_src_scrollspy_js)

[- Issues](#Issues)

* [2311](#2311)

* [2358](#2358)

* [22201](#22201)

* [23190](#23190)

* [12856](#12856)

* [25131](#25131)

* [24517](#24517)

* [22583](#22583)

* [4853](#4853)

* [14929](#14929)

* [4770](#4770)

* [524](#524)

[- Pull](#Pull)

* [29562](#29562)

* [27614](#27614)

* [28989](#28989)

* [10386](#10386)

* [28094](#28094)

* [10423](#10423)

* [17625](#17625)

<!-- toc -->

# Info
## description
The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web.

# Markdown
## _site_content_docs_4_3_components_close_button_md
```---
layout: docs
title: Close button
description: A generic close button for dismissing content like modals and alerts.
group: components
---

**Be sure to include text for screen readers**, as we've done with `aria-label`.

{{< example >}}
<button type="button" class="close" aria-label="Close">
  <span aria-hidden="true">&times;</span>
</button>
{{< /example >}}
```
## _site_content_docs_4_3_forms_checks_md
```---
layout: docs
title: Checks
description: Create consistent cross-browser and cross-device checkboxes and radios with our completely rewritten checks component.
group: forms
toc: true
---

## Approach

Browser default checkboxes and radios are replaced with the help of `.form-check`, a series of classes for both input types that improves the layout and behavior of their HTML elements, that provide greater customization and cross browser consistency. Checkboxes are for selecting one or several options in a list, while radios are for selecting one option from many.

Structurally, our `<input>`s and `<label>`s are sibling elements as opposed to an `<input>` within a `<label>`. This is slightly more verbose as you must specify `id` and `for` attributes to relate the `<input>` and `<label>`. We use the sibling selector (`~`) for all our `<input>` states, like `[checked]` or `[disabled]`. When combined with the `.form-check-label` class, we can easily style the text for each item based on the `<input>`'s state.

Our checks use custom Bootstrap icons to indicate checked or indeterminate states.

## Checks

{{< example >}}
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
  <label class="form-check-label" for="flexCheckDefault">
    Default checkbox
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked>
  <label class="form-check-label" for="flexCheckChecked">
    Checked checkbox
  </label>
</div>
{{< /example >}}

### Indeterminate

Checkboxes can utilize the `:indeterminate` pseudo class when manually set via JavaScript (there is no available HTML attribute for specifying it).

{{< example >}}
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate">
  <label class="form-check-label" for="flexCheckIndeterminate">
    Indeterminate checkbox
  </label>
</div>
{{< /example >}}

### Disabled

Add the `disabled` attribute and the associated `<label>`s are automatically styled to match with a lighter color to help indicate the input's state.

{{< example >}}
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckDisabled" disabled>
  <label class="form-check-label" for="flexCheckDisabled">
    Disabled checkbox
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckCheckedDisabled" checked disabled>
  <label class="form-check-label" for="flexCheckCheckedDisabled">
    Disabled checked checkbox
  </label>
</div>
{{< /example >}}

## Radios

{{< example >}}
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
  <label class="form-check-label" for="flexRadioDefault1">
    Default radio
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
  <label class="form-check-label" for="flexRadioDefault2">
    Default checked radio
  </label>
</div>
{{< /example >}}

### Disabled

Add the `disabled` attribute and the associated `<label>`s are automatically styled to match with a lighter color to help indicate the input's state.

{{< example >}}
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDisabled" id="flexRadioDisabled" disabled>
  <label class="form-check-label" for="flexRadioDisabled">
    Disabled radio
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDisabled" id="flexRadioCheckedDisabled" checked disabled>
  <label class="form-check-label" for="flexRadioCheckedDisabled">
    Disabled checked radio
  </label>
</div>
{{< /example >}}

## Switches

A switch has the markup of a custom checkbox but uses the `.form-switch` class to render a toggle switch. Switches also support the `disabled` attribute.

{{< example >}}
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
  <label class="form-check-label" for="flexSwitchCheckDefault">Default switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" checked>
  <label class="form-check-label" for="flexSwitchCheckChecked">Checked switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" id="flexSwitchCheckDisabled" disabled>
  <label class="form-check-label" for="flexSwitchCheckDisabled">Disabled switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" id="flexSwitchCheckCheckedDisabled" checked disabled>
  <label class="form-check-label" for="flexSwitchCheckCheckedDisabled">Disabled checked switch checkbox input</label>
</div>
{{< /example >}}

## Default (stacked)

By default, any number of checkboxes and radios that are immediate sibling will be vertically stacked and appropriately spaced with `.form-check`.

{{< example >}}
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
  <label class="form-check-label" for="defaultCheck1">
    Default checkbox
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="defaultCheck2" disabled>
  <label class="form-check-label" for="defaultCheck2">
    Disabled checkbox
  </label>
</div>
{{< /example >}}

{{< example >}}
<div class="form-check">
  <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios1" value="option1" checked>
  <label class="form-check-label" for="exampleRadios1">
    Default radio
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios2" value="option2">
  <label class="form-check-label" for="exampleRadios2">
    Second default radio
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios3" value="option3" disabled>
  <label class="form-check-label" for="exampleRadios3">
    Disabled radio
  </label>
</div>
{{< /example >}}

## Inline

Group checkboxes or radios on the same horizontal row by adding `.form-check-inline` to any `.form-check`.

{{< example >}}
<div class="form-check form-check-inline">
  <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1">
  <label class="form-check-label" for="inlineCheckbox1">1</label>
</div>
<div class="form-check form-check-inline">
  <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
  <label class="form-check-label" for="inlineCheckbox2">2</label>
</div>
<div class="form-check form-check-inline">
  <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3" disabled>
  <label class="form-check-label" for="inlineCheckbox3">3 (disabled)</label>
</div>
{{< /example >}}

{{< example >}}
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1">
  <label class="form-check-label" for="inlineRadio1">1</label>
</div>
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2">
  <label class="form-check-label" for="inlineRadio2">2</label>
</div>
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio3" value="option3" disabled>
  <label class="form-check-label" for="inlineRadio3">3 (disabled)</label>
</div>
{{< /example >}}

## Without labels

Omit the wrapping `.form-check` for checkboxes and radios that have no label text. Remember to still provide some form of label for assistive technologies (for instance, using `aria-label`).

{{< example >}}
<div>
  <input class="form-check-input" type="checkbox" id="checkboxNoLabel" value="" aria-label="...">
</div>

<div>
  <input class="form-check-input" type="radio" name="radioNoLabel" id="radioNoLabel1" value="" aria-label="...">
</div>
{{< /example >}}
```
## _site_content_docs_4_3_migration_md
```---
layout: docs
title: Migrating to v5
description: Track and review changes to the Bootstrap source files, documentation, and components to help you migrate from v4 to v5.
group: migration
aliases: "/migration/"
toc: true
---

## Browser support

See the browser and devices page for details on what is currently supported in Bootstrap 5. Since v4, here's what's changed to our browser support:

- Dropped support for Internet Explorer NN
- Dropped support for Firefox NN - MM
- Dropped support for Safari NN
- Dropped support for iOS Safari NN
- Dropped support for Chrome NN
- Dropped support for Android NN

## Sass

Changes to our source Sass files and compiled CSS.

- Removed `hover`, `hover-focus`, `plain-hover-focus`, and `hover-focus-active` mixins. Use regular CSS syntax for these moving forward. [See #28267](https://github.com/twbs/bootstrap/pull/28267).
- Remove previously deprecated mixins
  - `float()`
  - `form-control-mixin()`
  - `nav-divider()`
  - `retina-img()`
  - `text-hide()` (also dropped the associated utility class, `.text-hide`)
  - `visibility()`
- **Todo:** New variables?
- **Todo:** Rearrange forms source files (under `scss/forms/`)
- **Todo:** Rearrange grid source files (under `scss/grid/`)
- Removed print styles and `$enable-print-styles` variable. Print display classes, however, have remained intact. [See #28339](https://github.com/twbs/bootstrap/pull/28339).
- Dropped `color()`, `theme-color()` & `gray()` functions in favor of variables. [See #29083](https://github.com/twbs/bootstrap/pull/29083)
- The `theme-color-level()` function is renamed to `color-level()` and now accepts any color you want instead of only `$theme-color` colors. [See #29083](https://github.com/twbs/bootstrap/pull/29083)
- Line heights are dropped from several components to simplify our codebase. The `button-size()` and `pagination-size()` do not accept line height parameters anymore. [See #29271](https://github.com/twbs/bootstrap/pull/29271)
- The `button-variant()` mixin now accepts 3 optional color parameters, for each button state, to override the color provided by `color-yiq()`. By default, these parameters will find which color provides more contrast against the button state's background color with `color-yiq()`.
- The `button-outline-variant()` mixin now accepts an additional argument, `$active-color`, for setting the button's active state text color. By default, this parameter will find which color provides more contrast against the button's active background color with `color-yiq()`.

## JavaScript

Changes to our source and compiled JavaScript files.

- Dropped jQuery dependency and rewrote plugins to be in regular JavaScript.
- Removed underscore from public static methods like `_getInstance()` → `getInstance()`.

## Grid and layout

Changes to any layout tools and our grid system.

- Dropped `.media` component as it can be built with utility classes. [See #28265](https://github.com/twbs/bootstrap/pull/28265).
- **Todo:** Remove `position: relative` from grid columns
- **Todo:** Integrate CSS grid into our grid system

## Content, Reboot, etc

Changes to Reboot, typography, tables, and more.

- **Todo:** Make RFS enabled by default
- Reset default horizontal `padding-left` on `<ul>` and `<ol>` elements from browser default `40px` to `2rem`.
- Simplified table styles (no more 2px border on `thead > th` elements) and tightened cell padding.
- Dropped `.pre-scrollable` class. [See #29135](https://github.com/twbs/bootstrap/pull/29135)
- `.text-*` utilities do not add hover and focus states to links anymore. `.link-*` helper classes can be used instead. [See #29267](https://github.com/twbs/bootstrap/pull/29267)

## Forms

- Rearranged form documentation under its own top-level section.
  - Split out old Forms page into several subpages
  - Moved input groups docs under new Forms section
- Rearranged source Sass files under `scss/forms/`, including moving over input group styles.
- Combined native and custom checkboxes and radios into single `.form-check` class.
  - New checks support sizing via `em`/`font-size` or explicit modifier classes now.
  - New checks now appear larger by default for improved usability.
  - Dropped `.custom-control` and associated classes.
  - Renamed most `$custom-control` variables to `$form-control` ones.
- Combined native and custom selects into `.form-select`.
  - Dropped `.custom-select` and associated classes.
  - Renamed most `$custom-select` variables to `$form-select` ones.
- Updated file input component with same overall design, but improved HTML.
  - Refactored `.form-file` markup to resolve some visual bugs while allowing translation and button text changes via HTML instead of CSS.
  - Dropped native `.form-control-file` and `.form-control-range` components entirely.
  - Renamed `.custom-file` to `.form-file` (including variables).
  - Added support for `:focus` and `:disabled` styles.
- Renamed `.custom-range` to `.form-range` (including variables).
- Dropped `.form-group` for margin utilities (we've replaced our docs examples with `.mb-3`).
- Dropped support for `.form-control-plaintext` inside `.input-group`s.

## Components

### Alerts

- **Todo:** Remove auto-darkening of `<hr>` elements in `.alert-*` class variants. `<hr>`s use `rgba()` for their color, so these should naturally blend anyway.

### Badges

Badges were overhauled to better differentiate themselves from buttons and to better utilize utility classes.

- **Todo:** Removed and replaced `.badge` modifier classes with background utility classes (e.g., use `.bg-primary` instead of `.badge-primary`)
- **Todo:** Removed `.badge-pill` for the `.rounded-pill` utility class
- **Todo:** Removed badge's hover and focus styles for `a.badge` and `button.badge`.

### Cards

- Removed the card columns in favor of a Masonry grid [See #28922](https://github.com/twbs/bootstrap/pull/28922).

### Jumbotron

- The jumbotron component is removed in favor of utility classes like `.bg-light` for the background color and `.p-*` classes to control padding.

### Pagination

- Pagination links now have customizable `margin-left` that are dynamically rounded on all corners when separated from one another.

### Popovers

- Renamed `.arrow` to `.popover-arrow`

### Tooltips

- Renamed `.arrow` to `.tooltip-arrow`

## Accessibility

- `.sr-only-focusable` does not require `.sr-only` anymore. [See #28720](https://github.com/twbs/bootstrap/pull/28720).

## Utilities

- Renamed `.text-monospace` to `.font-monospace`
- Decreased the number of responsive order utilities per breakpoint. The highest order utility with a number now is `.order-5` instead of `.order-12`. [See #28874](https://github.com/twbs/bootstrap/pull/28874).
- New `line-height` utilities: `.lh-1`, `.lh-sm`, `.lh-base` and `.lh-lg`. See [here]({{< docsref "/utilities/text#line-height" >}}).
- Added `.bg-body` for quickly setting the `<body>`'s background to additional elements.
- **Todo:** Drop `.text-hide` as it's an antiquated method for hiding text that shouldn't be used anymore
- **Todo:** Split utilities into property-value utility classes and helpers

## Docs

-  Removed "Wall of browser bugs" page because it has become obsolete

## Build tools
```
## _github_CONTRIBUTING_md
```# Contributing to Bootstrap

Looking to contribute something to Bootstrap? **Here's how you can help.**

Please take a moment to review this document in order to make the contribution
process easy and effective for everyone involved.

Following these guidelines helps to communicate that you respect the time of
the developers managing and developing this open source project. In return,
they should reciprocate that respect in addressing your issue or assessing
patches and features.


## Using the issue tracker

The [issue tracker](https://github.com/twbs/bootstrap/issues) is
the preferred channel for [bug reports](#bug-reports), [features requests](#feature-requests)
and [submitting pull requests](#pull-requests), but please respect the following
restrictions:

* Please **do not** use the issue tracker for personal support requests.  Stack
  Overflow ([`bootstrap-4`](https://stackoverflow.com/questions/tagged/bootstrap-4) tag),
  [Slack](https://bootstrap-slack.herokuapp.com/) or [IRC](README.md#community) are better places to get help.

* Please **do not** derail or troll issues. Keep the discussion on topic and
  respect the opinions of others.

* Please **do not** post comments consisting solely of "+1" or ":thumbsup:".
  Use [GitHub's "reactions" feature](https://blog.github.com/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/)
  instead. We reserve the right to delete comments which violate this rule.

* Please **do not** open issues regarding the official themes offered on <https://themes.getbootstrap.com/>.
  Instead, please email any questions or feedback regarding those themes to `themes AT getbootstrap DOT com`.


## Issues and labels

Our bug tracker utilizes several labels to help organize and identify issues. Here's what they represent and how we use them:

- `browser bug` - Issues that are reported to us, but actually are the result of a browser-specific bug. These are diagnosed with reduced test cases and result in an issue opened on that browser's own bug tracker.
- `confirmed` - Issues that have been confirmed with a reduced test case and identify a bug in Bootstrap.
- `css` - Issues stemming from our compiled CSS or source Sass files.
- `docs` - Issues for improving or updating our documentation.
- `examples` - Issues involving the example templates included in our docs.
- `feature` - Issues asking for a new feature to be added, or an existing one to be extended or modified. New features require a minor version bump (e.g., `v3.0.0` to `v3.1.0`).
- `build` - Issues with our build system, which is used to run all our tests, concatenate and compile source files, and more.
- `help wanted` - Issues we need or would love help from the community to resolve.
- `js` - Issues stemming from our compiled or source JavaScript files.
- `meta` - Issues with the project itself or our GitHub repository.

For a complete look at our labels, see the [project labels page](https://github.com/twbs/bootstrap/labels).


## Bug reports

A bug is a _demonstrable problem_ that is caused by the code in the repository.
Good bug reports are extremely helpful, so thanks!

Guidelines for bug reports:

0. **[validate your HTML](https://html5.validator.nu/)** to ensure your
   problem isn't caused by a simple error in your own code.

1. **Use the GitHub issue search** &mdash; check if the issue has already been
   reported.

2. **Check if the issue has been fixed** &mdash; try to reproduce it using the
   latest `master` or development branch in the repository.

3. **Isolate the problem** &mdash; ideally create a [reduced test
   case](https://css-tricks.com/reduced-test-cases/) and a live example.
   [This JS Bin](https://jsbin.com/lolome/edit?html,output) is a helpful template.


A good bug report shouldn't leave others needing to chase you up for more
information. Please try to be as detailed as possible in your report. What is
your environment? What steps will reproduce the issue? What browser(s) and OS
experience the problem? Do other browsers show the bug differently? What
would you expect to be the outcome? All these details will help people to fix
any potential bugs.

Example:

> Short and descriptive example bug report title
>
> A summary of the issue and the browser/OS environment in which it occurs. If
> suitable, include the steps required to reproduce the bug.
>
> 1. This is the first step
> 2. This is the second step
> 3. Further steps, etc.
>
> `<url>` - a link to the reduced test case
>
> Any other information you want to share that is relevant to the issue being
> reported. This might include the lines of code that you have identified as
> causing the bug, and potential solutions (and your opinions on their
> merits).

### Reporting upstream browser bugs

Sometimes bugs reported to us are actually caused by bugs in the browser(s) themselves, not bugs in Bootstrap per se.

| Vendor(s)     | Browser(s)                   | Rendering engine | Bug reporting website(s)                                                              | Notes                                                    |
| ------------- | ---------------------------- | ---------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Mozilla       | Firefox                      | Gecko            | https://bugzilla.mozilla.org/enter_bug.cgi                                            | "Core" is normally the right product option to choose.   |
| Apple         | Safari                       | WebKit           | https://bugs.webkit.org/enter_bug.cgi?product=WebKit <br> https://bugreport.apple.com/ | In Apple's bug reporter, choose "Safari" as the product. |
| Google, Opera | Chrome, Chromium, Opera v15+ | Blink            | https://bugs.chromium.org/p/chromium/issues/list                                      | Click the "New issue" button.                            |
| Microsoft     | Edge                         | EdgeHTML         | https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/                 |                                                          |


## Feature requests

Feature requests are welcome. But take a moment to find out whether your idea
fits with the scope and aims of the project. It's up to *you* to make a strong
case to convince the project's developers of the merits of this feature. Please
provide as much detail and context as possible.


## Pull requests

Good pull requests—patches, improvements, new features—are a fantastic
help. They should remain focused in scope and avoid containing unrelated
commits.

**Please ask first** before embarking on any significant pull request (e.g.
implementing features, refactoring code, porting to a different language),
otherwise you risk spending a lot of time working on something that the
project's developers might not want to merge into the project.

Please adhere to the [coding guidelines](#code-guidelines) used throughout the
project (indentation, accurate comments, etc.) and any other requirements
(such as test coverage).

**Do not edit `bootstrap.css`, or `bootstrap.js`
directly!** Those files are automatically generated. You should edit the
source files in [`/bootstrap/scss/`](https://github.com/twbs/bootstrap/tree/master/scss)
and/or [`/bootstrap/js/src/`](https://github.com/twbs/bootstrap/tree/master/js/src) instead.

Similarly, when contributing to Bootstrap's documentation, you should edit the
documentation source files in
[the `/bootstrap/site/content/docs/` directory of the `master` branch](https://github.com/twbs/bootstrap/tree/master/site/content/docs).
**Do not edit the `gh-pages` branch.** That branch is generated from the
documentation source files and is managed separately by the Bootstrap Core Team.

Adhering to the following process is the best way to get your work
included in the project:

1. [Fork](https://help.github.com/articles/fork-a-repo/) the project, clone your fork,
   and configure the remotes:

   '''bash
   # Clone your fork of the repo into the current directory
   git clone https://github.com/<your-username>/bootstrap.git
   # Navigate to the newly cloned directory
   cd bootstrap
   # Assign the original repo to a remote called "upstream"
   git remote add upstream https://github.com/twbs/bootstrap.git
   '''

2. If you cloned a while ago, get the latest changes from upstream:

   '''bash
   git checkout master
   git pull upstream master
   '''

3. Create a new topic branch (off the main project development branch) to
   contain your feature, change, or fix:

   '''bash
   git checkout -b <topic-branch-name>
   '''

4. Commit your changes in logical chunks. Please adhere to these [git commit
   message guidelines](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
   or your code is unlikely be merged into the main project. Use Git's
   [interactive rebase](https://help.github.com/articles/about-git-rebase/)
   feature to tidy up your commits before making them public.

5. Locally merge (or rebase) the upstream development branch into your topic branch:

   '''bash
   git pull [--rebase] upstream master
   '''

6. Push your topic branch up to your fork:

   '''bash
   git push origin <topic-branch-name>
   '''

7. [Open a Pull Request](https://help.github.com/articles/about-pull-requests/)
    with a clear title and description against the `master` branch.

**IMPORTANT**: By submitting a patch, you agree to allow the project owners to
license your work under the terms of the [MIT License](../LICENSE) (if it
includes code changes) and under the terms of the
[Creative Commons Attribution 3.0 Unported License](https://creativecommons.org/licenses/by/3.0/)
(if it includes documentation changes).


## Code guidelines

### HTML

[Adhere to the Code Guide.](https://codeguide.co/#html)

- Use tags and elements appropriate for an HTML5 doctype (e.g., self-closing tags).
- Use CDNs and HTTPS for third-party JS when possible. We don't use protocol-relative URLs in this case because they break when viewing the page locally via `file://`.
- Use [WAI-ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) attributes in documentation examples to promote accessibility.

### CSS

[Adhere to the Code Guide.](https://codeguide.co/#css)

- When feasible, default color palettes should comply with [WCAG color contrast guidelines](https://www.w3.org/TR/WCAG20/#visual-audio-contrast).
- Except in rare cases, don't remove default `:focus` styles (via e.g. `outline: none;`) without providing alternative styles. See [this A11Y Project post](https://a11yproject.com/posts/never-remove-css-outlines/) for more details.

### JS

- No semicolons (in client-side JS)
- 2 spaces (no tabs)
- strict mode
- "Attractive"

### Checking coding style

Run `npm run test` before committing to ensure your changes follow our coding standards.


## License

By contributing your code, you agree to license your contribution under the [MIT License](../LICENSE).
By contributing to the documentation, you agree to license your contribution under the [Creative Commons Attribution 3.0 Unported License](https://creativecommons.org/licenses/by/3.0/).

Prior to v3.1.0, Bootstrap's code was released under the Apache License v2.0.
```
## _site_content_docs_4_3_components_pagination_md
```---
layout: docs
title: Pagination
description: Documentation and examples for showing pagination to indicate a series of related content exists across multiple pages.
group: components
toc: true
---

## Overview

We use a large block of connected links for our pagination, making links hard to miss and easily scalable—all while providing large hit areas. Pagination is built with list HTML elements so screen readers can announce the number of available links. Use a wrapping `<nav>` element to identify it as a navigation section to screen readers and other assistive technologies.

In addition, as pages likely have more than one such navigation section, it's advisable to provide a descriptive `aria-label` for the `<nav>` to reflect its purpose. For example, if the pagination component is used to navigate between a set of search results, an appropriate label could be `aria-label="Search results pages"`.

{{< example >}}
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
{{< /example >}}

## Working with icons

Looking to use an icon or symbol in place of text for some pagination links? Be sure to provide proper screen reader support with `aria` attributes.

{{< example >}}
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item">
      <a class="page-link" href="#" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>
{{< /example >}}

## Disabled and active states

Pagination links are customizable for different circumstances. Use `.disabled` for links that appear un-clickable and `.active` to indicate the current page.

While the `.disabled` class uses `pointer-events: none` to _try_ to disable the link functionality of `<a>`s, that CSS property is not yet standardized and doesn't account for keyboard navigation. As such, you should always add `tabindex="-1"` on disabled links and use custom JavaScript to fully disable their functionality.

{{< example >}}
<nav aria-label="...">
  <ul class="pagination">
    <li class="page-item disabled">
      <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item active" aria-current="page">
      <a class="page-link" href="#">2 <span class="sr-only">(current)</span></a>
    </li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
{{< /example >}}

You can optionally swap out active or disabled anchors for `<span>`, or omit the anchor in the case of the prev/next arrows, to remove click functionality and prevent keyboard focus while retaining intended styles.

{{< example >}}
<nav aria-label="...">
  <ul class="pagination">
    <li class="page-item disabled">
      <span class="page-link">Previous</span>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item active" aria-current="page">
      <span class="page-link">
        2
        <span class="sr-only">(current)</span>
      </span>
    </li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
{{< /example >}}

## Sizing

Fancy larger or smaller pagination? Add `.pagination-lg` or `.pagination-sm` for additional sizes.

{{< example >}}
<nav aria-label="...">
  <ul class="pagination pagination-lg">
    <li class="page-item active" aria-current="page">
      <span class="page-link">
        1
        <span class="sr-only">(current)</span>
      </span>
    </li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
  </ul>
</nav>
{{< /example >}}

{{< example >}}
<nav aria-label="...">
  <ul class="pagination pagination-sm">
    <li class="page-item active" aria-current="page">
      <span class="page-link">
        1
        <span class="sr-only">(current)</span>
      </span>
    </li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
  </ul>
</nav>
{{< /example >}}

## Alignment

Change the alignment of pagination components with [flexbox utilities]({{< docsref "/utilities/flex" >}}).

{{< example >}}
<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">
    <li class="page-item disabled">
      <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
{{< /example >}}

{{< example >}}
<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-end">
    <li class="page-item disabled">
      <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
{{< /example >}}
```
## _site_content_docs_4_3_components_button_group_md
```---
layout: docs
title: Button group
description: Group a series of buttons together on a single line with the button group, and super-power them with JavaScript.
group: components
toc: true
---

## Basic example

Wrap a series of buttons with `.btn` in `.btn-group`. Add on optional JavaScript radio and checkbox style behavior with [our buttons plugin]({{< docsref "/components/buttons#button-plugin" >}}).

{{< example >}}
<div class="btn-group" role="group" aria-label="Basic example">
  <button type="button" class="btn btn-secondary">Left</button>
  <button type="button" class="btn btn-secondary">Middle</button>
  <button type="button" class="btn btn-secondary">Right</button>
</div>
{{< /example >}}

{{< callout warning >}}
##### Ensure correct `role` and provide a label

In order for assistive technologies (such as screen readers) to convey that a series of buttons is grouped, an appropriate `role` attribute needs to be provided. For button groups, this would be `role="group"`, while toolbars should have a `role="toolbar"`.

In addition, groups and toolbars should be given an explicit label, as most assistive technologies will otherwise not announce them, despite the presence of the correct role attribute. In the examples provided here, we use `aria-label`, but alternatives such as `aria-labelledby` can also be used.
{{< /callout >}}

## Button toolbar

Combine sets of button groups into button toolbars for more complex components. Use utility classes as needed to space out groups, buttons, and more.

{{< example >}}
<div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
  <div class="btn-group mr-2" role="group" aria-label="First group">
    <button type="button" class="btn btn-secondary">1</button>
    <button type="button" class="btn btn-secondary">2</button>
    <button type="button" class="btn btn-secondary">3</button>
    <button type="button" class="btn btn-secondary">4</button>
  </div>
  <div class="btn-group mr-2" role="group" aria-label="Second group">
    <button type="button" class="btn btn-secondary">5</button>
    <button type="button" class="btn btn-secondary">6</button>
    <button type="button" class="btn btn-secondary">7</button>
  </div>
  <div class="btn-group" role="group" aria-label="Third group">
    <button type="button" class="btn btn-secondary">8</button>
  </div>
</div>
{{< /example >}}

Feel free to mix input groups with button groups in your toolbars. Similar to the example above, you'll likely need some utilities though to space things properly.

{{< example >}}
<div class="btn-toolbar mb-3" role="toolbar" aria-label="Toolbar with button groups">
  <div class="btn-group mr-2" role="group" aria-label="First group">
    <button type="button" class="btn btn-secondary">1</button>
    <button type="button" class="btn btn-secondary">2</button>
    <button type="button" class="btn btn-secondary">3</button>
    <button type="button" class="btn btn-secondary">4</button>
  </div>
  <div class="input-group">
    <div class="input-group-prepend">
      <div class="input-group-text" id="btnGroupAddon">@</div>
    </div>
    <input type="text" class="form-control" placeholder="Input group example" aria-label="Input group example" aria-describedby="btnGroupAddon">
  </div>
</div>

<div class="btn-toolbar justify-content-between" role="toolbar" aria-label="Toolbar with button groups">
  <div class="btn-group" role="group" aria-label="First group">
    <button type="button" class="btn btn-secondary">1</button>
    <button type="button" class="btn btn-secondary">2</button>
    <button type="button" class="btn btn-secondary">3</button>
    <button type="button" class="btn btn-secondary">4</button>
  </div>
  <div class="input-group">
    <div class="input-group-prepend">
      <div class="input-group-text" id="btnGroupAddon2">@</div>
    </div>
    <input type="text" class="form-control" placeholder="Input group example" aria-label="Input group example" aria-describedby="btnGroupAddon2">
  </div>
</div>
{{< /example >}}

## Sizing

Instead of applying button sizing classes to every button in a group, just add `.btn-group-*` to each `.btn-group`, including each one when nesting multiple groups.

<div class="bd-example">
  <div class="btn-group btn-group-lg" role="group" aria-label="Large button group">
    <button type="button" class="btn btn-secondary">Left</button>
    <button type="button" class="btn btn-secondary">Middle</button>
    <button type="button" class="btn btn-secondary">Right</button>
  </div>
  <br>
  <div class="btn-group" role="group" aria-label="Default button group">
    <button type="button" class="btn btn-secondary">Left</button>
    <button type="button" class="btn btn-secondary">Middle</button>
    <button type="button" class="btn btn-secondary">Right</button>
  </div>
  <br>
  <div class="btn-group btn-group-sm" role="group" aria-label="Small button group">
    <button type="button" class="btn btn-secondary">Left</button>
    <button type="button" class="btn btn-secondary">Middle</button>
    <button type="button" class="btn btn-secondary">Right</button>
  </div>
</div>

{{< highlight html >}}
<div class="btn-group btn-group-lg" role="group" aria-label="...">...</div>
<div class="btn-group" role="group" aria-label="...">...</div>
<div class="btn-group btn-group-sm" role="group" aria-label="...">...</div>
{{< /highlight >}}

## Nesting

Place a `.btn-group` within another `.btn-group` when you want dropdown menus mixed with a series of buttons.

{{< example >}}
<div class="btn-group" role="group" aria-label="Button group with nested dropdown">
  <button type="button" class="btn btn-secondary">1</button>
  <button type="button" class="btn btn-secondary">2</button>

  <div class="btn-group" role="group">
    <button id="btnGroupDrop1" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
      Dropdown
    </button>
    <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
      <a class="dropdown-item" href="#">Dropdown link</a>
      <a class="dropdown-item" href="#">Dropdown link</a>
    </div>
  </div>
</div>
{{< /example >}}

## Vertical variation

Make a set of buttons appear vertically stacked rather than horizontally. **Split button dropdowns are not supported here.**

<div class="bd-example">
  <div class="btn-group-vertical" role="group" aria-label="Vertical button group">
    <button type="button" class="btn btn-secondary">Button</button>
    <button type="button" class="btn btn-secondary">Button</button>
    <button type="button" class="btn btn-secondary">Button</button>
    <button type="button" class="btn btn-secondary">Button</button>
    <button type="button" class="btn btn-secondary">Button</button>
    <button type="button" class="btn btn-secondary">Button</button>
  </div>
</div>


<div class="bd-example">
  <div class="btn-group-vertical" role="group" aria-label="Vertical button group">
    <button type="button" class="btn btn-secondary">Button</button>
    <button type="button" class="btn btn-secondary">Button</button>
    <div class="btn-group" role="group">
      <button id="btnGroupVerticalDrop1" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
        Dropdown
      </button>
      <div class="dropdown-menu" aria-labelledby="btnGroupVerticalDrop1">
        <a class="dropdown-item" href="#">Dropdown link</a>
        <a class="dropdown-item" href="#">Dropdown link</a>
      </div>
    </div>
    <button type="button" class="btn btn-secondary">Button</button>
    <button type="button" class="btn btn-secondary">Button</button>
    <div class="btn-group" role="group">
      <button id="btnGroupVerticalDrop2" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
        Dropdown
      </button>
      <div class="dropdown-menu" aria-labelledby="btnGroupVerticalDrop2">
        <a class="dropdown-item" href="#">Dropdown link</a>
        <a class="dropdown-item" href="#">Dropdown link</a>
      </div>
    </div>
    <div class="btn-group" role="group">
      <button id="btnGroupVerticalDrop3" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
        Dropdown
      </button>
      <div class="dropdown-menu" aria-labelledby="btnGroupVerticalDrop3">
        <a class="dropdown-item" href="#">Dropdown link</a>
        <a class="dropdown-item" href="#">Dropdown link</a>
      </div>
    </div>
    <div class="btn-group" role="group">
      <button id="btnGroupVerticalDrop4" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
        Dropdown
      </button>
      <div class="dropdown-menu" aria-labelledby="btnGroupVerticalDrop4">
        <a class="dropdown-item" href="#">Dropdown link</a>
        <a class="dropdown-item" href="#">Dropdown link</a>
      </div>
    </div>
  </div>
</div>

{{< highlight html >}}
<div class="btn-group-vertical">
  ...
</div>
{{< /highlight >}}
```
## _site_content_docs_4_3_helpers_stretched_link_md
```---
layout: docs
title: Stretched link
description: Make any HTML element or Bootstrap component clickable by "stretching" a nested link via CSS.
group: helpers
---

Add `.stretched-link` to a link to make its [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block) clickable via a `::after` pseudo element. In most cases, this means that an element with `position: relative;` that contains a link with the `.stretched-link` class is clickable.

Cards have `position: relative` by default in Bootstrap, so in this case you can safely add the `.stretched-link` class to a link in the card without any other HTML changes.

Multiple links and tap targets are not recommended with stretched links. However, some `position` and `z-index` styles can help should this be required.

{{< example >}}
<div class="card" style="width: 18rem;">
  {{< placeholder width="100%" height="180" class="card-img-top" text="false" title="Card image cap" >}}
  <div class="card-body">
    <h5 class="card-title">Card with stretched link</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary stretched-link">Go somewhere</a>
  </div>
</div>
{{< /example >}}

Most custom components do not have `position: relative` by default, so we need to add the `.position-relative` here to prevent the link from stretching outside the parent element.

{{< example >}}
<div class="d-flex position-relative">
  {{< placeholder width="144" height="144" class="flex-shrink-0 mr-3" text="false" title="Generic placeholder image" >}}
  <div>
    <h5 class="mt-0">Custom component with stretched link</h5>
    <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
    <a href="#" class="stretched-link">Go somewhere</a>
  </div>
</div>
{{< /example >}}

Columns are `position: relative` by default, so clickable columns only require the `.stretched-link` class on a link. However, stretching a link over an entire `.row` requires `.position-static` on the column and `.position-relative` on the row.

{{< example >}}
<div class="row no-gutters bg-light position-relative">
  <div class="col-md-6 mb-md-0 p-md-4">
    {{< placeholder width="100%" height="200" class="w-100" text="false" title="Generic placeholder image" >}}
  </div>
  <div class="col-md-6 position-static p-4 pl-md-0">
    <h5 class="mt-0">Columns with stretched link</h5>
    <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
    <a href="#" class="stretched-link">Go somewhere</a>
  </div>
</div>
{{< /example >}}

## Identifying the containing block

If the stretched link doesn't seem to work, the [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block#Identifying_the_containing_block) will probably be the cause. The following CSS properties will make an element the containing block:

- A `position` value other than `static`
- A `transform` or `perspective` value other than `none`
- A `will-change` value of `transform` or `perspective`
- A `filter` value other than `none` or a `will-change` value of `filter` (only works on Firefox)

{{< example >}}
<div class="card" style="width: 18rem;">
  {{< placeholder width="100%" height="180" class="card-img-top" text="false" title="Card image cap" >}}
  <div class="card-body">
    <h5 class="card-title">Card with stretched links</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <p class="card-text">
      <a href="#" class="stretched-link text-danger" style="position: relative;">Stretched link will not work here, because <code>position: relative</code> is added to the link</a>
    </p>
    <p class="card-text bg-light" style="transform: rotate(0);">
      This <a href="#" class="text-warning stretched-link">stretched link</a> will only be spread over the <code>p</code>-tag, because a transform is applied to it.
    </p>
  </div>
</div>
{{< /example >}}
```
## _site_content_docs_4_3_content_typography_md
```---
layout: docs
title: Typography
description: Documentation and examples for Bootstrap typography, including global settings, headings, body text, lists, and more.
group: content
toc: true
---

## Global settings

Bootstrap sets basic global display, typography, and link styles. When more control is needed, check out the [textual utility classes]({{< docsref "/utilities/text" >}}).

- Use a [native font stack]({{< docsref "/content/reboot#native-font-stack" >}}) that selects the best `font-family` for each OS and device.
- For a more inclusive and accessible type scale, we assume the browser default root `font-size` (typically 16px) so visitors can customize their browser defaults as needed.
- Use the `$font-family-base`, `$font-size-base`, and `$line-height-base` attributes as our typographic base applied to the `<body>`.
- Set the global link color via `$link-color` and apply link underlines only on `:hover`.
- Use `$body-bg` to set a `background-color` on the `<body>` (`#fff` by default).

These styles can be found within `_reboot.scss`, and the global variables are defined in `_variables.scss`. Make sure to set `$font-size-base` in `rem`.

## Headings

All HTML headings, `<h1>` through `<h6>`, are available.

<table class="table">
  <thead>
    <tr>
      <th>Heading</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        {{< markdown >}}`<h1></h1>`{{< /markdown >}}
      </td>
      <td><span class="h1">h1. Bootstrap heading</span></td>
    </tr>
    <tr>
      <td>
        {{< markdown >}}`<h2></h2>`{{< /markdown >}}
      </td>
      <td><span class="h2">h2. Bootstrap heading</span></td>
    </tr>
    <tr>
      <td>
        {{< markdown >}}`<h3></h3>`{{< /markdown >}}
      </td>
      <td><span class="h3">h3. Bootstrap heading</span></td>
    </tr>
    <tr>
      <td>
        {{< markdown >}}`<h4></h4>`{{< /markdown >}}
      </td>
      <td><span class="h4">h4. Bootstrap heading</span></td>
    </tr>
    <tr>
      <td>
        {{< markdown >}}`<h5></h5>`{{< /markdown >}}
      </td>
      <td><span class="h5">h5. Bootstrap heading</span></td>
    </tr>
    <tr>
      <td>
        {{< markdown >}}`<h6></h6>`{{< /markdown >}}
      </td>
      <td><span class="h6">h6. Bootstrap heading</span></td>
    </tr>
  </tbody>
</table>

{{< highlight html >}}
<h1>h1. Bootstrap heading</h1>
<h2>h2. Bootstrap heading</h2>
<h3>h3. Bootstrap heading</h3>
<h4>h4. Bootstrap heading</h4>
<h5>h5. Bootstrap heading</h5>
<h6>h6. Bootstrap heading</h6>
{{< /highlight >}}

`.h1` through `.h6` classes are also available, for when you want to match the font styling of a heading but cannot use the associated HTML element.

{{< example >}}
<p class="h1">h1. Bootstrap heading</p>
<p class="h2">h2. Bootstrap heading</p>
<p class="h3">h3. Bootstrap heading</p>
<p class="h4">h4. Bootstrap heading</p>
<p class="h5">h5. Bootstrap heading</p>
<p class="h6">h6. Bootstrap heading</p>
{{< /example >}}

### Customizing headings

Use the included utility classes to recreate the small secondary heading text from Bootstrap 3.

{{< example >}}
<h3>
  Fancy display heading
  <small class="text-muted">With faded secondary text</small>
</h3>
{{< /example >}}

## Display headings

Traditional heading elements are designed to work best in the meat of your page content. When you need a heading to stand out, consider using a **display heading**—a larger, slightly more opinionated heading style. Keep in mind these headings are not responsive by default, but it's possible to enable [responsive font sizes](#responsive-font-sizes).

<div class="bd-example">
  <div class="display-1 pb-3 mb-3 border-bottom">Display 1</div>
  <div class="display-2 pb-3 mb-3 border-bottom">Display 2</div>
  <div class="display-3 pb-3 mb-3 border-bottom">Display 3</div>
  <div class="display-4">Display 4</div>
</div>

{{< highlight html >}}
<h1 class="display-1">Display 1</h1>
<h1 class="display-2">Display 2</h1>
<h1 class="display-3">Display 3</h1>
<h1 class="display-4">Display 4</h1>
{{< /highlight >}}

## Lead

Make a paragraph stand out by adding `.lead`.

{{< example >}}
<p class="lead">
  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Duis mollis, est non commodo luctus.
</p>
{{< /example >}}

## Inline text elements

Styling for common inline HTML5 elements.

{{< example >}}
<p>You can use the mark tag to <mark>highlight</mark> text.</p>
<p><del>This line of text is meant to be treated as deleted text.</del></p>
<p><s>This line of text is meant to be treated as no longer accurate.</s></p>
<p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
<p><u>This line of text will render as underlined</u></p>
<p><small>This line of text is meant to be treated as fine print.</small></p>
<p><strong>This line rendered as bold text.</strong></p>
<p><em>This line rendered as italicized text.</em></p>
{{< /example >}}

`.mark` and `.small` classes are also available to apply the same styles as `<mark>` and `<small>` while avoiding any unwanted semantic implications that the tags would bring.

While not shown above, feel free to use `<b>` and `<i>` in HTML5. `<b>` is meant to highlight words or phrases without conveying additional importance while `<i>` is mostly for voice, technical terms, etc.

## Text utilities

Change text alignment, transform, style, weight, line-height and color with our [text utilities]({{< docsref "/utilities/text" >}}) and [color utilities]({{< docsref "/utilities/colors" >}}).

## Abbreviations

Stylized implementation of HTML's `<abbr>` element for abbreviations and acronyms to show the expanded version on hover. Abbreviations have a default underline and gain a help cursor to provide additional context on hover and to users of assistive technologies.

Add `.initialism` to an abbreviation for a slightly smaller font-size.

{{< example >}}
<p><abbr title="attribute">attr</abbr></p>
<p><abbr title="HyperText Markup Language" class="initialism">HTML</abbr></p>
{{< /example >}}

## Blockquotes

For quoting blocks of content from another source within your document. Wrap `<blockquote class="blockquote">` around any <abbr title="HyperText Markup Language">HTML</abbr> as the quote.

{{< example >}}
<blockquote class="blockquote">
  <p class="mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
</blockquote>
{{< /example >}}

### Naming a source

Add a `<footer class="blockquote-footer">` for identifying the source. Wrap the name of the source work in `<cite>`.

{{< example >}}
<blockquote class="blockquote">
  <p class="mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
  <footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite></footer>
</blockquote>
{{< /example >}}

### Alignment

Use text utilities as needed to change the alignment of your blockquote.

{{< example >}}
<blockquote class="blockquote text-center">
  <p class="mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
  <footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite></footer>
</blockquote>
{{< /example >}}

{{< example >}}
<blockquote class="blockquote text-right">
  <p class="mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
  <footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite></footer>
</blockquote>
{{< /example >}}

## Lists

### Unstyled

Remove the default `list-style` and left margin on list items (immediate children only). **This only applies to immediate children list items**, meaning you will need to add the class for any nested lists as well.

{{< example >}}
<ul class="list-unstyled">
  <li>Lorem ipsum dolor sit amet</li>
  <li>Consectetur adipiscing elit</li>
  <li>Integer molestie lorem at massa</li>
  <li>Facilisis in pretium nisl aliquet</li>
  <li>Nulla volutpat aliquam velit
    <ul>
      <li>Phasellus iaculis neque</li>
      <li>Purus sodales ultricies</li>
      <li>Vestibulum laoreet porttitor sem</li>
      <li>Ac tristique libero volutpat at</li>
    </ul>
  </li>
  <li>Faucibus porta lacus fringilla vel</li>
  <li>Aenean sit amet erat nunc</li>
  <li>Eget porttitor lorem</li>
</ul>
{{< /example >}}

### Inline

Remove a list's bullets and apply some light `margin` with a combination of two classes, `.list-inline` and `.list-inline-item`.

{{< example >}}
<ul class="list-inline">
  <li class="list-inline-item">Lorem ipsum</li>
  <li class="list-inline-item">Phasellus iaculis</li>
  <li class="list-inline-item">Nulla volutpat</li>
</ul>
{{< /example >}}

### Description list alignment

Align terms and descriptions horizontally by using our grid system's predefined classes (or semantic mixins). For longer terms, you can optionally add a `.text-truncate` class to truncate the text with an ellipsis.

{{< example >}}
<dl class="row">
  <dt class="col-sm-3">Description lists</dt>
  <dd class="col-sm-9">A description list is perfect for defining terms.</dd>

  <dt class="col-sm-3">Euismod</dt>
  <dd class="col-sm-9">
    <p>Vestibulum id ligula porta felis euismod semper eget lacinia odio sem nec elit.</p>
    <p>Donec id elit non mi porta gravida at eget metus.</p>
  </dd>

  <dt class="col-sm-3">Malesuada porta</dt>
  <dd class="col-sm-9">Etiam porta sem malesuada magna mollis euismod.</dd>

  <dt class="col-sm-3 text-truncate">Truncated term is truncated</dt>
  <dd class="col-sm-9">Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</dd>

  <dt class="col-sm-3">Nesting</dt>
  <dd class="col-sm-9">
    <dl class="row">
      <dt class="col-sm-4">Nested definition list</dt>
      <dd class="col-sm-8">Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc.</dd>
    </dl>
  </dd>
</dl>
{{< /example >}}

## Responsive font sizes

Bootstrap v4.3 ships with the option to enable responsive font sizes, allowing text to scale more naturally across device and viewport sizes. <abbr title="Responsive font sizes">RFS</abbr> can be enabled by changing the `$enable-responsive-font-sizes` Sass variable to `true` and recompiling Bootstrap.

To support <abbr title="Responsive font sizes">RFS</abbr>, we use a Sass mixin to replace our normal `font-size` properties. Responsive font sizes will be compiled into `calc()` functions with a mix of `rem` and viewport units to enable the responsive scaling behavior. More about <abbr title="Responsive font sizes">RFS</abbr> and its configuration can be found on its [GitHub repository](https://github.com/twbs/rfs).
```
## _site_content_docs_4_3_components_breadcrumb_md
```---
layout: docs
title: Breadcrumb
description: Indicate the current page's location within a navigational hierarchy that automatically adds separators via CSS.
group: components
---

## Example

{{< example >}}
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item active" aria-current="page">Home</li>
  </ol>
</nav>

<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item active" aria-current="page">Library</li>
  </ol>
</nav>

<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item"><a href="#">Library</a></li>
    <li class="breadcrumb-item active" aria-current="page">Data</li>
  </ol>
</nav>
{{< /example >}}

## Changing the separator

Separators are automatically added in CSS through [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/::before) and [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/content). They can be changed by changing `$breadcrumb-divider`. The [quote](https://sass-lang.com/documentation/functions/string#quote) function is needed to generate the quotes around a string, so if you want `>` as separator, you can use this:

'''scss
$breadcrumb-divider: quote(">");
'''

It's also possible to use an **embedded SVG icon**:

'''scss
$breadcrumb-divider: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='8'%3E%3Cpath d='M2.5 0L1 1.5 3.5 4 1 6.5 2.5 8l4-4-4-4z' fill='currentColor'/%3E%3C/svg%3E");
'''

The separator can be removed by setting `$breadcrumb-divider` to `none`:

'''scss
$breadcrumb-divider: none;
'''

## Accessibility

Since breadcrumbs provide a navigation, it's a good idea to add a meaningful label such as `aria-label="breadcrumb"` to describe the type of navigation provided in the `<nav>` element, as well as applying an `aria-current="page"` to the last item of the set to indicate that it represents the current page.

For more information, see the [WAI-ARIA Authoring Practices for the breadcrumb pattern](https://www.w3.org/TR/wai-aria-practices/#breadcrumb).
```
## _site_content_docs_4_3_helpers_clearfix_md
```---
layout: docs
title: Clearfix
description: Quickly and easily clear floated content within a container by adding a clearfix utility.
group: helpers
aliases: "/docs/4.3/helpers/"
---

Easily clear `float`s by adding `.clearfix` **to the parent element**. Can also be used as a mixin.

{{< highlight html >}}
<div class="clearfix">...</div>
{{< /highlight >}}

{{< highlight scss >}}
// Mixin itself
@mixin clearfix() {
  &::after {
    display: block;
    content: "";
    clear: both;
  }
}

// Usage as a mixin
.element {
  @include clearfix;
}
{{< /highlight >}}

The following example shows how the clearfix can be used. Without the clearfix the wrapping div would not span around the buttons which would cause a broken layout.

{{< example >}}
<div class="bg-info clearfix">
  <button type="button" class="btn btn-secondary float-left">Example Button floated left</button>
  <button type="button" class="btn btn-secondary float-right">Example Button floated right</button>
</div>
{{< /example >}}
```
## _site_layouts_partials_callout_info_prefersreducedmotion_md
```The animation effect of this component is dependent on the `prefers-reduced-motion` media query. See the [reduced motion section of our accessibility documentation](/docs/{{ .Site.Params.docs_version }}/getting-started/accessibility/#reduced-motion).
```
## _site_content_docs_4_3_getting_started_build_tools_md
```---
layout: docs
title: Build tools
description: Learn how to use Bootstrap's included npm scripts to build our documentation, compile source code, run tests, and more.
group: getting-started
toc: true
---

## Tooling setup

Bootstrap uses [npm scripts](https://docs.npmjs.com/misc/scripts) for its build system. Our [package.json]({{< param repo >}}/blob/v{{< param current_version >}}/package.json) includes convenient methods for working with the framework, including compiling code, running tests, and more.

To use our build system and run our documentation locally, you'll need a copy of Bootstrap's source files and Node. Follow these steps and you should be ready to rock:

1. [Download and install Node.js](https://nodejs.org/en/download/), which we use to manage our dependencies.
2. Navigate to the root `/bootstrap` directory and run `npm install` to install our local dependencies listed in [package.json]({{< param repo >}}/blob/v{{< param current_version >}}/package.json).

When completed, you'll be able to run the various commands provided from the command line.

## Using npm scripts

Our [package.json]({{< param repo >}}/blob/v{{< param current_version >}}/package.json) includes numerous tasks for developing the project. Run `npm run` to see all the npm scripts in your terminal. **Primary tasks include:**

<table class="table">
  <thead>
    <tr>
      <th>Task</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code>npm start</code>
      </td>
      <td>
        Compiles CSS and JavaScript, builds the documentation, and starts a local server.
      </td>
    </tr>
    <tr>
      <td>
        <code>npm run dist</code>
      </td>
      <td>
       Creates the <code>dist/</code> directory with compiled files. Requires <a href="https://sass-lang.com/">Sass</a>, <a href="https://github.com/postcss/autoprefixer">Autoprefixer</a>, and <a href="https://github.com/terser/terser">terser</a>.
      </td>
    </tr>
    <tr>
      <td>
        <code>npm test</code>
      </td>
      <td>
        Runs tests locally after running <code>npm run dist</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>npm run docs-serve</code>
      </td>
      <td>
        Builds and runs the documentation locally.
      </td>
    </tr>
  </tbody>
</table>

## Autoprefixer

Bootstrap uses [Autoprefixer][autoprefixer] (included in our build process) to automatically add vendor prefixes to some CSS properties at build time. Doing so saves us time and code by allowing us to write key parts of our CSS a single time while eliminating the need for vendor mixins like those found in v3.

We maintain the list of browsers supported through Autoprefixer in a separate file within our GitHub repository. See [.browserslistrc]({{< param repo >}}/blob/v{{< param current_version >}}/.browserslistrc) for details.

## Local documentation

Running our documentation locally requires the use of Hugo, which gets installed via the [hugo-bin](https://www.npmjs.com/package/hugo-bin) npm package. Hugo is a blazingly fast and quite extensible static site generator that provides us: basic includes, Markdown-based files, templates, and more. Here's how to get it started:

1. Run through the [tooling setup](#tooling-setup) above to install all dependencies.
2. From the root `/bootstrap` directory, run `npm run docs-serve` in the command line.
3. Open `http://localhost:9001/` in your browser, and voilà.

Learn more about using Hugo by reading its [documentation](https://gohugo.io/documentation/).

## Troubleshooting

Should you encounter problems with installing dependencies, uninstall all previous dependency versions (global and local). Then, rerun `npm install`.

[autoprefixer]: https://github.com/postcss/autoprefixer
```
## _site_content_docs_4_3_layout_overview_md
```---
layout: docs
title: Overview
description: Components and options for laying out your Bootstrap project, including wrapping containers, a powerful grid system, and responsive utility classes.
group: layout
aliases: "/docs/4.3/layout/"
toc: true
---

## Containers

Containers are the most basic layout element in Bootstrap and are **required when using our default grid system**. Containers are used to contain, pad, and (sometimes) center the content within them. While containers *can* be nested, most layouts do not require a nested container.

Bootstrap comes with three different containers:

- `.container`, which sets a `max-width` at each responsive breakpoint
- `.container-fluid`, which is `width: 100%` at all breakpoints
- `.container-{breakpoint}`, which is `width: 100%` until the specified breakpoint

The table below illustrates how each container's `max-width` compares to the original `.container` and `.container-fluid` across each breakpoint.

See them in action and compare them in our [Grid example]({{< docsref "/examples/grid#containers" >}}).

<table class="table text-left">
  <thead>
    <tr>
      <th></th>
      <th>
        Extra small<br>
        <span class="font-weight-normal">&lt;576px</span>
      </th>
      <th>
        Small<br>
        <span class="font-weight-normal">&ge;576px</span>
      </th>
      <th>
        Medium<br>
        <span class="font-weight-normal">&ge;768px</span>
      </th>
      <th>
        Large<br>
        <span class="font-weight-normal">&ge;992px</span>
      </th>
      <th>
        Extra large<br>
        <span class="font-weight-normal">&ge;1200px</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>.container</code></td>
      <td class="text-muted">100%</td>
      <td>540px</td>
      <td>720px</td>
      <td>960px</td>
      <td>1140px</td>
    </tr>
    <tr>
      <td><code>.container-sm</code></td>
      <td class="text-muted">100%</td>
      <td>540px</td>
      <td>720px</td>
      <td>960px</td>
      <td>1140px</td>
    </tr>
    <tr>
      <td><code>.container-md</code></td>
      <td class="text-muted">100%</td>
      <td class="text-muted">100%</td>
      <td>720px</td>
      <td>960px</td>
      <td>1140px</td>
    </tr>
    <tr>
      <td><code>.container-lg</code></td>
      <td class="text-muted">100%</td>
      <td class="text-muted">100%</td>
      <td class="text-muted">100%</td>
      <td>960px</td>
      <td>1140px</td>
    </tr>
    <tr>
      <td><code>.container-xl</code></td>
      <td class="text-muted">100%</td>
      <td class="text-muted">100%</td>
      <td class="text-muted">100%</td>
      <td class="text-muted">100%</td>
      <td>1140px</td>
    </tr>
    <tr>
      <td><code>.container-fluid</code></td>
      <td class="text-muted">100%</td>
      <td class="text-muted">100%</td>
      <td class="text-muted">100%</td>
      <td class="text-muted">100%</td>
      <td class="text-muted">100%</td>
    </tr>
  </tbody>
</table>

### All-in-one

Our default `.container` class is a responsive, fixed-width container, meaning its `max-width` changes at each breakpoint.

{{< highlight html >}}
<div class="container">
  <!-- Content here -->
</div>
{{< /highlight >}}

### Fluid

Use `.container-fluid` for a full width container, spanning the entire width of the viewport.

{{< highlight html >}}
<div class="container-fluid">
  ...
</div>
{{< /highlight >}}

### Responsive

Responsive containers are new in Bootstrap v4.4. They allow you to specify a class that is 100% wide until the specified breakpoint is reached, after which we apply `max-width`s for each of the higher breakpoints. For example, `.container-sm` is 100% wide to start until the `sm` breakpoint is reached, where it will scale up with `md`, `lg`, and `xl`.

{{< highlight html >}}
<div class="container-sm">100% wide until small breakpoint</div>
<div class="container-md">100% wide until medium breakpoint</div>
<div class="container-lg">100% wide until large breakpoint</div>
<div class="container-xl">100% wide until extra large breakpoint</div>
{{< /highlight >}}

## Responsive breakpoints

Since Bootstrap is developed to be mobile first, we use a handful of [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries) to create sensible breakpoints for our layouts and interfaces. These breakpoints are mostly based on minimum viewport widths and allow us to scale up elements as the viewport changes.

Bootstrap primarily uses the following media query ranges—or breakpoints—in our source Sass files for our layout, grid system, and components.

{{< highlight scss >}}
// Extra small devices (portrait phones, less than 576px)
// No media query for `xs` since this is the default in Bootstrap

// Small devices (landscape phones, 576px and up)
@media (min-width: 576px) { ... }

// Medium devices (tablets, 768px and up)
@media (min-width: 768px) { ... }

// Large devices (desktops, 992px and up)
@media (min-width: 992px) { ... }

// Extra large devices (large desktops, 1200px and up)
@media (min-width: 1200px) { ... }
{{< /highlight >}}

Since we write our source CSS in Sass, all our media queries are available via Sass mixins:

{{< highlight scss >}}
// No media query necessary for xs breakpoint as it's effectively `@media (min-width: 0) { ... }`
@include media-breakpoint-up(sm) { ... }
@include media-breakpoint-up(md) { ... }
@include media-breakpoint-up(lg) { ... }
@include media-breakpoint-up(xl) { ... }

// Example: Hide starting at `min-width: 0`, and then show at the `sm` breakpoint
.custom-class {
  display: none;
}
@include media-breakpoint-up(sm) {
  .custom-class {
    display: block;
  }
}
{{< /highlight >}}

We occasionally use media queries that go in the other direction (the given screen size *or smaller*):

{{< highlight scss >}}
// Extra small devices (portrait phones, less than 576px)
@media (max-width: 575.98px) { ... }

// Small devices (landscape phones, less than 768px)
@media (max-width: 767.98px) { ... }

// Medium devices (tablets, less than 992px)
@media (max-width: 991.98px) { ... }

// Large devices (desktops, less than 1200px)
@media (max-width: 1199.98px) { ... }

// Extra large devices (large desktops)
// No media query since the extra-large breakpoint has no upper bound on its width
{{< /highlight >}}

{{< callout info >}}
{{< partial "callout-info-mediaqueries-breakpoints.md" >}}
{{< /callout >}}

Once again, these media queries are also available via Sass mixins:

{{< highlight scss >}}
@include media-breakpoint-down(xs) { ... }
@include media-breakpoint-down(sm) { ... }
@include media-breakpoint-down(md) { ... }
@include media-breakpoint-down(lg) { ... }
// No media query necessary for xl breakpoint as it has no upper bound on its width

// Example: Style from medium breakpoint and down
@include media-breakpoint-down(md) {
  .custom-class {
    display: block;
  }
}
{{< /highlight >}}

There are also media queries and mixins for targeting a single segment of screen sizes using the minimum and maximum breakpoint widths.

{{< highlight scss >}}
// Extra small devices (portrait phones, less than 576px)
@media (max-width: 575.98px) { ... }

// Small devices (landscape phones, 576px and up)
@media (min-width: 576px) and (max-width: 767.98px) { ... }

// Medium devices (tablets, 768px and up)
@media (min-width: 768px) and (max-width: 991.98px) { ... }

// Large devices (desktops, 992px and up)
@media (min-width: 992px) and (max-width: 1199.98px) { ... }

// Extra large devices (large desktops, 1200px and up)
@media (min-width: 1200px) { ... }
{{< /highlight >}}

These media queries are also available via Sass mixins:

{{< highlight scss >}}
@include media-breakpoint-only(xs) { ... }
@include media-breakpoint-only(sm) { ... }
@include media-breakpoint-only(md) { ... }
@include media-breakpoint-only(lg) { ... }
@include media-breakpoint-only(xl) { ... }
{{< /highlight >}}

Similarly, media queries may span multiple breakpoint widths:

{{< highlight scss >}}
// Example
// Apply styles starting from medium devices and up to extra large devices
@media (min-width: 768px) and (max-width: 1199.98px) { ... }
{{< /highlight >}}

The Sass mixin for targeting the same screen size range would be:

{{< highlight scss >}}
@include media-breakpoint-between(md, xl) { ... }
{{< /highlight >}}

## Z-index

Several Bootstrap components utilize `z-index`, the CSS property that helps control layout by providing a third axis to arrange content. We utilize a default z-index scale in Bootstrap that's been designed to properly layer navigation, tooltips and popovers, modals, and more.

These higher values start at an arbitrary number, high and specific enough to ideally avoid conflicts. We need a standard set of these across our layered components—tooltips, popovers, navbars, dropdowns, modals—so we can be reasonably consistent in the behaviors. There's no reason we couldn't have used `100`+ or `500`+.

We don't encourage customization of these individual values; should you change one, you likely need to change them all.

{{< highlight scss >}}
$zindex-dropdown:          1000 !default;
$zindex-sticky:            1020 !default;
$zindex-fixed:             1030 !default;
$zindex-modal-backdrop:    1040 !default;
$zindex-modal:             1050 !default;
$zindex-popover:           1060 !default;
$zindex-tooltip:           1070 !default;
{{< /highlight >}}

To handle overlapping borders within components (e.g., buttons and inputs in input groups), we use low single digit `z-index` values of `1`, `2`, and `3` for default, hover, and active states. On hover/focus/active, we bring a particular element to the forefront with a higher `z-index` value to show their border over the sibling elements.
```
## _site_content_docs_4_3_helpers_embed_md
```---
layout: docs
title: Embeds
description: Create responsive video or slideshow embeds based on the width of the parent by creating an intrinsic ratio that scales on any device.
group: helpers
toc: true
---

## About

Rules are directly applied to `<iframe>`, `<embed>`, `<video>`, and `<object>` elements; optionally use an explicit descendant class `.embed-responsive-item` when you want to match the styling for other attributes.

**Pro-Tip!** You don't need to include `frameborder="0"` in your `<iframe>`s as we override that for you.

## Example

Wrap any embed like an `<iframe>` in a parent element with `.embed-responsive` and an aspect ratio. The `.embed-responsive-item` isn't strictly required, but we encourage it.

{{< example >}}
<div class="embed-responsive embed-responsive-16by9">
  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0" allowfullscreen></iframe>
</div>
{{< /example >}}

## Aspect ratios

Aspect ratios can be customized with modifier classes. By default the following ratio classes are provided:

{{< highlight html >}}
<!-- 21:9 aspect ratio -->
<div class="embed-responsive embed-responsive-21by9">
  <iframe class="embed-responsive-item" src="..."></iframe>
</div>

<!-- 16:9 aspect ratio -->
<div class="embed-responsive embed-responsive-16by9">
  <iframe class="embed-responsive-item" src="..."></iframe>
</div>

<!-- 4:3 aspect ratio -->
<div class="embed-responsive embed-responsive-4by3">
  <iframe class="embed-responsive-item" src="..."></iframe>
</div>

<!-- 1:1 aspect ratio -->
<div class="embed-responsive embed-responsive-1by1">
  <iframe class="embed-responsive-item" src="..."></iframe>
</div>
{{< /highlight >}}

Within `_variables.scss`, you can change the aspect ratios you want to use. Here's an example of the `$embed-responsive-aspect-ratios` map:

{{< highlight scss >}}
$embed-responsive-aspect-ratios: (
  "21by9": (
    x: 21,
    y: 9
  ),
  "16by9": (
    x: 16,
    y: 9
  ),
  "4by3": (
    x: 4,
    y: 3
  ),
  "1by1": (
    x: 1,
    y: 1
  )
);
{{< /highlight >}}
```
## _SECURITY_md
```# Reporting Security Issues

The Bootstrap team and community take security issues in Bootstrap seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

To report a security issue, email [security@getbootstrap.com](mailto:security@getbootstrap.com) and include the word "SECURITY" in the subject line.

We'll endeavor to respond quickly, and will keep you updated throughout the process.
```
## _site_content_docs_4_3_components_progress_md
```---
layout: docs
title: Progress
description: Documentation and examples for using Bootstrap custom progress bars featuring support for stacked bars, animated backgrounds, and text labels.
group: components
toc: true
---

## How it works

Progress components are built with two HTML elements, some CSS to set the width, and a few attributes. We don't use [the HTML5 `<progress>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress), ensuring you can stack progress bars, animate them, and place text labels over them.

- We use the `.progress` as a wrapper to indicate the max value of the progress bar.
- We use the inner `.progress-bar` to indicate the progress so far.
- The `.progress-bar` requires an inline style, utility class, or custom CSS to set their width.
- The `.progress-bar` also requires some `role` and `aria` attributes to make it accessible.

Put that all together, and you have the following examples.

{{< example >}}
<div class="progress">
  <div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
</div>
{{< /example >}}

Bootstrap provides a handful of [utilities for setting width]({{< docsref "/utilities/sizing" >}}). Depending on your needs, these may help with quickly configuring progress.

{{< example >}}
<div class="progress">
  <div class="progress-bar w-75" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
</div>
{{< /example >}}

## Labels

Add labels to your progress bars by placing text within the `.progress-bar`.

{{< example >}}
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
</div>
{{< /example >}}

## Height

We only set a `height` value on the `.progress`, so if you change that value the inner `.progress-bar` will automatically resize accordingly.

{{< example >}}
<div class="progress" style="height: 1px;">
  <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress" style="height: 20px;">
  <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
</div>
{{< /example >}}

## Backgrounds

Use background utility classes to change the appearance of individual progress bars.

{{< example >}}
<div class="progress">
  <div class="progress-bar bg-success" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar bg-info" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar bg-warning" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar bg-danger" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
</div>
{{< /example >}}

## Multiple bars

Include multiple progress bars in a progress component if you need.

{{< example >}}
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 15%" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-bar bg-success" role="progressbar" style="width: 30%" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-bar bg-info" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
</div>
{{< /example >}}

## Striped

Add `.progress-bar-striped` to any `.progress-bar` to apply a stripe via CSS gradient over the progress bar's background color.

{{< example >}}
<div class="progress">
  <div class="progress-bar progress-bar-striped" role="progressbar" style="width: 10%" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar progress-bar-striped bg-success" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar progress-bar-striped bg-info" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar progress-bar-striped bg-warning" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar progress-bar-striped bg-danger" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
</div>
{{< /example >}}

## Animated stripes

The striped gradient can also be animated. Add `.progress-bar-animated` to `.progress-bar` to animate the stripes right to left via CSS3 animations.

<div class="bd-example">
  <div class="progress">
    <div class="progress-bar progress-bar-striped" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 75%"></div>
  </div>
  <button type="button" class="btn btn-secondary mt-3" data-toggle="button" id="btnToggleAnimatedProgress" aria-pressed="false" autocomplete="off">
    Toggle animation
  </button>
</div>

{{< highlight html >}}
<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 75%"></div>
</div>
{{< /highlight >}}
```
## _site_content_docs_4_3_utilities_api_md
```---
layout: docs
title: Utility API
description: The utility API is a Sass based tool to generate utility classes.
group: utilities
aliases: "/docs/4.3/utilities/"
toc: true
---

The bootstrap utilities are generated with the utility API which can be used to change or extend Bootstraps utility classes. If you don't have any idea what Sass maps are, you can consult the [official docs](https://sass-lang.com/documentation/values/maps) to get started.

The `$utilities` map contains all utilities and is later merged with your custom `$utilities` map if present. The utility map contains a keyed list of utility groups which accept the following options:

- `property`: Name of the property, this can be a string or an array of strings (needed for eg. horizontal paddings or margins).
- `responsive` _(optional)_: Boolean indicating if responsive classes need to be generated. `false` by default.
- `class` _(optional)_: Variable to change the class name if you don't want it to be the same as the property. In case you don't provide the `class` key and `property` key is an array of strings, the class name will be the first element of the `property` array.
- `values`: This can be a list of values or a map if you don't want the class name to be the same as the value. If null is used as map key, it isn't rendered.
- `print` _(optional)_: Boolean indicating if print classes need to be generated. `false` by default.


## Adding utilities to the utility API

All utility variables are added to the `$utilities` variable. Custom utility groups can added like this:

'''scss
$utilities: (
  "opacity": (
    property: opacity,
    values: (
      0: 0,
      25: .25,
      50: .5,
      100: 1,
    )
  )
 );
'''

Output:

'''css
.opacity-0 {
  opacity: 0;
}
.opacity-25 {
  opacity: .25;
}
.opacity-75 {
  opacity: .75;
}
.opacity-100 {
  opacity: 1;
}
'''


## Changing the class prefix

With the `class` option, the class prefix can be changed:

'''scss
$utilities: (
  "opacity": (
    property: opacity,
    class: o,
    values: (
      0: 0,
      25: .25,
      50: .5,
      100: 1,
    )
  )
 );
'''

Output:

'''css
.o-0 {
  opacity: 0;
}
.o-25 {
  opacity: .25;
}
.o-75 {
  opacity: .75;
}
.o-100 {
  opacity: 1;
}
'''

## Responsive utilities

With the `responsive` option, responsive utility classes can be generated:

'''scss
$utilities: (
  "opacity": (
    property: opacity,
    responsive: true,
    values: (
      0: 0,
      25: .25,
      50: .5,
      100: 1,
    )
  )
 );
'''

Output:

'''css
.opacity-0 {
  opacity: 0;
}
.opacity-25 {
  opacity: .25;
}
.opacity-75 {
  opacity: .75;
}
.opacity-100 {
  opacity: 1;
}
@media (min-width: 576px) {
  .opacity-sm-0 {
    opacity: 0;
  }
  .opacity-sm-25 {
    opacity: .25;
  }
  .opacity-sm-75 {
    opacity: .75;
  }
  .opacity-sm-100 {
    opacity: 1;
  }
}
@media (min-width: 768px) {
  .opacity-md-0 {
    opacity: 0;
  }
  .opacity-md-25 {
    opacity: .25;
  }
  .opacity-md-75 {
    opacity: .75;
  }
  .opacity-md-100 {
    opacity: 1;
  }
}
@media (min-width: 992px) {
  .opacity-lg-0 {
    opacity: 0;
  }
  .opacity-lg-25 {
    opacity: .25;
  }
  .opacity-lg-75 {
    opacity: .75;
  }
  .opacity-lg-100 {
    opacity: 1;
  }
}
@media (min-width: 1200px) {
  .opacity-xl-0 {
    opacity: 0;
  }
  .opacity-xl-25 {
    opacity: .25;
  }
  .opacity-xl-75 {
    opacity: .75;
  }
  .opacity-xl-100 {
    opacity: 1;
  }
}
'''

## Changing utilities

Overriding excising utilities is possible by using the same key. For example if you want more responsive overflow
utility classes you can do this:

'''scss
$utilities: (
  "overflow": (
    responsive: true,
    property: overflow,
    values: visible hidden scroll auto,
  ),
);
'''


## Print utilities

Enabling the `print` option will **also** generate utility classes for print.

'''scss
$utilities: (
  "opacity": (
    property: opacity,
    class: o,
    print: true,
    values: (
      0: 0,
      25: .25,
      50: .5,
      100: 1,
    )
  )
 );
'''

Output:

'''css
.o-0 {
  opacity: 0;
}
.o-25 {
  opacity: .25;
}
.o-75 {
  opacity: .75;
}
.o-100 {
  opacity: 1;
}

@media print {
  .o-print-0 {
    opacity: 0;
  }
  .o-print-25 {
    opacity: .25;
  }
  .o-print-75 {
    opacity: .75;
  }
  .o-print-100 {
    opacity: 1;
  }
}
'''

## Removing utilities

Utilities can also be removed by changing the group key to `null`:

'''scss
$utilities: (
  "float": null,
);
'''
```
## _site_layouts_partials_callout_warning_input_support_md
```##### Date & color input support

Keep in mind date inputs are [not fully supported](https://caniuse.com/#feat=input-datetime) by IE and Safari. Color inputs also [lack support](https://caniuse.com/#feat=input-color) on IE.
```
## _site_layouts_partials_callout_danger_async_methods_md
```#### Asynchronous methods and transitions

All API methods are **asynchronous** and start a **transition**. They return to the caller as soon as the transition is started but **before it ends**. In addition, a method call on a **transitioning component will be ignored**.

[See our JavaScript documentation for more information](/docs/{{ .Site.Params.docs_version }}/getting-started/javascript/).
```
## _site_content_docs_4_3_utilities_visibility_md
```---
layout: docs
title: Visibility
description: Control the visibility, without modifying the display, of elements with visibility utilities.
group: utilities
---

Set the `visibility` of elements with our visibility utilities. These utility classes do not modify the `display` value at all and do not affect layout – `.invisible` elements still take up space in the page. Content will be hidden both visually and for assistive technology/screen reader users.

Apply `.visible` or `.invisible` as needed.

{{< highlight html >}}
<div class="visible">...</div>
<div class="invisible">...</div>
{{< /highlight >}}

{{< highlight scss >}}
// Class
.visible {
  visibility: visible !important;
}
.invisible {
  visibility: hidden !important;
}
{{< /highlight >}}
```
## _README_md
```<p align="center">
  <a href="https://getbootstrap.com/">
    <img src="https://getbootstrap.com/docs/4.3/assets/brand/bootstrap-solid.svg" alt="Bootstrap logo" width="72" height="72">
  </a>
</p>

<h3 align="center">Bootstrap</h3>

<p align="center">
  Sleek, intuitive, and powerful front-end framework for faster and easier web development.
  <br>
  <a href="https://getbootstrap.com/docs/4.3/"><strong>Explore Bootstrap docs »</strong></a>
  <br>
  <br>
  <a href="https://github.com/twbs/bootstrap/issues/new?template=bug.md">Report bug</a>
  ·
  <a href="https://github.com/twbs/bootstrap/issues/new?template=feature.md&labels=feature">Request feature</a>
  ·
  <a href="https://themes.getbootstrap.com/">Themes</a>
  ·
  <a href="https://blog.getbootstrap.com/">Blog</a>
</p>


## Table of contents

- [Quick start](#quick-start)
- [Status](#status)
- [What's included](#whats-included)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Community](#community)
- [Versioning](#versioning)
- [Creators](#creators)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)


## Quick start

Several quick start options are available:

- [Download the latest release.](https://github.com/twbs/bootstrap/archive/v4.3.1.zip)
- Clone the repo: `git clone https://github.com/twbs/bootstrap.git`
- Install with [npm](https://www.npmjs.com/): `npm install bootstrap`
- Install with [yarn](https://yarnpkg.com/): `yarn add bootstrap@4.3.1`
- Install with [Composer](https://getcomposer.org/): `composer require twbs/bootstrap:4.3.1`
- Install with [NuGet](https://www.nuget.org/): CSS: `Install-Package bootstrap` Sass: `Install-Package bootstrap.sass`

Read the [Getting started page](https://getbootstrap.com/docs/4.3/getting-started/introduction/) for information on the framework contents, templates and examples, and more.


## Status

[![Build Status](https://github.com/twbs/bootstrap/workflows/Tests/badge.svg)](https://github.com/twbs/bootstrap/actions?workflow=Tests)
[![npm version](https://img.shields.io/npm/v/bootstrap.svg)](https://www.npmjs.com/package/bootstrap)
[![Gem version](https://img.shields.io/gem/v/bootstrap.svg)](https://rubygems.org/gems/bootstrap)
[![Meteor Atmosphere](https://img.shields.io/badge/meteor-twbs%3Abootstrap-blue.svg)](https://atmospherejs.com/twbs/bootstrap)
[![Packagist Prerelease](https://img.shields.io/packagist/vpre/twbs/bootstrap.svg)](https://packagist.org/packages/twbs/bootstrap)
[![NuGet](https://img.shields.io/nuget/vpre/bootstrap.svg)](https://www.nuget.org/packages/bootstrap/absoluteLatest)
[![peerDependencies Status](https://img.shields.io/david/peer/twbs/bootstrap.svg)](https://david-dm.org/twbs/bootstrap?type=peer)
[![devDependency Status](https://img.shields.io/david/dev/twbs/bootstrap.svg)](https://david-dm.org/twbs/bootstrap?type=dev)
[![Coverage Status](https://img.shields.io/coveralls/github/twbs/bootstrap/master.svg)](https://coveralls.io/github/twbs/bootstrap?branch=master)
[![CSS gzip size](https://img.badgesize.io/twbs/bootstrap/master/dist/css/bootstrap.min.css?compression=gzip&label=CSS+gzip+size)](https://github.com/twbs/bootstrap/tree/master/dist/css/bootstrap.min.css)
[![JS gzip size](https://img.badgesize.io/twbs/bootstrap/master/dist/js/bootstrap.min.js?compression=gzip&label=JS+gzip+size)](https://github.com/twbs/bootstrap/tree/master/dist/js/bootstrap.min.js)
[![BrowserStack Status](https://www.browserstack.com/automate/badge.svg?badge_key=SkxZcStBeExEdVJqQ2hWYnlWckpkNmNEY213SFp6WHFETWk2bGFuY3pCbz0tLXhqbHJsVlZhQnRBdEpod3NLSDMzaHc9PQ==--3d0b75245708616eb93113221beece33e680b229)](https://www.browserstack.com/automate/public-build/SkxZcStBeExEdVJqQ2hWYnlWckpkNmNEY213SFp6WHFETWk2bGFuY3pCbz0tLXhqbHJsVlZhQnRBdEpod3NLSDMzaHc9PQ==--3d0b75245708616eb93113221beece33e680b229)
[![Backers on Open Collective](https://img.shields.io/opencollective/backers/bootstrap.svg)](#backers)
[![Sponsors on Open Collective](https://img.shields.io/opencollective/sponsors/bootstrap.svg)](#sponsors)


## What's included

Within the download you'll find the following directories and files, logically grouping common assets and providing both compiled and minified variations. You'll see something like this:

'''text
bootstrap/
└── dist/
    ├── css/
    │   ├── bootstrap-grid.css
    │   ├── bootstrap-grid.css.map
    │   ├── bootstrap-grid.min.css
    │   ├── bootstrap-grid.min.css.map
    │   ├── bootstrap-reboot.css
    │   ├── bootstrap-reboot.css.map
    │   ├── bootstrap-reboot.min.css
    │   ├── bootstrap-reboot.min.css.map
    │   ├── bootstrap-utilities.css
    │   ├── bootstrap-utilities.css.map
    │   ├── bootstrap-utilities.min.css
    │   ├── bootstrap-utilities.min.css.map
    │   ├── bootstrap.css
    │   ├── bootstrap.css.map
    │   ├── bootstrap.min.css
    │   └── bootstrap.min.css.map
    └── js/
        ├── bootstrap.bundle.js
        ├── bootstrap.bundle.js.map
        ├── bootstrap.bundle.min.js
        ├── bootstrap.bundle.min.js.map
        ├── bootstrap.esm.js
        ├── bootstrap.esm.js.map
        ├── bootstrap.esm.min.js
        ├── bootstrap.esm.min.js.map
        ├── bootstrap.js
        ├── bootstrap.js.map
        ├── bootstrap.min.js
        └── bootstrap.min.js.map
'''

We provide compiled CSS and JS (`bootstrap.*`), as well as compiled and minified CSS and JS (`bootstrap.min.*`). [source maps](https://developers.google.com/web/tools/chrome-devtools/javascript/source-maps) (`bootstrap.*.map`) are available for use with certain browsers' developer tools. Bundled JS files (`bootstrap.bundle.js` and minified `bootstrap.bundle.min.js`) include [Popper](https://popper.js.org/).


## Bugs and feature requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/twbs/bootstrap/blob/master/.github/CONTRIBUTING.md#using-the-issue-tracker) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/twbs/bootstrap/issues/new).


## Documentation

Bootstrap's documentation, included in this repo in the root directory, is built with [Hugo](https://gohugo.io/) and publicly hosted on GitHub Pages at <https://getbootstrap.com/>. The docs may also be run locally.

Documentation search is powered by [Algolia's DocSearch](https://community.algolia.com/docsearch/). Working on our search? Be sure to set `debug: true` in `site/assets/js/src/search.js` file.

### Running documentation locally

1. Run `npm install` to install the Node.js dependencies, including Hugo (the site builder).
2. Run `npm run test` (or a specific npm script) to rebuild distributed CSS and JavaScript files, as well as our docs assets.
3. From the root `/bootstrap` directory, run `npm run docs-serve` in the command line.
4. Open `http://localhost:9001/` in your browser, and voilà.

Learn more about using Hugo by reading its [documentation](https://gohugo.io/documentation/).

### Documentation for previous releases

You can find all our previous releases docs on <https://getbootstrap.com/docs/versions/>.

[Previous releases](https://github.com/twbs/bootstrap/releases) and their documentation are also available for download.


## Contributing

Please read through our [contributing guidelines](https://github.com/twbs/bootstrap/blob/master/.github/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, if your pull request contains JavaScript patches or features, you must include [relevant unit tests](https://github.com/twbs/bootstrap/tree/master/js/tests). All HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Mark Otto](https://github.com/mdo).

Editor preferences are available in the [editor config](https://github.com/twbs/bootstrap/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <https://editorconfig.org/>.


## Community

Get updates on Bootstrap's development and chat with the project maintainers and community members.

- Follow [@getbootstrap on Twitter](https://twitter.com/getbootstrap).
- Read and subscribe to [The Official Bootstrap Blog](https://blog.getbootstrap.com/).
- Join [the official Slack room](https://bootstrap-slack.herokuapp.com/).
- Chat with fellow Bootstrappers in IRC. On the `irc.freenode.net` server, in the `##bootstrap` channel.
- Implementation help may be found at Stack Overflow (tagged [`bootstrap-4`](https://stackoverflow.com/questions/tagged/bootstrap-4)).
- Developers should use the keyword `bootstrap` on packages which modify or add to the functionality of Bootstrap when distributing through [npm](https://www.npmjs.com/browse/keyword/bootstrap) or similar delivery mechanisms for maximum discoverability.


## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Bootstrap is maintained under [the Semantic Versioning guidelines](https://semver.org/). Sometimes we screw up, but we adhere to those rules whenever possible.

See [the Releases section of our GitHub project](https://github.com/twbs/bootstrap/releases) for changelogs for each release version of Bootstrap. Release announcement posts on [the official Bootstrap blog](https://blog.getbootstrap.com/) contain summaries of the most noteworthy changes made in each release.


## Creators

**Mark Otto**

- <https://twitter.com/mdo>
- <https://github.com/mdo>

**Jacob Thornton**

- <https://twitter.com/fat>
- <https://github.com/fat>


## Thanks

<a href="https://www.browserstack.com/">
  <img src="https://live.browserstack.com/images/opensource/browserstack-logo.svg" alt="BrowserStack Logo" width="192" height="42">
</a>

Thanks to [BrowserStack](https://www.browserstack.com/) for providing the infrastructure that allows us to test in real browsers!


## Backers

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/bootstrap#backer)]

[![Bakers](https://opencollective.com/bootstrap/backers.svg?width=890)](https://opencollective.com/bootstrap#backers)


## Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/bootstrap#sponsor)]

[![](https://opencollective.com/bootstrap/sponsor/0/avatar.svg)](https://opencollective.com/bootstrap/sponsor/0/website)
[![](https://opencollective.com/bootstrap/sponsor/1/avatar.svg)](https://opencollective.com/bootstrap/sponsor/1/website)
[![](https://opencollective.com/bootstrap/sponsor/2/avatar.svg)](https://opencollective.com/bootstrap/sponsor/2/website)
[![](https://opencollective.com/bootstrap/sponsor/3/avatar.svg)](https://opencollective.com/bootstrap/sponsor/3/website)
[![](https://opencollective.com/bootstrap/sponsor/4/avatar.svg)](https://opencollective.com/bootstrap/sponsor/4/website)
[![](https://opencollective.com/bootstrap/sponsor/5/avatar.svg)](https://opencollective.com/bootstrap/sponsor/5/website)
[![](https://opencollective.com/bootstrap/sponsor/6/avatar.svg)](https://opencollective.com/bootstrap/sponsor/6/website)
[![](https://opencollective.com/bootstrap/sponsor/7/avatar.svg)](https://opencollective.com/bootstrap/sponsor/7/website)
[![](https://opencollective.com/bootstrap/sponsor/8/avatar.svg)](https://opencollective.com/bootstrap/sponsor/8/website)
[![](https://opencollective.com/bootstrap/sponsor/9/avatar.svg)](https://opencollective.com/bootstrap/sponsor/9/website)


## Copyright and license

Code and documentation copyright 2011-2019 the [Bootstrap Authors](https://github.com/twbs/bootstrap/graphs/contributors) and [Twitter, Inc.](https://twitter.com) Code released under the [MIT License](https://github.com/twbs/bootstrap/blob/master/LICENSE). Docs released under [Creative Commons](https://creativecommons.org/licenses/by/3.0/).
```
# Inline
## _site_assets_js_vendor_clipboard_min_js

## _js_dist_dom_selector_engine_js
### Line 97-102
```
  };

  return SelectorEngine;

}));
//# sourceMappingURL=selector-engine.js.map

```

## _js_tests_unit_dom_data_spec_js

## _build_postcss_config_js

## _site_content_docs_4_3_examples_offcanvas_offcanvas_js

## _js_src_dropdown_js
### Line 113-122
```

    this._addEventListeners()
    Data.setData(element, DATA_KEY, this)
  }

  // Getters

  static get VERSION() {
    return VERSION
  }

```
### Line 127-136
```

  static get DefaultType() {
    return DefaultType
  }

  // Public

  toggle() {
    if (this._element.disabled || this._element.classList.contains(ClassName.DISABLED)) {
      return

```
### Line 161-170
```

    if (showEvent.defaultPrevented) {
      return
    }

    // Disable totally Popper.js for Dropdown in Navbar
    if (!this._inNavbar) {
      if (typeof Popper === 'undefined') {
        throw new TypeError('Bootstrap\'s dropdowns require Popper.js (https://popper.js.org)')
      }

```
### Line 174-202
```
      if (this._config.reference === 'parent') {
        referenceElement = parent
      } else if (isElement(this._config.reference)) {
        referenceElement = this._config.reference

        // Check if it's jQuery element
        if (typeof this._config.reference.jquery !== 'undefined') {
          referenceElement = this._config.reference[0]
        }
      }

      // If boundary is not `scrollParent`, then set position to `static`
      // to allow the menu to "escape" the scroll parent's boundaries
      // https://github.com/twbs/bootstrap/issues/24251
      if (this._config.boundary !== 'scrollParent') {
        parent.classList.add(ClassName.POSITION_STATIC)
      }

      this._popper = new Popper(referenceElement, this._menu, this._getPopperConfig())
    }

    // If this is a touch-enabled device we add extra
    // empty mouseover listeners to the body's immediate children;
    // only needed because of broken event delegation on iOS
    // https://www.quirksmode.org/blog/archives/2014/02/mouse_event_bub.html
    if ('ontouchstart' in document.documentElement &&
      !makeArray(SelectorEngine.closest(parent, Selector.NAVBAR_NAV)).length) {
      makeArray(document.body.children)
        .forEach(elem => EventHandler.on(elem, 'mouseover', null, noop()))

```
### Line 251-260
```
    if (this._popper) {
      this._popper.scheduleUpdate()
    }
  }

  // Private

  _addEventListeners() {
    EventHandler.on(this._element, Event.CLICK, event => {
      event.preventDefault()

```
### Line 287-296
```

  _getPlacement() {
    const parentDropdown = this._element.parentNode
    let placement = AttachmentMap.BOTTOM

    // Handle dropup
    if (parentDropdown.classList.contains(ClassName.DROPUP)) {
      placement = AttachmentMap.TOP
      if (this._menu.classList.contains(ClassName.MENURIGHT)) {
        placement = AttachmentMap.TOPEND

```
### Line 341-350
```
          boundariesElement: this._config.boundary
        }
      }
    }

    // Disable Popper.js if we have a static display
    if (this._config.display === 'static') {
      popperConfig.modifiers.applyStyle = {
        enabled: false
      }

```
### Line 354-363
```
      ...popperConfig,
      ...this._config.popperConfig
    }
  }

  // Static

  static dropdownInterface(element, config) {
    let data = Data.getData(element, DATA_KEY)
    const _config = typeof config === 'object' ? config : null

```
### Line 418-428
```
      const hideEvent = EventHandler.trigger(parent, Event.HIDE, relatedTarget)
      if (hideEvent.defaultPrevented) {
        continue
      }

      // If this is a touch-enabled device we remove the extra
      // empty mouseover listeners we added for iOS support
      if ('ontouchstart' in document.documentElement) {
        makeArray(document.body.children)
          .forEach(elem => EventHandler.off(elem, 'mouseover', null, noop()))
      }

```
### Line 442-457
```
  static getParentFromElement(element) {
    return getElementFromSelector(element) || element.parentNode
  }

  static dataApiKeydownHandler(event) {
    // If not input/textarea:
    //  - And not a key in REGEXP_KEYDOWN => not a dropdown command
    // If input/textarea:
    //  - If space key => not a dropdown command
    //  - If key is other than escape
    //    - If key is not up or down => not a dropdown command
    //    - If trigger inside the menu => not a dropdown command
    if (/input|textarea/i.test(event.target.tagName) ?
      event.which === SPACE_KEYCODE || (event.which !== ESCAPE_KEYCODE &&
      ((event.which !== ARROW_DOWN_KEYCODE && event.which !== ARROW_UP_KEYCODE) ||
        SelectorEngine.closest(event.target, Selector.MENU))) :

```

## _js_src_carousel_js
### Line 131-140
```

    this._addEventListeners()
    Data.setData(element, DATA_KEY, this)
  }

  // Getters

  static get VERSION() {
    return VERSION
  }

```
### Line 141-160
```

  static get Default() {
    return Default
  }

  // Public

  next() {
    if (!this._isSliding) {
      this._slide(Direction.NEXT)
    }
  }

  nextWhenVisible() {
    // Don't call next when the page isn't visible
    // or the carousel or its parent isn't visible
    if (!document.hidden && isVisible(this._element)) {
      this.next()
    }
  }

```
### Line 235-244
```
    this._isSliding = null
    this._activeElement = null
    this._indicatorsElement = null
  }

  // Private

  _getConfig(config) {
    config = {
      ...Default,

```
### Line 257-271
```

    const direction = absDeltax / this.touchDeltaX

    this.touchDeltaX = 0

    // swipe left
    if (direction > 0) {
      this.prev()
    }

    // swipe right
    if (direction < 0) {
      this.next()
    }
  }

```
### Line 296-305
```
        this.touchStartX = event.touches[0].clientX
      }
    }

    const move = event => {
      // ensure swiping with one touch and not pinching
      if (event.touches && event.touches.length > 1) {
        this.touchDeltaX = 0
      } else {
        this.touchDeltaX = event.touches[0].clientX - this.touchStartX

```
### Line 311-326
```
        this.touchDeltaX = event.clientX - this.touchStartX
      }

      this._handleSwipe()
      if (this._config.pause === 'hover') {
        // If it's a touch-enabled device, mouseenter/leave are fired as
        // part of the mouse compatibility events on first tap - the carousel
        // would stop cycling until user tapped out of it;
        // here, we listen for touchend, explicitly pause the carousel
        // (as if it's the second time we tap on it, mouseenter compat event
        // is NOT fired) and after a timeout (to allow for mouse compatibility
        // events to fire) we explicitly restart cycling

        this.pause()
        if (this.touchTimeout) {
          clearTimeout(this.touchTimeout)

```
### Line 453-462
```
    if (slideEvent.defaultPrevented) {
      return
    }

    if (!activeElement || !nextElement) {
      // Some weirdness is happening, so we bail
      return
    }

    this._isSliding = true

```
### Line 524-533
```
    if (isCycling) {
      this.cycle()
    }
  }

  // Static

  static carouselInterface(element, config) {
    let data = Data.getData(element, DATA_KEY)
    let _config = {

```

## _js_tests_unit_util_sanitizer_spec_js

## _build_change_version_js
### Line 1-5
```
#!/usr/bin/env node

/*!
 * Script to update version number references in the project.
 * Copyright 2017-2019 The Bootstrap Authors

```
### Line 13-22
```
const path = require('path')
const sh = require('shelljs')

sh.config.fatal = true

// Blame TC39... https://github.com/benjamingr/RegExp.escape/issues/37
function regExpQuote(string) {
  return string.replace(/[-\\^$*+?.()|[\]{}]/g, '\\$&')
}


```
### Line 93-102
```
    '_gh_pages',
    'node_modules',
    'vendor'
  ])
  const INCLUDED_EXTENSIONS = new Set([
    // This extension whitelist is how we avoid modifying binary files
    '',
    '.css',
    '.html',
    '.js',

```

## _js_src_button_js
### Line 52-67
```
  constructor(element) {
    this._element = element
    Data.setData(element, DATA_KEY, this)
  }

  // Getters

  static get VERSION() {
    return VERSION
  }

  // Public

  toggle() {
    let triggerChangeEvent = true
    let addAriaPressed = true

```
### Line 116-125
```
  dispose() {
    Data.removeData(this._element, DATA_KEY)
    this._element = null
  }

  // Static

  static jQueryInterface(config) {
    return this.each(function () {
      let data = Data.getData(this, DATA_KEY)

```

## _js_src_toast_js
### Line 72-81
```
    this._timeout = null
    this._setListeners()
    Data.setData(element, DATA_KEY, this)
  }

  // Getters

  static get VERSION() {
    return VERSION
  }

```
### Line 86-95
```

  static get Default() {
    return Default
  }

  // Public

  show() {
    const showEvent = EventHandler.trigger(this._element, Event.SHOW)


```
### Line 167-176
```

    this._element = null
    this._config = null
  }

  // Private

  _getConfig(config) {
    config = {
      ...Default,

```
### Line 194-203
```
      Selector.DATA_DISMISS,
      () => this.hide()
    )
  }

  // Static

  static jQueryInterface(config) {
    return this.each(function () {
      let data = Data.getData(this, DATA_KEY)

```

## _js_dist_collapse_js
### Line 288-297
```
    } // Getters


    var _proto = Collapse.prototype;

    // Public
    _proto.toggle = function toggle() {
      if (this._element.classList.contains(ClassName.SHOW)) {
        this.hide();
      } else {

```
### Line 481-490
```
      var _this3 = this;

      var parent = this._config.parent;

      if (isElement(parent)) {
        // it's a jQuery object
        if (typeof parent.jquery !== 'undefined' || typeof parent[0] !== 'undefined') {
          parent = parent[0];
        }
      } else {

```
### Line 571-580
```
   * ------------------------------------------------------------------------
   */


  EventHandler.on(document, Event.CLICK_DATA_API, Selector.DATA_TOGGLE, function (event) {
    // preventDefault only for <a> elements (which change the URL) not inside the collapsible element
    if (event.target.tagName === 'A') {
      event.preventDefault();
    }


```
### Line 584-593
```
    selectorElements.forEach(function (element) {
      var data = Data.getData(element, DATA_KEY);
      var config;

      if (data) {
        // update parent attribute
        if (data._parent === null && typeof triggerData.parent === 'string') {
          data._config.parent = triggerData.parent;
          data._parent = data._getParent();
        }

```
### Line 622-627
```
  }

  return Collapse;

}));
//# sourceMappingURL=collapse.js.map

```

## _babelrc_js

## _js_tests_unit_toast_spec_js

## _js_dist_alert_js
### Line 154-163
```
    } // Getters


    var _proto = Alert.prototype;

    // Public
    _proto.close = function close(element) {
      var rootElement = this._element;

      if (element) {

```
### Line 287-292
```
  }

  return Alert;

}));
//# sourceMappingURL=alert.js.map

```

## _js_dist_modal_js
### Line 283-292
```
    } // Getters


    var _proto = Modal.prototype;

    // Public
    _proto.toggle = function toggle(relatedTarget) {
      return this._isShown ? this.hide() : this.show(relatedTarget);
    };


```
### Line 424-433
```
      var transition = this._element.classList.contains(ClassName.FADE);

      var modalBody = SelectorEngine.findOne(Selector.MODAL_BODY, this._dialog);

      if (!this._element.parentNode || this._element.parentNode.nodeType !== Node.ELEMENT_NODE) {
        // Don't move modal's DOM position
        document.body.appendChild(this._element);
      }

      this._element.style.display = 'block';

```
### Line 604-614
```
        }
      } else {
        callback();
      }
    } // ----------------------------------------------------------------------
    // the following methods are used to handle overflowing modals
    // ----------------------------------------------------------------------
    ;

    _proto._adjustDialog = function _adjustDialog() {
      var isModalOverflowing = this._element.scrollHeight > document.documentElement.clientHeight;

```
### Line 635-646
```

    _proto._setScrollbar = function _setScrollbar() {
      var _this9 = this;

      if (this._isBodyOverflowing) {
        // Note: DOMNode.style.paddingRight returns the actual value or '' if not set
        //   while $(DOMNode).css('padding-right') returns the calculated value or 0 if not set
        // Adjust fixed content padding
        makeArray(SelectorEngine.find(Selector.FIXED_CONTENT)).forEach(function (element) {
          var actualPadding = element.style.paddingRight;
          var calculatedPadding = window.getComputedStyle(element)['padding-right'];
          Manipulator.setDataAttribute(element, 'padding-right', actualPadding);

```
### Line 662-671
```

      document.body.classList.add(ClassName.OPEN);
    };

    _proto._resetScrollbar = function _resetScrollbar() {
      // Restore fixed content padding
      makeArray(SelectorEngine.find(Selector.FIXED_CONTENT)).forEach(function (element) {
        var padding = Manipulator.getDataAttribute(element, 'padding-right');

        if (typeof padding !== 'undefined') {

```
### Line 692-701
```
        document.body.style.paddingRight = padding;
      }
    };

    _proto._getScrollbarWidth = function _getScrollbarWidth() {
      // thx d.walsh
      var scrollDiv = document.createElement('div');
      scrollDiv.className = ClassName.SCROLLBAR_MEASURER;
      document.body.appendChild(scrollDiv);
      var scrollbarWidth = scrollDiv.getBoundingClientRect().width - scrollDiv.clientWidth;

```
### Line 760-769
```
      event.preventDefault();
    }

    EventHandler.one(target, Event.SHOW, function (showEvent) {
      if (showEvent.defaultPrevented) {
        // only register focus restorer if modal will actually get shown
        return;
      }

      EventHandler.one(target, Event.HIDDEN, function () {

```
### Line 804-809
```
  }

  return Modal;

}));
//# sourceMappingURL=modal.js.map

```

## _site_content_docs_4_3_examples_checkout_form_validation_js
### Line 1-12
```
// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {

```

## _js_src_tooltip_js
### Line 133-158
```
  constructor(element, config) {
    if (typeof Popper === 'undefined') {
      throw new TypeError('Bootstrap\'s tooltips require Popper.js (https://popper.js.org)')
    }

    // private
    this._isEnabled = true
    this._timeout = 0
    this._hoverState = ''
    this._activeTrigger = {}
    this._popper = null

    // Protected
    this.element = element
    this.config = this._getConfig(config)
    this.tip = null

    this._setListeners()
    Data.setData(element, this.constructor.DATA_KEY, this)
  }

  // Getters

  static get VERSION() {
    return VERSION
  }

```
### Line 179-188
```

  static get DefaultType() {
    return DefaultType
  }

  // Public

  enable() {
    this._isEnabled = true
  }

```
### Line 301-313
```

      this._popper = new Popper(this.element, tip, this._getPopperConfig(attachment))

      tip.classList.add(ClassName.SHOW)

      // If this is a touch-enabled device we add extra
      // empty mouseover listeners to the body's immediate children;
      // only needed because of broken event delegation on iOS
      // https://www.quirksmode.org/blog/archives/2014/02/mouse_event_bub.html
      if ('ontouchstart' in document.documentElement) {
        makeArray(document.body.children).forEach(element => {
          EventHandler.on(element, 'mouseover', noop())
        })

```
### Line 356-366
```
      return
    }

    tip.classList.remove(ClassName.SHOW)

    // If this is a touch-enabled device we remove the extra
    // empty mouseover listeners we added for iOS support
    if ('ontouchstart' in document.documentElement) {
      makeArray(document.body.children)
        .forEach(element => EventHandler.off(element, 'mouseover', noop))
    }

```
### Line 385-394
```
    if (this._popper !== null) {
      this._popper.scheduleUpdate()
    }
  }

  // Protected

  isWithContent() {
    return Boolean(this.getTitle())
  }

```
### Line 420-429
```
    if (typeof content === 'object' && isElement(content)) {
      if (content.jquery) {
        content = content[0]
      }

      // content is a DOM node or a jQuery
      if (this.config.html) {
        if (content.parentNode !== element) {
          element.innerHTML = ''
          element.appendChild(content)

```
### Line 456-465
```
    }

    return title
  }

  // Private

  _getPopperConfig(attachment) {
    const defaultBsConfig = {
      placement: attachment,

```
### Line 773-782
```
    this.hide()
    this.show()
    this.config.animation = initConfigAnimation
  }

  // Static

  static jQueryInterface(config) {
    return this.each(function () {
      let data = Data.getData(this, DATA_KEY)

```

## _js_src_util_index_js
### Line 7-16
```

const MAX_UID = 1000000
const MILLISECONDS_MULTIPLIER = 1000
const TRANSITION_END = 'transitionend'

// Shoutout AngusCroll (https://goo.gl/pxwQGp)
const toType = obj => ({}.toString.call(obj).match(/\s([a-z]+)/i)[1].toLowerCase())

/**
 * --------------------------------------------------------------------------

```
### Line 57-80
```
const getTransitionDurationFromElement = element => {
  if (!element) {
    return 0
  }

  // Get transition-duration of the element
  let {
    transitionDuration,
    transitionDelay
  } = window.getComputedStyle(element)

  const floatTransitionDuration = parseFloat(transitionDuration)
  const floatTransitionDelay = parseFloat(transitionDelay)

  // Return 0 if element or transition duration is not found
  if (!floatTransitionDuration && !floatTransitionDelay) {
    return 0
  }

  // If multiple durations are defined, take the first
  transitionDuration = transitionDuration.split(',')[0]
  transitionDelay = transitionDelay.split(',')[0]

  return (parseFloat(transitionDuration) + parseFloat(transitionDelay)) * MILLISECONDS_MULTIPLIER

```
### Line 152-161
```
const findShadowRoot = element => {
  if (!document.documentElement.attachShadow) {
    return null
  }

  // Can find the shadow root otherwise it'll return the document
  if (typeof element.getRootNode === 'function') {
    const root = element.getRootNode()
    return root instanceof ShadowRoot ? root : null
  }

```
### Line 162-171
```

  if (element instanceof ShadowRoot) {
    return element
  }

  // when we don't find a shadow root
  if (!element.parentNode) {
    return null
  }


```

## _js_src_scrollspy_js
### Line 92-101
```
    this._process()

    Data.setData(element, DATA_KEY, this)
  }

  // Getters

  static get VERSION() {
    return VERSION
  }

```
### Line 102-111
```

  static get Default() {
    return Default
  }

  // Public

  refresh() {
    const autoMethod = this._scrollElement === this._scrollElement.window ?
      OffsetMethod.OFFSET :

```
### Line 167-176
```
    this._targets = null
    this._activeTarget = null
    this._scrollHeight = null
  }

  // Private

  _getConfig(config) {
    config = {
      ...Default,

```
### Line 266-286
```
        .findOne(Selector.DROPDOWN_TOGGLE, SelectorEngine.closest(link, Selector.DROPDOWN))
        .classList.add(ClassName.ACTIVE)

      link.classList.add(ClassName.ACTIVE)
    } else {
      // Set triggered link as active
      link.classList.add(ClassName.ACTIVE)

      SelectorEngine
        .parents(link, Selector.NAV_LIST_GROUP)
        .forEach(listGroup => {
          // Set triggered links parents as active
          // With both <ul> and <nav> markup a parent is the previous sibling of any nav ancestor
          SelectorEngine.prev(listGroup, `${Selector.NAV_LINKS}, ${Selector.LIST_ITEMS}`)
            .forEach(item => item.classList.add(ClassName.ACTIVE))

          // Handle special case when .nav-link is inside .nav-item
          SelectorEngine.prev(listGroup, Selector.NAV_ITEMS)
            .forEach(navItem => {
              SelectorEngine.children(navItem, Selector.NAV_LINKS)
                .forEach(item => item.classList.add(ClassName.ACTIVE))

```
### Line 297-306
```
    makeArray(SelectorEngine.find(this._selector))
      .filter(node => node.classList.contains(ClassName.ACTIVE))
      .forEach(node => node.classList.remove(ClassName.ACTIVE))
  }

  // Static

  static jQueryInterface(config) {
    return this.each(function () {
      let data = Data.getData(this, DATA_KEY)

```

# Issues
## 2311
Title:
```

        forms margin
      
```
Author:
```
rikius
```
Text:
```

There is different viewing in Firefox 10.0.2 and Chrome 17.0.963.56 m. In Firefox there are more space then in Chrome, Chrome do not have at all space HTML elements are:  between fieldset  label and item with div class="control-group"
I am using Bootstrap 2.0.1 version.

```
Author:
```
mainerror
```
Text:
```

Could you provide a screenshot showing the difference?

```
Author:
```
rikius
```
Text:
```

Firefox :

Chrome:

also providing the source code of that.
<form class="form-horizontal" id="order-form" action="">        
    <fieldset>
        <legend>Order</legend>
        <div class="control-group">
            <label class="control-label required" for="Order_status">Status <span class="required">*</span></label>
            <div class="controls">
                <select class="span5" name="Order[status]" id="Order_status">
                    <option value=""></option>
                    <option value="200">New</option>
                    <option value="150">Confirmed</option>
                    <option value="100">Sent</option>
                    <option value="1" selected="selected">Canceled</option>
                </select><span class="help-inline" id="Order_status_em_" style="display: none"></span>
            </div>
        </div>            
        <div class="control-group">
            <label class="control-label" for="Order_create_time">Create Time</label>
            <div class="controls">
                <input class="span5" disabled="disabled" name="Order[create_time]" id="Order_create_time" type="text" value="2012-03-02 16:54:04" /><span class="help-inline" id="Order_create_time_em_" style="display: none"></span>
            </div>
        </div>            
        <div class="control-group">
            <label class="control-label" for="Order_product_code">Product Code</label>
            <div class="controls">
                <input class="span5" maxlength="20" disabled="disabled" name="Order[product_code]" id="Order_product_code" type="text" value="PRWJ16O26F1KTFV" /><span class="help-inline" id="Order_product_code_em_" style="display: none"></span>
            </div>
        </div>            
        <div class="control-group">
            <label class="control-label" for="Order_product_title">Product Title</label>
            <div class="controls">
                <input class="span5" maxlength="60" disabled="disabled" name="Order[product_title]" id="Order_product_title" type="text" value="asdfasdf" /><span class="help-inline" id="Order_product_title_em_" style="display: none"></span>
            </div>
        </div>            
        <div class="control-group">
            <label class="control-label" for="Order_product_price">Product Price</label>
            <div class="controls">
                <input class="span5" disabled="disabled" name="Order[product_price]" id="Order_product_price" type="text" value="33.00" /><span class="help-inline" id="Order_product_price_em_" style="display: none"></span>
            </div>
        </div>        
    </fieldset>

    <div class="form-actions">
        <button class="btn btn-primary" type="submit" name="yt0"><i class="icon-ok icon-white"></i> Save</button>            
        <button class="btn" type="reset" name="yt1"><i class="icon-ban-circle"></i> Reset</button>        
    </div>
</form>


```
Author:
```
rikius
```
Text:
```

Same is in bootstrap Demo forms section "Horizontal forms".

```
Author:
```
mainerror
```
Text:
```

It seems like the images are not available. It would be nice if you could fix that. Try uploading them to http://imgur.com

```
Author:
```
rikius
```
Text:
```

updated.

```
Author:
```
mainerror
```
Text:
```

This seems to be bug in Webkit. Apparently it ignores the margin rules on legend elements when they are declared inside of a fieldset.
Here is a fiddle demonstrating that it has nothing to do with Bootstrap. This is an example of a legend element abiding by the margin rules which is improperly used without a fieldset element.

```
Author:
```
mdo
```
Text:
```

Yup, there is another issue related to this we closed awhile back. There's not too much we can do about it unfortunately :. We'll readdress in the future if at all possible.

```

## 2358
Title:
```

        Carousel Cycle as standard
      
```
Author:
```
ShaneSheppard
```
Text:
```

Is it possible you guys could make the carousel.js cycle as standard? By adding a div class for those who only want the one slide cycle?

```
Author:
```
fat
```
Text:
```

the single cycle is a bug in 2.0.1 and will be fixed with the release of 2.0.2 (hopefully this week)

```
Author:
```
tommls
```
Text:
```

Thank you!! I thought it was me!! :)

```

## 22201
Title:
```

        Cover not working with bootstrap-theme.min.css
      
```
Author:
```
typical-h
```
Text:
```

Cover is not working with bootstrap-theme.min.css I am using Chrome, with Windows.

```
Author:
```
patrickhlauke
```
Text:
```

as per https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md#using-the-issue-tracker please provide a reduced test case showing the problem.

```
Author:
```
mdo
```
Text:
```

Also, theme file is for v3, which we're not actively working on right now. Tagging and closing.

```

## 23190
Title:
```

        $input-height-inner-lg is using $font-size-sm instead of $font-size-lg
      
```
Author:
```
envolute
```
Text:
```

This:
$input-height-inner-lg: ($font-size-sm * $input-btn-line-height-lg) + ($input-btn-padding-y-lg * 2) !default;
Must be like this:
$input-height-inner-lg: ($font-size-lg * $input-btn-line-height-lg) + ($input-btn-padding-y-lg * 2) !default;
ok??

```
Author:
```
envolute
```
Text:
```

Sorry, duplicate of #23150

```

## 12856
Title:
```

        docs navbar should be fixed-to-top
      
```
Author:
```
tkojemile
```
Text:
```

INFO: this is related to getbootstrap.com main site
Please make top menu fixed.
I belive that many people use it as reference and read styling, components and other there, so when you need fast swwitch you need to scroll to top of page for change :)
NHF :) 👍

```
Author:
```
cvrebert
```
Text:
```

Duplicate of #12626.

```

## 25131
Title:
```

        No Hand Cursor in button Boostrap 4 beta 3
      
```
Author:
```
hamzahamidi
```
Text:
```


Operating system : Ubuntu 16.4
Browser: Chrome 63, Firefox 58
Bootstrap 4 beta 3

I don't get the "hand" cursor when pointing on a button.

Here's the code: <button type="button" class="btn btn-primary">Primary</button>
And here's a bootsnipp to confirm that. Take a look please at the add user button.
But in the official bootstrap beta 3 website it's working fine I see the hand cursor.
https://getbootstrap.com/docs/4.0/components/buttons/

```
Author:
```
browner12
```
Text:
```

looks like they are still using the beta 2. give them a little time to update, services like this don't update immediately after release

```
Author:
```
mdo
```
Text:
```

Yup, closing per @browner12.

```

## 24517
Title:
```

        Horizontal rule hard-coded margin introduced in Beta
      
```
Author:
```
ernestbofill
```
Text:
```

Since the beta version of Bootstrap, the margin of the horizontal rule defined in _type.scss is a hard-coded making it difficult to customize.
In latest alpha:
// type.scss line 53:
hr {
  margin-top: $spacer-y;
  margin-bottom: $spacer-y;
  //...
}

In beta:
// type.scss line 53:
hr {
  margin-top: 1rem;
  margin-bottom: 1rem;
  //...
}

I would like this margin to use a variable so that it can be customized.

```
Author:
```
andresgalante
```
Text:
```

Hi @ernestbofill it was updated here: ed1de86
I'll create a PR to add hr variables.

```

## 22583
Title:
```

        npm ls
      
```
Author:
```
beninflash
```
Text:
```

Before opening an issue:

Search for duplicate or closed issues
Validate and lint any HTML to avoid common problems
Prepare a reduced test case for any bugs
Read the contributing guidelines

When asking general "how to" questions:

Please do not open an issue here
Instead, ask for help on StackOverflow, IRC, or Slack

When reporting a bug, include:

Operating system and version (Windows, Mac OS X, Android, iOS, Win10 Mobile)
Browser and version (Chrome, Firefox, Safari, IE, MS Edge, Opera 15+, Android Browser)
Reduced test cases and potential fixes using JS Bin

When suggesting a feature, include:

As much detail as possible for what we should add and why it's important to Bootstrap
Relevant links to prior art, screenshots, or live demos whenever possible


```

## 4853
Title:
```

        LESS Error
      
```
Author:
```
arturgrigor
```
Text:
```

{"type":"Parse","message":"Syntax Error on line 278","index":8378,"filename":"bootstrap.css","line":278,"column":0,"extract":["@fluidGridGutterWidth768:      percentage(@gridGutterWidth768/@gridRowWidth768);","@iconSpritePath: ../../images/libs/bootstrapjs/glyphicons-halflings.png;","@iconWhiteSpritePath: ../../images/libs/bootstrapjs/glyphicons-halflings-white.png;"]}

```
Author:
```
Yohn
```
Text:
```

I had that happen to me when I downloaded the docs and tried to build my own through the customize page..  It doesnt do that on the twitter.github.com/bootstrap customize page though

```
Author:
```
mdo
```
Text:
```

Check syntax and try again. Also be sure to use only the hosted version of the builder—no guarantees on the local version.

```

## 14929
Title:
```

        Bootstrap CDN returning XML error
      
```
Author:
```
georgesebastian
```
Text:
```

The links for the latest bootstrap v3.3.0 as provided on the Twitter Bootstrap page (http://getbootstrap.com/getting-started/#download) are not working. Instead I get an Access Denied error.
https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css
https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap-theme.min.css
https://netdna.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js
Attaching the screenshots below :




```
Author:
```
hnrch02
```
Text:
```

Unfortunately Bootstrap CDN hasn't been updated yet. Please use jsDelivr in the meantime:
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/bootstrap/3.3.0/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/bootstrap/3.3.0/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://cdn.jsdelivr.net/bootstrap/3.3.0/js/bootstrap.min.js"></script>

```
Author:
```
georgesebastian
```
Text:
```

I have filed an issue with the Bootstrap CDN github repo. Thank you for the jsDelivr links.

```
Author:
```
cvrebert
```
Text:
```

X-Ref: MaxCDN/bootstrapcdn#401

```

## 4770
Title:
```

        affix usability issue when sidebar's height highter available height
      
```
Author:
```
jycr
```
Text:
```

if the height of sidebar is greater than the available height of the window, it is impossible to see and reach last items.
You can see this problem with 800x600 resolution and the URL http://twitter.github.com/bootstrap/javascript.html#affix
A possible usability solution can be find on this page : https://www.bforbank.com/membre/souscription/livretWebFlow.action
(buggy on Chrome, but work perfectly on firefox 14)

```
Author:
```
mdo
```
Text:
```

Yeah, there's nothing we can do about that. Use good judgement for what you're affixing and you'll be fine.

```

## 524
Title:
```

        bootstrap-tabs.js should provide .activate function.
      
```
Author:
```
wildchild
```
Text:
```

Would be useful to activate desired tab using javascript.

```
Author:
```
fat
```
Text:
```

just trigger click on the tab you want to activate... $('#myTab').click()

```

# Pull
## 29562
Title:
```

        Update hugo-bin to v0.47.0 (Hugo 0.59.0)
      
```
Author:
```
XhmikosR
```
Text:
```


No description provided.


```

## 27614
Title:
```

        Docs: Improve accessibility of disabled link example
      
```
Author:
```
ysds
```
Text:
```

Add tabindex="-1" and aria-disabled="true" to each disabled link.

```

## 28989
Title:
```

        Remove text align from body
      
```
Author:
```
MartijnCuppens
```
Text:
```

This was causing issues for RTL, see #28238.
The text align didn't needed to be set to fix (#22858), adding th{ text-align: inherit; } was enough (see https://codepen.io/MartijnCuppens/pen/zVLZbG)
Fixes #28238

```
Author:
```
ysds
```
Text:
```

looks good, but I'm not sure this can be safely backported to v4.

```
Author:
```
MartijnCuppens
```
Text:
```


I'm not sure this can be safely backported to v4.

It could start aligning things to the right in rtl-layouts indeed, maybe we should only apply it to v5, just to be sure?

```
Author:
```
XhmikosR
```
Text:
```

Maybe this should be configurable and not set in reboot?

```
Author:
```
MartijnCuppens
```
Text:
```


Maybe this should be configurable

Done

and not set in reboot?

We already set other font related things in the body, so I guess that's the right spot.

```
Author:
```
XhmikosR
```
Text:
```

Yeah, but since reboot can be used standalone, you know.

```

## 10386
Title:
```

        Added ability to specify buttons text hover-color in variables.less
      
```
Author:
```
nathan-muir
```
Text:
```


No description provided.


```
Author:
```
mdo
```
Text:
```

The slightly annoying part about this is that it adds the same color declaration to every button. I understand the benefit, but I think I prefer the consolidation.

```

## 28094
Title:
```

        Update devDependencies and gems.
      
```
Author:
```
XhmikosR
```
Text:
```


No description provided.


```

## 10423
Title:
```

        CSS docs - Grid section: two dots are missing before 'col-md-8'
      
```
Author:
```
hustlzp
```
Text:
```

Add the two missing docs

```
Author:
```
juthilo
```
Text:
```

@hustlzp: Hi! Do you give your permission to change Bootstrap's license to the MIT license? You can simply reply here on this thread (or by replying to the notification email you might be getting). Thanks in advance for saving us a lot of work!

```
Author:
```
hustlzp
```
Text:
```

@juthilo Year!

```

## 17625
Title:
```

        Documentation clean up and consistency.
      
```
Author:
```
bhamodi
```
Text:
```

@mdo - just some general clean up of your .md files. 👍

```
Author:
```
bhamodi
```
Text:
```

Addressed your feedback @cvrebert.

```
Author:
```
bhamodi
```
Text:
```

Ping @cvrebert and @mdo, any update on this?

```
Author:
```
cvrebert
```
Text:
```

Merged with a couple tweaks. Thanks!

```

