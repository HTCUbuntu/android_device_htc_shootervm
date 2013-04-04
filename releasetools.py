# Copyright (C) 2013 The Android Open Source Project
# Copyright (C) 2013 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom OTA commands for shooter"""

import common
import os
import shutil

# Added ramjet73's hack for deleting WiMax Log's

def FullOTA_Assertions(info):
  info.script.AppendExtra('assert(getprop("ro.bootloader") == "1.04.2000" || getprop("ro.bootloader") == "1.50.5050" || getprop("ro.bootloader") == "1.40.1100"|| getprop("ro.bootloader") == "1.30.0000" || getprop("ro.bootloader") == "1.40.0000" || getprop("ro.bootloader") == "1.50.0000" || getprop("ro.bootloader") == "1.40.1000");')
  info.script.AppendExtra('ui_print("Running Ramjet73 Log Fix");')
  info.script.AppendExtra('ui_print("* Change WiMax logs directory to immutable and delete logs");')
  info.script.AppendExtra('ui_print("Mounting /data...");')
  info.script.AppendExtra('run_program("/sbin/busybox", "mount", "/data");')
  info.script.AppendExtra('show_progress(1.000000, 20);')
  info.script.AppendExtra('delete_recursive("/data/wimax/log");')
  info.script.AppendExtra('run_program("/sbin/busybox", "mkdir", "/data/wimax/log");')
  info.script.AppendExtra('run_program("/sbin/busybox", "chattr", "+i", "/data/wimax/log");')
  info.script.AppendExtra('unmount("/data");')
  info.script.AppendExtra('ui_print("WiMax fix is completed");')
  info.script.AppendExtra('show_progress(1.000000, 0);')
  info.script.AppendExtra('ui_print("Installing Angry Bean!");')
