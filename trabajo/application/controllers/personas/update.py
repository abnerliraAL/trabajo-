import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre,): 
        persona = config.model_personas.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update(persona)
    
    def POST(self, email, edad, apPat, apMat):
        formulario = web.input() # almacena los datos del formulario web
        nombre = formulario['nombre'] # almacena el nombre del input email
        email = formulario['email']
        edad = formulario['edad']
        apPat = formulario['apPat']
        apMat = formulario['apMat'] # almacena el email del input password
        config.model_personas.update_persona(nombre, email, edad, apPat, apMat) # actuliza los valores
        raise web.seeother('/') # redirecciona al index
