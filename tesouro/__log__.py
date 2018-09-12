
{'date': 'Wed Sep 12 2018 10:17:37.222 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 207
    main(gui=GUI).inicia()
  module <module> line 201
    return Jogo(gui=gui, jogadores=[JogadorSimples(None, jogador) for jogador in jogadores])
  module <module> line 188
    self._inicia(nome)
  module <module> line 195
    except (ModuleNotFoundError, TypeError):
NameError: name 'ModuleNotFoundError' is not defined
'''},
{'date': 'Wed Sep 12 2018 10:18:46.444 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 207
    main(gui=GUI).inicia()
  module <module> line 201
    return Jogo(gui=gui, jogadores=[JogadorSimples(None, jogador) for jogador in jogadores])
  module tesouro.tesouro line 349
    self.mesa = Mesa(jogadores)
  module tesouro.tesouro line 238
    self.admite = Jogo.GUI.admite
AttributeError: 'Gui' object has no attribute 'admite'
'''},