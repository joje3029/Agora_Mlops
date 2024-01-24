from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import os
import data_from_lib
from project.test import maria_test
import getdata_from_db
from suggest import suggest_model

# 여기서 할꺼. 기존에는 야후 파이낸스로 해서 가져오는거면 지금은 도서 데이터를 받아서 Db에 넣고
#2. 시계열이 아니라 추천을 돌려야함.

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc='/api-docs')

    test_api = api.namespace('test', description='Test API') # 콜 받는 주소
    data = api.namespace('getdata', description='데이터 get API')
    data_from_db = api.namespace('getdatafromdb', description='Getiing data from DB API')

    @test_api.route('/')
    class Test(Resource):
        def get(self):
            return "Hello World. This is Test."
    
    @data.route('/')
    class GetData(Resource): #여기를 국립중앙 도서관으로 보내게하면되겠네. // 여까지 함.
        def get(self):
            book_list_json=data_from_lib.getLib() #값 나오는거 봤으니까 이걸로 이제 머신 돌려야지.
            suggest_model(book_list_json)
            #suggest.py에 저 json을 넘기고.
            # suggest.py는 json을 판다스화 해서 일하고 오케
            return 
        
    @data_from_db.route('/') 
    class GetDataFromDB(Resource):
        def get(self):
            s = request.args.get('s',1,str)
            e = request.args.get('e',1,str)
            print(s, e, type(s))
            return getdata_from_db.getdata_from_db(s, e)

    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 9999)), debug=True)