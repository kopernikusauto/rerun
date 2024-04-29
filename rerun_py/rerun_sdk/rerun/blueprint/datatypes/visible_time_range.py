# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/re_types/definitions/rerun/blueprint/datatypes/visible_time_range.fbs".

# You can extend this class by creating a "VisibleTimeRangeExt" class in "visible_time_range_ext.py".

from __future__ import annotations

from typing import Any, Sequence, Union

import pyarrow as pa
from attrs import define, field

from ..._baseclasses import BaseBatch, BaseExtensionType
from ...blueprint import datatypes as blueprint_datatypes

__all__ = [
    "VisibleTimeRange",
    "VisibleTimeRangeArrayLike",
    "VisibleTimeRangeBatch",
    "VisibleTimeRangeLike",
    "VisibleTimeRangeType",
]


@define(init=False)
class VisibleTimeRange:
    """
    **Datatype**: Visible time range bounds for a timelines.

    This datatype does not specify whether it's a time or sequence based timeline.
    """

    def __init__(
        self: Any,
        start: blueprint_datatypes.VisibleTimeRangeBoundaryLike,
        end: blueprint_datatypes.VisibleTimeRangeBoundaryLike,
    ):
        """
        Create a new instance of the VisibleTimeRange datatype.

        Parameters
        ----------
        start:
            Low time boundary for sequence timeline.
        end:
            High time boundary for sequence timeline.

        """

        # You can define your own __init__ function as a member of VisibleTimeRangeExt in visible_time_range_ext.py
        self.__attrs_init__(start=start, end=end)

    start: blueprint_datatypes.VisibleTimeRangeBoundary = field()
    # Low time boundary for sequence timeline.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    end: blueprint_datatypes.VisibleTimeRangeBoundary = field()
    # High time boundary for sequence timeline.
    #
    # (Docstring intentionally commented out to hide this field from the docs)


VisibleTimeRangeLike = VisibleTimeRange
VisibleTimeRangeArrayLike = Union[
    VisibleTimeRange,
    Sequence[VisibleTimeRangeLike],
]


class VisibleTimeRangeType(BaseExtensionType):
    _TYPE_NAME: str = "rerun.blueprint.datatypes.VisibleTimeRange"

    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self,
            pa.struct([
                pa.field(
                    "start",
                    pa.struct([
                        pa.field(
                            "kind",
                            pa.sparse_union([
                                pa.field("_null_markers", pa.null(), nullable=True, metadata={}),
                                pa.field("RelativeToTimeCursor", pa.null(), nullable=True, metadata={}),
                                pa.field("Absolute", pa.null(), nullable=True, metadata={}),
                                pa.field("Infinite", pa.null(), nullable=True, metadata={}),
                            ]),
                            nullable=False,
                            metadata={},
                        ),
                        pa.field("time", pa.int64(), nullable=False, metadata={}),
                    ]),
                    nullable=False,
                    metadata={},
                ),
                pa.field(
                    "end",
                    pa.struct([
                        pa.field(
                            "kind",
                            pa.sparse_union([
                                pa.field("_null_markers", pa.null(), nullable=True, metadata={}),
                                pa.field("RelativeToTimeCursor", pa.null(), nullable=True, metadata={}),
                                pa.field("Absolute", pa.null(), nullable=True, metadata={}),
                                pa.field("Infinite", pa.null(), nullable=True, metadata={}),
                            ]),
                            nullable=False,
                            metadata={},
                        ),
                        pa.field("time", pa.int64(), nullable=False, metadata={}),
                    ]),
                    nullable=False,
                    metadata={},
                ),
            ]),
            self._TYPE_NAME,
        )


class VisibleTimeRangeBatch(BaseBatch[VisibleTimeRangeArrayLike]):
    _ARROW_TYPE = VisibleTimeRangeType()

    @staticmethod
    def _native_to_pa_array(data: VisibleTimeRangeArrayLike, data_type: pa.DataType) -> pa.Array:
        raise NotImplementedError(
            "Arrow serialization of VisibleTimeRange not implemented: We lack codegen for arrow-serialization of structs"
        )  # You need to implement native_to_pa_array_override in visible_time_range_ext.py
