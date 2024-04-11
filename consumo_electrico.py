# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:43:07 2020

@author: igna
CUANTO ME VA A COBRAR EDENOR ESTA VEZ?
"""
# cuadro tarifario

print("\n\nHumilde script para saber cuánto vamos a pagar de luz aprox:")


def gasto(consumo, ingreso):
    """
    Se le ingresa la unica variable que es el consumo bimensual
    y calcula el consumo mensual y elije el cuadro tarifario correcto
    basado en
    https://www.edenor.com/sites/default/files/2020-07/CuadroTarifario.pdf
    actualizado 11/04/2024: https://www.edenor.com/consumo
    """
    consumo_mensual = consumo / 2
    if consumo_mensual <= 150:
        cat = "T1-R1"
        cargo_fijo = 791.27
        cargo_variable = [67.826, 13.096, 12.219]
        total = calculadora(consumo_mensual, cargo_fijo, cargo_variable[ingreso], cat)
    elif 150 < consumo_mensual <= 400:
        cat = "T1-R2"
        cargo_fijo = 1687.65
        cargo_variable = [68.128, 13.399, 12.521]
        total = calculadora(consumo_mensual, cargo_fijo, cargo_variable[ingreso], cat)
    elif 401 < consumo_mensual <= 500:
        cat = "T1-R3"
        cargo_fijo = 5818.97
        cargo_variable = [73.730, 19, 18.122]
        total = calculadora(consumo_mensual, cargo_fijo, cargo_variable[ingreso], cat)
    elif 501 < consumo_mensual <= 600:
        cat = "T1-R4"
        cargo_fijo = 9309.04
        cargo_variable = [75.552, 20.822, 19.945]
        total = calculadora(consumo_mensual, cargo_fijo, cargo_variable[ingreso], cat)
    elif 601 < consumo_mensual <= 700:
        cat = "T1-R5"
        cargo_fijo = 24526.03
        cargo_variable = [79.586, 24.856, 19]
        total = calculadora(consumo_mensual, cargo_fijo, cargo_variable[ingreso], cat)
    elif 700 < consumo_mensual:  #  <= 800:
        cat = "T1-R6"
        cargo_fijo = 28923.74
        cargo_variable = [81.741, 27.011, 26.134]
        total = calculadora(consumo_mensual, cargo_fijo, cargo_variable[ingreso], cat)
    # elif 600 < consumo_mensual <= 700:
    #    cat = "T1-R7"
    #    cargo_fijo = 5789.72
    #    cargo_variable = 31.180
    #    total = calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)
    # elif 700 < consumo_mensual <= 1400:
    #    cat = "T1-R8"
    #    cargo_fijo = 7479.09
    #    cargo_variable = 31.493
    #    total = calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)
    # else:  # consumos superiores a 1400
    #    cat = "T1-R9"
    #    cargo_fijo = 9690.53
    #    cargo_variable = 31.830
    #    total = calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat)

    return total


def calculadora(consumo_mensual, cargo_fijo, cargo_variable, cat):
    """Calcula el total a pagar e imprime un mensaje con los detalles"""
    consumo = consumo_mensual
    neto = consumo * cargo_variable + cargo_fijo
    iva = 21 * neto / 100
    cont_muni = 6.4240 * neto / 100
    cont_prov = 0.0010 * neto / 100
    decLey7290_67_Ley15479PBA = 4 * neto / 100
    conceptos_electricos = neto
    abl = 1967.21
    impuestos_y_contribuciones = (
        iva + cont_muni + cont_prov + decLey7290_67_Ley15479PBA + abl
    )
    total = neto + impuestos_y_contribuciones
    msj = (
        f"\n\nConsumiste {consumo:.2f}, tu categoria es: {cat}"
        + f"\n{cat} Cargo fijo: ${cargo_fijo:.2f}"
        + f"\n{cat} Cargo variable/kWh: ${cargo_variable:.2f} - total: ${cargo_variable*consumo:.2f}"
        + f"\n\nTotal sin impuestos: ${neto:.2f}"
        + f"\n\niva: ${iva:.2f}"
        + f"\ncontribucion municipal: ${cont_muni:.2f}"
        + f"\ncontribucion provincial: ${cont_prov:.2f}"
        + f"\nDecreto-Ley 7.290/67 s/Ley 15.479 PBA: ${decLey7290_67_Ley15479PBA:.2f}\n"
        + f"\nTasa municipal por alumbrado público: ${abl}\n"
        + f"\n\nTOTAL: ${total:.2f}\n\n"
        + "El valor total puede tener error de +/- "
        "por un impuesto que en la factura no se deja bien en claro"
    )

    print(msj)
    return conceptos_electricos, impuestos_y_contribuciones, total, msj


def main():
    """main func"""
    try:
        kwh = float(input("Ingresa los kwh: \n"))
        ingreso = int(
            input("Ingresa tu tipo de ingreso, siendo 0 alto, 1 medio y 2 bajo\n")
        )
        resultado = gasto(kwh, ingreso)[0]
    except ValueError:
        resultado = "tenes que ingresar un numero"
    return resultado


if __name__ == "__main__":
    gasto = main()
    # print(gasto)
    while True:
        input("\napreta cualquiera pa salir\n")
        break
