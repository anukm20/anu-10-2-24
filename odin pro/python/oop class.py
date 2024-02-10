""""""
# class vehicle:
#     door=5
#     wheel=4
#     def start(self):
#         print("engine start")
# car=vehicle()
# car.start()




# class vehicle:
#      door=5
#      wheel=4
#      def start(self,a,b):
#          print(a+b,"engin start")
# car=vehicle() 
# car.start(20,2)



# class vehicle:
#     color="red"
#     def show(self):
#         print("color is: ",self.color)
# car=vehicle()
# car.show()



# class vehicle:
#     def selector(self,color):
#         self.color=color
#     def show(self):
#         print("color is: ",self.color)
# car=vehicle()
# car.selector("red")
# car.show()


# class vehicle:
#     def __init__(self,color,tyre):
#         self.color=color
#         self.tyre=tyre
#     def show(self):
#         print("color is",self.color,"tyre is",self.tyre)
# car=vehicle("red",4)
# car.show()


# class animal:
#     def __init__(self,legs,color,eyes):
#         self.legs=legs
#         self.color=color
#         self.eyes=eyes
#     def show(self):
#         print("legs is: ",self.legs,"color is: ",self.color,"eyes is: ",self.eyes)
# pet_animal=animal(4,"white",2)
# wild_animal=animal(4,"black",2)
# pet_animal.show()
# wild_animal.show()



# class vehicle:
#     color="red"
#     def engine(self):
#         print("all vehicle have engine")
# class car(vehicle):
#     def fourwheel(self):
#         print("car have 4 wheel",self.color)
# c=car()
# c.fourwheel()
# c.engine()


"""multilevel"""
# class granpa:
#     def kashandi(self):
#         print("kashandi family")
#     def farmer(self):
#         print("farmer")
# class father(granpa):
#     def driver(self):
#         print("driver")
#     def reader(self):
#         print("reader")
# class me(father):
#     def swimming(self):
#         print("swimming")
#     def engineer(self):
#         print("engineer")
# class mechild(me):
#     def gamer(self):
#         print("gamer")
# ob=father()
# ob.farmer()

"""multiole inheritance"""
# class father:
#     def driver(self):
#         print("driver")
# class mother:
#     def cook(self):
#         print("cook")
# class girl(father,mother):
#     def engineer(self):
#         print("engineer")
# g=girl()
# g.driver()
# g.cook()
# g.engineer()


"""prgm"""
class libraryitem:
    def title(self):
        print("voice of nature")
    def author(self):
        print("mark john")
    def id(self):
        print(201202) 
class book(libraryitem):
    def no_of_pages(self):
        print("420")
    def read_book(self):
        print("reading the book")
class dvd(libraryitem):
    def duration(self):
        print("4 hours")
    def dvd_play(self):
        print("playing the dvd")

b=book()
b.author()
b.id()
b.no_of_pages()
b.read_book()
b.title()

c=dvd()
c.duration()
c.dvd_play()
             


 
"""encapsulation private"""
# class bank:
#     def __init__(self,accno,__savings):
#         self.accno=accno
#         self.savings=__savings
#     def deposit(self,dep):
#         self.savings+=dep
#     def display(self):
#         print("savings=",self.savings)
        
# akku=bank(9995833724,10000)
# akku.deposit(2000)
# akku.display()


"""protected"""
# class A:
#     _a=10
#     def disp(self):
#         print(self._a)
# obj=A()
# obj.disp()
# print(obj._a)



"""abstract"""
# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     def engine(self):
#         print("engine provide")
#     @abstractmethod
#     def gear(self):
#         pass
# class car(vehicle):
#     def gear(self):
#         print("automatic gear")
# class truck(vehicle):
#     def wheel(self):
#         print("heavy")
#     def gear(self):
#         print("manuel gear")
# akku=car()
# akku.gear()
# ar=truck()
# ar.gear()
  
        





























