# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EvaluationReason(str, enum.Enum):
    UNKNOWN_EVALUATION_REASON = "UNKNOWN_EVALUATION_REASON"
    FLAG_DISABLED_EVALUATION_REASON = "FLAG_DISABLED_EVALUATION_REASON"
    FLAG_NOT_FOUND_EVALUATION_REASON = "FLAG_NOT_FOUND_EVALUATION_REASON"
    MATCH_EVALUATION_REASON = "MATCH_EVALUATION_REASON"
    ERROR_EVALUATION_REASON = "ERROR_EVALUATION_REASON"

    def visit(
        self,
        unknown_evaluation_reason: typing.Callable[[], T_Result],
        flag_disabled_evaluation_reason: typing.Callable[[], T_Result],
        flag_not_found_evaluation_reason: typing.Callable[[], T_Result],
        match_evaluation_reason: typing.Callable[[], T_Result],
        error_evaluation_reason: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EvaluationReason.UNKNOWN_EVALUATION_REASON:
            return unknown_evaluation_reason()
        if self is EvaluationReason.FLAG_DISABLED_EVALUATION_REASON:
            return flag_disabled_evaluation_reason()
        if self is EvaluationReason.FLAG_NOT_FOUND_EVALUATION_REASON:
            return flag_not_found_evaluation_reason()
        if self is EvaluationReason.MATCH_EVALUATION_REASON:
            return match_evaluation_reason()
        if self is EvaluationReason.ERROR_EVALUATION_REASON:
            return error_evaluation_reason()
