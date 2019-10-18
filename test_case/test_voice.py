from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """剧场"""

    def setUp(self):
        pass

    def test_get_rooms(self):
        """获取房间列表"""
        data = {
            'status': 0 # 0：未上线，1：已上线，2：已下线
        }
        res = requests.post(url=base_url + "/app/voice/get-rooms",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_room(self):
        """获取房间"""
        data = {
            'room_id': ""
        }
        res = requests.post(url=base_url + "/app/voice/get-room",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_room(self):
        """添加房间"""
        data = {
	        "name": "",
	        "cover": "",
	        "bg": "",
	        "musics": "",
	        "current_count": "",
	        "total_count": "",
	        "display_count": "",
	        "hot": "",
	        "display_hot": "",
	        "open_time": "",
	        "close time": "",
	        "play_time": "",
	        "stop_time": "",
	        "play_count": "",
	        "replay_interval": "",
	        "play_schedule": "",
	        "replay_times": "",
	        "character_ids": "",
	        "scriptid": ""
	    }
        res = requests.post(url=base_url + "/app/voice/add-room",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_room(self):
        """修改房间"""
        data = {
	        "room_id": "",
	        "fields": {

            },
	        "room": ""
	    }
        res = requests.post(url=base_url + "/app/voice/edit-room",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_character(self):
        """添加角色"""
        data = {
            'char': {

            }
        }
        res = requests.post(url=base_url + "/app/voice/add-character",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_character(self):
        """修改角色"""
        data = {
	        "char_id": "",
	        "fields": [],
	        "char": {
		        "name": "",
		        "mantra": "",
		        "dub": "",
		        "avatar": "",
		        "sprite": "",
		        "weight": "",
		        "display_hot": ""
		}
	}
        res = requests.post(url=base_url + "/app/voice/edit-character",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_script(self):
        """添加剧本"""
        data = {
	        "script": {
		        "lines": {
			    "char_id": "",
			    "image": "",
			    "dub": "",
			    "caption": ""
			}
		}
	}
        res = requests.post(url=base_url + "/app/voice/add-script",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_line(self):
        """添加对白"""
        data = {
	        "script": {
		        "lines": {
			        "char_id": "",
			        "image": "",
			        "dub": "",
			        "caption": ""
			}
		}
	}
        res = requests.post(url=base_url + "/app/voice/add-line",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_room1(self):
        """获取所有房间列表"""
        data = {
            'status': 0 # 0：未上线，1：已上线，2：已下线
        }
        res = requests.post(url=base_url + "/app/voice/edit-room",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
