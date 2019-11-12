from tool.get_token import *

class MyTestCase(unittest.TestCase):
    """"""
    def setUp(self):
        self.live_id = ""
        self.live_type = ""

    def test_get_live_play_addr(self):
        """"""
        data = {
            "live_id": self.live_id,
            "live_type": self.live_type,
        }
        res = requests.post(url= base_url + "/app/live/get-live-play-addr",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()