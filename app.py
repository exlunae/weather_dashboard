from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def main():
    return redirect('/index')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/info', methods=['POST', 'GET'])
def info():
    # if request.method == 'POST':
    info = request.form
    return render_template('info.html', info=info)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')  


if __name__ == "__main__":
    app.run(debug=True)