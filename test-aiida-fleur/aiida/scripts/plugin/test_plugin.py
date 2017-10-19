#!/usr/bin/env python
"""
This test runs the fleur_scf_wc, fleur_band_wc, fleur_dos_wc
"""
from aiida import load_dbenv, is_dbenv_loaded
if not is_dbenv_loaded():
    load_dbenv()
from aiida.orm import Code, DataFactory#, load_node
from aiida.work.run import submit, run
from aiida_fleur.tools.StructureData_util import rel_to_abs
from aiida_fleur.workflows.scf import fleur_scf_wc
from aiida_fleur.workflows.band import fleur_band_wc
from aiida_fleur.workflows.dos import fleur_dos_wc

StructureData = DataFactory('structure')
ParameterData = DataFactory('parameter')
#FleurinpData = DataFactory('fleurinp')

###############################
# Set your values here
codename = 'inpgen@torquessh'
codename2 = 'fleur@torquessh'
###############################

code = Code.get_from_string(codename)
code2 = Code.get_from_string(codename2)

print('Creating structure')
#s = load_node(117)
# Si_delta_inp
bohr_a_0= 0.52917721092 # A
a = 5.167355275190*bohr_a_0
cell = [[0.0,a,a],[a,0.0,a],[a,a,0.0]]
s = StructureData(cell=cell)
pos1 = rel_to_abs((1./8., 1./8., 1./8.), cell)
pos2 = rel_to_abs((-1./8., -1./8., -1./8.), cell)
s.append_atom(position=pos1,symbols='Si')
s.append_atom(position=pos2,symbols='Si')

print('Creating some parameter nodes')
parameters_fail1 = ParameterData(dict={'atom' : {'element': 'Si', 'rmt' : 2.8}})
parameters_fail2 = ParameterData(dict={'comp': {'kmax' : 1.2}})

# A structure would be enough, then the input generator will choose default values, 
# if you want to set parameters you have to provide a ParameterData node with some namelists of the inpgen:
delta_parameters = ParameterData(dict={
                          'title': 'Si, alpha silicon, bulk, delta project',
                          'atom':{'element' : 'Si', 'rmt' : 2.1, 'jri' : 981, 'lmax' : 12, 'lnonsph' : 6},
                          'comp': {'kmax': 5.0, 'gmaxxc' : 12.5, 'gmax' : 15.0},
                          'kpt': {'div1' : 17, 'div2': 17, 'div3' : 17, 'tkb' : 0.0005}})

si_fast_parameters = ParameterData(dict={
                          'title': 'Si, alpha silicon, bulk, tests runs',
                          'atom':{'element' : 'Si', 'rmt' : 2.1, 'jri' : 981, 'lmax' : 8, 'lnonsph' : 6},
                          'comp': {'kmax': 3.9, 'gmaxxc' : 11.5, 'gmax' : 12.5},
                          'kpt': {'div1' : 10, 'div2': 10, 'div3' : 10, 'tkb' : 0.0005}})    

# all workchains have default wc parameters here we provide some
wf_para = ParameterData(dict={'fleur_runmax' : 4, 
                              'density_criterion' : 0.000001,#})
                              'queue_name' : '',
                              'resources' : {"num_machines": 1},
                              'walltime_sec':  10*60})


# now we submit the some  workflows
print('running Fleur scf wc on Si')
#res_scf = run(fleur_scf_wc, wf_parameters=wf_para, structure=s,
#              calc_parameters=si_fast_parameters, inpgen=code, fleur=code2)

# dos& band

#fleurinp = res_scf.get('fleurinp')
#fleur_calc = load_node(res_scf.get('output_scf_wf_para').get_dict().get('last_calc_uuid'))
#remote = fleur_calc.out.remote_folder

#print('submitting Fleur bandstructure and dos wc using defaults on results of run scf on Si')
#res_dos = submit(fleur_dos_wc, fleurinp=fleurinp, remote=remote, fleur=code2)
#res_band = submit(fleur_band_wc, fleurinp=fleurinp, remote=remote, fleur=code2)

print('submmiting futher scf workchains on Si with different specified parameters, 2 should fail')
# Using defaults
res2 = submit(fleur_scf_wc, inpgen=code, fleur=code2)             

# This will fail, because the user requests stupid parameters 
# the workchain should terminate fine, and should tell you what was wrong
# fail in inpgen
res3 = submit(fleur_scf_wc, wf_parameters=wf_para, structure=s,
              calc_parameters=parameters_fail1, inpgen=code, fleur=code2)
# fail in fleur
res4 = submit(fleur_scf_wc, wf_parameters=wf_para, structure=s,
              calc_parameters=parameters_fail2, inpgen=code, fleur=code2)
