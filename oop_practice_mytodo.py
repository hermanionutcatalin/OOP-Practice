"""
Atribute:to do (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în to do list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""


class MyToDo:
    dict = {}

    def add_task(self, key, value):
        self.dict[key] = value

    def finalize_task(self, task):
        del self.dict[task]

    def display_todo(self):
        for item in self.dict.keys():
            print(item)

    def display_supplementary(self, task):
        if task in self.dict.keys():
            print(self.dict[task])
        else:
            x=input('Would you like to add this task as not in MyToDo Y/N:')

            if x.lower()=='n':
                print('Goodbye')

            elif x.lower()=='y':
                v=input('Please enter task description: ')
                self.dict[task]=v

            else:
                print('Please enter valid result')

my_dict=MyToDo()
my_dict.add_task("shopping","merg la Lidl")
my_dict.add_task("walk","merg in Tineretului")
my_dict.display_supplementary('walk')
my_dict.display_todo()
my_dict.finalize_task('shopping')
my_dict.display_todo()

