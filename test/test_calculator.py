from models import Evaluation, AttendancePolicy, ExtraPointsPolicy
from services import GradeCalculator
import pytest

def test_shouldReturnCorrectGradeWhenNormalCase():
    evs = [
        Evaluation(15, 0.5),
        Evaluation(10, 0.5)
    ]
    att = AttendancePolicy(True)
    extra = ExtraPointsPolicy([True, True])

    calc = GradeCalculator(evs, att, extra)
    result = calc.calculate()

    expected = (15*0.5 + 10*0.5) / 1 + 1
    assert result["nota_final"] == expected


def test_shouldReturnZeroWhenNoAttendance():
    evs = [Evaluation(20, 1)]
    att = AttendancePolicy(False)
    extra = ExtraPointsPolicy([True])

    calc = GradeCalculator(evs, att, extra)
    result = calc.calculate()

    assert result["nota_final"] == 0

def test_shouldWorkWhenNoExtraPoints():
    evs = [Evaluation(20, 1)]
    att = AttendancePolicy(True)
    extra = ExtraPointsPolicy([])

    calc = GradeCalculator(evs, att, extra)
    result = calc.calculate()

    assert result["nota_final"] == 20




def test_shouldRaiseErrorWhenWeightsDontSumToOne():
    evs = [
        Evaluation(15, 0.6),
        Evaluation(10, 0.5)
    ]
    att = AttendancePolicy(True)
    extra = ExtraPointsPolicy([])

    calc = GradeCalculator(evs, att, extra)

    with pytest.raises(ValueError):
        calc.calculate()


def test_shouldRaiseErrorWhenNoEvaluations():
    att = AttendancePolicy(True)
    extra = ExtraPointsPolicy([])

    with pytest.raises(ValueError):
        GradeCalculator([], att, extra).calculate()
