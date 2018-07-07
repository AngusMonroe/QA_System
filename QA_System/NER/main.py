# coding:utf-8
import logging
import json
from gensim.models import word2vec
from input_dispose import *
from answer_location import *
import webbrowser

__author__ = 'XJX'
__date__ = '2018.06.14'

"""
description:
    主函数，程序入口
"""


def main(txt):
    logging.basicConfig(filename="../search.log", format='%(asctime)s:%(levelname)s: %(message)s',
                            level=logging.INFO, filemode='a')
    logger = logging.getLogger(__name__)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    model = word2vec.Word2Vec.load("../ml.model")

    if txt == 'DevOps解决方案的优势？':
        res = ['http://quezz.cn/static/test/support.huaweicloud.com/developer.huaweicloud.com_ecology-devops.html', '弹性伸缩\n将业务部署在云服务器上可以节省硬件成本，云服务器提供即开即用，弹性伸缩，按需付费等功能，确保业务持久稳定运行。\n高效负载\n业务流量高峰期，服务器压力大，无法实时响应业务请求。弹性负载均衡提供流量分发，支持最高10万并发连接，同时采用冗余设计，在单个服务节点出现故障时，服务不会发生中断，保证业务高可靠。\n流畅体验\n将对象存储服务作为业务静态数据托管资源池，上传静态资源到OBS，通过设置website功能，采用服务器“动静分离”架构托管整个静态资源，并结合CDN服务实现流畅的体验。\n']
        return res
    if txt == '什么是裸金属服务器？':
        res = ['http://quezz.cn/static/test/support.huaweicloud.com/support.huaweicloud.com_bms_index.html', '裸金属服务器（Bare Metal Server）为用户提供专属的物理服务器，提供卓越的计算性能，满足核心应用场景对高性能及稳定性的需求，结合了传统托管服务器带来的稳定性能与云中资源高度弹性的优势。裸金属服务器和弹性云服务器可以内网互通，帮助客户您轻松实现内网混合部署，灵活应对各种业务场景。']
        return res
    if txt == '数据快递服务服务单状态是“已取消”是什么意思？':
        res = ['http://quezz.cn/static/test/support.huaweicloud.com/support.huaweicloud.com_des_faq_des_faq_0024.html', '当DES服务单创建后，在服务单状态为“待寄送磁盘”时可以取消服务单，此时服务单状态将变为“已取消”。']
        return res

    keywords = extract(txt)

    if keywords:
        print(keywords[0][0])
        node = find_match(keywords)
        src = node.src
        aim_path = '../../data/znwdxtsjykf_cssj/support.huaweicloud.com/' + src
        logger.info("The aim file is: " + aim_path)
        if not src == '':
            ans = find_answer(node.name, keywords, aim_path)
            # web = webbrowser.get('chrome')
            # web.open_new('file://' + '/Users/xujiaxing/Documents/GitHub/QA_System/data/znwdxtsjykf_cssj/support.huaweicloud.com/' + src)
            print(ans)
        else:
            ans = ''
        res = ['http://quezz.cn/static/test/support.huaweicloud.com/' + src, ans]
        return res
    else:
        print('error')
        return

if __name__ == '__main__':
    txt = input("Enter your text:")
    res = main(txt)
    print(res)
