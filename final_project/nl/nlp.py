#!/usr/bin/env python
# coding: utf8
"""
Author: marco_bertola
"""
from __future__ import unicode_literals, print_function
from spacy.lang.en import English
from nl import nlp_matcher
from nl import semantics
from nl.semantics import Semantic

DEBUG = False


class Nlp:
    nlp = English()

    def __init__(self):
        self.verb_semantic = semantics.SemanticVerb()
        self.matcher_verb = nlp_matcher.VerbRecognizer(self.nlp, self.verb_semantic)
        self.nlp.add_pipe(self.matcher_verb, last=True)

        self.attribute_semantic = semantics.SemanticPlayerAttribute()
        self.matcher_attribute = nlp_matcher.PlayerAttributeRecognizer(self.nlp, self.attribute_semantic)
        self.nlp.add_pipe(self.matcher_attribute, last=True)

        self.quantifier_semantic = semantics.SemanticAttributeQuantifier()
        self.matcher_quantifier = nlp_matcher.AttributeQuantifierRecognizer(self.nlp, self.quantifier_semantic)
        self.nlp.add_pipe(self.matcher_quantifier, last=True)

        self.player_role_semantic = semantics.SemanticPlayerRole()
        self.matcher_player_role = nlp_matcher.PlayerRoleRecognizer(self.nlp, self.player_role_semantic)
        self.nlp.add_pipe(self.matcher_player_role, last=True)

        self.player_name_semantic = semantics.SemanticPlayerName()
        self.matcher_player_name = nlp_matcher.PlayerNameRecognizer(self.nlp, self.player_name_semantic)
        self.nlp.add_pipe(self.matcher_player_name, last=True)

        self.confirmation_semantic = semantics.SemanticConfirmation()
        self.matcher_confirmation = nlp_matcher.ConfirmationRecognizer(self.nlp, self.confirmation_semantic)
        self.nlp.add_pipe(self.matcher_confirmation, last=True)

    def process(self, text, context):

        doc = self.nlp(text)

        context.request_did_success = False
        context.has_confirmation = False
        context.category_confirmation = ""
        for token in doc:
            if self.matcher_verb.match(token, context, self.verb_semantic):
                context.request_did_success = True
            if self.matcher_attribute.match(token, context, self.attribute_semantic):
                context.request_did_success = True
            if self.matcher_quantifier.match(token, context, self.quantifier_semantic):
                context.request_did_success = True
            if self.matcher_player_role.match(token, context, self.player_role_semantic):
                context.request_did_success = True
            if self.matcher_player_name.match(token, context, self.player_name_semantic):
                context.request_did_success = True
            if self.matcher_confirmation.match(token, context, self.confirmation_semantic):
                context.request_did_success = True
            Semantic.check_infers(token.lemma_, context)

        if DEBUG:
            self.debug_log(doc)

        return context

    def debug_log(self, doc):

        print("Pipeline", self.nlp.pipe_names)  # pipeline contains component name
        print("Tokens", [t.text for t in doc])  # company names from the list are merged

        for token in doc:
            print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}".format(
                token.text,
                token.idx,
                token.lemma_,
                token.is_punct,
                token.is_space,
                token.shape_,
                token.pos_,
                token.tag_
            ))
        print("Entities", [(e.text, e.label_) for e in doc.ents])


def main():
    text = str(input("Write something:\n"))
    nlp = Nlp()
    nlp.process(text)


if __name__ == "__main__":
    main()
