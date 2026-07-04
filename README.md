# TechFlow-gerenciador-tarefas

# 🚀 TechFlow Task Manager - Sistema de Gerenciamento Ágil

O **TechFlow Task Manager** é uma solução de software desenvolvida sob medida para uma startup de logística. O objetivo principal do sistema é permitir o acompanhamento do fluxo de trabalho em tempo real, a priorização de tarefas críticas de transporte/armazenamento e o monitoramento do desempenho da equipe, mitigando falhas de comunicação e gargalos operacionais.

---

## 📌 Escopo do Projeto e Funcionalidades

O sistema consiste em uma API REST desenvolvida em Python voltada para o gerenciamento de tarefas do ecossistema logístico.
* **Operações CRUD:** Criação, listagem e exclusão de tarefas em tempo real.
* **Dados da Tarefa:** ID autoincrementável, Título, Descrição, Status (A Fazer, Em Progresso, Concluído) e Prazo Limite.
* **Validação de Dados:** Mecanismos de segurança que impedem o cadastro de tarefas sem campos obrigatórios (como o título).

---

## Gestão de Mudanças

Durante o desenvolvimento do sistema, foi identificada a necessidade de incluir um campo de prazo para as tarefas. Inicialmente, o sistema permitia apenas o cadastro do título, descrição e status das atividades.

A adição do campo de prazo foi motivada pela necessidade de melhorar o acompanhamento das entregas e auxiliar a equipe na organização das tarefas de acordo com suas datas limite. Com essa funcionalidade, os usuários podem visualizar quais atividades possuem maior urgência, facilitando o planejamento e a priorização do trabalho.

Essa alteração representa uma mudança de escopo do projeto e demonstra a flexibilidade das metodologias ágeis, que permitem adaptar o sistema às necessidades identificadas durante o processo de desenvolvimento.
