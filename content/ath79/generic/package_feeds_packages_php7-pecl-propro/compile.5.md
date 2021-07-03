---
title: "compile.5"
date: 2021-07-01 17:06:21.012162
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
make package/feeds/packages/php7-pecl-propro/compile -j$(nproc) || make package/feeds/packages/php7-pecl-propro/compile V=s
```

#### Compile.txt

``` bash
bash: /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:50: /openwrt/build_dir/target-mips_24kc_musl/pecl-php7/propro-2.1.0/.prepared_66b579b3c0dfde10e1fb99dd0aafbb7c_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```