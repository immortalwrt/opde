---
title: "compile.7"
date: 2021-07-03 03:48:04.793684
hidden: false
draft: false
weight: -7
---

build number: `7`

#### re-implement command 

```bash
docker pull immortalwrt/opde:sdk
docker run -it --rm immortalwrt/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/telephony/freeswitch-mod-bcg729/compile -j$(nproc) || make package/feeds/telephony/freeswitch-mod-bcg729/compile V=s
```

#### Compile.txt

``` bash
mod_bcg729.c:30:10: fatal error: switch.h: No such file or directory
 #include "switch.h"
          ^~~~~~~~~~
compilation terminated.
make[3]: *** [Makefile:82: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/freeswitch-mod-bcg729-2017-06-29-686eb06d/.built] Error 1
```
