# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .evaluation_reason import EvaluationReason

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EvaluationResponse(pydantic.BaseModel):
    request_id: str = pydantic.Field(alias="requestId")
    entity_id: str = pydantic.Field(alias="entityId")
    request_context: typing.Dict[str, str] = pydantic.Field(alias="requestContext")
    match: bool
    flag_key: str = pydantic.Field(alias="flagKey")
    segment_key: str = pydantic.Field(alias="segmentKey")
    timestamp: dt.datetime
    value: str
    request_duration_millis: float = pydantic.Field(alias="requestDurationMillis")
    attachment: str
    reason: EvaluationReason
    segment_keys: typing.Optional[str] = pydantic.Field(alias="segmentKeys")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
