#! /usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of  program Vitollino
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

"""Jogos para usar com o Vitollino

    Quebra-cabeças para serem usados na construção de outros jogos.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    22.04
        Criação do módulo de jogos.

.. versionchanged::    22.04.a
        Usa os comandos originais do DOM.


.. seealso::

   Documentação geral do SuperPython: `Ajuda do SuperPython`_

.. _`Ajuda do SuperPython`: https://supygirls.readthedocs.io

"""
from vitollino.main import Cena, Elemento
from random import randint
# from browser import alert

# STYLE.update(width=850, height="650px")

IMGUR = "https://i.imgur.com/{}.jpg"
FUNDO = "qWcEao4"
CENAS = "CRNsfXO swVe1IW jiJY1NY GsdFmpz T6pmXbY dJ4WOIh".split()
CENAS_ = "swVe1IW nVpyITK     "
OFF = 2000
OFX, OFY = 100, 50


class Cubos:
    CUBOS = None

    def write(self, text):
        self.el.elt.html = text

    def __init__(self, cenas, tw=None, th=600, nx=4, ny=3, ofx=OFX, ofy=OFY):
        """Jogo que define cubos formando uma cena em cada lado.

        Joga-se clicando em uma das porções cardeais da face do cubo.
        O cubo irá rolar naquela direção.

        :param cenas: coleção de seis cenas a serem apresentadas.
        :param tw: tamanho em pixeis de largura da cena.
        :param th: tamanho em pixeis de altura da cena.
        :param nx: número de cubos na horizontal.
        :param ny: número de cubos na vertical.
        :param ofx: deslocamento na horizontal.
        :param ofy: deslocamento na vertical.
        """

        # from vitollino.main import Cena, Elemento

        class Face(Elemento):
            """Reperesenta a face do cubo.

            A face do cubo é sensível ao click em quatro diferentes porções cardeais.
            As porções cardeais são delimitadas pela duas diagonais do cubo.

            """
            def __init__(self, cubo, inx, face, **kwargs):
                """A face pertencente a um cubo do quebra-cabeças.

                :param cubo: o cubo ao qual pertence.
                :param inx: índice do cubo no quebra-cabeças.
                :param face: parte do endereço IMGUR da imagem.
                :param kwargs: parâmenteros a serem passados para o elemento 'Vitollino'.
                """
                self.cubo = cubo
                w, h = tw // nx, th // ny
                self.dh = h
                x, y = (inx % nx) * w, (inx // nx) * h
                super().__init__(IMGUR.format(face), x=x + ofx, y=y - OFF + ofy, w=w, h=h,
                                 cena=cena, vai=self.vai,
                                 style={'background-image': "url({})".format(IMGUR.format(face)),
                                        'background-size': f"{tw}px {th}px",
                                        "background-position": f'{-x}px {-y}px'},
                                 **kwargs)
                # self.siz = (tw, th)
                # self.pos = (-x, -y)
                self.yy = y - OFF + ofy
                self.xx = x + OFX
                self.elt.style.width = f"{w}px"
                self.elt.style.height = f"{h}px"
                self.elt.html = ""
                self.quad = 0

            @property
            def xx(self):
                top = self.elt.style.left[:-2]
                return int(top if top else 0)

            @xx.setter
            def xx(self, value):
                self.elt.style.left = "{}px".format(value)

            @property
            def yy(self):
                top = self.elt.style.top[:-2]
                return int(top if top else 0)

            @yy.setter
            def yy(self, value):
                self.elt.style.top = "{}px".format(value)

            def show(self):
                """Mostra esta face do cubo.

                :return: sempre verdadeiro, para indicar que a face está sendo mostrada.
                """
                self.yy += OFF if self.yy < -10 else 0
                return True

            def hide(self):
                """Esconde esta face do cubo.

                :return: sempre falso, para indicar que a face está sendo ocultada.
                """
                self.yy -= OFF if self.yy > 10 else 0
                return False

            def orient(self, ori):
                """ Reorienta a face para refletir as rolagens do cubo.

                :param ori: qudrante da rotação da face, entre 0 e 3.
                :return: sempre falso.
                """
                self.elt.style.transform = f"rotate({ori * 90}deg)"
                return False

            def vai(self, evt):
                """Recebe o click na face e calcula qual quadrante cardeal foi clicado.

                Calcula a posição relativa do click na face.
                Determina o click em relação às duas diagonais da face.
                As diagonais são x=-y e x=y+h.

                :param evt: evento recebido do nvegador.
                :return:
                """
                e = evt.target
                dim = e.getBoundingClientRect()
                x = evt.clientX - dim.left
                y = evt.clientY - dim.top
                e, n, h = x - y, x + y, self.dh
                self.quad = 0 if (e > 0) and (n < h) else 1 if (e > 0) and (n > h) else 2 if (e < 0) and (n > h) else 3
                # Cubo.CUBOS.write(f"x: {x} y: {y} qd: {self.quad}")
                self.cubo.go(self.quad)

        class Cubo:
            """Cubo para formar um quebra-cabeças de seis imagens.

            Cada cubo contém um recorte quadrado de cada uma das seis imagens nas suas faces.
            O cubo rola quando se clica na face que esta sendo apresentada (virada para cima).
            Ao rolar, o cubo vai apresentar uma nova face, dada pela direção indicada na rolagem.

            """
            ROLL = [
                [[19, 4, 21, 12], [18, 8, 22, 0], [17, 12, 23, 4], [16, 0, 20, 8], [6, 1, 12, 11], [12, 3, 6, 10]],
                [[5, 22, 13, 16], [9, 23, 1, 19], [13, 20, 5, 18], [1, 21, 9, 17], [2, 13, 8, 7], [0, 7, 10, 13]],
                [[23, 14, 17, 6], [20, 2, 16, 10], [21, 6, 19, 14], [22, 10, 18, 2], [14, 9, 4, 3], [4, 11, 14, 1]],
                [[15, 18, 7, 20], [3, 17, 11, 21], [7, 16, 15, 22], [11, 19, 3, 23], [10, 5, 0, 15], [8, 15, 2, 5]],
            ]
            """Vetor que representa o índice destino da rolagem dado um clique numa face."""

            def __init__(self, inx, faces):
                """Cubo que tem os recortes das seis imagens nas suas faces.

                :param inx: índice posicional do cubo no quebra-cabeças, no sentido da leitura.
                :param faces: lista com as seis imagens que serão apresentadas nas faces do cubo.
                """
                self.faces = [Face(cubo=self, inx=inx, face=face) for face in faces]
                self.face, self.orient = 0, 0

            def roll(self, inx):
                """Rola o dado na direção indicada.

                Caso esta rolagem complete uma das imagens do quebra-cabeça, indica sucesso.

                :param inx: índice que representa uma combinação da face com a orientação.
                :return: None
                """
                facer, self.orient = inx // 4, inx % 4
                self.face = [face.show() if facer == face_index else face.hide()
                             for face_index, face in enumerate(self.faces)].index(True)
                self.faces[self.face].orient(self.orient)
                Cubo.CUBOS.write("completou com sucesso") if Cubo.CUBOS.complete() else None

            @property
            def inx(self):
                """Índice que representa uma combinação da face com a orientação.

                :return: índice que representa uma combinação da face com a orientação.
                """
                return self.face * 4 + self.orient

            def go(self, inx):
                go_face_roll = Cubo.ROLL[self.orient][self.face][inx]
                self.roll(go_face_roll)
                # fc1, ot1 = self.face, self.orient
                # Cubo.CUBOS.write(f"inx: {inx} face: {fc0} ori: {ot0} gfr: {go_face_roll} face: {fc1} ori: {ot1} ")

        cena = Cena(IMGUR.format(FUNDO)).vai()
        tw, th = (tw, tw // nx * ny) if tw else (th // ny * nx, th)
        Cubo.CUBOS = self
        self.el = Elemento(IMGUR.format(FUNDO), w=300, h=100, cena=cena, style={"color": "white"})
        self.cubos = cubos = [Cubo(inx=inx, faces=cenas) for inx in range(nx * ny)]
        [cube.roll(randint(0, 23)) for cube in cubos]
        # [cube.roll(0) for cube in cubos]

    def complete(self):
        """Calcula para ver se todos os cubos apresentam a mesma face.

        :return: *True* se todas as faces dos cubos representam a mesma imagem.
        """
        # self.write(set(cubo.inx for cubo in self.cubos))
        return len(set(cubo.inx for cubo in self.cubos)) == 1


if __name__ == "__main__":
    Cubos(CENAS, tw=500, nx=2, ny=2)
