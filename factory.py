from flyweight import ChessPieceFlywight
class ChessPieceFactory:
    _flyweights={}
    @classmethod

    def get_flyweight(cls,name, color):
        key=(name,color)
        if not cls._flyweights.get(key):
            cls._flyweights[key]= ChessPieceFlywight(name,color)
        print(cls._flyweights)
        return cls._flyweights[key]

