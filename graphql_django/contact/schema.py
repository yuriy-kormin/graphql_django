import graphene
from graphene_django import DjangoObjectType
# used to change Django object into a format that is readable by GraphQL
from .models import Contact


class ContactType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        model = Contact
        field = ("id", "name", "phone_number")


class Query(graphene.ObjectType):
    listing = graphene.List(ContactType)
    get_by_id = graphene.Field(ContactType, id=graphene.Int())

    def resolve_listing(root, info):
        # We can easily optimize query count in the resolve method
        return Contact.objects.all()

    def resolve_get_by_id(root, info, id):
        return Contact.objects.get(id=id)


class ContactMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        phone_number = graphene.String()

    contact = graphene.Field(ContactType)
    # define the class we are getting the fields from

    @classmethod
    def mutate(cls, root, info, name, phone_number):
        # function that will save the data
        contact = Contact(name=name, phone_number=phone_number)
        contact.save()
        return ContactMutation(contact=contact)


class Mutation(graphene.ObjectType):
    create_contact = ContactMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
