# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest
from sensirion_driver_adapters.mocks.mock_shdlc_channel_provider import ShdlcMockPortChannelProvider
from sensirion_driver_adapters.shdlc_adapter.shdlc_serial_channel_provider import ShdlcSerialPortChannelProvider
from sensirion_uart_sps30.response_provider import Sps30ResponseProvider


def pytest_addoption(parser):
    """
    Register command line options
    """
    parser.addoption("--serial-port", action="store", type=str)
    parser.addoption("--serial-bitrate", action="store", type=int, default=115200)


def _get_serial_port(config, validate=False):
    """
    Get the serial port to be used for the tests.
    """
    port = config.getoption("--serial-port")
    if (validate is True) and (port is None):
        raise ValueError("Please specify the serial port to be used with "
                         "the '--serial-port' argument.")
    return port


def _get_serial_bitrate(config):
    """
    Get the serial port bitrate to be used for the tests.
    """
    return config.getoption("--serial-bitrate")


def pytest_report_header(config):
    """
    Add extra information to test report header
    """
    lines = [
        "SensorBridge serial port: " + str(_get_serial_port(config)),
        "SensorBridge serial bitrate: " + str(_get_serial_bitrate(config))
    ]
    return '\n'.join(lines)


@pytest.fixture(scope="session")
def channel_provider(request):
    serial_port = _get_serial_port(request.config, validate=False)
    serial_bitrate = _get_serial_bitrate(request.config)
    if serial_port is not None:
        yield ShdlcSerialPortChannelProvider(serial_port=serial_port,
                                             serial_baud_rate=serial_bitrate)
    else:
        yield ShdlcMockPortChannelProvider(response_provider=Sps30ResponseProvider())
