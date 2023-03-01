# masscan-tools
Format Masscan OutFile
这个小工具能把Masscan的Json格式输出的文件,使用自定义的任意字符串进行格式化输出。


例如使用:

 ```python masscan-tools.py result.json bbb.txt ":"```
 
 可以使用":"来隔开Host与Port
