#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   0_zone.py
@Time    :   2023/03/01 22:13:47
@Author  :   wkend
@Version :   1.0
'''
import requests
import json
import pandas as pd
import time
from termcolor import colored


def query_data(query, query_type, page, pagesize, zone_key_id):
    url = "https://0.zone/api/data/"
    headers = {
        "Content-Type": "application/json"
    }

    data_list = []
    flag = True
    while flag:
        payload = {
            "query": query,
            "query_type": query_type,
            "page": page,
            "pagesize": pagesize,
            "zone_key_id": zone_key_id
        }
        response = requests.post(url, headers=headers,
                                 timeout=2000, data=json.dumps(payload))
        if response.status_code != 200:
            print(colored("[+] Error: 请求出错，状态码为:"+response.status_code, 'red'))
            flag = False
        result_json = response.json()
        if result_json['code'] == 0:
            result_list = json.loads(response.text)['data']
            if result_json['pagesize'] == 0:
                print(colored('[+] 第{}页无数据，查询结束!'.format(page), 'blue'))
                flag = False
            else:
                print(colored('[-] 正在提取第{}页数据，，，'.format(page), 'blue'))
                for result in result_list:
                    data_list.append({
                        'ip': result['ip'],
                        'port': result['port'],
                        'url': result['url'],
                        'status_code': result['status_code'],  # 状态码
                        'company': result['group'],  # 公司名称
                        'title': result['title'],
                        'os': result['os'],
                        'cms': result['cms'],
                        'banner_os': result['banner_os'],
                        'component': result['component'],
                        'city': result['city'],
                        'device_type': result['device_type'],
                        'operator': result['operator'],  # 运营商
                        'service': result['service'],   # 服务
                        'extra_info': result['extra_info'],  # 设备分类
                        'app_name': result['app_name'],  # 应用名称
                        'tags': result['tags'],  # 标签
                    })
                time.sleep(3)
                page += 1
        else:
            print(colored("[+] Error: 查询出错，错误信息为:",
                  result_json['message'], 'red'))
            flag = False
    print(colored('[+] 共查询到{}条数据！'.format(result_json['total']), 'green'))
    return data_list


def process_data(data):
    df = pd.DataFrame(data)
    t = time.localtime()
    Timestamp = '{year}{mon}{day}{hour}{min}{sec}'.format(year=t.tm_year,
                                                          mon=t.tm_mon, day=t.tm_mday, hour=t.tm_hour, min=t.tm_min, sec=t.tm_sec)
    df.to_excel('threat_detection_results_{}.xlsx'.format(
        Timestamp), index=False)
    print(colored(
        "[+] 查询结果已经保存到results_{}.xlsx".format(Timestamp), 'green'))


def main():
    query = "(company=深圳壹账通智能科技有限公司)||(title==深圳壹账通智能科技有限公司)||(banner==深圳壹账通智能科技有限公司)||(ssl_info.detail=深圳壹账通智能科技有限公司)"  # 查询条件
    query_type = "site"  # 信息系统
    page = 1    # 第几页结果，理论上每日最多查询250次，即250页（如果查询结果有）
    pagesize = 40   # 每页条数，最大40
    zone_key_id = "168a16034fe673d61d6d2a32b9187d44"    # 查询api_key
    data = query_data(query, query_type, page, pagesize, zone_key_id)
    process_data(data)


if __name__ == "__main__":
    main()
