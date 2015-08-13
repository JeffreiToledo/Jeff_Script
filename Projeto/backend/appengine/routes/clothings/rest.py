# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from clothing_app import facade


def index():
    cmd = facade.list_clothings_cmd()
    clothing_list = cmd()
    short_form=facade.clothing_short_form()
    clothing_short = [short_form.fill_with_model(m) for m in clothing_list]
    return JsonResponse(clothing_short)


def save(**clothing_properties):
    cmd = facade.save_clothing_cmd(**clothing_properties)
    return _save_or_update_json_response(cmd)


def update(clothing_id, **clothing_properties):
    cmd = facade.update_clothing_cmd(clothing_id, **clothing_properties)
    return _save_or_update_json_response(cmd)


def delete(clothing_id):
    facade.delete_clothing_cmd(clothing_id)()


def _save_or_update_json_response(cmd):
    try:
        clothing = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.clothing_short_form()
    return JsonResponse(short_form.fill_with_model(clothing))

