from ligotools import readligo as rl
import numpy as np

def test_missing_file_loaddata():
    """Asserts that loaddata returns tuple (None, None, None) if the file does not exist"""
    assert rl.loaddata("data/H-H1_LOSC_ImaginaryFile.hdf5", "H1") == (None, None, None)

def test_dq_channel_to_seglist_mock_channel():
    """Tests the functionality of the dq_channel_to_seglist method
    
        Given the channel [0, 0, 1, 1, 1, 0, 1, 1, 0] and fs = 2, 
        the test expects slices [4,10) and [12,16) 
    """
    channel_1hz = np.array([0, 0, 1, 1, 1, 0, 1, 1, 0])
    segment_list = rl.dq_channel_to_seglist(channel_1hz, fs=2)
    assert isinstance(segment_list, list)
    assert isinstance(segment_list[0], slice)
    assert isinstance(segment_list[1], slice)
    assert len(segment_list) == 2
    assert segment_list[0].start == 4
    assert segment_list[0].stop == 10
    assert segment_list[1].start == 12
    assert segment_list[1].stop == 16