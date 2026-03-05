# Project Constitution (gemini.md)

This file contains the core invariants for the project.

## Data Schemas

### 1. Source of Truth: `campaign_structure.json`

This JSON file defines the campaign hierarchy before ad copy is generated.

```json
{
  "campaign_name": "Local Search - [Business Name]",
  "ad_groups": [
    {
      "name": "Fades & Cuts",
      "keyword_theme": "skin fade",
      "target_keywords": [
        { "term": "skin fade near me", "match_type": "Exact" },
        { "term": "mens haircut [City]", "match_type": "Phrase" }
      ],
      "generated_ads": [] 
    }
  ]
}
```

### 2. Intermediate Ad Object

Structure for a single ad variant during generation/validation.

```json
{
  "headline_1": "Best Skin Fade in [City]",
  "headline_2": "Book Your Spot Today",
  "headline_3": "Rated #1 Barber",
  "description_1": "Expert cuts and hot towel shaves. Walk-ins welcome but appointments recommended.",
  "description_2": "Don't settle for less. strict attention to detail. 5-star result every time.",
  "final_url": "https://example.com/book"
}
```

### 3. Delivery Payload: Google Ads Editor CSV

The final output format.

**Columns:**
`Campaign`, `Ad Group`, `Keyword`, `Criterion Type` (Match Type), `Headline 1`, `Headline 2`, `Headline 3`, `Description 1`, `Description 2`, `Final URL`, `Path 1`, `Path 2`

## Behavioral Rules

### 1. Tone & Style

- **Direct Response**: Use high urgency and scarcity.
- **Phrasing**: "Book Now", "Walk-ins Welcome", "Limited Spots", "Rated #1".
- **Local Focus**: Always include [City] or "Near Me" context where tailored.

### 2. Constraints (The DO Framework)

- **Self-Annealing Validation**:
  - **Headlines**: MUST be <= 30 characters.
  - **Descriptions**: MUST be <= 90 characters.
  - **Logic**: If `len(copy) > limit`, the tool MUST rewrite it. DO NOT output invalid lengths.
- **Structure**: 1 Keyword Theme per Ad Group.

## Architectural Invariants

- **Layer 1: Architecture (`architecture/`)**: Technical SOPs. Markdown files defining goals, inputs, tools, and edge cases.
- **Layer 2: Navigation**: Decisions routed here. No direct execution of complex logic, always route to tools.
- **Layer 3: Tools (`tools/`)**: Deterministic Python scripts. Atomic, testable.
- **"Data-First" Rule**: Define JSON Schema (Input/Output shapes) before writing code.
- **Self-Annealing**:
    1. Analyze error.
    2. Patch script.
    3. Test fix.
    4. Update Architecture (SOP).
- **Deliverables**: Cloud-based final payload (Google Ads CSV).
- **Intermediates**: Local `.tmp/` files (ephemeral).

## Maintenance Log

- **[2026-02-10] System Initialized (v1.0)**:
  - **Core**: `generate_keywords.py` and `generate_ads.py` operational.
  - **Handshake**: `validate_ads.py` verified with automated tests.
  - **Styling**: `export_csv.py` and `generate_preview.py` generate verified outputs.
  - **Status**: Stable. End-to-end pipeline verified.
