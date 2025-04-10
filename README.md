# Rethinking Reflection in Pre-Training

This repository contains various resources for the paper [Rethinking Reflection in Pre-Training](https://arxiv.org/abs/2504.04022) by Essential AI.
- [Prompts](#prompts)
- [Results](#results)
- [Tasks](#tasks)
- [Classifier](#classifier)
- [Datasets](https://huggingface.co/collections/EssentialAI/rethinking-reflection-in-pre-training-67f69f2374a7d50cc5c325ea) (on Hugging Face)

**Updates:**
* 2025-04 - we released [our paper](https://arxiv.org/abs/2504.04022) and made this [announcement](https://x.com/ashVaswani/status/1909642828554387675).

## Abstract
A language model’s ability to reflect on its own reasoning provides a key advantage for solving
complex problems. While most recent research has focused on how this ability develops during
reinforcement learning, we show that it actually begins to emerge much earlier—during the
model’s pre-training. To study this, we introduce deliberate errors into chains-of-thought and
test whether the model can still arrive at the correct answer by recognizing and correcting these
mistakes. By tracking performance across different stages of pre-training, we observe that this
self-correcting ability appears early and improves steadily over time. For instance, an OLMo-2-
7B model pre-trained on 4 trillion tokens displays self-correction on our six self-reflection
tasks.

## Prompts
As detailed in our paper, we modified existing datasets to create adversarial datasets that can elicit reflection behavior from LLMs. Our modifications involved prompting LLMs and the `prompts/` directory includes the specific instructions for each dataset.

## Results
Our experiments produced a substantial volume of results and samples JSON files. These will be released soon via Essential AI's [Hugging Face hub](https://huggingface.co/EssentialAI). In the meantime, in `results/`  we share csv files that collate our results, along with the plots from our paper and the code used to create them. 

## Tasks
Our experiments utilized the EleutherAI [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness). We created custom tasks, which are available in `tasks/`: 

* `bbh_adv`
* `cruxeval_i_adv`
* `cruxeval_o_adv`
* `gsm8k_adv`
* `gsm8k-platinum_adv`
* `triviaqa_adv`

### To get started:

Install `lm-eval` as per the LM-Evaluation Harness instructions [here](https://github.com/EleutherAI/lm-evaluation-harness?tab=readme-ov-file#install).

Next, `git clone https://github.com/Essential-AI/reflection.git`. 

Then, when calling `lm-eval`, include some or all of our custom task names, along with the `--include_path` flag and the path to `reflection/tasks/`. For example:

```
lm_eval --model hf \
    --tasks bbh_adv,cruxeval_i_adv,cruxeval_o_adv,gsm8k_adv,gsm8k-platinum_adv,triviaqa_adv
    --include_path reflection/tasks
    --model_args pretrained=EleutherAI/pythia-160m,revision=step100000,dtype="float" \
    --device cuda:0 \
    --batch_size auto:4
```

See [here](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md) for more details on how to use the `lm-eval` interface.

## Classifier
For the reflection classifier described in our paper, we created fewshot prompts tailored to each task. We share these in `classifer` as well as the golden labels obtained from human annotators.

## Licenses

Our code and results are made available under the [MIT](https://opensource.org/license/mit) license and our datasets are made available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode) license. Please see [here](https://huggingface.co/collections/EssentialAI/rethinking-reflection-in-pre-training-67f69f2374a7d50cc5c325ea) for license details of each dataset.

## Citation

Please cite both our paper and the original work for each dataset that we modified. Please see [here](https://huggingface.co/collections/EssentialAI/rethinking-reflection-in-pre-training-67f69f2374a7d50cc5c325ea) for the relevant citation details for each dataset.

```bibtex
@misc{ai2025rethinkingreflectionpretraining,
      title={Rethinking Reflection in Pre-Training}, 
      author={Essential AI and : and Darsh J Shah and Peter Rushton and Somanshu Singla and Mohit Parmar and Kurt Smith and Yash Vanjani and Ashish Vaswani and Adarsh Chaluvaraju and Andrew Hojel and Andrew Ma and Anil Thomas and Anthony Polloreno and Ashish Tanwer and Burhan Drak Sibai and Divya S Mansingka and Divya Shivaprasad and Ishaan Shah and Karl Stratos and Khoi Nguyen and Michael Callahan and Michael Pust and Mrinal Iyer and Philip Monk and Platon Mazarakis and Ritvik Kapila and Saurabh Srivastava and Tim Romanski},
      year={2025},
      eprint={2504.04022},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2504.04022}, 
}