[app]
title = Modern Calculator
package.name = moderncalculator
package.domain = org.moderncalculator

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,svg
source.include_patterns = assets/*,images/*
source.exclude_dirs = tests, bin, .git

version = 1.0
requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 0
osx.python_version = 3
osx.kivy_version = 2.1.0

# Android specific
android.permissions = INTERNET
android.arch = arm64-v8a
android.allow_backup = True
android.presplash_color = #F5F7FA
android.icon.filename = website/images/icon.png
android.presplash.filename = website/images/icon.png
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.accept_sdk_license = True
android.gradle_dependencies = org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.3.50
android.enable_androidx = True
android.logcat_filters = *:S python:D

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1 