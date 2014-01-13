
#!/usr/bin/env python
# encoding: utf-8
"""
test_Turbine_CostsSE.py

Created by Katherine Dykes on 2014-01-07.
Copyright (c) NREL. All rights reserved.
"""

import unittest
import numpy as np
from commonse.utilities import check_gradient_unit_test
from Plant_CostsSE.Plant_BOS.NREL_Onshore_BOS.nrel_bos_onshore import bos_nrel_onshore_component
from Plant_CostsSE.Plant_BOS.NREL_CSM_BOS.nrel_csm_bos import bos_csm_component
from Plant_CostsSE.Plant_OM.NREL_CSM_OM.nrel_csm_om import om_csm_component

#Plant Costs - BOS
class Test_bos_nrel_onshore_component(unittest.TestCase):

    def test1(self):

        bos = bos_nrel_onshore_component()
        bos.machine_rating = 5000.0
        bos.rotor_diameter = 126.0
        bos.turbine_cost = 5950209.283
        bos.turbine_number = 100
        bos.hub_height = 90.0
        bos.RNA_mass = 256634.5

        check_gradient_unit_test(self, bos)

class Test_bos_csm_component(unittest.TestCase):

    def test1(self):

        bos = bos_csm_component()
        bos.machine_rating = 5000.0
        bos.rotor_diameter = 126.0
        bos.turbine_cost = 5950209.283
        bos.turbine_number = 100 
        bos.hub_height = 90.0
        bos.RNA_mass = 256634.5 # RNA mass is not used in this simple model

        check_gradient_unit_test(self, bos, display=False)


#Plant Costs - OPEX
class Test_om_csm_component(unittest.TestCase):

    def test1(self):

        om = om_csm_component()
    
        om.machine_rating = 5000.0 # Need to manipulate input or underlying component will not execute
        om.net_aep = 1701626526.28
        om.sea_depth = 20.0
        om.year = 2009
        om.month = 10
        om.turbine_number = 100

        check_gradient_unit_test(self, om)
        
if __name__ == "__main__":
    unittest.main()