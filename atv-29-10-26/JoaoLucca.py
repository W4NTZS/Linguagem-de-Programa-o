class JoaoLucca:
    def calcularMedia(nota):
        acum = 0
        for i in nota:
            acum+=i
        media = acum / len(nota)
        return media

    def validarNota(nota):
        validacao = nota < 0 or nota > 10
        return validacao        
