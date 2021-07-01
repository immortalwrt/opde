---
title: "compile.5"
date: 2021-07-01 17:06:21.009249
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
make package/feeds/packages/php7-pecl-libevent/compile -j$(nproc) || make package/feeds/packages/php7-pecl-libevent/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-libevent2.patch using plaintext: 
patching file libevent.c
bash: /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:46: /openwrt/build_dir/target-mips_24kc_musl/pecl-php7/libevent-ce255e7e1e293030951fd68d5df06b2a4c077a89/.prepared_bb3ccb80c5dfd63a04150c40730c4cb3_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```
