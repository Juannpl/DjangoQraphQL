import graphene
from graphene_django.types import DjangoObjectType
from .models import Books

class BookType(DjangoObjectType):
    class Meta:
        model = Books

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(root, info):
        return Books.objects.all()

schema = graphene.Schema(query=Query)
