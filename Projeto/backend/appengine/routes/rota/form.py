# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router

'''@permission(ADMIN, GEREMNTE)'''
@login_not_required
@no_csrf
def index():
    contexto={'save_path': router.to_path(salvar)}
    return TemplateResponse(contexto)

@login_not_required
def salvar(_resp, nome):
    _resp.write(nome)

@login_not_required
@no_csrf
def usuario(_resp, _logged_user):
    _resp.write('Usuário Logado %s'%_logged_user)