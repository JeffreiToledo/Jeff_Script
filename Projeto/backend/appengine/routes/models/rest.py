# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from model_app import facade


def index():
    cmd = facade.list_models_cmd()
    model_list = cmd()
    short_form=facade.model_short_form()
    model_short = [short_form.fill_with_model(m) for m in model_list]
    return JsonResponse(model_short)


def save(**model_properties):
    cmd = facade.save_model_cmd(**model_properties)
    return _save_or_update_json_response(cmd)


def update(model_id, **model_properties):
    cmd = facade.update_model_cmd(model_id, **model_properties)
    return _save_or_update_json_response(cmd)


def delete(model_id):
    facade.delete_model_cmd(model_id)()


def _save_or_update_json_response(cmd):
    try:
        model = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.model_short_form()
    return JsonResponse(short_form.fill_with_model(model))

