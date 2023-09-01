# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:43:07 2020

@author: igna
CUANTO ME VA A COBRAR EDENOR ESTA VEZ?
"""
# cuadro tarifario

print("\n\nHumilde script para saber cuánto vamos a pagar de luz aprox:")


def Gasto(consumo):
    """
    Se le ingresa la unica variable que es el consumo bimensual
    y calcula el consumo mensual y elije el cuadro tarifario correcto
    basado en
    https://www.edenor.com/sites/default/files/2020-07/CuadroTarifario.pdf
    actualizado 31/08/2023: https://www.edenor.com/consumo
    """
    consumo_mensual = consumo / 2
    if consumo_mensual <= 150:
        cat = "T1-R1"
        cargo_fijo = 224.62
        cargo_variable = 28.773
        total = Calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)
    elif 150 < consumo_mensual <= 325:
        cat = "T1-R2"
        cargo_fijo = 443.24
        cargo_variable = 28.879
        total = Calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)
    elif 325 < consumo_mensual <= 400:
        cat = "T1-R3"
        cargo_fijo = 721.59
        cargo_variable = 29.193
        total = Calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)
    elif 400 < consumo_mensual <= 450:
        cat = "T1-R4"
        cargo_fijo = 821.43
        cargo_variable = 29.726
        total = Calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)
    elif 450 < consumo_mensual <= 500:
        cat = "T1-R5"
        cargo_fijo = 1192.15
        cargo_variable = 30.142
        total = Calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)
    elif 500 < consumo_mensual <= 600:
        cat = "T1-R6"
        cargo_fijo = 2247.33
        cargo_variable = 30.310
        total = Calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)
    elif 600 < consumo_mensual <= 700:
        cat = "T1-R7"
        cargo_fijo = 5789.72
        cargo_variable = 31.180
        total = Calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)
    elif 700 < consumo_mensual <= 1400:
        cat = "T1-R8"
        cargo_fijo = 7479.09
        cargo_variable = 31.493
        total = Calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)
    else:  # consumos superiores a 1400
        cat = "T1-R9"
        cargo_fijo = 9690.53
        cargo_variable = 31.830
        total = Calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)

    return total


def Calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat):
    consumo = consumo_mensual
    neto = consumo * cargo_variable + cargo_fijo
    IVA = 21 * neto / 100
    cont_muni = 6.4240 * neto / 100
    cont_prov = 0.0010 * neto / 100
    conceptos_electricos = neto
    impuestos_y_contribuciones = IVA + cont_muni + cont_prov
    total = neto + IVA + cont_muni + cont_prov
    msj = (
        "\n\nConsumiste %.2fkWh por mes, tu categoria es: " % consumo
        + cat
        + "\n"
        + cat
        + " Cargo fijo: $ %.2f" % cargo_fijo
        + "\n"
        + cat
        + " Cargo variable: $ %.3f - total: $ %.2f"
        % (cargo_variable, cargo_variable * consumo)
        + "\n\nTotal sin impuestos: $%.2f " % neto
        + "\n\nIVA: $%.2f " % IVA
        + "\ncontribucion municipal: $%.2f " % cont_muni
        + "\ncontribucion provincial: $%.2f " % cont_prov
        + "\n\nTOTAL: $%.2f\n\n" % total
        + "El valor total puede tener un error de +/- $250 "
        "por un impuesto que en la factura no se deja bien en claro"
    )
    print(msj)
    return conceptos_electricos, impuestos_y_contribuciones, total, msj


def main():
    try:
        kwh = float(input("Ingresa los kwh: \n"))
        resultado = Gasto(kwh)[0]
    except:
        resultado = "tenes que ingresar un numero"
    return resultado


if __name__ == "__main__":
    gasto = main()
    print(gasto)
    while True:
        input("\napreta cualquiera pa salir\n")
        break
