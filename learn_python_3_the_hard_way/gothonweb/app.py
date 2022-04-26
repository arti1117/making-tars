from flask import Flask, session, redirect, url_for, excape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)

@app.route("/")
def index():
    # 시작할 때 세션에 시작 값을 미리 넣어둔다
    session['방_이름'] = planisphere.시작_이름
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    방_이름 = session.get('방_이름')

    if request.method == "GET":
        if 방_이름:
            방 = planisphere.방_가져오기(방_이름)
            return render_template("show_room.html", 방=방)
        else:
            # 왜 여기 넣었을까요? 꼭 필요한가요?
            return render_template("you_died.html")
    else:
        행동 = request.form.get('action')

        if 방_이름 and 행동:
            방 = planisphere.방_가져오기(방_이름)
            다음_방 = 방.이동(행동)

            if not 다음_방:
                session['방_이름'] = planisphere.방_이름(방)
            else:
                session['방_이름'] = planisphere.방_이름(다음_방)

        return redirect(url_for("game"))

# @app.route('/hello', methods=['POST', 'GET'])
# def index():
#     인사말 = "Hello World"
# 
#     if request.method == "POST":
#         이름 = request.form['name']
#         인사 = request.form['greet']
#         인사말 = f'{인사}, {이름}'
#         return render_template("index.html", 인사말=인사말)
#     else:
#         return render_template("hello_form.html")

# 인터넷에 올리려면 secret_key를 반드시 변경해야 합니다.
app.secret_key = 'AD(@#UF_*$()#WEJDHFJKUJCKE'

if __name__ == "__main__":
    app.run()

