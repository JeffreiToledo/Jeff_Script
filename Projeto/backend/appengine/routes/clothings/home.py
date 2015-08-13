# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from clothing_app import facade
from routes.clothings import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_clothings_cmd()
    clothings = cmd()
    public_form = facade.clothing_public_form()
    clothing_public_dcts = [public_form.fill_with_model(clothing) for clothing in clothings]
    context = {'clothings': clothing_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

