# WhatsApp Automated Messaging Bot

Este projeto utiliza `Selenium` para automatizar o envio de mensagens pelo WhatsApp Web. O script oferece dois modos de envio: mensagens únicas para múltiplos números e mensagens personalizadas para cada número.

---

## ⚠️ Aviso Legal

**Este projeto é destinado exclusivamente para fins educacionais e de teste. O uso inadequado, como envio de spam ou mensagens não solicitadas, pode violar os termos de uso do WhatsApp e resultar em penalidades para a conta. Use de maneira ética e responsável.**

---

## Funcionalidades

- **Modo 1:** Envia a mesma mensagem para vários números.
- **Modo 2:** Envia mensagens personalizadas para números específicos, com base em um arquivo de configuração.

---

## Pré-requisitos

1. **Microsoft Edge** instalado.
2. Caminho do Edge WebDriver configurado corretamente (`msedgedriver.exe`).
3. Perfil do navegador configurado com login no WhatsApp Web.
4. Arquivos de texto com a lista de números:
   - `numeros.txt` (para mensagens únicas).
   - `numeros_mensagem.txt` (para mensagens personalizadas no formato `numero;mensagem`).

---

## Como usar

1. Clone o repositório e instale as dependências:

   ```bash
   git clone https://github.com/wpfsilvaa/whatsapp-bot.git
   cd whatsapp-bot
   pip install selenium
   ```

2. Configure os arquivos:
   - `numeros.txt`: Lista de números no formato `5511999999999`, um por linha.
   - `numeros_mensagem.txt`: Cada linha no formato `5511999999999;Sua mensagem personalizada`.

3.Altere o script pro funcionamento ficar correto:
   12   usuario_dir = "C:/Users/`SEU_USUARIO`/AppData/Local/Microsoft/Edge/User Data/`NOVO_PERFIL_CRIADO`"

4. Execute o script:

   ```bash
   python whatsapp_bot.py
   ```

5. Escolha o modo de disparo:
   - `(1)`: Mensagem única para vários números.
   - `(2)`: Mensagens personalizadas.

---

## Estrutura do Projeto

```
.
├── whatsapp_bot.py          # Script principal
├── numeros.txt              # Lista de números para o Modo 1
├── numeros_mensagem.txt     # Lista de números e mensagens para o Modo 2
└── README.md                # Documentação
```

---

## Avisos Importantes

- **Tempo de espera aleatório:** O script inclui um intervalo aleatório entre envios para evitar comportamento suspeito.
- **Arquivos de texto válidos:** Certifique-se de que os arquivos de configuração estão no formato correto.
- **Termos de Uso do WhatsApp:** Automação excessiva pode levar à suspensão da conta.

---

## ⚠️ Aviso Legal

**Este projeto é destinado exclusivamente para fins educacionais e de teste. O uso inadequado, como envio de spam ou mensagens não solicitadas, pode violar os termos de uso do WhatsApp e resultar em penalidades para a conta. Use de maneira ética e responsável.**

---
