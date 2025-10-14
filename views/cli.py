
from controllers.task_controller import TaskController as Controller


class CLI:
    def __init__(self, controller: Controller):
        self.controller = controller

    def run(self):
        # examples
        self.controller.ajouter("Apprendre Python")
        self.controller.ajouter("Faire les courses")

        while True:
            print("\n" + "=" * 30)
            print("1. Ajouter  2. Afficher")
            print("3. Terminer  4. Supprimer  0. Quitter")
            print("=" * 30)

            choix = input("Choix: ")

            if choix == "1":
                titre = input("Titre: ")
                if titre:
                    t = self.controller.ajouter(titre)
                    print(f"✓ Tâche ajoutée: {t.titre}")

            elif choix == "2":
                taches = self.controller.lister()
                if not taches:
                    print("Aucune tâche")
                for t in taches:
                    print(t)

            elif choix == "3":
                try:
                    id = int(input("ID: "))
                    if self.controller.terminer(id):
                        print(f"✓ Tâche {id} terminée")
                    else:
                        print(f"❌ Tâche {id} introuvable")
                except Exception:
                    print("❌ ID invalide")

            elif choix == "4":
                try:
                    id = int(input("ID: "))
                    if self.controller.supprimer(id):
                        print(f"✓ Tâche {id} supprimée")
                    else:
                        print(f"❌ Tâche {id} introuvable")
                except Exception:
                    print("❌ ID invalide")

            elif choix == "0":
                print("Au revoir!")
                break
