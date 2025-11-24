from models import Evaluation, AttendancePolicy, ExtraPointsPolicy
from services import GradeCalculator

def main():
    print("\n=== MÓDULO DE CÁLCULO DE NOTA FINAL - UTEC ===\n")

    evaluations = []

    n = int(input("Cantidad de evaluaciones: "))

    for i in range(n):
        grade = float(input(f"Nota {i+1}: "))
        weight = float(input(f"Peso {i+1}: "))
        evaluations.append(Evaluation(grade, weight))

    # Asistencia
    asistencia = input("¿Cumplió asistencia mínima? (s/n): ").strip().lower()
    attendance_policy = AttendancePolicy(asistencia == "s")

    # Puntos extra
    teachers = input("Acuerdo de docentes (ejemplo: T,F,T,T): ")
    teachers_bool = [t.strip().upper() == "T" for t in teachers.split(",")]
    extra_policy = ExtraPointsPolicy(teachers_bool)

    # Calcular
    calc = GradeCalculator(evaluations, attendance_policy, extra_policy)
    resultado = calc.calculate()

    print("\n===== RESULTADOS =====")
    print("Promedio ponderado :", resultado["promedio_ponderado"])
    print("Puntos extra        :", resultado["puntos_extra"])
    print("Asistencia mínima   :", resultado["asistencia_minima"])
    print("Nota final          :", resultado["nota_final"])
    print("======================\n")

if __name__ == "__main__":
    main()
