# home-assistant/home-assistant
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_LICENSE_md](#_LICENSE_md)

* [_github_PULL_REQUEST_TEMPLATE_md](#_github_PULL_REQUEST_TEMPLATE_md)

* [_CLA_md](#_CLA_md)

* [_github_ISSUE_TEMPLATE_Bug_report_md](#_github_ISSUE_TEMPLATE_Bug_report_md)

* [_CONTRIBUTING_md](#_CONTRIBUTING_md)

* [_CODE_OF_CONDUCT_md](#_CODE_OF_CONDUCT_md)

* [_github_ISSUE_TEMPLATE_md](#_github_ISSUE_TEMPLATE_md)

[- Inline](#Inline)

* [_homeassistant_components_openweathermap_sensor_py](#_homeassistant_components_openweathermap_sensor_py)

* [_homeassistant_components_threshold_binary_sensor_py](#_homeassistant_components_threshold_binary_sensor_py)

* [_homeassistant_components_konnected_sensor_py](#_homeassistant_components_konnected_sensor_py)

* [_homeassistant_components_thinkingcleaner_sensor_py](#_homeassistant_components_thinkingcleaner_sensor_py)

* [_homeassistant_components_seven_segments_image_processing_py](#_homeassistant_components_seven_segments_image_processing_py)

* [_homeassistant_components_dweet_sensor_py](#_homeassistant_components_dweet_sensor_py)

* [_homeassistant_components_homematic_notify_py](#_homeassistant_components_homematic_notify_py)

* [_tests_components_mqtt_test_legacy_vacuum_py](#_tests_components_mqtt_test_legacy_vacuum_py)

* [_homeassistant_components_bizkaibus_sensor_py](#_homeassistant_components_bizkaibus_sensor_py)

* [_docs_source_ext_edit_on_github_py](#_docs_source_ext_edit_on_github_py)

* [_homeassistant_components_nextbus_init_py](#_homeassistant_components_nextbus_init_py)

* [_homeassistant_components_telegram_init_py](#_homeassistant_components_telegram_init_py)

* [_tests_components_islamic_prayer_times_init_py](#_tests_components_islamic_prayer_times_init_py)

* [_homeassistant_components_google_calendar_py](#_homeassistant_components_google_calendar_py)

* [_homeassistant_components_insteon_fan_py](#_homeassistant_components_insteon_fan_py)

* [_tests_components_wake_on_lan_test_switch_py](#_tests_components_wake_on_lan_test_switch_py)

* [_homeassistant_components_fibaro_scene_py](#_homeassistant_components_fibaro_scene_py)

* [_script_hassfest_services_py](#_script_hassfest_services_py)

* [_tests_components_nx584_test_binary_sensor_py](#_tests_components_nx584_test_binary_sensor_py)

* [_homeassistant_components_nilu_air_quality_py](#_homeassistant_components_nilu_air_quality_py)

[- Issues](#Issues)

* [11167](#11167)

* [3850](#3850)

* [8660](#8660)

* [1181](#1181)

* [2508](#2508)

* [5298](#5298)

* [10086](#10086)

* [15254](#15254)

* [5347](#5347)

[- Pull](#Pull)

* [3257](#3257)

* [11286](#11286)

* [16597](#16597)

* [3909](#3909)

* [11423](#11423)

* [3210](#3210)

* [5745](#5745)

* [18336](#18336)

* [5903](#5903)

* [17101](#17101)

* [13748](#13748)

<!-- toc -->

# Info
## description
🏡 Open source home automation that puts local control and privacy first

# Markdown
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
# Inline
## _homeassistant_components_openweathermap_sensor_py

## _homeassistant_components_threshold_binary_sensor_py

## _homeassistant_components_konnected_sensor_py
### Line 32-41
```

    data = hass.data[KONNECTED_DOMAIN]
    device_id = discovery_info["device_id"]
    sensors = []

    # Initialize all DHT sensors.
    dht_sensors = [
        sensor
        for sensor in data[CONF_DEVICES][device_id][CONF_SENSORS]
        if sensor[CONF_TYPE] == "dht"
```
### Line 69-79
```
                )
            ],
            True,
        )

    # DS18B20 sensors entities are initialized when they report for the first
    # time. Set up a listener for that signal from the Konnected component.
    async_dispatcher_connect(hass, SIGNAL_DS18B20_NEW, async_add_ds18b20)


class KonnectedSensor(Entity):
```
### Line 89-103
```
        self._unit_of_measurement = SENSOR_TYPES[sensor_type][1]
        self._unique_id = addr or "{}-{}-{}".format(
            device_id, self._pin_num, sensor_type
        )

        # set initial state if known at initialization
        self._state = initial_state
        if self._state:
            self._state = round(float(self._state), 1)

        # set entity name if given
        self._name = self._data.get(CONF_NAME)
        if self._name:
            self._name += " " + SENSOR_TYPES[sensor_type][0]

```

## _homeassistant_components_thinkingcleaner_sensor_py

## _homeassistant_components_seven_segments_image_processing_py

## _homeassistant_components_dweet_sensor_py

## _homeassistant_components_homematic_notify_py

## _tests_components_mqtt_test_legacy_vacuum_py
### Line 664-682
```
    await hass.async_block_till_done()
    async_fire_mqtt_message(hass, "attr-topic1", '{ "val": "100" }')
    state = hass.states.get("vacuum.beer")
    assert state.attributes.get("val") == "100"

    # Change json_attributes_topic
    async_fire_mqtt_message(hass, "homeassistant/vacuum/bla/config", data2)
    await hass.async_block_till_done()

    # Verify we are no longer subscribing to the old topic
    async_fire_mqtt_message(hass, "attr-topic1", '{ "val": "50" }')
    state = hass.states.get("vacuum.beer")
    assert state.attributes.get("val") == "100"

    # Verify we are subscribing to the new topic
    async_fire_mqtt_message(hass, "attr-topic2", '{ "val": "75" }')
    state = hass.states.get("vacuum.beer")
    assert state.attributes.get("val") == "75"

```
### Line 706-715
```
    )

    async_fire_mqtt_message(hass, "test-topic", "payload")

    assert len(hass.states.async_entity_ids()) == 2
    # all vacuums group is 1, unique id created is 1


async def test_entity_device_info_with_identifier(hass, mqtt_mock):
    """Test MQTT vacuum device registry integration."""
```

## _homeassistant_components_bizkaibus_sensor_py

## _docs_source_ext_edit_on_github_py

## _homeassistant_components_nextbus_init_py

## _homeassistant_components_telegram_init_py

## _tests_components_islamic_prayer_times_init_py

## _homeassistant_components_google_calendar_py

## _homeassistant_components_insteon_fan_py

## _tests_components_wake_on_lan_test_switch_py

## _homeassistant_components_fibaro_scene_py

## _script_hassfest_services_py
### Line 54-63
```
    return False


def validate_services(integration: Integration):
    """Validate services."""
    # Find if integration uses services
    has_services = grep_dir(
        integration.path, "**/*.py", r"hass\.services\.(register|async_register)"
    )

```
### Line 83-92
```
        )


def validate(integrations: Dict[str, Integration], config):
    """Handle dependencies for integrations."""
    # check services.yaml is cool
    for integration in integrations.values():
        if not integration.manifest:
            continue

```

## _tests_components_nx584_test_binary_sensor_py

## _homeassistant_components_nilu_air_quality_py

# Issues
## 11167
Title:
```

        XMPP / Jabber "can't start new thread"
      
```
Author:
```
thundergreen
```
Text:
```

Make sure you are running the latest version of Home Assistant before reporting an issue.
You should only file an issue if you found a bug. Feature and enhancement requests should go in the Feature Requests section of our community forum:
Home Assistant release (hass --version):
0.59.2
Python release (python3 --version):
python 3.4
Component/platform:
XMPP / Jabber
Description of problem:
Problems with XMPP (unknown)
Expected:
it works
Problem-relevant configuration.yaml entries and steps to reproduce:
  - name: thorsten
    platform: xmpp 
    sender: home-assistant@emevth.no-ip.biz 
    password: home-assistant
    recipient: thorsten@emevth.no-ip.biz
    tls: true
    room: home-assistant@chat.noip.me
  - name: emilie
    platform: xmpp
    sender: home-assistant@emevth.no-ip.biz 
    password: home-assistant
    recipient: emilie@emevth.no-ip.biz
    tls: true





Traceback (if applicable):
2017-12-16 16:21:25 ERROR (MainThread) [homeassistant.core] Error doing job: Task exception was never retrieved
Traceback (most recent call last):
File "/usr/lib/python3.4/asyncio/tasks.py", line 233, in _step
result = coro.throw(exc)
File "/srv/hass/hass_venv/lib/python3.4/site-packages/homeassistant/core.py", line 1031, in _event_to_service_call
yield from service_handler.func(service_call)
File "/srv/hass/hass_venv/lib/python3.4/site-packages/homeassistant/components/notify/__init__.py", line 143, in async_notify_message
yield from notify_service.async_send_message(**kwargs)
File "/usr/lib/python3.4/asyncio/futures.py", line 388, in __iter__
yield self  # This tells Task to wait for completion.
File "/usr/lib/python3.4/asyncio/tasks.py", line 286, in _wakeup
value = future.result()
File "/usr/lib/python3.4/asyncio/futures.py", line 277, in result
raise self._exception
File "/usr/lib/python3.4/concurrent/futures/thread.py", line 54, in run
result = self.fn(*self.args, **self.kwargs)
File "/srv/hass/hass_venv/lib/python3.4/site-packages/homeassistant/components/notify/xmpp.py", line 64, in send_message
self._verify, self._room, data)
File "/srv/hass/hass_venv/lib/python3.4/site-packages/homeassistant/components/notify/xmpp.py", line 117, in send_message
SendNotificationBot()
File "/srv/hass/hass_venv/lib/python3.4/site-packages/homeassistant/components/notify/xmpp.py", line 92, in __init__
self.process()
File "/srv/hass/hass_venv/lib/python3.4/site-packages/sleekxmpp/basexmpp.py", line 245, in process
return XMLStream.process(self, *args, **kwargs)
File "/srv/hass/hass_venv/lib/python3.4/site-packages/sleekxmpp/xmlstream/xmlstream.py", line 1454, in process
self._start_thread('event_thread_%s' % t, self._event_runner)
File "/srv/hass/hass_venv/lib/python3.4/site-packages/sleekxmpp/xmlstream/xmlstream.py", line 1363, in _start_thread
self.__thread[name].start()
File "/usr/lib/python3.4/threading.py", line 850, in start
_start_new_thread(self._bootstrap, ())
RuntimeError: can't start new thread

Additional info:

```
Author:
```
thundergreen
```
Text:
```

Nobody using xmpp here ?

```
Author:
```
matthewslaney
```
Text:
```

Generally this is a system configuration issue and not an application issue. Check that the settings are reasonable for both your number of threads allowed and the stack size for each thread. Sometimes in trying to solve other problems, the stack size gets set unreasonably high, which then means it tries to allocate a huge amount of memory for each thread. FYI, this seems to be a fairly common problem with the default settings some system-on-a-chip systems like Raspberry Pi.

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

## 3850
Title:
```

        nested groups make the gui crash
      
```
Author:
```
rbflurry
```
Text:
```

Make sure you are running the latest version of Home Assistant before reporting an issue.
You should only file an issue if you found a bug. Feature and enhancement requests should go in the Feature Requests section of our community forum:
Home Assistant release (hass --version):
0.30.2
Python release (python3 --version):
3.5.2
Component/platform:
groups and device tracker.
Description of problem:
I have two groups of each containing two device_trackers that I then nested into a parent group
When clicking on the Parents group card (by the name) a long repeating list of the child groups is created and then the webpage crashes.
Expected:
I am not sure what the out come should be but I would imagine it should not be crashing.
Problem-relevant configuration.yaml entries and steps to reproduce:
  device_family:
   name: Family
   view: no
   entities:
    - group.device_ryan
    - group.device_chelsea
  device_ryan:
   name: Ryan
   view: no
   entities:
    - device_tracker.ryans_iphone_wifi
    - device_tracker.ryansiphone
  device_chelsea:
   name: Chelsea
   view: no
   entities:
    - device_tracker.chelseasiphone_wifi
    - device_tracker.chelseasiphone

create two groups containing device trackers
nest the two groups into a parent group
in the gui click on the card name of the parent group
wait for page to crash

Additional info:




```
Author:
```
1accscomm
```
Text:
```

This isn't isolated to device trackers.  Running version 0.32.2 and seeing the same behavior with some lights.
#####################################################################
# Kitchen
#####################################################################
  kitchen_view:
    name: Kitchen
    view: yes
    entities:
      - group.kitchen
      - media_player.kitchen

  kitchen:
    name: Kitchen
    entities:
      - group.kitchen_lights

  kitchen_lights:
    name: Kitchen Lights
    entities:
      - group.kitchen_overhead_light

  kitchen_overhead_light:
    name: Kitchen Overhead Light
    entities:
      - light.kitchen_overhead_1
      - light.kitchen_overhead_2
      - light.kitchen_overhead_3

Trying to expand the group group.kitchen_lights in the UI results in the following, as well as an eventual tab crash as seen above.


```
Author:
```
andrey-git
```
Text:
```

Nested group displays fine for me.
@rbflurry @1accscomm
Could you confirm whether this is still broken for you?

```
Author:
```
rbflurry
```
Text:
```

Yes it still crashes for me.

```
Author:
```
rbflurry
```
Text:
```

Probably not related but an new issue, I also cannot get the child groups to show on the same view. Except on the default view.

```
Author:
```
andrey-git
```
Text:
```

@rbflurry what version are you on?
Does it crash with lights or just with device trackers?

```
Author:
```
andrey-git
```
Text:
```

@rbflurry friendly ping on the question

```
Author:
```
andrey-git
```
Text:
```

Closing. Please reopen if someone can reproduce this.

```

## 8660
Title:
```

        Logbook order issue
      
```
Author:
```
abmantis
```
Text:
```

Home Assistant release (hass --version):
0.49.0
Python release (python3 --version):
Python 3.4.2
Component/platform:
Logbook
Description of problem:
Events that occur in the same second are not sorted by the correct order in the Logbook.
Not a bug but, displaying the seconds could be a nice improvement.
Expected:
Events would appear in their occurrence order even when they happen in the same second.

```
Author:
```
arsaboo
```
Text:
```

Yeah...that is annoying and, sometimes misleading. The Logbook sorting should be improved.

```
Author:
```
bmesuere
```
Text:
```

+1 for including the seconds in the logbook. This would be a great help when debugging scripts and automations.

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
fanaticDavid
```
Text:
```

Still an issue...

```
Author:
```
dgomes
```
Text:
```

This is a frontend issue, should be posted in https://github.com/home-assistant/home-assistant-polymer

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

## 1181
Title:
```

        Generalized MQTT switch component(s)
      
```
Author:
```
jasonmhite
```
Text:
```

One thing that would really be handy for me is a switch component that is "generalized" in the sense that it can have more than two states. My use case is that I have a thermostat that I built that takes commands over MQTT. I'd like to be able to toggle it between a discrete set of states fan/heat/cool etc and have it send the appropriate MQTT message to set that state. I could write a specialized component for it like with e.g. the Nest, but I think the functionality is generally a lot more useful so I figured I'd suggest it.
Basically what I imagine is something like:
switch:
  general_mqtt_switch:
     name: thermostat  state  
     available_states:
       heat: "heat_on"
       cool: "cool_on"
       off: "turn_off"
       fan: "fan_on"
     control_topic: thermostat/control/state
     state_topic: thermostat/info
     value_template: ...

Then, in the web interface, it'd expose a toggle selector (maybe something like a Bootstrap button group?). When you select one of the values, it then sends the given message to the control_topic. Homeassistant also would monitor state_topic to determine the current state, where the value_template can be given to parse the messages receieved into the states listed as the keys of available_states, which could possibly be indicated by highlighting the current state in the selector.
The other component that I think might be useful would be similar, basically a text-box input. My use case here would be to let me send an arbitrary payload to a given MQTT topic, namely a temperature setting for the thermostat. I imagine something like:
switch:
  mqtt_value_switch:
    name: thermostat temp
    topic: thermostat/control/temp

This would render in the webui as a textbox and a "submit" button. When you hit submit, it'd just dump the value in the text box to the specified MQTT topic.
Thanks for considering this! I really am enjoying using HA and I think these would be quite useful and I could ditch the custom webui I've written and have everything nicely integrated into HA. These are components that are obviously extremely flexible, so I think lots of people might find uses of their own for them.

```
Author:
```
balloob
```
Text:
```

The next release will introduce an input_select component that will get you half way to where you want to be.

```
Author:
```
jasonmhite
```
Text:
```

Indeed, that looks like a good start. I might try and hack on it myself some working from that, if I ever find some of that "free time" thing I keep hearing about.

```
Author:
```
fab33
```
Text:
```

Did you find how to update mqtt topic ? I try with automation without success. But I'm new to hass

```
Author:
```
jasonmhite
```
Text:
```

Closing, as input_select combined with the changes in #1510 make this possible. Short summary is to create an input_select with the entries that you want and add an automation rule that uses data_template to send the selected value whenever the input is changed.
Also, I missed that feature requests are supposed to go on the forum, so this doesn't belong here anyway.

```

## 2508
Title:
```

        utc_offset for recorder
      
```
Author:
```
balloob
```
Text:
```

We are no longer storing the UTC offset of when an event was recorded. This has the downside that machine learning algorithms or pattern detection algorithms do not know what the actual time was at the location where the event was fired. Was it 9 in the morning or 5 in the afternoon.
Home Assistant release (hass --version): 0.24.0.dev0
CC @rhooper

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
balloob
```
Text:
```

It's… still a thing.

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

## 5298
Title:
```

        Ubiquiti AP error connecting to server
      
```
Author:
```
compacson
```
Text:
```

Make sure you are running the latest version of Home Assistant before reporting an issue.
You should only file an issue if you found a bug. Feature and enhancement requests should go in the Feature Requests section of our community forum:
Home Assistant release (hass --version):
0.35.3
Python release (python3 --version):
Python 3.4.2
Component/platform:
device_tracker
ubiquiti
Description of problem:
When trying the device_tracker Ubiquiti component i got an error into home assistant
Failed to connect to Unifi. Error: HTTP Error 400: Bad Request<br />You will need to restart hass after fixing.
and in the log
17-01-12 23:35:47 homeassistant.components.device_tracker.unifi: Failed to connect to Unifi: HTTP Error 400: Bad Request
Im not so good with python, but from my reading it seems to be a https security error
Expected:
Connecting to the server using https
Problem-relevant configuration.yaml entries and steps to reproduce:

- platform: unifi host: 192.168.1.208 port: 8443 #site_id: default username: !secret device_tracker_unifi_username password: !secret device_tracker_unifi_password 
Traceback (if applicable):

Additional info:
Willing to help, i can give access to my config and teamviewer or anything that can help the debugging ^^

```
Author:
```
happyleavesaoc
```
Text:
```

I'm experiencing the same issue.

```
Author:
```
arsaboo
```
Text:
```

I recall seeing something similar....but restarting the Cloud Key took care for me.

```
Author:
```
compacson
```
Text:
```

i have a local server, try to restart it, but still the same problem

```
Author:
```
cgarwood
```
Text:
```

I have the unifi controller running on the same system as my hass install with no issues. What happens if you remove host and port from the config? My config looks like:
device_tracker:
  platform: unifi
  username: !secret unifi_username
  password: !secret unifi_password
  track_new_devices: false

```
Author:
```
compacson
```
Text:
```

17-01-13 11:17:46 homeassistant.components.device_tracker: Error setting up platform unifi
this is a normal error as there is no unifi on the local host ! ^^

```
Author:
```
cgarwood
```
Text:
```

Ah, I was thinking when you said you had a local server it was on the same system as hass, not that it was just local on your network

```
Author:
```
finish06
```
Text:
```

What version of the Unifi Controller are you running?

```
Author:
```
compacson
```
Text:
```

UniFi 5.3.8 Controller for Debian/Ubuntu Linux
the lastest one
https://www.ubnt.com/download/unifi/default/default/

```
Author:
```
HBDK
```
Text:
```

Experiencing the same also running 5.3.8.
i have tried with and without port and ip specified in the config.
i have no problem logging in with the same credentials from my browser.

```
Author:
```
finish06
```
Text:
```

Maybe try to not use the !secrets and instead place the credentials in the file (unlikely but maybe a special character, etc is involved)... also, did you try restarting the controller?

```
Author:
```
mattthhdp
```
Text:
```

I have try to restart the controller, no sucess same error
same thing for setting the user and pass directly without the !secret
the error is http, that make me think that the probleme is  a security error, looks like home assistant cannot connect to the https secure connection ?
(I am compacson, github from work but both are the same persone, its me :D)
17-01-13 18:51:02 homeassistant.components.device_tracker.unifi: Failed to connect to Unifi: HTTP Error 400: Bad Request
something like this maybe ?
http://stackoverflow.com/questions/33008450/error-downloading-https-webpage

```
Author:
```
finish06
```
Text:
```

I am unable to replicate this error...  the configuration file looks to be setup correctly...  and the unifi API is pconnecting over 'https'...

```
Author:
```
compacson
```
Text:
```

i can give you access over teamviewer if you want to take a look and maybe play around ?
I am mattthhdp
git from job the only difference

```
Author:
```
compacson
```
Text:
```

I have talk a lot on gitter and people with local installation dosent seems to have this issue, it's seems that people that have installer it on an other machine have the same problem as i do
my controler is on a debian vm with the UniFi 5.3.8 Controller. I have try to disable iptables to be sure that the problem wasent that.

```
Author:
```
xnoodle
```
Text:
```

Hm. I tested HA 0.35.3 on my Pi (Raspbian) and on a Ubuntu 16.04.1 virtual machine, against both Unifi controller 4 and 5 on Debian 8.7, with no issues seen.
Software was obtained from the official Unifi repos, version numbers below.
unifi_5.3.11-8935_all.deb
unifi_4.8.20-8422_all.deb

```
Author:
```
compacson
```
Text:
```

i am on a debian 8 ... but should not change anything, i have installed it via the repository ? maybe ??

```
Author:
```
finish06
```
Text:
```

I started to rebuild this API with the requests module, however I am now getting the above error continually when I attempt to connect to the database.  I do not understand it @ all.  However, my home-assistant connection is still alive and strong.  Through perusing the UBNT forums, I would recommend trying to re-install the webUI after purging it, i.e. apt-get purge unifi.

```
Author:
```
compacson
```
Text:
```

Will try this tomorrow after work ! i will give you the details as soons as i have finish

```
Author:
```
mattthhdp
```
Text:
```

@finish06 sorry for the very long delay... so i have try to purge, reboot, reinstall
same problem here

```
Author:
```
basn
```
Text:
```

Hm i am not getting it to connect either, but i run a newer version of unifi (5.4.9).
I only get;
ConnectionRefusedError: [Errno 61] Connection refused
While the port is open and working.

```
Author:
```
finish06
```
Text:
```

Any update?

```
Author:
```
mattthhdp
```
Text:
```

@finish06 we will have to wait for someone to look at the code/update the code, if nobody can/want this will be deprecated and remove

```
Author:
```
sdague
```
Text:
```

unifi is working mostly fine for me.
Note, unless you fix all the SSL certs on the controller, you'll also need "verify_ssl: False" as the default SSL certs are snakeoil.

```
Author:
```
sdague
```
Text:
```

Can you try adding "verify_ssl: False" to your stanza?

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

## 10086
Title:
```

        Upgrade to 0.56.1(2) makes Home Assistant hang
      
```
Author:
```
augustdipierro
```
Text:
```

Home Assistant release (hass --version):
0.56.1 and 0.56.2
Python release (python3 --version):
3.5.3
Component/platform:
Home Assistant on Debian 9 amd64
Description of problem:
After trying to startup with systemd after upgrading (in virtualenv), Home Assistant just hangs on these lines in log:
oct 23 20:57:18 server systemd[1]: Started Home Assistant.
oct 23 20:57:21 server hass[2268]: 2017-10-23 20:57:21 INFO (Thread-2) [homeassistant.config] Upgrading configuration directory from 0.56.0 to 0.56.2
oct 23 20:57:21 server hass[2268]: Config directory: /home/homeassistant/.homeassistant
Nothing more.
Expected:
Expected to run as normal, downgrading to 0.56.0 makes it work again with the same config.
Problem-relevant configuration.yaml entries and steps to reproduce:


?
?
?

Traceback (if applicable):

Additional info:
What debug information can I attach?

```
Author:
```
ntalekt
```
Text:
```

Do you have any zwave devices? Sometimes after upgrading my instance will take around 20 minutes to fully come up and display the UI.

```
Author:
```
pvizeli
```
Text:
```

Look like your config folder is locked

```
Author:
```
augustdipierro
```
Text:
```

@pvizeli oh. You are really right! Thank you!) A week ago I moved Home Assistant to another machine... and yes. The problem was caused by rights.
Files .HA_VERSION, .uuid and .ios_conf had root owner.
I am fool :).

```

## 15254
Title:
```

        Deconz lights not showing correctly in UI
      
```
Author:
```
jamesking420
```
Text:
```

Home Assistant release with the issue:
0.72.1
Last working Home Assistant release (if known):
??
Operating environment
hassio on raspberry pi 3b with a conbee stick and Deconz add on
Component/platform:
https://www.home-assistant.io/components/deconz/
Description of problem:
When I change a light colour on the colour wheel for, say kitchen light, and then navigate away from that light in the UI and look at the settings for another light (dining room), the colour wheel will show the current colour for the previous light (kitchen) that was changed, and not the true colour of dining room light.
I first noticed this when I switched all my lights to zigbee via conbee rather then hue bridge.
Additional Information
I know there have recently been some other bugs with Deconz lights, such as transitions to off not working and the lights not reporting their colour state. The second issue (colour state reporting) could be related to this maybe? Just thought I should mention it!

```
Author:
```
Kane610
```
Text:
```

Thanks for reporting! This is fixed in 0.73
It was a combination of component not being fully updated to use the new common base of Hue and saturation that HASS is employing as well as not taking in to consideration that sometimes xy values reported from lights would not be normalised.
You can try it out already now with the 0.73 beta, if you'd like.

```

## 5347
Title:
```

        Error setting up platform bluetooth_tracker
      
```
Author:
```
ianrobrien
```
Text:
```

Make sure you are running the latest version of Home Assistant before reporting an issue.
You should only file an issue if you found a bug. Feature and enhancement requests should go in the Feature Requests section of our community forum:
Home Assistant release (hass --version): 0.36.0
Python release (python3 --version): Python 3.4.2
Component/platform: Bluetooth Tracker
Description of problem: Error setting up platform bluetooth_tracker. Bluetooth tracker is not initialized.
Expected:
Successful initialization of Bluetooth device tracker
Problem-relevant configuration.yaml entries and steps to reproduce:
platform: bluetooth_tracker
track_new_devices: no

Add Bluetooth tracker
Start Home Assistant
View log to see error

Traceback (if applicable):
17-01-15 13:59:16 homeassistant.components.device_tracker: Error setting up platform bluetooth_tracker
Traceback (most recent call last):
  File "/srv/homeassistant/lib/python3.4/site-packages/homeassistant/components/device_tracker/__init__.py", line 164, in async_setup_platform
    None, platform.setup_scanner, hass, p_config, tracker.see)
  File "/usr/lib/python3.4/asyncio/futures.py", line 388, in __iter__
    yield self  # This tells Task to wait for completion.
  File "/usr/lib/python3.4/asyncio/tasks.py", line 286, in _wakeup
    value = future.result()
  File "/usr/lib/python3.4/asyncio/futures.py", line 277, in result
    raise self._exception
  File "/usr/lib/python3.4/concurrent/futures/thread.py", line 54, in run
    result = self.fn(*self.args, **self.kwargs)
  File "/srv/homeassistant/lib/python3.4/site-packages/homeassistant/components/device_tracker/bluetooth_tracker.py", line 89, in setup_scanner
    update_bluetooth(dt_util.utcnow())
  File "/srv/homeassistant/lib/python3.4/site-packages/homeassistant/components/device_tracker/bluetooth_tracker.py", line 87, in update_bluetooth
    now + timedelta(seconds=interval))
TypeError: unsupported type for timedelta seconds component: datetime.timedelta
Additional info:

```
Author:
```
balloob
```
Text:
```

Can you try this fix #5350 ?

```
Author:
```
dnuc
```
Text:
```

Looks like the fix is working for me. Thanks!

```
Author:
```
ianrobrien
```
Text:
```

Fixed in 0.36.1. Thanks!

```

# Pull
## 3257
Title:
```

        Add voluptuous to ecobee
      
```
Author:
```
pvizeli
```
Text:
```

Description:
Last of notify platform:

Add voluptuous to ecobee


```
Author:
```
fabaff
```
Text:
```

Looks good to me.

```

## 11286
Title:
```

        Monzo
      
```
Author:
```
rossdargan
```
Text:
```

Description:
Add in a monzo bank sensor
Pull request in home-assistant.github.io with documentation (if applicable): home-assistant/home-assistant.io#4271
Example entry for configuration.yaml (if applicable):
(documentation explains how to get a client id and secret)
sensor:
  - platform: monzo
    client_id: '***CLIENT ID***'
    client_secret: '***SECRET***'
    name: 'Optional name for the sensor'
    cache_path: '/.homeassistant/.optional-cache-location-for-token'
    current_account: true # only if you the current account
Checklist:
If user exposed functionality or configuration variables are added/changed:

 Documentation added/updated in home-assistant.github.io

If the code communicates with devices, web services, or third-party tools:

 Local tests with tox run successfully. Your PR cannot be merged unless tests pass
 New dependencies have been added to the REQUIREMENTS variable (example).
 New dependencies are only imported inside functions that use them (example).
 New dependencies have been added to requirements_all.txt by running script/gen_requirements_all.py.
 New files were added to .coveragerc.

If the code does not interact with devices:

 Local tests with tox run successfully. Your PR cannot be merged unless tests pass
 Tests have been added to verify that the new code works.


```
Author:
```
rossdargan
```
Text:
```

I don't think the travis build is failing because of my pull request... but I could be wrong!

```

## 16597
Title:
```

        Add websocket list APIs for the registries
      
```
Author:
```
balloob
```
Text:
```

Description:
This adds two APIs: one to list the device registry entries, one to list the entity registry entries.
Meant to power a frontend for devices 👍
CC @Kane610
Checklist:

 The code change is tested and works locally.
 Local tests pass with tox. Your PR cannot be merged unless tests pass

If the code does not interact with devices:

 Tests have been added to verify that the new code works.


```
Author:
```
Kane610
```
Text:
```

I don't know too much about this part of Hass, but it looks ok to me!

```

## 3909
Title:
```

        Async template
      
```
Author:
```
pvizeli
```
Text:
```

Description:
Porting all Template sensor to async and fix unittest.
If the code does not interact with devices:

 Local tests with tox run successfully. Your PR cannot be merged unless tests pass
 Tests have been added to verify that the new code works.


```
Author:
```
mention-bot
```
Text:
```

@pvizeli, thanks for your PR! By analyzing the history of the files in this pull request, we identified @fabaff, @balloob and @pavoni to be potential reviewers.

```
Author:
```
balloob
```
Text:
```

Awesome 🐬
Good to merge when comments addressed.

```
Author:
```
balloob
```
Text:
```

Oops, looks like some other merged PR introduced a merge conflict 😿 . Ok to merge when you have the conflict resolved.

```

## 11423
Title:
```

        Plex api update
      
```
Author:
```
ryanm101
```
Text:
```

Updating to plexapi==3.0.5
Removed removed server obj that was being used for the media URL generation as .url() is available in self._session
seasons() no longer exists -> renamed to season()
season() returns obj not list so corrected
season.index returns int, cast to str to zerofill
This should also fix the attr log spamming issue

```

## 3210
Title:
```

        Use voluptuous for Yamaha receiver
      
```
Author:
```
fabaff
```
Text:
```

Description:
Migration of the configuration check to voluptuous.
Related issue (if applicable): fixes 127528299
Example entry for configuration.yaml (if applicable):
media_player:
  platform: yamaha
  name: 'Basement Receiver'
@aoakeson @TheRealLink , would be nice if you could take a look at the changes and run a quick test. Thanks.

```

## 5745
Title:
```

        Upgrade psutil to 5.1.2
      
```
Author:
```
fabaff
```
Text:
```

5.1.2
Bug fixes

[Linux] sensors_battery().power_plugged may erroneously return None on Python 3.
[Linux] disk_io_counters() raises TypeError on python 3.
[Linux] sensors_battery()'s name and label fields on Python 3 are bytes instead of str.

Tested with the following configuration:
sensor:
  - platform: systemmonitor
    resources:
      - type: load_1m
      - type: 'disk_use_percent'
        arg: '/'
      - type: 'disk_use'
        arg: '/home'
      - type: 'disk_free'
        arg: '/'

```
Author:
```
mention-bot
```
Text:
```

@fabaff, thanks for your PR! By analyzing the history of the files in this pull request, we identified @balloob, @rmkraus and @theolind to be potential reviewers.

```

## 18336
Title:
```

        Switchmate library update
      
```
Author:
```
Danielhiversen
```
Text:
```

Description:
Switchmate library update
https://github.com/Danielhiversen/pySwitchmate/commits/master
Checklist:

 The code change is tested and works locally.
 Local tests pass with tox. Your PR cannot be merged unless tests pass
 There is no commented out code in this PR.

If the code communicates with devices, web services, or third-party tools:

 New dependencies have been added to the REQUIREMENTS variable ([example][ex-requir]).
 New dependencies are only imported inside functions that use them ([example][ex-import]).
 New or updated dependencies have been added to requirements_all.txt by running script/gen_requirements_all.py.
 New files were added to .coveragerc.


```

## 5903
Title:
```

        Fix getters that ignored labels.
      
```
Author:
```
andrey-git
```
Text:
```

Description:
Fix getters that ignored labels.
Catch possible exception in get_wakeup.
Checklist:
If the code does not interact with devices:

 Local tests with tox run successfully. Your PR cannot be merged unless tests pass


```
Author:
```
mention-bot
```
Text:
```

@andrey-git, thanks for your PR! By analyzing the history of the files in this pull request, we identified @turbokongen, @balloob and @fabaff to be potential reviewers.

```
Author:
```
pvizeli
```
Text:
```

I think the old get_config_value is the reason for slow zwave reports. They can run into recursive loop inside async loop and that is very bad. This solution fix that. What I not know if, should we have a global solution or put that only in this component

```
Author:
```
andrey-git
```
Text:
```

I don't think that was the reason. It would happen only if zwave is updating the dict at the same time. This should be rare.

```
Author:
```
pvizeli
```
Text:
```

You are right the real problem is that python-zwafe is not threadsafe

```
Author:
```
balloob
```
Text:
```

🐬
Ok to merge when tests pass!

```
Author:
```
balloob
```
Text:
```

Unable to cherry-pick this into 0.38.2 because master does not contain the _get_wakeup method.

```
Author:
```
andrey-git
```
Text:
```

It was a mistake to put 2 fixes in a single PR :(

```

## 17101
Title:
```

        Fix counter restore
      
```
Author:
```
mvn23
```
Text:
```

Add config option to disable restore (always use initial value on restart).
Add unit tests for restore config option.
Description:
Counter entities did not properly restore their former value upon restart.
This PR fixes the issue and makes restoring optional (default: True).
Related issue (if applicable): fixes #10994
Pull request in home-assistant.io with documentation (if applicable): home-assistant/home-assistant.io#6479
Example entry for configuration.yaml (if applicable):
counter:
  example_counter:
    restore: True
Checklist:

 The code change is tested and works locally.
 Local tests pass with tox. Your PR cannot be merged unless tests pass

If user exposed functionality or configuration variables are added/changed:

 Documentation added/updated in home-assistant.io

If the code communicates with devices, web services, or third-party tools:

N/A

If the code does not interact with devices:

 Tests have been added to verify that the new code works.


```
Author:
```
fabaff
```
Text:
```

We should go the same route as with the input_boolean and the other input components. If initial is missing then use restore.

```
Author:
```
mvn23
```
Text:
```

I have considered that, however with the counter component initial is used for resets as well, which is probably why it has a default value. In my opinion it makes sense to have both an initial state and an option to override it upon start for this component.
I do appreciate that the current default behaviour goes against the other components where initial is always used during startup, so I'm open to suggestions here.

```
Author:
```
fabaff
```
Text:
```

I can't remember what I was thinking when I wrote the component. Wild guess...I haven't considered the case with restoring a value and being able to reset the counter to the initial value 😉
Let's move ahead with your fix.

```
Author:
```
fabaff
```
Text:
```

Looks good to me 🐦

```
Author:
```
ajfriesen
```
Text:
```

Is it possible this is still an issue?
I think it was working no my hassio install on a raspberry pi.
Today I switched to hassio on ubuntu server with this:
https://www.home-assistant.io/hassio/installation/#alternative-install-on-generic-linux-server
When I restart hassio from the webinterface my counter will be reset to 0.
My counter:
counter:
  my_counter:
    step: 1
    restore: true

I have enabled the recorder component.
I also can see the last value from the counter in the entity card but it still will always come up with 0 as wrong value.
EDIT:
Nevermind.
My database got corrupted.
Had to delete the old one, created a new one and than everything works fine.

```

## 13748
Title:
```

        Modify pushover notify to support attachments
      
```
Author:
```
brkr19
```
Text:
```

This change removes the dependency on python-pushover since it does not yet support attachments and the Pushover API can be accessed simply using python requests.  I used the 'load_file' function from slack.py as the basis for the work in this module to keep things consistent.
This implements the feature request found here: https://community.home-assistant.io/t/pushing-images-with-pushover-3-0/40667
The documentation has been updated with an example (6329a89 - Add example file attachment parameters #5134)

```
Author:
```
homeassistant
```
Text:
```

Hi @brkr19,
It seems you haven't yet signed a CLA. Please do so here.
Once you do that we will be able to review and accept this pull request.
Thanks!

```
Author:
```
fabaff
```
Text:
```

python-pushover has support for attachments. It wasn't release yet but there is an open issue for that.
This change seems to simply move the functionality of python-pushover into Home Assistant. Removing python-pushover as a requirement is not the solution for the problem at hand. We don't want to ship protocol-, service- or device-specific code if there is a module available. If the code lives in Home Assistant third parties can't use it and it increases maintenance for all (we need to maintain it in Home Assistant and python-pushover need to do the same work).
The way to proceed will be bump python-pushover to 0.4 and update the pushover platform.

```
Author:
```
brkr19
```
Text:
```

Ok, thanks for the feedback.  I can certainly understand that point of view, but figured since the API is so simple (requests.post(PUSHOVER_API_URL, data=data, files=attachment)), it seemed more productive to incorporate that into Home Assistant and remove the dependency on another project.
So as I understand it, we just put this change on hold and wait for the maintainer of python-pushover to release changes?  The changes were committed over two months ago but I don't see a 0.4 release yet.
I can start preparing for that, as it looks like my code won't change much since they didn't fully implement the image sending by url component, so I would still need to handle downloading, verifying, and clean-up of that as well as checking the validity/accessibility of local images.

```
Author:
```
fabaff
```
Text:
```

Working with APIs can be simple...We try to move code out of Home Assistant for platform because if it's a module more people can profit from it, features can be added/tested there first, etc. It doesn't not  matter how simple the code. it's also easier to move a module to asyncio when you only have to deal with one building block.

So as I understand it, we just put this change on hold and wait for the maintainer of python-pushover to release changes? The changes were committed over two months ago but I don't see a 0.4 release yet.

The developer of python-pushover could be busy. Often it helps to get in touch with people outside of GitHub because most are flooded with notifications. As a last resort, if the developer is non-responsive, there is forking.

I can start preparing for that, as it looks like my code won't change much since they didn't fully implement the image sending by url component, so I would still need to handle downloading, verifying, and clean-up of that as well as checking the validity/accessibility of local images.

Again, it helps to improve the module then the code should go upstream.

```
Author:
```
brkr19
```
Text:
```

Got, it - thanks.  I have reached out to their project and will see what the response is.  In the meantime, I'll update my code to work with the latest version of the python-pushover.  Do I just keep this PR open and submit the new version of my code when theirs is ready?

```
Author:
```
fabaff
```
Text:
```


Do I just keep this PR open and submit the new version of my code when theirs is ready?

Let's keep that PR open for a couple of days and decide then.

```
Author:
```
Thibauth
```
Text:
```

I have just released a new version (python-pushover v0.4) which contains support for attachments.

```
Author:
```
brkr19
```
Text:
```

Thanks! I'll take a look at incorporating the features into this module later this week.

```
Author:
```
brkr19
```
Text:
```

I must have accidentally closed this somehow - probably when I rest my fork to the latest master.  Anyways, I have my code checked into my fork and will be testing it a bit more before creating a new PR.  In case anyone following this is looking for a preview, my commit can be found here: 6f354e6

```
Author:
```
gitmayer
```
Text:
```

Why are you storing the file in temp and reloading it?  This way didn't work for me, I just modified what you had to return the image data.
I changed this tofile = self.load_file(...)which now returns req.content instead of filename.
This would not work for me otherwise and it took me forever to figure out why.  I think my file permissions were not working with the temp file.  Plus it seems redundant to save it to a disk or ram just to load it again.
I'm still trying to make the changes for local files, but I apparently can't find a path that is allowed.

```

