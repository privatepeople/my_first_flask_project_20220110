from pymysql import connect
from pymysql.cursors import DictCursor

from app.api import contact

# 연락처에 관련된 로직을 담당하는 파일
# db 연결 / cursor 변수
db = connect(
    host='finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='admin',
    passwd='Vmfhwprxm!123',
    db='test_phone_book',
    charset='utf8',
    cursorclass=DictCursor
)

cursor = db.cursor()


def add_contact_to_db(params):
    
    # 사전 검사 : user_id 파라미터의 값이, 실제 사용자 id가 맞는지? 그런 사용자 있는지?
    sql = f"SELECT * FROM users WHERE id = {params['user_id']}"
    cursor.execute(sql)
    
    user_result = cursor.fetchone()
    
    if user_result == None:
        return {
            'code': 400,
            'message': '해당 사용자 id값은 잘못되었습니다.'
        }, 400
    
    # 연락처 추가 등록 쿼리
    sql = f"INSERT INTO contacts (user_id, name, phone_num, memo) VALUES ({params['user_id']}, '{params['name']}', '{params['phone']}', '{params['memo']}')"
    
    cursor.execute(sql)
    db.commit()
    
    return {
        'code': 200,
        'message': '임시 성공 응답',
    }
    
def get_contacts_from_db(params):
    # 기본 : 해당 사용자의 모든 연락처를 목록으로 리턴
    # 응용1 : 파라미터에 최신순/이름순 정렬 순서를 받자 => 그에 맞게 리턴
    # => 이 파라미터는 첨부되지 않을 수도 있다.
    # 응용2 : 한번에 10개씩만 내려주자. (게시판처럼 페이징 처리)
    
    sql = f"SELECT * FROM contacts WHERE user_id = {params['user_id']}"
    
    # order_type 파라미터가 실제로 올때만 추가 작업
    if 'order_type' in params.keys():
        order_type = params['order_type']
        if order_type == '최신순':
            sql = f"{sql} ORDER BY created_at DESC" # 기존 쿼리 뒤에, ORDER BY created_at DESC 추가
        elif order_type == '이름순':
            sql = f"{sql} ORDER BY name" # 기존 쿼리 뒤에, ORDER BY name 추가
            
    
    # 페이지의 번호가 들어온다면? => 일정 갯수만큼 남기고, 그 다음 n개
    if 'page_num' in params.keys():
        page_num = int(params['page_num'])
        
        # 0페이지 : 0개를 넘기고, 그 다음 2개
        # 1페이지 : 2개 넘기고, 그 다음 2개
        # 2페이지 : 4개 넘기고, 그 다음 2개 -> 넘기는 갯수 : page_num *2, 보여주는 갯수 : 무조건 2개
        sql = f"{sql} LIMIT {page_num * 2}, 2"
            
    print(sql)
    
    cursor.execute(sql)
    
    # DB의 실행 결과 목록이 담긴 변수
    query_result = cursor.fetchall()
    
    # 클라이언트에게 전해줄 목록
    contacts_arr = []

    # DB실행결과 한줄 => (가공) => 클라이언트에게 전해줄 목록에 담기도록.
    for row in query_result:
        # 클라이언트가 받아들이기 편리한 구조로 가공된 연락처를 담을 dict
        contact = {}
        # contact의 내용을 채우자
        contact['id'] = row['id']
        contact['name'] = row['name']
        contact['phone_num'] = row['phone_num']
        contact['memo'] = row['memo']
        
        # datetime으로 오는 데이터를 -> str로 가공해서 담아보자.
        # datetime -> str : strftime 활용 (2022-01-08 01:01:00 양식)
        contact['created_at'] = row['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        # 내용이 채워진 contact를 리스트에 추가
        contacts_arr.append(contact)
    
    return {
        'code': 200,
        'message': '내 연락처 목록',
        'data': {
            'contacts': contacts_arr # 리스트를 통째로 응답으로 -> JSONArray를 응답으로
        }
    }
    
    
# 키워드를 가지고 검색하는 기능. '경' => 조경진, 박진경 등등.. 경자가 포함되면 리턴. + 본인이 가진 연락처 중
def search_contact(params):
    sql = f"SELECT * FROM contacts WHERE name LIKE '%{params['keyword']}%'"
    
    cursor.execute(sql)
    
    search_list = cursor.fetchall()

    print(search_list)

    return {
        '임시' : '임시'
    }