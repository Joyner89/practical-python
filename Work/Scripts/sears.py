# sears.py
"""
将上方显示的代码复制粘贴到一个名为 `.` 的新程序中sears.py。运行该代码时，您将收到一条错误消息，导致程序崩溃，如下所示：

Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
读取错误信息是 Python 代码编写的重要组成部分。如果程序崩溃，回溯信息的最后一行才是程序崩溃的真正原因。在其上方，您应该会看到一段源代码片段，以及文件名和行号等标识信息。

哪一行代码出错了？
错误是什么？
修复错误
程序运行成功
"""

bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
sears_height = 442  # Height (meters)
num_bills = 1
day = 1
days = 0
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print("Number of days", day)
print("Number of bills", num_bills)
print("Final height", num_bills * bill_thickness)
