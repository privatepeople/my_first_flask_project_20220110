from pymysql import connect
from pymysql.cursors import DictCursor

# 사용자 정보 관련된 기능들을 모아두는 모듈
# app.py에서 이 함수들을 끌어다 사용

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

def user_test():
    
    # 추가 기능 작성
    
    # DB에서 아이디/비번을 조회해서, 로그인 확인 등등
    
    return {
        'name' : '이승훈',
        'birth_year' : 1994
    }

def login_test(id, pw):
    # id, pw를 이용해서 -> SQL 쿼리 작성 -> 결과에 따라 다른 응답 리턴
    
    sql = f"SELECT * FROM users WHERE email='{id}' AND password='{pw}'"
    cursor.execute(sql)
    
    query_result = cursor.fetchone()
    
    # 쿼리 결과 : None -> 아이디 비번 맞는 사람 X -> 로그인 실패.
    
    if query_result == None:
        return {
            'code': 400,
            'message': '아이디 또는 비밀번호가 잘못되었습니다.'
        }, 400
    else:
        # 검색 결과가 있다 => 아이디/비번 모두 맞는 사람 O -> 로그인 성공
        # query_result가 실체가 있다. (None이 아니다.)
        
        print(query_result)
        
        user_dict = {
            'id': query_result['id'],
            'email': query_result['email'],
            'nickname': query_result['nickname']
        }
        
        return {
            'code': 200,
            'message': '로그인 성공',
            'data': {
                'user': user_dict,
            }
        }
        
# 회원가입 담당 함수
# 1. 이메일이 이미 사용중이라면? -> 400으로 에러처리
# 2. 닉네임도 사용중이라면? -> 400으로 에러처리
# 둘 다 통과해야만 실제 INSERT INTO -> 결과를 200으로 내려주자 + 가입된 사용자 정보도 내려주자.


def sign_up(params):
    
    # 이메일이 사용중인지? 검사
    # params['email']와 같은 이메일이 DB에 있는지? 조회=> SELECT
    sql = f"SELECT * FROM users WHERE email='{params['email']}'"
    
    cursor.execute(sql)
    email_check_result = cursor.fetchone() # 같은 이메일이 하나라도 있는지?
    
    if email_check_result:
        # 이메일 검사 쿼리 결과가 => None이 아닌가? (실체가 있나?)
        # 있다면? 이미 이메일이 사용 중이다. => 등록 X.
        return {
            'code': 400,
            'message': '이미 사용중인 이메일입니다.'
        }, 400
    
    sql = f"INSERT INTO users (email, password, nickname) VALUES ('{params['email']}', '{params['pw']}', '{params['nick']}'); "
    
    print(f'완쉉된 쿼리 : {sql}')
    
    cursor.execute(sql)
    db.commit()
    
    return {
        'test': 'test'
    }