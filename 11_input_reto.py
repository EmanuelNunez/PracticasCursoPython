print('Responde las siguientes preguntas con un "SI" o un "NO"')
calificacion = 0

pregunta1 = input('Me gustan los gatos?')
if pregunta1 == 'SI':
    calificacion += 1

pregunta2 = input('Mi color favorito es Azul')
if pregunta2 == 'SI':
    calificacion += 1

pregunta3 = input('Me gustan los tacos?')
if pregunta3 == 'SI':
    calificacion += 1

print(calificacion)
