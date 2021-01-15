"""define class and it's attributes

class Card that inherits from Symbol and add an attribute:

value which is a string (one of )"""
class Symbol(self,color,icon):

    def __init__(self,color,icon):
        self.color = ["Red","Black"]
        self.icon = ["♥", "♦", "♣", "♠"]

#class get inheritance from Symbol and assigns an value
class Card(Symbol):
    def __init__(self,color,icon,value):
        Symbol.__init__(self,color,icon):
        self.value["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
