


class Task:
    _id = 0
    
    def __init__(self, titre):
        Task._id += 1
        self.id = Task._id
        self.titre = titre
        self.fait = False
    
    def __str__(self):
        statut = "✓" if self.fait else "○"
        return f"[{self.id}] {statut} {self.titre}"


class TodoList:
    
    
    def __init__(self):
        self.taches = []
    
    def ajouter(self, titre):
        task = Task(titre)
        self.taches.append(task)
        print(f"✓ Tâche ajoutée: {titre}")
    
    def afficher(self):
        if not self.taches:
            print("Aucune tâche")
        for t in self.taches:
            print(t)
    
    def terminer(self, id):
        for t in self.taches:
            if t.id == id:
                t.fait = True
                print(f"✓ Tâche {id} terminée")
                return
        print(f"❌ Tâche {id} introuvable")
    
    def supprimer(self, id):
        for t in self.taches:
            if t.id == id:
                self.taches.remove(t)
                print(f"✓ Tâche {id} supprimée")
                return
        print(f"❌ Tâche {id} introuvable")


def main():
    todo = TodoList()
    
    todo.ajouter("Apprendre Python")
    todo.ajouter("Faire les courses")
    
    while True:
        print("\n" + "="*30)
        print("1. Ajouter  2. Afficher")
        print("3. Terminer  4. Supprimer  0. Quitter")
        print("="*30)
        
        choix = input("Choix: ")
        
        if choix == "1":
            titre = input("Titre: ")
            if titre:
                todo.ajouter(titre)
        
        elif choix == "2":
            todo.afficher()
        
        elif choix == "3":
            try:
                id = int(input("ID: "))
                todo.terminer(id)
            except:
                print("❌ ID invalide")
        
        elif choix == "4":
            try:
                id = int(input("ID: "))
                todo.supprimer(id)
            except:
                print("❌ ID invalide")
        
        elif choix == "0":
            print("Au revoir!")
            break


if __name__ == "__main__":
    main()