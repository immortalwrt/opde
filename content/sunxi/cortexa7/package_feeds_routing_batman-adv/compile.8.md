---
title: "compile.8"
date: 2021-07-03 14:42:24.932715
hidden: false
draft: false
weight: -8
---

build number: `8`

#### re-implement command 

```bash
docker pull immortalwrt/opde:sdk
docker run -it --rm immortalwrt/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/routing/batman-adv/compile -j$(nproc) || make package/feeds/routing/batman-adv/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-Revert-batman-adv-genetlink-move-to-smaller-ops-wher.patch using plaintext: 
patching file compat-include/net/genetlink.h
patching file net/batman-adv/netlink.c

Applying ./patches/0002-Revert-batman-adv-Add-new-include-for-min-max-helper.patch using plaintext: 
patching file compat-include/linux/minmax.h
patching file net/batman-adv/bat_v.c
patching file net/batman-adv/bat_v_elp.c
patching file net/batman-adv/bat_v_ogm.c
patching file net/batman-adv/fragmentation.c
patching file net/batman-adv/hard-interface.c
patching file net/batman-adv/main.c
patching file net/batman-adv/netlink.c
patching file net/batman-adv/tp_meter.c

Applying ./patches/0003-batman-adv-Fix-build-of-multicast-code-against-Linux.patch using plaintext: 
patching file net/batman-adv/multicast.c

Applying ./patches/0004-batman-adv-Always-send-iface-index-name-in-genlmsg.patch using plaintext: 
patching file net/batman-adv/bat_iv_ogm.c
patching file net/batman-adv/bat_v.c
patching file net/batman-adv/netlink.c
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/linux-5.4.128'
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/bat_algo.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/bat_iv_ogm.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/bat_v.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/bat_v_elp.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/bat_v_ogm.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/bitarray.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/bridge_loop_avoidance.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/distributed-arp-table.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/fragmentation.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/gateway_client.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/gateway_common.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/hard-interface.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/hash.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/main.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/multicast.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/netlink.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/originator.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/routing.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/send.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/soft-interface.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/tp_meter.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/translation-table.o
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/tvlv.o
  LD [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/batman-adv.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/batman-adv.mod.o
  LD [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/batman-adv-2021.1/net/batman-adv/batman-adv.ko
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/linux-5.4.128'
Package kmod-batman-adv is missing dependencies for the following libraries:
libcrc32c.ko
make[3]: *** [Makefile:99: /openwrt/bin/targets/sunxi/cortexa7/packages/kmod-batman-adv_5.4.128+2021.1-1_arm_cortex-a7_neon-vfpv4.ipk] Error 1
```
