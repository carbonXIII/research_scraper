# twbs/bootstrap
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_site_content_docs_4_3_components_pagination_md](#_site_content_docs_4_3_components_pagination_md)

* [_site_content_docs_4_3_components_navbar_md](#_site_content_docs_4_3_components_navbar_md)

* [_site_content_docs_4_3_helpers_text_truncation_md](#_site_content_docs_4_3_helpers_text_truncation_md)

* [_site_layouts_partials_callout_info_mediaqueries_breakpoints_md](#_site_layouts_partials_callout_info_mediaqueries_breakpoints_md)

* [_github_ISSUE_TEMPLATE_bug_report_md](#_github_ISSUE_TEMPLATE_bug_report_md)

* [_site_content_docs_4_3_helpers_position_md](#_site_content_docs_4_3_helpers_position_md)

* [_site_content_docs_4_3_components_icons_md](#_site_content_docs_4_3_components_icons_md)

* [_site_content_docs_4_3_components_carousel_md](#_site_content_docs_4_3_components_carousel_md)

* [_site_content_docs_4_3_forms_layout_md](#_site_content_docs_4_3_forms_layout_md)

* [_site_content_docs_4_3_components_badge_md](#_site_content_docs_4_3_components_badge_md)

* [_site_content_docs_4_3_components_tooltips_md](#_site_content_docs_4_3_components_tooltips_md)

* [_site_content_docs_4_3_components_toasts_md](#_site_content_docs_4_3_components_toasts_md)

* [_site_content_docs_4_3_utilities_position_md](#_site_content_docs_4_3_utilities_position_md)

* [_site_content_docs_4_3_utilities_sizing_md](#_site_content_docs_4_3_utilities_sizing_md)

* [_site_layouts_partials_callout_danger_async_methods_md](#_site_layouts_partials_callout_danger_async_methods_md)

* [_site_content_docs_4_3_utilities_display_md](#_site_content_docs_4_3_utilities_display_md)

* [_site_content_docs_4_3_components_progress_md](#_site_content_docs_4_3_components_progress_md)

* [_site_content_docs_4_3_about_brand_md](#_site_content_docs_4_3_about_brand_md)

* [_site_content_docs_4_3_helpers_stretched_link_md](#_site_content_docs_4_3_helpers_stretched_link_md)

* [_site_content_docs_4_3_forms_file_md](#_site_content_docs_4_3_forms_file_md)

[- Inline](#Inline)

* [_js_dist_dom_data_js](#_js_dist_dom_data_js)

* [_build_build_plugins_js](#_build_build_plugins_js)

* [_package_js](#_package_js)

* [_js_dist_dom_selector_engine_js](#_js_dist_dom_selector_engine_js)

* [_js_src_dom_event_handler_js](#_js_src_dom_event_handler_js)

* [_dist_js_bootstrap_esm_js](#_dist_js_bootstrap_esm_js)

* [_js_src_dom_selector_engine_js](#_js_src_dom_selector_engine_js)

* [_js_src_button_js](#_js_src_button_js)

* [_js_tests_browsers_js](#_js_tests_browsers_js)

* [_js_dist_tab_js](#_js_dist_tab_js)

* [_js_dist_modal_js](#_js_dist_modal_js)

* [_js_src_tooltip_js](#_js_src_tooltip_js)

* [_js_dist_dom_manipulator_js](#_js_dist_dom_manipulator_js)

* [_js_src_toast_js](#_js_src_toast_js)

* [_js_tests_integration_bundle_js](#_js_tests_integration_bundle_js)

* [_js_src_tab_js](#_js_src_tab_js)

* [_js_src_dropdown_js](#_js_src_dropdown_js)

* [_dist_js_bootstrap_bundle_js](#_dist_js_bootstrap_bundle_js)

* [_js_tests_helpers_fixture_js](#_js_tests_helpers_fixture_js)

* [_site_content_docs_4_3_examples_checkout_form_validation_js](#_site_content_docs_4_3_examples_checkout_form_validation_js)

[- Issues](#Issues)

* [25110](#25110)

* [21851](#21851)

* [5035](#5035)

* [26506](#26506)

* [23545](#23545)

* [17784](#17784)

* [15963](#15963)

* [8496](#8496)

* [9348](#9348)

* [29204](#29204)

* [26711](#26711)

* [17943](#17943)

* [18790](#18790)

[- Pull](#Pull)

* [12909](#12909)

* [22401](#22401)

* [13095](#13095)

* [25123](#25123)

* [17689](#17689)

* [3073](#3073)

* [18463](#18463)

<!-- toc -->

# Info
## description
The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web.

# Markdown
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
## _site_content_docs_4_3_components_navbar_md
```---
layout: docs
title: Navbar
description: Documentation and examples for Bootstrap's powerful, responsive navigation header, the navbar. Includes support for branding, navigation, and more, including support for our collapse plugin.
group: components
toc: true
---

## How it works

Here's what you need to know before getting started with the navbar:

- Navbars require a wrapping `.navbar` with `.navbar-expand{-sm|-md|-lg|-xl}` for responsive collapsing and [color scheme](#color-schemes) classes.
- Navbars and their contents are fluid by default. Use [optional containers](#containers) to limit their horizontal width.
- Use our [spacing]({{< docsref "/utilities/spacing" >}}) and [flex]({{< docsref "/utilities/flex" >}}) utility classes for controlling spacing and alignment within navbars.
- Navbars are responsive by default, but you can easily modify them to change that. Responsive behavior depends on our Collapse JavaScript plugin.
- Ensure accessibility by using a `<nav>` element or, if using a more generic element such as a `<div>`, add a `role="navigation"` to every navbar to explicitly identify it as a landmark region for users of assistive technologies.

{{< callout info >}}
{{< partial "callout-info-prefersreducedmotion.md" >}}
{{< /callout >}}

Read on for an example and list of supported sub-components.

## Supported content

Navbars come with built-in support for a handful of sub-components. Choose from the following as needed:

- `.navbar-brand` for your company, product, or project name.
- `.navbar-nav` for a full-height and lightweight navigation (including support for dropdowns).
- `.navbar-toggler` for use with our collapse plugin and other [navigation toggling](#responsive-behaviors) behaviors.
- `.form-inline` for any form controls and actions.
- `.navbar-text` for adding vertically centered strings of text.
- `.collapse.navbar-collapse` for grouping and hiding navbar contents by a parent breakpoint.

Here's an example of all the sub-components included in a responsive light-themed navbar that automatically collapses at the `lg` (large) breakpoint.

{{< example >}}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-expanded="false">
          Dropdown
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
          <li><hr class="dropdown-divider"></li>
          <li><a class="dropdown-item" href="#">Something else here</a></li>
        </ul>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
{{< /example >}}

This example uses [color]({{< docsref "/utilities/colors" >}}) (`bg-light`) and [spacing]({{< docsref "/utilities/spacing" >}}) (`my-2`, `my-lg-0`, `mr-sm-0`, `my-sm-0`) utility classes.

### Brand

The `.navbar-brand` can be applied to most elements, but an anchor works best as some elements might require utility classes or custom styles.

{{< example >}}
<!-- As a link -->
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
</nav>

<!-- As a heading -->
<nav class="navbar navbar-light bg-light">
  <span class="navbar-brand mb-0 h1">Navbar</span>
</nav>
{{< /example >}}

Adding images to the `.navbar-brand` will likely always require custom styles or utilities to properly size. Here are some examples to demonstrate.

{{< example >}}
<!-- Just an image -->
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">
    <img src="/docs/{{< param docs_version >}}/assets/brand/bootstrap-solid.svg" width="30" height="30" alt="">
  </a>
</nav>
{{< /example >}}

{{< example >}}
<!-- Image and text -->
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">
    <img src="/docs/{{< param docs_version >}}/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="">
    Bootstrap
  </a>
</nav>
{{< /example >}}

### Nav

Navbar navigation links build on our `.nav` options with their own modifier class and require the use of [toggler classes](#toggler) for proper responsive styling. **Navigation in navbars will also grow to occupy as much horizontal space as possible** to keep your navbar contents securely aligned.

Active states—with `.active`—to indicate the current page can be applied directly to `.nav-link`s or their immediate parent `.nav-item`s.

{{< example >}}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Features</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Pricing</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
  </div>
</nav>
{{< /example >}}

And because we use classes for our navs, you can avoid the list-based approach entirely if you like.

{{< example >}}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-item nav-link active" href="#">Home <span class="sr-only">(current)</span></a>
      <a class="nav-item nav-link" href="#">Features</a>
      <a class="nav-item nav-link" href="#">Pricing</a>
      <a class="nav-item nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
    </div>
  </div>
</nav>
{{< /example >}}

You may also utilize dropdowns in your navbar nav. Dropdown menus require a wrapping element for positioning, so be sure to use separate and nested elements for `.nav-item` and `.nav-link` as shown below.

{{< example >}}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavDropdown">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Features</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Pricing</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-expanded="false">
          Dropdown link
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
          <li><a class="dropdown-item" href="#">Something else here</a></li>
        </ul>
      </li>
    </ul>
  </div>
</nav>
{{< /example >}}

### Forms

Place various form controls and components within a navbar with `.form-inline`.

{{< example >}}
<nav class="navbar navbar-light bg-light">
  <form class="form-inline">
    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
  </form>
</nav>
{{< /example >}}

Immediate children elements in `.navbar` use flex layout and will default to `justify-content: between`. Use additional [flex utilities]({{< docsref "/utilities/flex" >}}) as needed to adjust this behavior.

{{< example >}}
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand">Navbar</a>
  <form class="form-inline">
    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
  </form>
</nav>
{{< /example >}}

Input groups work, too:

{{< example >}}
<nav class="navbar navbar-light bg-light">
  <form class="form-inline">
    <div class="input-group">
      <div class="input-group-prepend">
        <span class="input-group-text" id="basic-addon1">@</span>
      </div>
      <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
    </div>
  </form>
</nav>
{{< /example >}}

Various buttons are supported as part of these navbar forms, too. This is also a great reminder that vertical alignment utilities can be used to align different sized elements.

{{< example >}}
<nav class="navbar navbar-light bg-light">
  <form class="form-inline">
    <button class="btn btn-outline-success" type="button">Main button</button>
    <button class="btn btn-sm btn-outline-secondary" type="button">Smaller button</button>
  </form>
</nav>
{{< /example >}}

### Text

Navbars may contain bits of text with the help of `.navbar-text`. This class adjusts vertical alignment and horizontal spacing for strings of text.

{{< example >}}
<nav class="navbar navbar-light bg-light">
  <span class="navbar-text">
    Navbar text with an inline element
  </span>
</nav>
{{< /example >}}

Mix and match with other components and utilities as needed.

{{< example >}}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar w/ text</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarText">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Features</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Pricing</a>
      </li>
    </ul>
    <span class="navbar-text">
      Navbar text with an inline element
    </span>
  </div>
</nav>
{{< /example >}}

## Color schemes

Theming the navbar has never been easier thanks to the combination of theming classes and `background-color` utilities. Choose from `.navbar-light` for use with light background colors, or `.navbar-dark` for dark background colors. Then, customize with `.bg-*` utilities.

<div class="bd-example">
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarColor01">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">About</a>
        </li>
      </ul>
      <form class="form-inline">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-info my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>

  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarColor02">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">About</a>
        </li>
      </ul>
      <form class="form-inline">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>

  <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #e3f2fd;">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor03" aria-controls="navbarColor03" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarColor03">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">About</a>
        </li>
      </ul>
      <form class="form-inline">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-primary my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
</div>

{{< highlight html >}}
<nav class="navbar navbar-dark bg-dark">
  <!-- Navbar content -->
</nav>

<nav class="navbar navbar-dark bg-primary">
  <!-- Navbar content -->
</nav>

<nav class="navbar navbar-light" style="background-color: #e3f2fd;">
  <!-- Navbar content -->
</nav>
{{< /highlight >}}

## Containers

Although it's not required, you can wrap a navbar in a `.container` to center it on a page or add one within to only center the contents of a [fixed or static top navbar](#placement).

{{< example >}}
<div class="container">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Navbar</a>
  </nav>
</div>
{{< /example >}}

When the container is within your navbar, its horizontal padding is removed at breakpoints lower than your specified `.navbar-expand{-sm|-md|-lg|-xl}` class. This ensures we're not doubling up on padding unnecessarily on lower viewports when your navbar is collapsed.

{{< example >}}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
    <a class="navbar-brand" href="#">Navbar</a>
  </div>
</nav>
{{< /example >}}

## Placement

Use our [position utilities]({{< docsref "/utilities/position" >}}) to place navbars in non-static positions. Choose from fixed to the top, fixed to the bottom, or stickied to the top (scrolls with the page until it reaches the top, then stays there). Fixed navbars use `position: fixed`, meaning they're pulled from the normal flow of the DOM and may require custom CSS (e.g., `padding-top` on the `<body>`) to prevent overlap with other elements.

Also note that **`.sticky-top` uses `position: sticky`, which [isn't fully supported in every browser](https://caniuse.com/#feat=css-sticky)**.

{{< example >}}
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">Default</a>
</nav>
{{< /example >}}

{{< example >}}
<nav class="navbar fixed-top navbar-light bg-light">
  <a class="navbar-brand" href="#">Fixed top</a>
</nav>
{{< /example >}}

{{< example >}}
<nav class="navbar fixed-bottom navbar-light bg-light">
  <a class="navbar-brand" href="#">Fixed bottom</a>
</nav>
{{< /example >}}

{{< example >}}
<nav class="navbar sticky-top navbar-light bg-light">
  <a class="navbar-brand" href="#">Sticky top</a>
</nav>
{{< /example >}}

## Responsive behaviors

Navbars can utilize `.navbar-toggler`, `.navbar-collapse`, and `.navbar-expand{-sm|-md|-lg|-xl}` classes to change when their content collapses behind a button. In combination with other utilities, you can easily choose when to show or hide particular elements.

For navbars that never collapse, add the `.navbar-expand` class on the navbar. For navbars that always collapse, don't add any `.navbar-expand` class.

### Toggler

Navbar togglers are left-aligned by default, but should they follow a sibling element like a `.navbar-brand`, they'll automatically be aligned to the far right. Reversing your markup will reverse the placement of the toggler. Below are examples of different toggle styles.

With no `.navbar-brand` shown in lowest breakpoint:

{{< example >}}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
    <a class="navbar-brand" href="#">Hidden brand</a>
    <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
{{< /example >}}

With a brand name shown on the left and toggler on the right:

{{< example >}}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
    <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
{{< /example >}}

With a toggler on the left and brand name on the right:

{{< example >}}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <a class="navbar-brand" href="#">Navbar</a>

  <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
    <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
{{< /example >}}

### External content

Sometimes you want to use the collapse plugin to trigger hidden content elsewhere on the page. Because our plugin works on the `id` and `data-target` matching, that's easily done!

{{< example >}}
<div class="collapse" id="navbarToggleExternalContent">
  <div class="bg-dark p-4">
    <h5 class="text-white h4">Collapsed content</h5>
    <span class="text-muted">Toggleable via the navbar brand.</span>
  </div>
</div>
<nav class="navbar navbar-dark bg-dark">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
</nav>
{{< /example >}}
```
## _site_content_docs_4_3_helpers_text_truncation_md
```---
layout: docs
title: Text truncation
description: Truncate long strings of text with an ellipsis.
group: helpers
toc: false
---

For longer content, you can add a `.text-truncate` class to truncate the text with an ellipsis. **Requires `display: inline-block` or `display: block`.**

{{< example >}}
<!-- Block level -->
<div class="row">
  <div class="col-2 text-truncate">
    Praeterea iter est quasdam res quas ex communi.
  </div>
</div>

<!-- Inline level -->
<span class="d-inline-block text-truncate" style="max-width: 150px;">
  Praeterea iter est quasdam res quas ex communi.
</span>
{{< /example >}}
```
## _site_layouts_partials_callout_info_mediaqueries_breakpoints_md
```Note that since browsers do not currently support [range context queries](https://www.w3.org/TR/mediaqueries-4/#range-context), we work around the limitations of [`min-` and `max-` prefixes](https://www.w3.org/TR/mediaqueries-4/#mq-min-max) and viewports with fractional widths (which can occur under certain conditions on high-dpi devices, for instance) by using values with higher precision for these comparisons.
```
## _github_ISSUE_TEMPLATE_bug_report_md
```---
name: Bug report
about: Tell us about a bug you may have identified in Bootstrap.

---

Before opening:

- [Search for duplicate or closed issues](https://github.com/twbs/bootstrap/issues?utf8=%E2%9C%93&q=is%3Aissue)
- [Validate](https://html5.validator.nu/) and [lint](https://github.com/twbs/bootlint#in-the-browser) any HTML to avoid common problems
- Read the [contributing guidelines](https://github.com/twbs/bootstrap/blob/master/.github/CONTRIBUTING.md)

Bug reports must include:

- Operating system and version (Windows, macOS, Android, iOS, Win10 Mobile)
- Browser and version (Chrome, Firefox, Safari, IE, MS Edge, Opera 15+, Android Browser)
- [Reduced test case](https://css-tricks.com/reduced-test-cases/) and suggested fix using [CodePen](https://codepen.io/) or [JS Bin](https://jsbin.com/)
```
## _site_content_docs_4_3_helpers_position_md
```---
layout: docs
title: Position
description: Use these helpers for quickly configuring the position of an element.
group: helpers
toc: true
---

## Fixed top

Position an element at the top of the viewport, from edge to edge. Be sure you understand the ramifications of fixed position in your project; you may need to add additional CSS.

{{< highlight html >}}
<div class="fixed-top">...</div>
{{< /highlight >}}

## Fixed bottom

Position an element at the bottom of the viewport, from edge to edge. Be sure you understand the ramifications of fixed position in your project; you may need to add additional CSS.

{{< highlight html >}}
<div class="fixed-bottom">...</div>
{{< /highlight >}}

## Sticky top

Position an element at the top of the viewport, from edge to edge, but only after you scroll past it. The `.sticky-top` utility uses CSS's `position: sticky`, which isn't fully supported in all browsers.

**IE11 and IE10 will render `position: sticky` as `position: relative`.** As such, we wrap the styles in a `@supports` query, limiting the stickiness to only browsers that can render it properly.

{{< highlight html >}}
<div class="sticky-top">...</div>
{{< /highlight >}}

## Responsive sticky top

Responsive variations also exist for `.sticky-top` utility.

{{< highlight html >}}
<div class="sticky-sm-top">Stick to the top on viewports sized SM (small) or wider</div>
<div class="sticky-md-top">Stick to the top on viewports sized MD (medium) or wider</div>
<div class="sticky-lg-top">Stick to the top on viewports sized LG (large) or wider</div>
<div class="sticky-xl-top">Stick to the top on viewports sized XL (extra-large) or wider</div>
{{< /highlight >}}
```
## _site_content_docs_4_3_components_icons_md
```---
layout: docs
title: Icons
description: Custom icons for Bootstrap components.
group: components
toc: true
---

<div class="booticons-list">
<svg class="booticon booticon-chevron-left" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path stroke="currentColor" stroke-width="2" d="M11 2L5 8l6 6" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
<svg class="booticon booticon-chevron-right" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path stroke="currentColor" stroke-width="2" d="M5 14l6-6-6-6" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
<svg class="booticon booticon-chevron-up" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path stroke="currentColor" stroke-width="2" d="M2 11l6-6 6 6" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
<svg class="booticon booticon-chevron-down" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path stroke="currentColor" stroke-width="2" d="M2 5l6 6 6-6" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
<svg class="booticon booticon-chevron-condensed-left" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path stroke="currentColor" stroke-width="2" d="M9 2L6 8l3 6" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
<svg class="booticon booticon-chevron-condensed-right" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path stroke="currentColor" stroke-width="2" d="M7 14l3-6-3-6" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
<svg class="booticon booticon-check" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path stroke="currentColor" stroke-width="2" d="M4 8.5L6.5 11l6-6" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
<svg class="booticon booticon-x" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path d="M8 8l-3 3 3-3 3 3-3-3zm0 0l3-3-3 3-3-3 3 3z" stroke="currentColor" stroke-width="2" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
<svg class="booticon booticon-dash" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path d="M5 8h6" stroke="currentColor" stroke-width="2" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
<svg class="booticon booticon-circle" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path d="M8 14A6 6 0 1 0 8 2a6 6 0 0 0 0 12zm0-2a4 4 0 1 1 0-8 4 4 0 0 1 0 8z" fill="currentColor" fill-rule="nonzero"/></svg>
<svg class="booticon booticon-dot" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path d="M8 8v.082" stroke="currentColor" stroke-width="2" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
</div>
```
## _site_content_docs_4_3_components_carousel_md
```---
layout: docs
title: Carousel
description: A slideshow component for cycling through elements—images or slides of text—like a carousel.
group: components
toc: true
---

## How it works

The carousel is a slideshow for cycling through a series of content, built with CSS 3D transforms and a bit of JavaScript. It works with a series of images, text, or custom markup. It also includes support for previous/next controls and indicators.

In browsers where the [Page Visibility API](https://www.w3.org/TR/page-visibility/) is supported, the carousel will avoid sliding when the webpage is not visible to the user (such as when the browser tab is inactive, the browser window is minimized, etc.).

{{< callout info >}}
{{< partial "callout-info-prefersreducedmotion.md" >}}
{{< /callout >}}

Please be aware that nested carousels are not supported, and carousels are generally not compliant with accessibility standards.

## Example

Carousels don't automatically normalize slide dimensions. As such, you may need to use additional utilities or custom styles to appropriately size content. While carousels support previous/next controls and indicators, they're not explicitly required. Add and customize as you see fit.

**The `.active` class needs to be added to one of the slides** otherwise the carousel will not be visible. Also be sure to set a unique id on the `.carousel` for optional controls, especially if you're using multiple carousels on a single page. Control and indicator elements must have a `data-target` attribute (or `href` for links) that matches the id of the `.carousel` element.

### Slides only

Here's a carousel with slides only. Note the presence of the `.d-block` and `.w-100` on carousel images to prevent browser default image alignment.

{{< example >}}
<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#555" background="#777" text="First slide" >}}
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#444" background="#666" text="Second slide" >}}
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#333" background="#555" text="Third slide" >}}
    </div>
  </div>
</div>
{{< /example >}}

### With controls

Adding in the previous and next controls:

{{< example >}}
<div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#555" background="#777" text="First slide" >}}
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#444" background="#666" text="Second slide" >}}
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#333" background="#555" text="Third slide" >}}
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
{{< /example >}}

### With indicators

You can also add the indicators to the carousel, alongside the controls, too.

{{< example >}}
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#555" background="#777" text="First slide" >}}
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#444" background="#666" text="Second slide" >}}
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#333" background="#555" text="Third slide" >}}
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
{{< /example >}}

### With captions

Add captions to your slides easily with the `.carousel-caption` element within any `.carousel-item`. They can be easily hidden on smaller viewports, as shown below, with optional [display utilities]({{< docsref "/utilities/display" >}}). We hide them initially with `.d-none` and bring them back on medium-sized devices with `.d-md-block`.

{{< example >}}
<div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleCaptions" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleCaptions" data-slide-to="1"></li>
    <li data-target="#carouselExampleCaptions" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#555" background="#777" text="First slide" >}}
      <div class="carousel-caption d-none d-md-block">
        <h5>First slide label</h5>
        <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
      </div>
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#444" background="#666" text="Second slide" >}}
      <div class="carousel-caption d-none d-md-block">
        <h5>Second slide label</h5>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      </div>
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#333" background="#555" text="Third slide" >}}
      <div class="carousel-caption d-none d-md-block">
        <h5>Third slide label</h5>
        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
      </div>
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
{{< /example >}}

### Crossfade

Add `.carousel-fade` to your carousel to animate slides with a fade transition instead of a slide.

{{< example >}}
<div id="carouselExampleFade" class="carousel slide carousel-fade" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#555" background="#777" text="First slide" >}}
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#444" background="#666" text="Second slide" >}}
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#333" background="#555" text="Third slide" >}}
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleFade" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleFade" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
{{< /example >}}

### Individual `.carousel-item` interval

Add `data-interval=""` to a `.carousel-item` to change the amount of time to delay between automatically cycling to the next item.

{{< example >}}
<div id="carouselExampleInterval" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active" data-interval="10000">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#555" background="#777" text="First slide" >}}
    </div>
    <div class="carousel-item" data-interval="2000">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#444" background="#666" text="Second slide" >}}
    </div>
    <div class="carousel-item">
      {{< placeholder width="800" height="400" class="bd-placeholder-img-lg d-block w-100" color="#333" background="#555" text="Third slide" >}}
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleInterval" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleInterval" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
{{< /example >}}


## Usage

### Via data attributes

Use data attributes to easily control the position of the carousel. `data-slide` accepts the keywords `prev` or `next`, which alters the slide position relative to its current position. Alternatively, use `data-slide-to` to pass a raw slide index to the carousel `data-slide-to="2"`, which shifts the slide position to a particular index beginning with `0`.

The `data-ride="carousel"` attribute is used to mark a carousel as animating starting at page load. If you don't use `data-ride="carousel"` to initialize your carousel, you have to initialize it yourself. **It cannot be used in combination with (redundant and unnecessary) explicit JavaScript initialization of the same carousel.**

### Via JavaScript

Call carousel manually with:

{{< highlight js >}}
var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel)
{{< /highlight >}}

### Options

Options can be passed via data attributes or JavaScript. For data attributes, append the option name to `data-`, as in `data-interval=""`.

<table class="table">
  <thead>
    <tr>
      <th style="width: 100px;">Name</th>
      <th style="width: 50px;">Type</th>
      <th style="width: 50px;">Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>interval</td>
      <td>number</td>
      <td>5000</td>
      <td>The amount of time to delay between automatically cycling an item. If false, carousel will not automatically cycle.</td>
    </tr>
    <tr>
      <td>keyboard</td>
      <td>boolean</td>
      <td>true</td>
      <td>Whether the carousel should react to keyboard events.</td>
    </tr>
    <tr>
      <td>pause</td>
      <td>string | boolean</td>
      <td>"hover"</td>
      <td><p>If set to <code>"hover"</code>, pauses the cycling of the carousel on <code>mouseenter</code> and resumes the cycling of the carousel on <code>mouseleave</code>. If set to <code>false</code>, hovering over the carousel won't pause it.</p>
      <p>On touch-enabled devices, when set to <code>"hover"</code>, cycling will pause on <code>touchend</code> (once the user finished interacting with the carousel) for two intervals, before automatically resuming. Note that this is in addition to the above mouse behavior.</p></td>
    </tr>
    <tr>
      <td>slide</td>
      <td>string | boolean</td>
      <td>false</td>
      <td>Autoplays the carousel after the user manually cycles the first item. If "carousel", autoplays the carousel on load.</td>
    </tr>
    <tr>
      <td>wrap</td>
      <td>boolean</td>
      <td>true</td>
      <td>Whether the carousel should cycle continuously or have hard stops.</td>
    </tr>
    <tr>
      <td>touch</td>
      <td>boolean</td>
      <td>true</td>
      <td>Whether the carousel should support left/right swipe interactions on touchscreen devices.</td>
    </tr>
  </tbody>
</table>

### Methods

{{< callout danger >}}
{{< partial "callout-danger-async-methods.md" >}}
{{< /callout >}}

You can create a carousel instance with the carousel constructor, for example, to initialize with additional options and start cycling through items:

{{< highlight js >}}
var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 2000,
  wrap: false
})
{{< /highlight >}}

<table class="table">
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>cycle</code></td>
      <td>Cycles through the carousel items from left to right.</td>
    </tr>
    <tr>
      <td><code>pause</code></td>
      <td>Stops the carousel from cycling through items.</td>
    </tr>
    <tr>
      <td><code>prev</code></td>
      <td>Cycles to the previous item. <strong>Returns to the caller before the previous item has been shown</strong> (e.g., before the <code>slid.bs.carousel</code> event occurs).</td>
    </tr>
    <tr>
      <td><code>next</code></td>
      <td>Cycles to the next item. <strong>Returns to the caller before the next item has been shown</strong> (e.g., before the <code>slid.bs.carousel</code> event occurs).</td>
    </tr>
    <tr>
      <td><code>nextWhenVisible</code></td>
      <td>Cycles the carousel to a particular frame (0 based, similar to an array). <strong>Returns to the caller before the target item has been shown</strong> (e.g., before the <code>slid.bs.carousel</code> event occurs).</td>
    </tr>
    <tr>
      <td><code>dispose</code></td>
      <td>Destroys an element's carousel.</td>
    </tr>
    <tr>
      <td><code>getInstance</code></td>
      <td>Static method which allows you to get the carousel instance associated with a DOM element.</td>
    </tr>
  </tbody>
</table>

### Events

Bootstrap's carousel class exposes two events for hooking into carousel functionality. Both events have the following additional properties:

- `direction`: The direction in which the carousel is sliding (either `"left"` or `"right"`).
- `relatedTarget`: The DOM element that is being slid into place as the active item.
- `from`: The index of the current item
- `to`: The index of the next item

All carousel events are fired at the carousel itself (i.e. at the `<div class="carousel">`).

<table class="table">
  <thead>
    <tr>
      <th style="width: 150px;">Event type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>slide.bs.carousel</code></td>
      <td>Fires immediately when the <code>slide</code> instance method is invoked.</td>
    </tr>
    <tr>
      <td><code>slid.bs.carousel</code></td>
      <td>Fired when the carousel has completed its slide transition.</td>
    </tr>
  </tbody>
</table>

{{< highlight js >}}
var myCarousel = document.getElementById('myCarousel')

myCarousel.addEventListener('slide.bs.carousel', function () {
  // do something...
})
{{< /highlight >}}

### Change transition duration

The transition duration of `.carousel-item` can be changed with the `$carousel-transition` Sass variable before compiling or custom styles if you're using the compiled CSS. If multiple transitions are applied, make sure the transform transition is defined first (eg. `transition: transform 2s ease, opacity .5s ease-out`).
```
## _site_content_docs_4_3_forms_layout_md
```---
layout: docs
title: Layout
description: Give your forms some structure—from inline to horizontal to custom grid implementations—with our form layout options.
group: forms
toc: true
---

## Forms

Every group of form fields should reside in a `<form>` element. Bootstrap provides no default styling for the `<form>` element, but there are some powerful browser features that are provided by default.

- New to browser forms? Consider reviewing [the MDN form docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form) for an overview and complete list of available attributes.
- `<button>`s within a `<form>` default to `type="submit"`, so strive to be specific and always include a `type`.
- You can disable every form element within a form with the `disabled` attribute on the `<form>`.

Since Bootstrap applies `display: block` and `width: 100%` to almost all our form controls, forms will by default stack vertically. Additional classes can be used to vary this layout on a per-form basis.

## Utilities

[Margin utilities]({{< docsref "/utilities/spacing" >}}) are the easiest way to add some structure to forms. They provide basic grouping of labels, controls, optional help text, and form validation messaging. We recommend sticking to `margin-bottom` utilities, and using a single direction throughout the form for consistency.

Feel free to build your forms however you like, with `<fieldset>`s, `<div>`s, or nearly any other element.

{{< example >}}
<form>
  <div class="mb-3">
    <label for="formGroupExampleInput">Example label</label>
    <input type="text" class="form-control" id="formGroupExampleInput" placeholder="Example input placeholder">
  </div>
  <div class="mb-3">
    <label for="formGroupExampleInput2">Another label</label>
    <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="Another input placeholder">
  </div>
</form>
{{< /example >}}

## Form grid

More complex forms can be built using our grid classes. Use these for form layouts that require multiple columns, varied widths, and additional alignment options. **Requires the `$enable-grid-classes` Sass variable to be enabled** (on by default).

{{< example >}}
<form>
  <div class="row">
    <div class="col">
      <input type="text" class="form-control" placeholder="First name">
    </div>
    <div class="col">
      <input type="text" class="form-control" placeholder="Last name">
    </div>
  </div>
</form>
{{< /example >}}

## Form row

You may also swap `.row` for `.form-row`, a variation of our standard grid row that overrides the default column gutters for tighter and more compact layouts. **Also requires the `$enable-grid-classes` Sass variable to be enabled** (on by default).

{{< example >}}
<form>
  <div class="form-row">
    <div class="col">
      <input type="text" class="form-control" placeholder="First name">
    </div>
    <div class="col">
      <input type="text" class="form-control" placeholder="Last name">
    </div>
  </div>
</form>
{{< /example >}}

More complex layouts can also be created with the grid system.

{{< example >}}
<form>
  <div class="form-row">
    <div class="mb-3 col-md-6">
      <label for="inputEmail4">Email</label>
      <input type="email" class="form-control" id="inputEmail4">
    </div>
    <div class="mb-3 col-md-6">
      <label for="inputPassword4">Password</label>
      <input type="password" class="form-control" id="inputPassword4">
    </div>
  </div>
  <div class="mb-3">
    <label for="inputAddress">Address</label>
    <input type="text" class="form-control" id="inputAddress" placeholder="1234 Main St">
  </div>
  <div class="mb-3">
    <label for="inputAddress2">Address 2</label>
    <input type="text" class="form-control" id="inputAddress2" placeholder="Apartment, studio, or floor">
  </div>
  <div class="form-row">
    <div class="mb-3 col-md-6">
      <label for="inputCity">City</label>
      <input type="text" class="form-control" id="inputCity">
    </div>
    <div class="mb-3 col-md-4">
      <label for="inputState">State</label>
      <select id="inputState" class="form-select">
        <option selected>Choose...</option>
        <option>...</option>
      </select>
    </div>
    <div class="mb-3 col-md-2">
      <label for="inputZip">Zip</label>
      <input type="text" class="form-control" id="inputZip">
    </div>
  </div>
  <div class="mb-3">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" id="gridCheck">
      <label class="form-check-label" for="gridCheck">
        Check me out
      </label>
    </div>
  </div>
  <button type="submit" class="btn btn-primary">Sign in</button>
</form>
{{< /example >}}

## Horizontal form

Create horizontal forms with the grid by adding the `.row` class to form groups and using the `.col-*-*` classes to specify the width of your labels and controls. Be sure to add `.col-form-label` to your `<label>`s as well so they're vertically centered with their associated form controls.

At times, you maybe need to use margin or padding utilities to create that perfect alignment you need. For example, we've removed the `padding-top` on our stacked radio inputs label to better align the text baseline.

{{< example >}}
<form>
  <div class="mb-3 row">
    <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label>
    <div class="col-sm-10">
      <input type="email" class="form-control" id="inputEmail3">
    </div>
  </div>
  <div class="mb-3 row">
    <label for="inputPassword3" class="col-sm-2 col-form-label">Password</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="inputPassword3">
    </div>
  </div>
  <fieldset class="mb-3">
    <div class="row">
      <legend class="col-form-label col-sm-2 pt-0">Radios</legend>
      <div class="col-sm-10">
        <div class="form-check">
          <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios1" value="option1" checked>
          <label class="form-check-label" for="gridRadios1">
            First radio
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios2" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Second radio
          </label>
        </div>
        <div class="form-check disabled">
          <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios3" value="option3" disabled>
          <label class="form-check-label" for="gridRadios3">
            Third disabled radio
          </label>
        </div>
      </div>
    </div>
  </fieldset>
  <div class="mb-3 row">
    <div class="col-sm-2">Checkbox</div>
    <div class="col-sm-10">
      <div class="form-check">
        <input class="form-check-input" type="checkbox" id="gridCheck1">
        <label class="form-check-label" for="gridCheck1">
          Example checkbox
        </label>
      </div>
    </div>
  </div>
  <div class="mb-3 row">
    <div class="col-sm-10">
      <button type="submit" class="btn btn-primary">Sign in</button>
    </div>
  </div>
</form>
{{< /example >}}

### Horizontal form label sizing

Be sure to use `.col-form-label-sm` or `.col-form-label-lg` to your `<label>`s or `<legend>`s to correctly follow the size of `.form-control-lg` and `.form-control-sm`.

{{< example >}}
<form>
  <div class="mb-3 row">
    <label for="colFormLabelSm" class="col-sm-2 col-form-label col-form-label-sm">Email</label>
    <div class="col-sm-10">
      <input type="email" class="form-control form-control-sm" id="colFormLabelSm" placeholder="col-form-label-sm">
    </div>
  </div>
  <div class="mb-3 row">
    <label for="colFormLabel" class="col-sm-2 col-form-label">Email</label>
    <div class="col-sm-10">
      <input type="email" class="form-control" id="colFormLabel" placeholder="col-form-label">
    </div>
  </div>
  <div class="mb-3 row">
    <label for="colFormLabelLg" class="col-sm-2 col-form-label col-form-label-lg">Email</label>
    <div class="col-sm-10">
      <input type="email" class="form-control form-control-lg" id="colFormLabelLg" placeholder="col-form-label-lg">
    </div>
  </div>
</form>
{{< /example >}}

## Column sizing

As shown in the previous examples, our grid system allows you to place any number of `.col`s within a `.row` or `.form-row`. They'll split the available width equally between them. You may also pick a subset of your columns to take up more or less space, while the remaining `.col`s equally split the rest, with specific column classes like `.col-7`.

{{< example >}}
<form>
  <div class="form-row">
    <div class="col-7">
      <input type="text" class="form-control" placeholder="City">
    </div>
    <div class="col">
      <input type="text" class="form-control" placeholder="State">
    </div>
    <div class="col">
      <input type="text" class="form-control" placeholder="Zip">
    </div>
  </div>
</form>
{{< /example >}}

## Auto-sizing

The example below uses a flexbox utility to vertically center the contents and changes `.col` to `.col-auto` so that your columns only take up as much space as needed. Put another way, the column sizes itself based on the contents.

{{< example >}}
<form>
  <div class="form-row align-items-center">
    <div class="col-auto">
      <label class="sr-only" for="autoSizingInput">Name</label>
      <input type="text" class="form-control mb-2" id="autoSizingInput" placeholder="Jane Doe">
    </div>
    <div class="col-auto">
      <label class="sr-only" for="autoSizingInputGroup">Username</label>
      <div class="input-group mb-2">
        <div class="input-group-prepend">
          <div class="input-group-text">@</div>
        </div>
        <input type="text" class="form-control" id="autoSizingInputGroup" placeholder="Username">
      </div>
    </div>
    <div class="col-auto">
      <label class="sr-only" for="autoSizingSelect">Preference</label>
      <select class="form-select mb-2" id="autoSizingSelect">
        <option selected>Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
      </select>
    </div>
    <div class="col-auto">
      <div class="form-check mb-2">
        <input class="form-check-input" type="checkbox" id="autoSizingCheck">
        <label class="form-check-label" for="autoSizingCheck">
          Remember me
        </label>
      </div>
    </div>
    <div class="col-auto">
      <button type="submit" class="btn btn-primary mb-2">Submit</button>
    </div>
  </div>
</form>
{{< /example >}}

You can then remix that once again with size-specific column classes.

{{< example >}}
<form>
  <div class="form-row align-items-center">
    <div class="col-sm-3 my-1">
      <label class="sr-only" for="specificSizeInputName">Name</label>
      <input type="text" class="form-control" id="specificSizeInputName" placeholder="Jane Doe">
    </div>
    <div class="col-sm-3 my-1">
      <label class="sr-only" for="specificSizeInputGroupUsername">Username</label>
      <div class="input-group">
        <div class="input-group-prepend">
          <div class="input-group-text">@</div>
        </div>
        <input type="text" class="form-control" id="specificSizeInputGroupUsername" placeholder="Username">
      </div>
    </div>
    <div class="col-sm-3 my-1">
      <label class="sr-only" for="specificSizeSelect">Preference</label>
      <select class="form-select" id="specificSizeSelect">
        <option selected>Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
      </select>
    </div>
    <div class="col-auto my-1">
      <div class="form-check">
        <input class="form-check-input" type="checkbox" id="autoSizingCheck2">
        <label class="form-check-label" for="autoSizingCheck2">
          Remember me
        </label>
      </div>
    </div>
    <div class="col-auto my-1">
      <button type="submit" class="btn btn-primary">Submit</button>
    </div>
  </div>
</form>
{{< /example >}}

## Inline forms

Use the `.form-inline` class to display a series of labels, form controls, and buttons on a single horizontal row. Form controls within inline forms vary slightly from their default states.

- Controls are `display: flex`, collapsing any HTML white space and allowing you to provide alignment control with [spacing]({{< docsref "/utilities/spacing" >}}) and [flexbox]({{< docsref "/utilities/flex" >}}) utilities.
- Controls and input groups receive `width: auto` to override the Bootstrap default `width: 100%`.
- Controls **only appear inline in viewports that are at least 576px wide** to account for narrow viewports on mobile devices.

You may need to manually address the width and alignment of individual form controls with [spacing utilities]({{< docsref "/utilities/spacing" >}}) (as shown below). Lastly, be sure to always include a `<label>` with each form control, even if you need to hide it from non-screenreader visitors with `.sr-only`.

{{< example >}}
<form class="form-inline">
  <label class="sr-only" for="inlineFormInputName">Name</label>
  <input type="text" class="form-control mb-2 mr-sm-2" id="inlineFormInputName" placeholder="Jane Doe">

  <label class="sr-only" for="inlineFormInputGroupUsername">Username</label>
  <div class="input-group mb-2 mr-sm-2">
    <div class="input-group-prepend">
      <div class="input-group-text">@</div>
    </div>
    <input type="text" class="form-control" id="inlineFormInputGroupUsername" placeholder="Username">
  </div>

  <label class="sr-only" for="inlineFormSelectPref">Preference</label>
  <select class="form-select mb-2 mr-sm-2" id="inlineFormSelectPref">
    <option selected>Choose...</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
  </select>

  <div class="form-check mb-2 mr-sm-2">
    <input class="form-check-input" type="checkbox" id="inlineFormCheck">
    <label class="form-check-label" for="inlineFormCheck">
      Remember me
    </label>
  </div>

  <button type="submit" class="btn btn-primary mb-2">Submit</button>
</form>
{{< /example >}}

{{< callout warning >}}
### Alternatives to hidden labels

Assistive technologies such as screen readers will have trouble with your forms if you don't include a label for every input. For these inline forms, you can hide the labels using the `.sr-only` class. There are further alternative methods of providing a label for assistive technologies, such as the `aria-label`, `aria-labelledby` or `title` attribute. If none of these are present, assistive technologies may resort to using the `placeholder` attribute, if present, but note that use of `placeholder` as a replacement for other labeling methods is not advised.
{{< /callout >}}
```
## _site_content_docs_4_3_components_badge_md
```---
layout: docs
title: Badges
description: Documentation and examples for badges, our small count and labeling component.
group: components
toc: true
---

## Example

Badges scale to match the size of the immediate parent element by using relative font sizing and `em` units. As of v5, badges no longer have focus or hover styles for links.

{{< example >}}
<h1>Example heading <span class="badge bg-secondary">New</span></h1>
<h2>Example heading <span class="badge bg-secondary">New</span></h2>
<h3>Example heading <span class="badge bg-secondary">New</span></h3>
<h4>Example heading <span class="badge bg-secondary">New</span></h4>
<h5>Example heading <span class="badge bg-secondary">New</span></h5>
<h6>Example heading <span class="badge bg-secondary">New</span></h6>
{{< /example >}}

Badges can be used as part of links or buttons to provide a counter.

{{< example >}}
<button type="button" class="btn btn-primary">
  Notifications <span class="badge bg-secondary">4</span>
</button>
{{< /example >}}

Note that depending on how they are used, badges may be confusing for users of screen readers and similar assistive technologies. While the styling of badges provides a visual cue as to their purpose, these users will simply be presented with the content of the badge. Depending on the specific situation, these badges may seem like random additional words or numbers at the end of a sentence, link, or button.

Unless the context is clear (as with the "Notifications" example, where it is understood that the "4" is the number of notifications), consider including additional context with a visually hidden piece of additional text.

{{< example >}}
<button type="button" class="btn btn-primary">
  Profile <span class="badge bg-secondary">9</span>
  <span class="sr-only">unread messages</span>
</button>
{{< /example >}}

## Background colors

Use our background utility classes to quickly change the appearance of a badge. Please note that when using Bootstrap's default `.bg-light`, you'll likely need a text color utility like `.text-dark` for proper styling. This is because background utilities do not set anything but `background-color`.

{{< example >}}
{{< badge.inline >}}
{{- range (index $.Site.Data "theme-colors") }}
<span class="badge bg-{{ .name }}{{ if or (eq .name "light") (eq .name "warning") }} text-dark{{ end }}">{{ .name | title }}</span>{{- end -}}
{{< /badge.inline >}}
{{< /example >}}

{{< callout info >}}
{{< partial "callout-warning-color-assistive-technologies.md" >}}
{{< /callout >}}

## Pill badges

Use the `.rounded-pill` utility class to make badges more rounded with a larger `border-radius`.

{{< example >}}
{{< badge.inline >}}
{{- range (index $.Site.Data "theme-colors") }}
<span class="badge rounded-pill bg-{{ .name }}{{ if or (eq .name "light") (eq .name "warning") }} text-dark{{ end }}">{{ .name | title }}</span>{{- end -}}
{{< /badge.inline >}}
{{< /example >}}
```
## _site_content_docs_4_3_components_tooltips_md
```---
layout: docs
title: Tooltips
description: Documentation and examples for adding custom Bootstrap tooltips with CSS and JavaScript using CSS3 for animations and data-attributes for local title storage.
group: components
toc: true
---

## Overview

Things to know when using the tooltip plugin:

- Tooltips rely on the 3rd party library [Popper.js](https://popper.js.org/) for positioning. You must include [popper.min.js]({{< param "cdn.popper" >}}) before bootstrap.js or use `bootstrap.bundle.min.js` / `bootstrap.bundle.js` which contains Popper.js in order for tooltips to work!
- Tooltips are opt-in for performance reasons, so **you must initialize them yourself**.
- Tooltips with zero-length titles are never displayed.
- Specify `container: 'body'` to avoid rendering problems in more complex components (like our input groups, button groups, etc).
- Triggering tooltips on hidden elements will not work.
- Tooltips for `.disabled` or `disabled` elements must be triggered on a wrapper element.
- When triggered from hyperlinks that span multiple lines, tooltips will be centered. Use `white-space: nowrap;` on your `<a>`s to avoid this behavior.
- Tooltips must be hidden before their corresponding elements have been removed from the DOM.
- Tooltips can be triggered thanks to an element inside a shadow DOM.

{{< callout info >}}
{{< partial "callout-info-prefersreducedmotion.md" >}}
{{< /callout >}}

Got all that? Great, let's see how they work with some examples.

## Example: Enable tooltips everywhere

One way to initialize all tooltips on a page would be to select them by their `data-toggle` attribute:

{{< highlight js >}}
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})
{{< /highlight >}}

## Examples

Hover over the links below to see tooltips:

<div class="bd-example tooltip-demo">
  <p class="muted">Tight pants next level keffiyeh <a href="#" data-toggle="tooltip" title="Default tooltip">you probably</a> haven't heard of them. Photo booth beard raw denim letterpress vegan messenger bag stumptown. Farm-to-table seitan, mcsweeney's fixie sustainable quinoa 8-bit american apparel <a href="#" data-toggle="tooltip" title="Another tooltip">have a</a> terry richardson vinyl chambray. Beard stumptown, cardigans banh mi lomo thundercats. Tofu biodiesel williamsburg marfa, four loko mcsweeney's cleanse vegan chambray. A really ironic artisan <a href="#" data-toggle="tooltip" title="Another one here too">whatever keytar</a>, scenester farm-to-table banksy Austin <a href="#" data-toggle="tooltip" title="The last tip!">twitter handle</a> freegan cred raw denim single-origin coffee viral.
  </p>
</div>

Hover over the buttons below to see the four tooltips directions: top, right, bottom, and left.

<div class="bd-example tooltip-demo">
  <div class="bd-example-tooltips">
    <button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="top" title="Tooltip on top">Tooltip on top</button>
    <button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="right" title="Tooltip on right">Tooltip on right</button>
    <button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="bottom" title="Tooltip on bottom">Tooltip on bottom</button>
    <button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="left" title="Tooltip on left">Tooltip on left</button>
    <button type="button" class="btn btn-secondary" data-toggle="tooltip" data-html="true" title="<em>Tooltip</em> <u>with</u> <b>HTML</b>">Tooltip with HTML</button>
  </div>
</div>

{{< highlight html >}}
<button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="top" title="Tooltip on top">
  Tooltip on top
</button>
<button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="right" title="Tooltip on right">
  Tooltip on right
</button>
<button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="bottom" title="Tooltip on bottom">
  Tooltip on bottom
</button>
<button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="left" title="Tooltip on left">
  Tooltip on left
</button>
{{< /highlight >}}

And with custom HTML added:

{{< highlight html >}}
<button type="button" class="btn btn-secondary" data-toggle="tooltip" data-html="true" title="<em>Tooltip</em> <u>with</u> <b>HTML</b>">
  Tooltip with HTML
</button>
{{< /highlight >}}

## Usage

The tooltip plugin generates content and markup on demand, and by default places tooltips after their trigger element.

Trigger the tooltip via JavaScript:

{{< highlight js >}}
var exampleEl = document.getElementById('example')
var tooltip = new bootstrap.Tooltip(exampleEl, options)
{{< /highlight >}}

{{< callout warning >}}
##### Overflow `auto` and `scroll`

Tooltip position attempts to automatically change when a parent container has `overflow: auto` or `overflow: scroll` like our `.table-responsive`, but still keeps the original placement's positioning. To resolve, set the `boundary` option to anything other than default value, `'scrollParent'`, such as `'window'`:

{{< highlight js >}}
var exampleEl = document.getElementById('example')
var tooltip = new bootstrap.Tooltip(exampleEl, {
  boundary: 'window'
})
{{< /highlight >}}
{{< /callout >}}

### Markup

The required markup for a tooltip is only a `data` attribute and `title` on the HTML element you wish to have a tooltip. The generated markup of a tooltip is rather simple, though it does require a position (by default, set to `top` by the plugin).

{{< callout warning >}}
##### Making tooltips work for keyboard and assistive technology users

You should only add tooltips to HTML elements that are traditionally keyboard-focusable and interactive (such as links or form controls). Although arbitrary HTML elements (such as `<span>`s) can be made focusable by adding the `tabindex="0"` attribute, this will add potentially annoying and confusing tab stops on non-interactive elements for keyboard users, and most assistive technologies currently do not announce the tooltip in this situation. Additionally, do not rely solely on `hover` as the trigger for your tooltip, as this will make your tooltips impossible to trigger for keyboard users.
{{< /callout >}}

{{< highlight html >}}
<!-- HTML to write -->
<a href="#" data-toggle="tooltip" title="Some tooltip text!">Hover over me</a>

<!-- Generated markup by the plugin -->
<div class="tooltip bs-tooltip-top" role="tooltip">
  <div class="tooltip-arrow"></div>
  <div class="tooltip-inner">
    Some tooltip text!
  </div>
</div>
{{< /highlight >}}

### Disabled elements

Elements with the `disabled` attribute aren't interactive, meaning users cannot focus, hover, or click them to trigger a tooltip (or popover). As a workaround, you'll want to trigger the tooltip from a wrapper `<div>` or `<span>`, ideally made keyboard-focusable using `tabindex="0"`, and override the `pointer-events` on the disabled element.

<div class="tooltip-demo">
{{< example >}}
<span class="d-inline-block" tabindex="0" data-toggle="tooltip" title="Disabled tooltip">
  <button class="btn btn-primary" style="pointer-events: none;" type="button" disabled>Disabled button</button>
</span>
{{< /example >}}
</div>

### Options

Options can be passed via data attributes or JavaScript. For data attributes, append the option name to `data-`, as in `data-animation=""`.

{{< callout warning >}}
Note that for security reasons the `sanitize`, `sanitizeFn` and `whiteList` options cannot be supplied using data attributes.
{{< /callout >}}

<table class="table">
  <thead>
    <tr>
      <th style="width: 100px;">Name</th>
      <th style="width: 100px;">Type</th>
      <th style="width: 50px;">Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>animation</td>
      <td>boolean</td>
      <td>true</td>
      <td>Apply a CSS fade transition to the tooltip</td>
    </tr>
    <tr>
      <td>container</td>
      <td>string | element | false</td>
      <td>false</td>
      <td>
        <p>Appends the tooltip to a specific element. Example: <code>container: 'body'</code>. This option is particularly useful in that it allows you to position the tooltip in the flow of the document near the triggering element - which will prevent the tooltip from floating away from the triggering element during a window resize.</p>
      </td>
    </tr>
    <tr>
      <td>delay</td>
      <td>number | object</td>
      <td>0</td>
      <td>
        <p>Delay showing and hiding the tooltip (ms) - does not apply to manual trigger type</p>
        <p>If a number is supplied, delay is applied to both hide/show</p>
        <p>Object structure is: <code>delay: { "show": 500, "hide": 100 }</code></p>
      </td>
    </tr>
    <tr>
      <td>html</td>
      <td>boolean</td>
      <td>false</td>
      <td>
        <p>Allow HTML in the tooltip.</p>
        <p>If true, HTML tags in the tooltip's <code>title</code> will be rendered in the tooltip. If false, <code>innerText</code> property will be used to insert content into the DOM.</p>
        <p>Use text if you're worried about XSS attacks.</p>
      </td>
    </tr>
    <tr>
      <td>placement</td>
      <td>string | function</td>
      <td>'top'</td>
      <td>
        <p>How to position the tooltip - auto | top | bottom | left | right.<br>When <code>auto</code> is specified, it will dynamically reorient the tooltip.</p>
        <p>When a function is used to determine the placement, it is called with the tooltip DOM node as its first argument and the triggering element DOM node as its second. The <code>this</code> context is set to the tooltip instance.</p>
      </td>
    </tr>
    <tr>
      <td>selector</td>
      <td>string | false</td>
      <td>false</td>
      <td>If a selector is provided, tooltip objects will be delegated to the specified targets. In practice, this is used to also apply tooltips to dynamically added DOM elements (<code>jQuery.on</code> support). See <a href="{{< param repo >}}/issues/4215">this</a> and <a href="https://codepen.io/Johann-S/pen/djJYPb">an informative example</a>.</td>
    </tr>
    <tr>
      <td>template</td>
      <td>string</td>
      <td><code>'&lt;div class="tooltip" role="tooltip"&gt;&lt;div class="tooltip-arrow"&gt;&lt;/div&gt;&lt;div class="tooltip-inner"&gt;&lt;/div&gt;&lt;/div&gt;'</code></td>
      <td>
        <p>Base HTML to use when creating the tooltip.</p>
        <p>The tooltip's <code>title</code> will be injected into the <code>.tooltip-inner</code>.</p>
        <p><code>.tooltip-arrow</code> will become the tooltip's arrow.</p>
        <p>The outermost wrapper element should have the <code>.tooltip</code> class and <code>role="tooltip"</code>.</p>
      </td>
    </tr>
    <tr>
      <td>title</td>
      <td>string | element | function</td>
      <td>''</td>
      <td>
        <p>Default title value if <code>title</code> attribute isn't present.</p>
        <p>If a function is given, it will be called with its <code>this</code> reference set to the element that the tooltip is attached to.</p>
      </td>
    </tr>
    <tr>
      <td>trigger</td>
      <td>string</td>
      <td>'hover focus'</td>
      <td>
        <p>How tooltip is triggered - click | hover | focus | manual. You may pass multiple triggers; separate them with a space.</p>
        <p><code>'manual'</code> indicates that the tooltip will be triggered programmatically via the <code>.tooltip('show')</code>, <code>.tooltip('hide')</code> and <code>.tooltip('toggle')</code> methods; this value cannot be combined with any other trigger.</p>
        <p><code>'hover'</code> on its own will result in tooltips that cannot be triggered via the keyboard, and should only be used if alternative methods for conveying the same information for keyboard users is present.</p>
      </td>
    </tr>
    <tr>
      <td>offset</td>
      <td>number | string | function</td>
      <td>0</td>
      <td>
        <p>Offset of the tooltip relative to its target.</p>
        <p>When a function is used to determine the offset, it is called with an object containing the offset data as its first argument. The function must return an object with the same structure. The triggering element DOM node is passed as the second argument.</p>
        <p>For more information refer to Popper.js's <a href="https://popper.js.org/popper-documentation.html#modifiers..offset.offset">offset docs</a>.</p>
      </td>
    </tr>
    <tr>
      <td>fallbackPlacement</td>
      <td>string | array</td>
      <td>'flip'</td>
      <td>Allow to specify which position Popper will use on fallback. For more information refer to
      Popper.js's <a href="https://popper.js.org/popper-documentation.html#modifiers..flip.behavior">behavior docs</a></td>
    </tr>
    <tr>
      <td>boundary</td>
      <td>string | element</td>
      <td>'scrollParent'</td>
      <td>Overflow constraint boundary of the tooltip. Accepts the values of <code>'viewport'</code>, <code>'window'</code>, <code>'scrollParent'</code>, or an HTMLElement reference (JavaScript only). For more information refer to Popper.js's <a href="https://popper.js.org/popper-documentation.html#modifiers..preventOverflow.boundariesElement">preventOverflow docs</a>.</td>
    </tr>
    <tr>
      <td>sanitize</td>
      <td>boolean</td>
      <td>true</td>
      <td>Enable or disable the sanitization. If activated <code>'template'</code> and <code>'title'</code> options will be sanitized.</td>
    </tr>
    <tr>
      <td>whiteList</td>
      <td>object</td>
      <td><a href="{{< docsref "/getting-started/javascript#sanitizer" >}}">Default value</a></td>
      <td>Object which contains allowed attributes and tags</td>
    </tr>
    <tr>
      <td>sanitizeFn</td>
      <td>null | function</td>
      <td>null</td>
      <td>Here you can supply your own sanitize function. This can be useful if you prefer to use a dedicated library to perform sanitization.</td>
    </tr>
    <tr>
      <td>popperConfig</td>
      <td>null | object</td>
      <td>null</td>
      <td>To change Bootstrap's default Popper.js config, see <a href="https://popper.js.org/popper-documentation.html#Popper.Defaults">Popper.js's configuration</a></td>
    </tr>
  </tbody>
</table>

{{< callout info >}}
#### Data attributes for individual tooltips

Options for individual tooltips can alternatively be specified through the use of data attributes, as explained above.
{{< /callout >}}

### Methods

{{< callout danger >}}
{{< partial "callout-danger-async-methods.md" >}}
{{< /callout >}}

#### show

Reveals an element's tooltip. **Returns to the caller before the tooltip has actually been shown** (i.e. before the `shown.bs.tooltip` event occurs). This is considered a "manual" triggering of the tooltip. Tooltips with zero-length titles are never displayed.

{{< highlight js >}}tooltip.show(){{< /highlight >}}

#### hide

Hides an element's tooltip. **Returns to the caller before the tooltip has actually been hidden** (i.e. before the `hidden.bs.tooltip` event occurs). This is considered a "manual" triggering of the tooltip.

{{< highlight js >}}tooltip.hide(){{< /highlight >}}

#### toggle

Toggles an element's tooltip. **Returns to the caller before the tooltip has actually been shown or hidden** (i.e. before the `shown.bs.tooltip` or `hidden.bs.tooltip` event occurs). This is considered a "manual" triggering of the tooltip.

{{< highlight js >}}tooltip.toggle(){{< /highlight >}}

#### dispose

Hides and destroys an element's tooltip. Tooltips that use delegation (which are created using [the `selector` option](#options)) cannot be individually destroyed on descendant trigger elements.

{{< highlight js >}}tooltip.dispose(){{< /highlight >}}

#### enable

Gives an element's tooltip the ability to be shown. **Tooltips are enabled by default.**

{{< highlight js >}}tooltip.enable(){{< /highlight >}}

#### disable

Removes the ability for an element's tooltip to be shown. The tooltip will only be able to be shown if it is re-enabled.

{{< highlight js >}}tooltip.disable(){{< /highlight >}}

#### toggleEnabled

Toggles the ability for an element's tooltip to be shown or hidden.

{{< highlight js >}}tooltip.toggleEnabled(){{< /highlight >}}

#### update

Updates the position of an element's tooltip.

{{< highlight js >}}tooltip.update(){{< /highlight >}}

### Events

<table class="table">
  <thead>
    <tr>
      <th style="width: 150px;">Event type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>show.bs.tooltip</td>
      <td>This event fires immediately when the <code>show</code> instance method is called.</td>
    </tr>
    <tr>
      <td>shown.bs.tooltip</td>
      <td>This event is fired when the tooltip has been made visible to the user (will wait for CSS transitions to complete).</td>
    </tr>
    <tr>
      <td>hide.bs.tooltip</td>
      <td>This event is fired immediately when the <code>hide</code> instance method has been called.</td>
    </tr>
    <tr>
      <td>hidden.bs.tooltip</td>
      <td>This event is fired when the tooltip has finished being hidden from the user (will wait for CSS transitions to complete).</td>
    </tr>
    <tr>
      <td>inserted.bs.tooltip</td>
      <td>This event is fired after the <code>show.bs.tooltip</code> event when the tooltip template has been added to the DOM.</td>
    </tr>
  </tbody>
</table>

{{< highlight js >}}
var myTooltipEl = document.getElementById('myTooltip')
var tooltip = new bootstrap.Tooltip(myTooltipEl)

myTooltipEl.addEventListener('hidden.bs.tooltip', function () {
  // do something...
})

tooltip.hide()
{{< /highlight >}}
```
## _site_content_docs_4_3_components_toasts_md
```---
layout: docs
title: Toasts
description: Push notifications to your visitors with a toast, a lightweight and easily customizable alert message.
group: components
toc: true
---

Toasts are lightweight notifications designed to mimic the push notifications that have been popularized by mobile and desktop operating systems. They're built with flexbox, so they're easy to align and position.

## Overview

Things to know when using the toast plugin:

- Toasts are opt-in for performance reasons, so **you must initialize them yourself**.
- **Please note that you are responsible for positioning toasts.**
- Toasts will automatically hide if you do not specify `autohide: false`.

{{< callout info >}}
{{< partial "callout-info-prefersreducedmotion.md" >}}
{{< /callout >}}

## Examples

### Basic

To encourage extensible and predictable toasts, we recommend a header and body. Toast headers use `display: flex`, allowing easy alignment of content thanks to our margin and flexbox utilities.

Toasts are as flexible as you need and have very little required markup. At a minimum, we require a single element to contain your "toasted" content and strongly encourage a dismiss button.

{{< example class="bg-light" >}}
<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="toast-header">
    {{< placeholder width="20" height="20" background="#007aff" class="rounded mr-2" text="false" title="false" >}}
    <strong class="mr-auto">Bootstrap</strong>
    <small>11 mins ago</small>
    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
  <div class="toast-body">
    Hello, world! This is a toast message.
  </div>
</div>
{{< /example >}}

### Translucent

Toasts are slightly translucent, too, so they blend over whatever they might appear over. For browsers that support the `backdrop-filter` CSS property, we'll also attempt to blur the elements under a toast.

{{< example class="bg-dark" >}}
<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="toast-header">
    {{< placeholder width="20" height="20" background="#007aff" class="rounded mr-2" text="false" title="false" >}}
    <strong class="mr-auto">Bootstrap</strong>
    <small class="text-muted">11 mins ago</small>
    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
  <div class="toast-body">
    Hello, world! This is a toast message.
  </div>
</div>
{{< /example >}}

### Stacking

When you have multiple toasts, we default to vertically stacking them in a readable manner.

{{< example class="bg-light" >}}
<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="toast-header">
    {{< placeholder width="20" height="20" background="#007aff" class="rounded mr-2" text="false" title="false" >}}
    <strong class="mr-auto">Bootstrap</strong>
    <small class="text-muted">just now</small>
    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
  <div class="toast-body">
    See? Just like this.
  </div>
</div>

<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="toast-header">
    {{< placeholder width="20" height="20" background="#007aff" class="rounded mr-2" text="false" title="false" >}}
    <strong class="mr-auto">Bootstrap</strong>
    <small class="text-muted">2 seconds ago</small>
    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
  <div class="toast-body">
    Heads up, toasts will stack automatically
  </div>
</div>
{{< /example >}}

## Placement

Place toasts with custom CSS as you need them. The top right is often used for notifications, as is the top middle. If you're only ever going to show one toast at a time, put the positioning styles right on the `.toast`.

{{< example class="bg-dark" >}}
<div aria-live="polite" aria-atomic="true" style="position: relative; min-height: 200px;">
  <div class="toast" style="position: absolute; top: 0; right: 0;">
    <div class="toast-header">
      {{< placeholder width="20" height="20" background="#007aff" class="rounded mr-2" text="false" title="false" >}}
      <strong class="mr-auto">Bootstrap</strong>
      <small>11 mins ago</small>
      <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <div class="toast-body">
      Hello, world! This is a toast message.
    </div>
  </div>
</div>
{{< /example >}}

For systems that generate more notifications, consider using a wrapping element so they can easily stack.

{{< example class="bg-dark" >}}
<div aria-live="polite" aria-atomic="true" style="position: relative; min-height: 200px;">
  <!-- Position it -->
  <div style="position: absolute; top: 0; right: 0;">

    <!-- Then put toasts within -->
    <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
      <div class="toast-header">
        {{< placeholder width="20" height="20" background="#007aff" class="rounded mr-2" text="false" title="false" >}}
        <strong class="mr-auto">Bootstrap</strong>
        <small class="text-muted">just now</small>
        <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="toast-body">
        See? Just like this.
      </div>
    </div>

    <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
      <div class="toast-header">
        {{< placeholder width="20" height="20" background="#007aff" class="rounded mr-2" text="false" title="false" >}}
        <strong class="mr-auto">Bootstrap</strong>
        <small class="text-muted">2 seconds ago</small>
        <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="toast-body">
        Heads up, toasts will stack automatically
      </div>
    </div>
  </div>
</div>
{{< /example >}}

You can also get fancy with flexbox utilities to align toasts horizontally and/or vertically.

{{< example class="bg-dark" >}}
<!-- Flexbox container for aligning the toasts -->
<div aria-live="polite" aria-atomic="true" class="d-flex justify-content-center align-items-center" style="min-height: 200px;">

  <!-- Then put toasts within -->
  <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      {{< placeholder width="20" height="20" background="#007aff" class="rounded mr-2" text="false" title="false" >}}
      <strong class="mr-auto">Bootstrap</strong>
      <small>11 mins ago</small>
      <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <div class="toast-body">
      Hello, world! This is a toast message.
    </div>
  </div>
</div>
{{< /example >}}

## Accessibility

Toasts are intended to be small interruptions to your visitors or users, so to help those with screen readers and similar assistive technologies, you should wrap your toasts in an [`aria-live` region](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Live_Regions). Changes to live regions (such as injecting/updating a toast component) are automatically announced by screen readers without needing to move the user's focus or otherwise interrupt the user. Additionally, include `aria-atomic="true"` to ensure that the entire toast is always announced as a single (atomic) unit, rather than announcing what was changed (which could lead to problems if you only update part of the toast's content, or if displaying the same toast content at a later point in time). If the information needed is important for the process, e.g. for a list of errors in a form, then use the [alert component]({{< docsref "/components/alerts" >}}) instead of toast.

Note that the live region needs to be present in the markup *before* the toast is generated or updated. If you dynamically generate both at the same time and inject them into the page, they will generally not be announced by assistive technologies.

You also need to adapt the `role` and `aria-live` level depending on the content. If it's an important message like an error, use `role="alert" aria-live="assertive"`, otherwise use `role="status" aria-live="polite"` attributes.

As the content you're displaying changes, be sure to update the [`delay` timeout](#options) to ensure people have enough time to read the toast.

{{< highlight html >}}
<div class="toast" role="alert" aria-live="polite" aria-atomic="true" data-delay="10000">
  <div role="alert" aria-live="assertive" aria-atomic="true">...</div>
</div>
{{< /highlight >}}

When using `autohide: false`, you must add a close button to allow users to dismiss the toast.

{{< example class="bg-light" >}}
<div role="alert" aria-live="assertive" aria-atomic="true" class="toast" data-autohide="false">
  <div class="toast-header">
    {{< placeholder width="20" height="20" background="#007aff" class="rounded mr-2" text="false" title="false" >}}
    <strong class="mr-auto">Bootstrap</strong>
    <small>11 mins ago</small>
    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
  <div class="toast-body">
    Hello, world! This is a toast message.
  </div>
</div>
{{< /example >}}

## JavaScript behavior

### Usage

Initialize toasts via JavaScript:

{{< highlight js >}}
var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
  return new bootstrap.Toast(toastEl, option)
})
{{< /highlight >}}

### Options

Options can be passed via data attributes or JavaScript. For data attributes, append the option name to `data-`, as in `data-animation=""`.

<table class="table">
  <thead>
    <tr>
      <th style="width: 100px;">Name</th>
      <th style="width: 100px;">Type</th>
      <th style="width: 50px;">Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>animation</td>
      <td>boolean</td>
      <td>true</td>
      <td>Apply a CSS fade transition to the toast</td>
    </tr>
    <tr>
      <td>autohide</td>
      <td>boolean</td>
      <td>true</td>
      <td>Auto hide the toast</td>
    </tr>
    <tr>
      <td>delay</td>
      <td>number</td>
      <td>
        <code>500</code>
      </td>
      <td>Delay hiding the toast (ms)</td>
    </tr>
  </tbody>
</table>

### Methods

{{< callout danger >}}
{{< partial "callout-danger-async-methods.md" >}}
{{< /callout >}}

#### show

Reveals an element's toast. **Returns to the caller before the toast has actually been shown** (i.e. before the `shown.bs.toast` event occurs).
You have to manually call this method, instead your toast won't show.

{{< highlight js >}}toast.show(){{< /highlight >}}

#### hide

Hides an element's toast. **Returns to the caller before the toast has actually been hidden** (i.e. before the `hidden.bs.toast` event occurs). You have to manually call this method if you made `autohide` to `false`.

{{< highlight js >}}toast.hide(){{< /highlight >}}

#### dispose

Hides an element's toast. Your toast will remain on the DOM but won't show anymore.

{{< highlight js >}}toast.dispose(){{< /highlight >}}

### Events

<table class="table">
  <thead>
    <tr>
      <th style="width: 150px;">Event type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>show.bs.toast</td>
      <td>This event fires immediately when the <code>show</code> instance method is called.</td>
    </tr>
    <tr>
      <td>shown.bs.toast</td>
      <td>This event is fired when the toast has been made visible to the user.</td>
    </tr>
    <tr>
      <td>hide.bs.toast</td>
      <td>This event is fired immediately when the <code>hide</code> instance method has been called.</td>
    </tr>
    <tr>
      <td>hidden.bs.toast</td>
      <td>This event is fired when the toast has finished being hidden from the user.</td>
    </tr>
  </tbody>
</table>

{{< highlight js >}}
var myToastEl = document.getElementById('myToast')
myToastEl.addEventListener('hidden.bs.toast', function () {
  // do something...
})
{{< /highlight >}}
```
## _site_content_docs_4_3_utilities_position_md
```---
layout: docs
title: Position
description: Use these shorthand utilities for quickly configuring the position of an element.
group: utilities
toc: true
---

## Common values

Quick positioning classes are available, though they are not responsive.

{{< highlight html >}}
<div class="position-static">...</div>
<div class="position-relative">...</div>
<div class="position-absolute">...</div>
<div class="position-fixed">...</div>
<div class="position-sticky">...</div>
{{< /highlight >}}
```
## _site_content_docs_4_3_utilities_sizing_md
```---
layout: docs
title: Sizing
description: Easily make an element as wide or as tall with our width and height utilities.
group: utilities
toc: true
---

## Relative to the parent

Width and height utilities are generated from the `$sizes` Sass map in `_variables.scss`. Includes support for `25%`, `50%`, `75%`, `100%`, and `auto` by default. Modify those values as you need to generate different utilities here.

{{< example >}}
<div class="w-25 p-3" style="background-color: #eee;">Width 25%</div>
<div class="w-50 p-3" style="background-color: #eee;">Width 50%</div>
<div class="w-75 p-3" style="background-color: #eee;">Width 75%</div>
<div class="w-100 p-3" style="background-color: #eee;">Width 100%</div>
<div class="w-auto p-3" style="background-color: #eee;">Width auto</div>
{{< /example >}}

{{< example >}}
<div style="height: 100px; background-color: rgba(255,0,0,0.1);">
  <div class="h-25 d-inline-block" style="width: 120px; background-color: rgba(0,0,255,.1)">Height 25%</div>
  <div class="h-50 d-inline-block" style="width: 120px; background-color: rgba(0,0,255,.1)">Height 50%</div>
  <div class="h-75 d-inline-block" style="width: 120px; background-color: rgba(0,0,255,.1)">Height 75%</div>
  <div class="h-100 d-inline-block" style="width: 120px; background-color: rgba(0,0,255,.1)">Height 100%</div>
  <div class="h-auto d-inline-block" style="width: 120px; background-color: rgba(0,0,255,.1)">Height auto</div>
</div>
{{< /example >}}

You can also use `max-width: 100%;` and `max-height: 100%;` utilities as needed.

{{< example >}}
{{< placeholder width="100%" height="100" class="mw-100" text="Max-width 100%" >}}
{{< /example >}}

{{< example >}}
<div style="height: 100px; background-color: rgba(255,0,0,.1);">
  <div class="mh-100" style="width: 100px; height: 200px; background-color: rgba(0,0,255,.1);">Max-height 100%</div>
</div>
{{< /example >}}

## Relative to the viewport

You can also use utilities to set the width and height relative to the viewport.

{{< highlight html >}}
<div class="min-vw-100">Min-width 100vw</div>
<div class="min-vh-100">Min-height 100vh</div>
<div class="vw-100">Width 100vw</div>
<div class="vh-100">Height 100vh</div>
{{< /highlight >}}
```
## _site_layouts_partials_callout_danger_async_methods_md
```#### Asynchronous methods and transitions

All API methods are **asynchronous** and start a **transition**. They return to the caller as soon as the transition is started but **before it ends**. In addition, a method call on a **transitioning component will be ignored**.

[See our JavaScript documentation for more information](/docs/{{ .Site.Params.docs_version }}/getting-started/javascript/).
```
## _site_content_docs_4_3_utilities_display_md
```---
layout: docs
title: Display property
description: Quickly and responsively toggle the display value of components and more with our display utilities. Includes support for some of the more common values, as well as some extras for controlling display when printing.
group: utilities
toc: true
---

## How it works

Change the value of the [`display` property](https://developer.mozilla.org/en-US/docs/Web/CSS/display) with our responsive display utility classes. We purposely support only a subset of all possible values for `display`. Classes can be combined for various effects as you need.

## Notation

Display utility classes that apply to all [breakpoints]({{< docsref "/layout/overview#responsive-breakpoints" >}}), from `xs` to `xl`, have no breakpoint abbreviation in them. This is because those classes are applied from `min-width: 0;` and up, and thus are not bound by a media query. The remaining breakpoints, however, do include a breakpoint abbreviation.

As such, the classes are named using the format:

* `.d-{value}` for `xs`
* `.d-{breakpoint}-{value}` for `sm`, `md`, `lg`, and `xl`.

Where *value* is one of:

* `none`
* `inline`
* `inline-block`
* `block`
* `table`
* `table-cell`
* `table-row`
* `flex`
* `inline-flex`

The display values can be altered by changing the `$displays` variable and recompiling the SCSS.

The media queries effect screen widths with the given breakpoint *or larger*. For example, `.d-lg-none` sets `display: none;` on both `lg` and `xl` screens.

## Examples

{{< example >}}
<div class="d-inline p-2 bg-primary text-white">d-inline</div>
<div class="d-inline p-2 bg-dark text-white">d-inline</div>
{{< /example >}}

{{< example >}}
<span class="d-block p-2 bg-primary text-white">d-block</span>
<span class="d-block p-2 bg-dark text-white">d-block</span>
{{< /example >}}

## Hiding elements

For faster mobile-friendly development, use responsive display classes for showing and hiding elements by device. Avoid creating entirely different versions of the same site, instead hide elements responsively for each screen size.

To hide elements simply use the `.d-none` class or one of the `.d-{sm,md,lg,xl}-none` classes for any responsive screen variation.

To show an element only on a given interval of screen sizes you can combine one `.d-*-none` class with a `.d-*-*` class, for example `.d-none .d-md-block .d-xl-none` will hide the element for all screen sizes except on medium and large devices.

<table class="table">
  <thead>
    <tr>
      <th>Screen size</th>
      <th>Class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hidden on all</td>
      <td><code>.d-none</code></td>
    </tr>
    <tr>
      <td>Hidden only on xs</td>
      <td><code>.d-none .d-sm-block</code></td>
    </tr>
    <tr>
      <td>Hidden only on sm</td>
      <td><code>.d-sm-none .d-md-block</code></td>
    </tr>
    <tr>
      <td>Hidden only on md</td>
      <td><code>.d-md-none .d-lg-block</code></td>
    </tr>
    <tr>
      <td>Hidden only on lg</td>
      <td><code>.d-lg-none .d-xl-block</code></td>
    </tr>
    <tr>
      <td>Hidden only on xl</td>
      <td><code>.d-xl-none</code></td>
    </tr>
    <tr>
      <td>Visible on all</td>
      <td><code>.d-block</code></td>
    </tr>
    <tr>
      <td>Visible only on xs</td>
      <td><code>.d-block .d-sm-none</code></td>
    </tr>
    <tr>
      <td>Visible only on sm</td>
      <td><code>.d-none .d-sm-block .d-md-none</code></td>
    </tr>
    <tr>
      <td>Visible only on md</td>
      <td><code>.d-none .d-md-block .d-lg-none</code></td>
    </tr>
    <tr>
      <td>Visible only on lg</td>
      <td><code>.d-none .d-lg-block .d-xl-none</code></td>
    </tr>
    <tr>
      <td>Visible only on xl</td>
      <td><code>.d-none .d-xl-block</code></td>
    </tr>
  </tbody>
</table>

{{< example >}}
<div class="d-lg-none">hide on lg and wider screens</div>
<div class="d-none d-lg-block">hide on screens smaller than lg</div>
{{< /example >}}

## Display in print

Change the `display` value of elements when printing with our print display utility classes. Includes support for the same `display` values as our responsive `.d-*` utilities.

- `.d-print-none`
- `.d-print-inline`
- `.d-print-inline-block`
- `.d-print-block`
- `.d-print-table`
- `.d-print-table-row`
- `.d-print-table-cell`
- `.d-print-flex`
- `.d-print-inline-flex`

The print and display classes can be combined.

{{< example >}}
<div class="d-print-none">Screen Only (Hide on print only)</div>
<div class="d-none d-print-block">Print Only (Hide on screen only)</div>
<div class="d-none d-lg-block d-print-block">Hide up to large on screen, but always show on print</div>
{{< /example >}}
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
## _site_content_docs_4_3_about_brand_md
```---
layout: docs
title: Brand guidelines
description: Documentation and examples for Bootstrap's logo and brand usage guidelines.
group: about
toc: true
---

Have a need for Bootstrap's brand resources? Great! We have only a few guidelines we follow, and in turn ask you to follow as well. These guidelines were inspired by MailChimp's [Brand Assets](https://mailchimp.com/about/brand-assets/).

## Mark and logo

Use either the Bootstrap mark (a capital **B**) or the standard logo (just **Bootstrap**). It should always appear in San Francisco Display Semibold. **Do not use the Twitter bird** in association with Bootstrap.

<div class="bd-brand-logos d-sm-flex text-center bg-light rounded overflow-hidden w-100 mb-3">
  <div class="bd-brand-item">
    <img src="/docs/{{< param docs_version >}}/assets/brand/bootstrap-solid.svg" alt="Bootstrap" width="144" height="144">
  </div>
  <div class="bd-brand-item inverse">
    <img src="/docs/{{< param docs_version >}}/assets/brand/bootstrap-outline.svg" alt="Bootstrap" width="144" height="144">
  </div>
</div>
<div class="bd-brand-logos d-sm-flex text-center bg-light rounded overflow-hidden w-100 mb-3">
  <div class="bd-brand-item">
    <span class="h1">Bootstrap</span>
  </div>
  <div class="bd-brand-item inverse">
    <span class="h1">Bootstrap</span>
  </div>
</div>

## Download mark

Download the Bootstrap mark in one of three styles, each available as an SVG file. **Click to download the logos**.

<div class="bd-brand-logos d-sm-flex text-center bg-light rounded overflow-hidden w-100 mb-3">
  <a href="/docs/{{< param docs_version >}}/assets/brand/bootstrap-solid.svg" download class="bd-brand-item" title="Download solid logo">
    <img src="/docs/{{< param docs_version >}}/assets/brand/bootstrap-solid.svg" alt="Bootstrap" width="144" height="144">
  </a>
  <a href="/docs/{{< param docs_version >}}/assets/brand/bootstrap-outline.svg" download class="bd-brand-item inverse" title="Download outlined logo">
    <img src="/docs/{{< param docs_version >}}/assets/brand/bootstrap-outline.svg" alt="Bootstrap" width="144" height="144">
  </a>
  <a href="/docs/{{< param docs_version >}}/assets/brand/bootstrap-punchout.svg" download class="bd-brand-item inverse" title="Download inverted logo">
    <img src="/docs/{{< param docs_version >}}/assets/brand/bootstrap-punchout.svg" alt="Bootstrap" width="144" height="144">
  </a>
</div>

## Name

The project and framework should always be referred to as **Bootstrap**. No Twitter before it, no capital _s_, and no abbreviations except for one, a capital **B**.

<div class="bd-brand-logos d-sm-flex text-center bg-light rounded overflow-hidden w-100 mb-3">
  <div class="bd-brand-item">
    <span class="h3">Bootstrap</span>
    <strong class="text-success">Right</strong>
  </div>
  <div class="bd-brand-item">
    <span class="h3 text-muted">BootStrap</span>
    <strong class="text-warning">Wrong</strong>
  </div>
  <div class="bd-brand-item">
    <span class="h3 text-muted">Twitter Bootstrap</span>
    <strong class="text-warning">Wrong</strong>
  </div>
</div>

## Colors

Our docs and branding use a handful of primary colors to differentiate what *is* Bootstrap from what *is in* Bootstrap. In other words, if it's purple, it's representative of Bootstrap.

<div class="color-swatches">
  <div class="color-swatch bd-purple"></div>
  <div class="color-swatch bd-purple-light"></div>
  <div class="color-swatch bd-purple-lighter"></div>
  <div class="color-swatch bd-gray"></div>
</div>
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
## _site_content_docs_4_3_forms_file_md
```---
layout: docs
title: File browser
description: Use our custom file inputs for consistent cross-browser styling, built-in customization, and lightweight JavaScript.
group: forms
toc: false
---

{{< callout info >}}
The recommended plugin to animate custom file input: [bs-custom-file-input](https://www.npmjs.com/package/bs-custom-file-input), that's what we are using currently here in our docs.
{{< /callout >}}

The file input is the most gnarly of the bunch and requires additional JavaScript if you'd like to hook them up with functional *Choose file...* and selected file name text.

{{< example >}}
<div class="form-file">
  <input type="file" class="form-file-input" id="customFile">
  <label class="form-file-label" for="customFile">
    <span class="form-file-text">Choose file...</span>
    <span class="form-file-button">Browse</span>
  </label>
</div>
{{< /example >}}

Add the `disabled` attribute to the `<input>` and the custom markup will be updated to appear disabled.

{{< example >}}
<div class="form-file">
  <input type="file" class="form-file-input" id="customFileDisabled" disabled>
  <label class="form-file-label" for="customFileDisabled">
    <span class="form-file-text">Choose file...</span>
    <span class="form-file-button">Browse</span>
  </label>
</div>
{{< /example >}}

Longer placeholder text is truncated and an ellipsis is added when there's not enough space.

{{< example >}}
<div class="form-file">
  <input type="file" class="form-file-input" id="customFileLong">
  <label class="form-file-label" for="customFileLong">
    <span class="form-file-text">Lorem ipsum posuere consectetur est at lobortis nulla vitae elit libero a pharetra augue fusce dapibus tellus ac cursus commodo tortor mauris condimentum nibh ut fermentum massa justo sit amet risus cras mattis consectetur purus sit amet fermentum</span>
    <span class="form-file-button">Browse</span>
  </label>
</div>
{{< /example >}}

We hide the default file `<input>` via `opacity` and instead style the `<label>`, and declare a `width` and `height` on the `<input>` for proper spacing for surrounding content.
```
# Inline
## _js_dist_dom_data_js
### Line 77-82
```
  };

  return Data;

}));
//# sourceMappingURL=data.js.map
```

## _build_build_plugins_js
### Line 12-23
```
const babel = require('rollup-plugin-babel')
const banner = require('./banner.js')

const plugins = [
  babel({
    // Only transpile our source code
    exclude: 'node_modules/**',
    // Include only required helpers
    externalHelpersWhitelist: [
      'defineProperties',
      'createClass',
      'inheritsLoose',
```

## _package_js
### Line 1-5
```
// package metadata file for Meteor.js

Package.describe({
  name: 'twbs:bootstrap', // https://atmospherejs.com/twbs/bootstrap
  summary: 'The most popular front-end framework for developing responsive, mobile first projects on the web.',
```

## _js_dist_dom_selector_engine_js
### Line 97-102
```
  };

  return SelectorEngine;

}));
//# sourceMappingURL=selector-engine.js.map
```

## _js_src_dom_event_handler_js
### Line 92-101
```

  return eventRegistry[uid]
}

function fixEvent(event, element) {
  // Add which for key events
  if (event.which === null && keyEventRegex.test(event.type)) {
    event.which = event.charCode === null ? event.keyCode : event.charCode
  }

```
### Line 129-138
```
          return fn.apply(target, [event])
        }
      }
    }

    // To please ESLint
    return null
  }
}

```
### Line 152-161
```

function normalizeParams(originalTypeEvent, handler, delegationFn) {
  const delegation = typeof handler === 'string'
  const originalHandler = delegation ? delegationFn : handler

  // allow to get the native events from namespaced events ('click.bs.button' --> 'click')
  let typeEvent = originalTypeEvent.replace(stripNameRegex, '')
  const custom = customEvents[typeEvent]

  if (custom) {
```
### Line 248-257
```
    const inNamespace = typeEvent !== originalTypeEvent
    const events = getEvent(element)
    const isNamespace = originalTypeEvent.charAt(0) === '.'

    if (typeof originalHandler !== 'undefined') {
      // Simplest case: handler is passed, remove that listener ONLY.
      if (!events || !events[typeEvent]) {
        return
      }

```
### Line 311-320
```
        bubbles,
        cancelable: true
      })
    }

    // merge custom informations in our event
    if (typeof args !== 'undefined') {
      Object.keys(args)
        .forEach(key => {
          Object.defineProperty(evt, key, {
```

## _dist_js_bootstrap_esm_js
### Line 502-511
```
  eventRegistry[uid] = eventRegistry[uid] || {};
  return eventRegistry[uid];
}

function fixEvent(event, element) {
  // Add which for key events
  if (event.which === null && keyEventRegex.test(event.type)) {
    event.which = event.charCode === null ? event.keyCode : event.charCode;
  }

```
### Line 660-669
```
    var inNamespace = typeEvent !== originalTypeEvent;
    var events = getEvent(element);
    var isNamespace = originalTypeEvent.charAt(0) === '.';

    if (typeof originalHandler !== 'undefined') {
      // Simplest case: handler is passed, remove that listener ONLY.
      if (!events || !events[typeEvent]) {
        return;
      }

```
### Line 868-877
```
  } // Getters


  var _proto = Alert.prototype;

  // Public
  _proto.close = function close(element) {
    var rootElement = this._element;

    if (element) {
```
### Line 1043-1052
```
  } // Getters


  var _proto = Button.prototype;

  // Public
  _proto.toggle = function toggle() {
    var triggerChangeEvent = true;
    var addAriaPressed = true;
    var rootElement = SelectorEngine.closest(this._element, Selector$1.DATA_TOGGLE);
```
### Line 1369-1387
```
  } // Getters


  var _proto = Carousel.prototype;

  // Public
  _proto.next = function next() {
    if (!this._isSliding) {
      this._slide(Direction.NEXT);
    }
  };

  _proto.nextWhenVisible = function nextWhenVisible() {
    // Don't call next when the page isn't visible
    // or the carousel or its parent isn't visible
    if (!document.hidden && isVisible(this._element)) {
      this.next();
    }
  };
```
### Line 1523-1532
```
        _this3.touchStartX = event.touches[0].clientX;
      }
    };

    var move = function move(event) {
      // ensure swiping with one touch and not pinching
      if (event.touches && event.touches.length > 1) {
        _this3.touchDeltaX = 0;
      } else {
        _this3.touchDeltaX = event.touches[0].clientX - _this3.touchStartX;
```
### Line 1539-1554
```
      }

      _this3._handleSwipe();

      if (_this3._config.pause === 'hover') {
        // If it's a touch-enabled device, mouseenter/leave are fired as
        // part of the mouse compatibility events on first tap - the carousel
        // would stop cycling until user tapped out of it;
        // here, we listen for touchend, explicitly pause the carousel
        // (as if it's the second time we tap on it, mouseenter compat event
        // is NOT fired) and after a timeout (to allow for mouse compatibility
        // events to fire) we explicitly restart cycling
        _this3.pause();

        if (_this3.touchTimeout) {
          clearTimeout(_this3.touchTimeout);
```
### Line 1696-1705
```
    if (slideEvent.defaultPrevented) {
      return;
    }

    if (!activeElement || !nextElement) {
      // Some weirdness is happening, so we bail
      return;
    }

    this._isSliding = true;
```
### Line 1958-1967
```
  } // Getters


  var _proto = Collapse.prototype;

  // Public
  _proto.toggle = function toggle() {
    if (this._element.classList.contains(ClassName$3.SHOW)) {
      this.hide();
    } else {
```
### Line 2151-2160
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
### Line 2241-2250
```
 * ------------------------------------------------------------------------
 */


EventHandler.on(document, Event$4.CLICK_DATA_API, Selector$3.DATA_TOGGLE, function (event) {
  // preventDefault only for <a> elements (which change the URL) not inside the collapsible element
  if (event.target.tagName === 'A') {
    event.preventDefault();
  }

```
### Line 2254-2263
```
  selectorElements.forEach(function (element) {
    var data = Data.getData(element, DATA_KEY$3);
    var config;

    if (data) {
      // update parent attribute
      if (data._parent === null && typeof triggerData.parent === 'string') {
        data._config.parent = triggerData.parent;
        data._parent = data._getParent();
      }
```
### Line 2389-2398
```
  } // Getters


  var _proto = Dropdown.prototype;

  // Public
  _proto.toggle = function toggle() {
    if (this._element.disabled || this._element.classList.contains(ClassName$4.DISABLED)) {
      return;
    }
```
### Line 2438-2459
```

        if (typeof this._config.reference.jquery !== 'undefined') {
          referenceElement = this._config.reference[0];
        }
      } // If boundary is not `scrollParent`, then set position to `static`
      // to allow the menu to "escape" the scroll parent's boundaries
      // https://github.com/twbs/bootstrap/issues/24251


      if (this._config.boundary !== 'scrollParent') {
        parent.classList.add(ClassName$4.POSITION_STATIC);
      }

      this._popper = new Popper(referenceElement, this._menu, this._getPopperConfig());
    } // If this is a touch-enabled device we add extra
    // empty mouseover listeners to the body's immediate children;
    // only needed because of broken event delegation on iOS
    // https://www.quirksmode.org/blog/archives/2014/02/mouse_event_bub.html


    if ('ontouchstart' in document.documentElement && !makeArray(SelectorEngine.closest(parent, Selector$4.NAVBAR_NAV)).length) {
      makeArray(document.body.children).forEach(function (elem) {
```
### Line 2663-2672
```
      var hideEvent = EventHandler.trigger(parent, Event$5.HIDE, relatedTarget);

      if (hideEvent.defaultPrevented) {
        continue;
      } // If this is a touch-enabled device we remove the extra
      // empty mouseover listeners we added for iOS support


      if ('ontouchstart' in document.documentElement) {
        makeArray(document.body.children).forEach(function (elem) {
```
### Line 2689-2704
```
  Dropdown.getParentFromElement = function getParentFromElement(element) {
    return getElementFromSelector(element) || element.parentNode;
  };

  Dropdown.dataApiKeydownHandler = function dataApiKeydownHandler(event) {
    // If not input/textarea:
    //  - And not a key in REGEXP_KEYDOWN => not a dropdown command
    // If input/textarea:
    //  - If space key => not a dropdown command
    //  - If key is other than escape
    //    - If key is not up or down => not a dropdown command
    //    - If trigger inside the menu => not a dropdown command
    if (/input|textarea/i.test(event.target.tagName) ? event.which === SPACE_KEYCODE || event.which !== ESCAPE_KEYCODE && (event.which !== ARROW_DOWN_KEYCODE && event.which !== ARROW_UP_KEYCODE || SelectorEngine.closest(event.target, Selector$4.MENU)) : !REGEXP_KEYDOWN.test(event.which)) {
      return;
    }

```
### Line 2728-2742
```
    }

    var index = items.indexOf(event.target);

    if (event.which === ARROW_UP_KEYCODE && index > 0) {
      // Up
      index--;
    }

    if (event.which === ARROW_DOWN_KEYCODE && index < items.length - 1) {
      // Down
      index++;
    }

    if (index < 0) {
```
### Line 2886-2895
```
  } // Getters


  var _proto = Modal.prototype;

  // Public
  _proto.toggle = function toggle(relatedTarget) {
    return this._isShown ? this.hide() : this.show(relatedTarget);
  };

```
### Line 3027-3036
```
    var transition = this._element.classList.contains(ClassName$5.FADE);

    var modalBody = SelectorEngine.findOne(Selector$5.MODAL_BODY, this._dialog);

    if (!this._element.parentNode || this._element.parentNode.nodeType !== Node.ELEMENT_NODE) {
      // Don't move modal's DOM position
      document.body.appendChild(this._element);
    }

    this._element.style.display = 'block';
```
### Line 3207-3217
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
### Line 3238-3249
```

  _proto._setScrollbar = function _setScrollbar() {
    var _this9 = this;

    if (this._isBodyOverflowing) {
      // Note: DOMNode.style.paddingRight returns the actual value or '' if not set
      //   while $(DOMNode).css('padding-right') returns the calculated value or 0 if not set
      // Adjust fixed content padding
      makeArray(SelectorEngine.find(Selector$5.FIXED_CONTENT)).forEach(function (element) {
        var actualPadding = element.style.paddingRight;
        var calculatedPadding = window.getComputedStyle(element)['padding-right'];
        Manipulator.setDataAttribute(element, 'padding-right', actualPadding);
```
### Line 3265-3274
```

    document.body.classList.add(ClassName$5.OPEN);
  };

  _proto._resetScrollbar = function _resetScrollbar() {
    // Restore fixed content padding
    makeArray(SelectorEngine.find(Selector$5.FIXED_CONTENT)).forEach(function (element) {
      var padding = Manipulator.getDataAttribute(element, 'padding-right');

      if (typeof padding !== 'undefined') {
```
### Line 3295-3304
```
      document.body.style.paddingRight = padding;
    }
  };

  _proto._getScrollbarWidth = function _getScrollbarWidth() {
    // thx d.walsh
    var scrollDiv = document.createElement('div');
    scrollDiv.className = ClassName$5.SCROLLBAR_MEASURER;
    document.body.appendChild(scrollDiv);
    var scrollbarWidth = scrollDiv.getBoundingClientRect().width - scrollDiv.clientWidth;
```
### Line 3363-3372
```
    event.preventDefault();
  }

  EventHandler.one(target, Event$6.SHOW, function (showEvent) {
    if (showEvent.defaultPrevented) {
      // only register focus restorer if modal will actually get shown
      return;
    }

    EventHandler.one(target, Event$6.HIDDEN, function () {
```
### Line 3452-3461
```

  return false;
};

var DefaultWhitelist = {
  // Global attributes allowed on any supplied element below.
  '*': ['class', 'dir', 'id', 'lang', 'role', ARIA_ATTRIBUTE_PATTERN],
  a: ['target', 'href', 'title', 'rel'],
  area: [],
  b: [],
```
### Line 3643-3652
```
  } // Getters


  var _proto = Tooltip.prototype;

  // Public
  _proto.enable = function enable() {
    this._isEnabled = true;
  };

```
### Line 3756-3767
```
      }

      EventHandler.trigger(this.element, this.constructor.Event.INSERTED);
      this._popper = new Popper(this.element, tip, this._getPopperConfig(attachment));
      tip.classList.add(ClassName$6.SHOW); // If this is a touch-enabled device we add extra
      // empty mouseover listeners to the body's immediate children;
      // only needed because of broken event delegation on iOS
      // https://www.quirksmode.org/blog/archives/2014/02/mouse_event_bub.html

      if ('ontouchstart' in document.documentElement) {
        makeArray(document.body.children).forEach(function (element) {
          EventHandler.on(element, 'mouseover', noop());
```
### Line 3816-3825
```
    if (hideEvent.defaultPrevented) {
      return;
    }

    tip.classList.remove(ClassName$6.SHOW); // If this is a touch-enabled device we remove the extra
    // empty mouseover listeners we added for iOS support

    if ('ontouchstart' in document.documentElement) {
      makeArray(document.body.children).forEach(function (element) {
        return EventHandler.off(element, 'mouseover', noop);
```
### Line 4342-4351
```
    return _Tooltip.apply(this, arguments) || this;
  }

  var _proto = Popover.prototype;

  // Overrides
  _proto.isWithContent = function isWithContent() {
    return this.getTitle() || this._getContent();
  };

```
### Line 4417-4426
```
    return Data.getData(element, DATA_KEY$7);
  };

  _createClass(Popover, null, [{
    key: "VERSION",
    // Getters
    get: function get() {
      return VERSION$7;
    }
  }, {
```
### Line 4552-4561
```
  } // Getters


  var _proto = ScrollSpy.prototype;

  // Public
  _proto.refresh = function refresh() {
    var _this2 = this;

    var autoMethod = this._scrollElement === this._scrollElement.window ? OffsetMethod.OFFSET : OffsetMethod.POSITION;
```
### Line 4690-4703
```

    if (link.classList.contains(ClassName$8.DROPDOWN_ITEM)) {
      SelectorEngine.findOne(Selector$8.DROPDOWN_TOGGLE, SelectorEngine.closest(link, Selector$8.DROPDOWN)).classList.add(ClassName$8.ACTIVE);
      link.classList.add(ClassName$8.ACTIVE);
    } else {
      // Set triggered link as active
      link.classList.add(ClassName$8.ACTIVE);
      SelectorEngine.parents(link, Selector$8.NAV_LIST_GROUP).forEach(function (listGroup) {
        // Set triggered links parents as active
        // With both <ul> and <nav> markup a parent is the previous sibling of any nav ancestor
        SelectorEngine.prev(listGroup, Selector$8.NAV_LINKS + ", " + Selector$8.LIST_ITEMS).forEach(function (item) {
          return item.classList.add(ClassName$8.ACTIVE);
        }); // Handle special case when .nav-link is inside .nav-item

```
### Line 4842-4851
```
  } // Getters


  var _proto = Tab.prototype;

  // Public
  _proto.show = function show() {
    var _this = this;

    if (this._element.parentNode && this._element.parentNode.nodeType === Node.ELEMENT_NODE && this._element.classList.contains(ClassName$9.ACTIVE) || this._element.classList.contains(ClassName$9.DISABLED)) {
```
### Line 5083-5092
```
  } // Getters


  var _proto = Toast.prototype;

  // Public
  _proto.show = function show() {
    var _this = this;

    var showEvent = EventHandler.trigger(this._element, Event$b.SHOW);
```
### Line 5252-5257
```
    return Toast.jQueryInterface;
  };
}

export { Alert, Button, Carousel, Collapse, Dropdown, Modal, Popover, ScrollSpy, Tab, Toast, Tooltip };
//# sourceMappingURL=bootstrap.esm.js.map
```

## _js_src_dom_selector_engine_js

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

## _js_tests_browsers_js

## _js_dist_tab_js
### Line 173-182
```
    } // Getters


    var _proto = Tab.prototype;

    // Public
    _proto.show = function show() {
      var _this = this;

      if (this._element.parentNode && this._element.parentNode.nodeType === Node.ELEMENT_NODE && this._element.classList.contains(ClassName.ACTIVE) || this._element.classList.contains(ClassName.DISABLED)) {
```
### Line 359-364
```
  }

  return Tab;

}));
//# sourceMappingURL=tab.js.map
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

## _js_dist_dom_manipulator_js
### Line 139-144
```
  };

  return Manipulator;

}));
//# sourceMappingURL=manipulator.js.map
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

## _js_tests_integration_bundle_js

## _js_src_tab_js
### Line 67-82
```
    this._element = element

    Data.setData(this._element, DATA_KEY, this)
  }

  // Getters

  static get VERSION() {
    return VERSION
  }

  // Public

  show() {
    if ((this._element.parentNode &&
      this._element.parentNode.nodeType === Node.ELEMENT_NODE &&
```
### Line 136-145
```
  dispose() {
    Data.removeData(this._element, DATA_KEY)
    this._element = null
  }

  // Private

  _activate(element, container, callback) {
    const activeElements = container && (container.nodeName === 'UL' || container.nodeName === 'OL') ?
      SelectorEngine.find(Selector.ACTIVE_UL, container) :
```
### Line 206-215
```
    if (callback) {
      callback()
    }
  }

  // Static

  static jQueryInterface(config) {
    return this.each(function () {
      const data = Data.getData(this, DATA_KEY) || new Tab(this)
```

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

## _dist_js_bootstrap_bundle_js
### Line 506-515
```
    eventRegistry[uid] = eventRegistry[uid] || {};
    return eventRegistry[uid];
  }

  function fixEvent(event, element) {
    // Add which for key events
    if (event.which === null && keyEventRegex.test(event.type)) {
      event.which = event.charCode === null ? event.keyCode : event.charCode;
    }

```
### Line 664-673
```
      var inNamespace = typeEvent !== originalTypeEvent;
      var events = getEvent(element);
      var isNamespace = originalTypeEvent.charAt(0) === '.';

      if (typeof originalHandler !== 'undefined') {
        // Simplest case: handler is passed, remove that listener ONLY.
        if (!events || !events[typeEvent]) {
          return;
        }

```
### Line 872-881
```
    } // Getters


    var _proto = Alert.prototype;

    // Public
    _proto.close = function close(element) {
      var rootElement = this._element;

      if (element) {
```
### Line 1047-1056
```
    } // Getters


    var _proto = Button.prototype;

    // Public
    _proto.toggle = function toggle() {
      var triggerChangeEvent = true;
      var addAriaPressed = true;
      var rootElement = SelectorEngine.closest(this._element, Selector$1.DATA_TOGGLE);
```
### Line 1373-1391
```
    } // Getters


    var _proto = Carousel.prototype;

    // Public
    _proto.next = function next() {
      if (!this._isSliding) {
        this._slide(Direction.NEXT);
      }
    };

    _proto.nextWhenVisible = function nextWhenVisible() {
      // Don't call next when the page isn't visible
      // or the carousel or its parent isn't visible
      if (!document.hidden && isVisible(this._element)) {
        this.next();
      }
    };
```
### Line 1527-1536
```
          _this3.touchStartX = event.touches[0].clientX;
        }
      };

      var move = function move(event) {
        // ensure swiping with one touch and not pinching
        if (event.touches && event.touches.length > 1) {
          _this3.touchDeltaX = 0;
        } else {
          _this3.touchDeltaX = event.touches[0].clientX - _this3.touchStartX;
```
### Line 1543-1558
```
        }

        _this3._handleSwipe();

        if (_this3._config.pause === 'hover') {
          // If it's a touch-enabled device, mouseenter/leave are fired as
          // part of the mouse compatibility events on first tap - the carousel
          // would stop cycling until user tapped out of it;
          // here, we listen for touchend, explicitly pause the carousel
          // (as if it's the second time we tap on it, mouseenter compat event
          // is NOT fired) and after a timeout (to allow for mouse compatibility
          // events to fire) we explicitly restart cycling
          _this3.pause();

          if (_this3.touchTimeout) {
            clearTimeout(_this3.touchTimeout);
```
### Line 1700-1709
```
      if (slideEvent.defaultPrevented) {
        return;
      }

      if (!activeElement || !nextElement) {
        // Some weirdness is happening, so we bail
        return;
      }

      this._isSliding = true;
```
### Line 1962-1971
```
    } // Getters


    var _proto = Collapse.prototype;

    // Public
    _proto.toggle = function toggle() {
      if (this._element.classList.contains(ClassName$3.SHOW)) {
        this.hide();
      } else {
```
### Line 2155-2164
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
### Line 2245-2254
```
   * ------------------------------------------------------------------------
   */


  EventHandler.on(document, Event$4.CLICK_DATA_API, Selector$3.DATA_TOGGLE, function (event) {
    // preventDefault only for <a> elements (which change the URL) not inside the collapsible element
    if (event.target.tagName === 'A') {
      event.preventDefault();
    }

```
### Line 2258-2267
```
    selectorElements.forEach(function (element) {
      var data = Data.getData(element, DATA_KEY$3);
      var config;

      if (data) {
        // update parent attribute
        if (data._parent === null && typeof triggerData.parent === 'string') {
          data._config.parent = triggerData.parent;
          data._parent = data._getParent();
        }
```
### Line 2391-2400
```
   */
  function getStyleComputedProperty(element, property) {
    if (element.nodeType !== 1) {
      return [];
    }
    // NOTE: 1 DOM access here
    var window = element.ownerDocument.defaultView;
    var css = window.getComputedStyle(element, null);
    return property ? css[property] : css;
  }
```
### Line 2419-2428
```
   * @memberof Popper.Utils
   * @argument {Element} element
   * @returns {Element} scroll parent
   */
  function getScrollParent(element) {
    // Return body, `getScroll` will take care to get the correct `scrollTop` from it
    if (!element) {
      return document.body;
    }

```
### Line 2432-2441
```
        return element.ownerDocument.body;
      case '#document':
        return element.body;
    }

    // Firefox want us to check `-x` and `-y` variations as well

    var _getStyleComputedProp = getStyleComputedProperty(element),
        overflow = _getStyleComputedProp.overflow,
        overflowX = _getStyleComputedProp.overflowX,
```
### Line 2480-2491
```
      return document.documentElement;
    }

    var noOffsetParent = isIE(10) ? document.body : null;

    // NOTE: 1 DOM access here
    var offsetParent = element.offsetParent || null;
    // Skip hidden elements which don't have an offsetParent
    while (offsetParent === noOffsetParent && element.nextElementSibling) {
      offsetParent = (element = element.nextElementSibling).offsetParent;
    }

```
### Line 2493-2503
```

    if (!nodeName || nodeName === 'BODY' || nodeName === 'HTML') {
      return element ? element.ownerDocument.documentElement : document.documentElement;
    }

    // .offsetParent will return the closest TH, TD or TABLE in case
    // no offsetParent is present, I hate this job...
    if (['TH', 'TD', 'TABLE'].indexOf(offsetParent.nodeName) !== -1 && getStyleComputedProperty(offsetParent, 'position') === 'static') {
      return getOffsetParent(offsetParent);
    }

```
### Line 2535-2560
```
   * @argument {Element} element1
   * @argument {Element} element2
   * @returns {Element} common offset parent
   */
  function findCommonOffsetParent(element1, element2) {
    // This check is needed to avoid errors in case one of the elements isn't defined for any reason
    if (!element1 || !element1.nodeType || !element2 || !element2.nodeType) {
      return document.documentElement;
    }

    // Here we make sure to give as "start" the element that comes first in the DOM
    var order = element1.compareDocumentPosition(element2) & Node.DOCUMENT_POSITION_FOLLOWING;
    var start = order ? element1 : element2;
    var end = order ? element2 : element1;

    // Get common ancestor container
    var range = document.createRange();
    range.setStart(start, 0);
    range.setEnd(end, 0);
    var commonAncestorContainer = range.commonAncestorContainer;

    // Both nodes are inside #document

    if (element1 !== commonAncestorContainer && element2 !== commonAncestorContainer || start.contains(end)) {
      if (isOffsetContainer(commonAncestorContainer)) {
        return commonAncestorContainer;
```
### Line 2561-2570
```
      }

      return getOffsetParent(commonAncestorContainer);
    }

    // one of the nodes is inside shadowDOM, find which one
    var element1root = getRoot(element1);
    if (element1root.host) {
      return findCommonOffsetParent(element1root.host, element2);
    } else {
```
### Line 2728-2739
```
   * @return {Object} client rect
   */
  function getBoundingClientRect(element) {
    var rect = {};

    // IE10 10 FIX: Please, don't ask, the element isn't
    // considered in DOM in some circumstances...
    // This isn't reproducible in IE10 compatibility mode of IE11
    try {
      if (isIE(10)) {
        rect = element.getBoundingClientRect();
        var scrollTop = getScroll(element, 'top');
```
### Line 2752-2770
```
      top: rect.top,
      width: rect.right - rect.left,
      height: rect.bottom - rect.top
    };

    // subtract scrollbar size from sizes
    var sizes = element.nodeName === 'HTML' ? getWindowSizes(element.ownerDocument) : {};
    var width = sizes.width || element.clientWidth || result.right - result.left;
    var height = sizes.height || element.clientHeight || result.bottom - result.top;

    var horizScrollbar = element.offsetWidth - width;
    var vertScrollbar = element.offsetHeight - height;

    // if an hypothetical scrollbar is detected, we must be sure it's not a `border`
    // we make this check conditional for performance reasons
    if (horizScrollbar || vertScrollbar) {
      var styles = getStyleComputedProperty(element);
      horizScrollbar -= getBordersSize(styles, 'x');
      vertScrollbar -= getBordersSize(styles, 'y');
```
### Line 2787-2796
```

    var styles = getStyleComputedProperty(parent);
    var borderTopWidth = parseFloat(styles.borderTopWidth, 10);
    var borderLeftWidth = parseFloat(styles.borderLeftWidth, 10);

    // In cases where the parent is fixed, we must ignore negative scroll in offset calc
    if (fixedPosition && isHTML) {
      parentRect.top = Math.max(parentRect.top, 0);
      parentRect.left = Math.max(parentRect.left, 0);
    }
```
### Line 2801-2813
```
      height: childrenRect.height
    });
    offsets.marginTop = 0;
    offsets.marginLeft = 0;

    // Subtract margins of documentElement in case it's being used as parent
    // we do this only on HTML because it's the only element that behaves
    // differently when margins are applied to it. The margins are included in
    // the box of the documentElement, in the other cases not.
    if (!isIE10 && isHTML) {
      var marginTop = parseFloat(styles.marginTop, 10);
      var marginLeft = parseFloat(styles.marginLeft, 10);

```
### Line 2814-2823
```
      offsets.top -= borderTopWidth - marginTop;
      offsets.bottom -= borderTopWidth - marginTop;
      offsets.left -= borderLeftWidth - marginLeft;
      offsets.right -= borderLeftWidth - marginLeft;

      // Attach marginTop and marginLeft because in some circumstances we may need them
      offsets.marginTop = marginTop;
      offsets.marginLeft = marginLeft;
    }

```
### Line 2879-2888
```
   * @argument {Element} element
   * @returns {Element} first transformed parent or documentElement
   */

  function getFixedPositionOffsetParent(element) {
    // This check is needed to avoid errors in case one of the elements isn't defined for any reason
    if (!element || !element.parentElement || isIE()) {
      return document.documentElement;
    }
    var el = element.parentElement;
```
### Line 2904-2922
```
   * @returns {Object} Coordinates of the boundaries
   */
  function getBoundaries(popper, reference, padding, boundariesElement) {
    var fixedPosition = arguments.length > 4 && arguments[4] !== undefined ? arguments[4] : false;

    // NOTE: 1 DOM access here

    var boundaries = { top: 0, left: 0 };
    var offsetParent = fixedPosition ? getFixedPositionOffsetParent(popper) : findCommonOffsetParent(popper, reference);

    // Handle viewport case
    if (boundariesElement === 'viewport') {
      boundaries = getViewportOffsetRectRelativeToArtbitraryNode(offsetParent, fixedPosition);
    } else {
      // Handle other cases based on DOM element used as boundaries
      var boundariesNode = void 0;
      if (boundariesElement === 'scrollParent') {
        boundariesNode = getScrollParent(getParentNode(reference));
        if (boundariesNode.nodeName === 'BODY') {
```
### Line 2928-2937
```
        boundariesNode = boundariesElement;
      }

      var offsets = getOffsetRectRelativeToArbitraryNode(boundariesNode, offsetParent, fixedPosition);

      // In case of HTML, we need a different computation
      if (boundariesNode.nodeName === 'HTML' && !isFixed(offsetParent)) {
        var _getWindowSizes = getWindowSizes(popper.ownerDocument),
            height = _getWindowSizes.height,
            width = _getWindowSizes.width;
```
### Line 2939-2953
```
        boundaries.top += offsets.top - offsets.marginTop;
        boundaries.bottom = height + offsets.top;
        boundaries.left += offsets.left - offsets.marginLeft;
        boundaries.right = width + offsets.left;
      } else {
        // for all the other DOM elements, this one is good
        boundaries = offsets;
      }
    }

    // Add paddings
    padding = padding || 0;
    var isPaddingNumber = typeof padding === 'number';
    boundaries.left += isPaddingNumber ? padding : padding.left || 0;
    boundaries.top += isPaddingNumber ? padding : padding.top || 0;
```
### Line 3085-3103
```
   * @returns {Object} popperOffsets - An object containing the offsets which will be applied to the popper
   */
  function getPopperOffsets(popper, referenceOffsets, placement) {
    placement = placement.split('-')[0];

    // Get popper node sizes
    var popperRect = getOuterSizes(popper);

    // Add position, width and height to our offsets object
    var popperOffsets = {
      width: popperRect.width,
      height: popperRect.height
    };

    // depending by the popper placement we have to compute its offsets slightly differently
    var isHoriz = ['right', 'left'].indexOf(placement) !== -1;
    var mainSide = isHoriz ? 'top' : 'left';
    var secondarySide = isHoriz ? 'left' : 'top';
    var measurement = isHoriz ? 'height' : 'width';
```
### Line 3121-3135
```
   * @argument prop
   * @argument value
   * @returns index or -1
   */
  function find$1(arr, check) {
    // use native find if supported
    if (Array.prototype.find) {
      return arr.find(check);
    }

    // use `filter` to obtain the same behavior of `find`
    return arr.filter(check)[0];
  }

  /**
```
### Line 3140-3156
```
   * @argument prop
   * @argument value
   * @returns index or -1
   */
  function findIndex(arr, prop, value) {
    // use native findIndex if supported
    if (Array.prototype.findIndex) {
      return arr.findIndex(function (cur) {
        return cur[prop] === value;
      });
    }

    // use `find` + `indexOf` if `findIndex` isn't supported
    var match = find$1(arr, function (obj) {
      return obj[prop] === value;
    });
    return arr.indexOf(match);
```
### Line 3169-3185
```
  function runModifiers(modifiers, data, ends) {
    var modifiersToRun = ends === undefined ? modifiers : modifiers.slice(0, findIndex(modifiers, 'name', ends));

    modifiersToRun.forEach(function (modifier) {
      if (modifier['function']) {
        // eslint-disable-line dot-notation
        console.warn('`modifier.function` is deprecated, use `modifier.fn`!');
      }
      var fn = modifier['function'] || modifier.fn; // eslint-disable-line dot-notation
      if (modifier.enabled && isFunction(fn)) {
        // Add properties to offsets to make them a complete clientRect object
        // we do this before each modifier to make sure the previous one doesn't
        // mess with these values
        data.offsets.popper = getClientRect(data.offsets.popper);
        data.offsets.reference = getClientRect(data.offsets.reference);

        data = fn(data, modifier);
```
### Line 3195-3204
```
   * Prefer `scheduleUpdate` over `update` because of performance reasons.
   * @method
   * @memberof Popper
   */
  function update() {
    // if popper is destroyed, don't perform any further update
    if (this.state.isDestroyed) {
      return;
    }

```
### Line 3209-3240
```
      attributes: {},
      flipped: false,
      offsets: {}
    };

    // compute reference element offsets
    data.offsets.reference = getReferenceOffsets(this.state, this.popper, this.reference, this.options.positionFixed);

    // compute auto placement, store placement inside the data object,
    // modifiers will be able to edit `placement` if needed
    // and refer to originalPlacement to know the original value
    data.placement = computeAutoPlacement(this.options.placement, data.offsets.reference, this.popper, this.reference, this.options.modifiers.flip.boundariesElement, this.options.modifiers.flip.padding);

    // store the computed placement inside `originalPlacement`
    data.originalPlacement = data.placement;

    data.positionFixed = this.options.positionFixed;

    // compute the popper offsets
    data.offsets.popper = getPopperOffsets(this.popper, data.offsets.reference, data.placement);

    data.offsets.popper.position = this.options.positionFixed ? 'fixed' : 'absolute';

    // run the modifiers
    data = runModifiers(this.modifiers, data);

    // the first `update` will call `onCreate` callback
    // the other ones will call `onUpdate` callback
    if (!this.state.isCreated) {
      this.state.isCreated = true;
      this.options.onCreate(data);
    } else {
```
### Line 3283-3292
```
   * @memberof Popper
   */
  function destroy() {
    this.state.isDestroyed = true;

    // touch DOM only if `applyStyle` modifier is enabled
    if (isModifierEnabled(this.modifiers, 'applyStyle')) {
      this.popper.removeAttribute('x-placement');
      this.popper.style.position = '';
      this.popper.style.top = '';
```
### Line 3297-3307
```
      this.popper.style[getSupportedPropertyName('transform')] = '';
    }

    this.disableEventListeners();

    // remove the popper if user explicity asked for the deletion on destroy
    // do not use `remove` because IE11 doesn't support it
    if (this.options.removeOnDestroy) {
      this.popper.parentNode.removeChild(this.popper);
    }
    return this;
```
### Line 3333-3346
```
   * @method
   * @memberof Popper.Utils
   * @private
   */
  function setupEventListeners(reference, options, state, updateBound) {
    // Resize event listener on window
    state.updateBound = updateBound;
    getWindow(reference).addEventListener('resize', state.updateBound, { passive: true });

    // Scroll event listener on scroll parents
    var scrollElement = getScrollParent(reference);
    attachToScrollParents(scrollElement, 'scroll', state.updateBound, state.scrollParents);
    state.scrollElement = scrollElement;
    state.eventsEnabled = true;
```
### Line 3365-3382
```
   * @method
   * @memberof Popper.Utils
   * @private
   */
  function removeEventListeners(reference, state) {
    // Remove resize event listener on window
    getWindow(reference).removeEventListener('resize', state.updateBound);

    // Remove scroll event listener on scroll parents
    state.scrollParents.forEach(function (target) {
      target.removeEventListener('scroll', state.updateBound);
    });

    // Reset state
    state.updateBound = null;
    state.scrollParents = [];
    state.scrollElement = null;
    state.eventsEnabled = false;
```
### Line 3417-3426
```
   * Object with a list of properties and values which will be applied to the element
   */
  function setStyles(element, styles) {
    Object.keys(styles).forEach(function (prop) {
      var unit = '';
      // add unit if the value is numeric and is one of the following
      if (['width', 'height', 'top', 'right', 'bottom', 'left'].indexOf(prop) !== -1 && isNumeric(styles[prop])) {
        unit = 'px';
      }
      element.style[prop] = styles[prop] + unit;
```
### Line 3454-3473
```
   * @argument {Object} data.attributes - List of attribute properties - values to apply to popper element
   * @argument {Object} options - Modifiers configuration and options
   * @returns {Object} The same data object
   */
  function applyStyle(data) {
    // any property present in `data.styles` will be applied to the popper,
    // in this way we can make the 3rd party modifiers add custom styles to it
    // Be aware, modifiers could override the properties defined in the previous
    // lines of this modifier!
    setStyles(data.instance.popper, data.styles);

    // any property present in `data.attributes` will be applied to the popper,
    // they will be set as HTML attributes of the element
    setAttributes(data.instance.popper, data.attributes);

    // if arrowElement is defined and arrowStyles has some properties
    if (data.arrowElement && Object.keys(data.arrowStyles).length) {
      setStyles(data.arrowElement, data.arrowStyles);
    }

```
### Line 3483-3503
```
   * @param {HTMLElement} reference - The reference element used to position the popper
   * @param {HTMLElement} popper - The HTML element used as popper
   * @param {Object} options - Popper.js options
   */
  function applyStyleOnLoad(reference, popper, options, modifierOptions, state) {
    // compute reference element offsets
    var referenceOffsets = getReferenceOffsets(state, popper, reference, options.positionFixed);

    // compute auto placement, store placement inside the data object,
    // modifiers will be able to edit `placement` if needed
    // and refer to originalPlacement to know the original value
    var placement = computeAutoPlacement(options.placement, referenceOffsets, popper, reference, options.modifiers.flip.boundariesElement, options.modifiers.flip.padding);

    popper.setAttribute('x-placement', placement);

    // Apply `position` to popper before anything else because
    // without the position applied we can't guarantee correct computations
    setStyles(popper, { position: options.positionFixed ? 'fixed' : 'absolute' });

    return options;
  }
```
### Line 3563-3572
```
  function computeStyle(data, options) {
    var x = options.x,
        y = options.y;
    var popper = data.offsets.popper;

    // Remove this legacy support in Popper.js v2

    var legacyGpuAccelerationOption = find$1(data.instance.modifiers, function (modifier) {
      return modifier.name === 'applyStyle';
    }).gpuAcceleration;
```
### Line 3576-3585
```
    var gpuAcceleration = legacyGpuAccelerationOption !== undefined ? legacyGpuAccelerationOption : options.gpuAcceleration;

    var offsetParent = getOffsetParent(data.instance.popper);
    var offsetParentRect = getBoundingClientRect(offsetParent);

    // Styles
    var styles = {
      position: popper.position
    };

```
### Line 3586-3613
```
    var offsets = getRoundedOffsets(data, window.devicePixelRatio < 2 || !isFirefox);

    var sideA = x === 'bottom' ? 'top' : 'bottom';
    var sideB = y === 'right' ? 'left' : 'right';

    // if gpuAcceleration is set to `true` and transform is supported,
    //  we use `translate3d` to apply the position to the popper we
    // automatically use the supported prefixed version if needed
    var prefixedProperty = getSupportedPropertyName('transform');

    // now, let's make a step back and look at this code closely (wtf?)
    // If the content of the popper grows once it's been positioned, it
    // may happen that the popper gets misplaced because of the new content
    // overflowing its reference element
    // To avoid this problem, we provide two options (x and y), which allow
    // the consumer to define the offset origin.
    // If we position a popper on top of a reference element, we can set
    // `x` to `top` to make the popper grow towards its top instead of
    // its bottom.
    var left = void 0,
        top = void 0;
    if (sideA === 'bottom') {
      // when offsetParent is <html> the positioning is relative to the bottom of the screen (excluding the scrollbar)
      // and not the bottom of the html element
      if (offsetParent.nodeName === 'HTML') {
        top = -offsetParent.clientHeight + offsets.bottom;
      } else {
        top = -offsetParentRect.height + offsets.bottom;
```
### Line 3628-3650
```
      styles[prefixedProperty] = 'translate3d(' + left + 'px, ' + top + 'px, 0)';
      styles[sideA] = 0;
      styles[sideB] = 0;
      styles.willChange = 'transform';
    } else {
      // othwerise, we use the standard `top`, `left`, `bottom` and `right` properties
      var invertTop = sideA === 'bottom' ? -1 : 1;
      var invertLeft = sideB === 'right' ? -1 : 1;
      styles[sideA] = top * invertTop;
      styles[sideB] = left * invertLeft;
      styles.willChange = sideA + ', ' + sideB;
    }

    // Attributes
    var attributes = {
      'x-placement': data.placement
    };

    // Update `data` attributes, styles and arrowStyles
    data.attributes = _extends({}, attributes, data.attributes);
    data.styles = _extends({}, styles, data.styles);
    data.arrowStyles = _extends({}, data.offsets.arrow, data.arrowStyles);

```
### Line 3687-3713
```
   * @returns {Object} The data object, properly modified
   */
  function arrow(data, options) {
    var _data$offsets$arrow;

    // arrow depends on keepTogether in order to work
    if (!isModifierRequired(data.instance.modifiers, 'arrow', 'keepTogether')) {
      return data;
    }

    var arrowElement = options.element;

    // if arrowElement is a string, suppose it's a CSS selector
    if (typeof arrowElement === 'string') {
      arrowElement = data.instance.popper.querySelector(arrowElement);

      // if arrowElement is not found, don't run the modifier
      if (!arrowElement) {
        return data;
      }
    } else {
      // if the arrowElement isn't a query selector we must check that the
      // provided DOM node is child of its popper node
      if (!data.instance.popper.contains(arrowElement)) {
        console.warn('WARNING: `arrow.element` must be child of its popper element!');
        return data;
      }
```
### Line 3725-3759
```
    var side = sideCapitalized.toLowerCase();
    var altSide = isVertical ? 'left' : 'top';
    var opSide = isVertical ? 'bottom' : 'right';
    var arrowElementSize = getOuterSizes(arrowElement)[len];

    //
    // extends keepTogether behavior making sure the popper and its
    // reference have enough pixels in conjunction
    //

    // top/left side
    if (reference[opSide] - arrowElementSize < popper[side]) {
      data.offsets.popper[side] -= popper[side] - (reference[opSide] - arrowElementSize);
    }
    // bottom/right side
    if (reference[side] + arrowElementSize > popper[opSide]) {
      data.offsets.popper[side] += reference[side] + arrowElementSize - popper[opSide];
    }
    data.offsets.popper = getClientRect(data.offsets.popper);

    // compute center of the popper
    var center = reference[side] + reference[len] / 2 - arrowElementSize / 2;

    // Compute the sideValue using the updated popper offsets
    // take popper margin in account because we don't have this info available
    var css = getStyleComputedProperty(data.instance.popper);
    var popperMarginSide = parseFloat(css['margin' + sideCapitalized], 10);
    var popperBorderSide = parseFloat(css['border' + sideCapitalized + 'Width'], 10);
    var sideValue = center - data.offsets.popper[side] - popperMarginSide - popperBorderSide;

    // prevent arrowElement from being placed not contiguously to its popper
    sideValue = Math.max(Math.min(popper[len] - arrowElementSize, sideValue), 0);

    data.arrowElement = arrowElement;
    data.offsets.arrow = (_data$offsets$arrow = {}, defineProperty(_data$offsets$arrow, side, Math.round(sideValue)), defineProperty(_data$offsets$arrow, altSide, ''), _data$offsets$arrow);
```
### Line 3808-3817
```
   * @method placements
   * @memberof Popper
   */
  var placements = ['auto-start', 'auto', 'auto-end', 'top-start', 'top', 'top-end', 'right-start', 'right', 'right-end', 'bottom-end', 'bottom', 'bottom-start', 'left-end', 'left', 'left-start'];

  // Get rid of `auto` `auto-start` and `auto-end`
  var validPlacements = placements.slice(3);

  /**
   * Given an initial placement, returns all the subsequent placements
```
### Line 3843-3858
```
   * @argument {Object} data - The data object generated by update method
   * @argument {Object} options - Modifiers configuration and options
   * @returns {Object} The data object, properly modified
   */
  function flip(data, options) {
    // if `inner` modifier is enabled, we can't use the `flip` modifier
    if (isModifierEnabled(data.instance.modifiers, 'inner')) {
      return data;
    }

    if (data.flipped && data.placement === data.originalPlacement) {
      // seems like flip is trying to loop, probably there's not enough space on any of the flippable sides
      return data;
    }

    var boundaries = getBoundaries(data.instance.popper, data.instance.reference, options.padding, options.boundariesElement, data.positionFixed);
```
### Line 3886-3895
```
      placementOpposite = getOppositePlacement(placement);

      var popperOffsets = data.offsets.popper;
      var refOffsets = data.offsets.reference;

      // using floor because the reference offsets may contain decimals we are not going to consider here
      var floor = Math.floor;
      var overlapsRef = placement === 'left' && floor(popperOffsets.right) > floor(refOffsets.left) || placement === 'right' && floor(popperOffsets.left) < floor(refOffsets.right) || placement === 'top' && floor(popperOffsets.bottom) > floor(refOffsets.top) || placement === 'bottom' && floor(popperOffsets.top) < floor(refOffsets.bottom);

      var overflowsLeft = floor(popperOffsets.left) < floor(boundaries.left);
```
### Line 3897-3918
```
      var overflowsTop = floor(popperOffsets.top) < floor(boundaries.top);
      var overflowsBottom = floor(popperOffsets.bottom) > floor(boundaries.bottom);

      var overflowsBoundaries = placement === 'left' && overflowsLeft || placement === 'right' && overflowsRight || placement === 'top' && overflowsTop || placement === 'bottom' && overflowsBottom;

      // flip the variation if required
      var isVertical = ['top', 'bottom'].indexOf(placement) !== -1;

      // flips variation if reference element overflows boundaries
      var flippedVariationByRef = !!options.flipVariations && (isVertical && variation === 'start' && overflowsLeft || isVertical && variation === 'end' && overflowsRight || !isVertical && variation === 'start' && overflowsTop || !isVertical && variation === 'end' && overflowsBottom);

      // flips variation if popper content overflows boundaries
      var flippedVariationByContent = !!options.flipVariationsByContent && (isVertical && variation === 'start' && overflowsRight || isVertical && variation === 'end' && overflowsLeft || !isVertical && variation === 'start' && overflowsBottom || !isVertical && variation === 'end' && overflowsTop);

      var flippedVariation = flippedVariationByRef || flippedVariationByContent;

      if (overlapsRef || overflowsBoundaries || flippedVariation) {
        // this boolean to detect any flip loop
        data.flipped = true;

        if (overlapsRef || overflowsBoundaries) {
          placement = flipOrder[index + 1];
```
### Line 3922-3932
```
          variation = getOppositeVariation(variation);
        }

        data.placement = placement + (variation ? '-' + variation : '');

        // this object contains `position`, we want to preserve it along with
        // any additional property we may add in the future
        data.offsets.popper = _extends({}, data.offsets.popper, getPopperOffsets(data.instance.popper, data.offsets.reference, data.placement));

        data = runModifiers(data.instance.modifiers, data, 'flip');
      }
```
### Line 3974-3988
```
   * @argument {Object} referenceOffsets
   * @returns {Number|String}
   * Value in pixels, or original string if no values were extracted
   */
  function toValue(str, measurement, popperOffsets, referenceOffsets) {
    // separate value from unit
    var split = str.match(/((?:\-|\+)?\d*\.?\d*)(.*)/);
    var value = +split[1];
    var unit = split[2];

    // If it's not a number it's an operator, I guess
    if (!value) {
      return str;
    }

```
### Line 3999-4018
```
      }

      var rect = getClientRect(element);
      return rect[measurement] / 100 * value;
    } else if (unit === 'vh' || unit === 'vw') {
      // if is a vh or vw, we calculate the size based on the viewport
      var size = void 0;
      if (unit === 'vh') {
        size = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
      } else {
        size = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
      }
      return size / 100 * value;
    } else {
      // if is an explicit pixel unit, we get rid of the unit and keep the value
      // if is an implicit unit, it's px, and we return just the value
      return value;
    }
  }

```
### Line 4028-4070
```
   * @returns {Array} a two cells array with x and y offsets in numbers
   */
  function parseOffset(offset, popperOffsets, referenceOffsets, basePlacement) {
    var offsets = [0, 0];

    // Use height if placement is left or right and index is 0 otherwise use width
    // in this way the first offset will use an axis and the second one
    // will use the other one
    var useHeight = ['right', 'left'].indexOf(basePlacement) !== -1;

    // Split the offset string to obtain a list of values and operands
    // The regex addresses values with the plus or minus sign in front (+10, -20, etc)
    var fragments = offset.split(/(\+|\-)/).map(function (frag) {
      return frag.trim();
    });

    // Detect if the offset string contains a pair of values or a single one
    // they could be separated by comma or space
    var divider = fragments.indexOf(find$1(fragments, function (frag) {
      return frag.search(/,|\s/) !== -1;
    }));

    if (fragments[divider] && fragments[divider].indexOf(',') === -1) {
      console.warn('Offsets separated by white space(s) are deprecated, use a comma (,) instead.');
    }

    // If divider is found, we divide the list of values and operands to divide
    // them by ofset X and Y.
    var splitRegex = /\s*,\s*|\s+/;
    var ops = divider !== -1 ? [fragments.slice(0, divider).concat([fragments[divider].split(splitRegex)[0]]), [fragments[divider].split(splitRegex)[1]].concat(fragments.slice(divider + 1))] : [fragments];

    // Convert the values with units to absolute pixels to allow our computations
    ops = ops.map(function (op, index) {
      // Most of the units rely on the orientation of the popper
      var measurement = (index === 1 ? !useHeight : useHeight) ? 'height' : 'width';
      var mergeWithPrevious = false;
      return op
      // This aggregates any `+` or `-` sign that aren't considered operators
      // e.g.: 10 + +5 => [10, +, +5]
      .reduce(function (a, b) {
        if (a[a.length - 1] === '' && ['+', '-'].indexOf(b) !== -1) {
          a[a.length - 1] = b;
          mergeWithPrevious = true;
```
### Line 4075-4090
```
          return a;
        } else {
          return a.concat(b);
        }
      }, [])
      // Here we convert the string values into number values (in px)
      .map(function (str) {
        return toValue(str, measurement, popperOffsets, referenceOffsets);
      });
    });

    // Loop trough the offsets arrays and execute the operations
    ops.forEach(function (op, index) {
      op.forEach(function (frag, index2) {
        if (isNumeric(frag)) {
          offsets[index] += frag * (op[index2 - 1] === '-' ? -1 : 1);
```
### Line 4145-4163
```
   * @returns {Object} The data object, properly modified
   */
  function preventOverflow(data, options) {
    var boundariesElement = options.boundariesElement || getOffsetParent(data.instance.popper);

    // If offsetParent is the reference element, we really want to
    // go one step up and use the next offsetParent as reference to
    // avoid to make this modifier completely useless and look like broken
    if (data.instance.reference === boundariesElement) {
      boundariesElement = getOffsetParent(boundariesElement);
    }

    // NOTE: DOM access here
    // resets the popper's position so that the document size can be calculated excluding
    // the size of the popper element itself
    var transformProp = getSupportedPropertyName('transform');
    var popperStyles = data.instance.popper.style; // assignment to help minification
    var top = popperStyles.top,
        left = popperStyles.left,
```
### Line 4167-4177
```
    popperStyles.left = '';
    popperStyles[transformProp] = '';

    var boundaries = getBoundaries(data.instance.popper, data.instance.reference, options.padding, boundariesElement, data.positionFixed);

    // NOTE: DOM access here
    // restores the original style properties after the offsets have been computed
    popperStyles.top = top;
    popperStyles.left = left;
    popperStyles[transformProp] = transform;

```
### Line 4218-4227
```
  function shift(data) {
    var placement = data.placement;
    var basePlacement = placement.split('-')[0];
    var shiftvariation = placement.split('-')[1];

    // if shift shiftvariation is specified, run the modifier
    if (shiftvariation) {
      var _data$offsets = data.offsets,
          reference = _data$offsets.reference,
          popper = _data$offsets.popper;
```
### Line 4257-4274
```
    var bound = find$1(data.instance.modifiers, function (modifier) {
      return modifier.name === 'preventOverflow';
    }).boundaries;

    if (refRect.bottom < bound.top || refRect.left > bound.right || refRect.top > bound.bottom || refRect.right < bound.left) {
      // Avoid unnecessary DOM access if visibility hasn't changed
      if (data.hide === true) {
        return data;
      }

      data.hide = true;
      data.attributes['x-out-of-boundaries'] = '';
    } else {
      // Avoid unnecessary DOM access if visibility hasn't changed
      if (data.hide === false) {
        return data;
      }

```
### Line 4740-4750
```
  /**
   * @callback onUpdate
   * @param {dataObject} data
   */

  // Utils
  // Methods
  var Popper = function () {
    /**
     * Creates a new Popper.js instance.
     * @class Popper
```
### Line 4761-4827
```

      this.scheduleUpdate = function () {
        return requestAnimationFrame(_this.update);
      };

      // make update() debounced, so that it only runs at most once-per-tick
      this.update = debounce(this.update.bind(this));

      // with {} we create a new object with the options inside it
      this.options = _extends({}, Popper.Defaults, options);

      // init state
      this.state = {
        isDestroyed: false,
        isCreated: false,
        scrollParents: []
      };

      // get reference and popper elements (allow jQuery wrappers)
      this.reference = reference && reference.jquery ? reference[0] : reference;
      this.popper = popper && popper.jquery ? popper[0] : popper;

      // Deep merge modifiers options
      this.options.modifiers = {};
      Object.keys(_extends({}, Popper.Defaults.modifiers, options.modifiers)).forEach(function (name) {
        _this.options.modifiers[name] = _extends({}, Popper.Defaults.modifiers[name] || {}, options.modifiers ? options.modifiers[name] : {});
      });

      // Refactoring modifiers' list (Object => Array)
      this.modifiers = Object.keys(this.options.modifiers).map(function (name) {
        return _extends({
          name: name
        }, _this.options.modifiers[name]);
      })
      // sort the modifiers by order
      .sort(function (a, b) {
        return a.order - b.order;
      });

      // modifiers have the ability to execute arbitrary code when Popper.js get inited
      // such code is executed in the same order of its modifier
      // they could add new properties to their options configuration
      // BE AWARE: don't add options to `options.modifiers.name` but to `modifierOptions`!
      this.modifiers.forEach(function (modifierOptions) {
        if (modifierOptions.enabled && isFunction(modifierOptions.onLoad)) {
          modifierOptions.onLoad(_this.reference, _this.popper, _this.options, modifierOptions, _this.state);
        }
      });

      // fire the first update to position the popper in the right place
      this.update();

      var eventsEnabled = this.options.eventsEnabled;
      if (eventsEnabled) {
        // setup event listeners, they will take care of update the position in specific situations
        this.enableEventListeners();
      }

      this.state.eventsEnabled = eventsEnabled;
    }

    // We can't use class properties because they don't get listed in the
    // class prototype and break stuff like Sinon stubs


    createClass(Popper, [{
      key: 'update',
```
### Line 4995-5004
```
    } // Getters


    var _proto = Dropdown.prototype;

    // Public
    _proto.toggle = function toggle() {
      if (this._element.disabled || this._element.classList.contains(ClassName$4.DISABLED)) {
        return;
      }
```
### Line 5044-5065
```

          if (typeof this._config.reference.jquery !== 'undefined') {
            referenceElement = this._config.reference[0];
          }
        } // If boundary is not `scrollParent`, then set position to `static`
        // to allow the menu to "escape" the scroll parent's boundaries
        // https://github.com/twbs/bootstrap/issues/24251


        if (this._config.boundary !== 'scrollParent') {
          parent.classList.add(ClassName$4.POSITION_STATIC);
        }

        this._popper = new Popper(referenceElement, this._menu, this._getPopperConfig());
      } // If this is a touch-enabled device we add extra
      // empty mouseover listeners to the body's immediate children;
      // only needed because of broken event delegation on iOS
      // https://www.quirksmode.org/blog/archives/2014/02/mouse_event_bub.html


      if ('ontouchstart' in document.documentElement && !makeArray(SelectorEngine.closest(parent, Selector$4.NAVBAR_NAV)).length) {
        makeArray(document.body.children).forEach(function (elem) {
```
### Line 5269-5278
```
        var hideEvent = EventHandler.trigger(parent, Event$5.HIDE, relatedTarget);

        if (hideEvent.defaultPrevented) {
          continue;
        } // If this is a touch-enabled device we remove the extra
        // empty mouseover listeners we added for iOS support


        if ('ontouchstart' in document.documentElement) {
          makeArray(document.body.children).forEach(function (elem) {
```
### Line 5295-5310
```
    Dropdown.getParentFromElement = function getParentFromElement(element) {
      return getElementFromSelector(element) || element.parentNode;
    };

    Dropdown.dataApiKeydownHandler = function dataApiKeydownHandler(event) {
      // If not input/textarea:
      //  - And not a key in REGEXP_KEYDOWN => not a dropdown command
      // If input/textarea:
      //  - If space key => not a dropdown command
      //  - If key is other than escape
      //    - If key is not up or down => not a dropdown command
      //    - If trigger inside the menu => not a dropdown command
      if (/input|textarea/i.test(event.target.tagName) ? event.which === SPACE_KEYCODE || event.which !== ESCAPE_KEYCODE && (event.which !== ARROW_DOWN_KEYCODE && event.which !== ARROW_UP_KEYCODE || SelectorEngine.closest(event.target, Selector$4.MENU)) : !REGEXP_KEYDOWN.test(event.which)) {
        return;
      }

```
### Line 5334-5348
```
      }

      var index = items.indexOf(event.target);

      if (event.which === ARROW_UP_KEYCODE && index > 0) {
        // Up
        index--;
      }

      if (event.which === ARROW_DOWN_KEYCODE && index < items.length - 1) {
        // Down
        index++;
      }

      if (index < 0) {
```
### Line 5492-5501
```
    } // Getters


    var _proto = Modal.prototype;

    // Public
    _proto.toggle = function toggle(relatedTarget) {
      return this._isShown ? this.hide() : this.show(relatedTarget);
    };

```
### Line 5633-5642
```
      var transition = this._element.classList.contains(ClassName$5.FADE);

      var modalBody = SelectorEngine.findOne(Selector$5.MODAL_BODY, this._dialog);

      if (!this._element.parentNode || this._element.parentNode.nodeType !== Node.ELEMENT_NODE) {
        // Don't move modal's DOM position
        document.body.appendChild(this._element);
      }

      this._element.style.display = 'block';
```
### Line 5813-5823
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
### Line 5844-5855
```

    _proto._setScrollbar = function _setScrollbar() {
      var _this9 = this;

      if (this._isBodyOverflowing) {
        // Note: DOMNode.style.paddingRight returns the actual value or '' if not set
        //   while $(DOMNode).css('padding-right') returns the calculated value or 0 if not set
        // Adjust fixed content padding
        makeArray(SelectorEngine.find(Selector$5.FIXED_CONTENT)).forEach(function (element) {
          var actualPadding = element.style.paddingRight;
          var calculatedPadding = window.getComputedStyle(element)['padding-right'];
          Manipulator.setDataAttribute(element, 'padding-right', actualPadding);
```
### Line 5871-5880
```

      document.body.classList.add(ClassName$5.OPEN);
    };

    _proto._resetScrollbar = function _resetScrollbar() {
      // Restore fixed content padding
      makeArray(SelectorEngine.find(Selector$5.FIXED_CONTENT)).forEach(function (element) {
        var padding = Manipulator.getDataAttribute(element, 'padding-right');

        if (typeof padding !== 'undefined') {
```
### Line 5901-5910
```
        document.body.style.paddingRight = padding;
      }
    };

    _proto._getScrollbarWidth = function _getScrollbarWidth() {
      // thx d.walsh
      var scrollDiv = document.createElement('div');
      scrollDiv.className = ClassName$5.SCROLLBAR_MEASURER;
      document.body.appendChild(scrollDiv);
      var scrollbarWidth = scrollDiv.getBoundingClientRect().width - scrollDiv.clientWidth;
```
### Line 5969-5978
```
      event.preventDefault();
    }

    EventHandler.one(target, Event$6.SHOW, function (showEvent) {
      if (showEvent.defaultPrevented) {
        // only register focus restorer if modal will actually get shown
        return;
      }

      EventHandler.one(target, Event$6.HIDDEN, function () {
```
### Line 6058-6067
```

    return false;
  };

  var DefaultWhitelist = {
    // Global attributes allowed on any supplied element below.
    '*': ['class', 'dir', 'id', 'lang', 'role', ARIA_ATTRIBUTE_PATTERN],
    a: ['target', 'href', 'title', 'rel'],
    area: [],
    b: [],
```
### Line 6249-6258
```
    } // Getters


    var _proto = Tooltip.prototype;

    // Public
    _proto.enable = function enable() {
      this._isEnabled = true;
    };

```
### Line 6362-6373
```
        }

        EventHandler.trigger(this.element, this.constructor.Event.INSERTED);
        this._popper = new Popper(this.element, tip, this._getPopperConfig(attachment));
        tip.classList.add(ClassName$6.SHOW); // If this is a touch-enabled device we add extra
        // empty mouseover listeners to the body's immediate children;
        // only needed because of broken event delegation on iOS
        // https://www.quirksmode.org/blog/archives/2014/02/mouse_event_bub.html

        if ('ontouchstart' in document.documentElement) {
          makeArray(document.body.children).forEach(function (element) {
            EventHandler.on(element, 'mouseover', noop());
```
### Line 6422-6431
```
      if (hideEvent.defaultPrevented) {
        return;
      }

      tip.classList.remove(ClassName$6.SHOW); // If this is a touch-enabled device we remove the extra
      // empty mouseover listeners we added for iOS support

      if ('ontouchstart' in document.documentElement) {
        makeArray(document.body.children).forEach(function (element) {
          return EventHandler.off(element, 'mouseover', noop);
```
### Line 6948-6957
```
      return _Tooltip.apply(this, arguments) || this;
    }

    var _proto = Popover.prototype;

    // Overrides
    _proto.isWithContent = function isWithContent() {
      return this.getTitle() || this._getContent();
    };

```
### Line 7023-7032
```
      return Data.getData(element, DATA_KEY$7);
    };

    _createClass(Popover, null, [{
      key: "VERSION",
      // Getters
      get: function get() {
        return VERSION$7;
      }
    }, {
```
### Line 7158-7167
```
    } // Getters


    var _proto = ScrollSpy.prototype;

    // Public
    _proto.refresh = function refresh() {
      var _this2 = this;

      var autoMethod = this._scrollElement === this._scrollElement.window ? OffsetMethod.OFFSET : OffsetMethod.POSITION;
```
### Line 7296-7309
```

      if (link.classList.contains(ClassName$8.DROPDOWN_ITEM)) {
        SelectorEngine.findOne(Selector$8.DROPDOWN_TOGGLE, SelectorEngine.closest(link, Selector$8.DROPDOWN)).classList.add(ClassName$8.ACTIVE);
        link.classList.add(ClassName$8.ACTIVE);
      } else {
        // Set triggered link as active
        link.classList.add(ClassName$8.ACTIVE);
        SelectorEngine.parents(link, Selector$8.NAV_LIST_GROUP).forEach(function (listGroup) {
          // Set triggered links parents as active
          // With both <ul> and <nav> markup a parent is the previous sibling of any nav ancestor
          SelectorEngine.prev(listGroup, Selector$8.NAV_LINKS + ", " + Selector$8.LIST_ITEMS).forEach(function (item) {
            return item.classList.add(ClassName$8.ACTIVE);
          }); // Handle special case when .nav-link is inside .nav-item

```
### Line 7448-7457
```
    } // Getters


    var _proto = Tab.prototype;

    // Public
    _proto.show = function show() {
      var _this = this;

      if (this._element.parentNode && this._element.parentNode.nodeType === Node.ELEMENT_NODE && this._element.classList.contains(ClassName$9.ACTIVE) || this._element.classList.contains(ClassName$9.DISABLED)) {
```
### Line 7689-7698
```
    } // Getters


    var _proto = Toast.prototype;

    // Public
    _proto.show = function show() {
      var _this = this;

      var showEvent = EventHandler.trigger(this._element, Event$b.SHOW);
```
### Line 7880-7885
```
  };

  return index_umd;

}));
//# sourceMappingURL=bootstrap.bundle.js.map
```

## _js_tests_helpers_fixture_js

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

# Issues
## 25110
Title:
```

        Missing border radius on input group with validation feedback
      
```
Author:
```
MoritzBru
```
Text:
```

With new beta 3 and using the new input-group stuff, inputs inside input-groups with some validation feedback after them are missing the border-radius.

red circle: without border-radius
green circle: with border-radius
This is an example from the bootstrap documentation

```
Author:
```
mdo
```
Text:
```

Damn, I'm super disappointed in myself for not catching this during Beta 3. I thought I had this all locked up with that rewrite. This is going to be tough.
/cc @ysds in case he has ideas having looked at some of this code recently

```
Author:
```
mdo
```
Text:
```

I spent an hour on this last night and had nothing, but just had an idea to use the validation state.
  .form-control,
  .custom-select {
    &:not(:last-child) { @include border-right-radius(0); }
    &:not(:first-child) { @include border-left-radius(0); }

    &:not(:last-child):required,
    &:not(:last-child).is-valid,
    &:not(:last-child).is-invalid {
      @include border-right-radius($input-border-radius);
    }
  }
This works on the particular docs example, but I need to see if it doesn't work elsewhere.

```
Author:
```
ysds
```
Text:
```

@mdo I am terribly sorry for the lack of confirmation. There is still a issue. e.g. appended addon:
<div class="input-group mb-3">
  <input type="text" class="form-control is-invalid" placeholder="Recipient's username">
  <div class="input-group-append">
    <span class="input-group-text">@example.com</span>
  </div>
  <div class="invalid-feedback">
    Please provide a valid zip.
  </div>
</div>
I created various test cases here. https://codepen.io/fellows3/pen/OzmMoz

```
Author:
```
mdo
```
Text:
```

Nice, thanks for the test case. I've forked your pen to:

Add my latest built CSS from my local changes I included in my last comment. This fixes the main validation bug from the docs, as well as the rounding of our file inputs.
Remove validation on multiple inputs—there's no way to do this, and we already explicitly do not support this.

See https://codepen.io/emdeoh/pen/OzmNNw?editors=1100. Have to improve some custom select and custom file, as well as dealing with the appended as you noted.

```
Author:
```
ysds
```
Text:
```

We also have to suppose a .was-validated case like:
https://getbootstrap.com/docs/4.0/components/forms/#custom-styles

```
Author:
```
mdo
```
Text:
```

@ysds That's where I'm hoping :required can help, which I've included in that snippet. Might need to sneak :optional in there, too.

```
Author:
```
ysds
```
Text:
```

I don't have any solution with only CSS3 selector to this issue. It would be impossible.
I think we should move .invalid-feedback to outside of input group. And then, extend .input-group class (.has-valid/invalid) as many times proposed in #23454. That would solve most of the issues (validation feedback of multiple input and combination with custom file input etc.). The .has-valid/invalid class will be unnecessary in the future by :has selector of CSS4.

```
Author:
```
mdo
```
Text:
```

Hmm, that'd be a breaking change from the final beta. I'm pushing for no breaking changes, but we'll see. I agree there doesn't seem to be a solution. I was trying to use some :nth-last-child stuff, but that's a bit messy right now.

```
Author:
```
mdo
```
Text:
```

I have some real funky CSS for y'all in #25352 to address as much of this as I can. 😅

```
Author:
```
altbdoor
```
Text:
```

Just dropping my two cents. I'm using v4.0 at the moment, and I was able to get the rounded corners back on the appended button with:
<div class="input-group">
    <input type="text" class="form-control is-invalid" readonly required>
    
    <div class="input-group-append">
        <button class="btn btn-outline-secondary rounded-right" type="button">
            Hey
        </button>
    </div>
    
    <div class="invalid-feedback">
        Error
    </div>
</div>
It needs an extra declaration of .rounded-right on the element within the .input-group-append. Not the most elegant, but at least it works.

```
Author:
```
MoritzBru
```
Text:
```


Damn, I'm super disappointed in myself for not catching this during Beta 3. I thought I had this all locked up with that rewrite. This is going to be tough

I guess thats what betas are for. 😉
@altbdoor Jep generally this works.
But when you change the $input-border-radius then you run into problems because the border utilities are based on the general $border-radius

```
Author:
```
cbossi
```
Text:
```

I found a solution to the problem using bootstrap's order classes:
You can place the .invalid-feedback element in between the input and the input-group-append element and then append the order-1 class to it. This way the .invalid-feedback element is NOT the last child inside the input-group (which would cause the border radius problem), but nonetheless appears at the end of the input-group:
<div class="form-group">
    <label for="name">Name</label>
    <div class="input-group">
    <input type="text" class="form-control" id="name" required>
    <div class="invalid-feedback order-1">
        Please provide a name.
    </div>
    <div class="input-group-append">
        <span class="input-group-text">
        <i class="fas fa-envelope"></i>
        </span>
    </div>
    </div>
</div>

```
Author:
```
flachware
```
Text:
```

I ran into the same issue. How about generally using the :last-of-type selector instead of :last-child in _input-group.scss and switching div.invalid-feedback to p.invalid-feedback?



```
Author:
```
claudioalmeiida
```
Text:
```

I find another problem when it does not use .dropdown-toggle class, I do not know if it was a known problem
https://codepen.io/anon/pen/BVZMVj


```
Author:
```
rushairer
```
Text:
```

So that????

```
Author:
```
kejodion
```
Text:
```

March 2019 and issue still exists. Is there no pull request for a fix?

```
Author:
```
mdo
```
Text:
```

@kjjdion If you have a fix, we'd love a PR, but otherwise, the lack of a PR means that there is no fix (or that's rather difficult to do).

```
Author:
```
nibblesnbits
```
Text:
```

Forgive my ignorance, but why would it be more complicated than this?
.input-group > .form-control:not(:first-child), .input-group > .custom-select:not(:first-child) {
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
.input-group > .input-group-prepend > .btn, .input-group > .input-group-prepend > .input-group-text, .input-group > .input-group-append:not(:last-child) > .btn, .input-group > .input-group-append:not(:last-child) > .input-group-text, .input-group > .input-group-append:last-child > .btn:not(:last-child):not(.dropdown-toggle), .input-group > .input-group-append:last-child > .input-group-text:not(:last-child) {
  border-top-right-radius: 0.25rem;
  border-bottom-right-radius: 0.25rem;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}
Obviously these are likely overly specific, but these rules seem to fix it in my app.


```
Author:
```
chrisbo
```
Text:
```

Although a sort of hack, adding the class rounded-right to my form inputs and textarea seems to have fixed my issue.

```
Author:
```
rushairer
```
Text:
```

Thanks all

```

## 21851
Title:
```

        [Docs] Search functionality not obvious for keyboard/screenreader users
      
```
Author:
```
patrickhlauke
```
Text:
```

The current search functionality for docs relies on users typing in search terms and then selecting matches from the dropdown of results shown.
Visually, the dropdown appears like options should be reachable with cursor up/down - but unintuitively, user has to TAB to them (as they're simply links).
For screenreader users, no announcement is made that results are being dynamically shown.
Lastly, submitting the form/hitting enter in the search field results in the page being reloaded, but no actual search being performed...this is confusing to all users.

```
Author:
```
craigstroman
```
Text:
```

Hi, is this issue being worked on?  If not I would be interested in working on it.

```
Author:
```
craigstroman
```
Text:
```

Do you want me to create a pull request for this?

```
Author:
```
Johann-S
```
Text:
```

Go ahead @craigstroman 👍 every opened​ issue are open for a PR, instead of the issue already have a PR

```
Author:
```
craigstroman
```
Text:
```

Hi, sorry for not responding sooner.  I will create a PR for this tomorrow then.

```
Author:
```
mdo
```
Text:
```

Should be good since #22715.

```
Author:
```
craigstroman
```
Text:
```

Hi,
Glad this was fixed.
I'm sorry for not completing this sooner like I said I would.  In the past 2 months I actually ended up getting a new job and moving to a new state.

```
Author:
```
mdo
```
Text:
```

No worries! We ended up in a good spot with DocSearch :).

```
Author:
```
patrickhlauke
```
Text:
```

Confirming that this now works a lot better for keyboard/AT users

```

## 5035
Title:
```

        IE8 input height too large with row-fluid
      
```
Author:
```
jschr
```
Text:
```

Can't seem to figure this one out. In IE8, my inputs are much taller then IE9 or Chrome. I narrowed it down to only happening within a fluid layout.
IE8: http://imgur.com/eHCVq
IE9: http://imgur.com/sLSPD

```
Author:
```
mdo
```
Text:
```

Dupe of an issue already open about this.

```

## 26506
Title:
```

        .btn-outline-light can't really be seen on Bootstrap docs
      
```
Author:
```
sts-ryan-holton
```
Text:
```

Hi!
I've just noticed whilst browsing the Bootstrap 4.1.1 docs that you can't really see the text of the .btn-outline-light button.
Could we consider some other text colour here? I don't think it's really legible and people who could be somewhat visually impaired might find it difficult to read?
Take a look:

(https://getbootstrap.com/docs/4.1/components/buttons/)

```
Author:
```
bardiharborow
```
Text:
```

.btn-outline-light really isn't supposed to be used on a white background, but there is no background colour that makes all colours accessible, and it's a pain to break it into it's own section with a black background for just one button.

```
Author:
```
sts-ryan-holton
```
Text:
```

@bardiharborow Completely understand, couldn't we just make the text a little darker for the docs for that particular button?

```
Author:
```
bardiharborow
```
Text:
```

I imagine that would confuse people more than it would help unfortunately.

```
Author:
```
patrickhlauke
```
Text:
```


couldn't we just make the text a little darker for the docs for that particular button?

no because then (if just done for the docs) it wouldn't reflect the actual color you'd get when using the class

```

## 23545
Title:
```

        .navbar-inverse not in CSS file
      
```
Author:
```
leecollings
```
Text:
```

Using either the bootstrap.css or bootstrap.min.css, a search for navbar-inverse returns no results.
Is there a list of all classes that are not included in the CSS files, to easily see what can and can't be used?

```
Author:
```
jipexu
```
Text:
```

Hi
there is not list of changed classe alpha=>beta ..
in the doc .."Theming the navbar has never been easier thanks to the combination of theming classes and background-color utilities. Choose from .navbar-light for use with light background colors, or .navbar-dark for dark background colors. Then, customize with .bg-* utilities."

```
Author:
```
leecollings
```
Text:
```

The v4 example of 'dashboard' shows the usage of navbar-inverse:
https://v4-alpha.getbootstrap.com/examples/dashboard/

```
Author:
```
jipexu
```
Text:
```

yep unfortunatly  but this not up to date .. is not a BS 4 beta example ...

```
Author:
```
Johann-S
```
Text:
```

https://getbootstrap.com/docs/4.0/migration/#navbar
thanks @jipexu

```

## 17784
Title:
```

        input groups are broken when using flexbox 
      
```
Author:
```
itised
```
Text:
```

If $enable-flex is set to true, input-group-addons shrink to their minimum size and content overflows out of them.

```
Author:
```
cvrebert
```
Text:
```

In which browser(s)?

```
Author:
```
itised
```
Text:
```

Safari 9.0 and Chrome 45, both on OS X 10.11.
I also just checked Firefox 41, and it has the opposite problem. In Firefox, the addons are much wider than they should be. They are also shorter than the inputs they are attached to.
Again, this is only when $enable-flex is set to true. If $enable-flex is false, all 3 browsers behave as expected.

```
Author:
```
DanCouper
```
Text:
```

+1 on this, specifically FireFox. This is the behavior I'm getting at the minute (the green dashed lines are where the edges of the a grid columns are) -
In Firefox (42 and 44.0a2):

In Chrome (47, correct behaviour):

As above, it's a flex issue; if I turn off flex it works universally. I assume it's related to how FF interprets the Flexbox spec, I'll do more isolated testing
Markup is this, I can't see any errors in structuring as per Bootstrap:
<fieldset class="form-group">
  <label class="sr-only" for="basket_lines_attributes_0_quantity">Quantity</label>
  <div class="input-group">
    <span class="input-group-btn">
      <button name="button" type="submit" class="btn btn-primary"><i class="fa fa-minus"></i></button>
    </span>
    <input value="1" class="form-control" name="basket[lines_attributes][0][quantity]" id="basket_lines_attributes_0_quantity" type="text">
    <span class="input-group-btn">
      <button name="button" type="submit" class="btn btn-primary"><i class="fa fa-plus"></i></button>
    </span>
  </div>
</fieldset>

EDIT
This is a very specific fix, I needed to apply it to a specific element, and I need to make a series of different usecases before I can think about PRing, but it's not a bug according to Mozillas bug tracker, Chrome et al just implement the spec incorrectly:
https://bugzilla.mozilla.org/show_bug.cgi?id=1108514
Applying min-width: 0 to my input fixes the problem immediately -


```
Author:
```
garlian
```
Text:
```

+1

```
Author:
```
mdo
```
Text:
```

Should be fixed now that #17756 is merged. Holler if it's still broken though and we can re-open.

```
Author:
```
wnr
```
Text:
```

Seems to me that this issue is still around. I tried it with exampleInputAmount in the docs components/forms/ locally with flex turned on @ commit 0416f761dddae04a1b4d3ce70afece518330ca4d.
Applying min-width: 0 seems to fix it indeed.

```
Author:
```
reisub-de
```
Text:
```

This bug is still there in v4.0.0-alpha.4

```
Author:
```
tharunsaik
```
Text:
```

you can simply add this default bootstrap grid CSS
.input-group { border-collapse: separate; display: table; } .input-group .form-control, .input-group-addon, .input-group-btn { display: table-cell; }

```
Author:
```
DanCouper
```
Text:
```

@tharunsaik removing flex isn't a solution the described problem, using display:table/table-cell simply [re]introduces a different set of problems (doing what you suggest immediately removes all the benefits of using flex just to solve a single specific issue). It happens due to Chrome's interpretation of the flex spec, and a possible solution is described above.

```
Author:
```
mdo
```
Text:
```

This is fixed y'all :).

```

## 15963
Title:
```

        Inheriting Bootstrap classes doesn't inherit nested/psuedo selectors
      
```
Author:
```
pauldotknopf
```
Text:
```

I have a input control framework that uses it's own classes. I would like to remove the vendor-provided theme and modify their classes to "extend/inherit" Bootstrap classes. That way, I don't have to change their rendered markup, and at the same time, I can use bootstrap styles without explicit styles, allowing future upgrades and bug fixes to Bootstrap to carry over to my vendor's theme.
The problem is that, when inheriting classes, the classes inherit have to be coded (in less) a certain way so that derived types will also contain all contextual/pseudo selectors as well.
Let me illustrate.
The following less...
.bootstrap-class {
    background:red;
}
.bootstrap-class input {
    background:blue;
}

.vendor-control {
    .bootstrap-class;
}

..will be rendered as...
.bootstrap-class {
  background: red;
}
.bootstrap-class input {
  background: blue;
}
.vendor-control {
  background: red;
}

See the problem? The nested input isn't styled for the derived .vendor-control class.
However, if you write your less like this...
.bootstrap-class {
    background:red;
    input {
        background:blue;
    }
}

.vendor-control {
    .bootstrap-class;
}

..the rendered markup will be...
.bootstrap-class {
  background: red;
}
.bootstrap-class input {
  background: blue;
}
.vendor-control {
  background: red;
}
.vendor-control input {
  background: blue;
}

This would greatly simplify the extension of vendor controls. For example, I can imagine a single "Kendo UI" less file that simply sets up inheritance, and the entire framework would, from then on, be entirely Bootstrap. Currently, Kendo UI provides a theme that looks like Bootstrap out-of-the-box, but imagine a less file that makes Kendo UI look like any customized Bootstrap layout, instantly, complete with all the "has-feedback" classes and what-not.
With that said, would you guys entertain a PR with these changes? The changes would be similar to the following.
This...
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}

...would be changed to...
.radio,
.radio-inline {
    input[type="radio"] {
        position: absolute;
        margin-left: -20px;
        margin-top: 4px \9;
    }
}
.checkbox,
.checkbox-inline {
    input[type="checkbox"] {
        position: absolute;
        margin-left: -20px;
        margin-top: 4px \9;
    }
}


```
Author:
```
kkirsche
```
Text:
```

This seems to me as though there would be a lot of code duplication or this would require a lot of mixins. I don't see this being put into V3 as its ending its life in prep for V4 but an admin would have to say for sure.

```
Author:
```
cvrebert
```
Text:
```

Have you tried @extend-ing the Bootstrap classes instead?

```
Author:
```
pauldotknopf
```
Text:
```

@cvrebert, Yes. The issue is the same, but the rendered markup is a little different.
This...
.bootstrap-class {
    background:red;
}
.bootstrap-class input {
    background:blue;
}

.vendor-control {
    &:extend(.bootstrap-class);
}

..is rendered as...
.bootstrap-class,
.vendor-control {
  background: red;
}
.bootstrap-class input {
  background: blue;
}


```
Author:
```
pauldotknopf
```
Text:
```

In addition, I don't think @extend works 100% as we intend here. In the following example, using the class as a mixin works, and @extend doesn't.
.bootstrap-class {
    background:red;
    input {
        background:blue;
        &:hover {
            background:green;
        }
    }
}

.vendor-control {
    .bootstrap-class;
}

..transforms to...
.bootstrap-class {
  background: red;
}
.bootstrap-class input {
  background: blue;
}
.bootstrap-class input:hover {
  background: green;
}
.vendor-control {
  background: red;
}
.vendor-control input {
  background: blue;
}
.vendor-control input:hover {
  background: green;
}

... which is correct. However, this...
.bootstrap-class {
    background:red;
    input {
        background:blue;
        &:hover {
            background:green;
        }
    }
}

.vendor-control {
    &:extend(.bootstrap-class);
}

...renders to...
.bootstrap-class,
.vendor-control {
  background: red;
}
.bootstrap-class input {
  background: blue;
}
.bootstrap-class input:hover {
  background: green;
}

which is not correct.
I'm not seeing the purpose of @extend in general, compared to using the class as a mixin, but I don't know.

```
Author:
```
DaSchTour
```
Text:
```

Well I guess there is a general misconception about less. Maybe you should try this:
.bootstrap-class {
  background:red;
    input {
      background:blue;
    }
}

.vendor-control {
    .bootstrap-class();
}
which will become this:
.bootstrap-class {
  background: red;
}
.bootstrap-class input {
  background: blue;
}
.vendor-control {
  background: red;
}
.vendor-control input {
  background: blue;
}
Using extend only adds a class to an existing part. This is the other way round. It works like extending an Object in a programming language.

```
Author:
```
pauldotknopf
```
Text:
```

Ya, I found that out.
The problem still remains though. Throughout Bootstrap, they use...
.class-name input {
   display: block;
}

...instead of...
.class-name {
   input {
      display: block;
   }
}


```
Author:
```
DaSchTour
```
Text:
```

Oh yes, I see.
So I guess instead of:
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;

  label {
    min-height: @line-height-computed; // Ensure the input doesn't jump when there is no text
    padding-left: 20px;
    margin-bottom: 0;
    font-weight: normal;
    cursor: pointer;
  }
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}

.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px; // Move up sibling radios or checkboxes for tighter spacing
}

// Radios and checkboxes on same line
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px; // space out consecutive inline controls
}
we should have something like this
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
 &-inline {
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
 input[type="radio"], input[type="checkbox"] {
   position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
 }
+ .radio-inline, + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px; // space out consecutive inline controls
 }
}
+ .radio, + .checkbox {
margin-top: -5px; // Move up sibling radios or checkboxes for tighter spacing
}

  label {
    min-height: @line-height-computed; // Ensure the input doesn't jump when there is no text
    padding-left: 20px;
    margin-bottom: 0;
    font-weight: normal;
    cursor: pointer;
  }
}
But I guess you see the dilemma, as this will not result in the expected CSS.

```
Author:
```
mdo
```
Text:
```

We don't unnecessarily nest things, nor try to make them more friendly to a particular implementation. It'd take some work to redo this all in the current version, and we currently have no plans for that kind of refactor. In v4, there will be a larger focus on classes—though some nesting will still be required—to mitigate things like this. When doing that required nesting though, we can try to account for this type of approach to using Bootstrap.

```

## 8496
Title:
```

        Custom Download not functioning
      
```
Author:
```
sangramfuture
```
Text:
```

http://twitter.github.io/bootstrap/customize.html clicked on the 'Customize and Download button.
Its not responding.
please provide alternative link for customize download if possible.

```
Author:
```
SVANNER
```
Text:
```

I confirm it is not working for me too. Get busy about 8 to 10 seconds and nothings downloads...

```
Author:
```
cvrebert
```
Text:
```

Presumably a duplicate of #7922.

```

## 9348
Title:
```

        variables.less
      
```
Author:
```
JustinDrake
```
Text:
```

Inside variables.less
@grid-gutter-width:         30px;
@navbar-padding-horizontal:        floor(@grid-gutter-width / 2);  // ~15px



If @grid-gutter-width is 30px then @navbar-padding-horizontal is exactly 15px (not "approximately 15px"; see comment)


When @grid-gutter-width is 30px, the floor is superfluous.



```
Author:
```
cvrebert
```
Text:
```

Re (2): But Bootstrap is customizable, so it won't always be 30px.

```

## 29204
Title:
```

        docs broken form examples
      
```
Author:
```
XhmikosR
```
Text:
```

It seems we still have a fewbroken form examples

the second one in https://twbs-bootstrap.netlify.com/docs/4.3/forms/layout/#auto-sizing
a few more here https://twbs-bootstrap.netlify.com/docs/4.3/forms/validation/. Basically where input-group-prepend is used


```
Author:
```
XhmikosR
```
Text:
```

Some more details, this seems to happen only on Firefox (68.0.1)



```
Author:
```
ysds
```
Text:
```

This must be related https://stackoverflow.com/questions/36247140/why-dont-flex-items-shrink-past-content-size

```

## 26711
Title:
```

        list-group inside card do not inherit card bg styles
      
```
Author:
```
dangowans
```
Text:
```

The Bootstrap documentation talks about applying background colors to entire cards by setting the appropriate bg- and text- classes on the card div.  It also talks about using list-groups inside cards.
The text color settings seem to apply to everything as expected, but the background color settings only apply to the card-header and card-body divs, and miss the list-groups.
Maybe this is on purpose.  Don't know.
JS Fiddle
https://jsfiddle.net/aq9Laaew/34724/
HTML
<div class="m-3">
  <div class="card bg-info text-white">
    <div class="card-header">
      List Group Demo
    </div>
    <div class="card-body">
      Test Body
    </div>
    <ul class="list-group list-group-flush">
      <li class="list-group-item">Item One</li>
      <li class="list-group-item">Item Two</li>
      <li class="list-group-item">Item Three</li>
    </ul>
  </div>
</div>
Screenshot


```
Author:
```
dangowans
```
Text:
```

As a "workaround", I added the list-group-item-info class to each list-group-item.  That's the behaviour I think should happen automatically if the list-group is inside a card with a background color set.

```
Author:
```
mdo
```
Text:
```

Closing as a won't fix—there should be no inheriting of background colors here. You can override with .bg-transparent or apply your own styles.

```
Author:
```
AndiLeni
```
Text:
```

I'm sorry to comment on a closed issue, but I think this fix is entirely justified. After all, Bootstrap consistently follows the concept of "styles are adopted". Just not at this point, which in my opinion means bad behavior for the developers. Furthermore, this behavior is not described in the docs and can also cause confusion in the future.
Thank you for your time.

```

## 17943
Title:
```

        HTML form <input type='number'> does not allow the letter 'e' as it should according to HTML spec
      
```
Author:
```
bfrager
```
Text:
```

The Bootstrap form validation checker returns the warning "Please enter a number" if e is entered into an input field with type=number.
The <a href'http://www.w3.org/TR/html-markup/input.number.html">HTML spec denotes that 'e' or 'E' is allowed in input fields with type=number as a mathematical symbol. From the spec:
A floating-point number consists of the following parts, in exactly the following order:
Optionally, the first character may be a "-" character.
One or more characters in the range "0—9".
Optionally, the following parts, in exactly the following order:
a "." character
one or more characters in the range "0—9"
Optionally, the following parts, in exactly the following order:
a "e" character or "E" character
optionally, a "-" character or "+" character 3.One or more characters in the range "0—9".

```
Author:
```
cvrebert
```
Text:
```


The Bootstrap form validation checker

There's no such thing. You're either referring to a third-party library such as https://github.com/1000hz/bootstrap-validator or to the HTML5 form field validation built into the web browser itself. Neither of which is controlled by Bootstrap.

```

## 18790
Title:
```

        .dropdown-toggle::after causes offset alignment in a container when used with .pull-*-right
      
```
Author:
```
kybishop
```
Text:
```

As of alpha2, .dropdown-toggle::after contains margin-right: .25rem, which causes offset alignment if the dropdown is the last element of a container where .pull-*right is used on the dropdown.
Example within a navbar:
https://jsfiddle.net/6twft72d/
https://jsfiddle.net/6twft72d/12/
This is admittedly a bit nitpicky, but it looks the slightest bit off when compared to how it used to look in alpha 1.

```
Author:
```
twbs-lmvtfy
```
Text:
```

Hi @kybishop!
You appear to have posted a live example (https://fiddle.jshell.net/6twft72d/show/light/), which is always a good first step. However, according to the HTML5 validator, your example has some validation errors, which might potentially be causing your issue:

line 67, column 9 thru column 56: Attribute disabled not allowed on element a at this point.
line 66, column 7 thru column 79: The aria-labelledby attribute must point to an element in the same document.

You'll need to fix these errors and post a revised example before we can proceed further.
Thanks!
(Please note that this is a fully automated comment.)

```
Author:
```
cvrebert
```
Text:
```

@kybishop Add the JavaScript to your example please. (And fix the above errors too.)

```
Author:
```
kybishop
```
Text:
```

Javascript added and errors fixed https://jsfiddle.net/6twft72d/4/

```
Author:
```
twbs-lmvtfy
```
Text:
```

Hi @kybishop!
You appear to have posted a live example (https://fiddle.jshell.net/6twft72d/4/show/light/), which is always a good first step. However, according to Bootlint, your example has some Bootstrap usage errors, which might potentially be causing your issue:

W005: Unable to locate jQuery, which is required for Bootstrap's JavaScript plugins to work
line 62, column 3: W012: .navbar's first child element should always be either .container or .container-fluid

You'll need to fix these errors and post a revised example before we can proceed further.
Thanks!
(Please note that this is a fully automated comment.)

```
Author:
```
kybishop
```
Text:
```

For real this time ;) https://jsfiddle.net/6twft72d/5/

```
Author:
```
cvrebert
```
Text:
```

W012 doesn't apply to v4, so we can ignore that one.

```
Author:
```
cvrebert
```
Text:
```

jQuery needs to come before bootstrap.js. Read the JS console error message.

```
Author:
```
kybishop
```
Text:
```

That's what I get for trying to submit an issue on mobile. Fixed now https://jsfiddle.net/6twft72d/12/

```
Author:
```
twbs-lmvtfy
```
Text:
```

Hi @kybishop!
You appear to have posted a live example (https://fiddle.jshell.net/6twft72d/12/show/light/), which is always a good first step. However, according to Bootlint, your example has some Bootstrap usage errors, which might potentially be causing your issue:

line 70, column 3: W012: .navbar's first child element should always be either .container or .container-fluid

You'll need to fix these errors and post a revised example before we can proceed further.
Thanks!
(Please note that this is a fully automated comment.)

```
Author:
```
mdo
```
Text:
```

This is because of #17137. I need to undo that.

```
Author:
```
mdo
```
Text:
```

Fix coming in #18807.

```

# Pull
## 12909
Title:
```

        Added support for AMD/CommonJS/Globals.
      
```
Author:
```
raulferras
```
Text:
```

Pull request related to #12783

```
Author:
```
VirtueMe
```
Text:
```

Lots of linting exception.

```
Author:
```
cvrebert
```
Text:
```

@raulferras Per the contribution guidelines, please use 2-space indents instead of tabs.

```
Author:
```
raulferras
```
Text:
```

Sure.

```
Author:
```
jenssimon
```
Text:
```

The "transition" dependencies won't work. The dependencies must not end with ".js".
So
(function (factory) {
  if (typeof define === 'function' && define.amd) {
    define(['jquery', './transition.js'], factory)
  } else if (typeof exports === 'object') {
    var jQuery = require('jquery')
    require('./transition.js')
    factory(jQuery)
  } else {
    factory(this.jQuery)
  }
}(function ($) {

should be replaced by
(function (factory) {
  if (typeof define === 'function' && define.amd) {
    define(['jquery', './transition'], factory)
  } else if (typeof exports === 'object') {
    var jQuery = require('jquery')
    require('./transition')
    factory(jQuery)
  } else {
    factory(this.jQuery)
  }
}(function ($) {

in

alert.js
carousel.js
collapse.js
modal.js
tab.js
tooltip.js


```
Author:
```
raulferras
```
Text:
```

Ok, fixed.
It worked to me under CommonJS as webpack allows it.

```
Author:
```
mokkabonna
```
Text:
```

Hope this finally is going to make it in. Right now I can't even use jquery with AMD (with noconflict) because of:



bootstrap/Gruntfile.js


         Line 35
      in
      73ad81d






 jqueryCheck: 'if (typeof jQuery === \'undefined\') { throw new Error(\'Bootstrap\\\'s JavaScript requires jQuery\') }\n\n', 






```
Author:
```
raulferras
```
Text:
```

I don't know of AMD, but with CommonJS (webpack) I'm currently doing this:
var $ = require('jquery');
window.jQuery = $;
require('bootstrap');
This does it for me.

```
Author:
```
zdroid
```
Text:
```

@raulferras You should use jQuery = $, without the window..

```
Author:
```
raulferras
```
Text:
```

That's true for bootstrap specifically, but other jQuery plugins require explicitly to overwrite window.jQuery, it all depends of the plugins/libs you're going to use.

```
Author:
```
cvrebert
```
Text:
```

Running cross-browser tests on Travis... https://travis-ci.org/twbs/bootstrap/builds/20557300

```
Author:
```
cvrebert
```
Text:
```

Browser tests pass!: https://travis-ci.org/twbs/bootstrap/jobs/20557303 😄

```
Author:
```
cvrebert
```
Text:
```

We should also add moduleType to bower.json after merging this. (Ref: bower/bower#934)

```
Author:
```
cvrebert
```
Text:
```

@twbs/team: So, aside from needing to test this manually/interactively in a few browsers beforehand, are there any objections to merging this PR?

```
Author:
```
mdo
```
Text:
```

I have zero objections as I know nothing about this. We'll need @fat to weigh in.

```
Author:
```
fat
```
Text:
```

yes. i object

```
Author:
```
fat
```
Text:
```

this stuff should be added at build time… dont think we should put it on the raw plugins

```
Author:
```
fat
```
Text:
```

i think ryan florence wrote a really complete version of this at one point… maybe we could use that to add at compile time?

```
Author:
```
cvrebert
```
Text:
```

Some possible options:

https://github.com/alexlawrence/grunt-umd
https://github.com/aearly/grunt-urequire


```
Author:
```
raulferras
```
Text:
```

If this is added at build time, will we be allowed to build the different plugins indepently?

```
Author:
```
cvrebert
```
Text:
```

@raulferras It'd produce individual per-plugin "module-ized" JS files, if that's what you mean.

```
Author:
```
raulferras
```
Text:
```

yes, great then.

```
Author:
```
fat
```
Text:
```

the more i think about this… the more I think that getting into the business of being other projects build systems seems like a bad idea.
I think as a guiding rule, it's generally safer to lean towards raw components, then trying to include all the hardware to connect to every 3rd party lib under the sun.
thoughts?

```
Author:
```
zdroid
```
Text:
```

Agree.
2014-03-23 2:51 GMT+01:00 Jacob notifications@github.com:

the more i think about this… the more I think that getting into the
business of being other projects build systems seems like a bad idea.
I think as a guiding rule, it's generally safer to lean towards raw
components, then trying to include all the hardware to connect to every 3rd
party lib under the sun.
thoughts?
—
Reply to this email directly or view it on GitHubhttps://github.com//pull/12909#issuecomment-38370499
.


Zlatan Vasović - ZDroid

```
Author:
```
enricostano
```
Text:
```

status? guide lines? any example out there? thanks!

```
Author:
```
fat
```
Text:
```

closing in favor of #13772

```

## 22401
Title:
```

        Remove incorrect role="tabpanel" from navs docs
      
```
Author:
```
patrickhlauke
```
Text:
```

role="tabpanel" is not appropriate as role for the overall container - it only applies to the individual content parts of each tab
Closes #22284
(note that there are still some fundamental problems with the tabs in both docs and their actual JS - this is only a quick fix to an obvious markup error in the docs)

```

## 13095
Title:
```

        Generate Translations list from YAML
      
```
Author:
```
juthilo
```
Text:
```

Also adds hreflang attribute to the links.
This might help with #13094.
@mdo Now that we split up the docs into includes, the difference in terms of contribution difficulty is not as high as before, I think.
/cc @cvrebert @XhmikosR

```
Author:
```
XhmikosR
```
Text:
```

I definitely like this approach! I will check this out closer later and let you know if I have any comments :)

```
Author:
```
XhmikosR
```
Text:
```

@juthilo: what do you think about this order?
- language: German
  code: de
  description: Bootstrap auf Deutsch
  url: http://holdirbootstrap.de/
This way it should be also more clear that the language order is based on the language name.

```
Author:
```
juthilo
```
Text:
```

Implemented the changes proposed by @XhmikosR.

```
Author:
```
XhmikosR
```
Text:
```

LGTM 👍

```

## 25123
Title:
```

        Darken $gray-600 by 10% for AA contrast
      
```
Author:
```
mdo
```
Text:
```

Closes #23319. Both .text-muted and .btn-outline-secondary (and indeed all secondary items) make use of $gray-600. New value provides a contrast ratio of 4.69.

```
Author:
```
patrickhlauke
```
Text:
```

for reference, see #25126

```
Author:
```
patrickhlauke
```
Text:
```

While this addresses the most egregious (and widely used) color, note that there are still many combinations in use that fail AA 4.5:1 ratio.

```

## 17689
Title:
```

        Docs: Clarify [hidden] & .hidden
      
```
Author:
```
cvrebert
```
Text:
```

CC: @mdo for review

```

## 3073
Title:
```

        Updated Glyphicons to use v1.6, as well as added a 'grey' coloured set of glyphicons
      
```
Author:
```
sashamor
```
Text:
```

Updated the glyphicons set to use v1.6, and added a variable to the LESS sheets.
Also added a 'grey', shadowed version of the glyphicons (as well as normal and white), and added an example of it to the docs.
Fixed a small typo in variables.css (which is why the previous pull request was cancelled).
From the Glyphicons changelog to v1.6:
11.04.2012 (All PNG files have been optimized by ImageOptim - http://imageoptim.pornel.net/)
GLYPHICONS 1.6
New Glyphicons:
filter
gamepad
playing_dices
sampler
web_browser
share
piano
candle
turtle
rabbit
blog
dashboard
certificate
calculator
book_open
iphone_shake
pin_classic
pin_flag
tie
wallet
globe
briefcase
suitcase
thumbs_up
thumbs_down
hand_right
hand_left
hand_up
hand_down
fullscreen
shopping_bag
hdd
nameplate
nameplate_alt
vases
announcement
dumbbell
file_import
file_export
bell
pinterest
dropbox
google+_alt
jolicloud
yahoo
blogger
picasa
amazon
tumblr
wordpress
New Halflings:
hdd
announcement
bell
certificate
thumbs_up
thumbs_down
hand_right
hand_left
hand_up
hand_down
circle_arrow_right
circle_arrow_left
circle_arrow_top
circle_arrow_down
globe
wrench
tasks_progress
filter
briefcase
fullscreen

Changed/fixed icons:
circle_arrow_left
circle_arrow_right
circle_arrow_top
circle_arrow_down
settings
fire
table
message_flag
message_lock
message_new
folder_lock
folder_flag
folder_new
tree_conifer

```
Author:
```
MGaetan89
```
Text:
```

The icon set has already been updated in d5063e5
Make a PR againt 2.0.3-wip and you'll see it. But the grey icon set would be new.

```
Author:
```
sashamor
```
Text:
```

Also, does that commit actually update the CSS files (and docs) to use/display the new icons?
Sasha
Edit: nevermind, I can see it now. But yeah, the grey icons are new.

```
Author:
```
mdo
```
Text:
```

We've already updated to 1.6 in 2.0.3-wip.

```

## 18463
Title:
```

        Introduce $nav-item-margin variable
      
```
Author:
```
cvrebert
```
Text:
```

In the name of less hardcoding.

```
Author:
```
cvrebert
```
Text:
```

CC: @mdo for review

```

