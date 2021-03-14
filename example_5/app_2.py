from flask import Flask, render_template


app = Flask('__name__')


@app.route('/')
def index():
    return 'je suis la page index'

@app.route('/<page>')
def page(page):
    return 'je suis la page {}'.format(page)


@app.route('/index/<page>')
def index_1(page):
    return render_template('index.html', text=page)

if __name__ == '__main__':
    app.run(debug=True)