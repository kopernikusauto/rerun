# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/re_types/definitions/rerun/testing/datatypes/fuzzy.fbs".

# You can extend this class by creating a "AffixFuzzer1Ext" class in "affix_fuzzer1_ext.py".

from __future__ import annotations

from typing import Any, Sequence, Union

import numpy as np
import numpy.typing as npt
import pyarrow as pa
from attrs import define, field
from rerun._baseclasses import BaseBatch, BaseExtensionType
from rerun._converters import (
    bool_or_none,
    float_or_none,
    str_or_none,
    to_np_float32,
)

from .. import datatypes

__all__ = ["AffixFuzzer1", "AffixFuzzer1ArrayLike", "AffixFuzzer1Batch", "AffixFuzzer1Like", "AffixFuzzer1Type"]


def _affix_fuzzer1__almost_flattened_scalar__special_field_converter_override(
    x: datatypes.FlattenedScalarLike,
) -> datatypes.FlattenedScalar:
    if isinstance(x, datatypes.FlattenedScalar):
        return x
    else:
        return datatypes.FlattenedScalar(x)


@define(init=False)
class AffixFuzzer1:
    def __init__(
        self: Any,
        single_string_required: str,
        many_strings_required: list[str],
        flattened_scalar: float,
        almost_flattened_scalar: datatypes.FlattenedScalarLike,
        single_float_optional: float | None = None,
        single_string_optional: str | None = None,
        many_floats_optional: npt.ArrayLike | None = None,
        many_strings_optional: list[str] | None = None,
        from_parent: bool | None = None,
    ):
        """Create a new instance of the AffixFuzzer1 datatype."""

        # You can define your own __init__ function as a member of AffixFuzzer1Ext in affix_fuzzer1_ext.py
        self.__attrs_init__(
            single_float_optional=single_float_optional,
            single_string_required=single_string_required,
            single_string_optional=single_string_optional,
            many_floats_optional=many_floats_optional,
            many_strings_required=many_strings_required,
            many_strings_optional=many_strings_optional,
            flattened_scalar=flattened_scalar,
            almost_flattened_scalar=almost_flattened_scalar,
            from_parent=from_parent,
        )

    single_string_required: str = field(converter=str)
    many_strings_required: list[str] = field()
    flattened_scalar: float = field(converter=float)
    almost_flattened_scalar: datatypes.FlattenedScalar = field(
        converter=_affix_fuzzer1__almost_flattened_scalar__special_field_converter_override
    )
    single_float_optional: float | None = field(default=None, converter=float_or_none)
    single_string_optional: str | None = field(default=None, converter=str_or_none)
    many_floats_optional: npt.NDArray[np.float32] | None = field(default=None, converter=to_np_float32)
    many_strings_optional: list[str] | None = field(default=None)
    from_parent: bool | None = field(default=None, converter=bool_or_none)


AffixFuzzer1Like = AffixFuzzer1
AffixFuzzer1ArrayLike = Union[
    AffixFuzzer1,
    Sequence[AffixFuzzer1Like],
]


class AffixFuzzer1Type(BaseExtensionType):
    _TYPE_NAME: str = "rerun.testing.datatypes.AffixFuzzer1"

    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self,
            pa.struct([
                pa.field("single_float_optional", pa.float32(), nullable=True, metadata={}),
                pa.field("single_string_required", pa.utf8(), nullable=False, metadata={}),
                pa.field("single_string_optional", pa.utf8(), nullable=True, metadata={}),
                pa.field(
                    "many_floats_optional",
                    pa.list_(pa.field("item", pa.float32(), nullable=False, metadata={})),
                    nullable=True,
                    metadata={},
                ),
                pa.field(
                    "many_strings_required",
                    pa.list_(pa.field("item", pa.utf8(), nullable=False, metadata={})),
                    nullable=False,
                    metadata={},
                ),
                pa.field(
                    "many_strings_optional",
                    pa.list_(pa.field("item", pa.utf8(), nullable=False, metadata={})),
                    nullable=True,
                    metadata={},
                ),
                pa.field("flattened_scalar", pa.float32(), nullable=False, metadata={}),
                pa.field(
                    "almost_flattened_scalar",
                    pa.struct([pa.field("value", pa.float32(), nullable=False, metadata={})]),
                    nullable=False,
                    metadata={},
                ),
                pa.field("from_parent", pa.bool_(), nullable=True, metadata={}),
            ]),
            self._TYPE_NAME,
        )


class AffixFuzzer1Batch(BaseBatch[AffixFuzzer1ArrayLike]):
    _ARROW_TYPE = AffixFuzzer1Type()

    @staticmethod
    def _native_to_pa_array(data: AffixFuzzer1ArrayLike, data_type: pa.DataType) -> pa.Array:
        raise NotImplementedError(
            "Arrow serialization of AffixFuzzer1 not implemented: We lack codegen for arrow-serialization of structs"
        )  # You need to implement native_to_pa_array_override in affix_fuzzer1_ext.py
