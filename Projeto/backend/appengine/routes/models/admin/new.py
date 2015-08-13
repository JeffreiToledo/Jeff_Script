# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from model_app import facade
from routes.models import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'models/admin/form.html')


def save(_handler, model_id=None, **model_properties):
    cmd = facade.save_model_cmd(**model_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'model': cmd.form}

        return TemplateResponse(context, 'models/admin/form.html')
    _handler.redirect(router.to_path(admin))

