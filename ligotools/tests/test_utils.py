import numpy as np
from ligotools.utils import whiten, reqshift


def test_whiten():
    """
    Checks that the whitened signal has the same length as the input signal 
    and that all values of the whitened signal are finite
    """
    strain = np.random.default_rng(0).standard_normal(2048)
    interp_psd = lambda freqs : np.ones_like(freqs)
    dt = 1 / 1024
    white_ht = whiten(strain, interp_psd, dt)
    assert white_ht.shape == strain.shape
    assert np.isfinite(white_ht).all()

def test_reqshift():
    """
    Checks that the shifted signal has the same length as the input signal 
    and that the shifted signal is indeed different from the original signal
    """
    sample_rate = 1024
    n = 2048
    t = np.arange(n)/sample_rate
    data = np.cos(2*np.pi*100*t)
    shifted_data = reqshift(data, fshift=150, sample_rate=sample_rate)
    assert shifted_data.shape == data.shape
    assert not np.allclose(shifted_data, data)