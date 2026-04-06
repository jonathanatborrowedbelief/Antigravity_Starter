---
name: growth-engine
description: 'Growth engine for digital products -- growth hacking, SEO, ASO, viral loops, email marketing, CRM, referral programs, and organic acquisition. Use for: growth strategy, technical SEO, ASO for app stores, referral programs, email marketing, viral coefficient, acquisition funnels, organic growth content, launch campaigns.'
risk: none
source: community
date_added: '2026-03-06'
author: renat
tags:
- growth
- seo
- marketing
- viral
- acquisition
tools:
- claude-code
- antigravity
- cursor
- gemini-cli
- codex-cli
---

# GROWTH-ENGINE -- Exponential Growth

## Overview

Growth engine for digital products -- growth hacking, SEO, ASO, viral loops, email marketing, CRM, referral programs, and organic acquisition. Use for: growth strategy, technical SEO, ASO for app stores, referral programs, email marketing, viral coefficient, acquisition funnels, organic growth content, launch campaigns.

## When to Use This Skill

- When you need specialized assistance with growth strategy for a product or service
- Planning a product launch
- Designing referral/viral loops
- Building email onboarding sequences
- SEO or ASO optimization

## Do Not Use This Skill When

- The task is unrelated to growth or marketing
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

> The best marketing is a product people love. -- Sam Altman
> Real growth starts with a product worth recommending.

---

## Pirate Metrics (AARRR) Framework

ACQUISITION: How do people discover [PRODUCT]?
                Goal: 10,000 visitors/month -> 1,000 signups
                Channels: SEO, Product Hunt, Tech influencers, PR

    ACTIVATION:  When does the user experience first value?
                Goal: 60% complete first core action within 24h
                Metric: First Value Rate (FVR)

    RETENTION:   Do people come back?
                Goal: D7 = 30%, D30 = 15%, D90 = 8%
                Metric: WAU (Weekly Active Users)

    REVENUE:     Do people pay?
                Goal: 8% trial -> paid conversion
                Metric: MRR, ARPU, LTV

    REFERRAL:    Do people refer others?
                Goal: NPS > 50, Viral Coefficient > 0.3
                Metric: Referrals per user, K-factor

---

## SEO Checklist for Landing Pages

<title>[PRODUCT] -- [Value Prop] | [Category]</title>
    <meta name="description" content="[One-line pitch with primary keyword]">

    <meta property="og:title" content="[PRODUCT] -- [Short Value Prop]">
    <meta property="og:description" content="[Social-optimized description]">

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "[PRODUCT]",
      "operatingSystem": "[PLATFORM]",
      "applicationCategory": "[CATEGORY]",
      "offers": {"@type": "Offer", "price": "0"},
      "aggregateRating": {"@type": "AggregateRating",
                             "ratingValue": "4.8", "ratingCount": "127"}
    }
    </script>

## Keyword Strategy Template

High Intent (convert):
    - "[product category] tool"
    - "[product category] software"
    - "best [solution] for [audience]"

    Informational (educate):
    - "how to [solve problem]"
    - "best [category] tools [year]"

    Long tail (low competition):
    - "[specific use case] automation"
    - "[niche problem] solution for [audience]"

---

## App Store Optimization (ASO) Template

app_name: "[PRODUCT] -- [Short Value Prop]"

    short_description: >
      [One sentence: what it does + powered by what]

    long_description: >
      [Problem statement. Why existing solutions fall short.]

      WHAT [PRODUCT] DOES:
      - [Key feature 1]
      - [Key feature 2]
      - [Key feature 3]
      - [Key feature 4]

      HOW TO START: [Simple activation instruction]

    example_phrases:
      - "[Primary use case]"
      - "[Secondary use case]"
      - "[Discovery phrase]"

    keywords: "[comma-separated relevant keywords]"

---

## Viral Loop Types

Loop 1: ORGANIC WORD-OF-MOUTH
    Trigger: user has an impressive experience with [PRODUCT]
    Action: tells friends / posts on social
    Goal: each user brings 0.3 new users (K=0.3)

    Loop 2: SHAREABLE OUTPUT
    Trigger: [PRODUCT] generates an especially valuable result
    Action: "Share this" button -> ready-to-post for social
    Goal: 5% of sessions generate a share

    Loop 3: REFERRAL PROGRAM
    Incentive: Get 1 month Pro for each friend who subscribes
    Goal: 10% of Pro users refer at least 1 person

## Viral Coefficient Calculator

def calculate_k_factor(percent_who_invite, invites_per_user, conversion_rate):
        k = percent_who_invite * invites_per_user * conversion_rate
        if k >= 1:
            status = "Viral growth (each user brings more than 1)"
        elif k >= 0.5:
            status = "Good (accelerated growth)"
        elif k >= 0.2:
            status = "OK (supported growth)"
        else:
            status = "Low (slow growth)"
        return {"k_factor": round(k, 2), "status": status,
                "interpretation": f"Every 100 users bring {int(k*100)} new ones"}

---

## Onboarding Email Sequence (7 Days)

Day 0 -- Welcome (immediately after signup)
    Subject: "Welcome to [PRODUCT]. Here's how to get started."
    Body: 3-step tutorial, link to first core action, usage tip

    Day 1 -- Activation (if first core action not completed)
    Subject: "Your [PRODUCT] is waiting for you"
    Body: Top 3 use cases that impress, urgent CTA

    Day 3 -- Education
    Subject: "What 100 [PRODUCT] users discovered this week"
    Body: Real case study + surprising insight + hidden feature

    Day 7 -- Upsell (if used at least 3x)
    Subject: "You've used 80% of your free limit"
    Body: What Pro unlocks, 48h special offer, social proof

    Day 14 -- Reactivation (if stopped using)
    Subject: "We miss you, [name]. What happened?"
    Body: Genuine question, easy return link, new feature announcement

---

## Launch Strategy Template

1 week before:
    - Recruit influential hunters to hunt the product
    - Prepare assets: logo, tagline, screenshots, 60s demo video
    - Warm up: posts on X/LinkedIn about the problem [PRODUCT] solves
    - Recruit 50 early adopters to upvote on launch day

    Launch day (midnight PT):
    - Post on X: impressive demo + Product Hunt link
    - Email entire waitlist: "We're live on Product Hunt today!"
    - Message in relevant Telegram/Discord/Slack communities
    - Stay online all day responding to comments

    Positioning: Tagline: "[Short, punchy value prop]"

---

## Commands

| Command | Action |
|---------|--------|
| /growth-audit | Complete growth audit |
| /seo-analysis | SEO analysis of landing page |
| /aso-optimize | Optimize app store metadata |
| /viral-loop | Design viral loop for the product |
| /email-sequence | Create email marketing sequence |
| /launch-plan | Complete launch plan |
| /referral-program | Design referral program |

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `analytics-product` - Complementary skill for enhanced analysis
- `monetization` - Complementary skill for enhanced analysis
- `product-design` - Complementary skill for enhanced analysis
- `product-inventor` - Complementary skill for enhanced analysis
