#!/usr/bin/env python
# coding: utf8
"""
Author: marco_bertola
"""
import re


class Semantic:
    infers = {}

    @staticmethod
    def check_infers(token, context):

        for key in Semantic.infers:
            if token == key:
                info = Semantic.infers.get(key)
                if info[0] == "has_attribute":
                    context.has_attribute = True
                    context.category_attribute = info[1]
                if info[0] == "has_quantifier":
                    context.has_quantifier = True
                    context.quantifier_attribute = info[1]

    def compute_infer(self, token, rules):
        m = re.search('\[(.+?)\]', rules)
        text = m.group(1)
        items = text.split(";")
        context_info = [items[1], items[2]]
        self.infers[token] = context_info

    def category(self, token):

        for key, value in self.semantics.items():
            if str(token) in value:
                return key
        return ""

    def trace(self):
        print(self.semantics)

    def get_all_values(self):

        elements = []
        for items in self.semantics.values():
            for item in items:
                elements.append(item)
        return elements

    def _build_tree(self, file):
        self.__recurse_tree(None, 0, file, self.semantics)

    def __recurse_tree(self, parent, depth, source, semantic):

        last_line = source.readline().rstrip()
        while last_line:
            tabs = last_line.count('\t')
            if tabs < depth:
                break
            node = last_line.strip()
            if tabs >= depth:
                if parent is not None:
                    nodes = node.split("->")
                    node = nodes[0]
                    if len(nodes) > 1:
                        self.compute_infer(node, nodes[1])
                    if parent in semantic.keys():
                        semantic[parent].append(node)
                    else:
                        synonymous = [node]
                        semantic[parent] = synonymous
                last_line = self.__recurse_tree(node, tabs + 1, source, semantic)

        return last_line


class SemanticVerb(Semantic):
    semantics = {}

    def __init__(self):
        self._build_tree(open("nl/voc/verb.voc"))


class SemanticPlayerAttribute(Semantic):
    semantics = {}

    def __init__(self):
        self._build_tree(open("nl/voc/playerAttribute.voc"))


class SemanticAttributeQuantifier(Semantic):
    semantics = {}

    def __init__(self):
        self._build_tree(open("nl/voc/attributeQuantifier.voc"))


class SemanticPlayerRole(Semantic):
    semantics = {}

    def __init__(self):
        self._build_tree(open("nl/voc/playerRole.voc"))


class SemanticConfirmation(Semantic):
    semantics = {}

    def __init__(self):
        self._build_tree(open("nl/voc/confirmation.voc"))


class SemanticPlayerName(Semantic):
    semantics = {}

    def __init__(self):
        self._build_tree(open("nl/data_feed/feed_players.lst"))
