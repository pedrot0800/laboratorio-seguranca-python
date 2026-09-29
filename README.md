# Laboratório de Segurança com Python

Projeto educacional sobre criptografia e recuperação de arquivos, registro de teclado e riscos de transmissão de informações. A documentação distingue resultados observados, relatos do usuário e verificações que não foram realizadas.

## Estado do projeto

| Etapa | Situação |
|---|---|
| Criptografia de uma cópia fictícia | Executada |
| Recuperação e comparação SHA-256 | Executadas; resultado `True` |
| Registro local de teclado | Execução e log apresentados |
| Encerramento da versão local | Mensagem registrada no terminal |
| Recebimento por e-mail | Captura da mensagem apresentada pelo usuário |
| Periodicidade dos envios | Não verificada |
| Encerramento da versão de e-mail | Não demonstrado |
| Testes automatizados | Sem resultados apresentados |
| Publicação no GitHub | Não confirmada |

## Objetivos

- Entender a relação entre criptografia, chaves e integridade.
- Analisar o risco de registrar entradas de teclado.
- Discutir o impacto da transmissão dessas informações.
- Documentar evidências e relacionar os comportamentos à defesa.

## Criptografia e recuperação

Foi criado manualmente `dados_teste/exemplo.txt`. Os scripts `src/ransomware/criptografar.py` e `src/ransomware/descriptografar.py` produziram uma cópia criptografada e um novo arquivo recuperado, preservando o original.

A comparação dos hashes SHA-256 do original e do recuperado retornou `True`. O experimento não bloqueou o original e não gerou cobrança ou mensagem de resgate.

Os scripts usam caminhos absolutos da máquina do teste. Eles não são portáveis sem ajustes. As chaves e saídas brutas permanecem como artefatos locais.

## Registro de teclado e mensagem recebida

O usuário apresentou evidências de `keylogger.pyw`, do respectivo `log.txt`, da chamada de `keylogger_email.py` e de uma mensagem na caixa de entrada. Os scripts de teclado foram executados em uma pasta externa ao projeto, conforme as capturas; os nomes não representam confirmação de inclusão desses arquivos neste repositório.

O código compartilhado usa um listener global de `pynput`. A captura não se limita à interface de um simulador. O arquivo `src/keylogger/simulador.py`, preparado anteriormente como alternativa com janela própria, não corresponde aos testes originais apresentados.

A mensagem recebida é evidência do resultado apresentado pelo usuário; uma captura isolada não comprova o intervalo entre envios, a continuidade da execução ou seu encerramento. A documentação não inclui instruções de configuração de envio de entradas capturadas.

## Ambiente

As capturas registram Windows, VS Code, PowerShell, Python 3.14.7 e `cryptography` 50.0.1. A versão de `pynput` não foi informada. Não há comprovação de uso de máquina virtual ou sandbox.

O arquivo `requirements.txt` declara a dependência da etapa de criptografia. Não deve ser interpretado como descrição completa do ambiente dos scripts externos de teclado.

## Documentação

- [Ambiente e limitações](docs/ambiente.md)
- [Experimentos e evidências](docs/experimentos.md)
- [Prevenção e defesa](docs/defesa.md)
- [Conclusão](docs/conclusao.md)

## Evidências

| Captura | Conteúdo |
|---|---|
| [01 — Criptografia](images/01-criptografia.png) | Execução e criação da cópia |
| [02 — Recuperação](images/02-descriptografia.png) | Criação do arquivo recuperado |
| [03 — Integridade](images/03-comparacao.png) | Comparação SHA-256 com resultado `True` |
| [04 — Registro local](images/04-keylogger-execucao.png) | Execução da versão local |
| [05 — Log](images/05-keylogger-registro.png) | Conteúdo de teste registrado |
| [06 — Encerramento local](images/06-encerramento-local-e-email.png) | Mensagem de encerramento local e chamada da versão de e-mail |
| [07 — Mensagem recebida](images/07-email-recebido.png) | Caixa de entrada apresentada pelo usuário |

## Defesa e limites

Backups, controle de permissões, monitoramento, proteção de credenciais e conscientização são discutidos na documentação. Não foram executados testes de eficácia dessas medidas.

O registro global pode alcançar informações fora do exercício. A transmissão amplia a exposição ao criar cópias externas. As capturas não demonstram isolamento, furtividade ou segurança geral da implementação.

## Publicação

Mantenha este README na raiz, com `docs/` e `images/`. Não publique chaves, credenciais ou registros pessoais. Revise também caminhos e nomes visíveis nas imagens. O `.gitignore` não protege uploads manuais nem remove arquivos já rastreados.

## Referências e créditos

- [Documentação do Python](https://docs.python.org/3/)
- [Documentação do Fernet](https://cryptography.io/en/latest/fernet/)
- [CISA — StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide)

A estrutura, a documentação e a adaptação dos scripts de criptografia receberam apoio de IA. O usuário realizou os testes e forneceu as evidências. As atualizações relativas aos códigos originais de teclado se restringem à análise documental dos materiais fornecidos.
