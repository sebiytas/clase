##videojuego

print("eres un futbolista profesional y deberás tomar decisiones que determinen tu futuro")

#nivel 1
nivel1 = input("primero, que prefieres. jugar en EUROPA como suplente o en AMERICA como titular? (ingresa el nombre de la region que elijas) ").lower()

if nivel1 == "america":
    print("ahora elige el pais de la liga en la que jugarás de entre estas 3: ARGENTINA, BRASIL, VENEZUELA")
    
    nivel2 = input().lower()
    if nivel2 == "argentina":
        print("ahora elige tu club")
        nivel3 = input("BOCA JUNIORS, RIVER PLATE o ROSARIO CENTRAL ").lower()
               
        if nivel3 == "boca juniors":
            print("eligo tu rol en el equipo")
            nivel4 = input("CREADOR, GOLEADOR o DEFENSOR").lower()

            if nivel4 == "creador":
                print("ahora dime que prefieres")
                nivel5 = input("le armas solo AL 9 o a TODO EL EQUIPO por igual o A NADIE?").lower()

                if nivel5 == "todo el equipo":
                    print("tienes la posibilidad de elegir uno de los 3 titulos con el club cual prefieres?")
                    nivel6 = input("la COPA argentina, la LIGA argentina o la LIBERTADORES").lower()
                        
                    if nivel6 == "libertadores":
                        print("felicidades, eres campeón de la maxima competición americana!!")
                        nivel7 = input("ahora elige: QUEDARSE en el club, IRSE del club ").lower()
                            
                        if nivel7 == "quedarse en el club":
                            print("decides quedarte en el club y eso te suma minutos")
                            nivel8 = input("el tecnico necesita q juegues en otra posicion para cubrir un hueco decides ACEPTAR y sumar minutos o RECHAZAR y jugarm menos ").lower()                           
                            
                            if nivel8 == "aceptar":
                                print("aceptaste, te terminaste adaptando y ahora tienes un gran desempeño en esa posición")
                                nivel9 = input("pero ahora el tecnico te pregunta si prefieres QUEDARTE es esa posicion o VOLVER a tu posicion natural, que eliges? ").lower()
                            
                                if nivel9 == "quedarte":
                                    print("te quedaste y te convertiste en uno de los mejores en esa posicion")
                                    nivel10 = input("que prefieres. el MUNDIAL o el BALÓN DE ORO").lower()

                                    if nivel10 == "mundial":
                                        print("felicidades, te convertiste en uno de los mejores jugadores del mundo de america y pasaste a la historia. FIN DEL JUEGO")
                                    elif nivel10 == "balon de oro":
                                        print("felicidades, pasaste a la historia por ser el primer jugador de una liga americana en ganar el balon de oro. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                elif nivel9 == "volver":    
                                    print("decidiste volver a tu posición natural y la rompiste como nunca")
                                    nivel10 = input("que prefieres. el premio PUSKAS o la BOTA DE ORO").lower()

                                    if nivel10 == "puskas":
                                        print("felicidades, ganaste el puskas y lo ganaste todo con el club. FIN DEL JUEGO")
                                    elif nivel10 == "bota de oro":
                                        print("felicidades, ganaste la bota y te convertiste en leyenda delclub. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                else:
                                    print("error. respuesta no valida")     
                            elif nivel8 == "volver":
                                print("decides volver a tu posicion pero no regresas bien")
                                print("debido a tu frustacion empiezas a jugar con nervios y debido a eso no esquivas una patada que te lesiona y te obliga a dejar el futbol para siempre. FIN DEL JUEGO")
                            else:
                                print("Error. Respuesta no válida.")
                        elif nivel7 == "irse":
                            print("te vas del club, brillar durante unos años en un club europeo. pero las lesiones terminan bajando mucho tu nivel")
                            print("al final no consigues un impacto mundial y te retiras siendo un jugador mas del montón. FIN DEL JUEGO")
                        else:
                            print("Error. Respuesta no válida.")
                            
                    elif nivel6 == "copa":
                        print("ganas la copa y decides esforzarte aun mas")
                        print("al final te terminas llendo a club maximo rival en el cual brillas pero te vuelves odiado por mucha personas debido a tu traición")
                        nivel7 = input("pides DISCULPAS o lo IGNORAS? ").lower()

                        if nivel7 == "disculpas":
                            print("te disculpas, nadie las criticas bajas pero siguen ahi. te retiras como un jugador mas de ese club. FIN DEL JUEGO")
                        elif nivel1 == "ignoras":
                            print("pasas a la historia como el jugador que cometió la mayor traicion a un cub. FIN DEL JUEGO")
                        else:
                            print("error. respuesta no valida")
                    elif nivel6 == "liga":
                        print("te vuelves un gran jugador del club. pasas por otros grandes clubes de america y te retiras como n jugador reconocido internacionalmente. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                        
                elif nivel5 == "al 9":
                    print("gracias a eso ganan muchos trofeos, pero el resto del equipo te detesta y quiere q te vayas")
                    nivel6 = input("te VAS o te QUEDAS?").lower()

                    if nivel6 == "vas":
                        print("te vas a un club pequeño y tu carrera se estanca y te vuelves uno mas del monton. FIN DEL JUEGO")
                    elif nivel6 == "quedas":
                        print("decides quedarte. las crticas siguen pero gans muchos titulos y la aficion te adora")
                        print("pasas a la historia del club bajo el apodo de LA SOMBRA DEL 9. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                elif nivel5 == "nadie":
                    print("el egoismo es malo. no consigues un buen desempeño por no jugarenel equipo y te terminan echando")
                    print("te terminas llendo a un club arabe donde ganas mucho y no debes preocuparte por jugar al 200%. FIN DEL JUEGO")
                else:
                    print("Error. Respuesta no válida.")
                    
            elif nivel4 == "goleador":
                print("te conviertes en el 9 ideal. los clubes grandes quieren ficharte")
                nivel5 = input("VAS o te QUEDAS? ")

                if nivel5 == "vas":
                    print("te vas un club grande. ganas la champions siendo mvp en la final y ganas la bota de oro. Pasas a ser idolo del club. FINAL DEL JUEGO")
                elif nivel5 == "qudedas":
                    print("te conviertes en elmejor jugador de america y ganas la bota de oro pasando a la historia del futbol y del club. FIN DEL JUEGO")

            elif nivel4 == "defensor":
                print("cometes una falta de roja en la final de la libertadores. eso baja tu moral y confianza y pierdes el nivel de juego q tenias pasando a ser olvidado y vendido por el club.")
                print("FIN DEL JUEGO")
            else:
                print("Error. Respuesta no válida.")
                
        if nivel3 == "river plate":
            print("eligo tu rol en el equipo")
            nivel4 = input("CREADOR, GOLEADOR o DEFENSOR").lower()

            if nivel4 == "creador":
                print("ahora dime que prefieres")
                nivel5 = input("le armas solo AL 9 o a TODO EL EQUIPO por igual o A NADIE?").lower()

                if nivel5 == "todo el equipo":
                    print("tienes la posibilidad de elegir uno de los 3 titulos con el club cual prefieres?")
                    nivel6 = input("la COPA argentina, la LIGA argentina o la LIBERTADORES").lower()
                        
                    if nivel6 == "libertadores":
                        print("felicidades, eres campeón de la maxima competición americana!!")
                        nivel7 = input("ahora elige: QUEDARSE en el club, IRSE del club ").lower()
                            
                        if nivel7 == "quedarse en el club":
                            print("decides quedarte en el club y eso te suma minutos")
                            nivel8 = input("el tecnico necesita q juegues en otra posicion para cubrir un hueco decides ACEPTAR y sumar minutos o RECHAZAR y jugarm menos ").lower()                           
                            
                            if nivel8 == "aceptar":
                                print("aceptaste, te terminaste adaptando y ahora tienes un gran desempeño en esa posición")
                                nivel9 = input("pero ahora el tecnico te pregunta si prefieres QUEDARTE es esa posicion o VOLVER a tu posicion natural, que eliges? ").lower()
                            
                                if nivel9 == "quedarte":
                                    print("te quedaste y te convertiste en uno de los mejores en esa posicion")
                                    nivel10 = input("que prefieres. el MUNDIAL o el BALÓN DE ORO").lower()

                                    if nivel10 == "mundial":
                                        print("felicidades, te convertiste en uno de los mejores jugadores del mundo de america y pasaste a la historia. FIN DEL JUEGO")
                                    elif nivel10 == "balon de oro":
                                        print("felicidades, pasaste a la historia por ser el primer jugador de una liga americana en ganar el balon de oro. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                elif nivel9 == "volver":    
                                    print("decidiste volver a tu posición natural y la rompiste como nunca")
                                    nivel10 = input("que prefieres. el premio PUSKAS o la BOTA DE ORO").lower()

                                    if nivel10 == "puskas":
                                        print("felicidades, ganaste el puskas y lo ganaste todo con el club. FIN DEL JUEGO")
                                    elif nivel10 == "bota de oro":
                                        print("felicidades, ganaste la bota y te convertiste en leyenda delclub. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                else:
                                    print("error. respuesta no valida")     
                            elif nivel8 == "volver":
                                print("decides volver a tu posicion pero no regresas bien")
                                print("debido a tu frustacion empiezas a jugar con nervios y debido a eso no esquivas una patada que te lesiona y te obliga a dejar el futbol para siempre. FIN DEL JUEGO")
                            else:
                                print("Error. Respuesta no válida.")
                        elif nivel7 == "irse":
                            print("te vas del club, brillar durante unos años en un club europeo. pero las lesiones terminan bajando mucho tu nivel")
                            print("al final no consigues un impacto mundial y te retiras siendo un jugador mas del montón. FIN DEL JUEGO")
                        else:
                            print("Error. Respuesta no válida.")
                            
                    elif nivel6 == "copa":
                        print("ganas la copa y decides esforzarte aun mas")
                        print("al final te terminas llendo a club maximo rival en el cual brillas pero te vuelves odiado por mucha personas debido a tu traición")
                        nivel7 = input("pides DISCULPAS o lo IGNORAS? ").lower()

                        if nivel7 == "disculpas":
                            print("te disculpas, nadie las criticas bajas pero siguen ahi. te retiras como un jugador mas de ese club. FIN DEL JUEGO")
                        elif nivel1 == "ignoras":
                            print("pasas a la historia como el jugador que cometió la mayor traicion a un cub. FIN DEL JUEGO")
                        else:
                            print("error. respuesta no valida")
                    elif nivel6 == "liga":
                        print("te vuelves un gran jugador del club. pasas por otros grandes clubes de america y te retiras como n jugador reconocido internacionalmente. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                        
                elif nivel5 == "al 9":
                    print("gracias a eso ganan muchos trofeos, pero el resto del equipo te detesta y quiere q te vayas")
                    nivel6 = input("te VAS o te QUEDAS?").lower()

                    if nivel6 == "vas":
                        print("te vas a un club pequeño y tu carrera se estanca y te vuelves uno mas del monton. FIN DEL JUEGO")
                    elif nivel6 == "quedas":
                        print("decides quedarte. las crticas siguen pero gans muchos titulos y la aficion te adora")
                        print("pasas a la historia del club bajo el apodo de LA SOMBRA DEL 9. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                elif nivel5 == "nadie":
                    print("el egoismo es malo. no consigues un buen desempeño por no jugarenel equipo y te terminan echando")
                    print("te terminas llendo a un club arabe donde ganas mucho y no debes preocuparte por jugar al 200%. FIN DEL JUEGO")
                else:
                    print("Error. Respuesta no válida.")
                    
            elif nivel4 == "goleador":
                print("te conviertes en el 9 ideal. los clubes grandes quieren ficharte")
                nivel5 = input("VAS o te QUEDAS? ")

                if nivel5 == "vas":
                    print("te vas un club grande. ganas la champions siendo mvp en la final y ganas la bota de oro. Pasas a ser idolo del club. FINAL DEL JUEGO")
                elif nivel5 == "qudedas":
                    print("te conviertes en elmejor jugador de america y ganas la bota de oro pasando a la historia del futbol y del club. FIN DEL JUEGO")

            elif nivel4 == "defensor":
                print("cometes una falta de roja en la final de la libertadores. eso baja tu moral y confianza y pierdes el nivel de juego q tenias pasando a ser olvidado y vendido por el club.")
                print("FIN DEL JUEGO")
            else:
                print("Error. Respuesta no válida.")
        elif nivel3 == "rosario central":
            print("eligo tu rol en el equipo")
            nivel4 = input("CREADOR, GOLEADOR o DEFENSOR").lower()

            if nivel4 == "creador":
                print("ahora dime que prefieres")
                nivel5 = input("le armas solo AL 9 o a TODO EL EQUIPO por igual o A NADIE?").lower()

                if nivel5 == "todo el equipo":
                    print("tienes la posibilidad de elegir uno de los 3 titulos con el club cual prefieres?")
                    nivel6 = input("la COPA argentina, la LIGA argentina o la LIBERTADORES").lower()
                        
                    if nivel6 == "libertadores":
                        print("felicidades, eres campeón de la maxima competición americana!!")
                        nivel7 = input("ahora elige: QUEDARSE en el club, IRSE del club ").lower()
                            
                        if nivel7 == "quedarse en el club":
                            print("decides quedarte en el club y eso te suma minutos")
                            nivel8 = input("el tecnico necesita q juegues en otra posicion para cubrir un hueco decides ACEPTAR y sumar minutos o RECHAZAR y jugarm menos ").lower()                           
                            
                            if nivel8 == "aceptar":
                                print("aceptaste, te terminaste adaptando y ahora tienes un gran desempeño en esa posición")
                                nivel9 = input("pero ahora el tecnico te pregunta si prefieres QUEDARTE es esa posicion o VOLVER a tu posicion natural, que eliges? ").lower()
                            
                                if nivel9 == "quedarte":
                                    print("te quedaste y te convertiste en uno de los mejores en esa posicion")
                                    nivel10 = input("que prefieres. el MUNDIAL o el BALÓN DE ORO").lower()

                                    if nivel10 == "mundial":
                                        print("felicidades, te convertiste en uno de los mejores jugadores del mundo de america y pasaste a la historia. FIN DEL JUEGO")
                                    elif nivel10 == "balon de oro":
                                        print("felicidades, pasaste a la historia por ser el primer jugador de una liga americana en ganar el balon de oro. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                elif nivel9 == "volver":    
                                    print("decidiste volver a tu posición natural y la rompiste como nunca")
                                    nivel10 = input("que prefieres. el premio PUSKAS o la BOTA DE ORO").lower()

                                    if nivel10 == "puskas":
                                        print("felicidades, ganaste el puskas y lo ganaste todo con el club. FIN DEL JUEGO")
                                    elif nivel10 == "bota de oro":
                                        print("felicidades, ganaste la bota y te convertiste en leyenda delclub. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                else:
                                    print("error. respuesta no valida")     
                            elif nivel8 == "volver":
                                print("decides volver a tu posicion pero no regresas bien")
                                print("debido a tu frustacion empiezas a jugar con nervios y debido a eso no esquivas una patada que te lesiona y te obliga a dejar el futbol para siempre. FIN DEL JUEGO")
                            else:
                                print("Error. Respuesta no válida.")
                        elif nivel7 == "irse":
                            print("te vas del club, brillar durante unos años en un club europeo. pero las lesiones terminan bajando mucho tu nivel")
                            print("al final no consigues un impacto mundial y te retiras siendo un jugador mas del montón. FIN DEL JUEGO")
                        else:
                            print("Error. Respuesta no válida.")
                            
                    elif nivel6 == "copa":
                        print("ganas la copa y decides esforzarte aun mas")
                        print("al final te terminas llendo a club maximo rival en el cual brillas pero te vuelves odiado por mucha personas debido a tu traición")
                        nivel7 = input("pides DISCULPAS o lo IGNORAS? ").lower()

                        if nivel7 == "disculpas":
                            print("te disculpas, nadie las criticas bajas pero siguen ahi. te retiras como un jugador mas de ese club. FIN DEL JUEGO")
                        elif nivel1 == "ignoras":
                            print("pasas a la historia como el jugador que cometió la mayor traicion a un cub. FIN DEL JUEGO")
                        else:
                            print("error. respuesta no valida")
                    elif nivel6 == "liga":
                        print("te vuelves un gran jugador del club. pasas por otros grandes clubes de america y te retiras como n jugador reconocido internacionalmente. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                        
                elif nivel5 == "al 9":
                    print("gracias a eso ganan muchos trofeos, pero el resto del equipo te detesta y quiere q te vayas")
                    nivel6 = input("te VAS o te QUEDAS?").lower()

                    if nivel6 == "vas":
                        print("te vas a un club pequeño y tu carrera se estanca y te vuelves uno mas del monton. FIN DEL JUEGO")
                    elif nivel6 == "quedas":
                        print("decides quedarte. las crticas siguen pero gans muchos titulos y la aficion te adora")
                        print("pasas a la historia del club bajo el apodo de LA SOMBRA DEL 9. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                elif nivel5 == "nadie":
                    print("el egoismo es malo. no consigues un buen desempeño por no jugarenel equipo y te terminan echando")
                    print("te terminas llendo a un club arabe donde ganas mucho y no debes preocuparte por jugar al 200%. FIN DEL JUEGO")
                else:
                    print("Error. Respuesta no válida.")
                    
            elif nivel4 == "goleador":
                print("te conviertes en el 9 ideal. los clubes grandes quieren ficharte")
                nivel5 = input("VAS o te QUEDAS? ")

                if nivel5 == "vas":
                    print("te vas un club grande. ganas la champions siendo mvp en la final y ganas la bota de oro. Pasas a ser idolo del club. FINAL DEL JUEGO")
                elif nivel5 == "qudedas":
                    print("te conviertes en elmejor jugador de america y ganas la bota de oro pasando a la historia del futbol y del club. FIN DEL JUEGO")

            elif nivel4 == "defensor":
                print("cometes una falta de roja en la final de la libertadores. eso baja tu moral y confianza y pierdes el nivel de juego q tenias pasando a ser olvidado y vendido por el club.")
                print("FIN DEL JUEGO")
            else:
                print("Error. Respuesta no válida.")
        else:
            print("Error. Respuesta no válida.")       
                            
    elif nivel2 == "brasil":
        print("ahora elige tu club")
        nivel3 = input("BOTAFOGO, SANTOSFC o GREMIO ").lower()
               
        if nivel3 == "botafogo":
            print("eligo tu rol en el equipo")
            nivel4 = input("CREADOR, GOLEADOR o DEFENSOR").lower()

            if nivel4 == "creador":
                print("ahora dime que prefieres")
                nivel5 = input("le armas solo AL 9 o a TODO EL EQUIPO por igual o A NADIE?").lower()

                if nivel5 == "todo el equipo":
                    print("tienes la posibilidad de elegir uno de los 3 titulos con el club cual prefieres?")
                    nivel6 = input("la COPA argentina, la LIGA argentina o la LIBERTADORES").lower()
                        
                    if nivel6 == "libertadores":
                        print("felicidades, eres campeón de la maxima competición americana!!")
                        nivel7 = input("ahora elige: QUEDARSE en el club, IRSE del club ").lower()
                            
                        if nivel7 == "quedarse en el club":
                            print("decides quedarte en el club y eso te suma minutos")
                            nivel8 = input("el tecnico necesita q juegues en otra posicion para cubrir un hueco decides ACEPTAR y sumar minutos o RECHAZAR y jugarm menos ").lower()                           
                            
                            if nivel8 == "aceptar":
                                print("aceptaste, te terminaste adaptando y ahora tienes un gran desempeño en esa posición")
                                nivel9 = input("pero ahora el tecnico te pregunta si prefieres QUEDARTE es esa posicion o VOLVER a tu posicion natural, que eliges? ").lower()
                            
                                if nivel9 == "quedarte":
                                    print("te quedaste y te convertiste en uno de los mejores en esa posicion")
                                    nivel10 = input("que prefieres. el MUNDIAL o el BALÓN DE ORO").lower()

                                    if nivel10 == "mundial":
                                        print("felicidades, te convertiste en uno de los mejores jugadores del mundo de america y pasaste a la historia. FIN DEL JUEGO")
                                    elif nivel10 == "balon de oro":
                                        print("felicidades, pasaste a la historia por ser el primer jugador de una liga americana en ganar el balon de oro. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                elif nivel9 == "volver":    
                                    print("decidiste volver a tu posición natural y la rompiste como nunca")
                                    nivel10 = input("que prefieres. el premio PUSKAS o la BOTA DE ORO").lower()

                                    if nivel10 == "puskas":
                                        print("felicidades, ganaste el puskas y lo ganaste todo con el club. FIN DEL JUEGO")
                                    elif nivel10 == "bota de oro":
                                        print("felicidades, ganaste la bota y te convertiste en leyenda delclub. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                else:
                                    print("error. respuesta no valida")     
                            elif nivel8 == "volver":
                                print("decides volver a tu posicion pero no regresas bien")
                                print("debido a tu frustacion empiezas a jugar con nervios y debido a eso no esquivas una patada que te lesiona y te obliga a dejar el futbol para siempre. FIN DEL JUEGO")
                            else:
                                print("Error. Respuesta no válida.")
                        elif nivel7 == "irse":
                            print("te vas del club, brillar durante unos años en un club europeo. pero las lesiones terminan bajando mucho tu nivel")
                            print("al final no consigues un impacto mundial y te retiras siendo un jugador mas del montón. FIN DEL JUEGO")
                        else:
                            print("Error. Respuesta no válida.")
                            
                    elif nivel6 == "copa":
                        print("ganas la copa y decides esforzarte aun mas")
                        print("al final te terminas llendo a club maximo rival en el cual brillas pero te vuelves odiado por mucha personas debido a tu traición")
                        nivel7 = input("pides DISCULPAS o lo IGNORAS? ").lower()

                        if nivel7 == "disculpas":
                            print("te disculpas, nadie las criticas bajas pero siguen ahi. te retiras como un jugador mas de ese club. FIN DEL JUEGO")
                        elif nivel1 == "ignoras":
                            print("pasas a la historia como el jugador que cometió la mayor traicion a un cub. FIN DEL JUEGO")
                        else:
                            print("error. respuesta no valida")
                    elif nivel6 == "liga":
                        print("te vuelves un gran jugador del club. pasas por otros grandes clubes de america y te retiras como n jugador reconocido internacionalmente. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                        
                elif nivel5 == "al 9":
                    print("gracias a eso ganan muchos trofeos, pero el resto del equipo te detesta y quiere q te vayas")
                    nivel6 = input("te VAS o te QUEDAS?").lower()

                    if nivel6 == "vas":
                        print("te vas a un club pequeño y tu carrera se estanca y te vuelves uno mas del monton. FIN DEL JUEGO")
                    elif nivel6 == "quedas":
                        print("decides quedarte. las crticas siguen pero gans muchos titulos y la aficion te adora")
                        print("pasas a la historia del club bajo el apodo de LA SOMBRA DEL 9. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                elif nivel5 == "nadie":
                    print("el egoismo es malo. no consigues un buen desempeño por no jugarenel equipo y te terminan echando")
                    print("te terminas llendo a un club arabe donde ganas mucho y no debes preocuparte por jugar al 200%. FIN DEL JUEGO")
                else:
                    print("Error. Respuesta no válida.")
                    
            elif nivel4 == "goleador":
                print("te conviertes en el 9 ideal. los clubes grandes quieren ficharte")
                nivel5 = input("VAS o te QUEDAS? ")

                if nivel5 == "vas":
                    print("te vas un club grande. ganas la champions siendo mvp en la final y ganas la bota de oro. Pasas a ser idolo del club. FINAL DEL JUEGO")
                elif nivel5 == "qudedas":
                    print("te conviertes en elmejor jugador de america y ganas la bota de oro pasando a la historia del futbol y del club. FIN DEL JUEGO")

            elif nivel4 == "defensor":
                print("cometes una falta de roja en la final de la libertadores. eso baja tu moral y confianza y pierdes el nivel de juego q tenias pasando a ser olvidado y vendido por el club.")
                print("FIN DEL JUEGO")
            else:
                print("Error. Respuesta no válida.")
                
        if nivel3 == "gremio":
            print("eligo tu rol en el equipo")
            nivel4 = input("CREADOR, GOLEADOR o DEFENSOR").lower()

            if nivel4 == "creador":
                print("ahora dime que prefieres")
                nivel5 = input("le armas solo AL 9 o a TODO EL EQUIPO por igual o A NADIE?").lower()

                if nivel5 == "todo el equipo":
                    print("tienes la posibilidad de elegir uno de los 3 titulos con el club cual prefieres?")
                    nivel6 = input("la COPA argentina, la LIGA argentina o la LIBERTADORES").lower()
                        
                    if nivel6 == "libertadores":
                        print("felicidades, eres campeón de la maxima competición americana!!")
                        nivel7 = input("ahora elige: QUEDARSE en el club, IRSE del club ").lower()
                            
                        if nivel7 == "quedarse en el club":
                            print("decides quedarte en el club y eso te suma minutos")
                            nivel8 = input("el tecnico necesita q juegues en otra posicion para cubrir un hueco decides ACEPTAR y sumar minutos o RECHAZAR y jugarm menos ").lower()                           
                            
                            if nivel8 == "aceptar":
                                print("aceptaste, te terminaste adaptando y ahora tienes un gran desempeño en esa posición")
                                nivel9 = input("pero ahora el tecnico te pregunta si prefieres QUEDARTE es esa posicion o VOLVER a tu posicion natural, que eliges? ").lower()
                            
                                if nivel9 == "quedarte":
                                    print("te quedaste y te convertiste en uno de los mejores en esa posicion")
                                    nivel10 = input("que prefieres. el MUNDIAL o el BALÓN DE ORO").lower()

                                    if nivel10 == "mundial":
                                        print("felicidades, te convertiste en uno de los mejores jugadores del mundo de america y pasaste a la historia. FIN DEL JUEGO")
                                    elif nivel10 == "balon de oro":
                                        print("felicidades, pasaste a la historia por ser el primer jugador de una liga americana en ganar el balon de oro. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                elif nivel9 == "volver":    
                                    print("decidiste volver a tu posición natural y la rompiste como nunca")
                                    nivel10 = input("que prefieres. el premio PUSKAS o la BOTA DE ORO").lower()

                                    if nivel10 == "puskas":
                                        print("felicidades, ganaste el puskas y lo ganaste todo con el club. FIN DEL JUEGO")
                                    elif nivel10 == "bota de oro":
                                        print("felicidades, ganaste la bota y te convertiste en leyenda delclub. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                else:
                                    print("error. respuesta no valida")     
                            elif nivel8 == "volver":
                                print("decides volver a tu posicion pero no regresas bien")
                                print("debido a tu frustacion empiezas a jugar con nervios y debido a eso no esquivas una patada que te lesiona y te obliga a dejar el futbol para siempre. FIN DEL JUEGO")
                            else:
                                print("Error. Respuesta no válida.")
                        elif nivel7 == "irse":
                            print("te vas del club, brillar durante unos años en un club europeo. pero las lesiones terminan bajando mucho tu nivel")
                            print("al final no consigues un impacto mundial y te retiras siendo un jugador mas del montón. FIN DEL JUEGO")
                        else:
                            print("Error. Respuesta no válida.")
                            
                    elif nivel6 == "copa":
                        print("ganas la copa y decides esforzarte aun mas")
                        print("al final te terminas llendo a club maximo rival en el cual brillas pero te vuelves odiado por mucha personas debido a tu traición")
                        nivel7 = input("pides DISCULPAS o lo IGNORAS? ").lower()

                        if nivel7 == "disculpas":
                            print("te disculpas, nadie las criticas bajas pero siguen ahi. te retiras como un jugador mas de ese club. FIN DEL JUEGO")
                        elif nivel1 == "ignoras":
                            print("pasas a la historia como el jugador que cometió la mayor traicion a un cub. FIN DEL JUEGO")
                        else:
                            print("error. respuesta no valida")
                    elif nivel6 == "liga":
                        print("te vuelves un gran jugador del club. pasas por otros grandes clubes de america y te retiras como n jugador reconocido internacionalmente. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                        
                elif nivel5 == "al 9":
                    print("gracias a eso ganan muchos trofeos, pero el resto del equipo te detesta y quiere q te vayas")
                    nivel6 = input("te VAS o te QUEDAS?").lower()

                    if nivel6 == "vas":
                        print("te vas a un club pequeño y tu carrera se estanca y te vuelves uno mas del monton. FIN DEL JUEGO")
                    elif nivel6 == "quedas":
                        print("decides quedarte. las crticas siguen pero gans muchos titulos y la aficion te adora")
                        print("pasas a la historia del club bajo el apodo de LA SOMBRA DEL 9. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                elif nivel5 == "nadie":
                    print("el egoismo es malo. no consigues un buen desempeño por no jugarenel equipo y te terminan echando")
                    print("te terminas llendo a un club arabe donde ganas mucho y no debes preocuparte por jugar al 200%. FIN DEL JUEGO")
                else:
                    print("Error. Respuesta no válida.")
                    
            elif nivel4 == "goleador":
                print("te conviertes en el 9 ideal. los clubes grandes quieren ficharte")
                nivel5 = input("VAS o te QUEDAS? ")

                if nivel5 == "vas":
                    print("te vas un club grande. ganas la champions siendo mvp en la final y ganas la bota de oro. Pasas a ser idolo del club. FINAL DEL JUEGO")
                elif nivel5 == "qudedas":
                    print("te conviertes en elmejor jugador de america y ganas la bota de oro pasando a la historia del futbol y del club. FIN DEL JUEGO")

            elif nivel4 == "defensor":
                print("cometes una falta de roja en la final de la libertadores. eso baja tu moral y confianza y pierdes el nivel de juego q tenias pasando a ser olvidado y vendido por el club.")
                print("FIN DEL JUEGO")
            else:
                print("Error. Respuesta no válida.")
        elif nivel3 == "santosfc":
            print("eligo tu rol en el equipo")
            nivel4 = input("CREADOR, GOLEADOR o DEFENSOR").lower()

            if nivel4 == "creador":
                print("ahora dime que prefieres")
                nivel5 = input("le armas solo AL 9 o a TODO EL EQUIPO por igual o A NADIE?").lower()

                if nivel5 == "todo el equipo":
                    print("tienes la posibilidad de elegir uno de los 3 titulos con el club cual prefieres?")
                    nivel6 = input("la COPA argentina, la LIGA argentina o la LIBERTADORES").lower()
                        
                    if nivel6 == "libertadores":
                        print("felicidades, eres campeón de la maxima competición americana!!")
                        nivel7 = input("ahora elige: QUEDARSE en el club, IRSE del club ").lower()
                            
                        if nivel7 == "quedarse en el club":
                            print("decides quedarte en el club y eso te suma minutos")
                            nivel8 = input("el tecnico necesita q juegues en otra posicion para cubrir un hueco decides ACEPTAR y sumar minutos o RECHAZAR y jugarm menos ").lower()                           
                            
                            if nivel8 == "aceptar":
                                print("aceptaste, te terminaste adaptando y ahora tienes un gran desempeño en esa posición")
                                nivel9 = input("pero ahora el tecnico te pregunta si prefieres QUEDARTE es esa posicion o VOLVER a tu posicion natural, que eliges? ").lower()
                            
                                if nivel9 == "quedarte":
                                    print("te quedaste y te convertiste en uno de los mejores en esa posicion")
                                    nivel10 = input("que prefieres. el MUNDIAL o el BALÓN DE ORO").lower()

                                    if nivel10 == "mundial":
                                        print("felicidades, te convertiste en uno de los mejores jugadores del mundo de america y pasaste a la historia. FIN DEL JUEGO")
                                    elif nivel10 == "balon de oro":
                                        print("felicidades, pasaste a la historia por ser el primer jugador de una liga americana en ganar el balon de oro. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                elif nivel9 == "volver":    
                                    print("decidiste volver a tu posición natural y la rompiste como nunca")
                                    nivel10 = input("que prefieres. el premio PUSKAS o la BOTA DE ORO").lower()

                                    if nivel10 == "puskas":
                                        print("felicidades, ganaste el puskas y lo ganaste todo con el club. FIN DEL JUEGO")
                                    elif nivel10 == "bota de oro":
                                        print("felicidades, ganaste la bota y te convertiste en leyenda delclub. FIN DEL JUEGO")
                                    else:
                                        print("error. respuesta no valida")
                                else:
                                    print("error. respuesta no valida")     
                            elif nivel8 == "volver":
                                print("decides volver a tu posicion pero no regresas bien")
                                print("debido a tu frustacion empiezas a jugar con nervios y debido a eso no esquivas una patada que te lesiona y te obliga a dejar el futbol para siempre. FIN DEL JUEGO")
                            else:
                                print("Error. Respuesta no válida.")
                        elif nivel7 == "irse":
                            print("te vas del club, brillar durante unos años en un club europeo. pero las lesiones terminan bajando mucho tu nivel")
                            print("al final no consigues un impacto mundial y te retiras siendo un jugador mas del montón. FIN DEL JUEGO")
                        else:
                            print("Error. Respuesta no válida.")
                            
                    elif nivel6 == "copa":
                        print("ganas la copa y decides esforzarte aun mas")
                        print("al final te terminas llendo a club maximo rival en el cual brillas pero te vuelves odiado por mucha personas debido a tu traición")
                        nivel7 = input("pides DISCULPAS o lo IGNORAS? ").lower()

                        if nivel7 == "disculpas":
                            print("te disculpas, nadie las criticas bajas pero siguen ahi. te retiras como un jugador mas de ese club. FIN DEL JUEGO")
                        elif nivel1 == "ignoras":
                            print("pasas a la historia como el jugador que cometió la mayor traicion a un cub. FIN DEL JUEGO")
                        else:
                            print("error. respuesta no valida")
                    elif nivel6 == "liga":
                        print("te vuelves un gran jugador del club. pasas por otros grandes clubes de america y te retiras como n jugador reconocido internacionalmente. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                        
                elif nivel5 == "al 9":
                    print("gracias a eso ganan muchos trofeos, pero el resto del equipo te detesta y quiere q te vayas")
                    nivel6 = input("te VAS o te QUEDAS?").lower()

                    if nivel6 == "vas":
                        print("te vas a un club pequeño y tu carrera se estanca y te vuelves uno mas del monton. FIN DEL JUEGO")
                    elif nivel6 == "quedas":
                        print("decides quedarte. las crticas siguen pero gans muchos titulos y la aficion te adora")
                        print("pasas a la historia del club bajo el apodo de LA SOMBRA DEL 9. FIN DEL JUEGO")
                    else:
                        print("Error. Respuesta no válida.")
                elif nivel5 == "nadie":
                    print("el egoismo es malo. no consigues un buen desempeño por no jugarenel equipo y te terminan echando")
                    print("te terminas llendo a un club arabe donde ganas mucho y no debes preocuparte por jugar al 200%. FIN DEL JUEGO")
                else:
                    print("Error. Respuesta no válida.")
                    
            elif nivel4 == "goleador":
                print("te conviertes en el 9 ideal. los clubes grandes quieren ficharte")
                nivel5 = input("VAS o te QUEDAS? ")

                if nivel5 == "vas":
                    print("te vas un club grande. ganas la champions siendo mvp en la final y ganas la bota de oro. Pasas a ser idolo del club. FINAL DEL JUEGO")
                elif nivel5 == "qudedas":
                    print("te conviertes en elmejor jugador de america y ganas la bota de oro pasando a la historia del futbol y del club. FIN DEL JUEGO")

            elif nivel4 == "defensor":
                print("cometes una falta de roja en la final de la libertadores. eso baja tu moral y confianza y pierdes el nivel de juego q tenias pasando a ser olvidado y vendido por el club.")
                print("FIN DEL JUEGO")
            else:
                print("Error. Respuesta no válida.")
        else:
            print("Error. Respuesta no válida.")
    elif nivel2 == "venezuela":
            print("da igual el club en el que juegues. no consigues salir de venezuela y pasar a tener un doble empleo (el futbol y trabajr en una cafeteria). FIN DEL JUEGO")

elif nivel1 == "europa":
    print("viajando a europa sufres un accidente de avion. sobrevives de milagro pero pierdes una de tus piernas, impidiendo cumplir tu sueño de ser futbolista profsionas. FIN DEL JUEGO")
else:
    print("error. respuesta no valida")