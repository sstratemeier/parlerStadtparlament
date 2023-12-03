# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import Optional

import fire
import pdb

from llama import Llama
import pandas as pd


def run_llama(s,generator,max_gen_len,temperature,top_p):
    if len(s)>1000:
        s = s[:900]
    instructions = [
        [
            {
                "role": "user",
                #                "content": f"Eine Politische Motion wird im Stadtparlament behandelt. Gib das Hauptstichwort zurück, das den Text am besten zusammenfasst. Die Ausgabe soll auf Deutsch erfolgen. Schreibe nichts als das Hauptstichwort!\n{s}",
                "content": f"Eine Politische Motion wird im Stadtparlament behandelt. Gib das Hauptstichwort zurück, das den Text am besten zusammenfasst. Die Ausgabe muss eines der folgenden Begriffe sein: 'Energie/Umwelt/Klima', 'Verkehr','Bildung','Sicherheit','Finanzen und Steuern','Soziales', 'Bauwesen', 'Kultur', 'Standortförderung','Sonstiges'. Schreibe nichts als das Hauptstichwort!\n{s}",
            }
        ],
    ]
    results = generator.chat_completion(
        instructions,  # type: ignore
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )

    s=''
    for instruction, result in zip(instructions, results):
        for msg in instruction:
            print(f"{msg['role'].capitalize()}: {msg['content']}\n")
        print("\n----------------------------------\n")
        print(
            f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
        )
        new_s = f"{result['generation']['role'].capitalize()}: {result['generation']['content']}"
        new_s = new_s.replace('Assistant:','')

        s+=new_s
        print("\n==================================\n")
    return s


def main(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 0.2,
    top_p: float = 0.95,
    max_seq_len: int = 512,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    df = pd.read_excel('../../opendatasg/output/Daten_mit_Quartier_v2.xlsx')

    L = []
    for i,s in df.Volltext.items():
        print(i,df.shape)
        answer = run_llama(s,generator, max_gen_len,temperature,top_p)
        L.append(answer)
    L = pd.Series(L,index=df.index)
    L.to_excel('llama_results2.xlsx')

    


if __name__ == "__main__":
    fire.Fire(main)
