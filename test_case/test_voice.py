from tool.get_token import *

class MyTestCase(unittest.TestCase):
    """剧场"""

    def setUp(self):
        self.status = ""    # 0：未上线，1：已上线，2：已下线
        self.room_id = ""
        self.content = "test专用聊天"
        self.char_id = ""

    def test_get_rooms(self):
        """获取房间列表"""
        data = {
            "status": self.status,
            "page_num": 1,
            "page_size": 5,
        }
        res = requests.post(url=base_url + "/app/voice/get-rooms",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_send_chat(self):
        """发送聊天消息"""
        data = {
            "room_id": self.room_id,
            "content": self.content,
        }
        res = requests.post(url=base_url + "/app/voice/send-chat",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_room(self):
        """获取房间"""
        data = {
            "room_id": self.room_id,
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
	        "musics": "[]",
	        "current_count": 1,
	        "total_count": 1,
	        "display_count": 1,
	        "hot": 1,
	        "display_hot": 1,
	        "open_time": 1,
	        "close time": 1,
	        "play_time": 1,
	        "stop_time": 1,
	        "play_count": 1,
	        "replay_interval": 1,
	        "play_schedule": 1,
	        "replay_times": {
                "start": 1,
                "end": 1,
            },
	        "character_ids": [],
	        "scriptid": 1,
	    }
        res = requests.post(url=base_url + "/app/voice/add-room",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_room(self):
        """修改房间"""
        data = {
	        "room_id": "",
	        "fields": "[]",
	        "room": {
	        "name": "",
	        "cover": "",
	        "bg": "",
	        "musics": "[]",
	        "current_count": 1,
	        "total_count": 1,
	        "display_count": 1,
	        "hot": 1,
	        "display_hot": 1,
	        "open_time": 1,
	        "close time": 1,
	        "play_time": 1,
	        "stop_time": 1,
	        "play_count": 1,
	        "replay_interval": 1,
	        "play_schedule": 1,
	        "replay_times": {
                "start": 1,
                "end": 1,
            },
	        "character_ids": [],
	        "scriptid": 1
	    },
	    }
        res = requests.post(url=base_url + "/app/voice/edit-room",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_character(self):
        """添加角色"""
        data = {
            'char': {
                "name": "",
                "mantra": "",
                "dub": "",
                "avatar": "",
                "sprite": "",
                "weight": 1,
                "display_hot": 1,
            },
        }
        res = requests.post(url=base_url + "/app/voice/add-character",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_character(self):
        """修改角色"""
        data = {
	        "char_id": self.char_id,
	        "fields": "[]",
	        "char": {
		        "name": "",
		        "mantra": "",
		        "dub": "",
		        "avatar": "",
		        "sprite": "",
		        "weight": 1,
		        "display_hot": 1,
		},
	}
        res = requests.post(url=base_url + "/app/voice/edit-character",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_script(self):
        """添加剧本"""
        data = {
	        "script": {
		        "lines": {
			        "char_id": 1,
			        "image": "",
			        "dub": "",
			        "caption": "",
			},
		},
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
			        "caption": "",
			},
		},
	}
        res = requests.post(url=base_url + "/app/voice/add-line",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_room1(self):
        """获取所有房间列表"""
        data = {
            'status': self.status,
        }
        res = requests.post(url=base_url + "/app/voice/edit-room",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
