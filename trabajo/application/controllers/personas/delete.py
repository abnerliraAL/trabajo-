import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, nombre): 
        personas = config.model_personas.select_nombre(nombre)
        return config.render.delete(personas) 
    
    def POST(self, nombre):
        formulario = web.input() 
        nombre = formulario['nombre'] 
        email= formulario['email']
        edad= formulario['edad']
        apPat= formulario['apPat']
        apMat= formulario['apMat']
        config.model_personas.delete_persona(nombre) 
        raise web.seeother('/') # Redirecciona a raiz
