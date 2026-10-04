[app]
title = Dialer
package.name = dialer
package.domain = org.example
source.dir = .
source.include_exts = py
version = 0.1
requirements = python3,kivy,plyer
orientation = portrait
fullscreen = 0
android.permissions = CALL_PHONE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
