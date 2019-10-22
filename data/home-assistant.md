# home-assistant/home-assistant
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_README_rst](#_README_rst)

* [_github_PULL_REQUEST_TEMPLATE_md](#_github_PULL_REQUEST_TEMPLATE_md)

* [_CLA_md](#_CLA_md)

* [_docs_source_api_event_rst](#_docs_source_api_event_rst)

* [_docs_source_api_homeassistant_rst](#_docs_source_api_homeassistant_rst)

* [_CODE_OF_CONDUCT_md](#_CODE_OF_CONDUCT_md)

* [_CONTRIBUTING_md](#_CONTRIBUTING_md)

* [_docs_source_api_helpers_rst](#_docs_source_api_helpers_rst)

* [_github_ISSUE_TEMPLATE_md](#_github_ISSUE_TEMPLATE_md)

* [_github_ISSUE_TEMPLATE_Bug_report_md](#_github_ISSUE_TEMPLATE_Bug_report_md)

* [_docs_source_api_util_rst](#_docs_source_api_util_rst)

* [_LICENSE_md](#_LICENSE_md)

* [_docs_source_index_rst](#_docs_source_index_rst)

* [_docs_source_api_bootstrap_rst](#_docs_source_api_bootstrap_rst)

* [_docs_source_api_device_tracker_rst](#_docs_source_api_device_tracker_rst)

* [_docs_source_api_entity_rst](#_docs_source_api_entity_rst)

* [_docs_source_api_core_rst](#_docs_source_api_core_rst)

[- Inline](#Inline)

* [_homeassistant_components_insteon_binary_sensor_py](#_homeassistant_components_insteon_binary_sensor_py)

* [_homeassistant_components_tahoma_sensor_py](#_homeassistant_components_tahoma_sensor_py)

* [_homeassistant_components_fitbit_init_py](#_homeassistant_components_fitbit_init_py)

* [_homeassistant_components_zha_core_decorators_py](#_homeassistant_components_zha_core_decorators_py)

* [_homeassistant_components_bbox_device_tracker_py](#_homeassistant_components_bbox_device_tracker_py)

* [_homeassistant_components_rmvtransport_init_py](#_homeassistant_components_rmvtransport_init_py)

* [_homeassistant_components_ifttt_const_py](#_homeassistant_components_ifttt_const_py)

* [_tests_components_seventeentrack_test_sensor_py](#_tests_components_seventeentrack_test_sensor_py)

* [_tests_components_luftdaten_init_py](#_tests_components_luftdaten_init_py)

* [_tests_components_wunderground_test_sensor_py](#_tests_components_wunderground_test_sensor_py)

* [_homeassistant_components_ephember_init_py](#_homeassistant_components_ephember_init_py)

* [_tests_components_api_streams_init_py](#_tests_components_api_streams_init_py)

* [_homeassistant_components_pushetta_init_py](#_homeassistant_components_pushetta_init_py)

* [_homeassistant_components_nilu_air_quality_py](#_homeassistant_components_nilu_air_quality_py)

* [_tests_components_workday_test_binary_sensor_py](#_tests_components_workday_test_binary_sensor_py)

* [_homeassistant_components_rmvtransport_sensor_py](#_homeassistant_components_rmvtransport_sensor_py)

* [_homeassistant_components_mopar_lock_py](#_homeassistant_components_mopar_lock_py)

* [_homeassistant_components_egardia_alarm_control_panel_py](#_homeassistant_components_egardia_alarm_control_panel_py)

* [_tests_components_withings_test_init_py](#_tests_components_withings_test_init_py)

* [_homeassistant_components_lametric_notify_py](#_homeassistant_components_lametric_notify_py)

[- Issues](#Issues)

* [11045](#11045)

* [22582](#22582)

* [27959](#27959)

* [15188](#15188)

* [22352](#22352)

* [718](#718)

* [5504](#5504)

* [16830](#16830)

* [23865](#23865)

* [5061](#5061)

* [13635](#13635)

* [19455](#19455)

[- Pull](#Pull)

* [18690](#18690)

* [17327](#17327)

* [67](#67)

* [17179](#17179)

* [24620](#24620)

* [16065](#16065)

* [27132](#27132)

* [25033](#25033)

<!-- toc -->

# Info
## description
🏡 Open source home automation that puts local control and privacy first

# Markdown
## _README_rst
```Home Assistant |Chat Status|
=================================================================================

Home Assistant is a home automation platform running on Python 3. It is able to track and control all devices at home and offer a platform for automating control.

To get started:

.. code:: bash

    python3 -m pip install homeassistant
    hass --open-ui

Check out `home-assistant.io <https://home-assistant.io>`__ for `a
demo <https://home-assistant.io/demo/>`__, `installation instructions <https://home-assistant.io/getting-started/>`__,
`tutorials <https://home-assistant.io/getting-started/automation-2/>`__ and `documentation <https://home-assistant.io/docs/>`__.

|screenshot-states|

Featured integrations
---------------------

|screenshot-components|

The system is built using a modular approach so support for other devices or actions can be implemented easily. See also the `section on architecture <https://developers.home-assistant.io/docs/en/architecture_index.html>`__ and the `section on creating your own
components <https://developers.home-assistant.io/docs/en/creating_component_index.html>`__.

If you run into issues while using Home Assistant or during development
of a component, check the `Home Assistant help section <https://home-assistant.io/help/>`__ of our website for further help and information.

.. |Chat Status| image:: https://img.shields.io/discord/330944238910963714.svg
   :target: https://discord.gg/c5DvZ4e
.. |screenshot-states| image:: https://raw.github.com/home-assistant/home-assistant/master/docs/screenshots.png
   :target: https://home-assistant.io/demo/
.. |screenshot-components| image:: https://raw.github.com/home-assistant/home-assistant/dev/docs/screenshot-components.png
   :target: https://home-assistant.io/integrations/
```
## _github_PULL_REQUEST_TEMPLATE_md
```## Breaking Change:

<!-- What is breaking and why we have to break it. Remove this section only if it was NOT a breaking change. -->

## Description:


**Related issue (if applicable):** fixes #<home-assistant issue number goes here>

**Pull request with documentation for [home-assistant.io](https://github.com/home-assistant/home-assistant.io) (if applicable):** home-assistant/home-assistant.io#<home-assistant.io PR number goes here>

## Example entry for `configuration.yaml` (if applicable):
'''yaml

'''

## Checklist:
  - [ ] The code change is tested and works locally.
  - [ ] Local tests pass with `tox`. **Your PR cannot be merged unless tests pass**
  - [ ] There is no commented out code in this PR.
  - [ ] I have followed the [development checklist][dev-checklist]

If user exposed functionality or configuration variables are added/changed:
  - [ ] Documentation added/updated in [home-assistant.io](https://github.com/home-assistant/home-assistant.io)

If the code communicates with devices, web services, or third-party tools:
  - [ ] [_The manifest file_][manifest-docs] has all fields filled out correctly. Update and include derived files by running `python3 -m script.hassfest`.
  - [ ] New or updated dependencies have been added to `requirements_all.txt` by running `python3 -m script.gen_requirements_all`.
  - [ ] Untested files have been added to `.coveragerc`.

If the code does not interact with devices:
  - [ ] Tests have been added to verify that the new code works.

[dev-checklist]: https://developers.home-assistant.io/docs/en/development_checklist.html
[manifest-docs]: https://developers.home-assistant.io/docs/en/creating_integration_manifest.html
```
## _CLA_md
```# Contributor License Agreement

'''
By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the Apache 2.0 license; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the Apache 2.0 license; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it) is maintained indefinitely
    and may be redistributed consistent with this project or the open
    source license(s) involved.
'''

## Attribution

The text of this license is available under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).  It is based on the Linux [Developer Certificate Of Origin](http://elinux.org/Developer_Certificate_Of_Origin), but is modified to explicitly use the Apache 2.0 license
and not mention sign-off.

## Signing

To sign this CLA you must first submit a pull request to a repository under the Home Assistant organization.

## Adoption

This Contributor License Agreement (CLA) was first announced on January 21st, 2017 in [this][cla-blog] blog post and adopted January 28th, 2017.

[cla-blog]: https://home-assistant.io/blog/2017/01/21/home-assistant-governance/
```
## _docs_source_api_event_rst
```.. _helpers_event_module:

:mod:`homeassistant.helpers.event`
----------------------------------

.. automodule:: homeassistant.helpers.event

.. autofunction:: track_state_change

.. autofunction:: track_point_in_time

.. autofunction:: track_point_in_utc_time

.. autofunction:: track_sunrise

.. autofunction:: track_sunset

.. autofunction:: track_utc_time_change

.. autofunction:: track_time_change
```
## _docs_source_api_homeassistant_rst
```homeassistant package
=====================

Subpackages
-----------

.. toctree::

    helpers
    util

Submodules
----------

bootstrap module
------------------------------

.. automodule:: homeassistant.bootstrap
    :members:
    :undoc-members:
    :show-inheritance:

config module
---------------------------

.. automodule:: homeassistant.config
    :members:
    :undoc-members:
    :show-inheritance:

const module
--------------------------

.. automodule:: homeassistant.const
    :members:
    :undoc-members:
    :show-inheritance:

core module
-------------------------

.. automodule:: homeassistant.core
    :members:
    :undoc-members:
    :show-inheritance:

exceptions module
-------------------------------

.. automodule:: homeassistant.exceptions
    :members:
    :undoc-members:
    :show-inheritance:

loader module
---------------------------

.. automodule:: homeassistant.loader
    :members:
    :undoc-members:
    :show-inheritance:


Module contents
---------------

.. automodule:: homeassistant
    :members:
    :undoc-members:
    :show-inheritance:
```
## _CODE_OF_CONDUCT_md
```# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [safety@home-assistant.io][email]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available [here][version].

## Adoption

This Code of Conduct was first adopted January 21st, 2017 and announced in [this][coc-blog] blog post.

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
[email]: mailto:safety@home-assistant.io
[coc-blog]: https://home-assistant.io/blog/2017/01/21/home-assistant-governance/
```
## _CONTRIBUTING_md
```# Contributing to Home Assistant

Everybody is invited and welcome to contribute to Home Assistant. There is a lot to do...if you are not a developer perhaps you would like to help with the documentation on [home-assistant.io](https://home-assistant.io/)? If you are a developer and have devices in your home which aren't working with Home Assistant yet, why not spend a couple of hours and help to integrate them?

The process is straight-forward.

 - Read [How to get faster PR reviews](https://github.com/kubernetes/community/blob/master/contributors/guide/pull-requests.md#best-practices-for-faster-reviews) by Kubernetes (but skip step 0)
 - Fork the Home Assistant [git repository](https://github.com/home-assistant/home-assistant).
 - Write the code for your device, notification service, sensor, or IoT thing.
 - Ensure tests work.
 - Create a Pull Request against the [**dev**](https://github.com/home-assistant/home-assistant/tree/dev) branch of Home Assistant.

Still interested? Then you should take a peek at the [developer documentation](https://developers.home-assistant.io/) to get more details.

```
## _docs_source_api_helpers_rst
```homeassistant.helpers package
=============================

Submodules
----------

homeassistant.helpers.aiohttp_client module
-------------------------------------------

.. automodule:: homeassistant.helpers.aiohttp_client
    :members:
    :undoc-members:
    :show-inheritance:


homeassistant.helpers.area_registry module
------------------------------------------

.. automodule:: homeassistant.helpers.area_registry
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.condition module
--------------------------------------

.. automodule:: homeassistant.helpers.condition
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.config_entry_flow module
----------------------------------------------

.. automodule:: homeassistant.helpers.config_entry_flow
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.config_validation module
----------------------------------------------

.. automodule:: homeassistant.helpers.config_validation
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.data_entry_flow module
--------------------------------------------

.. automodule:: homeassistant.helpers.data_entry_flow
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.deprecation module
----------------------------------------

.. automodule:: homeassistant.helpers.deprecation
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.device_registry module
--------------------------------------------

.. automodule:: homeassistant.helpers.device_registry
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.discovery module
--------------------------------------

.. automodule:: homeassistant.helpers.discovery
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.dispatcher module
---------------------------------------

.. automodule:: homeassistant.helpers.dispatcher
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.entity module
-----------------------------------

.. automodule:: homeassistant.helpers.entity
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.entity_component module
---------------------------------------------

.. automodule:: homeassistant.helpers.entity_component
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.entity_platform module
--------------------------------------------

.. automodule:: homeassistant.helpers.entity_platform
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.entity_registry module
--------------------------------------------

.. automodule:: homeassistant.helpers.entity_registry
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.entity_values module
------------------------------------------

.. automodule:: homeassistant.helpers.entity_values
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.entityfilter module
-----------------------------------------

.. automodule:: homeassistant.helpers.entityfilter
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.event module
----------------------------------

.. automodule:: homeassistant.helpers.event
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.icon module
---------------------------------

.. automodule:: homeassistant.helpers.icon
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.intent module
-----------------------------------

.. automodule:: homeassistant.helpers.intent
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.json module
---------------------------------

.. automodule:: homeassistant.helpers.json
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.location module
-------------------------------------

.. automodule:: homeassistant.helpers.location
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.logging module
------------------------------------

.. automodule:: homeassistant.helpers.logging
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.restore_state module
------------------------------------------

.. automodule:: homeassistant.helpers.restore_state
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.script module
-----------------------------------

.. automodule:: homeassistant.helpers.script
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.service module
------------------------------------

.. automodule:: homeassistant.helpers.service
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.signal module
-----------------------------------

.. automodule:: homeassistant.helpers.signal
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.state module
----------------------------------

.. automodule:: homeassistant.helpers.state
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.storage module
------------------------------------

.. automodule:: homeassistant.helpers.storage
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.sun module
--------------------------------

.. automodule:: homeassistant.helpers.sun
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.system_info module
----------------------------------------

.. automodule:: homeassistant.helpers.system_info
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.temperature module
----------------------------------------

.. automodule:: homeassistant.helpers.temperature
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.template module
-------------------------------------

.. automodule:: homeassistant.helpers.template
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.translation module
-----------------------------------------

.. automodule:: homeassistant.helpers.translation
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.helpers.typing module
-----------------------------------

.. automodule:: homeassistant.helpers.typing
    :members:
    :undoc-members:
    :show-inheritance:


Module contents
---------------

.. automodule:: homeassistant.helpers
    :members:
    :undoc-members:
    :show-inheritance:
```
## _github_ISSUE_TEMPLATE_md
```<!-- READ THIS FIRST:
- If you need additional help with this template please refer to https://www.home-assistant.io/help/reporting_issues/
- Make sure you are running the latest version of Home Assistant before reporting an issue: https://github.com/home-assistant/home-assistant/releases
- Frontend issues should be submitted to the home-assistant-polymer repository: https://github.com/home-assistant/home-assistant-polymer/issues
- iOS issues should be submitted to the home-assistant-iOS repository: https://github.com/home-assistant/home-assistant-iOS/issues
- Do not report issues for integrations if you are using custom integration: files in <config-dir>/custom_components
- This is for bugs only. Feature and enhancement requests should go in our community forum: https://community.home-assistant.io/c/feature-requests
- Provide as many details as possible. Paste logs, configuration sample and code into the backticks. Do not delete any text from this template!
-->

**Home Assistant release with the issue:**
<!--
- Frontend -> Developer tools -> Info
- Or use this command: hass --version
-->


**Last working Home Assistant release (if known):**


**Operating environment (Hass.io/Docker/Windows/etc.):**
<!--
Please provide details about your environment.
-->

**Integration:**
<!--
Please add the link to the documentation at https://www.home-assistant.io/integrations/ of the integration in question.
-->


**Description of problem:**



**Problem-relevant `configuration.yaml` entries and (fill out even if it seems unimportant):**
'''yaml

'''

**Traceback (if applicable):**
'''

'''

**Additional information:**

```
## _github_ISSUE_TEMPLATE_Bug_report_md
```---
name: Bug report
about: Create a report to help us improve

---

<!-- READ THIS FIRST:
- If you need additional help with this template please refer to https://www.home-assistant.io/help/reporting_issues/
- Make sure you are running the latest version of Home Assistant before reporting an issue: https://github.com/home-assistant/home-assistant/releases
- Frontend issues should be submitted to the home-assistant-polymer repository: https://github.com/home-assistant/home-assistant-polymer/issues
- iOS issues should be submitted to the home-assistant-iOS repository: https://github.com/home-assistant/home-assistant-iOS/issues
- Do not report issues for integrations if you are using a custom integration: files in <config-dir>/custom_components
- This is for bugs only. Feature and enhancement requests should go in our community forum: https://community.home-assistant.io/c/feature-requests
- Provide as many details as possible. Paste logs, configuration sample and code into the backticks. Do not delete any text from this template!
-->

**Home Assistant release with the issue:**
<!--
- Frontend -> Developer tools -> Info
- Or use this command: hass --version
-->


**Last working Home Assistant release (if known):**


**Operating environment (Hass.io/Docker/Windows/etc.):**
<!--
Please provide details about your environment.
-->

**Integration:**
<!--
Please add the link to the documentation at https://www.home-assistant.io/integrations/ of the integration in question.
-->


**Description of problem:**



**Problem-relevant `configuration.yaml` entries and (fill out even if it seems unimportant):**
'''yaml

'''

**Traceback (if applicable):**
'''

'''

**Additional information:**
```
## _docs_source_api_util_rst
```homeassistant.util package
==========================

Submodules
----------

homeassistant.util.async_ module
-------------------------------

.. automodule:: homeassistant.util.async_
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.util.color module
-------------------------------

.. automodule:: homeassistant.util.color
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.util.distance module
----------------------------------

.. automodule:: homeassistant.util.distance
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.util.dt module
----------------------------

.. automodule:: homeassistant.util.dt
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.util.location module
----------------------------------

.. automodule:: homeassistant.util.location
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.util.package module
---------------------------------

.. automodule:: homeassistant.util.package
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.util.temperature module
-------------------------------------

.. automodule:: homeassistant.util.temperature
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.util.unit_system module
-------------------------------------

.. automodule:: homeassistant.util.unit_system
    :members:
    :undoc-members:
    :show-inheritance:

homeassistant.util.yaml module
------------------------------

.. automodule:: homeassistant.util.yaml
    :members:
    :undoc-members:
    :show-inheritance:


Module contents
---------------

.. automodule:: homeassistant.util
    :members:
    :undoc-members:
    :show-inheritance:
```
## _LICENSE_md
```                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```
## _docs_source_index_rst
```================================
Home Assistant API Documentation
================================

Public API documentation for `Home Assistant developers`_.

Contents:

.. toctree::
   :maxdepth: 2
   :glob:

   api/*

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Home Assistant developers: https://developers.home-assistant.io/
```
## _docs_source_api_bootstrap_rst
```.. _bootstrap_module:

:mod:`homeassistant.bootstrap`
-------------------------

.. automodule:: homeassistant.bootstrap
    :members:
```
## _docs_source_api_device_tracker_rst
```.. _components_device_tracker_module:

:mod:`homeassistant.components.device_tracker`
----------------------------------------------

.. automodule:: homeassistant.components.device_tracker
    :members:

.. autoclass:: Device
    :members:
```
## _docs_source_api_entity_rst
```.. _helpers_entity_module:

:mod:`homeassistant.helpers.entity`
-----------------------------------

.. automodule:: homeassistant.helpers.entity

.. autoclass:: Entity
    :members:

.. autoclass:: ToggleEntity
    :members:
```
## _docs_source_api_core_rst
```.. _core_module:

:mod:`homeassistant.core`
-------------------------

.. automodule:: homeassistant.core

.. autoclass:: Config
    :members:

.. autoclass:: Event
    :members:

.. autoclass:: EventBus
    :members:

.. autoclass:: HomeAssistant
    :members:

.. autoclass:: State
    :members:

.. autoclass:: StateMachine
    :members:

.. autoclass:: ServiceCall
    :members:

.. autoclass:: ServiceRegistry
    :members:

Module contents
---------------

.. automodule:: homeassistant.core
    :members:
    :undoc-members:
    :show-inheritance:
```
# Inline
## _homeassistant_components_insteon_binary_sensor_py

## _homeassistant_components_tahoma_sensor_py

## _homeassistant_components_fitbit_init_py

## _homeassistant_components_zha_core_decorators_py

## _homeassistant_components_bbox_device_tracker_py

## _homeassistant_components_rmvtransport_init_py

## _homeassistant_components_ifttt_const_py

## _tests_components_seventeentrack_test_sensor_py

## _tests_components_luftdaten_init_py

## _tests_components_wunderground_test_sensor_py

## _homeassistant_components_ephember_init_py

## _tests_components_api_streams_init_py

## _homeassistant_components_pushetta_init_py

## _homeassistant_components_nilu_air_quality_py

## _tests_components_workday_test_binary_sensor_py
### Line 16-25
```

    def setup_method(self):
        """Set up things to be run when tests are started."""
        self.hass = get_test_home_assistant()

        # Set valid default config for test
        self.config_province = {
            "binary_sensor": {"platform": "workday", "country": "DE", "province": "BW"}
        }


```
### Line 75-84
```
            setup_component(self.hass, "binary_sensor", self.config_province)

        entity = self.hass.states.get("binary_sensor.workday_sensor")
        assert entity is not None

    # Freeze time to a workday - Mar 15th, 2017
    @patch(FUNCTION_PATH, return_value=date(2017, 3, 15))
    def test_workday_province(self, mock_date):
        """Test if workdays are reported correctly."""
        with assert_setup_component(1, "binary_sensor"):

```
### Line 87-96
```
        self.hass.start()

        entity = self.hass.states.get("binary_sensor.workday_sensor")
        assert entity.state == "on"

    # Freeze time to a weekend - Mar 12th, 2017
    @patch(FUNCTION_PATH, return_value=date(2017, 3, 12))
    def test_weekend_province(self, mock_date):
        """Test if weekends are reported correctly."""
        with assert_setup_component(1, "binary_sensor"):

```
### Line 99-108
```
        self.hass.start()

        entity = self.hass.states.get("binary_sensor.workday_sensor")
        assert entity.state == "off"

    # Freeze time to a public holiday in province BW - Jan 6th, 2017
    @patch(FUNCTION_PATH, return_value=date(2017, 1, 6))
    def test_public_holiday_province(self, mock_date):
        """Test if public holidays are reported correctly."""
        with assert_setup_component(1, "binary_sensor"):

```
### Line 119-128
```
            setup_component(self.hass, "binary_sensor", self.config_noprovince)

        entity = self.hass.states.get("binary_sensor.workday_sensor")
        assert entity is not None

    # Freeze time to a public holiday in province BW - Jan 6th, 2017
    @patch(FUNCTION_PATH, return_value=date(2017, 1, 6))
    def test_public_holiday_noprovince(self, mock_date):
        """Test if public holidays are reported correctly."""
        with assert_setup_component(1, "binary_sensor"):

```
### Line 131-140
```
        self.hass.start()

        entity = self.hass.states.get("binary_sensor.workday_sensor")
        assert entity.state == "on"

    # Freeze time to a public holiday in state CA - Mar 31st, 2017
    @patch(FUNCTION_PATH, return_value=date(2017, 3, 31))
    def test_public_holiday_state(self, mock_date):
        """Test if public holidays are reported correctly."""
        with assert_setup_component(1, "binary_sensor"):

```
### Line 143-152
```
        self.hass.start()

        entity = self.hass.states.get("binary_sensor.workday_sensor")
        assert entity.state == "off"

    # Freeze time to a public holiday in state CA - Mar 31st, 2017
    @patch(FUNCTION_PATH, return_value=date(2017, 3, 31))
    def test_public_holiday_nostate(self, mock_date):
        """Test if public holidays are reported correctly."""
        with assert_setup_component(1, "binary_sensor"):

```
### Line 163-172
```
            setup_component(self.hass, "binary_sensor", self.config_invalidprovince)

        entity = self.hass.states.get("binary_sensor.workday_sensor")
        assert entity is None

    # Freeze time to a public holiday in province BW - Jan 6th, 2017
    @patch(FUNCTION_PATH, return_value=date(2017, 1, 6))
    def test_public_holiday_includeholiday(self, mock_date):
        """Test if public holidays are reported correctly."""
        with assert_setup_component(1, "binary_sensor"):

```
### Line 175-184
```
        self.hass.start()

        entity = self.hass.states.get("binary_sensor.workday_sensor")
        assert entity.state == "on"

    # Freeze time to a saturday to test offset - Aug 5th, 2017
    @patch(FUNCTION_PATH, return_value=date(2017, 8, 5))
    def test_tomorrow(self, mock_date):
        """Test if tomorrow are reported correctly."""
        with assert_setup_component(1, "binary_sensor"):

```
### Line 187-196
```
        self.hass.start()

        entity = self.hass.states.get("binary_sensor.workday_sensor")
        assert entity.state == "off"

    # Freeze time to a saturday to test offset - Aug 5th, 2017
    @patch(FUNCTION_PATH, return_value=date(2017, 8, 5))
    def test_day_after_tomorrow(self, mock_date):
        """Test if the day after tomorrow are reported correctly."""
        with assert_setup_component(1, "binary_sensor"):

```
### Line 199-208
```
        self.hass.start()

        entity = self.hass.states.get("binary_sensor.workday_sensor")
        assert entity.state == "on"

    # Freeze time to a saturday to test offset - Aug 5th, 2017
    @patch(FUNCTION_PATH, return_value=date(2017, 8, 5))
    def test_yesterday(self, mock_date):
        """Test if yesterday are reported correctly."""
        with assert_setup_component(1, "binary_sensor"):

```

## _homeassistant_components_rmvtransport_sensor_py
### Line 236-245
```
            _LOGGER.warning("Could not retrive data from rmv.de")
            return
        self.station = _data.get("station")
        _deps = []
        for journey in _data["journeys"]:
            # find the first departure meeting the criteria
            _nextdep = {ATTR_ATTRIBUTION: ATTRIBUTION}
            if self._destinations:
                dest_found = False
                for dest in self._destinations:

```

## _homeassistant_components_mopar_lock_py

## _homeassistant_components_egardia_alarm_control_panel_py
### Line 108-117
```
        return status

    def parsestatus(self, status):
        """Parse the status."""
        _LOGGER.debug("Parsing status %s", status)
        # Ignore the statuscode if it is IGNORE
        if status.lower().strip() != REPORT_SERVER_CODES_IGNORE:
            _LOGGER.debug("Not ignoring status %s", status)
            newstatus = STATES.get(status.upper())
            _LOGGER.debug("newstatus %s", newstatus)

```

## _tests_components_withings_test_init_py

## _homeassistant_components_lametric_notify_py
### Line 68-77
```
        icon = self._icon
        cycles = self._cycles
        sound = None
        priority = self._priority

        # Additional data?
        if data is not None:
            if "icon" in data:
                icon = data["icon"]
            if "sound" in data:

```

# Issues
## 11045
Title:
```

        Google Assistant, voice comes after command?
      
```
Author:
```
olskar
```
Text:
```

Make sure you are running the latest version of Home Assistant before reporting an issue.
You should only file an issue if you found a bug. Feature and enhancement requests should go in the Feature Requests section of our community forum:
Home Assistant release (hass --version):
0.59.2
Python release (python3 --version):
Component/platform:
google-assistant
Description of problem:
When using the google assistant component in hass, the voice of google home comes after the command has been run. E.g I say "Turn of all lights", and then after all lights has been turned off, my google home answers "Ok, turning all lights of"
Expected:
The opposite, E.g I say "Turn of all lights", my google home answer, "ok turning of all lights" then turning of all lights
Problem-relevant configuration.yaml entries and steps to reproduce:
google_assistant:
  project_id: XXXXX
  client_id: XXXXX
  access_token: XXXXX
  api_key: XXXXX
  exposed_domains:
    - light
    - climate






Traceback (if applicable):

Additional info:

```
Author:
```
DubhAd
```
Text:
```

This is something you'd need to raise with Google, since it's down to how they order the actions and not something that Home Assistant can control.

```
Author:
```
dshokouhi
```
Text:
```

I am actually pretty happy that it happens faster than Google can say its been done.  It is actually faster than SmartThings.

```
Author:
```
ferdydek
```
Text:
```

This is intentional (by Google), as it has to first attempt to execute the command to get any potential errors and give them back to the user.
@olskar you should close the issue.

```
Author:
```
olskar
```
Text:
```

@ferdydek Are you sure about that? With IFTTT and hue bulbs, it is doing the "right order". But if youre sure im closing it

```
Author:
```
ferdydek
```
Text:
```

Let me put it this way - what HA's google assistant integration does is identical to how other smart home hubs (for example Philips hue) are behaving.
If you feel that we should have an option to choose if the GA behaves in both ways please create a new Feature Requests (https://community.home-assistant.io/c/feature-requests).

```

## 22582
Title:
```

        Stream record test is flaky
      
```
Author:
```
awarecan
```
Text:
```

Home Assistant release with the issue:
dev branch (0.91+)
Last working Home Assistant release (if known):
Operating environment (Hass.io/Docker/Windows/etc.):
Component/platform:
stream
Description of problem:
tests/components/stream/test_recorder.py::test_record_stream test randomly failed CI environment
For example:
https://circleci.com/gh/home-assistant/home-assistant/1155
I am not understanding why @hunterjm want to test segments == 3, is segments > 1 enough?
Problem-relevant configuration.yaml entries and (fill out even if it seems unimportant):

Traceback (if applicable):
__________________________ test_record_stream[pyloop] __________________________

hass = <homeassistant.core.HomeAssistant object at 0x7fdb80c43be0>
hass_client = <function hass_client.<locals>.auth_client at 0x7fdb80c488c8>

    async def test_record_stream(hass, hass_client):
        """
        Test record stream.
    
        Purposefully not mocking anything here to test full
        integration with the stream component.
        """
        await async_setup_component(hass, 'stream', {
            'stream': {}
        })
    
        with patch(
                'homeassistant.components.stream.recorder.recorder_save_worker'):
            # Setup demo track
            source = generate_h264_video()
            stream = preload_stream(hass, source)
            recorder = stream.add_provider('recorder')
            stream.start()
    
            segments = 0
            while True:
                segment = await recorder.recv()
                if not segment:
                    break
                segments += 1
    
            stream.stop()
    
>           assert segments == 3
E           assert 2 == 3
E             -2
E             +3

tests/components/stream/test_recorder.py:44: AssertionError
---------------------------- Captured stderr setup -----------------------------
DEBUG:asyncio:Using selector: EpollSelector
------------------------------ Captured log setup ------------------------------
selector_events.py          54 DEBUG    Using selector: EpollSelector
----------------------------- Captured stderr call -----------------------------
INFO:homeassistant.loader:Loaded stream from homeassistant.components.stream
INFO:homeassistant.loader:Loaded http from homeassistant.components.http
INFO:homeassistant.setup:Setting up http
INFO:homeassistant.setup:Setup of domain http took 0.0 seconds.
DEBUG:homeassistant.core:Bus:Handling <Event component_loaded[L]: component=http>
INFO:homeassistant.setup:Setting up stream
DEBUG:homeassistant.core:Bus:Handling <Event service_registered[L]: domain=stream, service=record>
INFO:homeassistant.setup:Setup of domain stream took 0.0 seconds.
DEBUG:homeassistant.core:Bus:Handling <Event component_loaded[L]: component=stream>
INFO:homeassistant.components.stream:Started stream: <_io.BytesIO object at 0x7fdb80bf2150>
ERROR:homeassistant.components.stream.worker:Error demuxing stream: No dts in packet
INFO:homeassistant.components.stream:Stopped stream: <_io.BytesIO object at 0x7fdb80bf2150>
------------------------------ Captured log call -------------------------------
loader.py                  197 INFO     Loaded stream from homeassistant.components.stream
loader.py                  197 INFO     Loaded http from homeassistant.components.http
setup.py                   137 INFO     Setting up http
setup.py                   163 INFO     Setup of domain http took 0.0 seconds.
core.py                    541 DEBUG    Bus:Handling <Event component_loaded[L]: component=http>
setup.py                   137 INFO     Setting up stream
core.py                    541 DEBUG    Bus:Handling <Event service_registered[L]: domain=stream, service=record>
setup.py                   163 INFO     Setup of domain stream took 0.0 seconds.
core.py                    541 DEBUG    Bus:Handling <Event component_loaded[L]: component=stream>
__init__.py                175 INFO     Started stream: <_io.BytesIO object at 0x7fdb80bf2150>
worker.py                   81 ERROR    Error demuxing stream: No dts in packet
__init__.py                191 INFO     Stopped stream: <_io.BytesIO object at 0x7fdb80bf2150>
--------------------------- Captured stderr teardown ---------------------------
DEBUG:homeassistant.core:Bus:Handling <Event homeassistant_stop[L]>
INFO:homeassistant.components.stream:Stopped stream workers.
INFO:tests.common:Writing data to auth: {'version': 1, 'key': 'auth', 'data': {'users': [{'id': '4fe1a9e3972d46d6b1c509252f7fe38c', 'group_ids': ['system-admin'], 'is_owner': False, 'is_active': True, 'name': 'Mock User', 'system_generated': False}], 'groups': [{'id': 'system-admin', 'name': 'Administrators'}, {'id': 'system-users', 'name': 'Users'}, {'id': 'system-read-only', 'name': 'Read Only'}], 'credentials': [], 'refresh_tokens': [{'id': 'a2fd577e46c14446becde169c3ade7ea', 'user_id': '4fe1a9e3972d46d6b1c509252f7fe38c', 'client_id': 'https://example.com/app', 'client_name': None, 'client_icon': None, 'token_type': 'normal', 'created_at': '2019-03-31T06:28:29.490927+00:00', 'access_token_expiration': 1800.0, 'token': '51869528854d090511fd8de88807b8ed0c62249ab9558c850e74cc6fca4a9eae479551965378be0803bb73abe546625c1f619854f944c0dc611fdd3fe6e8a5b1', 'jwt_key': 'fb6e4e36b9c618fffad611d6c39f7f8c1c36761a5ad8dcde17512efd19a0e77ff55c865e29657f7821cea5a35435ea62d7fcc9fffeb6fb8fa6fc060960832483', 'last_used_at': '2019-03-31T06:28:29.491045+00:00', 'last_used_ip': None}]}}
DEBUG:homeassistant.core:Bus:Handling <Event homeassistant_close[L]>
---------------------------- Captured log teardown -----------------------------
core.py                    541 DEBUG    Bus:Handling <Event homeassistant_stop[L]>
__init__.py                108 INFO     Stopped stream workers.
common.py                  874 INFO     Writing data to auth: {'version': 1, 'key': 'auth', 'data': {'users': [{'id': '4fe1a9e3972d46d6b1c509252f7fe38c', 'group_ids': ['system-admin'], 'is_owner': False, 'is_active': True, 'name': 'Mock User', 'system_generated': False}], 'groups': [{'id': 'system-admin', 'name': 'Administrators'}, {'id': 'system-users', 'name': 'Users'}, {'id': 'system-read-only', 'name': 'Read Only'}], 'credentials': [], 'refresh_tokens': [{'id': 'a2fd577e46c14446becde169c3ade7ea', 'user_id': '4fe1a9e3972d46d6b1c509252f7fe38c', 'client_id': 'https://example.com/app', 'client_name': None, 'client_icon': None, 'token_type': 'normal', 'created_at': '2019-03-31T06:28:29.490927+00:00', 'access_token_expiration': 1800.0, 'token': '51869528854d090511fd8de88807b8ed0c62249ab9558c850e74cc6fca4a9eae479551965378be0803bb73abe546625c1f619854f944c0dc611fdd3fe6e8a5b1', 'jwt_key': 'fb6e4e36b9c618fffad611d6c39f7f8c1c36761a5ad8dcde17512efd19a0e77ff55c865e29657f7821cea5a35435ea62d7fcc9fffeb6fb8fa6fc060960832483', 'last_used_at': '2019-03-31T06:28:29.491045+00:00', 'last_used_ip': None}]}}
core.py                    541 DEBUG    Bus:Handling <Event homeassistant_close[L]>

Additional information:

```
Author:
```
hunterjm
```
Text:
```

Was 3 locally. Checking >1 is probably fine. Maybe due to differing FFMPEG versions and defaults when generating the test video?

```

## 27959
Title:
```

        SolarEdge - Missing connections in power flow data
      
```
Author:
```
Beertje135
```
Text:
```

Home Assistant release with the issue:
0.100.2
Last working Home Assistant release (if known):
Before the move of SolarEdge from sensors to its own integration.
Operating environment (Hass.io/Docker/Windows/etc.):
Hass.io 
Integration:
https://www.home-assistant.io/integrations/solaredge
Description of problem:
Error for Missing connections in power flow data appears about 100 times per day.
Error Log:
Missing connections in power flow data
13:06 components/solaredge/sensor.py (ERROR) - message first occured at 18 oktober 2019 21:40 and shows up 230 times
and/or
2019-10-18 21:50:43 ERROR (SyncWorker_18) [homeassistant.components.solaredge.sensor] Missing connections in power flow data
Problem-relevant configuration.yaml entries and (fill out even if it seems unimportant):
solaredge:
  api_key: !secret api_key_solar_edge
  site_id: !secret client_id_solar_edge
Traceback (if applicable):
Not Applicable

Additional information:
https://community.home-assistant.io/t/solaredge-new-top-level-entry-missing-connections-in-power-flow-data/138170?u=bve

```

## 15188
Title:
```

        No State History Found
      
```
Author:
```
geastman4353
```
Text:
```

As the title reads, none of my devices are registering a state history

```
Author:
```
cgarwood
```
Text:
```

Please fill out the issue template. What version of HomeAssistant are you running? What installation method? What is your recorder: setup? Are there any errors in the HomeAssistant log?

```
Author:
```
geastman4353
```
Text:
```

Running Hassio Version 109 - Homeassistant Verison 0.72.1
Where would i find the recorder setup? I don't have anything in my configuration file for recorder and I never have but this is a recent issue. There are several errors in the HA log but they all appear to be based around WeatherUnderground or MyQ and seem to be internet related.

```
Author:
```
cgarwood
```
Text:
```

If there's not a recorder: line in your configuration.yaml then that's why there's no state history.
https://www.home-assistant.io/components/recorder has info on setting up the recorder

```
Author:
```
geastman4353
```
Text:
```

I'll give that a try. I'm not sure when that changed because I never had that line in there and never had an issue with state history before. I've updated the config file and I'll see if that works.

```
Author:
```
geastman4353
```
Text:
```

I've added the recorder line to my configuration and there is no change.
I have the following lines in my config:
history:
logbook:
recorder: 
I'm not seeing anything in history or logbook since I think 2 updates ago.



```
Author:
```
kylerw
```
Text:
```

I have the same issue. 0.73.1
recorder:
  purge_interval: 1
  purge_keep_days: 3
  db_url: !secret recorder_db_url
  exclude:
    domains:
      - automation
      - weblink
      - updater
    entities:
      - sun.sun


```
Author:
```
jurriaan
```
Text:
```

Same here, latest master, using Postgresql with recorder. Tables are a filled with recent data when looking manually.
> select max(last_updated) from states;
             max              
------------------------------
 2018-07-31 20:38:30.28531+00
(1 row)


```
Author:
```
jasonmhite
```
Text:
```

Also have this problem. Clicking on an entity in the frontend to view state history does not pop up the normal window, it only produces a message that the system_log.write service was called. Looking at the log the following message this is there:
ERROR (MainThread) [frontend.js.es5.201808310] http://x.x.x.x:8123/frontend_es5/app-8dfe9b8d.js:2:801147 Uncaught 

The message is clipped, but I am guessing there is some sort of exception in the frontend when trying to draw the history window.
My setup is also using postgres with pretty standard configurations for recorder and history. I can see recent updates in the database as well so the connection is fine and HA is logging stuff. It was otherwise working before upgrading from 0.75.3 to 0.77.2, though I definitely had it properly display the history window at least once on 0.77.2.
Update: this seems to be browser dependent. Works using Firefox, but not Vivaldi (based on Chromium).

```
Author:
```
ktpx
```
Text:
```

I have the same problem in the front end, that is, the history window when clicking entities does not show, only the service called.  Works on all other browsers...should open in issue for this.

```
Author:
```
jasonmhite
```
Text:
```

@ktpx What browser are you using?

```
Author:
```
AlfieJ04
```
Text:
```

I resolved this issue by renaming the home-assistant_v2.db to .old and then restarted HA which rebuilt my database.
Hope this helps someone.
A

```
Author:
```
ktpx
```
Text:
```


@ktpx What browser are you using?

It's only in vivaldi this happens (no graphs or popups)...which is my main browser, but now back on opera due to this problem.

```
Author:
```
jasonmhite
```
Text:
```

I tried clearing the db as well, no effect. I think we might have two separate issues here.
@ktpx Do you get any more detail in your log messages? Like I mentioned, mine is cut off in the logfile and I just get "Uncaught". It seems to be something with Vivaldi, but it's weird because Vivaldi's browser engine is the same as Chrome, but it works fine in Chrome for me.

```
Author:
```
jasonmhite
```
Text:
```

I wonder if this perhaps has to do with home-assistant/home-assistant-polymer#1624 ? It seems like a frontend issue since it works for me in other browsers. Unfortunately, I tried adding javascript_version: latest as was suggested over there and it didn't help, but it's a start. I gonna dive into this more and possibly open another issue over there.

```
Author:
```
balloobbot
```
Text:
```

There hasn't been any activity on this issue recently. Due to the high number of incoming GitHub notifications, we have to clean some of the old issues, as many of them have already been resolved with the latest updates.
Please make sure to update to the latest Home Assistant version and check if that solves the issue. Let us know if that works for you by adding a comment 👍

```
Author:
```
jasonmhite
```
Text:
```

@balloobbot This issue is still present in current versions. There's been no change, it still doesn't work.
I do think this issue is somehow specific to Vivaldi, which is strange because Vivaldi is reusing Chrome's rendering engine but I do not have this problem on Chrome. I don't really know how to debug this though, because there is no meaningful error message.

```
Author:
```
JuniorGamingTime
```
Text:
```

Is this still an issue you are experiencing? Can you please try upgrading to the latest version of Home Assistant (0.90) and report back if this is still a problem? Thanks!

```
Author:
```
jasonmhite
```
Text:
```

@JuniorGamingTime Yes, still a problem.

```
Author:
```
stale
```
Text:
```

There hasn't been any activity on this issue recently. Due to the high number of incoming GitHub notifications, we have to clean some of the old issues, as many of them have already been resolved with the latest updates.
Please make sure to update to the latest Home Assistant version and check if that solves the issue. Let us know if that works for you by adding a comment 👍
This issue now has been marked as stale and will be closed if no further activity occurs. Thank you for your contributions.

```
Author:
```
jasonmhite
```
Text:
```

This issue is still a problem.

```
Author:
```
Geoff571
```
Text:
```

Still a problem. Hassio 0.97.2
Logbook shows data, individual sensors show history when put into a history-graph card, but nothing on the UI History page.
It was working up until I switched to using MariaDB, then worked once never to be seen again. I even reverted back from using MariaDB and still no History.

```
Author:
```
lancusfpv
```
Text:
```

Is there any solution to this problem? I have 0.98.2 version and no state history found error on history tab.

```
Author:
```
nekomona
```
Text:
```

Same issue met and fixed on 0.99.2 with stock SQLite.
The issue happened when I rebooted my Pi for the first time. All the history and logbook are blanked, viewed both from the Lovelace and API, while the db file is still growing.
Renaming db file didn't work. However, when I renamed the .homeassistant folder and start hass again, the hass cannot automatically install and import certain packages. When I manually installed those packages through pip and renamed back my original folder, the system was back to work.
The packages I manually installed are netdisco==2.6.0 , hass-nabucasa==0.17 and home-assistant-frontend==20190919.0 .
I have little idea about the cause since all three packages are shown as "Attempting to install" in the log. Anyway it worked for me and the issue didn't show up again after rebooting.

```

## 22352
Title:
```

        Assume this is IP based.
      
```
Author:
```
ranunculales
```
Text:
```

Home Assistant release with the issue: 0.90.0 to 0.90.1
Last working Home Assistant release (if known): 0.89.2
Operating environment (Hass.io/Docker/Windows/etc.): Hass.io / Docker CE / Intel NUC / Ubuntu Server 18.0.4 LTS
Component/platform:  Appears to be - homekit_controller?
Description of problem:
Upgraded from 0.89.2 to 0.90.0 (and 0.90.1) and on boot, Hass.io fills my logs with about 27 of these tracebacks, all with different "MACs". I put those in quotes because these MACs are nowhere in my wireless controller (first thought, since it says "assuming IP based") and any OUI lookup I've spot checked returns unknown results.
Nothing seems broken so far, other than my OCD that there are logs I can't explain.
Problem-relevant configuration.yaml entries and (fill out even if it seems unimportant): Unknown at this point...

Traceback (if applicable):
8:52 AM components/homekit_controller/__init__.py (WARNING)

Log Details (WARNING)
Sun Mar 24 2019 08:52:30 GMT-0700 (PDT)

Loaded pairing for 8A:AB:9F:D5:4F:F8 with missing connection type. Assume this is IP based.

Additional information:

```
Author:
```
Jc2k
```
Text:
```

This is just a warning from an upstream library and is not a traceback as such.
The upstream library now supports IP and BLE connection types, and it assumes existing records are IP based but warns that your pairing.json is in an old format. This warning is completely harmless - it takes the right course of action.
These are HomeKit ID's no MAC addresses. They change every time you reset a device and are completely random. There will be one for every time you have done a homekit pairing, and you have 27 HomeKit pairings in your system. I'm guessing you don't have that many devices but have done a bunch of hard reset and re-pairs?
There is no mechanism for cleaning out old pairings through HA - this will be fixed by a branch I have in flight but the HA devs are really busy so getting even small PR's reviewed and merged takes time. In the meantime you can reduce the warnings by removing old records from your pairing.json file. If your configuration.yaml is in /config/ then you should have a /config/.homekit/pairing.json. There will be a bunch of other files in that folder starting with hk - you don't need them any more. Other than that, theres no easy way to tell which pairings are active. I think you can do something like python3 -m homekit.discover to see all active IP accessories on your network with their current homekit id.
For the remaining records you can totally fix your OCD by adding a "Connection": "IP" entry to each pairing.
Finally, the nuclear option is to rm (or mv to one side) your .homekit folder to one side and do one more reset and re-pair option. Then you'll only have one pairing per device and it should (i think) have the right Connection type set in pairing.json.
(Of course a future version will do the migration automatically, this is all purely to help your OCD until all of my outstanding branches are merged)

```
Author:
```
ranunculales
```
Text:
```

As always @Jc2k, you are beyond helpful; thank you for that detailed explanation, it's very much appreciated. I have 24 HomeKit devices (I was going all in before I stumbled on HA), with only a few resets... but no need to keep something open if the only thing that's broken is my OCD.

```

## 718
Title:
```

        z-wave fibaro FGMS-001 not added
      
```
Author:
```
kmadac
```
Text:
```

Hello, I have my first z-wave device which is fibaro multi sensor (motion, temperature, lux) here and z-wave usb stick Vision ZU 1401 in Raspberry Pi.
I have home-assistant 0.9.1 installed and following configuration in config file:
zwave:
  usb_path: /dev/ttyACM0
  config_path: /usr/local/share/python-openzwave/config

after I start hass, file OZW_Log.txt is created in .homeassistant directory. I cannot see any error there:
2015-12-09 20:12:37.863 Detail, 
2015-12-09 20:12:37.864 Info, Node001, Received reply to FUNC_ID_ZW_GET_ROUTING_INFO
2015-12-09 20:12:37.864 Info, Node001,     Neighbors of this node are:
2015-12-09 20:12:37.864 Info, Node001,  (none reported)
2015-12-09 20:12:37.865 Detail, Node001,   Expected reply was received
2015-12-09 20:12:37.865 Detail, Node001,   Message transaction complete
2015-12-09 20:12:37.865 Detail, 
2015-12-09 20:12:37.865 Detail, Node001, Removing current message
2015-12-09 20:12:37.866 Detail, Node001, Query Stage Complete (Neighbors)
2015-12-09 20:12:37.866 Detail, Node001, AdvanceQueries queryPending=0 queryRetries=0 queryStage=Session live=1
2015-12-09 20:12:37.866 Detail, Node001, QueryStage_Session
2015-12-09 20:12:37.867 Detail, Node001, QueryStage_Dynamic
2015-12-09 20:12:37.867 Detail, Node001, QueryStage_Configuration
2015-12-09 20:12:37.867 Detail, Node001, QueryStage_Complete
2015-12-09 20:12:37.867 Warning, CheckCompletedNodeQueries m_allNodesQueried=0 m_awakeNodesQueried=0
2015-12-09 20:12:37.868 Warning, CheckCompletedNodeQueries all=1, deadFound=0 sleepingOnly=1
2015-12-09 20:12:37.868 Info,          Node query processing complete.
2015-12-09 20:19:06.714 Info, mgr,     Manager::WriteConfig completed for driver with home ID of 0xdf1e1fc0
2015-12-09 20:19:07.755 Info, mgr,     Driver for controller /dev/ttyACM0 pending removal
2015-12-09 20:19:07.755 Always, ***************************************************************************
2015-12-09 20:19:07.756 Always, *********************  Cumulative Network Statistics  *********************
2015-12-09 20:19:07.756 Always, *** General
2015-12-09 20:19:07.756 Always, Driver run time: . .  . 0 days, 0 hours, 6 minutes
2015-12-09 20:19:07.756 Always, Frames processed: . . . . . . . . . . . . . . . . . . . . 9
2015-12-09 20:19:07.757 Always, Total messages successfully received: . . . . . . . . . . 9
2015-12-09 20:19:07.757 Always, Total Messages successfully sent: . . . . . . . . . . . . 10
2015-12-09 20:19:07.757 Always, ACKs received from controller:  . . . . . . . . . . . . . 10
2015-12-09 20:19:07.757 Always, *** Errors
2015-12-09 20:19:07.758 Always, Unsolicited messages received while waiting for ACK:  . . 0
2015-12-09 20:19:07.758 Always, Reads aborted due to timeouts:  . . . . . . . . . . . . . 0
2015-12-09 20:19:07.758 Always, Bad checksum errors:  . . . . . . . . . . . . . . . . . . 0
2015-12-09 20:19:07.758 Always, CANs received from controller:  . . . . . . . . . . . . . 0
2015-12-09 20:19:07.759 Always, NAKs received from controller:  . . . . . . . . . . . . . 0
2015-12-09 20:19:07.759 Always, Out of frame data flow errors:  . . . . . . . . . . . . . 0
2015-12-09 20:19:07.759 Always, Messages retransmitted: . . . . . . . . . . . . . . . . . 0
2015-12-09 20:19:07.760 Always, Messages dropped and not delivered: . . . . . . . . . . . 0
2015-12-09 20:19:07.760 Always, ***************************************************************************
2015-12-09 20:19:07.762 Detail, WriteMsg Wait Timeout m_currentMsg=00000000
2015-12-09 20:19:09.770 Info, mgr,     Driver for controller /dev/ttyACM0 removed


Also in hass log file I see that z-wave controller started and also no errors there.
INFO:root:Driver ready using library b'Static Controller' version b'Z-Wave 3.41'
INFO:root:home_id 0xdf1e1fc0, controller node id is 1

I tried to set sensor to inclusion mode and restart home assistant, but even though I cannot see any error, I cannot see any new sensor in web interface of home assistant.
Should the sensor be added and visible to home assistant automatically or should add new sensor item into config file?

```
Author:
```
balloob
```
Text:
```

Is the sensor set up to report it's status to your controller stick?
Once the stick picks up a Value being broadcasted it will load the sensor platform and show the sensor in the UI.

```
Author:
```
kmadac
```
Text:
```

Hi, Thanks for info.
Yes, according to sensor documentation I briefly pushed button 3 times and sensor led shone blue, which should inclusion of sensro to z-wave network. But no new messages appeared in log file. I tried also minozw app from openzwave with the same behavior, so it seems that there something wrong with USB stick or sensor itself. I will do more investigation during weekend.

```
Author:
```
sebasdoes
```
Text:
```

I have a Fibaro Smoke Sensor. If I try to use it with Hass (last I tried is 0.8), it will not work with similar results as you. It works fine in Domoticz though.
Is this maybe because it's a sleeping sensor for most of the time? I forced it into sending data by triggering the burglary alarm to no avail

```
Author:
```
kmadac
```
Text:
```

It seems like compatibility issue between openzwave and USB Stick Vision ZU1401EU. On openzwave mailing list I found that same behavior was reported in June 2015 - https://groups.google.com/forum/#!searchin/openzwave/vision/openzwave/5FS5s0PsfRo/irVLhwPuDE4J.
@sebasdoes: What USB stick do you have?

```
Author:
```
sebasdoes
```
Text:
```

To be honest I don't know for certain. Let me give the lsusb:
Bus 001 Device 008: ID 0658:0200 Sigma Designs, Inc.
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass            2 Communications
  bDeviceSubClass         0
  bDeviceProtocol         0
  bMaxPacketSize0         8
  idVendor           0x0658 Sigma Designs, Inc.
  idProduct          0x0200
  bcdDevice            0.00
  iManufacturer           0
  iProduct                0
  iSerial                 1 12345678-9012-3456-7890-123456789012
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength           67
    bNumInterfaces          2
    bConfigurationValue     1
    iConfiguration          0
    bmAttributes         0x80
      (Bus Powered)
    MaxPower              100mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         2 Communications
      bInterfaceSubClass      2 Abstract (modem)
      bInterfaceProtocol      1 AT-commands (v.25ter)
      iInterface              0
      CDC Header:
        bcdCDC               1.10
      CDC Call Management:
        bmCapabilities       0x00
        bDataInterface          1
      CDC ACM:
        bmCapabilities       0x00
      CDC Union:
        bMasterInterface        0
        bSlaveInterface         1
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0008  1x 8 bytes
        bInterval              32
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       0
      bNumEndpoints           2
      bInterfaceClass        10 CDC Data
      bInterfaceSubClass      0 Unused
      bInterfaceProtocol      0
      iInterface              0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x82  EP 2 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0020  1x 32 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x02  EP 2 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0020  1x 32 bytes
        bInterval               0
Device Status:     0x0000
  (Bus Powered)

```
Author:
```
sebasdoes
```
Text:
```

I upgraded to the newest python-openzwave just to rule that out. My logs haven't changed, but might be of use. The OZW_Log.txt file shows this message when I trigger an alarm:
2015-12-13 09:36:37.252 Detail,
2015-12-13 09:36:37.254 Info, Node005, ApplicationCommandHandler - Unhandled Command Class 0x71
2015-12-13 09:36:37.356 Detail, Node005,   Received: 0x01, 0x0d, 0x00, 0x04, 0x08, 0x05, 0x07, 0x9c, 0x02, 0x05, 0x00, 0x00, 0x00, 0x00, 0x67
2015-12-13 09:36:37.358 Detail,
2015-12-13 09:36:37.359 Info, Node005, ApplicationCommandHandler - Unhandled Command Class 0x9c
2015-12-13 09:36:37.371 Detail, Node005,   Received: 0x01, 0x0d, 0x00, 0x04, 0x00, 0x05, 0x07, 0x9c, 0x02, 0x05, 0x00, 0x00, 0x00, 0x00, 0x6f
2015-12-13 09:36:37.373 Detail,
2015-12-13 09:36:37.375 Info, Node005, ApplicationCommandHandler - Unhandled Command Class 0x9c
2015-12-13 09:37:22.518 Detail, Node005,   Received: 0x01, 0x0c, 0x00, 0x04, 0x00, 0x05, 0x06, 0x31, 0x05, 0x01, 0x22, 0x00, 0xe3, 0x00
2015-12-13 09:37:22.522 Detail,
2015-12-13 09:37:22.531 Info, Node005, ApplicationCommandHandler - Unhandled Command Class 0x31

```
Author:
```
kmadac
```
Text:
```

Thanks for pasting your logs. It seems that you have different issue than me. In my log, I cannot see any communication of sensor. Only data from Node001, which is controller itself are in log. You have different USB stick than me, and according to openzwave mailing list, Vision USB doesn't work with openzwave correctly. I will return Vision USB and will order other one (Aeon probably).
I will leave the issue opened and will report situation, once new USB stick will arrive.

```
Author:
```
deisi
```
Text:
```

I also have the fibaro FGMS-001 sensor and besides some other python-openzwave issues it is running.

```
Author:
```
kmadac
```
Text:
```

I exchanged USB sticks. I sent back Vision USB and purchased Aeon Z-Stick Gen5. I had to copy most recent openzwave config directory into /usr/local/share/python-openzwave because reference to commit in openzwave submodule doesn't contain configuration for Gen5 version. Now, I can see all 3 values in HA, so I'm closing the issue.
Thanks for help guys.

```

## 5504
Title:
```

        scrip/setup fails if npm is not installed
      
```
Author:
```
xifle
```
Text:
```

Home Assistant release (hass --version):
0.36.1
Python release (python3 --version):
3.4.3
Component/platform:
script/setup
(fails in script/bootstrap_frontend)
Description of problem:
setup script won't install home-assistant if npm is not installed (on non-docker setup).
Introduced with commit  c864ea6
Expected:
Shouldn't fail if npm is not installed

```

## 16830
Title:
```

        Jewish calendar sensor error in beta
      
```
Author:
```
dshokouhi
```
Text:
```

Home Assistant release with the issue:
0.79.0b0
Last working Home Assistant release (if known):
n/a new platform
Operating environment (Hass.io/Docker/Windows/etc.):
venv
Component/platform:
Jewish Calendar sensor: https://rc--home-assistant-docs.netlify.com/components/sensor.jewish_calendar/
Description of problem:
After setting up the platform according to the docs I get an error
Problem-relevant configuration.yaml entries and (fill out even if it seems unimportant):
sensor:
 - platform: jewish_calendar
   language: english
   sensors:
   - date
   - holiday_name
   - first_stars
Traceback (if applicable):
2018-09-24 14:02:36 ERROR (MainThread) [homeassistant.components.sensor] jewish_calendar: Error on device update!
Traceback (most recent call last):
  File "/home/pi/home-assistant/homeassistant/helpers/entity_platform.py", line 251, in _async_add_entity
    await entity.async_device_update(warning=False)
  File "/home/pi/home-assistant/homeassistant/helpers/entity.py", line 350, in async_device_update
    yield from self.async_update()
  File "/home/pi/home-assistant/homeassistant/components/sensor/jewish_calendar.py", line 121, in async_update
    for x in hdate.htables.HOLIDAYS
  File "/home/pi/home-assistant/homeassistant/components/sensor/jewish_calendar.py", line 122, in <genexpr>
    if x.index == date.get_holyday())
AttributeError: 'str' object has no attribute 'long'

Additional information:

```
Author:
```
fabaff
```
Text:
```

@tsvi, looks like that the - holiday_name sensor is causing the issue.

```
Author:
```
tsvi
```
Text:
```

Ok, I see the bug. Most of my tests were for Hebrew. In case of setting language to english, the library does not provide a long description. I think this logic should be moved into the library in any case.

```

## 23865
Title:
```

        No Weather or HomeCoach devices found
      
```
Author:
```
CookieMonster87
```
Text:
```

Home Assistant release with the issue:
0.93b
Last working Home Assistant release (if known):
0.92.2
Operating environment (Hass.io/Docker/Windows/etc.):
Docker
Component/platform:
Netatmo
Description of problem:
After started using 0.93 dev and now 0.93b3 this error apperas on every boot/restart
No Weather or HomeCoach devices found for None
1:37 PM components/netatmo/sensor.py (ERROR)
Netatmo component is working without any issues so only this error log entry.

```
Author:
```
MartinHjelmare
```
Text:
```

Fixed in #23907.

```
Author:
```
jonathanbower
```
Text:
```

I'm still having this issue with 0.94.2

```
Author:
```
CookieMonster87
```
Text:
```

Yes can confirm still same issue on
0.94.3

```
Author:
```
CookieMonster87
```
Text:
```

@MartinHjelmare
Can this be opened again? still same problem on 0.94.3

```
Author:
```
maheus
```
Text:
```

same error here #24435

```
Author:
```
cgtobi
```
Text:
```

This is fixed in #24788.

```
Author:
```
CookieMonster87
```
Text:
```

@cgtobi
Almost fixed in 95.2 :) Now the error is No HomeCoach devices found instead of No Weather or HomeCoach devices found. Is it possible to fix so it does not log error if the netatmo account dont have the HomeCoach device?

```
Author:
```
cgtobi
```
Text:
```

It is just a warning. But I will probably have to work on it as it seems to confuse people.

```

## 5061
Title:
```

        Kodi media player status unstable
      
```
Author:
```
liquidox
```
Text:
```

Make sure you are running the latest version of Home Assistant before reporting an issue.
You should only file an issue if you found a bug. Feature and enhancement requests should go in the Feature Requests section of our community forum:
Home Assistant release (hass --version):
0.35.0
Python release (python3 --version):
Python 3.5.2
Component/platform:
Kodi, media player
Description of problem:
I use the "playing" status on the Kodi component to dim our lights automatically. This works perfectly fine while playing regular media files. However, when playing Youtube or Twitch for example, the lights will start fading on/off constantly, seemingly thinking Kodi is both on and off all the time.
Expected:
No blinking.

```
Author:
```
jchapple
```
Text:
```

This also happens with LiveTV PVR recordings that are still recording while watching.

```
Author:
```
Zac-HD
```
Text:
```

Based on this line of code, I'd guess it's something to do with the live property.  However that's all the troubleshooting I can do without a device of my own!

```
Author:
```
sacotter
```
Text:
```

I am having the same issue.
hass: 0.35.2
Python: 3.4.2
Lights are flashing on/off every 10 s which matches the log below.
log snip of grep home-assistant.log -e "state automation.media_player":

17-02-05 19:40:41 homeassistant.core: Bus:Handling <Event state_changed[L]: old_state=<state automation.media_player_pausedstopped=on; last_triggered=2017-02-05T19:40:31.706632-05:00, friendly_name=Media player paused/stopped @ 2017-02-05T19:10:04.250068-05:00>, entity_id=automation.media_player_pausedstopped, new_state=<state automation.media_player_pausedstopped=on; last_triggered=2017-02-05T19:40:41.039384-05:00, friendly_name=Media player paused/stopped @ 2017-02-05T19:10:04.250068-05:00>>
17-02-05 19:40:41 homeassistant.components.websocket_api: WS 140176765522888: Sending {'id': 2, 'event': {'origin': 'LOCAL', 'time_fired': datetime.datetime(2017, 2, 6, 0, 40, 41, 39683, tzinfo=), 'event_type': 'state_changed', 'data': {'old_state': <state automation.media_player_pausedstopped=on; last_triggered=2017-02-05T19:40:31.706632-05:00, friendly_name=Media player paused/stopped @ 2017-02-05T19:10:04.250068-05:00>, 'entity_id': 'automation.media_player_pausedstopped', 'new_state': <state automation.media_player_pausedstopped=on; last_triggered=2017-02-05T19:40:41.039384-05:00, friendly_name=Media player paused/stopped @ 2017-02-05T19:10:04.250068-05:00>}}, 'type': 'event'}
17-02-05 19:40:41 homeassistant.core: Bus:Handling <Event state_changed[L]: old_state=<state automation.media_player_playing=on; last_triggered=2017-02-05T19:40:31.720079-05:00, friendly_name=Media player playing @ 2017-02-05T19:10:04.277505-05:00>, entity_id=automation.media_player_playing, new_state=<state automation.media_player_playing=on; last_triggered=2017-02-05T19:40:41.071529-05:00, friendly_name=Media player playing @ 2017-02-05T19:10:04.277505-05:00>>
17-02-05 19:40:41 homeassistant.components.websocket_api: WS 140176765522888: Sending {'id': 2, 'event': {'origin': 'LOCAL', 'time_fired': datetime.datetime(2017, 2, 6, 0, 40, 41, 71710, tzinfo=), 'event_type': 'state_changed', 'data': {'old_state': <state automation.media_player_playing=on; last_triggered=2017-02-05T19:40:31.720079-05:00, friendly_name=Media player playing @ 2017-02-05T19:10:04.277505-05:00>, 'entity_id': 'automation.media_player_playing', 'new_state': <state automation.media_player_playing=on; last_triggered=2017-02-05T19:40:41.071529-05:00, friendly_name=Media player playing @ 2017-02-05T19:10:04.277505-05:00>}}, 'type': 'event'}
17-02-05 19:40:51 homeassistant.core: Bus:Handling <Event state_changed[L]: old_state=<state automation.media_player_pausedstopped=on; last_triggered=2017-02-05T19:40:41.039384-05:00, friendly_name=Media player paused/stopped @ 2017-02-05T19:10:04.250068-05:00>, entity_id=automation.media_player_pausedstopped, new_state=<state automation.media_player_pausedstopped=on; last_triggered=2017-02-05T19:40:51.160414-05:00, friendly_name=Media player paused/stopped @ 2017-02-05T19:10:04.250068-05:00>>
17-02-05 19:40:51 homeassistant.components.websocket_api: WS 140176765522888: Sending {'id': 2, 'event': {'origin': 'LOCAL', 'time_fired': datetime.datetime(2017, 2, 6, 0, 40, 51, 160719, tzinfo=), 'event_type': 'state_changed', 'data': {'old_state': <state automation.media_player_pausedstopped=on; last_triggered=2017-02-05T19:40:41.039384-05:00, friendly_name=Media player paused/stopped @ 2017-02-05T19:10:04.250068-05:00>, 'entity_id': 'automation.media_player_pausedstopped', 'new_state': <state automation.media_player_pausedstopped=on; last_triggered=2017-02-05T19:40:51.160414-05:00, friendly_name=Media player paused/stopped @ 2017-02-05T19:10:04.250068-05:00>}}, 'type': 'event'}
17-02-05 19:40:51 homeassistant.core: Bus:Handling <Event state_changed[L]: old_state=<state automation.media_player_playing=on; last_triggered=2017-02-05T19:40:41.071529-05:00, friendly_name=Media player playing @ 2017-02-05T19:10:04.277505-05:00>, entity_id=automation.media_player_playing, new_state=<state automation.media_player_playing=on; last_triggered=2017-02-05T19:40:51.377762-05:00, friendly_name=Media player playing @ 2017-02-05T19:10:04.277505-05:00>>
17-02-05 19:40:51 homeassistant.components.websocket_api: WS 140176765522888: Sending {'id': 2, 'event': {'origin': 'LOCAL', 'time_fired': datetime.datetime(2017, 2, 6, 0, 40, 51, 377942, tzinfo=), 'event_type': 'state_changed', 'data': {'old_state': <state automation.media_player_playing=on; last_triggered=2017-02-05T19:40:41.071529-05:00, friendly_name=Media player playing @ 2017-02-05T19:10:04.277505-05:00>, 'entity_id': 'automation.media_player_playing', 'new_state': <state automation.media_player_playing=on; last_triggered=2017-02-05T19:40:51.377762-05:00, friendly_name=Media player playing @ 2017-02-05T19:10:04.277505-05:00>}}, 'type': 'event'}


```
Author:
```
balloobbot
```
Text:
```

There hasn't been any activity on this issue recently. Due to the high number of incoming GitHub notifications, we have to clean some of the old issues, as many of them have already been resolved with the latest updates.
Please make sure to update to the latest Home Assistant version and check if that solves the issue. Let us know if that works for you by adding a comment 👍

```
Author:
```
balloobbot
```
Text:
```

This issue will be auto-closed because there hasn't been any activity for a few months. Feel free to open a new one if you still experience this problem 👍

```

## 13635
Title:
```

        [songpal.containers] Got unknowns for Sysinfo [bleID: 858ABB0D & 0B6C7957 & 32EE70A2]
      
```
Author:
```
Timple
```
Text:
```

Home Assistant release with the issue:
0.66.0
Last working Home Assistant release (if known):
0.61.1
Operating environment (Hass.io/Docker/Windows/etc.):
Docker
Component/platform:
Songpal
Description of problem:
Error saying I had to open an issue
Problem-relevant configuration.yaml entries and (fill out even if it seems unimportant):
# Discover some devices automatically
discovery:
Traceback (if applicable):
home-assistant_1  | 2018-04-02 14:31:12 WARNING (MainThread) [songpal.service] More than on version for {'name': 'connectBluetoothDevice', 'versions': [{'version': '1.0'}, {'version': '1.1'}]}, using the first one
home-assistant_1  | 2018-04-02 14:31:12 WARNING (MainThread) [songpal.containers] Got unknowns for Sysinfo: {'bleID': '858ABB0D'} - please create an issue!
home-assistant_1  | 2018-04-02 14:31:21 WARNING (MainThread) [songpal.service] More than on version for {'name': 'connectBluetoothDevice', 'versions': [{'version': '1.0'}, {'version': '1.1'}]}, using the first one
home-assistant_1  | 2018-04-02 14:31:23 WARNING (MainThread) [homeassistant.components.media_player] Setup of platform songpal is taking over 10 seconds.
home-assistant_1  | 2018-04-02 14:31:23 WARNING (MainThread) [songpal.containers] Got unknowns for Sysinfo: {'bleID': '0B6C7957'} - please create an issue!
home-assistant_1  | 2018-04-02 14:36:24 WARNING (MainThread) [songpal.service] More than on version for {'name': 'connectBluetoothDevice', 'versions': [{'version': '1.0'}, {'version': '1.1'}]}, using the first one
home-assistant_1  | 2018-04-02 14:36:26 WARNING (MainThread) [homeassistant.components.media_player] Setup of platform songpal is taking over 10 seconds.
home-assistant_1  | 2018-04-02 14:36:27 WARNING (MainThread) [songpal.containers] Got unknowns for Sysinfo: {'bleID': '32EE70A2'} - please create an issue!

Additional information:
None, feel free to inquire more info

```
Author:
```
rytilahti
```
Text:
```

This has been fixed in upstream (rytilahti/python-songpal@33efa2e) and is part of the currently required python-songpal version (0.0.7), so I'm closing it.

```

## 19455
Title:
```

        Add fan mode to climate Lovelace card
      
```
Author:
```
thundergreen
```
Text:
```

Dear all.
I'm missing hard the fan mode option in climate Lovelace card like here :
https://community.home-assistant.io/t/dual-thermostat-card/85798
Is it possible to add those that would make the card complete and perfect.if not I will have to use custom cards
Cheers and thanks for this awesome projects

```
Author:
```
move
```
Text:
```

This issue was moved by MartinHjelmare to home-assistant/ui-schema#219.

```

# Pull
## 18690
Title:
```

        Async cover template tests
      
```
Author:
```
armills
```
Text:
```

Description:
Async tests for #17270

```

## 17327
Title:
```

        WIP: Add basic suggestion component
      
```
Author:
```
balloob
```
Text:
```

Description:
Preview of a suggestions component I'm working on. Goal of this component is to provide suggestions to the user on which entities are popular to interact with during a specific period of time. Will be used to power a new lovelace card 😎
This is the initial implementation and so very limited on purpose. Eventually we can start taking users into account and the location of the users (once we have a component that binds users to device trackers).
Can be heavy to generate, so plan is to generate it once a day.
It's smart enough to ignore any service call that results from another service call (ie I call a script that turns on 5 lights, only the script will show in popular list)
Checklist:

 The code change is tested and works locally.
 Local tests pass with tox. Your PR cannot be merged unless tests pass

If the code does not interact with devices:

 Tests have been added to verify that the new code works.


```
Author:
```
balloob
```
Text:
```

I realized when writing this component that we can greatly increase the performance of the logbook by avoiding loading all events into memory at once. Will PR that next.

```
Author:
```
balloob
```
Text:
```

This PR will be back, once I have a nice use case for it (in Lovelace)

```

## 67
Title:
```

        Add a global config object to Home Assistant
      
```
Author:
```
balloob
```
Text:
```

This adds a global config object to Home Assistant. It will auto detect location, temperature unit and time zone using the JSON api from freegeoip.net. Devices that have temperature states will have these automatically be converted to the preferred unit.
Config object contains the following information accessible at hass.config:

location
temperature unit
time zone
name of location where HA is running

(last two are not used right now).
Example configuration.yaml entries:
homeassistant:
  # Omitted values in this section will be auto detected using freegeoip.net

  # Location required to calculate the time the sun rises and sets
  latitude: 32.87336
  longitude: 117.22743

  # C for Celcius, F for Fahrenheit
  temperature_unit: C

  # Pick yours from here:
  # http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
  time_zone: America/Los_Angeles

  # Name of the location where Home Assistant is running
  name: Home
This PR supersedes PR #23 . Thanks to @kangaroo for the idea of auto setting the temperature unit based on location.

```
Author:
```
coveralls
```
Text:
```


Coverage decreased (-0.41%) to 66.69% when pulling 9b643d5 on ha-config into 569b15d on dev.

```
Author:
```
coveralls
```
Text:
```


Coverage decreased (-0.5%) to 66.59% when pulling 7a7f486 on ha-config into 569b15d on dev.

```

## 17179
Title:
```

        Add optional "all" parameter for groups
      
```
Author:
```
danielperna84
```
Text:
```

Description:
The current way groups work as per the documentation

When any member of a group is on then the group will also be on.

This may usually be what people expect. I do believe though, that there are cases where a groups state should only turn to on if all entities are on. I myself once wanted that, forgot what it was though and probably ended up using some workaround.
One simple example would be monitoring if a group of devices is on. Like: Notify me if not all devices of a particular group are on (alarm system or whatever). If one node goes down, the whole group is considered down. It's pretty straightforward to build an automation based on that single state of the group instead of writing templates or creating helper-entities.
Marked es WIP because I want to gather opinions on this before I start with the tests and update the documentation
Essentially this PR keeps using any as the default, but overrides that if all is set to true.
Pull request in home-assistant.io with documentation (if applicable): home-assistant/home-assistant.io#6557
Example entry for configuration.yaml (if applicable):
group:
  # Current implementation, group is on when at least one entity is on
  normal:
    name: normal
    entities:
      - input_boolean.bool1
      - input_boolean.bool2
      - input_boolean.bool3
  # New mode: group is on when all entities are on
  inverted:
    name: inverted
    all: true
    entities:
      - input_boolean.bool1
      - input_boolean.bool2
      - input_boolean.bool3
Checklist:

 The code change is tested and works locally.
 Local tests pass with tox. Your PR cannot be merged unless tests pass

If user exposed functionality or configuration variables are added/changed:

 Documentation added/updated in home-assistant.io

If the code does not interact with devices:

 Tests have been added to verify that the new code works.


```
Author:
```
frenck
```
Text:
```

If there are just 2 modes (any/all) why make this a string?
An all: true seems to be more elegant in that case.

```
Author:
```
danielperna84
```
Text:
```

You're right, makes sense.

```
Author:
```
balloob
```
Text:
```

The advantage of a string over a boolean is that it doesn't require a breaking change in the future if another mode would be added. Although I must admit that I can't think of any.

```
Author:
```
balloob
```
Text:
```

Ok to merge when description updated.

```
Author:
```
danielperna84
```
Text:
```

Is the new description ok? It's kind of hard to explain in just a few words. 😆

```
Author:
```
balloob
```
Text:
```

Yesss.

```

## 24620
Title:
```

        Add support for opencv wheels
      
```
Author:
```
pvizeli
```
Text:
```

Description:
We solved the problem with opencv-python wheels because we provide now our own:
https://github.com/home-assistant/hassio-opencv
In the past we revert this pinning but now we need it.

```

## 16065
Title:
```

        Grammar and spelling fixes
      
```
Author:
```
scop
```
Text:
```

Description:
Grammar and spelling fixes; mainly "setup" -> "set up" (the verb), and miscellaneous others.
As a side bonus, fixes the vast majority of D401's mentioned in PR #14557.
Checklist:

 The code change is tested and works locally.
 Local tests pass with tox. Your PR cannot be merged unless tests pass


```
Author:
```
fabaff
```
Text:
```

Thanks 🐦

```

## 27132
Title:
```

        Fix error on failed Plex setup
      
```
Author:
```
jjlawren
```
Text:
```

Description:
Parameter in log entry refers to incorrect location in config entry.
Checklist:

 The code change is tested and works locally.
 Local tests pass with tox. Your PR cannot be merged unless tests pass
 There is no commented out code in this PR.
 I have followed the development checklist


```

## 25033
Title:
```

        Jewish calendar sensor update based on schedule not every 30 seconds
      
```
Author:
```
zalke
```
Text:
```

Description:
Since the sensor values only change on a predictable schedule it does not
make sense to recalculate every 30 seconds.
Related issue (if applicable): fixes #
Pull request with documentation for home-assistant.io (if applicable): home-assistant/home-assistant.io#<home-assistant.io PR number goes here>
Example entry for configuration.yaml (if applicable):

Checklist:

 The code change is tested and works locally.
 Local tests pass with tox. Your PR cannot be merged unless tests pass
 There is no commented out code in this PR.
 I have followed the development checklist

If user exposed functionality or configuration variables are added/changed:

 Documentation added/updated in home-assistant.io

If the code communicates with devices, web services, or third-party tools:

 The manifest file has all fields filled out correctly. Update and include derived files by running python3 -m script.hassfest.
 New or updated dependencies have been added to requirements_all.txt by running python3 -m script.gen_requirements_all.
 Untested files have been added to .coveragerc.

If the code does not interact with devices:

 Tests have been added to verify that the new code works.


```
Author:
```
ghost
```
Text:
```

Hey there @tsvi, mind taking a look at this pull request as its been labeled with a integration (jewish_calendar) you are listed as a codeowner for? Thanks!
This is a automatic comment generated by codeowners-mention to help ensure issues and pull requests are seen by the right people.

```
Author:
```
homeassistant
```
Text:
```

Hi @zalke,
It seems you haven't yet signed a CLA. Please do so here.
Once you do that we will be able to review and accept this pull request.
Thanks!

```
Author:
```
pvizeli
```
Text:
```

Remove all your change (sorry but look like "I don't know what I do, so I do everything") and add a SCAN_INTERVAL=timedelta(minutes=30) on top of your file

```
Author:
```
tsvi
```
Text:
```

@pvizeli There's merit to what @zalke is trying to do. The sensors calculate times that are part of the Jewish calendar. There's no point in calculating every 30 seconds as the sensors only update values a few times a day. Please see my review.
Changing to a scan interval of 30 minutes won't help as we might miss the exact time we want the sensors to be updated.

```
Author:
```
tsvi
```
Text:
```

@zalke if you have no plans on modifying your code, I suggest this PR be closed.
I'll try to implement your excellent suggestions in the future, but it's definitely not a priority for me.
Thank you very much for your insights.

```

