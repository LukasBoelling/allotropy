# generated by datamodel-codegen:
#   filename:  fluorescence.json
#   timestamp: 2023-09-17T16:00:55+00:00

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from allotropy.allotrope.models.shared.components.plate_reader import (
    ProcessedDataAggregateDocument,
    SampleDocument,
)
from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueDegreeCelsius,
    TQuantityValueMicroliter,
    TQuantityValueMillimeter,
    TQuantityValueNanometer,
    TQuantityValueNumber,
    TQuantityValuePicogramPerMilliliter,
    TQuantityValueSecondTime,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TDatacube,
    TDateTimeValue,
    TStringValue,
)


class ContainerType(Enum):
    reactor = "reactor"
    controlled_lab_reactor = "controlled lab reactor"
    tube = "tube"
    well_plate = "well plate"
    differential_scanning_calorimetry_pan = "differential scanning calorimetry pan"
    qPCR_reaction_block = "qPCR reaction block"
    vial_rack = "vial rack"
    pan = "pan"
    reservoir = "reservoir"
    array_card_block = "array card block"
    capillary = "capillary"
    disintegration_apparatus_basket = "disintegration apparatus basket"
    jar = "jar"
    container = "container"
    tray = "tray"
    basket = "basket"
    cell_holder = "cell holder"


class ScanPositionSettingPlateReader(Enum):
    bottom_scan_position__plate_reader_ = "bottom scan position (plate reader)"
    scan_position_configuration__plate_reader_ = (
        "scan position configuration (plate reader)"
    )
    top_scan_position__plate_reader_ = "top scan position (plate reader)"


@dataclass
class DeviceSystemDocument:
    device_identifier: TStringValue
    model_number: TStringValue


@dataclass
class DeviceControlDocumentItem:
    device_type: Optional[TStringValue] = None
    shaking_configuration_description: Optional[TStringValue] = None
    detector_distance_setting__plate_reader_: Optional[TQuantityValueMillimeter] = None
    integration_time: Optional[TQuantityValueSecondTime] = None
    number_of_averages: Optional[TQuantityValueNumber] = None
    detector_gain_setting: Optional[TStringValue] = None
    scan_position_setting__plate_reader_: Optional[
        ScanPositionSettingPlateReader
    ] = None
    detector_carriage_speed_setting: Optional[TStringValue] = None
    detector_wavelength_setting: Optional[TQuantityValueNanometer] = None
    detector_bandwidth_setting: Optional[TQuantityValueNanometer] = None
    excitation_bandwidth_setting: Optional[TQuantityValueNanometer] = None
    excitation_wavelength_setting: Optional[TQuantityValueNanometer] = None
    wavelength_filter_cutoff_setting: Optional[TQuantityValueNanometer] = None
    field_index: Optional[int] = None


@dataclass
class DeviceControlAggregateDocument:
    device_control_document: Optional[list[DeviceControlDocumentItem]] = None


@dataclass
class MeasurementDocumentItem:
    device_control_aggregate_document: DeviceControlAggregateDocument
    sample_document: SampleDocument
    data_cube: Optional[TDatacube] = None
    compartment_temperature: Optional[TQuantityValueDegreeCelsius] = None
    processed_data_aggregate_document: Optional[ProcessedDataAggregateDocument] = None
    mass_concentration: Optional[TQuantityValuePicogramPerMilliliter] = None


@dataclass
class MeasurementAggregateDocument:
    measurement_identifier: TStringValue
    plate_well_count: TQuantityValueNumber
    measurement_document: list[MeasurementDocumentItem]
    measurement_time: Optional[TDateTimeValue] = None
    analyst: Optional[TStringValue] = None
    analytical_method_identifier: Optional[TStringValue] = None
    experimental_data_identifier: Optional[TStringValue] = None
    experiment_type: Optional[TStringValue] = None
    container_type: Optional[ContainerType] = None
    well_volume: Optional[TQuantityValueMicroliter] = None
    device_system_document: Optional[DeviceSystemDocument] = None


@dataclass
class Model:
    measurement_aggregate_document: Optional[MeasurementAggregateDocument] = None
    manifest: str = "http://purl.allotrope.org/manifests/fluorescence/BENCHLING/2023/09/fluorescence.manifest"
