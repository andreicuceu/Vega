import pytest
import numpy as np
import configparser
import lyafit.parser as parser
from lyafit.new_data import Data
from lyafit.correlation_item import CorrelationItem

@pytest.mark.skip
def test_data():
    filename = "D:\\work\\run\\DR16\\chi2.ini"

    # New init
    config = configparser.ConfigParser()
    config.read(filename)
    ini_files = config.get('data sets', 'ini files').split()
    data_config_path = ini_files[0]
    data_config = configparser.ConfigParser()
    data_config.read(data_config_path)
    item = CorrelationItem(data_config)
    data = Data(item)

    # Old init
    dic_init = parser.parse_chi2(filename)
    old_data = dic_init['data sets']['data'][0]

    assert np.allclose(data.rp, old_data.rp)
    assert np.allclose(data.rt, old_data.rt)
    assert np.allclose(data.r, old_data.r)
    assert np.allclose(data.mu, old_data.mu)
    assert np.allclose(data.z, old_data.z)
    assert np.allclose(data.r_square, old_data.rsquare)
    assert np.allclose(data.mu_square, old_data.musquare)

    assert np.allclose(data.mask, old_data.mask)
    assert np.allclose(data.log_cov_det, old_data.log_co_det)
    assert np.allclose(data.inv_masked_cov, old_data.ico)
    assert np.allclose(data.cov_mat, old_data.co)
    assert np.allclose(data.masked_data_vec, old_data.da_cut)
    assert np.allclose(data.data_vec, old_data.da)

    # assert data.tracer_catalog == old_data.tracerMet
    for key, val in data.metal_rp.items():
        assert np.allclose(val, old_data.rp_met[key])
    for key, val in data.metal_rt.items():
        assert np.allclose(val, old_data.rt_met[key])
    for key, val in data.metal_z.items():
        assert np.allclose(val, old_data.z_met[key])
    # for key, val in data.metal_dm.items():
        # assert (val != old_data.dm_met[key]).nnz == 0


# if __name__ == "__main__":
    # test_data()