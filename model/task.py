

class Task:

    _id = 0

    def __init__(self, titre: str):
        Task._id += 1
        self.id = Task._id
        self.titre = titre
        self.fait = False

    def __str__(self) -> str:
        statut = "✓" if self.fait else "○"
        return f"[{self.id}] {statut} {self.titre}"
