from mongoengine import Document, fields

class Prefix(Document):
    prefix = fields.StringField(required=True)
    next_char = fields.ListField(fields.StringField(),default=list)
