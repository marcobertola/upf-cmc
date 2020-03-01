#!/usr/bin/env python
# coding: utf8
"""
Author: marco_bertola
"""


class RequestContext:

    def __init__(self):
        self.request_is_still_active = True
        self.request_did_success = False
        self.request_is_the_first_one = False
        self.request_skip_input = False

        self.has_verb = False
        self.category_verb = ""

        self.has_attribute = False
        self.category_attribute = ""

        self.has_quantifier = False
        self.quantifier_attribute = ""

        self.has_player_role = False
        self.category_player_role = ""

        self.has_budget = False
        self.budget_amount = 0

        self.has_player_name = False
        self.player_name = ""

        self.has_confirmation = False
        self.category_confirmation = ""

    def reset_for_new_search(self):
        self.__init__()
        self.has_verb = True
        self.category_verb = "find"

    def trace(self):
        print("\n******CONTEXT******")
        print("has_verb\t", self.has_verb)
        print("category_verb\t", self.category_verb)
        print("has_attribute\t", self.has_attribute)
        print("category_attribute\t", self.category_attribute)
        print("has_quantifier\t", self.has_quantifier)
        print("quantifier_attribute\t", self.quantifier_attribute)
        print("has_player_role\t", self.has_player_role)
        print("category_player_role\t", self.category_player_role)
        print("has_budget\t", self.has_budget)
        print("budget_amount\t", self.budget_amount)
        print("has_player_name\t", self.has_player_name)
        print("player_name\t", self.player_name)
        print("request_is_still_active\t", self.request_is_still_active)
        print("request_did_success\t", self.request_did_success)
        print("has_confirmation\t", self.has_confirmation)
        print("category_confirmation\t", self.category_confirmation)
        print("************")
