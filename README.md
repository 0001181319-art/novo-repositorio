# 🎮 API de Biblioteca de Jogos

Este projeto é uma API REST desenvolvida em **Python com Flask**, que permite gerenciar uma biblioteca de jogos.  
A aplicação realiza operações de **CRUD (Create, Read, Update, Delete)** utilizando um banco de dados **SQLite**.

---

## 🚀 Tecnologias utilizadas

- Python
- Flask
- SQLite
- Thunder Client (para testes de API)

---

## 📁 Estrutura do projeto
/seu-projeto
│
├── app.py
├── biblioteca_jogos.db (gerado automaticamente)
└── README.md

---

## ⚙️ Como executar o projeto

### 1. Instalar dependências

```bash
pip install flask
| Campo      | Tipo         |
| ---------- | ------------ |
| id         | INTEGER (PK) |
| nome       | TEXT         |
| genero     | TEXT         |
| preco      | REAL         |
| plataforma | TEXT         |

GET /jogos
GET /jogos/{id}
POST /jogos
{
  "nome": "GTA V",
  "genero": "Ação",
  "preco": 99.90,
  "plataforma": "PC"
}
PUT /jogos/{id}
{
  "nome": "GTA VI",
  "genero": "Ação",
  "preco": 199.90,
  "plataforma": "PS5"
}
DELETE /jogos/{id}
