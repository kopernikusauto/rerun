// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/blueprint/components/filter_by_event.fbs".

#pragma once

#include "../../blueprint/datatypes/filter_by_event.hpp"
#include "../../result.hpp"

#include <cstdint>
#include <memory>
#include <utility>

namespace rerun::blueprint::components {
    /// **Component**: Configuration for the filter-by-event feature of the dataframe view.
    struct FilterByEvent {
        rerun::blueprint::datatypes::FilterByEvent filter_by_event;

      public:
        FilterByEvent() = default;

        FilterByEvent(rerun::blueprint::datatypes::FilterByEvent filter_by_event_)
            : filter_by_event(std::move(filter_by_event_)) {}

        FilterByEvent& operator=(rerun::blueprint::datatypes::FilterByEvent filter_by_event_) {
            filter_by_event = std::move(filter_by_event_);
            return *this;
        }

        /// Cast to the underlying FilterByEvent datatype
        operator rerun::blueprint::datatypes::FilterByEvent() const {
            return filter_by_event;
        }
    };
} // namespace rerun::blueprint::components

namespace rerun {
    static_assert(
        sizeof(rerun::blueprint::datatypes::FilterByEvent) ==
        sizeof(blueprint::components::FilterByEvent)
    );

    /// \private
    template <>
    struct Loggable<blueprint::components::FilterByEvent> {
        static constexpr const char Name[] = "rerun.blueprint.components.FilterByEvent";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype() {
            return Loggable<rerun::blueprint::datatypes::FilterByEvent>::arrow_datatype();
        }

        /// Serializes an array of `rerun::blueprint:: components::FilterByEvent` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const blueprint::components::FilterByEvent* instances, size_t num_instances
        ) {
            if (num_instances == 0) {
                return Loggable<rerun::blueprint::datatypes::FilterByEvent>::to_arrow(nullptr, 0);
            } else if (instances == nullptr) {
                return rerun::Error(
                    ErrorCode::UnexpectedNullArgument,
                    "Passed array instances is null when num_elements> 0."
                );
            } else {
                return Loggable<rerun::blueprint::datatypes::FilterByEvent>::to_arrow(
                    &instances->filter_by_event,
                    num_instances
                );
            }
        }
    };
} // namespace rerun