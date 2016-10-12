# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora

@step(u'Dado que tengo el número "([^"]*)" y "([^"]*)"')
def dado_que_tengo_el_numero_group1_y_group2(step, num1, num2):
    cal = Calculadora()
    world.resultado = cal.suma(int(num1),int(num2))
    world.resultadoResta = cal.resta(int(num1),int(num2))
    world.resultadoMult = cal.mult(int(num1),int(num2))
    world.resultadoDiv = cal.div(int(num1),int(num2))


@step(u'cuando realizo la resta')
def cuando_realizo_la_resta(step):
    pass


@step(u'cuando realizo la multiplicacion')
def cuando_realizo_la_multiplicacion(step):
    pass

@step(u'cuando realizo la suma')
def cuando_realizo_la_suma(step):
	pass

@step(u'cuando realizo la division')
def cuando_realizo_la_division(step):
	pass

@step(u'entonces el resultado que obtengo es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_group1(step, esperado):
    assert int(esperado) ==  world.resultado , 'El resultado no es mismo'

@step(u'entonces el resultado resta que obtengo es "([^"]*)"')
def entonces_el_resultado_resta_que_obtengo_es_group1(step, esperado):
    assert int(esperado) ==  world.resultadoResta , 'El resultado no es mismo'

@step(u'entonces el resultado multiplicacion que obtengo es "([^"]*)"')
def entonces_el_resultado_multiplicacion_que_obtengo_es_group1(step, esperado):
    assert int(esperado) ==  world.resultadoMult , 'El resultado no es mismo'

@step(u'entonces el resultado division que obtengo es "([^"]*)"')
def entonces_el_resultado_division_que_obtengo_es_group1(step, esperado):
    assert int(esperado) ==  world.resultadoDiv , 'El resultado no es mismo'

