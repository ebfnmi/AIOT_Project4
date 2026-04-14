from flask import Flask, request, render_template # 웹 서버를 만들기 위한 도구(Flask)와 사용자의 요청을 읽는 도구(request), 화면을 보여주는 도구(render_template)를 가져온다.
from gpiozero import LED # LED를 켜고 끄기 위한 도구를 가져온다.

app = Flask(__name__) # 서버 객체를 생성한다.

red_led = LED(21) # GPIO 21번 핀에 연결된 LED를 제어한다.

@app.route('/') # 웹 사이트의 기본이 되는 주소이다. 
def home(): # / 기본 경로로 들어오면 실행되는 함수이다.
   return render_template("index.html") # template 폴더 안에 있는 index.html 파일을 열어서 보여준다. 

@app.route('/data', methods = ['POST']) # /data 주소로 POST 요청이 들어오면 실행한다.
def data(): # /data 주소로 신호를 보내면 실행되는 함수이다. 
    data = request.form['led'] # 사용자가 누른 버튼의 값(on 또는 off)이 무엇인지 읽어서 data라는 변수에 저장한다. 
    
    if(data == 'on'): # request.form['led']를 통해 가져온 값이 on인지 확인하는 조건문이다. 
        red_led.on() # 위의 조건이 맞다면 gpiozero 라이브러리를 통해 라즈베리 파이 21번 핀에 전압을 가하고 LED의 불이 들어오게 된다. 
        return home() # LED를 킨 직후에 다시 home() 함수를 호출하고, on 버튼을 눌렀을 때 원래의 제어 화면(index.html)을 띄운다.

    elif(data == 'off'): # request.form['led']를 통해 가져온 값이 off인지 확인하는 조건문이다. 
        red_led.off() # 위의 조건이 맞다면 gpiozero 라이브러리를 통해 라즈베리 파이 21번 핀에 전압을 차단하여 LED의 불이 소등된다.
        return home() 

if __name__ == '__main__': # 터미널에서 실행했을 때만 작동이 되게 한다. 
   app.run(host = '0.0.0.0', port = '80') # 모든 IP(0.0.0.0)에서 80번 포트로 실행한다.