# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-08-01
# @FILE   : xhs.py

import requests

url = "https://www.xiaohongshu.com/discovery/item/62e6e2250000000012002d24?share_from_user_hidden=true&xhsshare=CopyLink&appuid=5d3880af000000001000cd93&apptime=1659330471"

payload={}
headers = {
  'authority': 'www.xiaohongshu.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
  'cache-control': 'max-age=0',
  'cookie': 'xhsTrackerId=1a74ba74-e8da-4e71-cedc-1ef035fa885b; a1=1823300ecf3dkts1sut7lyj3pbro519938zppbfpv00000152098; smidV2=20220725093755ef42544692919fd5753925109c8c160e00f0de1fb6c8bcbf0; gid=yYJqq88iJSqYyYJqq88dSYDiiqfT9MyM79W1uUhvVqUDFU88l2yjjU888y2J8jY8qDqqiYid; gid.sig=lu9graIMNRFZgf5rG3gM5FEjMLGzFlg61FBY8ILquvk; extra_exp_ids=wx_launch_open_app_decrement_v2_clt,wx_launch_open_app_decrement_clt,wx_launch_open_app_duration_origin,recommend_comment_hide_exp1,recommend_comment_hide_v2_exp2,recommend_comment_hide_v3_origin,supervision_exp,supervision_v2_exp,commentshow_exp1,gif_clt1,ques_exp1; timestamp2=1659330392329122c6cd88b63662779250225871125a58d8588987a793589b1; timestamp2.sig=pSPiN8jsr70RyTMAUXzGYcv2r_v77foaFxc-gvKaEEI; xhsTracker=url=noteDetail&xhsshare=CopyLink; xhsTracker=url=noteDetail&xhsshare=CopyLink',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


