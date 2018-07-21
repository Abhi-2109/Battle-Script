#This will coinatin some shop, iems which will make it as entirely action role playing game



class Item :

    #here the items should have its name type and description and propperty like potion type which will do heal

    def __init__(self, name, type, description, prop):
        self.name = name
        self.type =type
        self.description = description
        self.prop =prop