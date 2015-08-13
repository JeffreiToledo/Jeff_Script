# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from model_app import facade
from routes.models import admin


@no_csrf
def index(model_id):
    model = facade.get_model_cmd(model_id)()
    detail_form = facade.model_detail_form()
    context = {'save_path': router.to_path(save, model_id), 'model': detail_form.fill_with_model(model)}
    return TemplateResponse(context, 'models/admin/form.html')


def save(_handler, model_id, **model_properties):
    cmd = facade.update_model_cmd(model_id, **model_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'model': cmd.form}

        return TemplateResponse(context, 'models/admin/form.html')
    _handler.redirect(router.to_path(admin))

