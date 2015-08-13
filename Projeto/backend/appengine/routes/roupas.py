# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router
from gaegraph.model import Node, Arc
from google.appengine.ext import ndb
from gaeforms.base import Form
from gaeforms import base
from gaeforms.ndb.form import ModelForm
from tekton.gae.middleware.redirect import RedirectResponse



@no_csrf
def index(_logged_user):
   chave_do_usuario = _logged_user.key
   query=AutorArco.query(AutorArco.origin==chave_do_usuario)
   autor_arcos = query.fetch()
   chaves_de_roupas=[arco.destination for arco in autor_arcos]
   roupa_lista = ndb.get_multi(chaves_de_roupas)
   form=RoupaFormTable()
   roupa_lista=[form.fill_with_model(roupa) for roupa in roupa_lista]
   editar_form_path=router.to_path(editar_form)
   delete_path = router.to_path(delete)
   for roupa in roupa_lista:
       roupa['edit_path']='%s/%s'%(editar_form_path,roupa['id'])
       roupa['delete_path']='%s/%s'%(delete_path,roupa['id'])
   contexto = {'roupa_lista':roupa_lista}
   return TemplateResponse(contexto)

def delete(roupa_id):
    chave = ndb.Key(Roupa,int(roupa_id))
    chave.delete()
    return RedirectResponse(router.to_path(index))

@no_csrf
def editar_form(roupa_id):
    roupa_id=int(roupa_id)
    roupa = Roupa.get_by_id(roupa_id)
    roupa_form=RoupaForm()
    roupa_form.fill_with_model(roupa)
    contexto = {'salvar_path': router.to_path(editar,roupa_id), 'roupa':roupa_form}
    return TemplateResponse(contexto, 'roupas/form.html')

def editar(roupa_id, **propriedades):
    roupa_id=int(roupa_id)
    roupa=Roupa.get_by_id(roupa_id)
    roupa_form = RoupaForm(**propriedades)
    erros = roupa_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar), 'erros': erros, 'roupas': roupa_form}
        return TemplateResponse(contexto, 'roupas/form.html')
    else:
        roupa_form.fill_model(roupas)
        roupa.put()
        return RedirectResponse(router.to_path(index))


@no_csrf
def form():
    contexto={'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


class Roupa(Node):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty()
    release = ndb.DateProperty(auto_now=True)


class RoupaForm(ModelForm):
    _model_class = Roupa
    _include = [Roupa.price, Roupa.release, Roupa.title]



class AutorArco(Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Roupa, required=True)

class BookFormTable(Node):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty()
    release = ndb.DateProperty(auto_now=True)



def salvar(_resp, **propriedades):
    roupa_form = RoupaForm(**propriedades)
    erros = roupa_form.validate()
    if erros:
        #_resp.write(erros)
        contexto={'salvar_path': router.to_path(salvar), 'erros' : erros, 'roupas': roupa_form}
        return TemplateResponse(contexto,'roupas/form.html')
    else:
        pass

        roupa = roupa_form.fill_model()
        chave_da_roupa = roupa.put()
        chave_de_usuario = _logged_user.key
        autor_arco = AutorArco(origin=chave_de_usuario, destination=chave_da_roupa)
        autor_arco.put()

        return RedirectResponse(router.to_path(index))