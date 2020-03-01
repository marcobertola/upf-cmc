#!/usr/bin/env python3
from dialogs.dialogs import *
from nl import *
from nl import nlp
import random
from db.NFI import get_request_players


#################### LIST OF INTENTS ############################


def intent_has_verb_and_player(context):
    return context.has_verb and context.has_player_name


def intent_no_verb(context):
    return context.has_verb == False


def intent_not_has_budget(context):
    return context.has_budget == False


def intent_has_only_verb(context):
    return context.has_verb \
           and not context.has_attribute \
           and not context.has_player_role \
           and not context.has_quantifier \
           and not context.has_budget \
           and not context.has_player_name


def intent_is_ready_for_search(context):
    return context.has_verb \
           and context.has_attribute \
           and context.has_player_role \
           and context.has_quantifier \
           and context.has_budget \
           and context.category_verb == "find"


def intent_is_quit(context):
    return context.category_verb == "quit"


def intent_is_help(context):
    return context.category_verb == "help"


def intent_is_invalid(context):
    return not context.request_did_success


def intent_is_missing_role(context):
    return context.has_player_role is False


def intent_is_missing_attribute(context):
    return context.has_attribute is False


def intent_is_missing_quantifier(context):
    return context.has_quantifier is False


def intent_is_first_request(context):
    return context.request_is_the_first_one


def list_request_players_is_empty(list_request_player):
    return list_request_player == ""


def ask_for_budget(context, dialog):
    while intent_not_has_budget(context):
        dialog.processDialog(ID_ASK_FOR_BUDGET)
        budget = input("type from the keyboard (only digits):")
        if budget.isdigit():
            dialog.processDialog(ID_THANKS)
            context.budget_amount = budget
            context.has_budget = True
            return context
        else:
            dialog.processDialog(ID_BUDGET_NOT_VALID)


##############################################################


def process_logic(context, dialog):
    context = process_intents(context, dialog)
    return context


def process_intents(context, dialog):
    if intent_is_first_request(context):
        context.request_is_the_first_one = False

    if intent_is_invalid(context):
        dialog.processDialog(ID_INTENT_NOT_CLEAR)

    if intent_is_help(context):
        dialog.processDialog(ID_HELP)
        return context

    if intent_is_quit(context):
        context.request_is_still_active = False
        dialog.processDialog(ID_GOODBYE)
        return context

    if intent_no_verb(context):
        dialog.processDialog(ID_NO_VERB)
        return context

    if intent_has_only_verb(context):
        dialog.processDialog(ID_WELCOME)

    if intent_has_verb_and_player(context):
        if not context.has_confirmation:
            dialog.processDialog(ID_FIND_HAS_PLAYER_NAME, [context.player_name])
            player_details, no_results = get_request_players(context)
            print(player_details)
            dialog.processDialog(ID_CONFIRM_BUY_HIM)
            return context
        elif context.category_confirmation == "yes":
            dialog.processDialog(ID_PURCHASE_COMPLETE)
            context.request_is_still_active = False
            return context
        else:
            dialog.processDialog(ID_RESTART_QUERY)
            context.reset_for_new_search()
            return context

    if intent_not_has_budget(context):
        context = ask_for_budget(context, dialog)

    if intent_is_missing_role(context):
        dialog.processDialog(ID_ASK_PLAYER_ROLE)
        return context

    if intent_is_missing_attribute(context):
        dialog.processDialog(ID_ASK_ATTRIBUTE, [context.category_player_role])
        return context

    if intent_is_missing_quantifier(context):
        dialog.processDialog(ID_ASK_QUANTIFIER, [context.category_attribute, context.category_player_role])
        return context

    if intent_is_ready_for_search(context):
        if not context.has_confirmation:
            dialog.processDialog(ID_FIND_REQUEST_IS_READY, [context.category_player_role, context.quantifier_attribute,
                                                            context.category_attribute])
            list_request_player, no_results = get_request_players(context)

            if no_results:
                dialog.processDialog(ID_NO_RESULTS,
                                     [context.category_player_role, context.quantifier_attribute,
                                      context.category_attribute])
                context.reset_for_new_search()
                return context

            if list_request_players_is_empty(list_request_player):
                dialog.processDialog(ID_INCREASE_BUDGET)
                context.budget_amount = 0
                context.has_budget = False
                context.request_skip_input = True
                context = ask_for_budget(context, dialog)
                return context
            else:
                dialog.processDialog(ID_PLAYER_LIST)
                print(list_request_player)
                dialog.processDialog(ID_CONFIRM_BUY)
                return context

        elif context.category_confirmation == "yes":
            dialog.processDialog(ID_TELL_ME_NAME)
            return context

        else:
            dialog.processDialog(ID_RESTART_QUERY)
            context.reset_for_new_search()
            return context

    context.request_is_still_active = False
    return context
