# 0_zone_tool
零零信安api信息系统查询脚本

![image](https://github.com/wkend/0_zone_tool/assets/37563697/6097854a-4abe-4fd9-a9d4-d6620da08d0a)


# 用法
安装所需依赖
```
python3 -m pip install -r requirements.txt
```
替换代码中的`zone_key_id`和`query`
```
zone_key_id = "xxxxxxxxxxxxxxxxxx"
query = "(company=xxx有限公司)||(title==xxx有限公司)||(banner==xxx有限公司)||(ssl_info.detail=xxx有限公司)"
```
![image](https://github.com/wkend/0_zone_tool/assets/37563697/0ebdb9b2-6bea-4e33-974a-fafa3a546ecb)

运行脚本即可，结果保存到excle文件中
```
python3 0_zone.py
[-] 正在提取第1页数据，，，
[-] 正在提取第2页数据，，，
[-] 正在提取第3页数据，，，
[+] 第4页无数据，查询结束!
[+] 共查询到91条数据！
[+] 查询结果已经保存到results_20233215655.xlsx
```
![image](https://user-images.githubusercontent.com/37563697/222225610-07bf4cb3-9227-4ad4-b55a-6dbe56a33771.png)

## 参考语法
```
# 查询条件
query = "(company=xxx有限公司)||(title==xxx有限公司)||(banner==xxx有限公司)||(ssl_info.detail=xxx有限公司)"
```

# 说明

> 默认从第一页开始提取数据，每页条数最大为40，单个查询条件最多可获取10000条，单日累计查询次数上限为250次，请求速率<=2次/秒。

超过单日查询限制时：

![image](https://github.com/wkend/0_zone_tool/assets/37563697/cf6d0637-a228-4755-b9f4-936c32018b73)


已查询到的数据会保存：
![image](https://github.com/wkend/0_zone_tool/assets/37563697/fabe3009-7ae7-4504-ad0a-efacc25f958b)


