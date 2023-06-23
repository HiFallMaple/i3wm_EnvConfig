import time
import os
import logging
import subprocess
import re

logging.basicConfig(filename=".log", encoding="utf-8", level=logging.INFO)

# exist = os.popen("ps -ef | grep LINE.exe")
# e = exist.readlines()
# if len(e) < 3:
#     logging.debug(e)
#     logging.debug("Line not started.")
#     exist.close()
#     continue
# exist.close()
output = os.popen("wmctrl -l -G -p -x")
s = output.readlines()
id = ''
for item in s:
    logging.debug(item)
    if item.find("line.exe.line.exe") != -1:
        id = item.split()[0]
        break
output.close()
print(id)
logging.info("line window id: " + id)



## 抓取陰影 id
# 執行 xwininfo 命令
# print("請點選最上方的陰影框")
# result = subprocess.run(["xwininfo"], capture_output=True, text=True)

# # 輸出 xwininfo 命令的輸出
# print(result.stdout)

# 抓取 Window id
# pattern = r"xwininfo: Window id: 0x[0-9a-fA-F]+"
# match = re.search(pattern, result.stdout)

# if match:
#     shadow_id_str = match.group()
#     print("fetch:", shadow_id_str)
#     pattern = r"0x[0-9a-fA-F]+"
#     match = re.search(pattern, result.stdout)
#     if match:
#         shadow_id = int(match.group(), 16)
#         print(f"Window ID: {shadow_id:x}")
#     else:
#         print("fetch ID failed")
# else:
#     print("Can't find Window ID")

shadow_id = int(id, 16)+ 0xa
for num in range(4):
    shadow = id[:-2]
    shadow += f"{shadow_id:x}"
    logging.info("xdotool windowunmap " + shadow)
    os.system("xdotool windowunmap " + shadow)
    shadow_id+=4

