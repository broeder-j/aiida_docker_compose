#/usr/bin/env python
"""
This test runs the Fleur dos workflow
"""
from aiida import load_dbenv, is_dbenv_loaded
if not is_dbenv_loaded():
    load_dbenv()
from aiida.orm import Code, DataFactory
from aiida.orm import load_node
from aiida.tools.codespecific.fleur.dos import fleur_dos_wc
from aiida.work.run import submit
###############################
# Set your values here
codename = 'fleur@pseudocluster'#'fleur_iff003_v0_27@iff003'
###############################

code = Code.get_from_string(codename)

fleurinp = load_node(434)
fleur_calc = load_node(438)
remote = fleur_calc.out.remote_folder
#wf_para = ParameterData(dict={})

res = submit(fleur_dos_wc, fleurinp=fleurinp, remote=remote, fleur=code)
#res = fleur_dos_wc.run(fleurinp=fleurinp, remote=remote, fleur=code)
#res = dos.run(wf_parameters=wf_para, fleurinp=fleurinp, fleur_calc=remote, fleur=code2)
