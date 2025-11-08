# Projeto de Malware 


## 🚀 Descrição do Projeto

O objetivo é duplo:
1.  Implementar simulações básicas de um Ransomware e um Keylogger em Python.
2.  Refletir e documentar as estratégias de defesa, detecção e mitigação contra essas ameaças.

## 🛠️ Ferramentas Utilizadas
* **Python 3.x**
* **cryptography:** Para a simulação de Ransomware (criptografia Fernet).
* **pynput:** Para a simulação de Keylogger (captura de teclado).
* **smtplib:** Para o envio de logs por e-mail.

---

## 🔐 Parte 1: Simulação de Ransomware


### Como Executar (em Ambiente Seguro!)
1.  Execute `encrypt.py` para criptografar todos os arquivos `.txt` no diretório.
2.  Uma chave (`chave.key`) será gerada (guarde-a!).
3.  Uma nota de resgate (`LEIA_ME.txt`) será criada.
4.  Execute `decrypt.py` (que precisa da `chave.key`) para reverter o processo.



## ⌨️ Parte 2: Simulação de Keylogger



### Como Executar (em Ambiente Seguro!)
1.  Configure as credenciais de e-mail (e-mail e senha de app) no script.
2.  Execute o script `keylogger.pyw`.
3.  Digite em um bloco de notas ou navegador.
4.  O script irá capturar as teclas, salvar em `log.txt` e enviá-lo por e-mail.

---

## 🛡️ Reflexões sobre Defesa e Mitigação

Esta é a seção mais importante do estudo. Como nos protegemos?

### 1. Contra Ransomware
* **Backups:** A estratégia 3-2-1 (3 cópias, 2 mídias, 1 offsite) é a defesa mais eficaz.
* **EDR e Antivírus:** Soluções baseadas em heurística detectam o comportamento de criptografia em massa.
* **Patching:** Manter o sistema e softwares atualizados corrige vulnerabilidades.
* **Conscientização (Phishing):** Treinamento para não clicar em links ou anexos maliciosos.

### 2. Contra Keyloggers
* **Autenticação de Dois Fatores (MFA):** Torna a senha roubada inútil sem o segundo fator.
* **Gerenciadores de Senha:** O "auto-preenchimento" evita a digitação da senha, burlando a captura.
* **Firewall de Saída:** Pode bloquear a tentativa do keylogger de enviar os dados para o atacante.
* **Sandboxing:** Executar programas suspeitos em ambientes isolados para análise.
