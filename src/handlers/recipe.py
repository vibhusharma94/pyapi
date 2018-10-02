from src.common.mixins import HttpHandler
from src.web.response import Response
from src.validators import RecipeSchema, RatingSchema
from src.common.constants import status
from src.models import (
    Recipe, RecipeRating)
from src.utils import (
    auth_enabled, get_object_or_404,
    get_paginated_response)



class RecipeRatingHandler(HttpHandler):

    methods = ['post']

    def post(self, request, pk=None):
        obj = get_object_or_404(self.db_session, Recipe, pk=pk)
        schema = RatingSchema()
        if schema.is_valid(request.data):
            instance = RecipeRating(value=schema.data['value'], recipe_id=obj.id)
            self.db_session.add(instance)
            self.db_session.commit()
            return Response(content=instance.to_dict(), status=status.HTTP_STATUS_201)
        return Response(content=schema.errors, status=status.HTTP_STATUS_400)
        

class RecipeHandler(HttpHandler):
    """
    Implements CRUD Apis. 
    """
    methods = ['get' , 'post', 'put', 'delete']

    def list(self, request):
        """
        Returns paginated response. Supports filters.
        """
        params = dict((k, request.args.get(k, '')) for k in \
                ('name', 'preptime', 'difficulty',  'vegetarian') \
                 if request.args.get(k))
        search_string = params.pop('name', '')
        query = self.db_session.query(Recipe).filter_by(**params)
        if search_string:
            query = query.filter(Recipe.name.startswith(search_string)).all()
        
        resp = get_paginated_response(query, request)
        return Response(content=resp, status=status.HTTP_STATUS_200)

    def get(self, request, pk=None):
        obj = get_object_or_404(self.db_session, Recipe, pk=pk)
        data = obj.to_dict()
        data['avg_rating'] = obj.avg_rating
        return Response(content=data, status=status.HTTP_STATUS_200)

    @auth_enabled
    def post(self, request):
        schema = RecipeSchema()
        if schema.is_valid(request.data):
            instance = Recipe(**schema.data)
            self.db_session.add(instance)
            self.db_session.commit()
            return Response(content=instance.to_dict(), status=status.HTTP_STATUS_201)
        return Response(content=schema.errors, status=status.HTTP_STATUS_400)

    @auth_enabled
    def put(self, request, pk=None):
        obj = get_object_or_404(self.db_session, Recipe, pk=pk)
        schema = RecipeSchema()
        if schema.is_valid(request.data):
            for key, value in schema.data.items():
                setattr(obj, key, value)
            self.db_session.commit()
            return Response(content=obj.to_dict())
        return Response(status=status.HTTP_STATUS_400)
        
    @auth_enabled
    def delete(self, request, pk=None):
        obj = get_object_or_404(self.db_session, Recipe, pk=pk)
        self.db_session.delete(obj)
        self.db_session.commit()
        return Response(status=status.HTTP_STATUS_204)

