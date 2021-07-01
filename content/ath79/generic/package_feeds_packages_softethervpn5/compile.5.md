---
title: "compile.5"
date: 2021-07-01 16:48:03.259440
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
make package/feeds/packages/softethervpn5/compile -j$(nproc) || make package/feeds/packages/softethervpn5/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-iconv-cmake-fix.patch using plaintext: 
patching file src/Mayaqua/CMakeLists.txt

Applying ./patches/002-pthread-include-fix.patch using plaintext: 
patching file src/Mayaqua/Encrypt.h

Applying ./patches/100-increase-cfg-save-intervall.patch using plaintext: 
patching file src/Cedar/Server.h

Applying ./patches/101-add-config-write-syslog.patch using plaintext: 
patching file src/Cedar/Server.c
-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Looking for sys/auxv.h
-- Looking for sys/auxv.h - found
-- Build date: 30/06/2021
-- Build time: 13:29:01
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Checking for one of the modules 'libsodium'
-- Looking for cbreak in /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libncurses.so
-- Looking for cbreak in /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libncurses.so - found
-- Looking for nodelay in /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libncurses.so
-- Looking for nodelay in /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libncurses.so - found
-- Found Curses: /openwrt/staging_dir/target-mips_24kc_musl/usr/lib/libncurses.so  
CMake Error at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindOpenSSL.cmake:570 (find_package_handle_standard_args)
  src/Mayaqua/CMakeLists.txt:19 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/SoftEtherVPN-5.02.5180/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:178: /openwrt/build_dir/target-mips_24kc_musl/SoftEtherVPN-5.02.5180/.configured_a17fb5ef857664f03cd0ce37cc5ea591] Error 1
```
