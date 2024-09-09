class ChessPieceFlywight:
    def __init__(self,name,color) -> None:
        self.name=name
        self.color=color
    def display (self,position):
        print(f"Displaying{self.name}{self.color}at {position}")
        