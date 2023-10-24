import pytest
from io import StringIO
from pathlib import Path

from allotropy.parser_factory import Vendor
from allotropy.parsers.perkin_elmer_envision.elmer_envision_parser import (
    ElmerEnvisionParser,
)
from allotropy.parsers.utils.timestamp_parser import TimestampParser
from allotropy.to_allotrope import allotrope_from_io
from tests.parsers.perkin_elmer_envision.elmer_envision_data import get_data, get_model
from tests.parsers.test_utils import from_file, validate_contents, validate_schema

output_files = (
    "PE_Envision_example01",
    "PE_Envision_example02",
    "PE_Envision_example03",
)

VENDOR_TYPE = Vendor.PERKIN_ELMER_ENVISION


@pytest.mark.parametrize("output_file", output_files)
def test_parse_elmer_envision_to_asm(output_file: str) -> None:
    test_filepath = f"tests/parsers/perkin_elmer_envision/testdata/{output_file}.csv"
    expected_filepath = (
        f"tests/parsers/perkin_elmer_envision/testdata/{output_file}.json"
    )
    allotrope_dict = from_file(test_filepath, VENDOR_TYPE)
    validate_schema(allotrope_dict, "fluorescence/BENCHLING/2023/10/fluorescence.json")
    validate_contents(allotrope_dict, expected_filepath)


def test_parse_elmer_envision_to_asm_without_software_info() -> None:
    output_file = "PE_Envision_no_software_info01"
    test_filepath = f"tests/parsers/perkin_elmer_envision/testdata/{output_file}.csv"
    expected_filepath = (
        f"tests/parsers/perkin_elmer_envision/testdata/{output_file}.json"
    )
    allotrope_dict = from_file(test_filepath, VENDOR_TYPE)
    validate_schema(allotrope_dict, "fluorescence/BENCHLING/2023/10/fluorescence.json")
    validate_contents(allotrope_dict, expected_filepath)


@pytest.mark.short
def test_get_model() -> None:
    parser = ElmerEnvisionParser(TimestampParser())
    filename = "__dummy__.csv"
    model = parser._get_model(get_data(), filename)

    if model.measurement_aggregate_document:
        model.measurement_aggregate_document.measurement_identifier = ""

    assert model == get_model(filename)
