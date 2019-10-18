from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """编辑器"""

    def setUp(self):
        self.page_num = 1
        self.page_size = 5
        self.book_id = 130464463863808
        self.chapter_id = 130464463872000

    def test_cates(self):
        """获取分类"""
        res = requests.post(url=base_url + "/app/editor/cates",headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_books(self):
        """书本列表"""
        data = {
            "sort": -1,
            "sort_type": 0,
            "audit_status": -1,
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/editor/books", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_book(self):
        """添加书本"""
        data = {
            "name": "python创建书本",
            "desc": "窝窝头，一块钱四个，嘿嘿！",
            "image": "",
            "cate": [],
            "work_status": 0,
            "cate_id": ""
        }
        res = requests.post(url=base_url + "/app/editor/add-book", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_book(self):
        """删除书本"""
        data = {
            "book_id": self.test_add_book()
        }
        res = requests.post(url=base_url + "/app/editor/del-book", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_out_book(self):
        """下架书本"""
        data = {
            "book_id": ""
        }
        res = requests.post(url=base_url + "/app/editor/out-book", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_audit(self):
        """书本提审"""
        data = {
            "book_id": ""
        }
        res = requests.post(url=base_url + "/app/editor/audit", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_book(self):
        """书本信息"""
        data = {
            "book_id": self.book_id
        }
        res = requests.post(url=base_url + "/app/editor/book", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_book(self):
        """修改书本信息"""
        data = {
            "book_id": self.book_id,
            "name": "",
            "desc": "",
            "image": "",
            "cate":"", # 分类    [1,2,3,4]
            "work_status":""
        }
        res = requests.post(url=base_url + "/app/editor/edit-book", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_chapters(self):
        """章节列表"""
        data = {
            "book_id": self.book_id,
            "order": 1 # 0 倒序  1 正序
        }
        res = requests.post(url=base_url + "/app/editor/chapters", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_chapter(self):
        """删除章节"""
        data = {
            "book_id": self.book_id,
            "chapter_id": ""
        }
        res = requests.post(url=base_url + "/app/editor/del-chapter", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_chapter(self):
        """修改章节"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "name": ""
        }
        res = requests.post(url=base_url + "/app/editor/edit-chapter", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_json(self):
        """获取预览的json"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "page_id": ""
        }
        res = requests.post(url=base_url + "/app/editor/get-json", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_cmd(self):
        """添加章节指令"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "page_id": "",
            "index": "",
            "cmd": {
                "background": "",
                "characterId": "",
                "cmdId": "",
                "content": "",
                "type": ""
            }
        }
        res = requests.post(url=base_url + "/app/editor/add-cmd", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_cmd(self):
        """删除章节指令"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "page_id": "",
            "index": ""
        }
        res = requests.post(url=base_url + "/app/editor/del-cmd", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_cmd(self):
        """编辑章节指令"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "page_id": "",
            "index": "",
            "cmd": {
                "background": "",
                "characterId": "",
                "cmdId": "",
                "content": "",
                "type": ""
            }
        }
        res = requests.post(url=base_url + "/app/editor/edit-cmd", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_characters(self):
        """角色列表"""
        data = {
            "book_id": self.book_id
        }
        res = requests.post(url=base_url + "/app/editor/characters", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_character(self):
        """添加角色"""
        data = {
            "book_id": self.book_id,
            "icon": "https://xms-dev-1251001060.file.myqcloud.com/2366779543/2019/9/1568710377.776.jpg",
            "name": "python",
            "align": "left"
        }
        res = requests.post(url=base_url + "/app/editor/add-character", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_character(self):
        """修改角色"""
        data = {
            "book_id": self.book_id,
            "character_id": self.chapter_id,
            "nick_name": "python1111"
        }
        res = requests.post(url=base_url + "/app/editor/edit-character", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_character(self):
        """删除角色"""
        data = {
            "book_id": self.chapter_id,
            "character_id": self.chapter_id
        }
        res = requests.post(url=base_url + "/app/editor/del-character", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_pages(self):
        """Page获取页"""
        data = {
            "book_id": self.book_id
        }
        res = requests.post(url=base_url + "/app/editor/get-pages", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_page(self):
        """Page添加页"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "node": {
                "to": {},
                "from": {},
                "branch_title": "",
                "branch_ui": "",
                "cover": "",
                "type": "",
                "status": "",
                "name": ""
            }
        }
        res = requests.post(url=base_url + "/app/editor/add-page", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_editor_page(self):
        """Page修改页"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "page_id": "",
            "node": {
                "to": {},
                "from": {},
                "branch_title": "",
                "branch_ui": "",
                "cover": "",
                "type": "",
                "status": "",
                "name": ""
            }
        }
        res = requests.post(url=base_url + "/app/editor/editor-page", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_page(self):
        """Page删除页"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "page_id": ""
        }
        res = requests.post(url=base_url + "/app/editor/del-page", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_pages(self):
        """Page批量删除页"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "page_id": ""
        }
        res = requests.post(url=base_url + "/app/editor/del-pages", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_asset_music(self):
        """获取音乐"""
        data = {
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/editor/asset-music", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_asset_list(self):
        """获取素材"""
        data = {
            "asset_type": "",
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/editor/asset-list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_history(self):
        """上报常用素材"""
        data = {
            "asset_id": self.book_id,
            "asset_type": ""
        }
        res = requests.post(url=base_url + "/app/editor/add-history", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_asset_history_list(self):
        """获取常用素材列表"""
        data = {
            "asset_type": "",
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/editor/asset-history-list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_pic_editor_cmd(self):
        """图文编辑器预览接口"""
        data = {
            "book_id": self.book_id
        }
        res = requests.post(url=base_url + "/app/editor/get-pic-editor-cmd", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_pic_editor_cmd(self):
        """图文编辑器新增命令"""
        data = {
            "book_id": self.book_id
        }
        res = requests.post(url=base_url + "/app/editor/add-pic-editor-cmd", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_pic_editor_cmd(self):
        """图文编辑器编辑命令"""
        data = {
            "book_id": self.book_id,
            "chapter_id": "",
            "page_id": "",
            "index": "",
            "cmd": {
                "id": "",
                "type": "",
                "content": ""
            },
            "old_index" :""
        }
        res = requests.post(url=base_url + "/app/editor/edit-pic-editor-cmd", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_pic_editor_cmd(self):
        """图文编辑器删除命令"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "page_id": "",
            "index": ""
        }
        res = requests.post(url=base_url + "/app/editor/del-pic-editor-cmd", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_pages(self):
        """Page批量添加页"""
        data = {
            "book_id": self.book_id,
            "chapter_id": self.chapter_id,
            "node": ""
        }
        res = requests.post(url=base_url + "/app/editor/add-pages", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_user_book_num(self):
        """书本数量"""
        res = requests.post(url=base_url + "/app/editor/get-user-book-num", headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()