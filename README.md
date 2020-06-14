# Fine-Grained R2R
Code and data of the Fine-Grained-R2R Dataset proposed in paper **Sub-Instruction Aware Vision-and-Language Navigation**.

* The code and data are pre-released and confidential to close collaborators/colleagues only, the copyright resides with the authors of the paper Sub-Instruction Aware Vision-and-Language Navigation, please do not distribute.
* This dataset is build upon the [Room-to-Room (R2R) dataset](https://github.com/peteanderson80/Matterport3DSimulator/tree/master/tasks/R2R), we refer the readers to its repository for more details.

## data
The Fine-Grained R2R data, which enriches the R2R dataset with sub-instructions and their corresponding paths. The overall instruction and trajectory of each sample remains the same.

* For paths in the train, the validation seen and the validation unseen splits, we add two new entries:
  * **new_instructions**: A list of sub-instructions produced by the **Chunking Function** from the complete instructions.
  * **chunk_view**: A list of sub-paths corresponding to the sub-instructions, where each number in the list is an index of a viewpoint in the ground-truth path. The index starts at 1.
  
* Some sub-instructions which refer to camera rotation or a *STOP* action could match to a single viewpoint.

* For the test unseen split, we only provide the sub-instructions but not the sub-paths.

## source
The code of the proposed **Chunking Function** for generating sub-instructions.

* Install the [StanfordNLP package](https://github.com/stanfordnlp/stanza/) ([v0.1.2](https://pypi.org/project/stanfordnlp/0.1.2/) in our experiment) and download the English models for the neural pipeline.

* Run *make_subinstr.py* to generate data with sub-instructions from the original R2R data.

* The generated files had been sent to AMT for annotating the sub-paths.



