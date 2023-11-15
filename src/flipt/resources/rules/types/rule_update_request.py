# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .rule_segment_operator import RuleSegmentOperator

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RuleUpdateRequest(pydantic.BaseModel):
    segment_key: str = pydantic.Field(alias="segmentKey")
    segment_keys: typing.Optional[typing.List[str]] = pydantic.Field(alias="segmentKeys")
    segment_operator: typing.Optional[RuleSegmentOperator] = pydantic.Field(alias="segmentOperator")

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
