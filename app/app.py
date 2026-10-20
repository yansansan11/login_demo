from flask import Flask, request, jsonify, render_template, redirect, session, url_for

app = Flask(__name__, template_folder="../templates")
app.secret_key ="test-secret-key"

USERS = {"admin":"123456"}


@app.route("/", methods=["GET"])
def login_page():
    return render_template("login.html")
@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"code":1001, "msg":"用户名或密码不能为空"}), 400
    if USERS.get(username) == password:
        session["user"] = username
        return jsonify({"code":200, "msg":"登录成功"})
    return jsonify({"code":1002, "msg":"用户名或密码错误"}), 401

@app.route("/home", methods=["GET"])
def home():
    if "user" not in session:
        return redirect(url_for("login_page"))
    return render_template("home.html", user=session["user"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
