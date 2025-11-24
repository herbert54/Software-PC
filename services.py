from models import Evaluation, AttendancePolicy, ExtraPointsPolicy

class GradeCalculator:
    MAX_EVALUATIONS = 10

    def __init__(self, evaluations: list[Evaluation],
                 attendance_policy: AttendancePolicy,
                 extra_points_policy: ExtraPointsPolicy):
        
        self.evaluations = evaluations
        self.attendance_policy = attendance_policy
        self.extra_points_policy = extra_points_policy

    def calculate(self) -> dict:
        # RNF01: no más de 10 evaluaciones
        if len(self.evaluations) > self.MAX_EVALUATIONS:
            raise ValueError("No se permiten más de 10 evaluaciones.")

        total_weight = sum(e.weight for e in self.evaluations)

        if total_weight <= 0:
            raise ValueError("La suma de pesos debe ser mayor a 0.")

        # Cálculo del promedio ponderado
        weighted_sum = sum(e.grade * e.weight for e in self.evaluations)
        promedio = weighted_sum / total_weight

        # Aplicar asistencia
        final_grade = self.attendance_policy.apply_penalty(promedio)

        # Agregar puntos extra
        extra = self.extra_points_policy.extra_points()
        final_grade += extra

        return {
            "promedio_ponderado": promedio,
            "puntos_extra": extra,
            "asistencia_minima": self.attendance_policy.has_minimum,
            "nota_final": final_grade
        }
