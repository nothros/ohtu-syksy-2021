from matchers import And, HasAtLeast, HasFewerThan, PlaysIn, HasFewerThan, All, Or
class QueryBuilder:


    def __init__(self, query=All()):
        self.query = query
    
    def build(self):
        return self.query

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self.query))
        
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self.query))
        
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self.query))

    def oneOf(self, *matchers):
        return QueryBuilder(And(Or(matchers), self.query))
    