Projeto – TrokaMassa (Pior UX/UI)
A Engenharia do Erro – A Pior Experiência de Usuário (UI vs UX)

 Sobre o Projeto
O TrokaMassa é uma plataforma fictícia de compra e venda de produtos usados desenvolvida para o desafio "UI vs. UX & A Engenharia do Erro". O objetivo do projeto é criar um fluxo de acesso (tela de login e autenticação) propositalmente caótico, repleto de obstáculos, elementos enganosos e falhas de acessibilidade.
Apesar de todas as pegadinhas e barreiras introduzidas na interface, o fluxo é totalmente funcional e vencível, permitindo que o usuário chegue até a mensagem final de confirmação de acesso.

Princípios e Heurísticas Violados
Consistência e Padrões (Heurística #4 de Nielsen): Inversão do padrão visual de ações primárias e secundárias. O botão verde com estilo de confirmação na verdade limpa todo o formulário (reset), enquanto o botão de confirmação ("Entrar") é cinza, apagado e sem destaque.
Prevenção de Erros (Heurística #5 de Nielsen): O campo de seleção de idade utiliza um controle deslizante (input range) com precisão decimal extrema (step="0.0001"), tornando quase impossível selecionar um valor inteiro exato de forma simples.
Acessibilidade - Contraste Mínimo (WCAG 2.1 - Critério 1.4.3): O rótulo explicativo do campo de e-mail utiliza texto em cor branca sobre fundo branco, ficando invisível a menos que o usuário destaque o texto com o cursor.
Visibilidade do Status do Sistema (Heurística #1 de Nielsen): Remoção do contorno de foco visual nos campos de entrada (outline: none), impedindo que o usuário identifique visualmente qual elemento está ativo ao navegar via teclado.
Controle e Liberdade do Usuário (Heurística #3 de Nielsen): Anúncios e janelas pop-up flutuantes cruzam a tela e bloqueiam o formulário, com botões de fechar ("X") que acionam avisos adicionais em vez de fechar a propaganda.

Proposta de Correção (Versão Ideal)
Slider Decimal de Idade: Substituir por um campo numérico simples (<input type="number">) ou seletor de data de nascimento para facilitar o preenchimento.
Botões com Ações Invertidas: Destacar o botão de confirmação ("Entrar") com cor primária e usar estilo neutro para ações secundárias ou de cancelamento.
Rótulo sem Contraste: Aplicar cores de alto contraste que atendam à proporção mínima da WCAG (ex.: texto escuro sobre fundo claro).
Anúncios e Obstáculos Flutuantes: Remover pop-ups do fluxo de login e garantir que os botões de fechar ("X") encerrem os elementos imediatamente.

Integrantes do Grupo: 
Ayram Viviane	
Guilherme da Silva
Sthefany Campos
