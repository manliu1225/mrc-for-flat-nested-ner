#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 



# Author: Xiaoy LI 
# Description:
# mrc_ner_data_processor.py


import os
from data_loader.mrc_utils import read_mrc_ner_examples 



class QueryNERProcessor(object):
    # processor for the query-based ner dataset 
    # change
    def get_train_examples(self, data_dir):
    # def get_train_examples(self, file, data_dir):
        data = read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.train"))
        # data = read_mrc_ner_examples(os.path.join(data_dir, file))
        return data

    def get_dev_examples(self, data_dir):
    # def get_dev_examples(self, file, data_dir):
        return read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.dev"))
        # return read_mrc_ner_examples(os.path.join(data_dir, file))

    def get_test_examples(self, data_dir):
    # def get_test_examples(self, file, data_dir):
        return read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.test"))
        # return read_mrc_ner_examples(os.path.join(data_dir, file))


class Conll03Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["ORG", "PER", "LOC", "MISC", "O"]


class MSRAProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["NS", "NR", "NT", "O"]


class Onto4ZhProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["LOC", "PER", "GPE", "ORG", "O"]


class Onto5EngProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ['ORDINAL', 'CARDINAL', 'LOC', 'WORK_OF_ART', 'LANGUAGE', 'ORG', 'FAC', 'PERSON', 'EVENT', 'TIME', 'LAW', 'NORP', 'PERCENT', 'DATE', 'GPE', 'QUANTITY', 'PRODUCT', 'MONEY', 'O']


class ResumeZhProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["ORG", "LOC", "NAME", "RACE", "TITLE", "EDU", "PRO", "CONT", "O"]


class GeniaProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ['cell_line', 'cell_type', 'DNA', 'RNA', 'protein', "O"]


class ACE2005Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["GPE", "ORG", "PER", "FAC", "VEH", "LOC", "WEA", "O"]


class ACE2004Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["GPE", "ORG", "PER", "FAC", "VEH", "LOC", "WEA", "O"]








