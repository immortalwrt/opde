---
title: "compile.5"
date: 2021-07-01 16:59:19.838222
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
make package/feeds/packages/domoticz/compile -j$(nproc) || make package/feeds/packages/domoticz/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/012-minizip-overflow.patch using plaintext: 
patching file main/unzip_stream.h
-- The C compiler identification is GNU 8.4.0
-- The CXX compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - failed
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - broken
CMake Error at /openwrt/staging_dir/host/share/cmake-3.20/Modules/CMakeTestCCompiler.cmake:66 (message):
  The C compiler

    "/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc"

  is not able to compile a simple test program.

  It fails with the following output:

    Change Dir: /openwrt/build_dir/target-mips_24kc_musl/domoticz-2021.1/CMakeFiles/CMakeTmp
    
    Run Build Command(s):/openwrt/staging_dir/host/bin/ninja cmTC_13e1a && [1/2] Building C object CMakeFiles/cmTC_13e1a.dir/testCCompiler.c.o
    [2/2] Linking C executable cmTC_13e1a
    FAILED: cmTC_13e1a 
    : && /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/domoticz-2021.1=domoticz-2021.1 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -flto -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/lib -L/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib -znow -zrelro -lpython3.9 CMakeFiles/cmTC_13e1a.dir/testCCompiler.c.o -o cmTC_13e1a   && :
    /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/lib/gcc/mips-openwrt-linux-musl/8.4.0/../../../../mips-openwrt-linux-musl/bin/ld: cannot find -lpython3.9
    collect2: error: ld returned 1 exit status
    ninja: build stopped: subcommand failed.
    
    

  

  CMake will not be able to correctly generate this project.
Call Stack (most recent call first):
  CMakeLists.txt:4 (project)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/domoticz-2021.1/CMakeFiles/CMakeOutput.log".
See also "/openwrt/build_dir/target-mips_24kc_musl/domoticz-2021.1/CMakeFiles/CMakeError.log".
make[3]: *** [Makefile:134: /openwrt/build_dir/target-mips_24kc_musl/domoticz-2021.1/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
