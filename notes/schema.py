from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note as NoteModel

class Note(DjangoObjectType):
    
    class Meta:
        model = NoteModel

        # Describe the data as a node in the graph for GraphQL
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    notes = graphene.List(Note)

    def resolve_notes(self, info):
        """Decide which notes to return"""

        user = info.context.user # User docs or debugger to find
        
        if settings.DEBUG:
            return NoteModel.objects.all()
        elif user.is_anonymous:
            return NoteModel.objects.none()
        else:
            return NoteModel.objects.filter(user=user)

# Add a schema and attach the query
schema = graphene.Schema(query=Query)
