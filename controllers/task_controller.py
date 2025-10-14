
from typing import List
from model.task import Task


class TaskController:
    def __init__(self):
        self.taches: List[Task] = []

    def ajouter(self, titre: str) -> Task:
        task = Task(titre)
        self.taches.append(task)
        return task

    def lister(self) -> List[Task]:
        return list(self.taches)

    def terminer(self, id: int) -> bool:
        for t in self.taches:
            if t.id == id:
                t.fait = True
                return True
        return False

    def supprimer(self, id: int) -> bool:
        for t in self.taches:
            if t.id == id:
                self.taches.remove(t)
                return True
        return False
