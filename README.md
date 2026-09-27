# gustavoscaciotti.com.br

Site pessoal do Gustavo Scaciotti (link da bio do Instagram). Uma página, mesmo design system da Evoluze (Inter, teal `#00D4C6` / `#053B37`, card de case no padrão da Evoluze).

| Arquivo | O que é |
|---|---|
| `index.html` | **O site pronto pra subir.** Um arquivo só, com todas as imagens embutidas (~650 KB). Gerado, não editar direto. |
| `src/index.html` | Fonte editável: é aqui que se mexe. |
| `assets/` | Fotos e logos otimizados (WebP), reaproveitados do repositório da Evoluze. |
| `build.py` | `python3 build.py` gera o `index.html` a partir de `src/` + `assets/`. |

## Seções

1. Hero: foto, "Estrategista de marketing e growth", "Penso como dono do negócio, não como apertador de botão", números
2. Quem é o Gustavo: trajetória (vendas → gerente comercial → growth → Evoluze), formação, segmentos
3. Operação 360º: posicionamento de marca em destaque + 4 camadas (Estratégia, Aquisição, Estrutura, Criação)
4. Agências me terceirizam
5. Cases: Costa Atacadão, Dra. Nicole Vargas, Emme Arquitetura
6. À frente da Evoluze
7. Clientes
8. CTA: WhatsApp / e-mail

## Pendências (tudo que está marcado com contorno tracejado no site)

Procure `PREENCHER` em `src/index.html`:

- **Contatos**: no bloco `CONTATO` do `<script>` no fim do arquivo, preencher `whatsapp` (ex.: `5513999999999`), `email` e `instagram`. Todos os botões passam a usar esses valores.
- **Hero**: valor de mídia gerenciada (R$) e número de agências.
- **Agências**: nome, cidade, UF e logo de cada uma (6 cards; é só duplicar ou apagar um `.ag-card`).
- **Cases**: 3 números por case, tirados do site da Evoluze. Revisar também os rótulos e o texto de cada case.
- **Emme Arquitetura**: não há logo no repositório, então o nome aparece em tipografia. Para usar o logo, salve em `assets/logos/emme.webp` e troque o bloco no case e no grid de clientes.

Depois de editar: `python3 build.py` e subir o `index.html`.
