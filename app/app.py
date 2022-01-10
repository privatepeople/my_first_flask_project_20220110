from flask import Flask, jsonify
from flask.templating import render_template

def create_app():
    # 플라스크 서버를 변수에 담자.
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행
    
    @app.route("/") # 만들고있는 서버의 / (아무것도 안붙인 주소) 로 접속하면 보여줄 내용
    def home():
        # return 내용 : HTML 등 웹 프로트엔트 태그.
        return "<h1>Hello World!!<h1>" # Hello World 문장 리턴 => 이 내용을 사용자에게 보여주겠다.
    
    @app.route("/test") # 서버의 /test 주소로 오면 수행해줄 일을 작성
    def test():
        return "이곳은 테스트 페이지입니다."
    
    @app.route("/web")
    def web_test():
        return render_template('web_test.html') # templates 폴더 내부의 파일을 불러주는 역할.
    
    @app.route("/json")
    def json_test():
        # JSON : 양식 = "이름표" : 실제 값의 조합. => dict를 이용하면 작업이 편하다.
        test_dict = {}
        test_dict['name'] = '이승훈'
        test_dict['birth_year'] = 1994
        test_dict['height'] = 174.4
        test_dict['is_male'] = True
        
        return jsonify(test_dict) # dict -> json 변경 함수 활용, JSON 응답 내려주기
    
    # 이 서버를 사용하도록 결과로 내보내자.
    return app