``` mermaid
sequenceDiagram
    participant Aluno
    participant Sistema
    participant Professor

    Aluno ->> Sistema: Login
    Sistema -->> Aluno: Confirmação de login

    loop Agendamento de Entrevista
        Aluno ->> Sistema: Escolher tipo de entrevista
        Sistema -->> Aluno: Confirmação do tipo de entrevista selecionado
        Aluno ->> Sistema: Agendar entrevista
        Sistema -->> Aluno: Confirmação do agendamento
    end

    loop Reagendar ou Cancelar Entrevista
        Aluno ->> Sistema: Reagendar ou cancelar entrevista
        Sistema -->> Aluno: Confirmação do reagendamento ou cancelamento
    end

    Aluno ->> Sistema: Realizar teste de nivelamento
    Sistema -->> Aluno: Resultado do teste de nivelamento

    Aluno ->> Sistema: Baixar script de estudo
    Sistema -->> Aluno: Script disponível para download

    Aluno ->> Sistema: Participar da entrevista
    Professor ->> Sistema: Conduzir entrevista
    Sistema -->> Aluno: Confirmação da entrevista
    Sistema -->> Professor: Confirmação da entrevista