from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def missionname():
    return "<h1><b>Миссия Колонизация Марса</b></h1>"


@app.route('/index')
def devizz():
    return "<h2><b><i>И на Марсе будут яблони цвести!</i></b></h2>"


@app.route('/promotion')
def promotion():
    text = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']
    return ''.join([f'<h2><i>{i}</i></h2>' for i in text])


@app.route('/image_mars')
def bootstrap_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1></br>
                    <img src="{url_for('static', filename='img/marss.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась"></br>
                    Вот она какая, красная планета.                        
                  </body>
                </html>'''


@app.route('/promotion_image')
def bootstrap_image_prom():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1></br>
                    <img src="{url_for('static', filename='img/marss.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась"></br>
                    <h3>Человечество вырастает из детства.</br></h3>
                    <h3>Человечеству мала одна планета.</br></h3>
                    <h3>Мы сделаем обитаемыми безжизненные пока планеты.</br></h3>
                    <h3>И начнем с Марса!</br></h3>
                    <h3>Присоединяйся!</h3>                   
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')