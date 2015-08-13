# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from model_app import facade
from routes.models.admin import new, edit


def delete(_handler, model_id):
    facade.delete_model_cmd(model_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_models_cmd()
    models = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.model_short_form()

    def short_model_dict(model):
        model_dct = short_form.fill_with_model(model)
        model_dct['edit_path'] = router.to_path(edit_path, model_dct['id'])
        model_dct['delete_path'] = router.to_path(delete_path, model_dct['id'])
        return model_dct

    short_models = [short_model_dict(model) for model in models]
    context = {'models': short_models,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

