# 0_zone_tool
零零信安api信息系统查询脚本

# 用法
1.替换代码中的zone_key_id和查询条件
```
# api_key
zone_key_id = "xxxxxxxxxxxxxxxxxx"
```

## 参考语法
```
# 查询条件
query = "(company=xxx有限公司)||(title==xxx有限公司)||(banner==xxx有限公司)||(ssl_info.detail=xxx有限公司)"
```

2.运行脚本即可，结果保存到excle文件中
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

# 说明

默认从第一页开始提取数据，每页条数最大为40，单个查询条件最多可获取10000条，单日累计查询次数上限为250次，请求速率<=2次/秒。

超过单日查询限制时：
<img width="794" alt="Snipaste_2023-07-24_19-45-24" src="https://github.com/wkend/0_zone_tool/assets/37563697/d8fe2fb2-d67e-4356-826a-3a09d83b8240">
