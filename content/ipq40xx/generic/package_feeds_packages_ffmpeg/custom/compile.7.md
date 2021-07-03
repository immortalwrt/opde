---
title: "compile.7"
date: 2021-07-03 03:51:48.015650
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
make package/feeds/packages/ffmpeg/compile -j$(nproc) || make package/feeds/packages/ffmpeg/compile V=s
```

#### Compile.txt

``` bash
cp: cannot stat '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/ffmpeg-custom/ffmpeg-4.3.2/ipkg-install/usr/bin/ffmpeg': No such file or directory
make[3]: *** [Makefile:755: /openwrt/bin/packages/arm_cortex-a7_neon-vfpv4/packages/ffmpeg-custom_4.3.2-1_arm_cortex-a7_neon-vfpv4.ipk] Error 1
```
