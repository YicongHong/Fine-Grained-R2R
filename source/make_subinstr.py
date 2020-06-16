# # Copyright 2020, Yicong Hong <yicong.hong@anu.edu.au>. All rights reserved.

import json
import copy
import stanfordnlp
import numpy as np
from collections import Counter
from utils import Tokenizer, print_progress, check_lemma
from chunking_function import create_chunk

if __name__ == '__main__':

    split = 'train' # 'test', 'val_seen', 'val_unseen'
    source = './R2R-original/R2R_{}.json'.format(split)
    target = './output_subinstr/FGR2R_{}.json'.format(split)

    with open(source,'r') as f_:
        data = json.load(f_)

    nlp = stanfordnlp.Pipeline()
    new_data = copy.deepcopy(data)

    total_length = len(data)

    for idx, item in enumerate(data):
        new_instr = []
        for instr in item['instructions'][0:3]:
            doc = nlp(instr)

            ''' break a sentence using the chunking function '''
            instr_lemma = create_chunk(doc)

            # build the new instruction list with breakdowned sentences
            new_instr.append(instr_lemma)

        # merge into the data dictionary
        new_data[idx]['new_instructions'] = str(new_instr)
        print_progress(idx + 1, total_length, prefix='Progress:', suffix='Complete', bar_length=50)

    with open(target, 'a') as file_:
        json.dump(new_data, file_, ensure_ascii=False, indent=4)


    ''' individual samples '''
    # instrs = [
    #     "Head straight until you pass the wall with holes in it the turn left and wait by the glass table with the white chairs. ",
    #     'Facing the three archways go forward and immediately right, go through the rectangular archway and go into the first room on your left, go along the table, and stop at the chairs.',
    #     'With the stone pillar on your right and the table on your left walk into the main room going forward and passing the tennis table on your left go between the work tables and go forward to the table and stop in front of the table in front of the love seat.',
    #     'Leaving the room facing the wall in the hallway take a left and go down the hallway straight ahead down the hall and taking a left into the last bedroom in the second door on the left on the at the end of this hall before entering the next hallway.',
    #     'Go downstairs, turn left and wait to the right outside.'
    # ]
    #
    # nlp = stanfordnlp.Pipeline()
    # for ii, instr in enumerate(instrs):
    #     doc = nlp(instr)
    #
    #     instr_lemma = create_chunk(doc)
    #     print(ii, '------------')
    #     print(instr)
    #     print(instr_lemma)
