# Fine-Grained R2R
Code and data of the Fine-Grained R2R Dataset proposed in paper [**Sub-Instruction Aware Vision-and-Language Navigation**](https://arxiv.org/abs/2004.02707).

This dataset enriches the benchmark Room-to-Room (R2R) dataset by dividing the instructions into sub-instructions and pairing each of those with their corresponding viewpoints in the path.

* The copyright resides with the authors of the paper Sub-Instruction Aware Vision-and-Language Navigation.
* This dataset is build upon the [Room-to-Room (R2R)](https://github.com/peteanderson80/Matterport3DSimulator/tree/master/tasks/R2R) dataset, we refer the readers to its repository for more details.

## Data
The Fine-Grained R2R data, which enriches the R2R dataset with sub-instructions and their corresponding paths. The overall instruction and trajectory of each sample remains the same.

* For paths in the train, the validation seen and the validation unseen splits, we add two new entries:
  * **new_instructions**: A list of sub-instructions produced by the **Chunking Function** from the complete instructions. You can use ```import ast``` and ```ast.literal_eval()``` to read it a list.
  * **chunk_view**: A list of sub-paths corresponding to the sub-instructions, where each number in the list is an index of a viewpoint in the ground-truth path. The index starts at 1.
  
* Some sub-instructions which refer to camera rotation or a *STOP* action could match to a single viewpoint.

* For the test unseen split, we only provide the sub-instructions but not the sub-paths.

## Source
The code of the proposed **Chunking Function** for generating sub-instructions.

* Install the [StanfordNLP package](https://github.com/stanfordnlp/stanza/) ([v0.1.2](https://pypi.org/project/stanfordnlp/0.1.2/) in our experiment) and download the English models for the neural pipeline.

* Run ```make_subinstr.py``` to generate data with sub-instructions from the original R2R data.

* The generated files had been sent to the [Amazon Mechanical Turk](https://www.mturk.com/) (AMT) for annotating the sub-paths.

## Reference
If you use or dicsuss the Fine-Grained R2R dataset in your work, please cite our paper:
```
@article{hong2020sub,
  title={Sub-Instruction Aware Vision-and-Language Navigation},
  author={Hong, Yicong and Rodriguez-Opazo, Cristian and Wu, Qi and Gould, Stephen},
  journal={arXiv preprint arXiv:2004.02707},
  year={2020}
}
```
This paper is currently under review, we will release the latest version online soon.

## Contact

If you have any question regarding the dataset or publication, please create an issue in this repository or email to yicong.hong@anu.edu.au.
