# Ambiente e escopo observado

As capturas fornecidas mostram Windows, PowerShell e VS Code. O terminal apresentou Python 3.14.7 e a biblioteca `cryptography` 50.0.1. O código de teclado compartilhado importa `pynput`, mas sua versão instalada não foi informada.

A criptografia e a recuperação foram realizadas com um arquivo fictício na estrutura do projeto. Os scripts de teclado foram chamados de uma pasta externa, identificada como KEYLOGGER nas capturas. O estudo documental não pressupõe que esses scripts estejam incluídos em `src/`.

Não há comprovação de VM, sandbox ou restrição de rede. Um ambiente virtual Python separa dependências e não fornece isolamento de segurança. A existência de uma mensagem na caixa de entrada também não determina como a rede do laboratório estava configurada.

O script de criptografia aponta para uma amostra específica e preserva o original. Os códigos de teclado compartilhados utilizam listener global, sem restrição à janela do exercício. O encerramento da versão local aparece no terminal; o da versão de e-mail não foi demonstrado.

Nenhuma credencial, chave de criptografia ou log bruto é necessária para a documentação pública.
