# flask 프레임워크를 이용한, Restful API 서버 개발

from flask import Flask
from flask_restful import Api

from resources.recipe import RecipeListResource, RecipePublishResource, RecipeResource


app = Flask( __name__ )
api = Api( app )

# API를 구분해서 실행시키는 것은,
# HTTP METHOD 와 URL의 조합이다.

# 경로(Path)와 리소스(API코드)를 연결한다.
api.add_resource( RecipeListResource, '/user/register')
api.add_resource( RecipeResource , '/user/register/<int:recipe_id>')
api.add_resource( RecipePublishResource, '/user/register/<int:recipe_id>/publish')

if __name__ == '__main__' :
    app.run()

