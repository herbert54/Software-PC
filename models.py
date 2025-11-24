class Evaluation:
    def __init__(self, grade: float, weight: float):
        if weight < 0:
            raise ValueError("El peso no puede ser negativo.")
        if grade < 0 or grade > 20:
            raise ValueError("La nota debe estar entre 0 y 20.")
        
        self.grade = grade
        self.weight = weight


class AttendancePolicy:
    def __init__(self, has_minimum: bool):
        self.has_minimum = has_minimum

    def apply_penalty(self, grade: float) -> float:
        """
        Si no cumple asistencia mínima -> Nota final = 0
        """
        return grade if self.has_minimum else 0.0


class ExtraPointsPolicy:
    def __init__(self, teachers_agreement: list[bool]):
        self.teachers_agreement = teachers_agreement

    def extra_points(self) -> float:
        """
        Si todos los docentes están de acuerdo -> +1 punto
        """
        return 1.0 if all(self.teachers_agreement) else 0.0
