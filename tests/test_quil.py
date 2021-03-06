
# Copyright 2016-2018, Rigetti Computing
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import pytest

import quantumflow as qf


QUIL_FILES = [
    'hello_world.quil',
    'empty.quil',
    'classical_logic.quil',
    'control_flow.quil',
    'measure.quil',
    'qaoa.quil',
    'bell.quil',
    'include.quil',
    ]

RUNNABLE_QUIL_FILES = QUIL_FILES[:-1]


def test_parse_quilfile():
    print()
    for quilfile in QUIL_FILES:
        filename = 'tests/quil/'+quilfile
        print("<<<"+filename+">>>")
        qf.parse_quilfile(filename)


def test_run_quilfile():
    print()
    for quilfile in RUNNABLE_QUIL_FILES:
        filename = 'tests/quil/'+quilfile
        print("<<<"+filename+">>>")
        prog = qf.parse_quilfile(filename)
        prog.run()


def test_unparsable():
    with pytest.raises(RuntimeError):
        qf.parse_quilfile('tests/quil/unparsable.quil')
