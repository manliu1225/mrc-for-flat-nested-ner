#!/usr/bin/env bash 
# -*- coding: utf-8 -*- 

FOLDER_PATH=/home/liuman/acl19/mrc-for-flat-nested-ner-master
PATH_TO_BERT_MRC_DATA=/home/liuman/acl19/mrc-for-flat-nested-ner-master/data_preprocess/example/ace05
PATH_TO_SAVE_MODEL_CKPT=/home/liuman/acl19/mrc-for-flat-nested-ner-master
CONFIG_PATH=${FOLDER_PATH}/config/en_bert_base_uncased.json
DATA_PATH=${PATH_TO_BERT_MRC_DATA}
BERT_PATH=/home/liuman/acl19/uncased_L-12_H-768_A-12/uncased_L-12_H-768_A-12
EXPORT_DIR=${PATH_TO_SAVE_MODEL_CKPT}
data_sign=ace2005
#ace2004, en_onto, conll03, ace2005
entity_sign=flat

export PYTHONPATH=${FOLDER_PATH}
export CUDA_DEVICE_ORDER="PCI_BUS_ID"
export CUDA_VISIBLE_DEVICES="1"
python3 ${FOLDER_PATH}/run/train_bert_mrc.py \
--config_path ${CONFIG_PATH} \
--data_dir ${DATA_PATH} \
--bert_model ${BERT_PATH} \
--output_dir ${EXPORT_DIR} \
--entity_sign ${entity_sign} \
--data_sign ${data_sign} \
--n_gpu 1 \
--export_model True \
--dropout 0.3 \
--checkpoint 600 \
--max_seq_length 100 \
--train_batch_size 16 \
--dev_batch_size 16 \
--test_batch_size 16 \
--learning_rate 8e-6 \
--weight_start 1.0 \
--weight_end 1.0 \
--weight_span 1.0 \
--num_train_epochs 20 \
--seed 2333 \
--warmup_proportion -1 \
--gradient_accumulation_steps 1