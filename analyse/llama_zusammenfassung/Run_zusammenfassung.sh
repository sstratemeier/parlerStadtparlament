#!/bin/sh
torchrun --nproc_per_node 1 zusammenfassung.py \
    --ckpt_dir CodeLlama-7b-Instruct/ \
    --tokenizer_path CodeLlama-7b-Instruct/tokenizer.model \
    --max_seq_len 1000 --max_batch_size 4
