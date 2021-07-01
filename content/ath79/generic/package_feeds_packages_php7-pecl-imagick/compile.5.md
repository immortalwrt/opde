---
title: "compile.5"
date: 2021-07-01 16:43:54.122254
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
make package/feeds/packages/php7-pecl-imagick/compile -j$(nproc) || make package/feeds/packages/php7-pecl-imagick/compile V=s
```

#### Compile.txt

``` bash
bash: /openwrt/staging_dir/target-mips_24kc_musl/usr/bin/phpize7: No such file or directory
make[3]: *** [Makefile:44: /openwrt/build_dir/target-mips_24kc_musl/pecl-php7/imagick-3.4.4/.prepared_2ae62090abdc85a5eace7c6b72b562de_18f1e190c5d53547fed41a3eaa76e9e9] Error 127
```
