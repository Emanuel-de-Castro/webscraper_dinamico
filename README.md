# Web Scraper Dinâmico - Enjoei

Projeto de automação e coleta de dados em Python para buscar produtos no Enjoei e salvar os resultados em arquivo texto. O script usa Selenium para controlar o navegador, interagir com elementos dinâmicos da página e percorrer os resultados de busca em mais de uma página.

# Sobre o projeto

Este projeto foi desenvolvido como exercício de portfólio para demonstrar scraping em site dinâmico, com abertura de navegador, fechamento de modal, envio de pesquisa, captura de cards de produto, tratamento simples de repetição de itens e navegação por paginação.


O fluxo geral faz uma busca pelo nome digitado pelo usuário, abre o site do Enjoei, fecha o pop-up inicial, preenche o campo de pesquisa, coleta nome, preço e link dos produtos exibidos e grava essas informações no arquivo enjoei.txt.

# Tecnologias usadas
    
    Python 3
    
    Selenium
    
    ChromeDriver compatível com a versão do navegador..


# Funcionalidades

Busca produtos a partir de um termo digitado pelo usuário.

Interage com elementos carregados dinamicamente na página.

Fecha o modal inicial antes da pesquisa, o que é um caso comum em automações com Selenium.

Extrai nome, preço e link de cada card encontrado.

Evita salvar itens duplicados em memória durante a execução.

Salva os resultados em um arquivo .txt para consulta posterior.

Percorre múltiplas páginas de resultados até não encontrar mais botão de próxima página.


# Estrutura 

  projeto/
  
  ├─ scraper.py
  
  ├─ requirements.txt
  
  ├─ .gitignore
  
  ├─ README.md
  
  └─ enjoei.txt
  
  O arquivo enjoei.txt é gerado ou atualizado durante a execução e armazena os itens encontrados para cada busca realizada.



# Requisitos

Antes de executar, o ambiente precisa ter Python instalado e a biblioteca Selenium disponível. A instalação da biblioteca Selenium pode ser feita com pip install selenium, conforme a documentação e materiais introdutórios do ecossistema Selenium para Python.


# Exemplo de saída

--- ITEM: NOTEBOOK ---
Notebook Dell Inspiron - R$ 2.300 - https://www.enjoei.com.br/p/...
Notebook Lenovo IdeaPad - R$ 1.950 - https://www.enjoei.com.br/p/...
O formato acima representa o padrão salvo pelo script: nome do produto, preço e link do anúncio em uma única linha por item.

# Como o código funciona

Entrada do usuário
O script solicita um termo de busca com input() e usa esse valor para pesquisar produtos na plataforma.

Automação do navegador
O Selenium abre uma instância do Chrome com webdriver.Chrome() e acessa a página principal do Enjoei. Selenium é indicado justamente quando a página depende de renderização e interação no navegador para expor os dados.

Interação com a interface
O código localiza o botão de fechar modal e o campo de pesquisa com XPath, clica nos elementos necessários e envia a busca com Keys.ENTER. Esse tipo de interação é comum em scraping de páginas dinâmicas que dependem de eventos de interface.

Coleta dos cards
Após carregar os resultados, o script localiza os cards de produto, percorre cada card e tenta extrair três campos: título, preço e link. Em páginas dinâmicas, essa coleta normalmente acontece depois da renderização dos componentes no DOM do navegador.

Paginação
Enquanto existir o botão de próxima página, o script continua navegando e coletando novos itens. Paginação e scroll fazem parte dos cenários típicos de scraping com Selenium em sites modernos.

Prevenção de duplicados
Os resultados são comparados com um conjunto (set) em memória antes de serem gravados, evitando repetição durante a mesma execução do programa.

# Pontos positivos do projeto

  Mostra conhecimento prático de Selenium em ambiente real.
  
  Trabalha com site dinâmico em vez de HTML estático simples.
  
  Usa coleta paginada, o que aumenta o valor do projeto para portfólio.
  
  Salva os dados em arquivo local de forma simples e objetiva.
  
  Aplica uma lógica básica para evitar registros duplicados.
