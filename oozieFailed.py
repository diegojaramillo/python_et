#!/usr/bin/python
# -*- coding: utf-8 -*-
#Autor: Diego Jaramillo Celis    #FC:10/06/2015    #FUM:12/06/2015
#script para obtener información de los ultimos n workflows fallidos en oozie, donde n es el parametro de entrada para el # de workflows
#ex: python oozieFailed.py 5 http://sbmdeglz05.ambientesbc.lab:11000/oozie

import shlex
import subprocess
import sys

def fn_command_line(commandLine): #funcion para ejecutar los comandos de oozie
    global oozieList
    getList = subprocess.Popen(commandLine, shell=False, stdout=subprocess.PIPE)
    oozieList = getList.communicate()[0]

commandLine="oozie jobs -oozie "+str(sys.argv[2])+ " localtime -len "+str(sys.argv[1])+ " -filter status=KILLED"
fn_command_line(shlex.split (commandLine)) #obtener listado de n fallidos

for line1 in oozieList.split('\n'):
    line1 = line1.rstrip()
    if not line1.startswith ('---') and  not line1.startswith ('Job'): #obtener id del WF
	wfID = line1[:36]
	fn_command_line(shlex.split ('oozie job -oozie http://sbmdeglz05.ambientesbc.lab:11000/oozie -info '+wfID)) #detalle de cada etapa del WF
	print 'Workflow Id: '+wfID
	for line2 in oozieList.split('\n'):
	    line2 = line2.rstrip()
	    if line2.startswith('Workflow'):
		print line2
	    if line2.find('ERROR')== -1: #obtener el stage fallido del WF
	        continue
	    stage=line2.split()[0]
            fn_command_line(shlex.split ('oozie job -oozie http://sbmdeglz05.ambientesbc.lab:11000/oozie -info '+stage+' -verbose')) #detalle del stage fallido
	    print 'Workflow stage: '+stage
	    for line3 in oozieList.split('\n'):
		if line3.startswith('Console'): #obtener el application_id
		    print line3[65:95]
		    print '***************'+'\n'
