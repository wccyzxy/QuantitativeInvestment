
import flask
from flask_cors import cross_origin
import record


app = flask.Flask(__name__)


@app.route('/record', methods=['GET'])
@cross_origin()
def get_records():
    '''
    响应发出的json
    ---------
    {
        "status": "ok",
        "data": [
            {"Date": "xxxxx", "CashFlow": "1234"},
            ...
        ],
    }
    '''
    # username = flask.request.args['username']
    record_data = b.data.to_dict(orient='records')
    statistics = b.data.get_statistics()
    response = {
        'status': 'ok',
        'data': record_data
    }
    return response


@app.route('/record/remove', methods=['POST'])
@cross_origin()
def remove_records():
    pass


@app.route('/record/add', methods=['POST'])
@cross_origin()
def add_records():
    '''
    记账，投入或取出。

    接收到的json
    ---------
    {
        "action": "invest" | "take_back",
        "name": "str",
        "date": "yyyyddmm", 
        "cash": "1234"
    }
    '''
    recived_data = flask.request.form
    if recived_data['action'] == 'invest':
        b.invest(recived_data['date'], float(recived_data['cash']))
    elif recived_data['action'] == 'take_back':
        b.take_back(recived_data['date'], float(recived_data['cash']))
    else:
        return 'error'
    print(b.data)
    return flask.redirect('/')
    # return 'ok'


# @app.route('/')
# @cross_origin()
# def main():
#     statistics = b.get_statistics()
#     render_dict = {
#         'records': b.data,
#         'statistics': statistics
#     }
#     return flask.render_web('mainpage.html', **render_dict)


if __name__ == "__main__":
    b = record.Book('a')
    b.invest('20010101', 1000)
    b.take_back('20010501', 500)

    app.run()
