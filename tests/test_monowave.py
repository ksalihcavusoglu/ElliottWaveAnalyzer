from models.MonoWave import MonoWaveUp
from models.MonoWave import MonoWaveDown

import numpy as np


def test_monowaveup_instance_is_created():
    lows = np.random.rand(100)
    highs = np.random.rand(100)
    dates = np.random.rand(100)

    monowave_up = MonoWaveUp(lows, highs, dates, 0)

    assert isinstance(monowave_up, MonoWaveUp)

def test_monowavedown_instance_is_created():
    lows = np.random.rand(100)
    highs = np.random.rand(100)
    dates = np.random.rand(100)

    monowave_down = MonoWaveDown(lows, highs, dates, 0)

    assert isinstance(monowave_down, MonoWaveDown)