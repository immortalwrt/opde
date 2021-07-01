---
title: "compile.5"
date: 2021-07-01 16:51:03.316658
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
make package/feeds/packages/php7-pecl-mcrypt/compile -j$(nproc) || make package/feeds/packages/php7-pecl-mcrypt/compile V=s
```

#### Compile.txt

``` bash
bash: /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:44: /openwrt/build_dir/target-mips_24kc_musl/pecl-php7/mcrypt-1.0.4/.prepared_286edd61e1d624ca54c941c828b0d976_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```
