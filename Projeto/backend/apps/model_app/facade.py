# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from model_app.commands import ListModelCommand, SaveModelCommand, UpdateModelCommand, \
    ModelPublicForm, ModelDetailForm, ModelShortForm


def save_model_cmd(**model_properties):
    """
    Command to save Model entity
    :param model_properties: a dict of properties to save on model
    :return: a Command that save Model, validating and localizing properties received as strings
    """
    return SaveModelCommand(**model_properties)


def update_model_cmd(model_id, **model_properties):
    """
    Command to update Model entity with id equals 'model_id'
    :param model_properties: a dict of properties to update model
    :return: a Command that update Model, validating and localizing properties received as strings
    """
    return UpdateModelCommand(model_id, **model_properties)


def list_models_cmd():
    """
    Command to list Model entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListModelCommand()


def model_detail_form(**kwargs):
    """
    Function to get Model's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ModelDetailForm(**kwargs)


def model_short_form(**kwargs):
    """
    Function to get Model's short form. just a subset of model's properties
    :param kwargs: form properties
    :return: Form
    """
    return ModelShortForm(**kwargs)

def model_public_form(**kwargs):
    """
    Function to get Model'spublic form. just a subset of model's properties
    :param kwargs: form properties
    :return: Form
    """
    return ModelPublicForm(**kwargs)


def get_model_cmd(model_id):
    """
    Find model by her id
    :param model_id: the model id
    :return: Command
    """
    return NodeSearch(model_id)


def delete_model_cmd(model_id):
    """
    Construct a command to delete a Model
    :param model_id: model's id
    :return: Command
    """
    return DeleteNode(model_id)

