def Menu():

    """Funcion que Muestra el Menu"""

    print """************
    

Calculadora

************

Menu

1) Suma

2) Resta

3) Multiplicacion

4) Division

5) Salir

6) OPCION 6

                                /|         ,
                              ,///        /|
                             // //     ,///
                            // //     // //
                           // //     || ||
                           || ||    // //
                           || ||   // //
                           || ||  // //
                           || || || ||
                           \\,\|,|\_//
                            \\)\)\\|/
                            )-."" .-(
                           //^\` `/^\\
                          //  |   |  \\
                        ,/_| 0| _ | 0|_\,
                      /`    `"=.v.="`    `\
                     /`    _."{_,_}"._    `\
                     `/`  ` \  |||  / `  `\`
                      `",_  \\=^~^=//  _,"`
                          "=,\'-=-'/,="
                              '---'
      ESTO FUE TODO POR HOY EN FANTASIAS ANIMADAS DE AYER Y HOY
"""
def Calculadora():

    """Funcion Para Calcular Operaciones Aritmeticas"""

    Menu()

    opc = int(input("Selecione Opcion\n"))

    while (opc >0 and opc <5):

        x = int(input("Ingrese Numero\n"))

        y = int(input("Ingrese Otro Numero\n"))

        if (opc==1):

            print "La Suma es:", x+y

            opc = int(input("Selecione Opcion\n"))

        elif(opc==2):

            print "La Resta es:",x-y

            opc = int(input("Selecione Opcion\n"))

        elif(opc==3):

            print "La Multiplicacion es:",x*y

            opc = int(input("Selecione Opcion\n"))

        elif(opc==4):

            try:

              print "La Division es:", x/y

              opc = int(input("Selecione Opcion\n"))

            except ZeroDivisionError:

              print "No se Permite la Division Entre 0"

              opc = int(input("Selecione Opcion\n"))

Calculadora()
print "Hola"
print "Hola2"
print "hola3"
print """

                                /|         ,
                              ,///        /|
                             // //     ,///
                            // //     // //
                           // //     || ||
                           || ||    // //
                           || ||   // //
                           || ||  // //
                           || || || ||
                           \\,\|,|\_//
                            \\)\)\\|/
                            )-."" .-(
                           //^\` `/^\\
                          //  |   |  \\
                        ,/_| 0| _ | 0|_\,
                      /`    `"=.v.="`    `\
                     /`    _."{_,_}"._    `\
                     `/`  ` \  |||  / `  `\`
                      `",_  \\=^~^=//  _,"`
                          "=,\'-=-'/,="
                              '---'
      ESTO FUE TODO POR HOY EN FANTASIAS ANIMADAS DE AYER Y HOY

"""
