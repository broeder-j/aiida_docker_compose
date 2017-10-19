#!/usr/bin/env python
"""
This test runs the Fleur band workflow
"""
from aiida import load_dbenv, is_dbenv_loaded
if not is_dbenv_loaded():
    load_dbenv()
from aiida.orm import Code, DataFactory
from aiida.orm import load_node
from aiida.tools.codespecific.fleur.band import fleur_band_wc

StructureData = DataFactory('structure')
ParameterData = DataFactory('parameter')
FleurinpData = DataFactory('fleurinp')

###############################
# Set your values here
codename2 = 'fleur@pseudocluster'
###############################

code2 = Code.get_from_string(codename2)

fleurinp = load_node(434)
fleur_calc = load_node(438)
remote = fleur_calc.out.remote_folder
#wf_para = ParameterData(dict={'queue' : 'th123_node'})

res = submit(fleur_band_wc, fleurinp=fleurinp, remote=remote, fleur=code2)
#res = fleur_band_wc.run(fleurinp=fleurinp, remote=remote, fleur=code2)
#res = band.run(wf_parameters=wf_para, fleurinp=fleurinp, remote=remote, fleur=code2)
