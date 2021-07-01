---
title: "compile.5"
date: 2021-07-01 16:56:50.176668
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
make package/feeds/base/r8152/compile -j$(nproc) || make package/feeds/base/r8152/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/100-add-LED-configuration-from-OF.patch using plaintext: 
patching file r8152.c
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/realtek-r8152-linux-2.15'
/openwrt/staging_dir/host/bin/find: '/openwrt/kernel/drivers/net/usb_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.128': No such file or directory
/bin/sh: 1: lsmod: not found
make -C /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.128 M=/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/realtek-r8152-linux-2.15 modules
make[5]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.128'
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/realtek-r8152-linux-2.15/r8152.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/realtek-r8152-linux-2.15/r8152.mod.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/realtek-r8152-linux-2.15/r8152.ko
make[5]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.128'
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/realtek-r8152-linux-2.15'
Package kmod-usb-net-rtl8152-vendor is missing dependencies for the following libraries:
usbcore.ko
make[3]: *** [Makefile:66: /openwrt/bin/targets/ath79/generic/packages/kmod-usb-net-rtl8152-vendor_5.4.128+2.15-ath79-1_mips_24kc.ipk] Error 1
```
