# dotnet/core
[- Info](#Info)

* [description](#description)

[- Markdown](#Markdown)

* [_release_notes_3_0_preview_3_0_0_preview8_download_md](#_release_notes_3_0_preview_3_0_0_preview8_download_md)

* [_release_notes_2_1_2_1_11_2_1_11_download_md](#_release_notes_2_1_2_1_11_2_1_11_download_md)

* [_release_notes_2_1_Preview_2_1_600_preview_commits_md](#_release_notes_2_1_Preview_2_1_600_preview_commits_md)

* [_release_notes_download_archives_preview4_download_md](#_release_notes_download_archives_preview4_download_md)

* [_release_notes_1_0_1_0_11_md](#_release_notes_1_0_1_0_11_md)

* [_release_notes_2_1_api_diff_2_0_vs_2_1_System_ComponentModel_Design_Serialization_md](#_release_notes_2_1_api_diff_2_0_vs_2_1_System_ComponentModel_Design_Serialization_md)

* [_release_notes_1_1_1_0_1_1_api_diff_1_0_1_1_api_diff_System_Threading_Tasks_md](#_release_notes_1_1_1_0_1_1_api_diff_1_0_1_1_api_diff_System_Threading_Tasks_md)

* [_release_notes_2_1_Preview_api_diff_preview2_2_1_preview2_System_IO_md](#_release_notes_2_1_Preview_api_diff_preview2_2_1_preview2_System_IO_md)

* [_release_notes_3_0_preview_api_diff_preview1_3_0_preview1_System_Reflection_md](#_release_notes_3_0_preview_api_diff_preview1_3_0_preview1_System_Reflection_md)

* [_release_notes_1_1_1_0_sdk_contributor_list_md](#_release_notes_1_1_1_0_sdk_contributor_list_md)

* [_release_notes_2_1_api_diff_2_0_vs_2_1_System_Threading_Tasks_Dataflow_md](#_release_notes_2_1_api_diff_2_0_vs_2_1_System_Threading_Tasks_Dataflow_md)

* [_release_notes_3_0_preview_api_diff_preview3_3_0_preview3_System_Threading_md](#_release_notes_3_0_preview_api_diff_preview3_3_0_preview3_System_Threading_md)

* [_release_notes_2_1_Preview_api_diff_rc1_2_1_rc1_md](#_release_notes_2_1_Preview_api_diff_rc1_2_1_rc1_md)

* [_release_notes_3_0_preview_api_diff_preview7_3_0_preview7_System_Reflection_Metadata_md](#_release_notes_3_0_preview_api_diff_preview7_3_0_preview7_System_Reflection_Metadata_md)

* [_release_notes_3_0_preview_api_diff_preview8_Asp_Net_3_0_preview8_Microsoft_AspNetCore_Components_Browser_md](#_release_notes_3_0_preview_api_diff_preview8_Asp_Net_3_0_preview8_Microsoft_AspNetCore_Components_Browser_md)

* [_release_notes_1_1_1_1_8_md](#_release_notes_1_1_1_1_8_md)

* [_release_notes_2_1_Preview_api_diff_preview2_2_1_preview2_System_Reflection_Metadata_md](#_release_notes_2_1_Preview_api_diff_preview2_2_1_preview2_System_Reflection_Metadata_md)

* [_release_notes_2_2_2_2_204_SDK_2_2_204_SDK_download_md](#_release_notes_2_2_2_2_204_SDK_2_2_204_SDK_download_md)

* [_release_notes_3_0_preview_api_diff_preview8_Asp_Net_3_0_preview8_Microsoft_JSInterop_Internal_md](#_release_notes_3_0_preview_api_diff_preview8_Asp_Net_3_0_preview8_Microsoft_JSInterop_Internal_md)

* [_release_notes_3_0_preview_api_diff_preview7_3_0_preview7_md](#_release_notes_3_0_preview_api_diff_preview7_3_0_preview7_md)

* [_README_md](#_README_md)

[- Inline](#Inline)

* [_release_notes_1_0_install_1_0_1_sh](#_release_notes_1_0_install_1_0_1_sh)

[- Issues](#Issues)

* [2653](#2653)

* [745](#745)

* [2186](#2186)

* [954](#954)

* [758](#758)

* [1125](#1125)

* [959](#959)

* [3332](#3332)

* [1297](#1297)

* [1181](#1181)

* [2857](#2857)

* [292](#292)

[- Pull](#Pull)

* [1582](#1582)

* [710](#710)

* [2606](#2606)

* [1136](#1136)

* [1438](#1438)

* [1160](#1160)

* [3302](#3302)

* [3183](#3183)

<!-- toc -->

# Info
## description
Home repository for .NET Core

# Markdown
## _release_notes_3_0_preview_3_0_0_preview8_download_md
```# .NET Core 3.0.0 Preview 8

.NET Core 3.0.0 Preview 8 comprises:

* .NET Core Runtime 3.0.0-preview8-28405-07
* ASP.NET Core 3.0.0-preview8.19405.7
* .NET Core SDK 3.0.100-preview8-013656

See the [Release Notes][release-notes] for details about what is included in this update.

|           | SDK Installer<sup>1</sup>                        | SDK Binaries<sup>1</sup>                 | Runtime Installer                                        | Runtime Binaries                                 | ASP.NET Core Runtime           |
| --------- | :------------------------------------------:     | :----------------------:                 | :---------------------------:                            | :-------------------------:                      | :-----------------:            |
| Windows   | [x86][dotnet-sdk-win-x86.exe] \| [x64][dotnet-sdk-win-x64.exe] | [x86][dotnet-sdk-win-x86.zip] \| [x64][dotnet-sdk-win-x64.zip] \| [ARM][dotnet-sdk-win-arm.zip] | [x86][dotnet-runtime-win-x86.exe] \| [x64][dotnet-runtime-win-x64.exe] | [x86][dotnet-runtime-win-x86.zip] \| [x64][dotnet-runtime-win-x64.zip] \| [ARM][dotnet-runtime-win-arm.zip] | [x86][aspnetcore-runtime-win-x86.exe] \| [x64][aspnetcore-runtime-win-x64.exe] \| [ARM][aspnetcore-runtime-win-arm.zip] \| <br> [Hosting Bundle][dotnet-hosting-win.exe]<sup>2</sup> |
| macOS     | [x64][dotnet-sdk-osx-x64.pkg]  | [x64][dotnet-sdk-osx-x64.tar.gz]     | [x64][dotnet-runtime-osx-x64.pkg] | [x64][dotnet-runtime-osx-x64.tar.gz] | [x64][aspnetcore-runtime-osx-x64.tar.gz]<sup>1</sup>
| Linux     | [See installations steps below][linux-install]   | [x64][dotnet-sdk-linux-x64.tar.gz] \| [ARM][dotnet-sdk-linux-arm.tar.gz] \| [ARM64][dotnet-sdk-linux-arm64.tar.gz] \| [x64 Alpine][dotnet-sdk-linux-musl-x64.tar.gz] | - | [x64][dotnet-runtime-linux-x64.tar.gz] \| [ARM][dotnet-runtime-linux-arm.tar.gz] \| [ARM64][dotnet-runtime-linux-arm64.tar.gz] \| [x64 Alpine][dotnet-runtime-linux-musl-x64.tar.gz] | [x64][aspnetcore-runtime-linux-x64.tar.gz]<sup>1</sup>  \| [ARM][aspnetcore-runtime-linux-arm.tar.gz]<sup>1</sup> \| [ARM64][aspnetcore-runtime-linux-arm64.tar.gz] \| [x64 Alpine][aspnetcore-runtime-linux-musl-x64.tar.gz]<sup>1</sup> |
| RHEL6     | -                                                | [x64][dotnet-sdk-rhel.6-x64.tar.gz]                    | -                                                        | [x64][dotnet-runtime-rhel.6-x64.tar.gz] | - |
| Checksums | [SDK][checksums-sdk]                             | -                                        | [Runtime][checksums-runtime]                             | - | - |

1. Includes the .NET Core and ASP.NET Core Runtimes
2. For hosting stand-alone apps on Windows Servers. Includes the ASP.NET Core Module for IIS and can be installed separately on servers without installing .NET Core runtime.

## Docker

The [.NET Core Docker images](https://hub.docker.com/r/microsoft/dotnet/) have been updated for this release. Details on our Docker versioning and how to work with the images can be seen in ["Staying up-to-date with .NET Container Images"](https://devblogs.microsoft.com/dotnet/staying-up-to-date-with-net-container-images/).

## Installing .NET Core on Linux

### Install using Snap

Because of the isolated environment, using Snap is the preferred way to install and try .NET Core Previews on [Linux distributions that support Snap](https://docs.snapcraft.io/installing-snapd/6735).

After configuring Snap on your system, run the following command to install the latest .NET Core SDK.

`sudo snap install dotnet-sdk --channel=beta --classic`

When .NET Core in installed using the Snap package, the default .NET Core command is `dotnet-sdk.dotnet`, as opposed to just `dotnet`. The benefit of the namespaced command is that it will not conflict with a globally installed .NET Core version you may have. This command can be aliased to `dotnet` with:

`sudo snap alias dotnet-sdk.dotnet dotnet`

**Note:** Some distros require an additional step to enable access to the SSL certificate. If you experience SSL errors when running `dotnet restore`, see [Linux Setup](https://github.com/dotnet/core/blob/master/Documentation/linux-setup.md) for a possible resolution.

### Install using deb/rpm packages

Preview release installers are not available from the Microsoft package repositories but you can download them and install manually or, set up a local package repository. Setting up a local package repository will result in a typical package manager installation experience. Consult your distros documentation to understand this option.

A manual installatoin requires the use of your distro's package installer to install each of the files *in the order presented below.* If you attempt to install them out of order, dependency checks will not succeed and the installation will fail. Download the correct System Dependencies Installer along with the `host, hostfxr, runtime, aspnetcore-runtime` and `sdk` installers.

Please see the [3.0 Supported OS](https://github.com/dotnet/core/blob/master/release-notes/3.0/3.0-supported-os.md) document for specific distro version support status.

| **System Dependencies Installer** |
| :-- |
| [Centos 7][dotnet-runtime-deps-centos.7-x64.rpm] |
| [Fedora][dotnet-runtime-deps-fedora.27-x64.rpm] |
| [OpenSUSE][dotnet-runtime-deps-opensuse.42-x64.rpm] |
| [Oracle Linux 7][dotnet-runtime-deps-oraclelinux.7-x64.rpm] |
| [RHEL 7][dotnet-runtime-deps-rhel.7-x64.rpm] |
| [SLES 12][dotnet-runtime-deps-sles.12-x64.rpm] |
| [Debian-based systems][dotnet-runtime-deps-x64.deb] |

| **Component** | **Package Type** |
| :--- | :---: |
| dotnet-host | [deb][dotnet-host-x64.deb] \| [rpm][dotnet-host-x64.rpm] |
| dotnet-hostfxr | [deb][dotnet-hostfxr-x64.deb] \| [rpm][dotnet-hostfxr-x64.rpm] |
| dotnet-runtime | [deb][dotnet-runtime-x64.deb] \| [rpm][dotnet-runtime-x64.rpm] |
| aspnetcore-runtime | [deb][aspnetcore-runtime-x64.deb] \| [rpm][aspnetcore-runtime-x64.rpm] |
| dotnet-targeting-pack | [deb][dotnet-targeting-pack-x64.deb] \| [rpm][dotnet-targeting-pack-x64.rpm] |
| dotnet-apphost-targeting-pack | [deb][dotnet-apphost-pack-x64.deb] \| [rpm][dotnet-apphost-pack-x64.rpm] |
| aspnetcore-targeting-pack | [deb][aspnetcore-targeting-pack.deb] \| [rpm][aspnetcore-targeting-pack.rpm] |
| netstandard-targeting-pack | [deb][netstandard-targeting-pack-x64.deb] \| [rpm][netstandard-targeting-pack-x64.rpm] |
| dotnet-sdk | [deb][dotnet-sdk-x64.deb] \| [rpm][dotnet-sdk-x64.rpm] |

After downloading the files, run your package utility to install the files in the following order.

1. dotnet-runtime-deps (System Dependencies Installer)
2. dotnet-host
3. dotnet-hostfxr
4. dotnet-runtime
5. aspnetcore-runtime
6. dotnet-targeting-pack
7. dotnet-apphost-targeting-pack
8. aspnetcore-targeting-pack
9. netstandard-targeting-pack
10. dotnet-sdk

**CentOS, Fedora, OpenSUSE, Oracle Linux, RHEL and SLES** 
`sudo rpm -ivh [package name]`

**Debian and Ubuntu** 
`sudo dpkg -i [package name]`

Here is a simple example script for Fedora to download and install the packages as described above. 

''' bash
cd $HOME/Downloads
mkdir preview8
cd preview8

wget -c https://download.visualstudio.microsoft.com/download/pr/e6c88fa0-7af3-4a5e-924c-c2b7746a3c56/058c182d3153f92102c36ba18a540c73/dotnet-host-3.0.0-preview8-28405-07-x64.rpm
wget -c https://download.visualstudio.microsoft.com/download/pr/be0dd399-26ff-4535-8817-cea74af8870f/caba64c029563357d10101531e7d1bba/dotnet-hostfxr-3.0.0-preview8-28405-07-x64.rpm
wget -c https://download.visualstudio.microsoft.com/download/pr/c7b80a75-be96-41ed-a17d-fb5d2a7e4ca7/c6ba37aa37e57cc4f15d068921abe225/dotnet-runtime-3.0.0-preview8-28405-07-x64.rpm
wget -c https://download.visualstudio.microsoft.com/download/pr/c76d6e7e-dcba-41bf-83ae-77ef4d4b83b9/80a4ac4e1f832552ebcc5f080bf80610/dotnet-runtime-deps-3.0.0-preview8-28405-07-fedora.27-x64.rpm
wget -c https://download.visualstudio.microsoft.com/download/pr/fca66248-bd05-4948-8efd-390b5d056397/c3078f7d3368438863eb26d93308858f/aspnetcore-runtime-3.0.0-preview8.19405.7-x64.rpm
wget -c https://download.visualstudio.microsoft.com/download/pr/5e6e263d-a49d-4ae5-99f1-56a04e9f10d7/8c787474558b11857b5920ce00466af8/dotnet-sdk-3.0.100-preview8-013656-x64.rpm

wget -c https://download.visualstudio.microsoft.com/download/pr/ec8c5f86-bf16-460d-b873-671b4d01cf21/389bf94fb1070ff4f115b68212b0ab0e/dotnet-apphost-pack-3.0.0-preview8-28405-07-x64.rpm
wget -c https://download.visualstudio.microsoft.com/download/pr/ba96af61-e1c3-4668-b2fc-7230c79e1cd0/382c3eabc382e3928ebc56299414c4c8/dotnet-targeting-pack-3.0.0-preview8-28405-07-x64.rpm
wget -c https://download.visualstudio.microsoft.com/download/pr/82467fdf-3521-4a44-85c6-ef23061a022d/9e07507d17cc70800891aa4441581c9c/netstandard-targeting-pack-2.1.0-preview8-28405-07-x64.rpm
wget -c https://download.visualstudio.microsoft.com/download/pr/26473bdd-e207-4e89-9eb5-14729db564a9/673896c711e4b8d54543b1c790c31be8/aspnetcore-targeting-pack-3.0.0-preview8.19405.7.rpm

sudo rpm -ivh dotnet-runtime-deps-3.0.0-preview8-28405-07-fedora.27-x64.rpm
sudo rpm -ivh dotnet-host-3.0.0-preview8-28405-07-x64.rpm
sudo rpm -ivh dotnet-hostfxr-3.0.0-preview8-28405-07-x64.rpm
sudo rpm -ivh dotnet-runtime-3.0.0-preview8-28405-07-x64.rpm
sudo rpm -ivh aspnetcore-runtime-3.0.0-preview8.19405.7-x64.rpm
sudo rpm -ivh dotnet-apphost-pack-3.0.0-preview8-28405-07-x64.rpm
sudo rpm -ivh dotnet-targeting-pack-3.0.0-preview8-28405-07-x64.rpm
sudo rpm -ivh netstandard-targeting-pack-2.1.0-preview8-28405-07-x64.rpm
sudo rpm -ivh aspnetcore-targeting-pack-3.0.0-preview8.19405.7.rpm
sudo rpm -ivh dotnet-sdk-3.0.100-preview8-013656-x64.rpm
'''

### Installation from a binary archive

Installing from the packages detailed above is recommended or you can install from binary archive, if that better suits your needs. When using binary archives to install, the contents must be extracted to a user location such as `$HOME/dotnet`, a symbolic link created for `dotnet` and a few dependencies installed. Dependency requirements can be seen in the [Linux System Prerequisites](https://github.com/dotnet/core/blob/master/Documentation/linux-prereqs.md) document.

'''bash
mkdir -p $HOME/dotnet && tar zxf dotnet.tar.gz -C $HOME/dotnet
export PATH=$PATH:$HOME/dotnet
'''

## .NET Core Runtime-only installation

If only the .NET Core Runtime is needed, install `dotnet-runtime-3.0` using your package manager. If you also need ASP.NET Core functionality, installing `aspnetcore-runtime-3.0` will install both the ASP Runtime and .NET Core Runtime.

## Windows Server Hosting

If you are looking to host stand-alone apps on Servers, the following installer can be used on Windows systems.

### Windows

You can download the Windows Server Hosting installer and run the following command from an Administrator command prompt:

* [dotnet-hosting-3.0.0-preview8.19405.7-win.exe][dotnet-hosting-win.exe]

This will install the ASP.NET Core Module for IIS.

[blob-runtime]: https://dotnetcli.blob.core.windows.net/dotnet/Runtime/
[blob-sdk]: https://dotnetcli.blob.core.windows.net/dotnet/Sdk/
[release-notes]: https://github.com/dotnet/core/blob/master/release-notes/3.0/preview/3.0.0-preview8.md

[//]: # ( Runtime 3.0.0-preview8-28405-07)
[dotnet-host-x64.deb]: https://download.visualstudio.microsoft.com/download/pr/24de5026-3471-4803-b674-689b338569df/10770879c266d430f4707e4f05f14559/dotnet-host-3.0.0-preview8-28405-07-x64.deb
[dotnet-host-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/e6c88fa0-7af3-4a5e-924c-c2b7746a3c56/058c182d3153f92102c36ba18a540c73/dotnet-host-3.0.0-preview8-28405-07-x64.rpm
[dotnet-hostfxr-x64.deb]: https://download.visualstudio.microsoft.com/download/pr/f65168d8-ecae-473a-a5ca-4300ed6d82ca/1ef8f137d05783380d128550fb1f0eb8/dotnet-hostfxr-3.0.0-preview8-28405-07-x64.deb
[dotnet-hostfxr-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/be0dd399-26ff-4535-8817-cea74af8870f/caba64c029563357d10101531e7d1bba/dotnet-hostfxr-3.0.0-preview8-28405-07-x64.rpm

[dotnet-apphost-pack-x64.deb]: https://download.visualstudio.microsoft.com/download/pr/0afc82ac-e13e-4079-8579-0b17ead6479a/37153d3072e9f32ae816664b40302c28/dotnet-apphost-pack-3.0.0-preview8-28405-07-x64.deb
[dotnet-apphost-pack-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/ec8c5f86-bf16-460d-b873-671b4d01cf21/389bf94fb1070ff4f115b68212b0ab0e/dotnet-apphost-pack-3.0.0-preview8-28405-07-x64.rpm
[dotnet-runtime-linux-arm.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/a2e0f456-964a-4b90-bcd2-37b18bcdbfeb/30dc00fa236512937c1fbbdbecd269bb/dotnet-runtime-3.0.0-preview8-28405-07-linux-arm.tar.gz
[dotnet-runtime-linux-arm64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/177a9aa3-d714-4c14-8421-8ba58eaad7fa/cc80f512ca48c6b57ddb923e3505c7b6/dotnet-runtime-3.0.0-preview8-28405-07-linux-arm64.tar.gz
[dotnet-runtime-linux-musl-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/40161cce-db0e-4b42-826d-a8c8a48f926b/36589bcb129c09d631430908812e549a/dotnet-runtime-3.0.0-preview8-28405-07-linux-musl-x64.tar.gz
[dotnet-runtime-linux-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/3873ce54-438c-43bd-871b-0472e4d5462b/01353d2e8c4289bb344d935c4bf4de3e/dotnet-runtime-3.0.0-preview8-28405-07-linux-x64.tar.gz
[dotnet-runtime-osx-x64.pkg]: https://download.visualstudio.microsoft.com/download/pr/1fe828e7-0544-4f49-b13f-0e14674c8c9a/27ec82f1180d55732827bd96fe303631/dotnet-runtime-3.0.0-preview8-28405-07-osx-x64.pkg
[dotnet-runtime-osx-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/2bd72232-17fe-4108-a6a4-1883ad898443/98d9f83c932aa00567c234f47f9423b2/dotnet-runtime-3.0.0-preview8-28405-07-osx-x64.tar.gz
[dotnet-runtime-rhel.6-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/4257101f-2cc4-4a69-86ec-1919a199746a/beddc17d2d5f7ffdfc2416c57b756c4d/dotnet-runtime-3.0.0-preview8-28405-07-rhel.6-x64.tar.gz
[dotnet-runtime-win-arm.zip]: https://download.visualstudio.microsoft.com/download/pr/328328f0-5072-4977-b487-e5dadea73bfb/68b1e99931e11074962b1d761af7080b/dotnet-runtime-3.0.0-preview8-28405-07-win-arm.zip
[dotnet-runtime-win-x64.exe]: https://download.visualstudio.microsoft.com/download/pr/f416c728-d905-4774-af89-ff8cdc9d2689/cafc4302d161e67c58513d0c2948ddc9/dotnet-runtime-3.0.0-preview8-28405-07-win-x64.exe
[dotnet-runtime-win-x64.zip]: https://download.visualstudio.microsoft.com/download/pr/76735c7a-b2b9-47e6-9264-38ec2c7da035/f1a9bc6f91d03248a3f2cca392b8a680/dotnet-runtime-3.0.0-preview8-28405-07-win-x64.zip
[dotnet-runtime-win-x86.exe]: https://download.visualstudio.microsoft.com/download/pr/16406ea2-f456-478c-ab15-07f9469c4be5/09c33d058632cec9d97d858d5ddcffb6/dotnet-runtime-3.0.0-preview8-28405-07-win-x86.exe
[dotnet-runtime-win-x86.zip]: https://download.visualstudio.microsoft.com/download/pr/26841e45-2665-4509-9ef0-1fc1660c9015/e92ec24b1825ea21b0c606e4358c9d3b/dotnet-runtime-3.0.0-preview8-28405-07-win-x86.zip
[dotnet-runtime-x64.deb]: https://download.visualstudio.microsoft.com/download/pr/b19fcec7-447a-465a-b1d5-b18084485b8d/40017d81e52d89f3aaac2537357c6c63/dotnet-runtime-3.0.0-preview8-28405-07-x64.deb
[dotnet-runtime-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/c7b80a75-be96-41ed-a17d-fb5d2a7e4ca7/c6ba37aa37e57cc4f15d068921abe225/dotnet-runtime-3.0.0-preview8-28405-07-x64.rpm
[dotnet-runtime-deps-centos.7-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/5be6adc2-91f1-4b19-9a7c-e0e702410f7d/c43d92c201fa97351da60cca0694003d/dotnet-runtime-deps-3.0.0-preview8-28405-07-centos.7-x64.rpm
[dotnet-runtime-deps-fedora.27-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/c76d6e7e-dcba-41bf-83ae-77ef4d4b83b9/80a4ac4e1f832552ebcc5f080bf80610/dotnet-runtime-deps-3.0.0-preview8-28405-07-fedora.27-x64.rpm
[dotnet-runtime-deps-opensuse.42-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/4d4b4728-6e76-48db-8e45-24c2821509bf/d251cdbf921c9c169d54e2ab2a7e0571/dotnet-runtime-deps-3.0.0-preview8-28405-07-opensuse.42-x64.rpm
[dotnet-runtime-deps-oraclelinux.7-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/83403c6f-93e8-4a0f-982b-96c193af0997/bf053f5d21cea9b0cab965ebd46b1d6f/dotnet-runtime-deps-3.0.0-preview8-28405-07-oraclelinux.7-x64.rpm
[dotnet-runtime-deps-rhel.7-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/026acef2-64dc-4028-ac04-413daf0f77d1/fb6340a3423fa2432ae7f5fd4ac8a828/dotnet-runtime-deps-3.0.0-preview8-28405-07-rhel.7-x64.rpm
[dotnet-runtime-deps-sles.12-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/6a8f5337-1e21-4553-b953-a2464a6d4084/28fefb47068cd854e2eab35678e2d154/dotnet-runtime-deps-3.0.0-preview8-28405-07-sles.12-x64.rpm
[dotnet-runtime-deps-x64.deb]: https://download.visualstudio.microsoft.com/download/pr/54a51271-ab58-41f3-9b18-a939888251fe/9b44470e8bc2bb6259e91696ad4e56b5/dotnet-runtime-deps-3.0.0-preview8-28405-07-x64.deb
[dotnet-targeting-pack-x64.deb]: https://download.visualstudio.microsoft.com/download/pr/cb26477c-ca65-4fa7-86cc-de0131303875/b844b61ec6ddab5d82dabc6c5efd419b/dotnet-targeting-pack-3.0.0-preview8-28405-07-x64.deb
[dotnet-targeting-pack-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/ba96af61-e1c3-4668-b2fc-7230c79e1cd0/382c3eabc382e3928ebc56299414c4c8/dotnet-targeting-pack-3.0.0-preview8-28405-07-x64.rpm
[netstandard-targeting-pack-osx-x64.pkg]: https://download.visualstudio.microsoft.com/download/pr/b482d47d-151a-4771-ae98-a05e22faac82/f4447c80442379ed65f5b307a8d0d1e3/netstandard-targeting-pack-2.1.0-preview8-28405-07-osx-x64.pkg
[netstandard-targeting-pack-x64.deb]: https://download.visualstudio.microsoft.com/download/pr/4caf9463-865a-4265-83e6-15fc4c217eb2/320dde5e522457a91b2a1daaa57bb764/netstandard-targeting-pack-2.1.0-preview8-28405-07-x64.deb
[netstandard-targeting-pack-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/82467fdf-3521-4a44-85c6-ef23061a022d/9e07507d17cc70800891aa4441581c9c/netstandard-targeting-pack-2.1.0-preview8-28405-07-x64.rpm

[//]: # ( ASP 3.0.0-preview8.19405.7)
[aspnetcore-runtime-linux-arm.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/8b734651-326f-4eb4-8a75-da94e991a901/f404fe1e1a2e989cb2e7bde13a3a2be5/aspnetcore-runtime-3.0.0-preview8.19405.7-linux-arm.tar.gz
[aspnetcore-runtime-linux-arm64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/0dcbd93c-7fb7-49a6-98f9-9233e97e5c62/6bbfd6a0f2a96793a0f4c38e3cc66306/aspnetcore-runtime-3.0.0-preview8.19405.7-linux-arm64.tar.gz
[aspnetcore-runtime-linux-musl-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/8eefd1be-89e6-4e51-ae9f-75716111e4ba/818c35f8dca4d2e564bbe3da869990f3/aspnetcore-runtime-3.0.0-preview8.19405.7-linux-musl-x64.tar.gz
[aspnetcore-runtime-linux-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/0bff102b-7983-4947-be67-be740e168ec1/d4b2a3818f2849501710b6ee16a1e2be/aspnetcore-runtime-3.0.0-preview8.19405.7-linux-x64.tar.gz
[aspnetcore-runtime-osx-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/b252c8ee-ae2d-4f0c-844b-e9417ca7fa09/39c32d263cab2b233a12399dd246a498/aspnetcore-runtime-3.0.0-preview8.19405.7-osx-x64.tar.gz
[aspnetcore-runtime-rh.rhel.7-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/47a7a0c6-1be7-46f3-87f9-f5be2ea8b6d7/c027ed71e0019276fc98dadb23665a72/aspnetcore-runtime-3.0.0-preview8.19405.7-rh.rhel.7-x64.rpm
[aspnetcore-runtime-win-arm.zip]: https://download.visualstudio.microsoft.com/download/pr/70632f83-b799-4d0b-b543-5b9bbb5a816d/9450fef9f62d19bfad16d9007712173e/aspnetcore-runtime-3.0.0-preview8.19405.7-win-arm.zip
[aspnetcore-runtime-win-x64.exe]: https://download.visualstudio.microsoft.com/download/pr/7554fcf8-7e94-4b8d-96cc-4ace14ac2694/d78ac8ce7902cae8683a6eca67b78111/aspnetcore-runtime-3.0.0-preview8.19405.7-win-x64.exe
[aspnetcore-runtime-win-x64.zip]: https://download.visualstudio.microsoft.com/download/pr/376f6702-cd40-423e-bfc7-00ae38668679/a1e0306d4a56f91c0918db32560bc796/aspnetcore-runtime-3.0.0-preview8.19405.7-win-x64.zip
[aspnetcore-runtime-win-x86.exe]: https://download.visualstudio.microsoft.com/download/pr/321ca295-9e7e-42e2-b54a-1d738bfbb290/014f76039ba4edc71fd6cc5d07774d0b/aspnetcore-runtime-3.0.0-preview8.19405.7-win-x86.exe
[aspnetcore-runtime-win-x86.zip]: https://download.visualstudio.microsoft.com/download/pr/e626edfe-4423-453b-9d43-4ddb5b5deb7d/f0e4480cbb181e6888ce5fd24de7cbc0/aspnetcore-runtime-3.0.0-preview8.19405.7-win-x86.zip
[aspnetcore-runtime-x64.deb]: https://download.visualstudio.microsoft.com/download/pr/13e08a26-96aa-4b54-ab4f-ab967fa13be2/1bbd4e9a5f04e254ec43ede7f43e7005/aspnetcore-runtime-3.0.0-preview8.19405.7-x64.deb
[aspnetcore-runtime-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/fca66248-bd05-4948-8efd-390b5d056397/c3078f7d3368438863eb26d93308858f/aspnetcore-runtime-3.0.0-preview8.19405.7-x64.rpm
[aspnetcore-targeting-pack.deb]: https://download.visualstudio.microsoft.com/download/pr/90cf071f-8412-45b1-9237-ade8d9d5b871/adcdf7d67cb0554f6a53af3d3b303e9d/aspnetcore-targeting-pack-3.0.0-preview8.19405.7.deb
[aspnetcore-targeting-pack.rpm]: https://download.visualstudio.microsoft.com/download/pr/26473bdd-e207-4e89-9eb5-14729db564a9/673896c711e4b8d54543b1c790c31be8/aspnetcore-targeting-pack-3.0.0-preview8.19405.7.rpm
[dotnet-hosting-win.exe]: https://download.visualstudio.microsoft.com/download/pr/b1bc1733-f98d-4a46-ac6c-0183b16344f7/2c46d765b3d2295f575c116b25e5f0b1/dotnet-hosting-3.0.0-preview8.19405.7-win.exe

[//]: # ( SDK 3.0.100-preview8-013656 )
[dotnet-sdk-linux-arm.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/f91f8a12-9278-452c-9c1d-2db285d1ed24/1b9e29825adfaab4a4b616464b00ccc0/dotnet-sdk-3.0.100-preview8-013656-linux-arm.tar.gz
[dotnet-sdk-linux-arm64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/e1463b0d-7289-4e4c-bd2a-a6c008d52793/f9c937d47dd4c5447e863adefb44ab78/dotnet-sdk-3.0.100-preview8-013656-linux-arm64.tar.gz
[dotnet-sdk-linux-musl-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/f455c93d-abd2-4c4b-89da-39c6dd763eb9/2d17f950ee996f7499c1b6ce463f77e1/dotnet-sdk-3.0.100-preview8-013656-linux-musl-x64.tar.gz
[dotnet-sdk-linux-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/a0e368ac-7161-4bde-a139-1a3ef5a82bbe/439cdbb58950916d3718771c5d986c35/dotnet-sdk-3.0.100-preview8-013656-linux-x64.tar.gz
[dotnet-sdk-osx-x64.pkg]: https://download.visualstudio.microsoft.com/download/pr/d6b24cf2-ca2a-46f4-b6c8-72e851b80e16/c0fb5d8040803f8f88326dfde012ddfa/dotnet-sdk-3.0.100-preview8-013656-osx-x64.pkg
[dotnet-sdk-osx-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/a974d0a6-d03a-41c1-9dfd-f5884655fd33/cf9d659401cca08c3c55374b3cb8b629/dotnet-sdk-3.0.100-preview8-013656-osx-x64.tar.gz
[dotnet-sdk-rhel.6-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/2ca974af-c77d-4c18-89f8-3572dea18d24/8c86e55c4b6f7bd69a80fe84a40c5c6d/dotnet-sdk-3.0.100-preview8-013656-rhel.6-x64.tar.gz
[dotnet-sdk-win-arm.zip]: https://download.visualstudio.microsoft.com/download/pr/e24cdd15-ccbe-4524-b623-f6b198d07856/4dd5cac3a1b93257e98044a7ee07c259/dotnet-sdk-3.0.100-preview8-013656-win-arm.zip
[dotnet-sdk-win-x64.exe]: https://download.visualstudio.microsoft.com/download/pr/a46fa009-033b-430d-89a8-c9a107f73d87/d25f962e8212aafb3b0c426eb8cb4dc6/dotnet-sdk-3.0.100-preview8-013656-win-x64.exe
[dotnet-sdk-win-x64.zip]: https://download.visualstudio.microsoft.com/download/pr/701abc79-0ceb-406c-aa4b-5e429c665448/05424ebe3bdb06688b910664fbff0671/dotnet-sdk-3.0.100-preview8-013656-win-x64.zip
[dotnet-sdk-win-x86.exe]: https://download.visualstudio.microsoft.com/download/pr/20950cfc-c203-45ae-ba74-2d1c66178285/8426d962b1c4a2b3f8ae785d0d7aab2a/dotnet-sdk-3.0.100-preview8-013656-win-x86.exe
[dotnet-sdk-win-x86.zip]: https://download.visualstudio.microsoft.com/download/pr/0ae7a584-c325-43d8-a087-e65e9d6a1c54/d7dc063ce3732d76dd97955125e2982f/dotnet-sdk-3.0.100-preview8-013656-win-x86.zip
[dotnet-sdk-x64.deb]: https://download.visualstudio.microsoft.com/download/pr/3dd3123a-7ada-40d0-b920-cd9b22cdb172/5e9142450ceec2b15829ca0fe5c54a68/dotnet-sdk-3.0.100-preview8-013656-x64.deb
[dotnet-sdk-x64.rpm]: https://download.visualstudio.microsoft.com/download/pr/5e6e263d-a49d-4ae5-99f1-56a04e9f10d7/8c787474558b11857b5920ce00466af8/dotnet-sdk-3.0.100-preview8-013656-x64.rpm

[checksums-runtime]: https://dotnetcli.blob.core.windows.net/dotnet/checksums/3.0.0-preview8-28405-07-runtime-sha.txt
[checksums-sdk]: https://dotnetcli.blob.core.windows.net/dotnet/checksums/3.0.100-preview8-013656-sdk-sha.txt

[linux-install]: https://www.microsoft.com/net/download/linux
[linux-setup]: https://github.com/dotnet/core/blob/master/Documentation/linux-setup.md

[dotnet-blog]: https://devblogs.microsoft.com/dotnet/announcing-net-core-3-0-preview-8/
[aspnet-blog]: https://devblogs.microsoft.com/aspnet/asp-net-core-and-blazor-updates-in-net-core-3-0-preview-8/
[ef-blog]: https://devblogs.microsoft.com/dotnet/announcing-entity-framework-core-3-0-preview-8-and-entity-framework-6-3-preview-8

[aspnet_bugs]: https://github.com/aspnet/AspNetCore/issues?q=is%3Aissue+milestone%3A3.0.0-preview8+label%3ADone+label%3Abug
[aspnet_features]: https://github.com/aspnet/AspNetCore/issues?q=is%3Aissue+milestone%3A3.0.0-preview8+label%3ADone+label%3Aenhancement
[coreclr_bugs]: https://github.com/dotnet/coreclr/issues?utf8=%E2%9C%93&q=is%3Aissue+milestone%3A3.0+label%3Abug+
[coreclr_features]: https://github.com/dotnet/coreclr/issues?q=is%3Aissue+milestone%3A3.0+label%3Aenhancement
[corefx_bugs]: https://github.com/dotnet/corefx/issues?q=is%3Aissue+milestone%3A3.0+label%3Abug
[corefx_features]: https://github.com/dotnet/corefx/issues?q=is%3Aissue+milestone%3A3.0+label%3Aenhancement
```
## _release_notes_2_1_2_1_11_2_1_11_download_md
```# .NET Core 2.1.11

.NET Core 2.1.11 comprises:

* .NET Core Runtime 2.1.11
* ASP.NET Core 2.1.11
* .NET Core SDK

See the [Release Notes](2.1.11.md) for details about what is included in this update.

**Note:** If you are a Visual Studio user, there are MSBuild version requirements so use only the .NET Core SDK supported for each Visual Studio version. If you use other development environments, we recommend using the latest SDK release.

| VS Version | .NET Core SDK |
| :-- | :--: |
| Visual Studio 2017 (Windows) | [2.1.507](#downloads) |
| Visual Studio 2019 (Windows) | [2.1.604](../2.1.604-SDK/2.1.604-SDK-download.md) |
| Visual Studio for Mac | https://docs.microsoft.com/en-us/visualstudio/mac/net-core-support |

## Downloads

|           | SDK Installer<sup>1</sup>                        | SDK Binaries<sup>1</sup>                 | Runtime Installer                                        | Runtime Binaries                                 | ASP.NET Core Runtime           |
| --------- | :------------------------------------------:     | :----------------------:                 | :---------------------------:                            | :-------------------------:                      | :-----------------:            |
| Windows   | [x86][dotnet-sdk-win-x86.exe] \| [x64][dotnet-sdk-win-x64.exe] | [x86][dotnet-sdk-win-x86.zip] \| [x64][dotnet-sdk-win-x64.zip] | [x86][dotnet-runtime-win-x86.exe] \| [x64][dotnet-runtime-win-x64.exe] | [x86][dotnet-runtime-win-x86.zip] \| [x64][dotnet-runtime-win-x64.zip] | [x86][aspnetcore-runtime-win-x86.exe] \| [x64][aspnetcore-runtime-win-x64.exe] \| <br> [Hosting Bundle][dotnet-hosting-win.exe]<sup>2</sup> |
| macOS     | [x64][dotnet-sdk-osx-x64.pkg]  | [x64][dotnet-sdk-osx-x64.tar.gz]     | [x64][dotnet-runtime-osx-x64.pkg] | [x64][dotnet-runtime-osx-x64.tar.gz] | [x64][aspnetcore-runtime-osx-x64.tar.gz]<sup>1</sup>
| Linux     | [See installations steps below][linux-install]   | [x64][dotnet-sdk-linux-x64.tar.gz] \| [ARM][dotnet-sdk-linux-arm.tar.gz] \| [ARM64][dotnet-sdk-linux-arm64.tar.gz] \| [x64 Alpine][dotnet-sdk-linux-musl-x64.tar.gz] | - | [x64][dotnet-runtime-linux-x64.tar.gz] \| [ARM][dotnet-runtime-linux-arm.tar.gz] \| [ARM64][dotnet-runtime-linux-arm64.tar.gz] \| [x64 Alpine][dotnet-runtime-linux-musl-x64.tar.gz] | [x64][aspnetcore-runtime-linux-x64.tar.gz]<sup>1</sup>  \| [ARM][aspnetcore-runtime-linux-arm.tar.gz]<sup>1</sup> \| [x64 Alpine][aspnetcore-runtime-linux-musl-x64.tar.gz]<sup>1</sup> |
| RHEL6     | -                                                | [x64][dotnet-sdk-rhel.6-x64.tar.gz]                    | -                                                        | [x64][dotnet-runtime-rhel.6-x64.tar.gz] | - |
| Checksums | [SDK][checksums-sdk]                             | -                                        | [Runtime][checksums-runtime]                             | - | - |
| Symbols   | [CLI][cli-symbols.zip] \| [SDK][dotnet-sdk-symbols.zip]  | -                                        | [Runtime][coreclr-symbols.zip] \| [Shared Framework][corefx-symbols.zip] \| [Setup][core-setup-symbols.zip] | - | [ASP.NET Core][aspnet-symbols.zip] |

1. Includes the .NET Core and ASP.NET Core Runtimes
2. For hosting stand-alone apps on Windows Servers. Includes the ASP.NET Core Module for IIS and can be installed separately on servers without installing .NET Core runtime.


## Docker

The [.NET Core Docker images](https://hub.docker.com/r/microsoft/dotnet/) have been updated for this release. Details on our Docker versioning and how to work with the images can be seen in ["Staying up-to-date with .NET Container Images"](https://devblogs.microsoft.com/dotnet/staying-up-to-date-with-net-container-images/).

## Installing .NET Core on Linux

### Install using Snap

Snap is a system which installs applications in an isolated environment and provides for automatic updates. Many distributions which are not directly supported by .NET Core can use Snaps to install. See the [list of distributions supported Snap](https://docs.snapcraft.io/installing-snapd/6735) for details.

After configuring Snap on your system, run the following command to install the latest .NET Core SDK.

`sudo snap install dotnet-sdk --classic`

When .NET Core in installed using the Snap package, the default .NET Core command is `dotnet-sdk.dotnet`, as opposed to just `dotnet`. The benefit of the namespaced command is that it will not conflict with a globally installed .NET Core version you may have. This command can be aliased to `dotnet` with:

`sudo snap alias dotnet-sdk.dotnet dotnet`

**Note:** Some distros require an additional step to enable access to the SSL certificate. If you experience SSL errors when running `dotnet restore`, see [Linux Setup](https://github.com/dotnet/core/blob/master/Documentation/linux-setup.md) for a possible resolution.

### Install using a Package Manager

Before installing .NET, you will need to register the Microsoft key, register the product repository, and install required dependencies. This only needs to be done once per machine. Refer to [Setting up Linux for .NET Core][linux-setup] for the requirements.

The commands listed below do not specifically incude package managers to help with readability. Here are the package managers typically used by the Distros on which .NET Core is supported.

| Distro | Package Manager  |
| ---             | :----:  |
| CentOS, Oracle  | yum     |
| Debian, Ubuntu  | apt-get |
| Fedora          | dnf     |
| OpenSUSE, SLES  | zypper  |

### Develop applications
To develop applications using the .NET Core SDK, run the following command. The .NET Core runtime and ASP.NET Core runtime are included.

'''bash
sudo [package manager] update or refresh
sudo [package manager] install dotnet-sdk-2.1
'''

### Run applications
If you only need to run existing applications, run the following command. The .NET Core runtime and ASP.NET Core runtime are included.

'''bash
sudo [package manager] update or refresh
sudo [package manager] install aspnetcore-runtime-2.1
'''

### Installation from a binary archive

Installing from the packages detailed above is recommended or you can install from binary archive, if that better suits your needs. When using binary archives to install, the contents must be extracted to a user location such as `$HOME/dotnet`, a symbolic link created for `dotnet` and a few dependencies installed. Dependency requirements can be seen in the [Linux System Prerequisites](https://github.com/dotnet/core/blob/master/Documentation/linux-prereqs.md) document.

'''bash
mkdir -p $HOME/dotnet && tar zxf dotnet.tar.gz -C $HOME/dotnet
export PATH=$PATH:$HOME/dotnet
'''

## .NET Core Runtime-only installation

If only the .NET Core Runtime is needed, install `dotnet-runtime-2.1` using your package manager. If you also need ASP.NET Core functionality, installing `aspnetcore-runtime-2.1` will install both the ASP Runtime and .NET Core Runtime.

## Windows Server Hosting

If you are looking to host stand-alone apps on Servers, the following installer can be used on Windows systems.

### Windows

You can download the Windows Server Hosting installer and run the following command from an Administrator command prompt:

* [dotnet-hosting-2.1.11-win.exe][dotnet-hosting-win.exe]

This will install the ASP.NET Core Module for IIS.

[blob-runtime]: https://dotnetcli.blob.core.windows.net/dotnet/Runtime/
[blob-sdk]: https://dotnetcli.blob.core.windows.net/dotnet/Sdk/
[release-notes]: https://github.com/dotnet/core/blob/master/release-notes/2.1/2.1.11/2.1.11.md

[dotnet-runtime-linux-arm.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/7e34e5f5-e817-4ba4-9bfe-03f341e2a807/5779a613184dd09596f71681064cdaa8/dotnet-runtime-2.1.11-linux-arm.tar.gz
[dotnet-runtime-linux-arm64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/f3238746-7a47-407f-9d30-20de4bfd93e2/0c26aad99851325fd5240909f120614d/dotnet-runtime-2.1.11-linux-arm64.tar.gz
[dotnet-runtime-linux-musl-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/ec41f227-48b2-4a15-a10b-020003e5630b/57d30d09d6cda24b2c9baabdc999f254/dotnet-runtime-2.1.11-linux-musl-x64.tar.gz
[dotnet-runtime-linux-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/dd164132-d4c4-4c1a-8233-a4fc7e157935/bffa5312d613cab1a14f0858f947a6fc/dotnet-runtime-2.1.11-linux-x64.tar.gz
[dotnet-runtime-osx-x64.pkg]: https://download.visualstudio.microsoft.com/download/pr/2e53964c-4433-4668-96c4-9365c9b8a82c/9c4b64e4ed0ef36be09b8a6f7e1f677c/dotnet-runtime-2.1.11-osx-x64.pkg
[dotnet-runtime-osx-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/37fc6578-1d55-45a6-9abb-7c50c70d9640/f5c243f9a198185909e78018aa650dcf/dotnet-runtime-2.1.11-osx-x64.tar.gz
[dotnet-runtime-rhel.6-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/4753698b-f678-4470-a0cf-bcc896d78d45/8bdeb1fd072988ceb7bcf982c7f70c66/dotnet-runtime-2.1.11-rhel.6-x64.tar.gz
[dotnet-runtime-win-arm.zip]: https://download.visualstudio.microsoft.com/download/pr/cb38e0f6-8dc7-4594-9cd6-046964d3c894/b2aa5430c110c0dc6486096b4c834aaf/dotnet-runtime-2.1.11-win-arm.zip
[dotnet-runtime-win-x64.exe]: https://download.visualstudio.microsoft.com/download/pr/0a2dd531-45b5-4d59-9b8f-be5ac2d2e1de/5549783adc792b37ffd1d39c59ee44e2/dotnet-runtime-2.1.11-win-x64.exe
[dotnet-runtime-win-x64.zip]: https://download.visualstudio.microsoft.com/download/pr/e2abeb77-02c9-44e8-ac97-007610b73a18/da40662a3333b8aea5a5cd7bcdd2cc97/dotnet-runtime-2.1.11-win-x64.zip
[dotnet-runtime-win-x86.exe]: https://download.visualstudio.microsoft.com/download/pr/100156ff-737e-4e31-840b-019a13df9519/d34c5667c69603c63d4a9f509f933655/dotnet-runtime-2.1.11-win-x86.exe
[dotnet-runtime-win-x86.zip]: https://download.visualstudio.microsoft.com/download/pr/0621a50e-d816-48f4-9d87-34ed5a5cac83/7bd42f7c0028c64a638716efc9f16bc2/dotnet-runtime-2.1.11-win-x86.zip
[aspnetcore-runtime-linux-arm.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/c2a18acf-4d99-4182-b663-e375bce7d11f/602d241f15d05e954fb54e4180e3fab9/aspnetcore-runtime-2.1.11-linux-arm.tar.gz
[aspnetcore-runtime-linux-musl-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/103a417e-384c-4c59-ac6a-ffe32f9a6d3c/f68e5e76f269a8b75c52bb965adc5b71/aspnetcore-runtime-2.1.11-linux-musl-x64.tar.gz
[aspnetcore-runtime-linux-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/5f0a5410-f311-47d6-a0d7-f8afe245bfc2/d4b0370ee8fdac3e8d8b0da7ec6b649a/aspnetcore-runtime-2.1.11-linux-x64.tar.gz
[aspnetcore-runtime-osx-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/51a5d770-1657-4a5f-a91a-7ffd6cc807d9/7e3f05213ae80a1d5c69e3ac57f79935/aspnetcore-runtime-2.1.11-osx-x64.tar.gz
[aspnetcore-runtime-win-x64.exe]: https://download.visualstudio.microsoft.com/download/pr/d5fcdd67-2037-4b72-99cc-af2c8149dd50/0efc18d67e67ef7d9866af97c04b7ff1/aspnetcore-runtime-2.1.11-win-x64.exe
[aspnetcore-runtime-win-x64.zip]: https://download.visualstudio.microsoft.com/download/pr/02857adc-b4dc-45dd-8d94-91259e32d8b0/bc59bdd5cc47a52024c215e71e2976c7/aspnetcore-runtime-2.1.11-win-x64.zip
[aspnetcore-runtime-win-x86.exe]: https://download.visualstudio.microsoft.com/download/pr/2f25a7cb-aeb0-4be8-a836-942603234572/bf992c77c51dff5f73f39475b7e7d140/aspnetcore-runtime-2.1.11-win-x86.exe
[aspnetcore-runtime-win-x86.zip]: https://download.visualstudio.microsoft.com/download/pr/9f4aafc6-5dd7-4cf7-bec8-a01e8b4fb89a/a6e483792905bbd3b2df3db4f48de13a/aspnetcore-runtime-2.1.11-win-x86.zip
[dotnet-hosting-win.exe]: https://download.visualstudio.microsoft.com/download/pr/0ad9d7d3-3cca-48e8-a5cc-07a5a6b8a020/820fd44b4eca9f31b11875d75068bb74/dotnet-hosting-2.1.11-win.exe
[dotnet-sdk-linux-arm.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/fdbe8dd2-48c8-4ebf-9f99-fb7ff754f4b3/10b0884bcbb04d74155e2474b476cb1e/dotnet-sdk-2.1.507-linux-arm.tar.gz
[dotnet-sdk-linux-arm64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/7d084958-4fc5-48cb-bbf5-c94d98f796a7/501cba38b87badfaa39d262c23919cab/dotnet-sdk-2.1.507-linux-arm64.tar.gz
[dotnet-sdk-linux-musl-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/a82af378-d707-4c64-8e56-da2d0a62f0f7/8c3efbc60cdf66fcfa2db1ea3e4f7fcc/dotnet-sdk-2.1.507-linux-musl-x64.tar.gz
[dotnet-sdk-linux-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/c82b55d4-f2b4-4d54-8848-66d53fe113ec/defe61b7a4bc81ae28e976afdd4ae183/dotnet-sdk-2.1.507-linux-x64.tar.gz
[dotnet-sdk-osx-x64.pkg]: https://download.visualstudio.microsoft.com/download/pr/cfab2310-202d-4a46-8a80-13a0fe0a5917/4fef66f60a0ae12d6e93bdd308c642a4/dotnet-sdk-2.1.507-osx-x64.pkg
[dotnet-sdk-osx-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/8698ce7a-0d86-40af-a955-9407bd4e9969/f2d9af9d7d7d0e959b875a7347abdc6e/dotnet-sdk-2.1.507-osx-x64.tar.gz
[dotnet-sdk-rhel.6-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/3e1c269a-1e72-4109-ae57-dcb0da621f22/9c00e2d10d44ed645e632784c0f68eea/dotnet-sdk-2.1.507-rhel.6-x64.tar.gz
[dotnet-sdk-win-x64.exe]: https://download.visualstudio.microsoft.com/download/pr/6674c926-b8f3-416b-abc2-1db57fa50dc9/6f53e3c39b2dae4e78a1325f3427ee11/dotnet-sdk-2.1.507-win-x64.exe
[dotnet-sdk-win-x64.zip]: https://download.visualstudio.microsoft.com/download/pr/8169bcb9-02bf-4380-8876-f63bfb0533d0/ac681a87b5fa21953cb9a0c0fffc4fe7/dotnet-sdk-2.1.507-win-x64.zip
[dotnet-sdk-win-x86.exe]: https://download.visualstudio.microsoft.com/download/pr/bc958862-8a27-470d-a22d-8075964271e5/df19cf19705249cfd37fd64df97157eb/dotnet-sdk-2.1.507-win-x86.exe
[dotnet-sdk-win-x86.zip]: https://download.visualstudio.microsoft.com/download/pr/5de9f59c-f953-4f93-9fa8-5d7015103255/342598bf94a7cb0c5e2222c09017f890/dotnet-sdk-2.1.507-win-x86.zip
[aspnet-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/10122067-a94f-4053-94e8-f03deda2135f/064bb8dde0397d188f6e88ed7eeac62c/aspnet-2.1.11-symbols.zip
[cli-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/fa32c182-4029-4d71-a5d8-3aad70e00f92/f2137db910cd2ea8adff8ff195b12556/cli-2.1.11-symbols.zip
[core-setup-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/b63f344a-5a87-41ae-82d2-81990ca1e867/ec5a0af3e688522dda8b7b51adbb0083/core-setup-2.1.11-symbols.zip
[coreclr-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/c6b1326f-8c0e-474a-b6c6-b372660403e3/9b2a0cb31e64bb1ad8736692284c0fec/coreclr-2.1.11-symbols.zip
[corefx-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/210587a4-fb59-49a4-8fbb-f15e95751f49/ecf9abdb30a2428236b499d2144826bc/corefx-2.1.11-symbols.zip
[dotnet-sdk-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/a782c245-3b40-4cbd-8c6e-a88758d591be/980df24ada29dd20ea452e1cb9c31d36/dotnet-sdk-2.1.11-symbols.zip
[sdk-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/563ddb49-52c6-44e5-bf1f-4c3d69d96380/7a18b8197e797933da76469b5e916127/sdk-2.1.507-symbols.zip

[checksums-runtime]: https://dotnetcli.blob.core.windows.net/dotnet/checksums/2.1.11-runtime-sha.txt
[checksums-sdk]: https://dotnetcli.blob.core.windows.net/dotnet/checksums/2.1.507-sdk-sha.txt

[linux-install]: https://www.microsoft.com/net/download/linux
[linux-setup]: https://github.com/dotnet/core/blob/master/Documentation/linux-setup.md
[dotnet-blog]: https://devblogs.microsoft.com/dotnet/net-core-may-2019/

```
## _release_notes_2_1_Preview_2_1_600_preview_commits_md
```# Commits to .NET Core SDK 2.1.600 Preview

This is a curated list of commits across the .NET Core SDK 2.1.600 Preview development cycle.

## CLI

* [`[237d5c07f]`](https://github.com/dotnet/cli/commit/237d5c07f) Update FSharp.Compiler to 10.3.0-rtm-181113-07
* [`[47248757a]`](https://github.com/dotnet/cli/commit/47248757a) Fix helix queue machine affinity call
* [`[9033fa9d0]`](https://github.com/dotnet/cli/commit/9033fa9d0) Updating NuGet to 5.0.0-preview1.5663
* [`[df07caaff]`](https://github.com/dotnet/cli/commit/df07caaff) Updating NuGet to 5.0.0-preview1.5495
* [`[c129ba1f2]`](https://github.com/dotnet/cli/commit/c129ba1f2) Updating the Windows pool to a pool that supports net472. This will likely have to be force merged before the new pool gets picked up.
* [`[d5327fa08]`](https://github.com/dotnet/cli/commit/d5327fa08) Updating some more projects due to MSbuild not having a target for netstandard2.0. Also, reacting to the msbuild versioning change to Current.
* [`[8bedf2c1b]`](https://github.com/dotnet/cli/commit/8bedf2c1b) Additional framework changes for full framework due to MSBuild supported TFMs.
* [`[9aa3248ef]`](https://github.com/dotnet/cli/commit/9aa3248ef) Updating roslyn and msbuild dependencies for dev16. Needed to move projects to netcoreapp2.2 as msbuild dropped support for netstandard2.0.
* [`[a62a0fead]`](https://github.com/dotnet/cli/commit/a62a0fead) Updating the CLI branding to 2.1.600 for this branch.```
## _release_notes_download_archives_preview4_download_md
```# .NET Core SDK 1.0 Preview 4 build 004233

The installers and binary archives on this page include .NET Core 1.0 SDK Preview 4. [Checksums](https://dotnetcli.blob.core.windows.net/dotnet/checksums/1.0.1-SDK-Preview-4-4233-SHA.txt) are available to verify downloads.

| .NET Core 1.0 Preview 4 | SDK Installer                                        | SDK Binaries                                        | Runtime Installer | Runtime Binaries |
| ----------------------- | :----------------------------------------------: | :----------------------------------------------:| :--: | :--: |
| Windows                 | [32-bit](https://go.microsoft.com/fwlink/?linkid=838402) / [64-bit](https://go.microsoft.com/fwlink/?linkid=838401)  | [32-bit](https://go.microsoft.com/fwlink/?linkid=837978) / [64-bit](https://go.microsoft.com/fwlink/?linkid=837977) | [32-bit](https://go.microsoft.com/fwlink/?LinkID=827516) / [64-bit](https://go.microsoft.com/fwlink/?LinkID=827515) | [32-bit](https://go.microsoft.com/fwlink/?LinkID=825883) / [64-bit](https://go.microsoft.com/fwlink/?LinkID=825882) |
| macOS                   | [64-bit](https://go.microsoft.com/fwlink/?linkid=838403)  | [64-bit](https://go.microsoft.com/fwlink/?linkid=837973)                          | [64-bit](https://go.microsoft.com/fwlink/?LinkID=827517) | [64-bit](https://go.microsoft.com/fwlink/?LinkID=825884) |
| CentOS 7.1              | -                                                         | [64-bit](https://go.microsoft.com/fwlink/?linkid=837969)                          | - | [64-bit](https://go.microsoft.com/fwlink/?LinkID=825888) |
| Debian 8                | -                                                         | [64-bit](https://go.microsoft.com/fwlink/?linkid=837970)                          | - | [64-bit](https://go.microsoft.com/fwlink/?LinkID=825887) |
| Fedora 23               | -                                                         | [64-bit](https://go.microsoft.com/fwlink/?linkid=837971)                          | - | [64-bit](https://go.microsoft.com/fwlink/?LinkID=825891) |
| openSUSE 13.2           | -                                                         | [64-bit](https://go.microsoft.com/fwlink/?linkid=837972)                          | - | [64-bit](https://go.microsoft.com/fwlink/?LinkID=825890) |
| Ubuntu 14.04            | See notes below for Ubuntu 14.04 and Mint 17 installers   | [64-bit](https://go.microsoft.com/fwlink/?linkid=837976)                          | - | [64-bit](https://go.microsoft.com/fwlink/?LinkID=825885) |
| Ubuntu 16.04            | See notes below for Ubuntu 16.04 and Mint 18 installers   | [64-bit](https://go.microsoft.com/fwlink/?linkid=837975)                          | - | [64-bit](https://go.microsoft.com/fwlink/?LinkID=825886) |

## Installation from a binary archive

When using binary archives to install, we recommend the contents be extracted to `/opt/dotnet` and a symbolic link created for `dotnet`. If an earlier release of .NET Core is already installed, the directory and symbolic link may already exist. Ubuntu and Mint users should follow the instructions in the Ubuntu Installation section below.

'''bash
sudo mkdir -p /opt/dotnet
sudo tar zxf [tar.gz filename] -C /opt/dotnet
sudo ln -s /opt/dotnet/dotnet /usr/local/bin
'''

## Ubuntu installation

'''
dotnet-host-ubuntu-x64.deb
dotnet-hostfxr-ubuntu-x64.deb
dotnet-sharedframework-ubuntu-x64.deb
dotnet-sdk-ubuntu-x64.1.0.0-preview4-004233.deb
'''

### Set up package source

The first step is to establish the source feed for the package manager. This is only needed if you have not previously set up the source or if you are installing for the first time.

#### Ubuntu 14.04 and Linux Mint 17

'''bash
sudo sh -c 'echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/dotnet-release/ trusty main" > /etc/apt/sources.list.d/dotnetdev.list'
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893
sudo apt-get update
sudo apt-get install dotnet-dev-1.0.0-preview4-004233

'''

Installed packages

'''
dotnet-host-ubuntu-x64.1.0.1.deb
dotnet-hostfxr-ubuntu-x64.1.0.1.deb
dotnet-sharedframework-ubuntu-x64.1.0.1.deb
dotnet-sdk-ubuntu-x64.1.0.0-preview4-004233.deb
'''

#### Ubuntu 16.04 and Linux Mint 18

'''bash
sudo sh -c 'echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/dotnet-release/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list'
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893
sudo apt-get update
sudo apt-get install dotnet-dev-1.0.0-preview4-004233
'''

Installed packages

'''
dotnet-host-ubuntu.16.04-x64.1.0.1.deb
dotnet-hostfxr-ubuntu.16.04-x64.1.0.1.deb
dotnet-sharedframework-ubuntu.16.04-x64.1.0.1.deb
dotnet-sdk-ubuntu.16.04-x64.1.0.0-preview4-004233.deb
'''
```
## _release_notes_1_0_1_0_11_md
```# .NET Core April 2018 Update - April 17, 2018

Microsoft is releasing updates for .NET Core and ASP.NET Core. Issues addressed by this update are summarized in the [fixes](#notable-fixes-and-commits) section below.

.NET Core 1.0.11 and SDK 1.1.8 are available for download and usage in your environment.

* [Getting Started](https://www.microsoft.com/net/core/)
* [Downloads](https://github.com/dotnet/core/blob/master/release-notes/download-archives/1.0.11-download.md)

The .NET Core SDK 1.1.9 includes .NET Core 1.0.11 Runtime so downloading the runtime packages separately is not needed when installing the SDK. After installing the .NET Core SDK 1.1.8, the following command will show that you're running version `1.1.9` of the tools.

`dotnet --version`

Your feedback is important and appreciated. We've created an issue at [dotnet/core #1452](https://github.com/dotnet/core/issues/1452) for your questions and comments.

## Docker Images

The [.NET Core Docker images](https://hub.docker.com/r/microsoft/dotnet/) have been updated for this release. Look for the 1.0.11 images.

## Azure AppServices

Deployment of this update to Azure AppServices is in process. Because AppServices is a high availability service, the deployment is carfully staged across regions over a period of time. Deployment will begin in the West US 2 and North Central US regions with remaining regions following over a few days.

## Known Issues

### Using Linux package managers to update `dotnet-host.x86_64` breaks .NET Core

**Issue:** Running the package manager `update` command on Linux systems where .NET Core has been previously installed may offer an update for `dotnet-host.x86_64`. If the update is allowed to proceed, .NET Core could be in a broken state as only the dotnet host is updated.

**Resolution:** To install the update, either the Runtime or SDK must be explicitly installed. e.g. `sudo apt-get install dotnet-sharedframework-microsoft.netcore.app-1.0.11`, if you only need the runtime or `sudo apt-get dotnet-dev-1.1.9`, to install both the SDK and Runtime.

We are working to improve our Linux packages to enable correct package manager update behavior. This work is being tracked in the following issues:

* [dotnet/core-setup/issues/3556](https://github.com/dotnet/core-setup/issues/3556)
* [dotnet/cli/issues/8209](https://github.com/dotnet/cli/issues/8209)

## Package and Binary updates

The following packages and binaries are updated by the April 2018 update:

* System.Console

## Notable Fixes and Commits

#### CoreFX

[`[1e4cbe3]`](https://github.com/dotnet/corefx/pull/27634/commits/1e4cbe30140735b944d7918d7a8384ec5f45f183) : Adding support for ncurses 6.1 TERM format on System.Console.```
## _release_notes_2_1_api_diff_2_0_vs_2_1_System_ComponentModel_Design_Serialization_md
```# System.ComponentModel.Design.Serialization

''' diff
 namespace System.ComponentModel.Design.Serialization {
-    public struct MemberRelationship
+    public readonly struct MemberRelationship
 }
'''

```
## _release_notes_1_1_1_0_1_1_api_diff_1_0_1_1_api_diff_System_Threading_Tasks_md
```# System.Threading.Tasks

''' diff
 namespace System.Threading.Tasks {
     public struct ValueTask<TResult> : IEquatable<ValueTask<TResult>> {
+        public static AsyncValueTaskMethodBuilder<TResult> CreateAsyncMethodBuilder();
     }
 }
'''

```
## _release_notes_2_1_Preview_api_diff_preview2_2_1_preview2_System_IO_md
```# System.IO

''' diff
 namespace System.IO {
     public static class Directory {
+        public static IEnumerable<string> EnumerateDirectories(string path, string searchPattern, EnumerationOptions enumerationOptions);
+        public static IEnumerable<string> EnumerateFiles(string path, string searchPattern, EnumerationOptions enumerationOptions);
+        public static IEnumerable<string> EnumerateFileSystemEntries(string path, string searchPattern, EnumerationOptions enumerationOptions);
+        public static string[] GetDirectories(string path, string searchPattern, EnumerationOptions enumerationOptions);
+        public static string[] GetFiles(string path, string searchPattern, EnumerationOptions enumerationOptions);
+        public static string[] GetFileSystemEntries(string path, string searchPattern, EnumerationOptions enumerationOptions);
     }
     public sealed class DirectoryInfo : FileSystemInfo {
+        public IEnumerable<DirectoryInfo> EnumerateDirectories(string searchPattern, EnumerationOptions enumerationOptions);
+        public IEnumerable<FileInfo> EnumerateFiles(string searchPattern, EnumerationOptions enumerationOptions);
+        public IEnumerable<FileSystemInfo> EnumerateFileSystemInfos(string searchPattern, EnumerationOptions enumerationOptions);
+        public DirectoryInfo[] GetDirectories(string searchPattern, EnumerationOptions enumerationOptions);
+        public FileInfo[] GetFiles(string searchPattern, EnumerationOptions enumerationOptions);
+        public FileSystemInfo[] GetFileSystemInfos(string searchPattern, EnumerationOptions enumerationOptions);
     }
+    public class EnumerationOptions {
+        public EnumerationOptions();
+        public FileAttributes AttributesToSkip { get; set; }
+        public int BufferSize { get; set; }
+        public bool IgnoreInaccessible { get; set; }
+        public MatchCasing MatchCasing { get; set; }
+        public MatchType MatchType { get; set; }
+        public bool RecurseSubdirectories { get; set; }
+        public bool ReturnSpecialDirectories { get; set; }
+    }
+    public enum MatchCasing {
+        CaseInsensitive = 2,
+        CaseSensitive = 1,
+        PlatformDefault = 0,
+    }
+    public enum MatchType {
+        Simple = 0,
+        Win32 = 1,
+    }
     public class MemoryStream : Stream {
-        public override Task WriteAsync(ReadOnlyMemory<byte> source, CancellationToken cancellationToken=default(CancellationToken));

+        public override ValueTask WriteAsync(ReadOnlyMemory<byte> source, CancellationToken cancellationToken=default(CancellationToken));
     }
     public static class Path {
+        public static ReadOnlySpan<char> GetDirectoryName(ReadOnlySpan<char> path);
+        public static ReadOnlySpan<char> GetExtension(ReadOnlySpan<char> path);
+        public static ReadOnlySpan<char> GetFileName(ReadOnlySpan<char> path);
+        public static ReadOnlySpan<char> GetFileNameWithoutExtension(ReadOnlySpan<char> path);
+        public static string GetFullPath(string path, string basePath);
+        public static ReadOnlySpan<char> GetPathRoot(ReadOnlySpan<char> path);
+        public static bool HasExtension(ReadOnlySpan<char> path);
+        public static bool IsPathFullyQualified(ReadOnlySpan<char> path);
+        public static bool IsPathRooted(ReadOnlySpan<char> path);
+        public static string Join(ReadOnlySpan<char> path1, ReadOnlySpan<char> path2);
+        public static string Join(ReadOnlySpan<char> path1, ReadOnlySpan<char> path2, ReadOnlySpan<char> path3);
+        public static bool TryJoin(ReadOnlySpan<char> path1, ReadOnlySpan<char> path2, ReadOnlySpan<char> path3, Span<char> destination, out int charsWritten);
+        public static bool TryJoin(ReadOnlySpan<char> path1, ReadOnlySpan<char> path2, Span<char> destination, out int charsWritten);
     }
     public abstract class Stream : MarshalByRefObject, IDisposable {
-        public virtual int Read(Span<byte> destination);
+        public virtual int Read(Span<byte> buffer);
-        public virtual ValueTask<int> ReadAsync(Memory<byte> destination, CancellationToken cancellationToken=default(CancellationToken));
+        public virtual ValueTask<int> ReadAsync(Memory<byte> buffer, CancellationToken cancellationToken=default(CancellationToken));
-        public virtual void Write(ReadOnlySpan<byte> source);
+        public virtual void Write(ReadOnlySpan<byte> buffer);
-        public virtual Task WriteAsync(ReadOnlyMemory<byte> source, CancellationToken cancellationToken=default(CancellationToken));

+        public virtual ValueTask WriteAsync(ReadOnlyMemory<byte> buffer, CancellationToken cancellationToken=default(CancellationToken));
     }
 }
'''

```
## _release_notes_3_0_preview_api_diff_preview1_3_0_preview1_System_Reflection_md
```# System.Reflection

''' diff
 namespace System.Reflection {
     public class CustomAttributeData {
-        public Type AttributeType { get; }
+        public virtual Type AttributeType { get; }
     }
+    public interface ICustomTypeProvider {
+        Type GetCustomType();
+    }
     public enum MethodImplAttributes {
+        AggressiveOptimization = 512,
     }
     public abstract class TypeInfo : Type, IReflectableType {
+        protected TypeInfo();
     }
 }
'''

```
## _release_notes_1_1_1_0_sdk_contributor_list_md
```# Contributions to .NET Core SDK 1.0

We're still working out the best way to present contributors and trying to be as accurate as possible. The list below is generated with the following command listed below in an attempt to capture all contributions which have gone into .NET Core SDK 1.0. Where multiple email addresses were returned for a single person, the counts were aggregated with the email address reported the most commits.


'''bash
git shortlog -sne --no-merges --until release/1.1.0@{2017-02-25}
'''

When you navigate to a contributors commit page, the results are not filtered by release so more commits than are listed below will be shown.

## .NET Core Tools (SDK)

- [Bryan Thornbury (403)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=brthor@microsoft.com)
- [Livar Cunha (303)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=livar@live.com)
- [Eric Erhardt (273)](https://github.com/dotnet/cli/commits/rel/1.0.0?author=eric.erhardt@microsoft.com)
- [Piotr Puszkiewicz (237)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=piotrp@microsoft.com)
- [Sridhar Periyasamy (222)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=sridhper@microsoft.com)
- [David Fowler (164)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=davidfowl@gmail.com)
- [Andrew Stanton-Nurse (148)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=andrew@andrewnurse.net)
- [Pavel Krymets (109)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=pavel@krymets.com)
- [Senthil (106)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=schellap@microsoft.com)
- [Zlatko Knezevic (86)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=zlakne@microsoft.com)
- [Krzysztof Wicher (74)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=kwicher@microsoft.com)
- [Troy Dai (66)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=troy.dai@outlook.com)
- [Mihai Codoban (43)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=micodoba@microsoft.com)
- [Faizan Ahmad (32)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=faahmad@microsoft.com)
- [Krzysztof Wicher (29)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=mordotymoja@gmail.com)
- [Matt Ellis (26)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=matell@microsoft.com)
- [Andy Gocke (25)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=angocke@microsoft.com)
- [Enrico Sada (22)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=enrico@sada.io)
- [Pranav K (20)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=prkrishn@hotmail.com)
- [Justin Goshi (19)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jgoshi@microsoft.com)
- [Andrew Stanton-Nurse (19)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=andrew@stanton-nurse.com)
- [eerhardt (19)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=eric.erhardt@microsoft.com)
- [Eric Mellino (18)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=erme@microsoft.com)
- [Eric St. John (16)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=ericstj@microsoft.com)
- [Petr Onderka (15)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=gsvick@gmail.com)
- [Dan Quirk (13)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=danquirk@microsoft.com)
- [Glenn Condrun (12)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=glennc@microsoft.com)
- [discostu105 (11)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=c.neumueller@gmail.com)
- [Tanner Gooding (11)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=tannergooding@users.noreply.github.com)
- [Richard Lander (10)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=rlander@microsoft.com)
- [Justin Emgarten (10)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=justin@emgarten.com)
- [moozzyk (10)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=pawelka@microsoft.com)
- [Gaurav Khanna (10)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=gkhanna@microsoft.com)
- [Ajay Bhargav Baaskaran (9)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=ajbaaska@microsoft.com)
- [jplebre (9)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jplebre@gmail.com)
- [Rohit Agrawal (9)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=ragrawal@microsoft.com)
- [Jonathan Miller (8)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jonmill@microsoft.com)
- [Rob Mensching (8)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=rob@firegiant.com)
- [Jeff Kluge (8)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jeffkl@microsoft.com)
- [MichaelSimons (7)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=msimons@microsoft.com)
- [Wes Haggard (7)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=Wes.Haggard@microsoft.com)
- [Adam Gorman (7)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=adamgor@microsoft.com)
- [Peter Marcu (7)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=Peter.Marcu@Microsoft.com)
- [Nick Guerrera (7)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=nicholg@microsoft.com)
- [Lakshan Fernando (7)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=lakshanf@microsoft.com)
- [Todd Moscinski (7)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=toddmosc@microsoft.com)
- [Matt Mitchell (6)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=mmitche@microsoft.com)
- [Charles Stoner (6)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=chucks@microsoft.com)
- [dasMulli (6)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=martin.andreas.ullrich@gmail.com)
- [cartermp (6)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=phcart@microsoft.com)
- [Ryan Nowak (5)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=nowakra@gmail.com)
- [Nate Amundson (5)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=naamunds@microsoft.com)
- [Jared Parsons (5)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jaredpar@microsoft.com)
- [Michael Simons (4)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=msimons@microsoft.com)
- [Austin Wise (4)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=AustinWise@gmail.com)
- [Joel Verhagen (4)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jver@microsoft.com)
- [N. Taylor Mullen (4)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=nimullen@microsoft.com)
- [mendhak (3)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=gpslogger@mendhak.com)
- [Dennis Fricke (3)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=github@dennis-fricke.de)
- [Nate McMaster (3)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=nate.mcmaster@microsoft.com)
- [Tomas Matousek (3)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=tomas.matousek@microsoft.com)
- [James Ko (3)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jamesqko@gmail.com)
- [Davis Goodin (3)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=dagood@microsoft.com)
- [Arun Mahapatra (3)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=codito@users.noreply.github.com)
- [v-masche (3)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=v-masche@DDVMASCHE492)
- [Aditya Mandaleeka (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=adityam@microsoft.com)
- [Bill Wert (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=billwert@microsoft.com)
- [Daniel Podder (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=dpodder@gmail.com)
- [Faizan2304 (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=faizan2304@hotmail.com)
- [Fredric Silberberg (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=frsilb@microsoft.com)
- [Jeremy Meng (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jeremy.ymeng@gmail.com)
- [Kevin Jones (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=kevin@vcsjones.com)
- [Lakshmi Priya Sekar (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=lasekar@microsoft.com)
- [Lee Campbell (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=lee.ryan.campbell@gmail.com)
- [Manish Jayaswal (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=manishj@microsoft.com)
- [Mike Lorbetske (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=mlorbe@microsoft.com)
- [Peter Schneider (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=office@schneider-netservices.com)
- [Phil Henning (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=phenning@microsoft.com)
- [Rob Relyea (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=rrelyea@microsoft.com)
- [Shannon (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=sdeminick@gmail.com)
- [Victor Hurdugaci (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=victor.hurdugaci@microsoft.com)
- [rkakadia (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=rajesh.kakadia@gmail.com)
- [seancpeters (2)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=sepeters@microsoft.com)
- [Kyungwoo Lee (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=kyulee@microsoft.com)
- [nattress (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=simonn@microsoft.com)
- [Jérémie Galarneau (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jeremie.galarneau@gmail.com)
- [Juergen Hoetzel (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=juergen@archlinux.org)
- [Jostein Kjonigsen (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jostein@kjonigsen.net)
- [Jonathan Miller (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jon@jonathans-mbp.guest.corp.microsoft.com)
- [Noah Falk (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=noahfalk@microsoft.com)
- [Adam Baxter (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=voltagex@voltagex.org)
- [Jonathan Miller (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jon@Jonathans-MacBook-Pro.local)
- [Peter Jas (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=necmon@yahoo.com)
- [John Van Tuyl (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jpvantuyl@gmail.com)
- [Alex KeySmith (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=AlexKeySmith@users.noreply.github.com)
- [John Luo (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jt.luo@mail.utoronto.ca)
- [Ajay Bhargav Baaskaran (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=ajaybhargavb@gmail.com)
- [Joel Hendrix (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jhendrix@microsoft.com)
- [Jan Vorlicek (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=janvorli@microsoft.com)
- [Jan Kotas (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jkotas@microsoft.com)
- [Hyung-Kyu Choi (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=hk0110.choi@samsung.com)
- [Geoff Norton (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=grompf@gmail.com)
- [Rob Relyea (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=rob@relyeas.net)
- [Aleksandar Milicevic (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=almili@microsoft.com)
- [Falco (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=rs38@users.noreply.github.com)
- [Erik Schierboom (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=erik_schierboom@hotmail.com)
- [Scott Carlton (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=v-sccarl@microsoft.com)
- [Senthil Chellappan (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=schellap@bose.guest.corp.microsoft.com)
- [wtgodbe (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=wigodbe@microsoft.com)
- [Simon de Lang (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=simondelang@gmail.com)
- [Dongyun Jin (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=dongyun.jin@samsung.com)
- [Tanner Gooding (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=tannergooding@outlook.com)
- [Dennis Fischer (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=fischer_dennis@live.de)
- [The Gitter Badger (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=badger@gitter.im)
- [David Lechner (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=david@lechnology.com)
- [Daniel Podder (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=dapodd@microsoft.com)
- [Daniel Bradley (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=daniel@danielbradley.net)
- [shahid-pk (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=shahid.mrd@hotmail.com)
- [Damian Edwards (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=damian@damianedwards.com)
- [William Li (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=wul@microsoft.com)
- [Zhi Li (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=zhili128@outlook.com)
- [Chris Rummel (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=crummel@microsoft.com)
- [Chris R (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=crummel@microsoft.com)
- [Cesar Blum Silveira (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=cesars@microsoft.com)
- [stephentoub (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=stoub@microsoft.com)
- [Brice Lambson (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=bricelam@outlook.com)
- [Brice Lambson (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=bricelam@microsoft.com)
- [drewgil (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=drewgil@microsoft.com)
- [Brian Robbins (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=brianrob@microsoft.com)
- [factormystic (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=factormystic@gmail.com)
- [Ben Adams (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=thundercat@illyriad.co.uk)
- [jacalvar (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jacalvar@microsoft.com)
- [Bart Koelman (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=bartkoelmanNOSPAM@NOSPAMgmail.com)
- [jtkech (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=jean-thierry.kechichian@wanadoo.fr)
- [kloun (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=andrey0bolkonsky@gmail.com)
- [kotov.a (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=kotov.a@hotmail.com)
- [martincostello (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=martin@martincostello.com)
- [Alexander Kozlenko (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=alexander.kozlenko@live.com)
- [Alex Panov (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=alpaix@outlook.com)
- [Mark Clearwater (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=mclearwater@gmail.com)
- [Mark Junker (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=fubar-coder@users.noreply.github.com)
- [Mark Rendle (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=mark@markrendle.net)
- [Luke Latham (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=mis@guardrex.com)
- [Matt Galbraith (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=MattGal@users.noreply.github.com)
- [Luke Elliott (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=revlucio@gmail.com)
- [Mattias Karlsson (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=mattias@devlead.se)
- [Lakshmi Priya (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=Priya91@users.noreply.github.com)
- [Kai Eichinger (1)](https://github.com/dotnet/cli/commits/rel/1.0.0-preview2.1?author=cH40z-Lord@outlook.com)


```
## _release_notes_2_1_api_diff_2_0_vs_2_1_System_Threading_Tasks_Dataflow_md
```# System.Threading.Tasks.Dataflow

''' diff
 namespace System.Threading.Tasks.Dataflow {
-    public struct DataflowMessageHeader : IEquatable<DataflowMessageHeader>
+    public readonly struct DataflowMessageHeader : IEquatable<DataflowMessageHeader>
 }
'''

```
## _release_notes_3_0_preview_api_diff_preview3_3_0_preview3_System_Threading_md
```# System.Threading

''' diff
 namespace System.Threading {
-    public readonly struct CancellationTokenRegistration : IDisposable, IEquatable<CancellationTokenRegistration>
+    public readonly struct CancellationTokenRegistration : IAsyncDisposable, IDisposable, IEquatable<CancellationTokenRegistration>
-    public sealed class Timer : MarshalByRefObject, IDisposable
+    public sealed class Timer : MarshalByRefObject, IAsyncDisposable, IDisposable
 }
'''

```
## _release_notes_2_1_Preview_api_diff_rc1_2_1_rc1_md
```# API Difference release-2.1-preview2 vs release-2.1-rc1

API listing follows standard diff formatting. Lines preceded by a '+' are
additions and a '-' indicates removal.

* [System](#system)
* [System.Buffers](#systembuffers)
* [System.Runtime.InteropServices](#systemruntimeinteropservices)

## System

''' diff
 namespace System {
     [System.Runtime.InteropServices.StructLayoutAttribute(System.Runtime.InteropServices.LayoutKind.Sequential)]
     public struct Decimal : IComparable, IComparable<decimal>, IConvertible, IDeserializationCallback, IEquatable<decimal>, IFormattable {
-        public static Decimal Parse(ReadOnlySpan<char> s, NumberStyles style=(NumberStyles)(7), IFormatProvider provider=null);
+        public static Decimal Parse(ReadOnlySpan<char> s, NumberStyles style=(NumberStyles)(111), IFormatProvider provider=null);
     }
     [System.Runtime.InteropServices.StructLayoutAttribute(System.Runtime.InteropServices.LayoutKind.Sequential)]
     public struct Double : IComparable, IComparable<double>, IConvertible, IEquatable<double>, IFormattable {
-        public static Double Parse(ReadOnlySpan<char> s, NumberStyles style=(NumberStyles)(7), IFormatProvider provider=null);
+        public static Double Parse(ReadOnlySpan<char> s, NumberStyles style=(NumberStyles)(231), IFormatProvider provider=null);
     }
     [System.Runtime.InteropServices.StructLayoutAttribute(System.Runtime.InteropServices.LayoutKind.Sequential)]
     public struct Memory<T> {
-        public Memory(MemoryManager<T> manager, int start, int length);

-        public static Memory<T> CreateFromPinnedArray(T[] array, int start, int length);

     }
     [System.Runtime.InteropServices.StructLayoutAttribute(System.Runtime.InteropServices.LayoutKind.Sequential)]
     public struct ReadOnlySpan<T> {
+        public ref T GetPinnableReference();
     }
     [System.Runtime.InteropServices.StructLayoutAttribute(System.Runtime.InteropServices.LayoutKind.Sequential)]
     public struct SequencePosition : IEquatable<SequencePosition> {
-        public static bool operator ==(SequencePosition left, SequencePosition right);

-        public static bool operator !=(SequencePosition left, SequencePosition right);

     }
     [System.Runtime.InteropServices.StructLayoutAttribute(System.Runtime.InteropServices.LayoutKind.Sequential)]
     public struct Single : IComparable, IComparable<float>, IConvertible, IEquatable<float>, IFormattable {
-        public static Single Parse(ReadOnlySpan<char> s, NumberStyles style=(NumberStyles)(7), IFormatProvider provider=null);
+        public static Single Parse(ReadOnlySpan<char> s, NumberStyles style=(NumberStyles)(231), IFormatProvider provider=null);
     }
     [System.Runtime.InteropServices.StructLayoutAttribute(System.Runtime.InteropServices.LayoutKind.Sequential)]
     public struct Span<T> {
+        public ref T GetPinnableReference();
     }
 }
'''

## System.Buffers

''' diff
 namespace System.Buffers {
     public abstract class MemoryManager<T> : IDisposable, IMemoryOwner<T>, IPinnable {
-        public virtual int Length { get; }

+        protected Memory<T> CreateMemory(int length);
+        protected Memory<T> CreateMemory(int start, int length);
     }
 }
'''

## System.Runtime.InteropServices

''' diff
 namespace System.Runtime.InteropServices {
     public static class MemoryMarshal {
+        public static Memory<T> CreateFromPinnedArray<T>(T[] array, int start, int length);
     }
     public static class SequenceMarshal {
-        public static bool TryGetMemoryManager<T>(ReadOnlySequence<T> sequence, out MemoryManager<T> manager, out int start, out int length);

     }
 }
'''

```
## _release_notes_3_0_preview_api_diff_preview7_3_0_preview7_System_Reflection_Metadata_md
```# System.Reflection.Metadata

''' diff
 namespace System.Reflection.Metadata {
     public class ImageFormatLimitationException : Exception {
+        protected ImageFormatLimitationException(SerializationInfo info, StreamingContext context);
     }
 }
'''

```
## _release_notes_3_0_preview_api_diff_preview8_Asp_Net_3_0_preview8_Microsoft_AspNetCore_Components_Browser_md
```# Microsoft.AspNetCore.Components.Browser

''' diff
-namespace Microsoft.AspNetCore.Components.Browser {
 {
-    public static class RendererRegistryEventDispatcher {
 {
-        public static Task DispatchEvent(RendererRegistryEventDispatcher.BrowserEventDescriptor eventDescriptor, string eventArgsJson);

-        public class BrowserEventDescriptor {
 {
-            public BrowserEventDescriptor();

-            public int BrowserRendererId { get; set; }

-            public string EventArgsType { get; set; }

-            public EventFieldInfo EventFieldInfo { get; set; }

-            public int EventHandlerId { get; set; }

-        }
-    }
-}
'''

```
## _release_notes_1_1_1_1_8_md
```# .NET Core April 2018 Update - April 17, 2018

Microsoft is releasing updates for .NET Core and ASP.NET Core. Issues addressed by this update are summarized in the [fixes](#notable-fixes-and-commits) section below.

.NET Core 1.1.8 and SDK 1.1.9 are available for download and usage in your environment.

* [Getting Started](https://www.microsoft.com/net/core/)
* [Downloads](https://github.com/dotnet/core/blob/master/release-notes/download-archives/1.1.8-download.md)

The .NET Core SDK 1.1.9 includes .NET Core 1.1.8 Runtime so downloading the runtime packages separately is not needed when installing the SDK. After installing the .NET Core SDK 1.1.9, the following command will show that you're running version `1.1.9` of the tools.

`dotnet --version`

Your feedback is important and appreciated. We've created an issue at [dotnet/core #1452](https://github.com/dotnet/core/issues/1452) for your questions and comments.

## Docker Images

The [.NET Core Docker images](https://hub.docker.com/r/microsoft/dotnet/) have been updated for this release. Look for the 1.1.8 images.

## Azure AppServices

Deployment of this update to Azure AppServices is in process. Because AppServices is a high availability service, the deployment is carfully staged across regions over a period of time. Deployment will begin in the West US 2 and North Central US regions with remaining regions following over a few days.

## Known Issues

### Using Linux package managers to update `dotnet-host.x86_64` breaks .NET Core

**Issue:** Running the package manager `update` command on Linux systems where .NET Core has been previously installed may offer an update for `dotnet-host.x86_64`. If the update is allowed to proceed, .NET Core could be in a broken state as only the dotnet host is updated.

**Resolution:** To install the update, either the Runtime or SDK must be explicitly installed. e.g. `sudo apt-get install dotnet-sharedframework-microsoft.netcore.app-1.1.8`, if you only need the runtime or `sudo apt-get dotnet-dev-1.1.9`, to install both the SDK and Runtime.

We are working to improve our Linux packages to enable correct package manager update behavior. This work is being tracked in the following issues:

* [dotnet/core-setup/issues/3556](https://github.com/dotnet/core-setup/issues/3556)
* [dotnet/cli/issues/8209](https://github.com/dotnet/cli/issues/8209)

## Package and Binary updates

The following packages and binaries are updated by the April 2018 update:

* System.Console
* libcoreclr.so
* libdbgshim.so
* libmscordac.so
* libjit.so
* crossgen
* ilasm
* ildasm

## Notable Fixes and Commits

#### CoreFX

[`[4859394]`](https://github.com/dotnet/corefx/pull/27632/commits/4859394b7e7cbae1bc7257926fbe1cdb1769085a) : Adding support for ncurses 6.1 TERM format on System.Console.

#### CoreCLR
[`[18e410f]`](https://github.com/dotnet/coreclr/pull/16576/commits/18e410ffaa72a2bc390421478a65c6ddd9e19edd) : Fix detection of YMM regs presence```
## _release_notes_2_1_Preview_api_diff_preview2_2_1_preview2_System_Reflection_Metadata_md
```# System.Reflection.Metadata

''' diff
 namespace System.Reflection.Metadata {
     public sealed class DebugMetadataHeader {
+        public int IdStartOffset { get; }
     }
     [System.Runtime.InteropServices.StructLayoutAttribute(System.Runtime.InteropServices.LayoutKind.Sequential)]
     public struct TypeDefinition {
+        public bool IsNested { get; }
     }
 }
'''

```
## _release_notes_2_2_2_2_204_SDK_2_2_204_SDK_download_md
```# .NET Core SDK 2.2.204

This .NET Core SDK release is the version which shipped with Visual Studio 2019. It includes the following released .NET Core and ASP.NET Core Runtimes.

* .NET Core SDK 2.2.204
* .NET Core Runtime 2.2.5
* ASP.NET Core 2.2.5

**Note:** If you are a Visual Studio user, there are MSBuild version requirements so use only the .NET Core SDK supported for each Visual Studio version. If you use other development environments, we recommend using the latest SDK release.

| VS Version | .NET Core SDK |
| :-- | :--: |
| Visual Studio 2017 (Windows) | [2.2.107](../2.2.5/2.2.5-download.md) |
| Visual Studio 2019 (Windows) | [2.2.204](#downloads) |
| Visual Studio for Mac | https://docs.microsoft.com/en-us/visualstudio/mac/net-core-support |

## Downloads

|           | SDK Installer<sup>1</sup>                        | SDK Binaries<sup>1</sup>                 | Runtime Installer                                        | Runtime Binaries                                 | ASP.NET Core Runtime           |
| --------- | :------------------------------------------:     | :----------------------:                 | :---------------------------:                            | :-------------------------:                      | :-----------------:            |
| Windows   | [x86][dotnet-sdk-win-x86.exe] \| [x64][dotnet-sdk-win-x64.exe] | [x86][dotnet-sdk-win-x86.zip] \| [x64][dotnet-sdk-win-x64.zip] | [x86][dotnet-runtime-win-x86.exe] \| [x64][dotnet-runtime-win-x64.exe] | [x86][dotnet-runtime-win-x86.zip] \| [x64][dotnet-runtime-win-x64.zip] | [x86][aspnetcore-runtime-win-x86.exe] \| [x64][aspnetcore-runtime-win-x64.exe] \| <br> [Hosting Bundle][dotnet-hosting-win.exe]<sup>2</sup> |
| macOS     | [x64][dotnet-sdk-osx-x64.pkg]  | [x64][dotnet-sdk-osx-x64.tar.gz]     | [x64][dotnet-runtime-osx-x64.pkg] | [x64][dotnet-runtime-osx-x64.tar.gz] | [x64][aspnetcore-runtime-osx-x64.tar.gz]<sup>1</sup>
| Linux     | [See installations steps below][linux-install]   | [x64][dotnet-sdk-linux-x64.tar.gz] \| [ARM][dotnet-sdk-linux-arm.tar.gz] \| [ARM64][dotnet-sdk-linux-arm64.tar.gz] \| [x64 Alpine][dotnet-sdk-linux-musl-x64.tar.gz] | - | [x64][dotnet-runtime-linux-x64.tar.gz] \| [ARM][dotnet-runtime-linux-arm.tar.gz] \| [ARM64][dotnet-runtime-linux-arm64.tar.gz] \| [x64 Alpine][dotnet-runtime-linux-musl-x64.tar.gz] | [x64][aspnetcore-runtime-linux-x64.tar.gz]<sup>1</sup>  \| [ARM][aspnetcore-runtime-linux-arm.tar.gz]<sup>1</sup> \| [x64 Alpine][aspnetcore-runtime-linux-musl-x64.tar.gz]<sup>1</sup> |
| RHEL6     | -                                                | [x64][dotnet-sdk-rhel.6-x64.tar.gz]                    | -                                                        | [x64][dotnet-runtime-rhel.6-x64.tar.gz] | - |
| Checksums | [SDK][checksums-sdk]                             | -                                        | [Runtime][checksums-runtime]                             | - | - |
| Symbols   | [CLI][cli-symbols.zip] \| [SDK][dotnet-sdk-symbols.zip]  | -                                        | [Runtime][coreclr-symbols.zip] \| [Shared Framework][corefx-symbols.zip] \| [Setup][core-setup-symbols.zip] | - | [ASP.NET Core][aspnet-symbols.zip] |

1. Includes the .NET Core and ASP.NET Core Runtimes
2. For hosting stand-alone apps on Windows Servers. Includes the ASP.NET Core Module for IIS and can be installed separately on servers without installing .NET Core runtime.

## Docker

The [.NET Core Docker images](https://hub.docker.com/r/microsoft/dotnet/) have been updated for this release. Details on our Docker versioning and how to work with the images can be seen in ["Staying up-to-date with .NET Container Images"](https://devblogs.microsoft.com/dotnet/staying-up-to-date-with-net-container-images/).

## Installing .NET Core on Linux

### Install using a Package Manager

Before installing .NET, you will need to register the Microsoft key, register the product repository, and install required dependencies. This only needs to be done once per machine. Refer to [Setting up Linux for .NET Core][linux-setup] for the requirements.

The commands listed below do not specifically incude package managers to help with readability. Here are the package managers typically used by the Distros on which .NET Core is supported.

| Distro | Package Manager  |
| ---             | :----:  |
| CentOS, Oracle  | yum     |
| Debian, Ubuntu  | apt-get |
| Fedora          | dnf     |
| OpenSUSE, SLES  | zypper  |

### Develop applications
To develop applications using the .NET Core SDK, run the following command. The .NET Core runtime and ASP.NET Core runtime are included.

'''bash
sudo [package manager] update or refresh
sudo [package manager] install dotnet-sdk-2.2
'''

### Run applications
If you only need to run existing applications, run the following command. The .NET Core runtime and ASP.NET Core runtime are included.

'''bash
sudo [package manager] update or refresh
sudo [package manager] install aspnetcore-runtime-2.2
'''

### Installation from a binary archive

Installing from the packages detailed above is recommended or you can install from binary archive, if that better suits your needs. When using binary archives to install, the contents must be extracted to a user location such as `$HOME/dotnet`, a symbolic link created for `dotnet` and a few dependencies installed. Dependency requirements can be seen in the [Linux System Prerequisites](https://github.com/dotnet/core/blob/master/Documentation/linux-prereqs.md) document.

'''bash
mkdir -p $HOME/dotnet && tar zxf dotnet.tar.gz -C $HOME/dotnet
export PATH=$PATH:$HOME/dotnet
'''

## .NET Core Runtime-only installation

If only the .NET Core Runtime is needed, install `dotnet-runtime-2.2` using your package manager. If you also need ASP.NET Core functionality, installing `aspnetcore-runtime-2.2` will install both the ASP Runtime and .NET Core Runtime.

## Windows Server Hosting

If you are looking to host stand-alone apps on Servers, the following installer can be used on Windows systems.

### Windows

You can download the Windows Server Hosting installer and run the following command from an Administrator command prompt:

* [dotnet-hosting-2.2.5-win.exe][dotnet-hosting-win.exe]

This will install the ASP.NET Core Module for IIS.

[blob-runtime]: https://dotnetcli.blob.core.windows.net/dotnet/Runtime/
[blob-sdk]: https://dotnetcli.blob.core.windows.net/dotnet/Sdk/
[release-notes]: https://github.com/dotnet/core/blob/master/release-notes/2.2/2.2.204-SDK/2.2.204-SDK.md

[dotnet-runtime-linux-arm.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/87521bd8-1522-4141-9532-91d580292c42/59116d9f6ebced4fdc8b76b9e3bbabbf/dotnet-runtime-2.2.5-linux-arm.tar.gz
[dotnet-runtime-linux-arm64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/7aca89ca-5196-4b89-93bc-1ee1eeb251d7/ca4ff94c8692a6846a756fc07174974d/dotnet-runtime-2.2.5-linux-arm64.tar.gz
[dotnet-runtime-linux-musl-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/e6c7d880-e951-49ba-9ad1-1b7ab92647c0/82fd0a220c311dae0096aa1fc857b003/dotnet-runtime-2.2.5-linux-musl-x64.tar.gz
[dotnet-runtime-linux-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/21968111-f65e-48c7-9c35-8b40de4af06c/66b7a2c7b92b54bd3311f4509cc9b9ed/dotnet-runtime-2.2.5-linux-x64.tar.gz
[dotnet-runtime-osx-x64.pkg]: https://download.visualstudio.microsoft.com/download/pr/5a373bc6-6284-4bce-aff5-791900a05241/f6761a726ca304512f05258d416f2a6b/dotnet-runtime-2.2.5-osx-x64.pkg
[dotnet-runtime-osx-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/3451957c-1d40-4ec4-a439-d018f92c5c12/77a0101ccfb7f5edc768f258450b295c/dotnet-runtime-2.2.5-osx-x64.tar.gz
[dotnet-runtime-rhel.6-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/f7969882-ed80-4f57-8f7e-10576a3a43ad/afa91359198122a385e9527187c7313c/dotnet-runtime-2.2.5-rhel.6-x64.tar.gz
[dotnet-runtime-win-arm.zip]: https://download.visualstudio.microsoft.com/download/pr/526d7d4f-cacf-452f-af9c-a13d55949490/32a864dadc46f8cea3924aee2023d347/dotnet-runtime-2.2.5-win-arm.zip
[dotnet-runtime-win-x64.exe]: https://download.visualstudio.microsoft.com/download/pr/57b58505-b244-485f-b2fb-181c442f314e/07aad4d611362c0e6ddf8ea77799ebdd/dotnet-runtime-2.2.5-win-x64.exe
[dotnet-runtime-win-x64.zip]: https://download.visualstudio.microsoft.com/download/pr/84ea4970-ac74-4a0c-a93d-b2438c507dac/9babcf7e3f459a1ddb1fe0df02fdc619/dotnet-runtime-2.2.5-win-x64.zip
[dotnet-runtime-win-x86.exe]: https://download.visualstudio.microsoft.com/download/pr/3810a636-75a9-497a-98f0-48ad497e339e/093ab61953f8a1d05fa27e54ffa7868b/dotnet-runtime-2.2.5-win-x86.exe
[dotnet-runtime-win-x86.zip]: https://download.visualstudio.microsoft.com/download/pr/ae0efd9e-e55d-4148-9d95-dd3e5fd8e6d2/5297cf422f6b4818077a6f459acde520/dotnet-runtime-2.2.5-win-x86.zip
[aspnetcore-runtime-linux-arm.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/cd6635b9-f6f8-4c2d-beda-2e381fe39586/740973b83c199bf863a51c83a2432151/aspnetcore-runtime-2.2.5-linux-arm.tar.gz
[aspnetcore-runtime-linux-musl-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/f49a9f48-15ca-430e-b618-2e133c266d2e/e79e338cbbd15e0835b27c25d9463976/aspnetcore-runtime-2.2.5-linux-musl-x64.tar.gz
[aspnetcore-runtime-linux-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/411768dc-83c3-4b15-acd3-d4490aad6dde/90e0b4848a18585ab4fc170c8d7a2fbe/aspnetcore-runtime-2.2.5-linux-x64.tar.gz
[aspnetcore-runtime-osx-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/d655e91b-d5b3-4925-9520-1f7b7dcb73ac/b860dd24c035e206d3edc181129cc47d/aspnetcore-runtime-2.2.5-osx-x64.tar.gz
[aspnetcore-runtime-win-arm.zip]: https://download.visualstudio.microsoft.com/download/pr/c239e990-da4e-4c6f-9f47-c39b8679d159/4b4795085f593d3479b222fef5721d54/aspnetcore-runtime-2.2.5-win-arm.zip
[aspnetcore-runtime-win-x64.exe]: https://download.visualstudio.microsoft.com/download/pr/28989ee4-5f2a-4a2e-bc48-4fdb8e3e78af/81cf0048a65e782111ecb76116f1439d/aspnetcore-runtime-2.2.5-win-x64.exe
[aspnetcore-runtime-win-x64.zip]: https://download.visualstudio.microsoft.com/download/pr/1e67f249-a5d7-48a3-81c6-99b5ce398295/bc840f7a713e39e2e7ef30034adbeedf/aspnetcore-runtime-2.2.5-win-x64.zip
[aspnetcore-runtime-win-x86.exe]: https://download.visualstudio.microsoft.com/download/pr/bd58c47e-0538-4c15-aaaa-edef158ccaa0/008cf89ab5a656e3305bb99ce3ed8d82/aspnetcore-runtime-2.2.5-win-x86.exe
[aspnetcore-runtime-win-x86.zip]: https://download.visualstudio.microsoft.com/download/pr/b969a905-45f3-47cb-9496-4d502df0d904/5b2467d0289ab68863fa2ef7f13c2f7d/aspnetcore-runtime-2.2.5-win-x86.zip
[dotnet-hosting-win.exe]: https://download.visualstudio.microsoft.com/download/pr/34f4b2a6-c3b8-495c-a11f-6db955f27757/8c340c1a8c25966e39e0c0a4b308dff4/dotnet-hosting-2.2.5-win.exe
[dotnet-sdk-linux-arm.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/fc0c7de2-24cb-45e4-a354-df612b5c3420/b8cc998c1c66717309d1e59ea979e1f3/dotnet-sdk-2.2.204-linux-arm.tar.gz
[dotnet-sdk-linux-arm64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/3d3d9050-ab4e-4303-9c2b-48fabbf10ed6/fba8b766585dbeeea3a6b608304f7526/dotnet-sdk-2.2.204-linux-arm64.tar.gz
[dotnet-sdk-linux-musl-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/4d98fe3d-3e82-4480-aacb-58b6960ff723/fc2bcc933285bbf97367854728e6f3bd/dotnet-sdk-2.2.204-linux-musl-x64.tar.gz
[dotnet-sdk-linux-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/ece856bb-de15-4df3-9677-67cc817ffc1b/521da52132d23deae5400b8e19e23691/dotnet-sdk-2.2.204-linux-x64.tar.gz
[dotnet-sdk-osx-x64.pkg]: https://download.visualstudio.microsoft.com/download/pr/fa52799f-b3cd-4d79-9869-a6b3997b96d7/20479fc2b7925ef40592a40ef89f3099/dotnet-sdk-2.2.204-osx-x64.pkg
[dotnet-sdk-osx-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/405eba1f-9a78-4ac0-99f3-3fad5107022c/d793c7a75613fb985bb6f7aff522437e/dotnet-sdk-2.2.204-osx-x64.tar.gz
[dotnet-sdk-rhel.6-x64.tar.gz]: https://download.visualstudio.microsoft.com/download/pr/e2943c98-ddba-4768-af91-9936995d5b5d/b10543dc39973d697201a7a13419a9e6/dotnet-sdk-2.2.204-rhel.6-x64.tar.gz
[dotnet-sdk-win-arm.zip]: https://download.visualstudio.microsoft.com/download/pr/d9122ef2-19cc-47d9-8388-f9eba774aa95/045c9fe68e6fbd6db66b505e19b1f927/dotnet-sdk-2.2.204-win-arm.zip
[dotnet-sdk-win-x64.exe]: https://download.visualstudio.microsoft.com/download/pr/e50ce3cf-d86a-4f23-8e75-0d86f6d1eea8/1c0b05791a5b730927664828e002d2c1/dotnet-sdk-2.2.204-win-x64.exe
[dotnet-sdk-win-x64.zip]: https://download.visualstudio.microsoft.com/download/pr/dd744f69-407a-4e70-a877-a5202cbd29ef/0a1cba3bb6e76f698ddd5d0099b0a236/dotnet-sdk-2.2.204-win-x64.zip
[dotnet-sdk-win-x86.exe]: https://download.visualstudio.microsoft.com/download/pr/e849877c-fd37-4a7f-9b53-50b1424d9d0e/66ab464f677a02ee2f8b0fe6159e06b2/dotnet-sdk-2.2.204-win-x86.exe
[dotnet-sdk-win-x86.zip]: https://download.visualstudio.microsoft.com/download/pr/1eafc84c-733a-47c7-8cf7-f121a67550c5/99f2116250751d7e57d8dfc2fadd38af/dotnet-sdk-2.2.204-win-x86.zip
[aspnet-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/0c8969d6-a150-4fd0-b5ee-f85cf47b29fd/8628d29e58df3e675327e89a3cc02eb6/aspnet-2.2.5-symbols.zip
[aspnet-extensions-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/1d8cdfb8-e3b4-470a-838b-629a4df38034/a3b613b6c5bd68514e6ffdc68e43402d/aspnet-extensions-2.2.5-symbols.zip
[cli-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/b7a489d4-5833-486e-af48-47aeba1deead/6e23995d55fdb4241e9135a5f60a975d/cli-2.2.5-symbols.zip
[core-setup-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/0cb24dfa-e1c8-4c7d-b6e8-ada512a895b4/4431f0316bd4af2c8d93df78bddd3931/core-setup-2.2.5-symbols.zip
[coreclr-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/173d6b83-0ee0-4a76-88d4-1b2cb9defc35/5603ecf3d3b2b346f1c41d1ea9d1a6dc/coreclr-2.2.5-symbols.zip
[corefx-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/8ca8518d-3e3e-438b-bb1d-130e96896abf/fb6ce1b1bb8215f0d41c9004d45819ec/corefx-2.2.5-symbols.zip
[dotnet-sdk-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/bc10e87f-b8c9-475f-b128-c79f1b10a479/89bb00ae7d070290942a48261504a73a/dotnet-sdk-2.2.5-symbols.zip
[sdk-symbols.zip]: https://download.visualstudio.microsoft.com/download/pr/8d15bfff-d1c7-448a-adea-6f44d4191413/59632e1b6558ab689a837a1acb6875b3/sdk-2.2.204-symbols.zip

[checksums-runtime]: https://dotnetcli.blob.core.windows.net/dotnet/checksums/2.2.4-runtime-sha.txt
[checksums-sdk]: https://dotnetcli.blob.core.windows.net/dotnet/checksums/2.2.204-sdk-sha.txt

[linux-install]: https://www.microsoft.com/net/download/linux
[linux-setup]: https://github.com/dotnet/core/blob/master/Documentation/linux-setup.md

[dotnet-blog]: https://devblogs.microsoft.com/dotnet/net-core-may-2019/
```
## _release_notes_3_0_preview_api_diff_preview8_Asp_Net_3_0_preview8_Microsoft_JSInterop_Internal_md
```# Microsoft.JSInterop.Internal

''' diff
-namespace Microsoft.JSInterop.Internal {
 {
-    public sealed class JSAsyncCallResult

-}
'''

```
## _release_notes_3_0_preview_api_diff_preview7_3_0_preview7_md
```# API Difference netcoreapp3.0-preview6 vs netcoreapp3.0-preview7

API listing follows standard diff formatting. Lines preceded by a '+' are
additions and a '-' indicates removal.

* [System](3.0-preview7_System.md)
* [System.Collections.Generic](3.0-preview7_System.Collections.Generic.md)
* [System.Collections.Immutable](3.0-preview7_System.Collections.Immutable.md)
* [System.Data.Common](3.0-preview7_System.Data.Common.md)
* [System.Diagnostics](3.0-preview7_System.Diagnostics.md)
* [System.Diagnostics.Tracing](3.0-preview7_System.Diagnostics.Tracing.md)
* [System.Reflection.Emit](3.0-preview7_System.Reflection.Emit.md)
* [System.Reflection.Metadata](3.0-preview7_System.Reflection.Metadata.md)
* [System.Runtime.Intrinsics](3.0-preview7_System.Runtime.Intrinsics.md)
* [System.Runtime.Loader](3.0-preview7_System.Runtime.Loader.md)
* [System.Runtime.Serialization](3.0-preview7_System.Runtime.Serialization.md)
* [System.Security.Cryptography](3.0-preview7_System.Security.Cryptography.md)
* [System.Text](3.0-preview7_System.Text.md)
* [System.Text.Json](3.0-preview7_System.Text.Json.md)
* [System.Text.Json.Serialization](3.0-preview7_System.Text.Json.Serialization.md)
* [System.Threading](3.0-preview7_System.Threading.md)

```
## _README_md
```﻿# .NET Core Home

The dotnet/core repository is a good starting point for .NET Core.

The latest major release is [.NET Core 3.0](release-notes/3.0). The latest patch updates are listed in [.NET Core release notes](release-notes/README.md).

## Download the latest .NET Core SDK

* [.NET Core 3.0 SDK](release-notes/3.0/README.md)

## .NET Core Releases and Daily Builds

* [.NET Core released builds](release-notes/README.md)
* [.NET Core daily builds](daily-builds.md)

## Learn about .NET Core

* [Learn about .NET Core](https://docs.microsoft.com/dotnet/core)
* [.NET Core Roadmap](https://github.com/dotnet/core/blob/master/roadmap.md)
* [Learn about the .NET platform](https://docs.microsoft.com/dotnet/standard/)
* [.NET Core release notes](https://github.com/dotnet/core/blob/master/release-notes/README.md)
* [.NET Core Announcements](https://github.com/dotnet/announcements)
* [.NET Core blog](https://blogs.msdn.microsoft.com/dotnet/tag/net-core/)

## Getting help

* [File a .NET Core issue](https://github.com/dotnet/core/issues)
* [File an ASP.NET Core issue](https://github.com/aspnet/home/issues)
* [File an issue for other components](Documentation/core-repos.md)
* [Ask on Stack Overflow](https://stackoverflow.com/questions/tagged/.net-core)
* [Contact Microsoft Support](https://support.microsoft.com/contactus/)
* [VS Developer Community Portal](https://developercommunity.visualstudio.com/) for "full" .NET Framework feedback (or via [Report a Problem](https://aka.ms/vs-rap) tool)

## How to Engage, Contribute and Provide Feedback

The .NET Core team encourages [contributions](https://github.com/dotnet/coreclr/blob/master/Documentation/project-docs/contributing.md), both issues and PRs. The first step is finding the [.NET Core repository](Documentation/core-repos.md) that you want to contribute to.

### Community

This project uses the [.NET Foundation Code of Conduct](https://dotnetfoundation.org/code-of-conduct) to define expected conduct in our community.
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting a project maintainer at conduct@dotnetfoundation.org.

## .NET Foundation

The .NET Core platform is part of the [.NET Foundation](http://www.dotnetfoundation.org).

## Licenses

.NET Core repos typically use either the [MIT](LICENSE.TXT) or
[Apache 2](http://www.apache.org/licenses/LICENSE-2.0) licenses for code.
Some projects license documentation and other forms of content under
[Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/).

See specific [repos](Documentation/core-repos.md) to understand the license used.
```
# Inline
## _release_notes_1_0_install_1_0_1_sh
### Line 1-8
```
# This is a simple script to assist in manually installing Microsoft.NETCore.App 1.0.1
# and is primarily meant to help Linux users encountering https://github.com/dotnet/cli/issues/3681
# Complete installers are expected to be available with a mid-September release rendering This
# script unneccessary.

echo ===========================================
read -p "Download and install 1.0.1 now? (y/n) " answer


```
### Line 70-81
```
            *fedora.23*)
                archive="dotnet-fedora.23-x64.1.0.1.tar.gz"
            ;;
        esac #rid

        # Check to see if tmp-update has been left behind. If so, clean up first. 
        if [ -d $tmp_dir ]; then
            #tmp_dir left behind from previous attempt
            echo
            echo "Directory "$tmp_dir" already exists and needs to be cleaned before proceding."
            echo
            read -p "Clean up temporary files and locations used by this script (y/n)?" answer

```
### Line 95-117
```
        else
            istmpclean=1 #tmp_dir not found
        fi # exists tmp_dir
        
        if [ $istmpclean == 1 ]; then
            # create ~/tmp-update and cd
            mkdir $tmp_dir && cd $tmp_dir

            # Get Microsoft.NETCore.App archive chosen above 
            echo "Downloading:" $archive
            curl -SL -O -# $download$archive

            echo
            echo "Extracting" $archive

            # Extract /shared
            tar -xvz -f $archive "./shared/Microsoft.NETCore.App/1.0.1/"

            # Move 1.0.1
            echo
            echo "Moving 1.0.1 to" $netcoreapp_dir
            sudo mv shared/Microsoft.NETCore.App/1.0.1 $netcoreapp_dir


```

# Issues
## 2653
Title:
```

        dotnet core not runing
      
```
Author:
```
AgieAja
```
Text:
```

Problem encountered on https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install
Operating System: macos
Provide details about the problem you are experiencing. Include your operating system version, exact error message, code sample, and anything else that is relevant.

```
Author:
```
karelz
```
Text:
```

Did you restart your command line? You need to run the executable - path has to be set, etc.

```

## 745
Title:
```

        Packages restore failed
      
```
Author:
```
subek
```
Text:
```

Package restore
Package restore failed in asp.net core 1.1
Note : i am referencing my project to

"frameworks": {
"net461": { }
},

Recently i upgraded my project from asp.net core 1.0 to 1.1 and it works fine on my old laptop by i switched the project to fresh new laptop ,Installed visual studio 15 .here is the configuration of the VS 15

I have also installed the required SDK as mentioned on this link
https://jeremylindsayni.wordpress.com/2016/11/20/upgrading-from-net-core-1-0-t0-1-1-with-visual-studio-2015/

. Now my project json file looks likes this :

and global.json looks like this

{
"projects": [ "." ]
}

but as you can see the packages are not loading as expected.
when i do dotnet restore from the package manager console
i get something like this :

Any Idea ??

```
Author:
```
Petermarcu
```
Text:
```

It looks like you are still using the unreleased version of everything from late 2015. I would strongly recommend that you upgrade to the supported SDK and tooling. Is there a reason you can't upgrade to the supported .NET Core tooling?

```
Author:
```
subek
```
Text:
```

@Petermarcu  Thanks for the reply man.. i finally was able to solve the issue but not with the latest version but the version i did the update was ..
Microsoft .Net Core 1.0.1 -SDK 1.0.0 Preview 2- 003131
Microsoft .Net Core 1.0.1 -VS 2015 Tooling Preview 2
and this worked for me.

```
Author:
```
Petermarcu
```
Text:
```

Glad to hear it worked for you.

```
Author:
```
shooreshi
```
Text:
```

Same problem here except the installation of the listed SDK and Tooling did not resolve the issue for me in a particular solution while it did work in others after updating my global.json.  I am currently getting dozens of errors  in a specific solution of type:

Severity	Code	Description	Project	File	Line	Suppression State
Error	NU1002	The dependency Microsoft.AspNetCore.Hosting.Abstractions 2.0.1 does not support framework .NETFramework,Version=v4.6.1.

Where the listed dependencies in project.json are not supported.  E.g. error from output:

error: Package Microsoft.Extensions.Logging.Abstractions 2.0.0 is not compatible with net461 (.NETFramework,Version=v4.6.1). Package Microsoft.Extensions.Logging.Abstractions 2.0.0 supports: netstandard2.0 (.NETStandard,Version=v2.0)

Any suggestions other than the nuclear option of removing dotnet 2.1.4 and VS 2017 completely?  Upgrading the solution is out of the question for the moment.

```

## 2186
Title:
```

        Couldn't find a valid ICU package installed on the system?
      
```
Author:
```
olavt
```
Text:
```

I have been running a .NET Core 2.2 application in a Docker container fine on Raspberry PI 3 (using Raspbian Stretch Lite November 2018) with no problems for several weeks.
But, today when trying to run a newly built container I get:
FailFast:
Couldn't find a valid ICU package installed on the system. Set the configuration flag System.Globalization.Invariant to true if you want to run with no globalization support.
at System.Environment.FailFast(System.String)
at System.Globalization.GlobalizationMode.GetGlobalizationInvariantMode()
at System.Globalization.GlobalizationMode..cctor()
at System.Globalization.CultureData.CreateCultureWithInvariantData()
at System.Globalization.CultureData.get_Invariant()
at System.Globalization.CultureInfo..cctor()
at System.StringComparer..cctor()
at System.AppDomain.InitializeCompatibilityFlags()
at System.AppDomain.CreateAppDomainManager()
at System.AppDomain.Setup(System.Object)
This is my Dockerfile:
FROM microsoft/dotnet:2.2-runtime-stretch-slim-arm32v7
WORKDIR /app
COPY bin/Debug/netcoreapp2.2/linux-arm/publish .
ENTRYPOINT ["dotnet", "NesoyaController.dll"]

```
Author:
```
karelz
```
Text:
```

Looks like this documented problem based on quick internet search: https://github.com/dotnet/core/blob/master/Documentation/build-and-install-rhel6-prerequisites.md#troubleshooting

```
Author:
```
olavt
```
Text:
```

How can the article you quoted be relevant to running .NET Core 2.2 in a Docker container using the Microsoft provided base image? Shouldn't the Docker image run with all the dependencies included on the Docker host? As I understand the above article is relevant for installing directly on the OS.

```
Author:
```
karelz
```
Text:
```

Does the Docket image contain the libraries referenced in the article? Given that Docker images try to be as small as possible (esp. --slim variants - see Docker repo), I wouldn't be surprised if that's the case ...
Either way, I assumed, the docs are enough to point in the right direction. Is that not the case? If not, what is unclear or missing?

```
Author:
```
olavt
```
Text:
```

I have been running .NET Core application in Docker images over the past 12 months without this kind of problems. Why should it surface out of the blue?

```
Author:
```
olavt
```
Text:
```

The image runs fine one another Raspberry PI 3 (using the OS image and components), so I suspect that something have went wrong with the platform the Docker image runs on.

```
Author:
```
karelz
```
Text:
```

I was about to suggest that I can see 4 possible reasons:

Change in OS,
Change in Docker image used,
Change in the app, or
The app took different code path.

Looks like you narrowed it down to option 1.

```
Author:
```
andrewwebber
```
Text:
```

I have just experienced this issue when trying to run a self contained dotnet core application on CoreOS Container Linux, without a Docker container.
E.g.
dotnet publish -c Release -o out -r linux-x64
tar -xcvzf out.gz ./out
scp ...
extract ...
run binary
For me this means that self contained publish output still has some dependencies which might need clarification.

```
Author:
```
denniske
```
Text:
```

Same issue here. Deployed self contained application into google/cloud-sdk:slim.

```
Author:
```
andrewwebber
```
Text:
```

My workaround was to edit the generated runtimeconfig.json after following this documentation
https://github.com/dotnet/core/blob/master/Documentation/build-and-install-rhel6-prerequisites.md
{
    "runtimeOptions": {
        "configProperties": {
            "System.Globalization.Invariant": true
        },
    }
}

```
Author:
```
denniske
```
Text:
```

This solved my problem. Instead of modifying the generated runtimeconfig.json, I created a runtimeconfig.template.json in the project folder which is used automatically by dotnet publish to generate the runtimeconfig.json:
{
    "configProperties": {
        "System.Globalization.Invariant": true
    }
}


```

## 954
Title:
```

        NuGet for System.Collections.Immutable has unresolved dependency towards netstandard
      
```
Author:
```
robert-j-engdahl
```
Text:
```

Issue Title
Installing the NuGet package System.Collections.Immutable v1.4.0 targeting .Net 4.6.1 does not include its dependency towards netstandard.
General
After
install-package System.Collections.Immutable -ProjectName SomeProject

And using ImmutableHashSet in some class, Visual Studio is fine, but my TeamCity build fails with the following errors:
Analysis\Recalculation\Recursive\RecursiveAnalysisRecalculatorTest.cs(89, 104): error CS0012: The type 'Object' is defined in an assembly that is not referenced. You must add a reference to assembly 'netstandard, Version=2.0.0.0, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51'.

This goes for other types I've been using for ages such as IEnumerable<> and ValueType.
(And if this is not the right place to file such an issue, you might fix the link for the project site given here https://www.nuget.org/packages/System.Collections.Immutable/)

```
Author:
```
robert-j-engdahl
```
Text:
```

This could be caused by my test projects being 4.6.1 and my production being 4.6.
It did, however, not help to
Install-Package NETStandard.Library -Version 2.0.0

There might be issues that concern the backwards compatibility of 4.6.1 that I am not aware of.

```
Author:
```
a-vishar
```
Text:
```

Running into the same issue on 4.6.2.

```
Author:
```
ghost
```
Text:
```

You will need to install the VS 2017 (MSBuild 2017) on your team city server. Additionally 4.6.0 won't work, you need at least 4.6.2.
https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15
Additionally, I would recommend changing your nuget's to package reference if you haven't already. Look for packages that were installed using an older .net framework version, you will need to reinstall those to ensure you get the correct versions.
Please close this issue as it's not related to .net/standard/core

```
Author:
```
Petermarcu
```
Text:
```

There are some issues with 4.6.1's support of .NET Standard 2.0. For example netstandard.dll version 2.0.0 isn't there and needs to be present with the application (or test in this case). I'm going to move this issue to dotnet/standard because I do think there could be a problem here that we need to look into.

```
Author:
```
Petermarcu
```
Text:
```

Issue moved to dotnet/standard #534 via ZenHub

```

## 758
Title:
```

        Can't run code analysis using MSBuild for .NET Core 2.0 / .NET Standard 2.0 projects
      
```
Author:
```
mizbrodin
```
Text:
```

Hello,
I'm using Visual Studio Enterprise 2017 Preview Version 15.3.0 Preview 4.0 (VisualStudio.15.Preview/15.3.0-pre.4.0+26711.1)
When I try to run code analysis using MSBuild for any .NET Core 2.0 or .NET Standard 2.0 projects using a command like this:
msbuild  /p:RunCodeAnalysis=true netcore2ClassLibrary1.csproj
I'm getting the following errors:

Running Code Analysis...
MSBUILD : error : CA0055 : Could not identify platform for 'E:\Source\Temp\NetS
tandardClassLibrary1\netcore2ClassLibrary1\bin\Debug\netcoreapp2.0\netcore2Clas
sLibrary1.dll'. [E:\Source\Temp\NetStandardClassLibrary1\netcore2ClassLibrary1
netcore2ClassLibrary1.csproj]
MSBUILD : error : CA0052 : No targets were selected. [E:\Source\Temp\NetStandar
dClassLibrary1\netcore2ClassLibrary1\netcore2ClassLibrary1.csproj]
Code Analysis Complete -- 2 error(s), 0 warning(s)

Is this an expected behaviour? If yes, is there any other way to run code analysis for .NET Core/Standard 2.0 projects from a command line and produce the same kind of CodeAnalysisLog.xml file which is produced by MSBuild for .NET Framework projects? (I need it for our CI, for a solution which consists of a large set of old .NET Framework projects and some new .NET Standard projects as well)
Thanks
Max

```
Author:
```
mokeyish
```
Text:
```

@mizbrodin I have this problem, too，but I think you can use jetbrains rider instead。did you solved the problem？

```
Author:
```
mizbrodin
```
Text:
```

@mokeyish I don't have a solution for this problem yet.
Our company doesn't have a license for JetBrains Rider and, at the moment, I don't know anything about this IDE and its build tools. We have Visual Studio Enterprise licenses as part of our MSDN Subscription and I'd prefer to be able to use MSBuild for running code analysis in our CI build configuration as we do it for other projects.

```
Author:
```
ShrenikOne
```
Text:
```

Hi All, We are facing similar issue. Any workaround or solution, Also I additional observation, while compile with "netstandard2.0" as "TargetFramework", generated assembly Platform Target coming as Unknown while with "netstandard1.4" its coming as "Windows Runtime".

```
Author:
```
CFlatWouldbeMinor
```
Text:
```

Same issue here.
It seems to me static code analysis is very fuzzy, or I just used to the existing full framework FxCop solution

```
Author:
```
nelsonmorais
```
Text:
```

Same issue here.

```
Author:
```
skorunka
```
Text:
```

Same problem.

```
Author:
```
sindamnataraj
```
Text:
```

same issue here.

```
Author:
```
FarisFAhmed
```
Text:
```

I have Visual Studio 2017 (15.2) and a .NetStandard core library project.

If the project is targeted for 1.4 and I run MSBuild.exe then everything works
If the project is targeted for 1.5 and I run MSBuild.exe then I get this error:
MSBUILD : error : CA0055 : Coult not identify platform for "...dll path..."


```
Author:
```
csano
```
Text:
```

Are there any plans to address this? Any other options for running FxCop against .NET core projects?

```
Author:
```
zvirja
```
Text:
```

I have a feeling that Microsoft will not continue to support FxCop. Rather, it's expected that you install Microsoft.CodeAnalysis.FxCopAnalyzers NuGet package to your solution and it will run the code analysis via Roslyn API. Actually, they are cooler than FxCop as they:

work quicker;
provide feedback instantly (highlight errors while you are typing);
provide quick fixes.

See more detail here: https://github.com/dotnet/roslyn-analyzers.
Notice, not all the analyzers have been already ported, so it might still make sense to run code analysis for the supported frameworks (e.g. net 452).

```
Author:
```
jahmai
```
Text:
```

@zvirja Do you know if the Nuget package respects the CodeAnalysis MSBuild configuration settings like <RunCodeAnalysis>false</RunCodeAnalysis>, CodeAnalysis dictionarys and the ruleset files?

```
Author:
```
zvirja
```
Text:
```

I've used this package in the AutoFixture project and it seems to respect everything you mentioned.

```
Author:
```
Petermarcu
```
Text:
```

@zvirja is correct. The path forward is the Microsoft.CodeAnalysis.FxCopAnalyzers NuGet package. A large portion of the rules have been moved over to analyzers. FXCop was a solution implemented before the richness of the new C# compiler existed.

```
Author:
```
jahmai
```
Text:
```

Thanks all I'll give the package a try today.

```
Author:
```
Petermarcu
```
Text:
```

Sounds good. I'm going to close this for now but we can re-open this if it doesn't work.

```
Author:
```
dvm-2k1
```
Text:
```

Please let me know Is this CA0055 and CA0052 issues got resolved for .Net Core 2.0 (netcoreapp2.0) projects?
Asking this because I'm still getting these errors when enabled our .Net Core 2.0 projects to use code analysis ruleset which are defined for our projects and trying to build from Visual Studio 2017 (updated to 15.3.5 version) and by using MSBuild command.
As per this conversion thread, I've installed Nuget package of  Microsoft.CodeAnalysis.FxCopAnalyzers to our .net core 2.0 projects, but still getting CA0055 and CA0052 errors. Please help me out to resolve these issues which are blocking our builds.

```
Author:
```
Petermarcu
```
Text:
```

@dvm-2k1 I opened an issue for you here: dotnet/roslyn-analyzers#1313
Thats is the best place to get help for that specific issue.

```
Author:
```
msd-kharazi
```
Text:
```

same here.

```
Author:
```
MelbourneDeveloper
```
Text:
```

@Petermarcu has anyone committed to fixing this issue?
Why is this issue closed? It's still a problem.
The other closed issue says that we need to install a NuGet package and compile at the command line.
Is anyone actually bothering to fix the problem inside Visual Studio?

```
Author:
```
AlexanderJ-ULabs
```
Text:
```

This is still an issue.

```
Author:
```
mokeyish
```
Text:
```

@AlexanderJ-ULabs Your version of Visual Sdtudio and dotnet core might not  be latest enough.

```
Author:
```
Styxxy
```
Text:
```

I came across the same problem when having a solution mixed with .NET Full (non-SDK style projects) and .NET  Standard projects (SDK style projects).
I fixed it by adding following custom target at the end of the project (I actually created a shared targets file which I imports in each SDK style project):
  <Target Name="IgnoreRunCodeAnalysis" Condition=" '$(RunCodeAnalysis)' == 'true' " BeforeTargets="RunCodeAnalysis">
    <Message Importance="normal" Text="Set RunCodeAnalysisOnThisProject to false" />
    <PropertyGroup>
      <RunCodeAnalysisOnThisProject>false</RunCodeAnalysisOnThisProject>
    </PropertyGroup>
  </Target>
If you want code analysis, you can include the (nuget) package Microsoft.CodeAnalysis.FxCopAnalyzers. I did it like below (in my project files), so I can still leverage the global property RunCodeAnalysis:
  <ItemGroup Condition=" '$(RunCodeAnalysis)' == 'true' ">
    <PackageReference Include="Microsoft.CodeAnalysis.FxCopAnalyzers" Version="2.6.1" />
  </ItemGroup>

```
Author:
```
JeremyCaney
```
Text:
```

The idea of replacing the legacy FXCop tooling built into Visual Studio with the NuGet package makes good sense to me. That said, ideally, developers wouldn’t need to Google this error and find this thread to understand the problem. Instead, the tooing should detect the incompatibility and suggest the upgrade path to the user. (Fully recognizing that this level of tooling is likely outside the scope of the team maintaining this repository.)

```
Author:
```
MelbourneDeveloper
```
Text:
```

This article seems pretty relevant:
https://docs.microsoft.com/en-us/visualstudio/code-quality/fxcop-analyzers-faq?view=vs-2017

```
Author:
```
MelbourneDeveloper
```
Text:
```

@Petermarcu
I just added the FX Cop Analyzers NuGet package to my project, and I can see that it does add new errors to the build output. So, I promoted warning to errors, and I get similar errors to those that used to exist in the Visual Studio code rules in the old csproj format, but the issue at first glance is that I can't choose which errors to turn on or off. I have to type them in the suppress field. That's pretty fiddly. Using a suppress puts a pragma in the code which isn't so nice.
Can we get some kind of explanation and history for why Visual Studio has gone down this path? Is it so that code rules could be supported on other platforms like Visual Studio for Mac?
I've written a blog article on how to use the code rules here: https://christianfindlay.wordpress.com/2019/02/11/c-code-rules-part-1/ . I'd really appreciate some feedback, and if someone would write up why FxCop as a command line app is not the recommended approach anymore, I'd be glad to append it to the blog post.

```
Author:
```
karelz
```
Text:
```

@MelbourneDeveloper I recommend to ask on the https://github.com/dotnet/roslyn-analyzers repo
Regarding VS for Mac - that's a good question, I'd ask them on their feedback channel.

```
Author:
```
MelbourneDeveloper
```
Text:
```

@karelz yep, that's already been asked here:
dotnet/roslyn-analyzers#2026

```
Author:
```
karelz
```
Text:
```

@MelbourneDeveloper ok, so you should be all set then, right?

```
Author:
```
MelbourneDeveloper
```
Text:
```

@karelz when they answer the question, yeah.

```
Author:
```
karelz
```
Text:
```

@MelbourneDeveloper understood - my point is that the discussion over here is "finished" and all is properly routed / addressed. If not, please let me know.

```
Author:
```
MelbourneDeveloper
```
Text:
```

@karelz , I understand that there is a path from migrating from the FxCop tool, to the Roslyn Analyzer NuGet package. Basically, it's not finished, and it's not completely integrated in to Visual Studio, but for now, people have some level of code rules. The issue is already closed, so I don't think there's anything to be said for this particular question.

```

## 1125
Title:
```

        Is possible remove IL code from xxx.ni.dll compiled by CrossGen?
      
```
Author:
```
hzexe
```
Text:
```

To software protection，like .NET Native.

```
Author:
```
Petermarcu
```
Text:
```

Issue moved to dotnet/coreclr #15347 via ZenHub

```

## 959
Title:
```

        Serialization error in .net core 2.0, same code was working in .net core 1.1
      
```
Author:
```
chintan3100
```
Text:
```

public class CustomClass
{
[Required]
public System.Guid? clientId { get; set; }
}
"\"bb2f3da7-bf79-4d14-9d54-0a1f7ff5f902\""
system.argumentexception Could not cast or convert from System.String to System.Guid. newtonsoft.json
at Newtonsoft.Json.Serialization.JsonSerializerInternalReader.EnsureType(JsonReader reader, Object value, CultureInfo culture, JsonContract contract, Type targetType)
at Newtonsoft.Json.Serialization.JsonSerializerInternalReader.SetPropertyValue(JsonProperty property, JsonConverter propertyConverter, JsonContainerContract containerContract, JsonProperty containerProperty, JsonReader reader, Object target)
at Newtonsoft.Json.Serialization.JsonSerializerInternalReader.PopulateObject(Object newObject, JsonReader reader, JsonObjectContract contract, JsonProperty member, String id)

```
Author:
```
chintan3100
```
Text:
```

I can not change client call who calling API with "\"bb2f3da7-bf79-4d14-9d54-0a1f7ff5f902\"". Client has code freeze.

```
Author:
```
chintan3100
```
Text:
```

Hi
.net core 1.1 : When we return string from api it like
"bb2f3da7-bf79-4d14-9d54-0a1f7ff5f902"
.net core 2.0
"\"bb2f3da7-bf79-4d14-9d54-0a1f7ff5f902\""

```
Author:
```
Petermarcu
```
Text:
```

@ViktorHofer @danmosemsft can you take a look?

```
Author:
```
ViktorHofer
```
Text:
```

@chintan3100 I spent some time trying to reproduce your issue but I don't have enough information to understand what's going on here.
Please post a small reproduction code. I don't know which APIs you are using (even it they aren't .NET Core related but Json.NET).

```
Author:
```
Petermarcu
```
Text:
```

@ViktorHofer can you move this issue over to dotnet/corefx to track it?

```
Author:
```
ViktorHofer
```
Text:
```

Issue moved to dotnet/corefx #24473 via ZenHub

```

## 3332
Title:
```

        CookieContainer do not handle session cookies (when Expires is not specified)
      
```
Author:
```
M-Boukhlouf
```
Text:
```

CookieContainer do not handle session cookies (when Expires is not specified)
According to this page: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

The maximum lifetime of the cookie as an HTTP-date timestamp. If not specified, the cookie will have the lifetime of a session cookie. A session is finished when the client is shut down meaning that session cookies will get removed at that point.

Yet, in this case when the Expires is not specified in this Set-Cookie header:
Set-Cookie: name=value; path=/store; httponly
The CookieContainer set the Expires property to "1/1/0001 12:00:00 AM"
Which is expired and the cookie is not used in the following requests.

```
Author:
```
M-Boukhlouf
```
Text:
```

This seems to fix it:
After making the request, make a loop on the cookies of that uri, and if the expires was not set, it adds 10 years or how much long you want the session
foreach (Cookie cookie in cookieContainer.GetCookies(uri))
{
	if (cookie.Expires.Ticks == 0)
	{
		cookie.Expires = DateTime.Now.AddYears(10);
	}
}

I still think the CookieContainer should somehow handle it by itself.

```
Author:
```
davidsh
```
Text:
```

.NET Cookies don't work exactly the way browsers handle them.  There is no such thing as "session cookies" in .NET.  Cookies are received on the wire or created by APIs. Then they are stored in an in-memory CookieContainer object. If there is no 'Expires' attribute, then they live "forever" in the sense of living in the CookieContainer object. But when the application exits (the one that created the CookieContainer), the cookie goes away.
Basically, the current behavior is by-design.

```
Author:
```
davidsh
```
Text:
```

@scalablecory fyi. "Cookie" is part of System.Net namespace.

```
Author:
```
M-Boukhlouf
```
Text:
```


If there is no 'Expires' attribute, then they live "forever" in the sense of living in the CookieContainer object. But when the application exits (the one that created the CookieContainer), the cookie goes away.

False, the whole issue I'm having is that the cookie is treated as if it's already expired, thus it's not used afterwards.

```

## 1297
Title:
```

        .NET Core 2.1 Preview 1
      
```
Author:
```
leecow
```
Text:
```

.NET Core 2.1 Preview 1
.NET Core Preview 1 is available. This release includes:

.NET Core 2.1.0-preview1-26216-03 and .NET Core SDK 2.1.300-preview1-008174

You can read about the updates in the .NET Core blog post
Please report any issues you find with 2.1 Preview 1, either responding to this issue, creating a new issue or creating a new issue in one of the following repos:

dotnet/cli - for CLI tools and questions
dotnet/corefx - for API issues and questions
dotnet/coreclr - for runtime issues
dotnet/core-setup - for installer issues
nuget/home - for NuGet questions and issues


```
Author:
```
leedale1981
```
Text:
```

Probably a stupid question but why does .NET Core 2.1.0-preview1 install SDK 2.1.300 but the previous version 2.0.5 installs a later version of the SDK 2.1.4?

```
Author:
```
Petermarcu
```
Text:
```

Because versioning got out of sync and confused people. We now plan to always alight the major and minor.

```
Author:
```
savornicesei
```
Text:
```

Please, please, please, have an unstable and a stable repo for linux distribution.
It took me some time to get everything right on my openSUSE box and I don't want any updates to preview versions of .NET
Other than that ... long live .NET on linux! 👍

```
Author:
```
leecow
```
Text:
```

Thanks @savornicesei - I'm looking into our options.

```
Author:
```
savornicesei
```
Text:
```

@leecow Perhaps open build system could ease the pain of linux multi-distro preview/stable releases

```
Author:
```
tkggusraqk
```
Text:
```

TransactionScope, is the problem fixed?

```
Author:
```
EdLorenzQAT
```
Text:
```

I tested TransactionScope on Linux using this preview and it takes a NPE which is the same result I was seeing from the previous version.
However, under windows, initial testing looks good.

```
Author:
```
jherby2k
```
Text:
```

I'd like to try the new Span-ified functionality like Stream.Read(Span destination) in my library projects, but it looks like they will need to target .NET Standard 2.1. Is there even going to be a .net standard 2.1?? Any other way to obtain these APIs? I added System.Memory but it looks like this method is part of the SDK.

```
Author:
```
BennyTordrupVisma
```
Text:
```

LiuHai119, please stop spamming.

```
Author:
```
simeyla
```
Text:
```

Is there a target date for Preview 2?

```
Author:
```
DaveSlinn
```
Text:
```

The recent update of VS 2017 to 15.6 has broken the build of our solution. It seems to have installed a new folder in the dotnet/sdk called 2.1.100 - and the dotnet cli seems to no longer resolve the references in our solution file properly.

When I do a dotnet --version, I get 2.1.100.  Dev boxes that have are still on 1.5.5.7 do not have 2.1.100 (they have 2.1.4) and still work fine.
What is 2.1.100 and what changed in it from 2.1.4 that is now breaking our builds?

```
Author:
```
Petermarcu
```
Text:
```

@livarcocc Can you look into this one?

```
Author:
```
DaveSlinn
```
Text:
```

Update: after I posted this, I looked into it further and discovered that the dotnet restore was now stopping our builds (whereas prior to the update, it would just display an MSB4019 error.  @livarcocc has already redirected my issue on that to the NuGet team for input at  NuGet/Home#6665

```
Author:
```
bobuva
```
Text:
```

I've installed the preview and trying to make an SSL connection that requires Tls1.2 and ALPN. I know I'm using TLS1.2 because I specify it here:
                    ProxyClient.TestUbuntuHost,
                    null,
                    System.Security.Authentication.SslProtocols.Tls12,
                    false);

but how do I know whether it is using ALPN in the handshake?
Note: I'm going to create a separate issue to get clarification on ALPN usage.

```
Author:
```
Petermarcu
```
Text:
```

@karelz should we open an issue in corefx to track @bobuva's reported issue?

```
Author:
```
karelz
```
Text:
```

Sure, filing questions as separate issues is a good idea. CoreFX is a good place to ask this one.
ALPN is going to be used only if you try to negotiate some application protocol via ApplicationProtocols. See a test. You can always verify by capturing networking traffic via Wireshark.

```
Author:
```
buvinghausen
```
Text:
```

Was excited to see .NET Core 2.1 Preview 2 drop on NuGet 16 hours ago.  Is there an ETA on when the runtime & SDK will make it to Docker Hub?

```
Author:
```
Petermarcu
```
Text:
```

Closing this issue in favor of Preview 2. #1422

```

## 1181
Title:
```

        Core assets missing / Nuget Packages do not restore, and/or corrupt NuGetFallbackFolder
      
```
Author:
```
steevcoco
```
Text:
```

This issue is exactly as described in:
#1006 - ".Net Core v2.0 - Nuget Packages are not getting restored"
and
#5995 - "Assets from packages are missing after restore"
#920 - ".NET Core 2 does not work...."
But, I actually just performed a Windows Defender full "System Refresh", and then a full reinstall of VS Enterprise 15.5.2, and had the issue, so then uninstalled, and did VS Installer InstallCleanup -f, and even after that yet one more full Repair ...
And still I was only able to fix it by eventually removing the NuGetFallbackFolder.
I thought I should post another issue because none of those extensive 'Repairs' actually fixed the problem!

```
Author:
```
Petermarcu
```
Text:
```

@rrelyea probably should move to nuget/home?

```
Author:
```
salmonz
```
Text:
```

I have the same problem. Workaround is run dotnet restore in the console.

```
Author:
```
salmonz
```
Text:
```

@steevcoco what was the permanent resolution? I don't think running dotnet restore int the console is acceptable. Preferred behaviour is when you create a new project in Visual Studio and build, all dependencies should resolve.

```
Author:
```
steevcoco
```
Text:
```

@salmonz sorry: I actually closed the issue because I have not seen the problem again ...
My ACTUAL solution did require deleting the NuGetFallbackFolder. You THEN can do dotnet restore on some solution to rebuild that folder: I had to delete the folder to get it in working order again.
I closed the issue because it has just been sitting open ... Perhaps I should re-open it.

```

## 2857
Title:
```

        dotnet run
      
```
Author:
```
micky9020
```
Text:
```

C:\Users\micky>dotnet run
No se ha podido encontrar un proyecto para ejecutar. Asegúrese de que exista uno en C:\Users\micky o pase la ruta de acceso al proyecto mediante --project.

```
Author:
```
leecow
```
Text:
```

Assuming you have created a project, it looks like you need to navigate to that directory before attempting dotnet run.

```
Author:
```
carlossanlop
```
Text:
```

Translated:

Could not find a project to execute. Make sure that a project exists in C:\Users\micky or pass the access path to the project using --project

Closing due to lack of activity, and @leecow 's answer seems to be the right answer. @micky9020 feel free to reopen the issue if you have any additional questions.

```

## 292
Title:
```

        Missing methods in 1.0.0-preview2-003131
      
```
Author:
```
viewport73
```
Text:
```

I am trying to build an .netcore5.0 (sdk version"1.0.0-preview2-003131") library and I am trying to access Type.GetTypeCode(), MemberTypes.Field, Type.GetTypeInfo().FindMembers() methods but they are missing from the System.Type library.
The methods were accessible/available in previous version of .netcore5.0 (sdk version "1.0.0-preview2-003121).
Is there any other library where I can use the above methods?

```

# Pull
## 1582
Title:
```

        Add ARM32 and Alpine Support
      
```
Author:
```
richlander
```
Text:
```


No description provided.


```
Author:
```
leecow
```
Text:
```

LGTM

```

## 710
Title:
```

        Update 2.0 release docs
      
```
Author:
```
leecow
```
Text:
```


No description provided.


```

## 2606
Title:
```

        Releases.json fixes
      
```
Author:
```
arthurrump
```
Text:
```


No description provided.


```
Author:
```
arthurrump
```
Text:
```

ping @leecow

```

## 1136
Title:
```

        fix link
      
```
Author:
```
leecow
```
Text:
```


No description provided.


```

## 1438
Title:
```

        Document issue in Preview 2 with SocketsHttpHandler on single core machines
      
```
Author:
```
rmkerr
```
Text:
```

Documenting corefx issue #28979. The instructions on switching to the platform handler are taken from the Preview 2 release blog post.

```

## 1160
Title:
```

        link to 2.1.2 SDK rel page
      
```
Author:
```
leecow
```
Text:
```


No description provided.


```

## 3302
Title:
```

        Preview 9 release content
      
```
Author:
```
leecow
```
Text:
```


No description provided.


```

## 3183
Title:
```

        minor update to the roadmap
      
```
Author:
```
mairaw
```
Text:
```

Saw questions around this on gitter. Thought I'd make that info more clear.

```

