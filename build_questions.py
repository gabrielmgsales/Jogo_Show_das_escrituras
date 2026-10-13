# -*- coding: utf-8 -*-
"""Regenera os cinco bancos no diretório deste script."""
from build_data_bom import build as build_bom
from build_data_nt import build as build_nt
from build_data_ot import build as build_ot
from build_data_dc import build as build_dc
from build_data_pgv import build as build_pgv

if __name__ == "__main__":
    for build in (build_bom, build_nt, build_ot, build_dc, build_pgv):
        build()
    print("Concluído: 500 perguntas geradas.")
