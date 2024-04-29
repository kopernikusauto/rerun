# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/re_types/definitions/rerun/components/visualizer_overrides.fbs".

# You can extend this class by creating a "VisualizerOverridesExt" class in "visualizer_overrides_ext.py".

from __future__ import annotations

from typing import Any, Sequence, Union

import pyarrow as pa
from attrs import define, field

from .._baseclasses import BaseBatch, BaseExtensionType, ComponentBatchMixin

__all__ = [
    "VisualizerOverrides",
    "VisualizerOverridesArrayLike",
    "VisualizerOverridesBatch",
    "VisualizerOverridesLike",
    "VisualizerOverridesType",
]


@define(init=False)
class VisualizerOverrides:
    """**Component**: The name of a visualizer."""

    def __init__(self: Any, value: VisualizerOverridesLike):
        """Create a new instance of the VisualizerOverrides component."""

        # You can define your own __init__ function as a member of VisualizerOverridesExt in visualizer_overrides_ext.py
        self.__attrs_init__(value=value)

    value: list[str] = field()


VisualizerOverridesLike = VisualizerOverrides
VisualizerOverridesArrayLike = Union[
    VisualizerOverrides,
    Sequence[VisualizerOverridesLike],
]


class VisualizerOverridesType(BaseExtensionType):
    _TYPE_NAME: str = "rerun.components.VisualizerOverrides"

    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self, pa.list_(pa.field("item", pa.utf8(), nullable=False, metadata={})), self._TYPE_NAME
        )


class VisualizerOverridesBatch(BaseBatch[VisualizerOverridesArrayLike], ComponentBatchMixin):
    _ARROW_TYPE = VisualizerOverridesType()

    @staticmethod
    def _native_to_pa_array(data: VisualizerOverridesArrayLike, data_type: pa.DataType) -> pa.Array:
        raise NotImplementedError(
            "Arrow serialization of VisualizerOverrides not implemented: We lack codegen for arrow-serialization of structs"
        )  # You need to implement native_to_pa_array_override in visualizer_overrides_ext.py
