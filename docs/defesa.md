# Prevenção, detecção e recuperação

## Antivírus e monitoramento

Antivírus e ferramentas de monitoramento podem identificar arquivos conhecidos e comportamentos suspeitos. Alterações repetidas em arquivos ou atividade inesperada de processos merecem investigação, mas um alerta isolado não confirma um ataque. A ausência de alerta também não comprova que uma execução é segura.

## Firewall e rede

Restrições de rede podem reduzir conexões desnecessárias e dificultar a transmissão indevida de informações. Elas não impedem, por si só, que um programa com acesso local altere arquivos ou registre entradas. Por isso, o controle de rede deve ser combinado com permissões e proteção do dispositivo.

## Isolamento e privilégio mínimo

Uma sandbox ou máquina virtual dedicada ajuda a separar os experimentos do ambiente de uso pessoal. Pastas compartilhadas e permissões excessivas podem aumentar o alcance de uma execução. O laboratório deve usar somente dados fictícios e os acessos necessários ao exercício.

## Conscientização e atualizações

Anexos, downloads e solicitações enganosas podem induzir a execução de programas não confiáveis. Conferir a origem e o contexto reduz esse risco. Atualizar os sistemas e aplicações também reduz a exposição a falhas corrigidas. Ataques podem explorar tanto vulnerabilidades técnicas quanto decisões humanas.

## Backups e autenticação

A CISA recomenda manter backups offline e testar sua restauração. Isso se relaciona diretamente ao objetivo do laboratório: recuperar dados precisa ser um procedimento verificável. A autenticação multifator é outra camada de proteção contra uso indevido de credenciais, embora não substitua a proteção do dispositivo. Fonte: [Guia StopRansomware](https://www.cisa.gov/stopransomware/ransomware-guide).

## Relação com os experimentos

| Comportamento estudado | Impacto | Medidas relacionadas |
|---|---|---|
| Criptografia indevida | Indisponibilidade de dados | Backups, permissões limitadas e monitoramento |
| Captura de entradas | Exposição de informações | Proteção do dispositivo, origem confiável de software e consentimento |
| Saída indevida de dados | Perda de confidencialidade | Controle de rede e investigação de conexões |
| Execução de conteúdo não confiável | Comprometimento do ambiente | Atualizações, conscientização e isolamento |

## Resposta a um incidente

Em um cenário real, a resposta envolve comunicar a equipe responsável, conter o alcance do incidente, preservar evidências e planejar a recuperação de um ambiente confiável. A restauração deve considerar a causa do comprometimento para evitar recorrência.

Esta análise é conceitual. Não foram executados testes de antivírus, firewall ou resposta a incidentes neste projeto.
