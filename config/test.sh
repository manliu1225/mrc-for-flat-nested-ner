#!/usr/bin/env bash 
# -*- coding: utf-8 -*- 

FOLDER_PATH=/home/liuman/acl19/mrc-for-flat-nested-ner-master
PATH-TO-BERT_MRC-DATA=/home/liuman/acl19/mrc-for-flat-nested-ner-master/data_preprocess/example
PATH-TO-SAVE-MODEL-CKPT=/home/liuman/acl19/mrc-for-flat-nested-ner-master
CONFIG_PATH=${FOLDER_PATH}/config/en_bert_base_uncased.json
DATA_PATH=/PATH-TO-BERT_MRC-DATA/mrc-dev_ace05.json 
BERT_PATH=/home/liuman/acl19/bert
EXPORT_DIR=/PATH-TO-SAVE-MODEL-CKPT
data_sign=ace2005 
entity_sign=flat

export PYTHONPATH=${FOLDER_PATH}
CUDA_VISIBLE_DEVICES=0 python3 ${FOLDER_PATH}/run/train_bert_mrc.py \
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
--num_train_epochs 10 \
--seed 2333 \
--warmup_proportion -1 \
--gradient_accumulation_steps 1