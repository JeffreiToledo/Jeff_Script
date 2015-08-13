# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from clothing_app import facade
from routes.clothings.admin import new, edit


def delete(_handler, clothing_id):
    facade.delete_clothing_cmd(clothing_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_clothings_cmd()
    clothings = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.clothing_short_form()

    def short_clothing_dict(clothing):
        clothing_dct = short_form.fill_with_model(clothing)
        clothing_dct['edit_path'] = router.to_path(edit_path, clothing_dct['id'])
        clothing_dct['delete_path'] = router.to_path(delete_path, clothing_dct['id'])
        return clothing_dct

    short_clothings = [short_clothing_dict(clothing) for clothing in clothings]
    context = {'clothings': short_clothings,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

