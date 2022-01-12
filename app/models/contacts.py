# DB에 있는, contacts 테이블을 표현하는 클래스

class Contacts():
    # 생성자 -> dict를 넣으면 객체 변수를 자동 세팅
    
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.phone = data_dict['phone_num'] # DB의 컬럼 : phone_num, 변수이름 : phone
        self.memo = data_dict['memo']
        self.created_at = data_dict['created_at']