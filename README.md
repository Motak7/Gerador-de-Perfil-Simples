Gerador de Perfil Simples
Descrição
Este projeto em Python é um Gerador de Perfil Simples que coleta informações básicas de usuários e exibe um resumo formatado desses dados. O programa interage com o usuário no terminal, solicitando as seguintes informações:

Nome: Nome completo do usuário.
Idade: Idade do usuário (em anos). O programa valida se a idade está entre 1 e 149 anos.
Altura: Altura do usuário (em metros). O programa valida se a altura está entre 0.5 e 2.5 metros.
Estudando Programação?: Pergunta se o usuário está atualmente estudando programação, com resposta esperada 's' para sim ou 'n' para não.
Após coletar as informações de um ou mais usuários, o programa exibe um resumo formatado na tela, mostrando os dados de cada perfil em formato de tabela.

Objetivo:

O principal objetivo deste projeto é demonstrar os conceitos básicos de:

Entrada e Saída de Dados: Como solicitar informações do usuário no terminal (input) e exibir resultados formatados (print).
Estruturas de Dados: Utilização de listas (perfils) para armazenar múltiplos perfis e dicionários para organizar os dados de cada perfil (nome, idade, altura, etc.).
Validação de Dados: Implementação de verificações simples para garantir que os dados inseridos pelo usuário estejam dentro de limites razoáveis (idade e altura).
Loops e Condicionais: Uso de while para permitir a criação de múltiplos perfis e if/elif/else para validação e lógica do programa.
Tratamento de Erros: Utilização de try/except para lidar com entradas inválidas do usuário (como digitar letras onde se espera números).
Instalação
Nenhuma instalação é necessária para executar este projeto. Como é um script Python simples, você precisa apenas ter o Python instalado no seu computador.

Python: Certifique-se de ter o Python 3 instalado. Você pode baixar a versão mais recente em https://www.python.org/downloads/.
Uso
Para executar o Gerador de Perfil Simples, siga estes passos:

Salve o código: Copie o código Python fornecido e salve-o em um arquivo com a extensão .py (por exemplo, gerador_perfil.py).
Abra o terminal: Abra o terminal ou prompt de comando do seu sistema operacional.
Navegue até o diretório: Use o comando cd para navegar até o diretório onde você salvou o arquivo gerador_perfil.py. Por exemplo, se você salvou na pasta "Documentos" dentro de uma pasta "Projetos", o comando seria algo como: cd Documentos/Projetos
Execute o script: Execute o script Python com o comando: python gerador_perfil.py
Interagindo com o Programa:

Ao executar o script, o programa irá:

Exibir a mensagem --- Novo Perfil --- para indicar o início da coleta de dados de um novo perfil.
Solicitar que você insira o Nome, Idade, Altura e responda se a pessoa Está estudando programação? para cada perfil, seguindo as instruções no terminal.
Após inserir os dados de um perfil, perguntar Deseja adicionar outro perfil? (s/n):.
Digite s para adicionar outro perfil e repetir o processo.
Digite n para parar de adicionar perfis e exibir o resumo.
Se você inserir dados inválidos (idade fora da faixa, altura fora da faixa, ou letras onde se espera números), o programa exibirá mensagens de erro e pedirá para você inserir os dados novamente.
Ao finalizar a entrada de perfis, o programa exibirá --- Resultados --- seguido de uma tabela formatada com os dados de todos os perfis inseridos.
Por fim, exibirá Pressione Enter para sair... e aguardará você pressionar a tecla Enter para encerrar o programa.
Exemplos
Exemplo de interação no terminal:

--- Novo Perfil ---
Nome: Ana Silva
Idade: 25
Altura (m): 1.65
Está estudando programação? (s/n): s
Deseja adicionar outro perfil? (s/n): s

--- Novo Perfil ---
Nome: Pedro Oliveira
Idade: 17
Altura (m): 1,78
Está estudando programação? (s/n): n
Deseja adicionar outro perfil? (s/n): n

--- Resultados ---
Nome            | Idade | Altura | Estudando?
Ana Silva       |  25   |   1.65m |     Sim
Pedro Oliveira  |  17   |   1.78m |     Não

Pressione Enter para sair...

Contribuições
Contribuições para melhorias ou sugestões são bem-vindas! Se você tiver ideias para expandir este projeto simples, sinta-se à vontade para:

Fazer um Fork do repositório (se este projeto estiver hospedado em um repositório online, como GitHub).
Criar uma nova branch (git checkout -b feature/nova-funcionalidade).
Implementar suas alterações.
Comitar suas alterações (git commit -m 'Adicionar nova funcionalidade').
Enviar para o branch (git push origin feature/nova-funcionalidade).
Abrir um Pull Request.
Licença
Este projeto é distribuído sob a Licença MIT. Você é livre para usar, modificar e distribuir este código para fins pessoais e comerciais.

Contato
Para dúvidas ou feedback sobre este projeto, você pode entrar em contato através de [ryan.tupina@gmail.com] ou [https://www.linkedin.com/in/ryan-mota-28ba171b1/].
