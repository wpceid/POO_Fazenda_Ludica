# POO_Fazenda_Ludica

Repositório criado para entrega de exercício da aula de Engenharia de Software

# 🐄 Fazenda Lúdica com POO em Python

Este projeto simula uma fazenda lúdica utilizando os pilares da Programação Orientada a Objetos (POO) com Python.

## 🎯 Objetivos

- Aplicar os conceitos de:
  - Classe e Objeto
  - Herança
  - Polimorfismo
  - Encapsulamento
- Praticar controle de versão com Git e GitHub

## 🧩 Estrutura do Projeto

### 1. Classe Base: `Animal`

- **Atributos**: `nome`, `idade`
- **Métodos**:
  - `__init__`: inicializa os atributos
  - `emitir_som`: retorna `"O animal emite um som."`
  - `apresentar`: retorna `"Olá, sou [nome] e tenho [idade] anos."`

### 2. Subclasses

#### 🐶 `Cachorro`

- Atributo adicional: `raca`
- `emitir_som`: retorna `"Au! Au!"`

#### 🐱 `Gato`

- Atributo adicional: `cor_pelo`
- `emitir_som`: retorna `"Miau!"`

#### 🐮 `Vaca`

- Atributo adicional encapsulado: `__producao_leite_litros`
- `emitir_som`: retorna `"Muuu!"`
- Métodos:
  - `obter_producao_leite()`: retorna a produção atual
  - `registrar_ordenha(litros)`: atualiza a produção

### 3. Demonstração

Instâncias criadas:

```python
Cachorro("Rex", 3, "Labrador")
Gato("Mimi", 5, "Branco")
Vaca("Mimosa", 7, 25.5)
```