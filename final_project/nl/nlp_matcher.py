from __future__ import unicode_literals, print_function

import plac
from spacy.lang.en import English
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc, Span, Token
from nl import semantics


class Recognizer(object):
    name = ""
    extension = ""

    def __call__(self, doc):
        matches = self.matcher(doc)
        spans = []
        for _, start, end in matches:
            entity = Span(doc, start, end, label=self.label)
            spans.append(entity)
            for token in entity:
                token._.set(self.extension, True)
            doc.ents = list(doc.ents) + [entity]
        for span in spans:
            span.merge()
        return doc  # don't forget to return the Doc!


##########################################################################

class VerbRecognizer(Recognizer):
    name = "VERB"
    extension = "has_verb"

    def __init__(self, nlp, semantic):
        elements = semantic.get_all_values()
        self.label = nlp.vocab.strings[self.name]

        patterns = [nlp(org) for org in elements]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add(self.name, None, *patterns)

        Token.set_extension(self.extension, default=False, force=True)
        Doc.set_extension(self.extension, getter=self.has_verb, force=True)
        Span.set_extension(self.extension, getter=self.has_verb, force=True)

    def has_verb(self, tokens):
        return any([t._.get(self.extension) for t in tokens])

    def match(self, token, context, semantic):
        if token._.has_verb:
            context.has_verb = True
            context.category_verb = semantic.category(token)
        return token._.has_verb


##########################################################################

class PlayerAttributeRecognizer(Recognizer):
    name = "NOUN"
    extension = "has_attribute"

    def __init__(self, nlp, semantic):
        elements = semantic.get_all_values()
        self.label = nlp.vocab.strings[self.name]

        patterns = [nlp(org) for org in elements]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add(self.name, None, *patterns)

        Token.set_extension(self.extension, default=False, force=True)
        Doc.set_extension(self.extension, getter=self.has_attribute, force=True)
        Span.set_extension(self.extension, getter=self.has_attribute,force=True)

    def has_attribute(self, tokens):
        return any([t._.get(self.extension) for t in tokens])

    def match(self, token, context, semantic):
        if token._.has_attribute:
            context.has_attribute = True
            context.category_attribute = semantic.category(token)
        return token._.has_attribute


##########################################################################

class AttributeQuantifierRecognizer(Recognizer):
    name = "ADJ"
    extension = "has_quantifier"

    def __init__(self, nlp, semantic):
        elements = semantic.get_all_values()
        self.label = nlp.vocab.strings[self.name]

        patterns = [nlp(org) for org in elements]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add(self.name, None, *patterns)

        Token.set_extension(self.extension, default=False, force=True)
        Doc.set_extension(self.extension, getter=self.has_quantifier, force=True)
        Span.set_extension(self.extension, getter=self.has_quantifier, force=True)

    def has_quantifier(self, tokens):
        return any([t._.get(self.extension) for t in tokens])

    def match(self, token, context, semantic):
        if token._.has_quantifier:
            context.has_quantifier = True
            context.quantifier_attribute = semantic.category(token)
        return token._.has_quantifier

##########################################################################


class PlayerRoleRecognizer(Recognizer):
    name = "NOUN_ROLE"
    extension = "has_player_role"

    def __init__(self, nlp, semantic):
        elements = semantic.get_all_values()
        self.label = nlp.vocab.strings[self.name]

        patterns = [nlp(org) for org in elements]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add(self.name, None, *patterns)

        Token.set_extension(self.extension, default=False, force= True)
        Doc.set_extension(self.extension, getter=self.has_player_role, force=True)
        Span.set_extension(self.extension, getter=self.has_player_role, force=True)

    def has_player_role(self, tokens):
        return any([t._.get(self.extension) for t in tokens])

    def match(self, token, context, semantic):
        if token._.has_player_role:
            context.has_player_role = True
            context.category_player_role = semantic.category(token)
        return token._.has_player_role

##########################################################################


class PlayerNameRecognizer(Recognizer):
    name = "PLAYER_NAME"
    extension = "has_player_name"

    def __init__(self, nlp, semantic):
        elements = semantic.get_all_values()
        self.label = nlp.vocab.strings[self.name]

        patterns = [nlp(org) for org in elements]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add(self.name, None, *patterns)

        Token.set_extension(self.extension, default=False, force= True)
        Doc.set_extension(self.extension, getter=self.has_player_name, force=True)
        Span.set_extension(self.extension, getter=self.has_player_name, force=True)

    def has_player_name(self, tokens):
        return any([t._.get(self.extension) for t in tokens])

    def match(self, token, context, semantic):
        if token._.has_player_name:
            context.has_player_name = True
            context.player_name = token
        return token._.has_player_name

##########################################################################

class ConfirmationRecognizer(Recognizer):
    name = "CONFIRMATION"
    extension = "has_confirmation"

    def __init__(self, nlp, semantic):
        elements = semantic.get_all_values()
        self.label = nlp.vocab.strings[self.name]

        patterns = [nlp(org) for org in elements]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add(self.name, None, *patterns)

        Token.set_extension(self.extension, default=False, force= True)
        Doc.set_extension(self.extension, getter=self.has_confirmation, force=True)
        Span.set_extension(self.extension, getter=self.has_confirmation, force=True)

    def has_confirmation(self, tokens):
        return any([t._.get(self.extension) for t in tokens])

    def match(self, token, context, semantic):
        if token._.has_confirmation:
            context.has_confirmation = True
            context.category_confirmation = semantic.category(token)
        return token._.has_confirmation

##########################################################################
