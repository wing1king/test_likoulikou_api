from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """游戏数据"""

    def setUp(self):
        self.count = ""
        self.product_id = ""
        self.source = ""
        self.order_id = ""

    def test_get_cfg(self):
        """获取充值配置"""
        res = requests.post(url=base_url + "/app/pay/get-cfg", headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_creat_order(self):
        """创建订单"""
        data = {
            "count": self.count,
            "product_id": self.product_id,
            "source": self.source
        }
        res = requests.post(url=base_url + "/app/pay/creat-order", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_query_orde(self):
        """查询订单状态"""
        data = {
            "order_id": self.order_id
        }
        res = requests.post(url=base_url + "/app/pay/query-order", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
