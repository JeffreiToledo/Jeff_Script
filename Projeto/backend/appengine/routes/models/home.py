# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from model_app import facade
from routes.models import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_models_cmd()
    models = cmd()
    public_form = facade.model_public_form()
    model_public_dcts = [public_form.fill_with_model(model) for model in models]
    context = {'models': model_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

