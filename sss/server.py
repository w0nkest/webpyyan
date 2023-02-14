from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', defaults={'title': 'insert text'})
@app.route('/<title>')
@app.route('/index', defaults={'title': 'insert text'})
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training', defaults={'prof': 'да'})
@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        return render_template('picture.html', type='Инженерные тренажеры',
                               src=f'{url_for("static", filename="img/milleniumfalconit.png")}')
    return render_template('picture.html', type='Научные симуляторы',
                           src=f'{url_for("static", filename="img/milleniumfalconns.png")}')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')