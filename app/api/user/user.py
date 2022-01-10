# 사용자 정보 관련된 기능들을 모아두는 모듈
# app.py에서 이 함수들을 끌어다 사용

def user_test():
    
    # 추가 기능 작성
    
    # DB에서 아이디/비번을 조회해서, 로그인 확인 등등
    
    return {
        'name' : '이승훈',
        'birth_year' : 1994
    }

def login_test(id, pw):
    # 아이디 : admin / 비번 : qwer 라고 하면, 로그인 성공 응답.
    # 그 외 : 실패 처리
    
    if id == 'admin' and pw == 'qwer':
        return {
            'code' : 200,
            'message' : 'login ok'
        }
    else:
        return {
            'code' : 400,
            'message' :  'id or pw incorrect'
        }