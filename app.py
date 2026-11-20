from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "kunci_rahasia_project_semester_1"

# Data akun login disimpan menggunakan Tuple / Dictionary (Materi Pertemuan 2 & 6)
AKUN_USER = ("faridngentod", "zaki123")


def cek_login(input_user, input_pass):
    """Fungsi untuk memeriksa kecocokan username dan password (Materi Pertemuan 4 & 9)"""
    if input_user == AKUN_USER[0] and input_pass == AKUN_USER[1]:
        return True
    else:
        return False


@app.route("/")
def index():
    # Jika sudah login, langsung ke dashboard
    if "username" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    pesan_error = ""

    # Percabangan jika tombol Login ditekan (method POST)
    if request.method == "POST":
        username_input = request.form["username"]
        password_input = request.form["password"]

        # Memanggil fungsi cek_login
        if cek_login(username_input, password_input) == True:
            session["username"] = username_input
            return redirect(url_for("dashboard"))
        else:
            pesan_error = "Username atau Password salah! Silakan coba lagi."

    return render_template("login.html", pesan_error=pesan_error)


@app.route("/dashboard")
def dashboard():
    # Cek apakah user sudah login menggunakan operator keanggotaan 'not in' (Materi Pertemuan 3)
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", username=session["username"])


@app.route("/logout")
def logout():
    # Menghapus session saat log out
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
