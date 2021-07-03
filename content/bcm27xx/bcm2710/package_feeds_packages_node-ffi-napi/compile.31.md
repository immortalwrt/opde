---
title: "compile.31"
date: 2021-06-10 17:05:06.975338
hidden: false
draft: false
weight: -31
---

build number: `31`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/node-ffi-napi/compile -j$(nproc) || make package/feeds/packages/node-ffi-napi/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/0001-do_not_build_libffi.patch using plaintext: 
patching file binding.gyp

Applying ./patches/0002-support_mips.patch using plaintext: 
patching file src/ffi.cc
npm info it worked if it ends with ok
npm info using npm@6.14.13
npm info using node@v14.17.0
npm info lifecycle ffi-napi@4.0.3~preinstall: ffi-napi@4.0.3
npm timing stage:loadCurrentTree Completed in 12ms
npm timing stage:loadIdealTree:cloneCurrentTree Completed in 0ms
npm timing stage:loadIdealTree:loadShrinkwrap Completed in 1ms
npm http fetch GET 200 https://registry.npmjs.org/nyc 239ms
npm http fetch GET 200 https://registry.npmjs.org/fs-extra 246ms
npm http fetch GET 200 https://registry.npmjs.org/prebuildify 247ms
npm http fetch GET 200 https://registry.npmjs.org/get-uv-event-loop-napi-h 240ms
npm http fetch GET 200 https://registry.npmjs.org/node-addon-api 240ms
npm http fetch GET 200 https://registry.npmjs.org/node-gyp-build 240ms
npm http fetch GET 200 https://registry.npmjs.org/debug 243ms
npm http fetch GET 200 https://registry.npmjs.org/mocha 257ms
npm http fetch GET 200 https://registry.npmjs.org/nyc/-/nyc-15.1.0.tgz 137ms
npm http fetch GET 200 https://registry.npmjs.org/fs-extra/-/fs-extra-9.1.0.tgz 139ms
npm http fetch GET 200 https://registry.npmjs.org/prebuildify/-/prebuildify-4.1.2.tgz 130ms
npm http fetch GET 200 https://registry.npmjs.org/node-addon-api/-/node-addon-api-3.2.1.tgz 117ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-4.3.1.tgz 115ms
npm http fetch GET 200 https://registry.npmjs.org/get-uv-event-loop-napi-h/-/get-uv-event-loop-napi-h-1.0.6.tgz 119ms
npm http fetch GET 200 https://registry.npmjs.org/node-gyp-build/-/node-gyp-build-4.2.3.tgz 119ms
npm http fetch GET 200 https://registry.npmjs.org/mocha/-/mocha-7.2.0.tgz 117ms
npm http fetch GET 200 https://registry.npmjs.org/at-least-node 35ms
npm http fetch GET 200 https://registry.npmjs.org/ref-napi 51ms
npm http fetch GET 200 https://registry.npmjs.org/jsonfile 48ms
npm http fetch GET 200 https://registry.npmjs.org/graceful-fs 51ms
npm http fetch GET 200 https://registry.npmjs.org/ref-struct-di 54ms
npm http fetch GET 200 https://registry.npmjs.org/execspawn 48ms
npm http fetch GET 200 https://registry.npmjs.org/universalify 60ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp-classic 54ms
npm http fetch GET 200 https://registry.npmjs.org/ref-struct-di/-/ref-struct-di-1.1.1.tgz 83ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp-classic/-/mkdirp-classic-0.5.3.tgz 75ms
npm http fetch GET 200 https://registry.npmjs.org/ref-napi/-/ref-napi-3.0.3.tgz 94ms
npm http fetch GET 200 https://registry.npmjs.org/jsonfile/-/jsonfile-6.1.0.tgz 90ms
npm http fetch GET 200 https://registry.npmjs.org/at-least-node/-/at-least-node-1.0.0.tgz 104ms
npm http fetch GET 200 https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.6.tgz 90ms
npm http fetch GET 200 https://registry.npmjs.org/universalify/-/universalify-2.0.0.tgz 82ms
npm http fetch GET 200 https://registry.npmjs.org/execspawn/-/execspawn-1.0.1.tgz 87ms
npm http fetch GET 200 https://registry.npmjs.org/ref-array-di 581ms
npm http fetch GET 200 https://registry.npmjs.org/npm-run-path 36ms
npm http fetch GET 200 https://registry.npmjs.org/node-abi 37ms
npm http fetch GET 200 https://registry.npmjs.org/prebuildify-ci 600ms
npm http fetch GET 200 https://registry.npmjs.org/minimist 45ms
npm http fetch GET 200 https://registry.npmjs.org/tar-fs 82ms
npm http fetch GET 200 https://registry.npmjs.org/get-symbol-from-current-process-h 83ms
npm http fetch GET 200 https://registry.npmjs.org/ref-array-di/-/ref-array-di-1.2.2.tgz 73ms
npm http fetch GET 200 https://registry.npmjs.org/pump 88ms
npm http fetch GET 200 https://registry.npmjs.org/ms 89ms
npm http fetch GET 200 https://registry.npmjs.org/prebuildify-ci/-/prebuildify-ci-1.0.5.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/npm-run-path/-/npm-run-path-3.1.0.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/node-abi/-/node-abi-2.30.0.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/@istanbuljs%2fload-nyc-config 90ms
npm http fetch GET 200 https://registry.npmjs.org/minimist/-/minimist-1.2.5.tgz 75ms
npm http fetch GET 200 https://registry.npmjs.org/tar-fs/-/tar-fs-2.1.1.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/pump/-/pump-3.0.0.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/get-symbol-from-current-process-h/-/get-symbol-from-current-process-h-1.0.2.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.1.2.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/caching-transform 42ms
npm http fetch GET 200 https://registry.npmjs.org/convert-source-map 47ms
npm http fetch GET 200 https://registry.npmjs.org/decamelize 54ms
npm http fetch GET 200 https://registry.npmjs.org/find-cache-dir 43ms
npm http fetch GET 200 https://registry.npmjs.org/@istanbuljs/load-nyc-config/-/load-nyc-config-1.1.0.tgz 83ms
npm http fetch GET 200 https://registry.npmjs.org/find-up 55ms
npm http fetch GET 200 https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.7.0.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/foreground-child 40ms
npm http fetch GET 200 https://registry.npmjs.org/get-package-type 40ms
npm http fetch GET 200 https://registry.npmjs.org/@istanbuljs%2fschema 104ms
npm http fetch GET 200 https://registry.npmjs.org/find-cache-dir/-/find-cache-dir-3.3.1.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/caching-transform/-/caching-transform-4.0.0.tgz 70ms
npm http fetch GET 200 https://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-coverage 35ms
npm http fetch GET 200 https://registry.npmjs.org/glob 71ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-hook 46ms
npm http fetch GET 200 https://registry.npmjs.org/find-up/-/find-up-4.1.0.tgz 73ms
npm http fetch GET 200 https://registry.npmjs.org/get-package-type/-/get-package-type-0.1.0.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/foreground-child/-/foreground-child-2.0.0.tgz 71ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-coverage/-/istanbul-lib-coverage-3.0.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/@istanbuljs/schema/-/schema-0.1.3.tgz 67ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-instrument 58ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-hook/-/istanbul-lib-hook-3.0.0.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/glob/-/glob-7.1.7.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-report 48ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-processinfo 56ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-instrument/-/istanbul-lib-instrument-4.0.3.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-source-maps 39ms
npm http fetch GET 200 https://registry.npmjs.org/p-map 37ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-reports 55ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-processinfo/-/istanbul-lib-processinfo-2.0.2.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/node-preload 51ms
npm http fetch GET 200 https://registry.npmjs.org/make-dir 53ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-report/-/istanbul-lib-report-3.0.0.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/rimraf 40ms
npm http fetch GET 200 https://registry.npmjs.org/resolve-from 54ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-lib-source-maps/-/istanbul-lib-source-maps-4.0.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/p-map/-/p-map-3.0.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/make-dir/-/make-dir-3.1.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/node-preload/-/node-preload-0.2.1.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/process-on-spawn 90ms
npm http fetch GET 200 https://registry.npmjs.org/rimraf/-/rimraf-3.0.2.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/resolve-from/-/resolve-from-5.0.0.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/spawn-wrap 50ms
npm http fetch GET 200 https://registry.npmjs.org/signal-exit 56ms
npm http fetch GET 200 https://registry.npmjs.org/yargs 48ms
npm http fetch GET 200 https://registry.npmjs.org/test-exclude 59ms
npm http fetch GET 200 https://registry.npmjs.org/istanbul-reports/-/istanbul-reports-3.0.2.tgz 88ms
npm http fetch GET 200 https://registry.npmjs.org/process-on-spawn/-/process-on-spawn-1.0.0.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/browser-stdout 34ms
npm http fetch GET 200 https://registry.npmjs.org/yargs/-/yargs-15.4.1.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-colors 73ms
npm http fetch GET 200 https://registry.npmjs.org/chokidar 48ms
npm http fetch GET 200 https://registry.npmjs.org/spawn-wrap/-/spawn-wrap-2.0.0.tgz 71ms
npm http fetch GET 200 https://registry.npmjs.org/test-exclude/-/test-exclude-6.0.0.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-3.2.6.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/diff 51ms
npm http fetch GET 200 https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.3.tgz 79ms
npm http fetch GET 200 https://registry.npmjs.org/escape-string-regexp 43ms
npm http fetch GET 200 https://registry.npmjs.org/browser-stdout/-/browser-stdout-1.3.1.tgz 65ms
npm WARN deprecated debug@3.2.6: Debug versions >=3.2.0 <3.2.7 || >=4 <4.3.1 have a low-severity ReDos regression when used in a Node.js environment. It is recommended you upgrade to 3.2.7 or 4.3.1. (https://github.com/visionmedia/debug/issues/797)
npm http fetch GET 200 https://registry.npmjs.org/chokidar/-/chokidar-3.3.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/diff/-/diff-3.5.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-colors/-/ansi-colors-3.2.3.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/find-up/-/find-up-3.0.0.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/growl 52ms
npm http fetch GET 200 https://registry.npmjs.org/he 49ms
npm http fetch GET 200 https://registry.npmjs.org/glob/-/glob-7.1.3.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/js-yaml 46ms
npm http fetch GET 200 https://registry.npmjs.org/log-symbols 42ms
npm http fetch GET 200 https://registry.npmjs.org/minimatch 36ms
npm http fetch GET 200 https://registry.npmjs.org/he/-/he-1.2.0.tgz 72ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.1.1.tgz 88ms
npm http fetch GET 200 https://registry.npmjs.org/node-environment-flags 80ms
npm http fetch GET 200 https://registry.npmjs.org/growl/-/growl-1.10.5.tgz 81ms
npm http fetch GET 200 https://registry.npmjs.org/log-symbols/-/log-symbols-3.0.0.tgz 72ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp 95ms
npm http fetch GET 200 https://registry.npmjs.org/js-yaml/-/js-yaml-3.13.1.tgz 77ms
npm http fetch GET 200 https://registry.npmjs.org/object.assign 82ms
npm http fetch GET 200 https://registry.npmjs.org/strip-json-comments 74ms
npm http fetch GET 200 https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz 91ms
npm http fetch GET 200 https://registry.npmjs.org/node-environment-flags/-/node-environment-flags-1.0.6.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.5.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/object.assign/-/object.assign-4.1.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/which 44ms
npm http fetch GET 200 https://registry.npmjs.org/supports-color 45ms
npm http fetch GET 200 https://registry.npmjs.org/yargs-parser 45ms
npm http fetch GET 200 https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/yargs/-/yargs-13.3.2.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/yargs-unparser 43ms
npm http fetch GET 200 https://registry.npmjs.org/wide-align 53ms
npm http fetch GET 200 https://registry.npmjs.org/which/-/which-1.3.1.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-3.2.7.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/supports-color/-/supports-color-6.0.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/util-extend 40ms
npm http fetch GET 200 https://registry.npmjs.org/wide-align/-/wide-align-1.1.3.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/yargs-parser/-/yargs-parser-13.1.2.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/yargs-unparser/-/yargs-unparser-1.6.0.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/ghreleases 44ms
npm http fetch GET 200 https://registry.npmjs.org/gunzip-maybe 49ms
npm http fetch GET 200 https://registry.npmjs.org/util-extend/-/util-extend-1.0.3.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/request 39ms
npm http fetch GET 200 https://registry.npmjs.org/array-index 78ms
npm http fetch GET 200 https://registry.npmjs.org/ghreleases/-/ghreleases-2.0.2.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/unzipper 42ms
npm http fetch GET 200 https://registry.npmjs.org/gunzip-maybe/-/gunzip-maybe-1.4.2.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/semver 40ms
npm http fetch GET 200 https://registry.npmjs.org/tar-fs/-/tar-fs-1.16.3.tgz 61ms
npm http fetch GET 200 https://registry.npmjs.org/path-key 58ms
npm http fetch GET 200 https://registry.npmjs.org/request/-/request-2.88.2.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/array-index/-/array-index-1.0.0.tgz 40ms
npm WARN deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
npm http fetch GET 200 https://registry.npmjs.org/unzipper/-/unzipper-0.9.15.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/tar-stream 27ms
npm http fetch GET 200 https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/chownr 60ms
npm http fetch GET 200 https://registry.npmjs.org/semver/-/semver-5.7.1.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/js-yaml/-/js-yaml-3.14.1.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/end-of-stream 47ms
npm http fetch GET 200 https://registry.npmjs.org/camelcase 40ms
npm http fetch GET 200 https://registry.npmjs.org/once 46ms
npm http fetch GET 200 https://registry.npmjs.org/chownr/-/chownr-1.1.4.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer 44ms
npm http fetch GET 200 https://registry.npmjs.org/tar-stream/-/tar-stream-2.2.0.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/camelcase/-/camelcase-5.3.1.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/commondir 46ms
npm http fetch GET 200 https://registry.npmjs.org/once/-/once-1.4.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.4.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/hasha 42ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/commondir/-/commondir-1.0.1.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/pkg-dir 73ms
npm http fetch GET 200 https://registry.npmjs.org/package-hash 37ms
npm http fetch GET 200 https://registry.npmjs.org/write-file-atomic 36ms
npm http fetch GET 200 https://registry.npmjs.org/hasha/-/hasha-5.2.2.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/path-exists 28ms
npm http fetch GET 200 https://registry.npmjs.org/locate-path 33ms
npm http fetch GET 200 https://registry.npmjs.org/pkg-dir/-/pkg-dir-4.2.0.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/package-hash/-/package-hash-4.0.0.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/cross-spawn 38ms
npm http fetch GET 200 https://registry.npmjs.org/fs.realpath 28ms
npm http fetch GET 200 https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz 12ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/locate-path/-/locate-path-5.0.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/inflight 37ms
npm http fetch GET 200 https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.3.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/write-file-atomic/-/write-file-atomic-3.0.3.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/inherits 39ms
npm http fetch GET 200 https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/append-transform 77ms
npm http fetch GET 200 https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/path-is-absolute 30ms
npm http fetch GET 200 https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/uuid 36ms
npm http fetch GET 200 https://registry.npmjs.org/supports-color/-/supports-color-7.2.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/semver/-/semver-6.3.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/append-transform/-/append-transform-2.0.0.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/archy 46ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fcore 49ms
npm http fetch GET 200 https://registry.npmjs.org/source-map 43ms
npm http fetch GET 200 https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/aggregate-error 45ms
npm http fetch GET 200 https://registry.npmjs.org/uuid/-/uuid-3.4.0.tgz 30ms
npm WARN deprecated uuid@3.4.0: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
npm http fetch GET 200 https://registry.npmjs.org/archy/-/archy-1.0.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/require-directory 41ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/core/-/core-7.14.5.tgz 70ms
npm http fetch GET 200 https://registry.npmjs.org/aggregate-error/-/aggregate-error-3.1.0.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/html-escaper 58ms
npm http fetch GET 200 https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/require-main-filename 40ms
npm http fetch GET 200 https://registry.npmjs.org/fromentries 57ms
npm http fetch GET 200 https://registry.npmjs.org/get-caller-file 48ms
npm http fetch GET 200 https://registry.npmjs.org/cliui 62ms
npm http fetch GET 200 https://registry.npmjs.org/html-escaper/-/html-escaper-2.0.2.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/package-repo 465ms
npm http fetch GET 200 https://registry.npmjs.org/require-main-filename/-/require-main-filename-2.0.0.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/set-blocking 43ms
npm http fetch GET 200 https://registry.npmjs.org/fromentries/-/fromentries-1.3.2.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/cliui/-/cliui-6.0.0.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/string-width 43ms
npm http fetch GET 200 https://registry.npmjs.org/which-module 45ms
npm http fetch GET 200 https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz 61ms
npm http fetch GET 200 https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/string-width/-/string-width-4.2.2.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/which-module/-/which-module-2.0.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/is-windows 33ms
npm http fetch GET 200 https://registry.npmjs.org/yargs-parser/-/yargs-parser-18.1.3.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/which/-/which-2.0.2.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/y18n 53ms
npm http fetch GET 200 https://registry.npmjs.org/anymatch 43ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.1.3.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/braces 31ms
npm http fetch GET 200 https://registry.npmjs.org/is-windows/-/is-windows-1.0.2.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/is-binary-path 27ms
npm http fetch GET 200 https://registry.npmjs.org/y18n/-/y18n-4.0.3.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/is-glob 39ms
npm http fetch GET 200 https://registry.npmjs.org/anymatch/-/anymatch-3.1.2.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/glob-parent 51ms
npm http fetch GET 200 https://registry.npmjs.org/normalize-path 40ms
npm http fetch GET 200 https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/braces/-/braces-3.0.2.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/fsevents 46ms
npm http fetch GET 200 https://registry.npmjs.org/readdirp 53ms
npm http fetch GET 200 https://registry.npmjs.org/is-glob/-/is-glob-4.0.1.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/argparse 47ms
npm http fetch GET 200 https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/locate-path/-/locate-path-3.0.0.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/fsevents/-/fsevents-2.1.3.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/esprima 39ms
npm http fetch GET 200 https://registry.npmjs.org/readdirp/-/readdirp-3.2.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/chalk 41ms
npm WARN deprecated fsevents@2.1.3: "Please update to latest v2.3 or v2.2"
npm http fetch GET 200 https://registry.npmjs.org/argparse/-/argparse-1.0.10.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/brace-expansion 53ms
npm http fetch GET 200 https://registry.npmjs.org/define-properties 22ms
npm http fetch GET 200 https://registry.npmjs.org/object.getownpropertydescriptors 31ms
npm http fetch GET 200 https://registry.npmjs.org/function-bind 27ms
npm http fetch GET 200 https://registry.npmjs.org/has-symbols 28ms
npm http fetch GET 200 https://registry.npmjs.org/object-keys 38ms
npm http fetch GET 200 https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/esprima/-/esprima-4.0.1.tgz 62ms
npm http fetch GET 200 https://registry.npmjs.org/cliui/-/cliui-5.0.0.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/define-properties/-/define-properties-1.1.3.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/object.getownpropertydescriptors/-/object.getownpropertydescriptors-2.1.2.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/find-up/-/find-up-3.0.0.tgz 14ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/yargs-parser/-/yargs-parser-13.1.2.tgz 13ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/isexe 39ms
npm http fetch GET 200 https://registry.npmjs.org/yargs/-/yargs-13.3.2.tgz 7ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/has-symbols/-/has-symbols-1.0.2.tgz 80ms
npm http fetch GET 200 https://registry.npmjs.org/string-width/-/string-width-2.1.1.tgz 29ms
npm http fetch GET 200 https://registry.npmjs.org/flat 34ms
npm http fetch GET 200 https://registry.npmjs.org/has-flag 44ms
npm http fetch GET 200 https://registry.npmjs.org/string-width/-/string-width-3.1.0.tgz 69ms
npm http fetch GET 200 https://registry.npmjs.org/lodash 45ms
npm http fetch GET 200 https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/after 30ms
npm http fetch GET 200 https://registry.npmjs.org/ghrepos 45ms
npm http fetch GET 200 https://registry.npmjs.org/flat/-/flat-4.1.1.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.uniq 104ms
npm http fetch GET 200 https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz 95ms
npm http fetch GET 200 https://registry.npmjs.org/url-template 95ms
npm http fetch GET 200 https://registry.npmjs.org/ghutils 121ms
npm http fetch GET 200 https://registry.npmjs.org/after/-/after-0.8.2.tgz 100ms
npm http fetch GET 200 https://registry.npmjs.org/package-repo/-/package-repo-1.0.0.tgz 446ms
npm http fetch GET 200 https://registry.npmjs.org/ghrepos/-/ghrepos-2.1.0.tgz 113ms
npm http fetch GET 200 https://registry.npmjs.org/browserify-zlib 40ms
npm http fetch GET 200 https://registry.npmjs.org/xtend 44ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.uniq/-/lodash.uniq-4.5.0.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/ghutils/-/ghutils-3.2.6.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/url-template/-/url-template-2.0.8.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/is-gzip 39ms
npm http fetch GET 200 https://registry.npmjs.org/is-deflate 43ms
npm http fetch GET 200 https://registry.npmjs.org/peek-stream 51ms
npm http fetch GET 200 https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.5.tgz 4ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/xtend/-/xtend-4.0.2.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/through2 37ms
npm http fetch GET 200 https://registry.npmjs.org/peek-stream/-/peek-stream-1.1.3.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/is-deflate/-/is-deflate-1.0.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/pumpify 42ms
npm http fetch GET 200 https://registry.npmjs.org/browserify-zlib/-/browserify-zlib-0.1.4.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/is-gzip/-/is-gzip-1.0.0.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/pump/-/pump-1.0.3.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/tar-stream/-/tar-stream-1.6.2.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/aws-sign2 25ms
npm http fetch GET 200 https://registry.npmjs.org/caseless 30ms
npm http fetch GET 200 https://registry.npmjs.org/aws4 32ms
npm http fetch GET 200 https://registry.npmjs.org/extend 29ms
npm http fetch GET 200 https://registry.npmjs.org/forever-agent 30ms
npm http fetch GET 200 https://registry.npmjs.org/pumpify/-/pumpify-1.5.1.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/combined-stream 43ms
npm http fetch GET 200 https://registry.npmjs.org/form-data 39ms
npm http fetch GET 200 https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz 26ms
npm http fetch GET 200 https://registry.npmjs.org/aws4/-/aws4-1.11.0.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz 54ms
npm http fetch GET 200 https://registry.npmjs.org/through2/-/through2-2.0.5.tgz 95ms
npm http fetch GET 200 https://registry.npmjs.org/extend/-/extend-3.0.2.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/har-validator 37ms
npm http fetch GET 200 https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/http-signature 28ms
npm http fetch GET 200 https://registry.npmjs.org/is-typedarray 19ms
npm http fetch GET 200 https://registry.npmjs.org/har-validator/-/har-validator-5.1.5.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/isstream 25ms
npm WARN deprecated har-validator@5.1.5: this library is no longer supported
npm http fetch GET 200 https://registry.npmjs.org/oauth-sign 36ms
npm http fetch GET 200 https://registry.npmjs.org/performance-now 35ms
npm http fetch GET 200 https://registry.npmjs.org/json-stringify-safe 46ms
npm http fetch GET 200 https://registry.npmjs.org/qs 43ms
npm http fetch GET 200 https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/mime-types 57ms
npm http fetch GET 200 https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/simple-mime 399ms
npm http fetch GET 200 https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz 61ms
npm http fetch GET 200 https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz 69ms
npm http fetch GET 200 https://registry.npmjs.org/mime-types/-/mime-types-2.1.31.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/tough-cookie 56ms
npm http fetch GET 200 https://registry.npmjs.org/qs/-/qs-6.5.2.tgz 72ms
npm http fetch GET 200 https://registry.npmjs.org/tunnel-agent 50ms
npm http fetch GET 200 https://registry.npmjs.org/es6-symbol 23ms
npm http fetch GET 200 https://registry.npmjs.org/big-integer 27ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-indexof-polyfill 23ms
npm http fetch GET 200 https://registry.npmjs.org/debug/-/debug-2.6.9.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/binary 45ms
npm http fetch GET 200 https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.5.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/bluebird 48ms
npm http fetch GET 200 https://registry.npmjs.org/duplexer2 43ms
npm http fetch GET 200 https://registry.npmjs.org/simple-mime/-/simple-mime-0.1.0.tgz 76ms
npm http fetch GET 200 https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/big-integer/-/big-integer-1.6.48.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/es6-symbol/-/es6-symbol-3.1.3.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-indexof-polyfill/-/buffer-indexof-polyfill-1.0.2.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/binary/-/binary-0.3.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/fstream 29ms
npm http fetch GET 200 https://registry.npmjs.org/duplexer2/-/duplexer2-0.1.4.tgz 62ms
npm http fetch GET 200 https://registry.npmjs.org/listenercount 52ms
npm http fetch GET 200 https://registry.npmjs.org/fs-constants 37ms
npm http fetch GET 200 https://registry.npmjs.org/setimmediate 45ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream 36ms
npm http fetch GET 200 https://registry.npmjs.org/bluebird/-/bluebird-3.4.7.tgz 73ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream 58ms
npm http fetch GET 200 https://registry.npmjs.org/bl 54ms
npm http fetch GET 200 https://registry.npmjs.org/fstream/-/fstream-1.0.12.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/wrappy 57ms
npm http fetch GET 200 https://registry.npmjs.org/listenercount/-/listenercount-1.0.1.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.0.tgz 37ms
npm http fetch GET 200 https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.7.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/is-stream 40ms
npm http fetch GET 200 https://registry.npmjs.org/bl/-/bl-4.1.0.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/fs-constants/-/fs-constants-1.0.0.tgz 75ms
npm http fetch GET 200 https://registry.npmjs.org/type-fest 58ms
npm http fetch GET 200 https://registry.npmjs.org/is-stream/-/is-stream-2.0.0.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.flattendeep 64ms
npm http fetch GET 200 https://registry.npmjs.org/imurmurhash 27ms
npm http fetch GET 200 https://registry.npmjs.org/p-locate 37ms
npm http fetch GET 200 https://registry.npmjs.org/release-zalgo 50ms
npm http fetch GET 200 https://registry.npmjs.org/type-fest/-/type-fest-0.8.1.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/shebang-command 35ms
npm http fetch GET 200 https://registry.npmjs.org/lodash.flattendeep/-/lodash.flattendeep-4.4.0.tgz 22ms
npm http fetch GET 200 https://registry.npmjs.org/typedarray-to-buffer 54ms
npm http fetch GET 200 https://registry.npmjs.org/p-locate/-/p-locate-4.1.0.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/default-require-extensions 59ms
npm http fetch GET 200 https://registry.npmjs.org/release-zalgo/-/release-zalgo-1.0.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fcode-frame 55ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-compilation-targets 41ms
npm http fetch GET 200 https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz 80ms
npm http fetch GET 200 https://registry.npmjs.org/typedarray-to-buffer/-/typedarray-to-buffer-3.1.5.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-module-transforms 41ms
npm http fetch GET 200 https://registry.npmjs.org/default-require-extensions/-/default-require-extensions-3.0.0.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fgenerator 71ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.14.5.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2ftraverse 37ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fparser 47ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2ftypes 42ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelpers 75ms
npm http fetch GET 200 https://registry.npmjs.org/gensync 37ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.14.5.tgz 128ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.14.5.tgz 142ms
npm http fetch GET 200 https://registry.npmjs.org/json5 117ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2ftemplate 152ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/generator/-/generator-7.14.5.tgz 132ms
npm http fetch GET 200 https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.2.tgz 93ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helpers/-/helpers-7.14.5.tgz 94ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/types/-/types-7.14.5.tgz 101ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/traverse/-/traverse-7.14.5.tgz 108ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/parser/-/parser-7.14.5.tgz 105ms
npm http fetch GET 200 https://registry.npmjs.org/json5/-/json5-2.2.0.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi 43ms
npm http fetch GET 200 https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/indent-string 47ms
npm http fetch GET 200 https://registry.npmjs.org/clean-stack 54ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/template/-/template-7.14.5.tgz 70ms
npm http fetch GET 200 https://registry.npmjs.org/wrap-ansi 56ms
npm http fetch GET 200 https://registry.npmjs.org/emoji-regex 51ms
npm http fetch GET 200 https://registry.npmjs.org/is-fullwidth-code-point 60ms
npm http fetch GET 200 https://registry.npmjs.org/binary-extensions 53ms
npm http fetch GET 200 https://registry.npmjs.org/picomatch 60ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.0.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/indent-string/-/indent-string-4.0.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/fill-range 28ms
npm http fetch GET 200 https://registry.npmjs.org/clean-stack/-/clean-stack-2.2.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/is-extglob 36ms
npm http fetch GET 200 https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz 50ms
npm http fetch GET 200 https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.2.0.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/picomatch/-/picomatch-2.3.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-6.2.0.tgz 64ms
npm http fetch GET 200 https://registry.npmjs.org/p-locate/-/p-locate-3.0.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz 7ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/fill-range/-/fill-range-7.0.1.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/sprintf-js 42ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-styles 43ms
npm http fetch GET 200 https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-5.1.0.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/balanced-match 44ms
npm http fetch GET 200 https://registry.npmjs.org/es-abstract 44ms
npm http fetch GET 200 https://registry.npmjs.org/sprintf-js/-/sprintf-js-1.0.3.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi/-/strip-ansi-4.0.0.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/strip-ansi/-/strip-ansi-5.2.0.tgz 58ms
npm http fetch GET 200 https://registry.npmjs.org/concat-map 69ms
npm http fetch GET 200 https://registry.npmjs.org/call-bind 59ms
npm http fetch GET 200 https://registry.npmjs.org/emoji-regex/-/emoji-regex-7.0.3.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz 80ms
npm http fetch GET 200 https://registry.npmjs.org/call-bind/-/call-bind-1.0.2.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/is-buffer 49ms
npm http fetch GET 200 https://registry.npmjs.org/es-abstract/-/es-abstract-1.18.3.tgz 72ms
npm http fetch GET 200 https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz 67ms
npm http fetch GET 200 https://registry.npmjs.org/github-url-to-object 48ms
npm http fetch GET 200 https://registry.npmjs.org/jsonist 55ms
npm http fetch GET 200 https://registry.npmjs.org/duplexify 24ms
npm http fetch GET 200 https://registry.npmjs.org/pako 33ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-from 45ms
npm http fetch GET 200 https://registry.npmjs.org/github-url-to-object/-/github-url-to-object-2.2.6.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-alloc 41ms
npm http fetch GET 200 https://registry.npmjs.org/duplexify/-/duplexify-3.7.1.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/is-buffer/-/is-buffer-2.0.5.tgz 63ms
npm http fetch GET 200 https://registry.npmjs.org/jsonist/-/jsonist-2.1.2.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/bl/-/bl-1.2.3.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/to-buffer 57ms
npm http fetch GET 200 https://registry.npmjs.org/pako/-/pako-0.2.9.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/duplexify/-/duplexify-3.7.1.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.1.tgz 55ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-alloc/-/buffer-alloc-1.2.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/pump/-/pump-2.0.1.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/to-buffer/-/to-buffer-1.1.1.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/delayed-stream 32ms
npm http fetch GET 200 https://registry.npmjs.org/asynckit 31ms
npm http fetch GET 200 https://registry.npmjs.org/ajv 34ms
npm http fetch GET 200 https://registry.npmjs.org/har-schema 50ms
npm http fetch GET 200 https://registry.npmjs.org/assert-plus 76ms
npm http fetch GET 200 https://registry.npmjs.org/jsprim 78ms
npm http fetch GET 200 https://registry.npmjs.org/mime-db 61ms
npm http fetch GET 200 https://registry.npmjs.org/sshpk 71ms
npm http fetch GET 200 https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz 65ms
npm http fetch GET 200 https://registry.npmjs.org/ms/-/ms-2.0.0.tgz 58ms
npm http fetch GET 200 https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz 79ms
npm http fetch GET 200 https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/jsprim/-/jsprim-1.4.1.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/sshpk/-/sshpk-1.16.1.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/mime-db/-/mime-db-1.48.0.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/psl 28ms
npm http fetch GET 200 https://registry.npmjs.org/punycode 40ms
npm http fetch GET 200 https://registry.npmjs.org/d 36ms
npm http fetch GET 200 https://registry.npmjs.org/buffers 32ms
npm http fetch GET 200 https://registry.npmjs.org/ext 39ms
npm http fetch GET 200 https://registry.npmjs.org/punycode/-/punycode-2.1.1.tgz 19ms
npm http fetch GET 200 https://registry.npmjs.org/psl/-/psl-1.8.0.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/string_decoder 27ms
npm http fetch GET 200 https://registry.npmjs.org/chainsaw 55ms
npm http fetch GET 200 https://registry.npmjs.org/core-util-is 34ms
npm http fetch GET 200 https://registry.npmjs.org/d/-/d-1.0.1.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/buffers/-/buffers-0.1.1.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/isarray 27ms
npm http fetch GET 200 https://registry.npmjs.org/ext/-/ext-1.4.0.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/util-deprecate 96ms
npm http fetch GET 200 https://registry.npmjs.org/buffer 42ms
npm http fetch GET 200 https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/util-deprecate 60ms
npm http fetch GET 200 https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz 60ms
npm http fetch GET 200 https://registry.npmjs.org/chainsaw/-/chainsaw-0.1.0.tgz 78ms
npm http fetch GET 200 https://registry.npmjs.org/process-nextick-args 72ms
npm http fetch GET 200 https://registry.npmjs.org/p-limit 53ms
npm http fetch GET 200 https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz 22ms
npm http fetch GET 200 https://registry.npmjs.org/buffer/-/buffer-5.7.1.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz 27ms
npm http fetch GET 200 https://registry.npmjs.org/strip-bom 25ms
npm http fetch GET 200 https://registry.npmjs.org/es6-error 33ms
npm http fetch GET 200 https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/bitbucket-url-to-object 468ms
npm http fetch GET 200 https://registry.npmjs.org/shebang-regex 41ms
npm http fetch GET 200 https://registry.npmjs.org/p-limit/-/p-limit-2.3.0.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/strip-bom/-/strip-bom-4.0.0.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-module-imports 49ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-replace-supers 48ms
npm http fetch GET 200 https://registry.npmjs.org/es6-error/-/es6-error-4.1.1.tgz 43ms
npm http fetch GET 200 https://registry.npmjs.org/string_decoder/-/string_decoder-1.3.0.tgz 172ms
npm http fetch GET 200 https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-simple-access 56ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhighlight 87ms
npm http fetch GET 200 https://registry.npmjs.org/bitbucket-url-to-object/-/bitbucket-url-to-object-0.3.0.tgz 71ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.14.5.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-split-export-declaration 42ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-simple-access/-/helper-simple-access-7.14.5.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-validator-identifier 45ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-replace-supers/-/helper-replace-supers-7.14.5.tgz 76ms
npm http fetch GET 200 https://registry.npmjs.org/to-fast-properties 57ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/highlight/-/highlight-7.14.5.tgz 70ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-validator-option 76ms
npm http fetch GET 200 https://registry.npmjs.org/browserslist 83ms
npm http fetch GET 200 https://registry.npmjs.org/jsesc 83ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-split-export-declaration/-/helper-split-export-declaration-7.14.5.tgz 116ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fcompat-data 144ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-function-name 108ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.14.5.tgz 107ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.14.5.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz 71ms
npm http fetch GET 200 https://registry.npmjs.org/jsesc/-/jsesc-2.5.2.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/browserslist/-/browserslist-4.16.6.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex 21ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz 24ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-hoist-variables 48ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.14.5.tgz 42ms
npm http fetch GET 200 https://registry.npmjs.org/color-convert 26ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex 52ms
npm http fetch GET 200 https://registry.npmjs.org/globals 87ms
npm http fetch GET 200 https://registry.npmjs.org/to-regex-range 77ms
npm http fetch GET 200 https://registry.npmjs.org/es-to-primitive 53ms
npm http fetch GET 200 https://registry.npmjs.org/get-intrinsic 51ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-function-name/-/helper-function-name-7.14.5.tgz 97ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-hoist-variables/-/helper-hoist-variables-7.14.5.tgz 59ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex 81ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.0.tgz 77ms
npm http fetch GET 200 https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex/-/ansi-regex-3.0.0.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/globals/-/globals-11.12.0.tgz 40ms
npm http fetch GET 200 https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/es-to-primitive/-/es-to-primitive-1.2.1.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.1.1.tgz 36ms
npm http fetch GET 200 https://registry.npmjs.org/has 30ms
npm http fetch GET 200 https://registry.npmjs.org/is-callable 30ms
npm http fetch GET 200 https://registry.npmjs.org/ansi-regex/-/ansi-regex-4.1.0.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/object-inspect 32ms
npm http fetch GET 200 https://registry.npmjs.org/is-string 36ms
npm http fetch GET 200 https://registry.npmjs.org/is-negative-zero 41ms
npm http fetch GET 200 https://registry.npmjs.org/is-regex 41ms
npm http fetch GET 200 https://registry.npmjs.org/has/-/has-1.0.3.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/string.prototype.trimstart 25ms
npm http fetch GET 200 https://registry.npmjs.org/string.prototype.trimend 32ms
npm http fetch GET 200 https://registry.npmjs.org/is-callable/-/is-callable-1.2.3.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/is-string/-/is-string-1.0.6.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/is-url 41ms
npm http fetch GET 200 https://registry.npmjs.org/is-negative-zero/-/is-negative-zero-2.0.1.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/is-regex/-/is-regex-1.1.3.tgz 48ms
npm http fetch GET 200 https://registry.npmjs.org/object-inspect/-/object-inspect-1.10.3.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/string.prototype.trimstart/-/string.prototype.trimstart-1.0.4.tgz 41ms
npm http fetch GET 200 https://registry.npmjs.org/unbox-primitive 58ms
npm http fetch GET 200 https://registry.npmjs.org/object.assign/-/object.assign-4.1.2.tgz 122ms
npm http fetch GET 200 https://registry.npmjs.org/bl/-/bl-3.0.1.tgz 99ms
npm http fetch GET 200 https://registry.npmjs.org/stream-shift 103ms
npm http fetch GET 200 https://registry.npmjs.org/string.prototype.trimend/-/string.prototype.trimend-1.0.4.tgz 113ms
npm http fetch GET 200 https://registry.npmjs.org/is-url/-/is-url-1.2.4.tgz 86ms
npm http fetch GET 200 https://registry.npmjs.org/unbox-primitive/-/unbox-primitive-1.0.1.tgz 49ms
npm http fetch GET 200 https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz 2ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/hyperquest 31ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-alloc-unsafe 29ms
npm http fetch GET 200 https://registry.npmjs.org/stream-shift/-/stream-shift-1.0.1.tgz 31ms
npm http fetch GET 200 https://registry.npmjs.org/uri-js 23ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-fill 35ms
npm http fetch GET 200 https://registry.npmjs.org/fast-deep-equal 34ms
npm http fetch GET 200 https://registry.npmjs.org/fast-json-stable-stringify 47ms
npm http fetch GET 200 https://registry.npmjs.org/extsprintf 36ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema 35ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema-traverse 49ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-alloc-unsafe/-/buffer-alloc-unsafe-1.1.0.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/verror 28ms
npm http fetch GET 200 https://registry.npmjs.org/hyperquest/-/hyperquest-2.1.3.tgz 75ms
npm http fetch GET 200 https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz 62ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-fill/-/buffer-fill-1.0.0.tgz 64ms
npm http fetch GET 200 https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz 52ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz 51ms
npm http fetch GET 200 https://registry.npmjs.org/verror/-/verror-1.10.0.tgz 47ms
npm http fetch GET 200 https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/asn1 35ms
npm http fetch GET 200 https://registry.npmjs.org/tweetnacl 26ms
npm http fetch GET 200 https://registry.npmjs.org/bcrypt-pbkdf 37ms
npm http fetch GET 200 https://registry.npmjs.org/dashdash 46ms
npm http fetch GET 200 https://registry.npmjs.org/asn1/-/asn1-0.2.4.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/getpass 54ms
npm http fetch GET 200 https://registry.npmjs.org/es5-ext 45ms
npm http fetch GET 200 https://registry.npmjs.org/type 46ms
npm http fetch GET 200 https://registry.npmjs.org/ecc-jsbn 55ms
npm http fetch GET 200 https://registry.npmjs.org/jsbn 65ms
npm http fetch GET 200 https://registry.npmjs.org/safer-buffer 68ms
npm http fetch GET 200 https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz 39ms
npm http fetch GET 200 https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz 32ms
npm http fetch GET 200 https://registry.npmjs.org/es5-ext/-/es5-ext-0.10.53.tgz 97ms
npm http fetch GET 200 https://registry.npmjs.org/type/-/type-1.2.0.tgz 96ms
npm http fetch GET 200 https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz 92ms
npm http fetch GET 200 https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz 101ms
npm http fetch GET 200 https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz 86ms
npm http fetch GET 200 https://registry.npmjs.org/type/-/type-2.5.0.tgz 86ms
npm http fetch GET 200 https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz 91ms
npm http fetch GET 200 https://registry.npmjs.org/traverse 79ms
npm http fetch GET 200 https://registry.npmjs.org/base64-js 53ms
npm http fetch GET 200 https://registry.npmjs.org/ieee754 40ms
npm http fetch GET 200 https://registry.npmjs.org/traverse/-/traverse-0.3.9.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/p-try 35ms
npm http fetch GET 200 https://registry.npmjs.org/js-tokens 32ms
npm http fetch GET 200 https://registry.npmjs.org/escalade 23ms
npm http fetch GET 200 https://registry.npmjs.org/p-try/-/p-try-2.2.0.tgz 23ms
npm http fetch GET 200 https://registry.npmjs.org/caniuse-lite 49ms
npm http fetch GET 200 https://registry.npmjs.org/ieee754/-/ieee754-1.2.1.tgz 46ms
npm http fetch GET 200 https://registry.npmjs.org/colorette 56ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-optimise-call-expression 69ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-member-expression-to-functions 112ms
npm http fetch GET 200 https://registry.npmjs.org/escalade/-/escalade-3.1.1.tgz 56ms
npm http fetch GET 200 https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz 107ms
npm http fetch GET 200 https://registry.npmjs.org/node-releases 97ms
npm http fetch GET 200 https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001236.tgz 101ms
npm http fetch GET 200 https://registry.npmjs.org/electron-to-chromium 158ms
npm http fetch GET 200 https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz 158ms
npm http fetch GET 200 https://registry.npmjs.org/colorette/-/colorette-1.2.2.tgz 108ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-optimise-call-expression/-/helper-optimise-call-expression-7.14.5.tgz 97ms
npm http fetch GET 200 https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz 85ms
npm http fetch GET 200 https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.3.752.tgz 28ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-member-expression-to-functions/-/helper-member-expression-to-functions-7.14.5.tgz 108ms
npm http fetch GET 200 https://registry.npmjs.org/color-name 42ms
npm http fetch GET 200 https://registry.npmjs.org/is-number 35ms
npm http fetch GET 200 https://registry.npmjs.org/is-date-object 38ms
npm http fetch GET 200 https://registry.npmjs.org/node-releases/-/node-releases-1.1.73.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/is-symbol 39ms
npm http fetch GET 200 https://registry.npmjs.org/has-bigints 39ms
npm http fetch GET 200 https://registry.npmjs.org/which-boxed-primitive 39ms
npm http fetch GET 200 https://registry.npmjs.org/@babel%2fhelper-get-function-arity 63ms
npm http fetch GET 200 https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz 53ms
npm http fetch GET 200 https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz 57ms
npm http fetch GET 200 https://registry.npmjs.org/is-date-object/-/is-date-object-1.0.4.tgz 67ms
npm http fetch GET 200 https://registry.npmjs.org/which-boxed-primitive/-/which-boxed-primitive-1.0.2.tgz 61ms
npm http fetch GET 200 https://registry.npmjs.org/duplexer2/-/duplexer2-0.0.2.tgz 76ms
npm http fetch GET 200 https://registry.npmjs.org/has-bigints/-/has-bigints-1.0.1.tgz 68ms
npm http fetch GET 200 https://registry.npmjs.org/buffer-from/-/buffer-from-0.1.2.tgz 82ms
npm http fetch GET 200 https://registry.npmjs.org/@babel/helper-get-function-arity/-/helper-get-function-arity-7.14.5.tgz 64ms
npm http fetch GET 200 https://registry.npmjs.org/is-symbol/-/is-symbol-1.0.4.tgz 75ms
npm http fetch GET 200 https://registry.npmjs.org/through2/-/through2-0.6.5.tgz 67ms
npm http fetch GET 200 https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz 9ms (from cache)
npm http fetch GET 200 https://registry.npmjs.org/extsprintf/-/extsprintf-1.4.0.tgz 38ms
npm http fetch GET 200 https://registry.npmjs.org/next-tick 32ms
npm http fetch GET 200 https://registry.npmjs.org/es6-iterator 36ms
npm http fetch GET 200 https://registry.npmjs.org/is-bigint 50ms
npm http fetch GET 200 https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz 44ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream/-/readable-stream-1.0.34.tgz 33ms
npm http fetch GET 200 https://registry.npmjs.org/next-tick/-/next-tick-1.0.0.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/is-number-object 65ms
npm http fetch GET 200 https://registry.npmjs.org/is-boolean-object 74ms
npm http fetch GET 200 https://registry.npmjs.org/es6-iterator/-/es6-iterator-2.0.3.tgz 45ms
npm http fetch GET 200 https://registry.npmjs.org/readable-stream/-/readable-stream-1.1.14.tgz 66ms
npm http fetch GET 200 https://registry.npmjs.org/is-bigint/-/is-bigint-1.0.2.tgz 35ms
npm http fetch GET 200 https://registry.npmjs.org/is-number-object/-/is-number-object-1.0.5.tgz 25ms
npm http fetch GET 200 https://registry.npmjs.org/isarray/-/isarray-0.0.1.tgz 30ms
npm http fetch GET 200 https://registry.npmjs.org/is-boolean-object/-/is-boolean-object-1.1.1.tgz 34ms
npm http fetch GET 200 https://registry.npmjs.org/string_decoder/-/string_decoder-0.10.31.tgz 40ms
npm timing stage:loadIdealTree:loadAllDepsIntoIdealTree Completed in 5776ms
npm timing stage:loadIdealTree Completed in 5885ms
npm timing stage:generateActionsToTake Completed in 54ms
npm timing action:extract Completed in 97ms
npm timing action:finalize Completed in 19ms
npm timing action:refresh-package-json Completed in 29ms
npm info lifecycle ms@2.1.2~preinstall: ms@2.1.2
npm info lifecycle debug@4.3.1~preinstall: debug@4.3.1
npm info lifecycle get-symbol-from-current-process-h@1.0.2~preinstall: get-symbol-from-current-process-h@1.0.2
npm info lifecycle node-addon-api@3.2.1~preinstall: node-addon-api@3.2.1
npm info lifecycle node-gyp-build@4.2.3~preinstall: node-gyp-build@4.2.3
npm info lifecycle get-symbol-from-current-process-h@1.0.2~preinstall: get-symbol-from-current-process-h@1.0.2
npm info lifecycle ms@2.1.3~preinstall: ms@2.1.3
npm info lifecycle debug@3.2.7~preinstall: debug@3.2.7
npm info lifecycle get-uv-event-loop-napi-h@1.0.6~preinstall: get-uv-event-loop-napi-h@1.0.6
npm info lifecycle ref-napi@3.0.3~preinstall: ref-napi@3.0.3
npm info lifecycle ref-struct-di@1.1.1~preinstall: ref-struct-di@1.1.1
npm timing action:preinstall Completed in 2ms
npm info linkStuff ms@2.1.2
npm info linkStuff debug@4.3.1
npm info linkStuff get-symbol-from-current-process-h@1.0.2
npm info linkStuff node-addon-api@3.2.1
npm info linkStuff node-gyp-build@4.2.3
npm info linkStuff get-symbol-from-current-process-h@1.0.2
npm info linkStuff ms@2.1.3
npm info linkStuff debug@3.2.7
npm info linkStuff get-uv-event-loop-napi-h@1.0.6
npm info linkStuff ref-napi@3.0.3
npm info linkStuff ref-struct-di@1.1.1
npm timing action:build Completed in 8ms
npm info lifecycle ms@2.1.2~install: ms@2.1.2
npm info lifecycle debug@4.3.1~install: debug@4.3.1
npm info lifecycle get-symbol-from-current-process-h@1.0.2~install: get-symbol-from-current-process-h@1.0.2
npm info lifecycle node-addon-api@3.2.1~install: node-addon-api@3.2.1
npm info lifecycle node-gyp-build@4.2.3~install: node-gyp-build@4.2.3
npm info lifecycle get-symbol-from-current-process-h@1.0.2~install: get-symbol-from-current-process-h@1.0.2
npm info lifecycle ms@2.1.3~install: ms@2.1.3
npm info lifecycle debug@3.2.7~install: debug@3.2.7
npm info lifecycle get-uv-event-loop-napi-h@1.0.6~install: get-uv-event-loop-napi-h@1.0.6
npm info lifecycle ref-napi@3.0.3~install: ref-napi@3.0.3

> ref-napi@3.0.3 install /openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3/node_modules/ref-napi
> node-gyp-build

gyp info it worked if it ends with ok
gyp info using node-gyp@5.1.0
gyp info using node@14.17.0 | linux | x64
gyp info find Python using Python version 3.8.5 found at "/openwrt/staging_dir/host/bin/python"
gyp info spawn /openwrt/staging_dir/host/bin/python
gyp info spawn args [
gyp info spawn args   '/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/gyp/gyp_main.py',
gyp info spawn args   'binding.gyp',
gyp info spawn args   '-f',
gyp info spawn args   'make',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3/node_modules/ref-napi/build/config.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/addon.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/staging_dir/target-aarch64_cortex-a53_musl/usr/include/node/common.gypi',
gyp info spawn args   '-Dlibrary=shared_library',
gyp info spawn args   '-Dvisibility=default',
gyp info spawn args   '-Dnode_root_dir=/openwrt/staging_dir/target-aarch64_cortex-a53_musl/usr/',
gyp info spawn args   '-Dnode_gyp_dir=/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp',
gyp info spawn args   '-Dnode_lib_file=/openwrt/staging_dir/target-aarch64_cortex-a53_musl/usr/$(Configuration)/node.lib',
gyp info spawn args   '-Dmodule_root_dir=/openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3/node_modules/ref-napi',
gyp info spawn args   '-Dnode_engine=v8',
gyp info spawn args   '--depth=.',
gyp info spawn args   '--no-parallel',
gyp info spawn args   '--generator-output',
gyp info spawn args   'build',
gyp info spawn args   '-Goutput_dir=.'
gyp info spawn args ]
gyp info spawn make
gyp info spawn args [ 'BUILDTYPE=Release', '-C', 'build' ]
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3/node_modules/ref-napi/build'
  CC(target) Release/obj.target/nothing/../node-addon-api/nothing.o
rm -f Release/obj.target/../node-addon-api/nothing.a Release/obj.target/../node-addon-api/nothing.a.ar-file-list; mkdir -p `dirname Release/obj.target/../node-addon-api/nothing.a`
aarch64-openwrt-linux-musl-gcc-ar crs Release/obj.target/../node-addon-api/nothing.a @Release/obj.target/../node-addon-api/nothing.a.ar-file-list
  COPY Release/nothing.a
  CXX(target) Release/obj.target/binding/src/binding.o
  SOLINK_MODULE(target) Release/obj.target/binding.node
  COPY Release/binding.node
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3/node_modules/ref-napi/build'
gyp info ok 
npm timing audit submit Completed in 255ms
npm http fetch POST 200 https://registry.npmjs.org/-/npm/v1/security/audits/quick 255ms
npm timing audit body Completed in 1ms
npm info lifecycle ref-struct-di@1.1.1~install: ref-struct-di@1.1.1
npm timing action:install Completed in 2547ms
npm info lifecycle ms@2.1.2~postinstall: ms@2.1.2
npm info lifecycle debug@4.3.1~postinstall: debug@4.3.1
npm info lifecycle get-symbol-from-current-process-h@1.0.2~postinstall: get-symbol-from-current-process-h@1.0.2
npm info lifecycle node-addon-api@3.2.1~postinstall: node-addon-api@3.2.1
npm info lifecycle node-gyp-build@4.2.3~postinstall: node-gyp-build@4.2.3
npm info lifecycle get-symbol-from-current-process-h@1.0.2~postinstall: get-symbol-from-current-process-h@1.0.2
npm info lifecycle ms@2.1.3~postinstall: ms@2.1.3
npm info lifecycle debug@3.2.7~postinstall: debug@3.2.7
npm info lifecycle get-uv-event-loop-napi-h@1.0.6~postinstall: get-uv-event-loop-napi-h@1.0.6
npm info lifecycle ref-napi@3.0.3~postinstall: ref-napi@3.0.3
npm info lifecycle ref-struct-di@1.1.1~postinstall: ref-struct-di@1.1.1
npm timing action:postinstall Completed in 3ms
npm timing stage:executeActions Completed in 2721ms
npm timing stage:rollbackFailedOptional Completed in 0ms
npm info linkStuff ffi-napi@4.0.3
npm info lifecycle ffi-napi@4.0.3~install: ffi-napi@4.0.3

> ffi-napi@4.0.3 install /openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3
> node-gyp-build

gyp info it worked if it ends with ok
gyp info using node-gyp@5.1.0
gyp info using node@14.17.0 | linux | x64
gyp info find Python using Python version 3.8.5 found at "/openwrt/staging_dir/host/bin/python"
gyp info spawn /openwrt/staging_dir/host/bin/python
gyp info spawn args [
gyp info spawn args   '/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/gyp/gyp_main.py',
gyp info spawn args   'binding.gyp',
gyp info spawn args   '-f',
gyp info spawn args   'make',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3/build/config.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/addon.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/openwrt/staging_dir/target-aarch64_cortex-a53_musl/usr/include/node/common.gypi',
gyp info spawn args   '-Dlibrary=shared_library',
gyp info spawn args   '-Dvisibility=default',
gyp info spawn args   '-Dnode_root_dir=/openwrt/staging_dir/target-aarch64_cortex-a53_musl/usr/',
gyp info spawn args   '-Dnode_gyp_dir=/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp',
gyp info spawn args   '-Dnode_lib_file=/openwrt/staging_dir/target-aarch64_cortex-a53_musl/usr/$(Configuration)/node.lib',
gyp info spawn args   '-Dmodule_root_dir=/openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3',
gyp info spawn args   '-Dnode_engine=v8',
gyp info spawn args   '--depth=.',
gyp info spawn args   '--no-parallel',
gyp info spawn args   '--generator-output',
gyp info spawn args   'build',
gyp info spawn args   '-Goutput_dir=.'
gyp info spawn args ]
gyp info spawn make
gyp info spawn args [ 'BUILDTYPE=Release', '-C', 'build' ]
make[4]: Entering directory '/openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3/build'
  CXX(target) Release/obj.target/ffi_bindings/src/ffi.o
../src/ffi.cc:4:10: fatal error: fficonfig.h: No such file or directory
 #include "fficonfig.h"
          ^~~~~~~~~~~~~
compilation terminated.
make[4]: *** [ffi_bindings.target.mk:117: Release/obj.target/ffi_bindings/src/ffi.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3/build'
gyp ERR! build error 
gyp ERR! stack Error: `make` failed with exit code: 2
gyp ERR! stack     at ChildProcess.onExit (/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/lib/build.js:194:23)
gyp ERR! stack     at ChildProcess.emit (events.js:376:20)
gyp ERR! stack     at Process.ChildProcess._handle.onexit (internal/child_process.js:277:12)
gyp ERR! System Linux 5.8.0-1033-azure
gyp ERR! command "/openwrt/staging_dir/hostpkg/bin/node" "/openwrt/staging_dir/hostpkg/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js" "rebuild"
gyp ERR! cwd /openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3
gyp ERR! node -v v14.17.0
gyp ERR! node-gyp -v v5.1.0
gyp ERR! not ok 
npm info lifecycle ffi-napi@4.0.3~install: Failed to exec install script
npm ERR! code ELIFECYCLE
npm ERR! errno 1
npm ERR! ffi-napi@4.0.3 install: `node-gyp-build`
npm ERR! Exit status 1
npm ERR! 
npm ERR! Failed at the ffi-napi@4.0.3 install script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.
npm timing npm Completed in 9911ms

npm ERR! A complete log of this run can be found in:
npm ERR!     /openwrt/tmp/npm-cache-3MAYCIdAMR/_logs/2021-06-10T16_18_59_836Z-debug.log
make[3]: *** [Makefile:92: /openwrt/build_dir/target-aarch64_cortex-a53_musl/node-ffi-napi-4.0.3/.built] Error 1
```