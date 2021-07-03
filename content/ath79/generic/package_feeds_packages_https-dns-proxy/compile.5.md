---
title: "compile.5"
date: 2021-07-01 16:58:20.157231
hidden: false
draft: false
weight: -5
---

build number: `5`

#### re-implement command 

```bash
docker pull immortalwrt/opde:sdk
docker run -it --rm immortalwrt/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/https-dns-proxy/compile -j$(nproc) || make package/feeds/packages/https-dns-proxy/compile V=s
```

#### Compile.txt

``` bash
-- The C compiler identification is GNU 8.4.0
-- The CXX compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Deprecation Warning at CMakeLists.txt:2 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Found Git: /openwrt/staging_dir/host/bin/git (found version "2.25.1") 
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
-- Version: 
-- clang-tidy not found.
-- Configuring done
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
LIBCURL_INCLUDE_DIR
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/https-dns-proxy-2021-06-03
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/https-dns-proxy-2021-06-03
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/https-dns-proxy-2021-06-03
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/https-dns-proxy-2021-06-03
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/https-dns-proxy-2021-06-03
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/https-dns-proxy-2021-06-03
   used as include directory in directory /openwrt/build_dir/target-mips_24kc_musl/https-dns-proxy-2021-06-03

CMake Warning (dev) in CMakeLists.txt:
  Policy CMP0021 is not set: Fatal error on relative paths in
  INCLUDE_DIRECTORIES target property.  Run "cmake --help-policy CMP0021" for
  policy details.  Use the cmake_policy command to set the policy and
  suppress this warning.

  Found relative path while evaluating include directories of
  "https_dns_proxy":

    "LIBCURL_INCLUDE_DIR-NOTFOUND"

This warning is for project developers.  Use -Wno-dev to suppress it.

-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_ASM_COMPILER
    CMAKE_ASM_COMPILER_LAUNCHER
    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_EXPORT_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
    CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY
    CMAKE_FIND_ROOT_PATH_MODE_LIBRARY
    CMAKE_MODULE_LINKER_FLAGS
    CMAKE_SHARED_LINKER_FLAGS
    DL_LIBRARY


CMake Generate step failed.  Build files cannot be regenerated correctly.
make[3]: *** [Makefile:53: /openwrt/build_dir/target-mips_24kc_musl/https-dns-proxy-2021-06-03/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```