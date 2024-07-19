# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/archetypes/transform3d.fbs".

# You can extend this class by creating a "Transform3DExt" class in "transform3d_ext.py".

from __future__ import annotations

from attrs import define, field

from .. import components
from .._baseclasses import (
    Archetype,
)
from .transform3d_ext import Transform3DExt

__all__ = ["Transform3D"]


@define(str=False, repr=False, init=False)
class Transform3D(Transform3DExt, Archetype):
    """
    **Archetype**: A transform between two 3D spaces, i.e. a pose.

    All components are applied in the inverse order they are listed here.
    E.g. if both a 4x4 matrix with a translation and a translation vector are present,
    the translation is applied first, followed by the matrix.

    Each transform component can be listed multiple times, but transform tree propagation is only possible
    if there's only one instance for each transform component.

    Examples
    --------
    ### Variety of 3D transforms:
    ```python
    from math import pi

    import rerun as rr
    from rerun.datatypes import Angle, RotationAxisAngle

    rr.init("rerun_example_transform3d", spawn=True)

    arrow = rr.Arrows3D(origins=[0, 0, 0], vectors=[0, 1, 0])

    rr.log("base", arrow)

    rr.log("base/translated", rr.Transform3D(translation=[1, 0, 0]))
    rr.log("base/translated", arrow)

    rr.log(
        "base/rotated_scaled",
        rr.Transform3D(
            rotation=RotationAxisAngle(axis=[0, 0, 1], angle=Angle(rad=pi / 4)),
            scale=2,
        ),
    )
    rr.log("base/rotated_scaled", arrow)
    ```
    <center>
    <picture>
      <source media="(max-width: 480px)" srcset="https://static.rerun.io/transform3d_simple/141368b07360ce3fcb1553079258ae3f42bdb9ac/480w.png">
      <source media="(max-width: 768px)" srcset="https://static.rerun.io/transform3d_simple/141368b07360ce3fcb1553079258ae3f42bdb9ac/768w.png">
      <source media="(max-width: 1024px)" srcset="https://static.rerun.io/transform3d_simple/141368b07360ce3fcb1553079258ae3f42bdb9ac/1024w.png">
      <source media="(max-width: 1200px)" srcset="https://static.rerun.io/transform3d_simple/141368b07360ce3fcb1553079258ae3f42bdb9ac/1200w.png">
      <img src="https://static.rerun.io/transform3d_simple/141368b07360ce3fcb1553079258ae3f42bdb9ac/full.png" width="640">
    </picture>
    </center>

    ### Transform hierarchy:
    ```python
    import numpy as np
    import rerun as rr
    import rerun.blueprint as rrb

    rr.init("rerun_example_transform3d_hierarchy", spawn=True)

    # One space with the sun in the center, and another one with the planet.
    rr.send_blueprint(
        rrb.Horizontal(rrb.Spatial3DView(origin="sun"), rrb.Spatial3DView(origin="sun/planet", contents="sun/**"))
    )

    rr.set_time_seconds("sim_time", 0)

    # Planetary motion is typically in the XY plane.
    rr.log("/", rr.ViewCoordinates.RIGHT_HAND_Z_UP, static=True)

    # Setup points, all are in the center of their own space:
    # TODO(#1361): Should use spheres instead of points.
    rr.log("sun", rr.Points3D([0.0, 0.0, 0.0], radii=1.0, colors=[255, 200, 10]))
    rr.log("sun/planet", rr.Points3D([0.0, 0.0, 0.0], radii=0.4, colors=[40, 80, 200]))
    rr.log("sun/planet/moon", rr.Points3D([0.0, 0.0, 0.0], radii=0.15, colors=[180, 180, 180]))

    # Draw fixed paths where the planet & moon move.
    d_planet = 6.0
    d_moon = 3.0
    angles = np.arange(0.0, 1.01, 0.01) * np.pi * 2
    circle = np.array([np.sin(angles), np.cos(angles), angles * 0.0]).transpose()
    rr.log("sun/planet_path", rr.LineStrips3D(circle * d_planet))
    rr.log("sun/planet/moon_path", rr.LineStrips3D(circle * d_moon))

    # Movement via transforms.
    for i in range(0, 6 * 120):
        time = i / 120.0
        rr.set_time_seconds("sim_time", time)
        r_moon = time * 5.0
        r_planet = time * 2.0

        rr.log(
            "sun/planet",
            rr.Transform3D(
                translation=[np.sin(r_planet) * d_planet, np.cos(r_planet) * d_planet, 0.0],
                rotation=rr.RotationAxisAngle(axis=(1, 0, 0), degrees=20),
            ),
        )
        rr.log(
            "sun/planet/moon",
            rr.Transform3D(
                translation=[np.cos(r_moon) * d_moon, np.sin(r_moon) * d_moon, 0.0],
                from_parent=True,
            ),
        )
    ```
    <center>
    <picture>
      <source media="(max-width: 480px)" srcset="https://static.rerun.io/transform_hierarchy/cb7be7a5a31fcb2efc02ba38e434849248f87554/480w.png">
      <source media="(max-width: 768px)" srcset="https://static.rerun.io/transform_hierarchy/cb7be7a5a31fcb2efc02ba38e434849248f87554/768w.png">
      <source media="(max-width: 1024px)" srcset="https://static.rerun.io/transform_hierarchy/cb7be7a5a31fcb2efc02ba38e434849248f87554/1024w.png">
      <source media="(max-width: 1200px)" srcset="https://static.rerun.io/transform_hierarchy/cb7be7a5a31fcb2efc02ba38e434849248f87554/1200w.png">
      <img src="https://static.rerun.io/transform_hierarchy/cb7be7a5a31fcb2efc02ba38e434849248f87554/full.png" width="640">
    </picture>
    </center>

    """

    # __init__ can be found in transform3d_ext.py

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            transform=None,  # type: ignore[arg-type]
            translation=None,  # type: ignore[arg-type]
            scale=None,  # type: ignore[arg-type]
            mat3x3=None,  # type: ignore[arg-type]
            axis_length=None,  # type: ignore[arg-type]
        )

    @classmethod
    def _clear(cls) -> Transform3D:
        """Produce an empty Transform3D, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    transform: components.Transform3DBatch = field(
        metadata={"component": "required"},
        converter=components.Transform3DBatch._required,  # type: ignore[misc]
    )
    # The transform
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    translation: components.Translation3DBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.Translation3DBatch._optional,  # type: ignore[misc]
    )
    # Translation vectors.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    scale: components.Scale3DBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.Scale3DBatch._optional,  # type: ignore[misc]
    )
    # Scaling factor.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    mat3x3: components.TransformMat3x3Batch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.TransformMat3x3Batch._optional,  # type: ignore[misc]
    )
    # 3x3 transformation matrices.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    axis_length: components.AxisLengthBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.AxisLengthBatch._optional,  # type: ignore[misc]
    )
    # Visual length of the 3 axes.
    #
    # The length is interpreted in the local coordinate system of the transform.
    # If the transform is scaled, the axes will be scaled accordingly.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__  # type: ignore[assignment]
