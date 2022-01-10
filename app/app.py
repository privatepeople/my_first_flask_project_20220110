from flask import Flask

def create_app():
    # 플라스크 서버를 변수에 담자.
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행
    
    @app.route("/") # 만들고있는 서버의 / (아무것도 안붙인 주소) 로 접속하면 보여줄 내용
    def test():
        return "<h1>Hello World!!<h1>" # Hello World 문장 리턴 => 이 내용을 사용자에게 보여주겠다.
    
    # 이 서버를 사용하도록 결과로 내보내자.
    return app