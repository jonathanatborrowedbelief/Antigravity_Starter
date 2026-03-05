---
name: ui-ux-pro-max
description: Provides design intelligence for building professional UI/UX across multiple platforms and frameworks. Auto-activates when the user requests UI/UX work like building a landing page, dashboard, mobile app, or any web interface. Triggers on: "build a landing page", "design a UI", "create a dashboard", "make it look better", "style this component", or any visual/design request. Includes 67 UI styles, 96 color palettes, 57 font pairings, 99 UX guidelines, and 100 industry-specific reasoning rules.
---

# UI UX Pro Max

AI design intelligence for building professional, production-grade UI/UX across 13 tech stacks.

**Repo:** [github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **Site:** [uupm.cc](https://uupm.cc)

---

## When to Use This Skill

- User asks to build, design, or style any UI (landing pages, dashboards, apps, components)
- User wants to improve visual design or fix anti-patterns
- User needs a design system generated for their product type
- Any request involving: layout, color palettes, typography, UI styles, or UX patterns

---

## What's Available

| Resource | Count | Examples |
|---|---|---|
| UI Styles | 67 | Glassmorphism, Claymorphism, Brutalism, Neumorphism, Bento Grid, Minimalism, Dark Mode, AI-Native |
| Color Palettes | 96 | SaaS, E-commerce, Healthcare, Fintech, Beauty, Wellness, and more |
| Font Pairings | 57 | Curated Google Fonts combinations with import URLs |
| Chart Types | 25 | For analytics and dashboard use cases |
| UX Guidelines | 99 | Best practices, anti-patterns, accessibility |
| Reasoning Rules | 100 | Industry-specific design system generation (v2.0) |
| Tech Stacks | 13 | React, Next.js, Astro, Vue, Nuxt.js, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui, Jetpack Compose |

---

## How It Works

1. **You request** — Any UI/UX task: build, design, create, implement, review, fix, improve
2. **Design system generated** — AI analyzes your project type and generates a complete, tailored design system using 100 reasoning rules
3. **Smart matching** — Selects the best style, color palette, and font pairing for your domain
4. **Code generation** — Implements with proper colors, fonts, spacing, and best practices
5. **Pre-delivery check** — Validates against common UI/UX anti-patterns before output

---

## Design System Output (Example)

When triggered, the skill generates a structured design recommendation like:

```
TARGET: Serenity Spa
STYLE:  Soft UI Evolution — Soft shadows, calming, premium feel, organic shapes
COLORS: Primary #E8B4B8 (Soft Pink) | Secondary #A8D5BA (Sage) | CTA #D4AF37 (Gold)
FONTS:  Cormorant Garamond / Montserrat — Elegant, calming, sophisticated
AVOID:  Bright neon colors, harsh animations, dark mode, AI purple/pink gradients
```

---

## Pre-Delivery Checklist (Always Apply)

- [ ] No emojis as icons — use SVG (Heroicons or Lucide)
- [ ] `cursor-pointer` on all clickable elements
- [ ] Hover states with smooth transitions (150–300ms)
- [ ] Text contrast ≥ 4.5:1 (WCAG AA) in light mode
- [ ] Focus states visible for keyboard navigation
- [ ] `prefers-reduced-motion` respected
- [ ] Responsive at: 375px, 768px, 1024px, 1440px

---

## Supported Stacks

Just mention your stack in the prompt, or defaults to **HTML + Tailwind**.

- React · Next.js · Astro · Vue · Nuxt.js · Nuxt UI
- Svelte · SwiftUI · React Native · Flutter
- HTML + Tailwind · shadcn/ui · Jetpack Compose

---

## Usage Examples

```
# Auto-activate (just describe the task)
Build a landing page for my SaaS product
Create a dashboard for healthcare analytics
Design a portfolio website with dark mode
Make a mobile app UI for e-commerce
Build a fintech banking app with dark theme

# Slash command (for supported editors)
/ui-ux-pro-max Build a landing page for my SaaS product
```

---

## Advanced: Design System CLI

If the skill is installed locally (`.claude/skills/ui-ux-pro-max/`):

```bash
# Generate design system with ASCII output
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness" --design-system -p "Serenity Spa"

# Generate with Markdown output
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "fintech banking" --design-system -f markdown

# Domain-specific search
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "glassmorphism" --domain style
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "elegant serif" --domain typography
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "dashboard" --domain chart

# Stack-specific guidelines
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "form validation" --stack react
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "responsive layout" --stack html-tailwind
```

---

## Resources

- [GitHub Repo](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [Official Site — uupm.cc](https://uupm.cc)
