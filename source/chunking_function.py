# # Copyright 2020, Yicong Hong <yicong.hong@anu.edu.au>. All rights reserved.

''' A heuristic based on word dependecies and governors '''

import json
import copy
import stanfordnlp
import numpy as np
from collections import Counter
from utils import Tokenizer, print_progress, check_lemma

def create_chunk(doc):

    max_kdx = len(doc.sentences) - 1
    instr_lemma = [['<start>']]
    for kdx, sent in enumerate(doc.sentences):

        root_sub = []; conj_sub = []
        for word in sent.words:
            if (word.dependency_relation == 'root'):
                root_sub.append(int(word.index))
            elif (word.dependency_relation == 'conj' and word.governor == 1) or (word.dependency_relation == 'conj' and (word.governor in root_sub or word.governor in conj_sub)):
                conj_sub.append(int(word.index))

        max_jdx = len(sent.words) - 1
        instr_lemma_sub = []; instr_depend_sub = []; instr_lemma_sub = []; ti = 0
        for jdx, word in enumerate(sent.words):
            if (word.dependency_relation == 'root') and (('root' in instr_depend_sub) or ('parataxis' in instr_depend_sub)):
                # print('1', word.lemma, instr_depend_sub)
                if len(instr_lemma_sub) >= 2:
                    ''' check for the special cases of turning and the word "and","then" '''
                    if (('advmod' in instr_depend_sub) or ('xcomp' in instr_depend_sub)) and ('obj' not in instr_depend_sub) and ('obl' not in instr_depend_sub) and ('nmod' not in instr_depend_sub):
                        if (instr_lemma[-1][-1] == 'and') or (instr_lemma_sub[0]=='and') or (instr_lemma[-1][-1] == 'then') or (instr_lemma_sub[0]=='then'):
                            instr_lemma[-1] += instr_lemma_sub
                            instr_lemma_sub = []; instr_depend_sub = []
                        else:
                            'add to the next chunk'
                    else:
                        # print('a', instr_lemma_sub)
                        instr_lemma.append(instr_lemma_sub)
                        instr_lemma_sub = []; instr_depend_sub = []

            elif ti <= len(conj_sub)-1:
                if word.governor == conj_sub[ti]:
                    ti += 1
                    # print('2', word.lemma, instr_depend_sub)
                    if len(instr_lemma_sub) >= 2:
                        ''' check for the special cases of turning and the word "and","then" '''
                        if (len(instr_lemma_sub) < 4) and (('advmod' in instr_depend_sub) or ('xcomp' in instr_depend_sub)) and ('obj' not in instr_depend_sub) and ('obl' not in instr_depend_sub) and ('nmod' not in instr_depend_sub):
                            if (instr_lemma[-1][-1] == 'and') or (instr_lemma_sub[0]=='and') or (instr_lemma[-1][-1] == 'then') or (instr_lemma_sub[0]=='then'):
                                instr_lemma[-1] += instr_lemma_sub
                                instr_lemma_sub = []; instr_depend_sub = []
                            else:
                                'add to the next chunk'
                        else:
                            # print('b', instr_lemma_sub)
                            instr_lemma.append(instr_lemma_sub)
                            instr_lemma_sub = []; instr_depend_sub = []

            elif (word.dependency_relation == 'parataxis') and (('root' in instr_depend_sub) or ('parataxis' in instr_depend_sub)):
                if len(instr_lemma_sub) >= 2:
                    ''' check for the special cases of turning and the word "and","then" '''
                    if (('advmod' in instr_depend_sub) or ('xcomp' in instr_depend_sub)) and ('obj' not in instr_depend_sub) and ('obl' not in instr_depend_sub) and ('nmod' not in instr_depend_sub):
                        if (instr_lemma[-1][-1] == 'and') or (instr_lemma_sub[0]=='and') or (instr_lemma[-1][-1] == 'then') or (instr_lemma_sub[0]=='then'):
                            instr_lemma[-1] += instr_lemma_sub
                            instr_lemma_sub = []; instr_depend_sub = []
                        else:
                            'add to the next chunk'
                    else:
                        instr_lemma.append(instr_lemma_sub)
                        instr_lemma_sub = []; instr_depend_sub = []

            if word.dependency_relation not in ['punct']:
                instr_lemma_sub.append(check_lemma(word))
                instr_depend_sub.append(word.dependency_relation)

        if len(instr_lemma_sub) >= 2:
            instr_lemma.append(instr_lemma_sub)
        else:
            instr_lemma[-1] += instr_lemma_sub

    return instr_lemma[1:]
