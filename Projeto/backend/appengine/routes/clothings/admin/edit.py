# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from clothing_app import facade
from routes.clothings import admin


@no_csrf
def index(clothing_id):
    clothing = facade.get_clothing_cmd(clothing_id)()
    detail_form = facade.clothing_detail_form()
    context = {'save_path': router.to_path(save, clothing_id), 'clothing': detail_form.fill_with_model(clothing)}
    return TemplateResponse(context, 'clothings/admin/form.html')


def save(_handler, clothing_id, **clothing_properties):
    cmd = facade.update_clothing_cmd(clothing_id, **clothing_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'clothing': cmd.form}

        return TemplateResponse(context, 'clothings/admin/form.html')
    _handler.redirect(router.to_path(admin))

