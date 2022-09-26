# Podemos utilzar el método especial  __init__ (conocido como constructor)
# y el objeto actual self para hacer un creador de objetos del tipo definido con la
# palabra reservada class
# 


class Student:
    def __init__(self,name,position,skills):
        self.name = name
        self.position = position
        self.skills = skills 
    
    def say_name(self):
        print("Mi nombre es",self.name,"Mi cargo es",self.position,"y mis habilidades son",self.skills)

Alice = Student("alice","Fullstack Developer",["Python", "Git", "HTML","CSS","Javascript"])
Bob_el_chef = Student("bob el chef","kitchen assistant",["international cuisine","pastry"])
Alice.say_name()
Bob_el_chef.say_name()



