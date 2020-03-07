from flask import Flask
from flask_celery import make_celery
from send import Publish

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] =   'amqp://localhost//'
app.config['CELERY_BACKEND'] = 'redis://localhost:6379'

celery = make_celery(app)

@app.route("/processo/<tag>")
def processo(tag):
    testando.delay(tag)
    envia = Publish('localhost','start_rubicon_job','rubicon')
    envia.send()
    envia.close_comm()
    return {"message":"start_rubicon_job"}

@celery.task(name='celery_example.testando',)
def testando(string):
    return {"message":"TETANDO RECEBEU: "+string}





if __name__ == "__main__":
    app.run(debug=True)
