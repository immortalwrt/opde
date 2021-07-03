---
title: "compile.7"
date: 2021-07-03 03:49:34.034204
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
make package/feeds/base/fast-classifier/compile -j$(nproc) || make package/feeds/base/fast-classifier/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/linux-5.4.128'
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.o
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.c: In function 'fast_classifier_init':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.c:1888:1: warning: label 'exit4' defined but not used [-Wunused-label]
 exit4:
 ^~~~~
  Building modules, stage 2.
  MODPOST 1 modules
ERROR: "sfe_ipv6_register_sync_rule_callback" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_register_sync_rule_callback" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "athrs_fast_nat_recv" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_update_rule" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_create_rule" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_update_rule" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_create_rule" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "nf_ct_tcp_no_window_check" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_mark_rule" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_destroy_rule" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_mark_rule" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_destroy_rule" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_recv" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_recv" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv4_destroy_all_rules_for_dev" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
ERROR: "sfe_ipv6_destroy_all_rules_for_dev" [/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/fast-classifier.ko] undefined!
make[5]: *** [scripts/Makefile.modpost:94: __modpost] Error 1
make[4]: *** [Makefile:1647: modules] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/linux-5.4.128'
make[3]: *** [Makefile:72: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/fast-classifier/.built] Error 2
```