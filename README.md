# REVU
# External Memory Matters: Generalizable Object-Action Memory for Retrieval-Augmented Long-Term Video Understanding
The official repository of our paper "**External Memory Matters: Generalizable Object-Action Memory for Retrieval-Augmented Long-Term Video Understanding**".


## Highlights
  1. **Innovative External Memory Mechanism**: The paper proposes a scalable external textual object memory module that combines both static and dynamic multimodal information, which effectively helps large language model (LLM)-based models align text and visual features. This design not only enhances the model's ability to understand rare or newly emerging objects but also significantly improves its performance in complex scenes. By dynamically retrieving object information from an external database and integrating it with video content, this approach effectively aggregates knowledge to address dynamic changes in an open world. This retrieval-augmented strategy not only improves the model's generalization ability but also reduces dependence on large-scale training data, lowering computational costs.

  2. **Effectiveness and Performance**: On several benchmark datasets (such as LVU, MSRVTT, and MSVD), the model achieves state-of-the-art performance, particularly excelling in handling complex scenes and rare objects. This demonstrates the method's effectiveness in long video understanding tasks. Additionally, experimental results show that the model can adapt to data from different domains, exhibiting strong generalization ability. This makes the method highly flexible and applicable in practical scenarios.

  3. **Depth and Breadth of the Research**: **Multimodal Fusion Depth**: The method not only focuses on aligning object and action names with visual features but also deeply integrates external knowledge with video content through the retrieval-augmented strategy, offering a more comprehensive understanding of video scenes. While the primary focus is on long video understanding tasks, the design concept and framework of the method are highly versatile, making it extensible to other video-related tasks such as video summarization and video editing.


## Abstract
Long video understanding with Large Language Models (LLMs) enables the description of objects that are not explicitly present in the training data. However, continuous changes in known objects and the emergence of new ones require up-to-date knowledge of objects and their dynamics for effective understanding of the open world. To alleviate this, we propose an efficient Retrieval Enhanced Video Understanding method, dubbed REVU, which leverages external knowledge to enhance the performance of open-world learning. First, REVU introduces an extensible external text-object memory with minimal text-visual mapping, involving static and dynamic multimodal information to help LLMs-based models align text and vision features. Second, REVU retrieves object information from external databases and dynamically integrates frame-specific data from videos, enabling effective knowledge aggregation to comprehend the open world. We conducted experiments on multiple benchmark datasets, and our model demonstrates strong adaptability to out-of-domain data without requiring additional fine-tuning or retraining. Experiments on benchmark video understanding datasets reveal that our model achieves state-of-the-art performance and robust generalization.


## Model Overview
<p align="center">
<img src="figs/architecture.png" alt="model" width="80%">
</p>


## Demo
You can explore our demo by running `demo.ipynb`. This demonstration illustrates how our MA-LMM serves as a plug-and-play module that can be integrated into InstructBLIP seamlessly, requiring no fine-tuning for zero-shot evaluation.


## Requirements

You can install the conda environment by running:
```bash
git clone https://github.com/boheumd/MA-LMM.git
cd MA-LMM
pip install -e .
```

If you are running the code on Apple Silicon, you need to use `eva-decord` instead of `decord`. Here is the modification in the `requirements.txt` file you should do:

```text
contexttimer
eva-decord
einops>=0.4.1
fairscale==0.4.4
...
```

**Before running `pip install -e .`, ensure you have the correct requirements.**


## Dataset
For the long-term video understanding task, we conduct experiments including [LVU](https://github.com/chaoyuaw/lvu) and standard video summarization dataset [Breakfast](https://serre-lab.clps.brown.edu/resource/breakfast-actions-dataset/).

For the video question answering task, we conduct experiments including [MSRVTT](https://github.com/xudejing/video-question-answering) and [MSVD](https://github.com/xudejing/video-question-answering).

You can download videos for each dataset through the script provided here (lavis/datasets/download_scripts). For LVU/Breakfast/COIN datasets, please download the original videos through the official link provided above.

Then extract video frames of each video with fps=10. Example preprocess code is provided here [extract_frames.py](https://github.com/boheumd/MA-LMM/blob/main/data/extract_frames.py).
Since different FFMPEG versions are used, the actual extracted frame lengths can be slightly inconsistent. You may need to update the actual frame_length for each video in the annotation file.
   ```
    ├── data
        └── breakfast
            ├── annotation
            ├── frames
            ├── videos
        └── lvu
            ├── annotation
            ├── frames
            ├── videos
        └── msrvtt
            ├── annotation
            ├── frames
            ├── videos
        └── msvd
            ├── annotation
            ├── frames
            ├── videos
   ```


## Running

### Download Pre-trained LLM
Following [malmm](https://github.com/boheumd/MA-LMM), we use Vicuna-v1.1 as our pre-trained LLM weights, you can download from this [link](https://github.com/lm-sys/FastChat/blob/main/docs/vicuna_weights_version.md) as arrange in this format.
   ```
   ├── llm
        ├── vicuna-7b
        ├── vicuna-13b
   ```

### Finetuning on Downstreaming Tasks
Following [malmm](https://github.com/boheumd/MA-LMM), our model leverages pre-trained weights from [InstructBlip](https://github.com/salesforce/LAVIS/tree/main/projects/instructblip), which was only pre-trained on image-text pairs. Our training process occurred on four 4090 GPUs. If you would like to fine-tune the model for various video datasets, first of all, you need to select the corresponding `file_path`, `base`, `name`, and `data[item]` in the `adjust.py` file, then please run the following command:

#### LVU dataset
Please choose the task from the following list, you need to modify the task on line 15 of the `train.py` file:
['director', 'genre', 'relationship', 'scene', 'way_speaking', 'writer', 'year']
```bash
bash run_scripts/${dataset}/train.sh
```

#### msvd_qa:
```bash
bash run_scripts/${dataset}/train_qa.sh
```

#### msrvtt:
```bash
bash run_scripts/${dataset}/train_qa.sh
```

#### breakfast:
```bash
bash run_scripts/${dataset}/train.sh
```

### Testing
We also provided finetuned checkpoints for each video dataset. Please download the [saved_model.tar](https://drive.google.com/file/d/1mq6fg69Ofm32-1HjEunoFtPg8ymAIcOp/view?usp=sharing) and unzip it. 
For the test script corresponding to each dataset, provide the path to the extracted checkpoint to execute the evaluation.
```bash
bash run_scripts/${dataset}/test.sh ${checkpoint_path}
```

### Zero-shot Evaluation
Our model can also leverage pre-trained weights from [InstructBlip](https://github.com/salesforce/LAVIS/tree/main/projects/instructblip) without any finetuning to conduct zero-shot evaluation on video datasets.
```bash
bash run_scripts/${dataset}/test.sh
```


## External Memory Bank
We have designed two external memory banks, located in the `ext_data` folder: one is the object memory bank (`object_memory.py`), and the other is the action memory bank (`action_memory.py`). If the user wants to update the external memory bank according to specific needs, they can run `add_data.py` to write data into the external memory bank.


## Citation
  Coming soon!


## Acknowledgement
We referenced the repo below for the code
- [malmm](https://github.com/boheumd/MA-LMM)
