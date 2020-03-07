from flask import Flask
from flask_celery import make_celery


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] =   'amqp://localhost//'
app.config['CELERY_BACKEND'] = 'redis://localhost:6379'

celery = make_celery(app)

@app.route("/processo/<tag>")
def processo(tag):
    testando.delay(tag)
    return {"message_producer":"_uuuuu async sexy guy >///<"}

@celery.task(name='celery_example.testando')
def testando(string):
    return {"message":"TETANDO RECEBEU: "+string}





if __name__ == "__main__":
    app.run(debug=True)
