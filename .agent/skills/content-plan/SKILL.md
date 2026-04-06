---
name: content-plan
description: Plan and generate shoot-day-ready Instagram content across 5 formats. Supports batch planning for multi-week content sprints.
argument-hint: [topic] [--freebie=yes|no] [--keyword=KEYWORD] [--batch=topics.txt] [--start-date=YYYY-MM-DD] [--generate-topics=N]
---

# Content Plan Skill

## Overview

Generates a complete, shoot-day-ready content plan from a single topic across 5 Instagram formats. Each format gets a full script, production table, Instagram caption, and format-specific assets (Remotion configs, carousel slides, diagram descriptions).

Integrates with the existing IG content analyzer pipeline for brand voice consistency, Airtable tracking, and performance feedback.

## Purpose

- Turn any topic into 5 format-specific content pieces in one pass
- Generate shoot-ready scripts with timing, visual cues, and production tables
- Auto-render carousel slides via Remotion
- Generate ManyChat DM automation copy for freebie content
- Track everything in Airtable with linked Content Plans
- Support batch planning for 90-piece content sprints (18 topics x 5 formats)

## Input Requirements

### Required
1. **Topic** — the subject of the content (e.g., "Setting up your first AI automation", "3 automations that saved my client 20 hours/week")

### Optional
2. `--freebie=yes|no` — whether to include ManyChat freebie CTA (default: no, uses teaching CTA)
3. `--keyword=WORD` — ManyChat trigger keyword (default: derived from topic, only used when --freebie=yes)
4. `--batch=file.txt` — path to a file with one topic per line for batch planning
5. `--start-date=YYYY-MM-DD` — first post date for scheduling (default: 7 days from today)
6. `--generate-topics=N` — auto-generate N topics from content pillars + Airtable trends + Skool pain points

## Brand Voice Integration

**CRITICAL: Load brand voice before generating any content.**

1. Load the brand profile YAML:
   ```python
   # From: tools/ig_content_analyzer/brand_profiles/aisystemsbyjon/aisystemsbyjon.yaml
   ```

2. Detect content type from the topic using keyword matching:
   - `educational` — how to, tutorial, beginner, getting started, basics
   - `smb_automation` — automation, workflow, CRM, client, ROI, save time
   - `community` — production, API, architecture, advanced, edge case
   - `personal` — milestone markers, emotional content, raw energy

3. Build brand context using the content type for voice routing:
   ```python
   # Calls: analyze_content.build_brand_context(profile, content_type, 'aisystemsbyjon')
   ```

4. Apply these rules to ALL generated scripts:
   - **3-line opening**: Hook (high TAM + curiosity) → Credibility (why listen?) → Value Bridge (what you'll get)
   - **Enumeration**: "One, Two, Three" — NOT "Number one, Number two"
   - **Ad-lib markers**: Insert `[AD-LIB]` between major points for breathing room
   - **Profanity**: Strategic, not decorative. Every cuss word earns its spot.
   - **Banned phrases**: "Ever wonder", "Let's dive in", "Buckle up", "Game-changer", "without further ado", LinkedIn jargon
   - **Sentence style**: Short punchy sentences. Fragments for emphasis. "Right?" as conversational anchor.

## CTA Strategy (Dual System)

### Teaching CTA (default, `--freebie=no`)
Used when content teaches something or saves time.
> "Boom, just saved you [specific thing]. Venmo me $5 for a coffee."

Rules:
- Value bridge is mandatory — state what you saved them
- The $5 coffee line is personality play, tongue-in-cheek
- NO product CTAs, NO "link in bio", NO "DM me"
- Vary the value bridge per topic

### Freebie CTA (`--freebie=yes`)
Used when giving away a downloadable resource.
> "Comment [KEYWORD] and I'll DM you the [freebie name]."

Rules:
- Keyword must be single word, ALL CAPS, memorable
- Caption must reinforce the keyword CTA
- ManyChat DM flow copy is generated (see Section 8)

## Execution Steps

### Step 1: Research Context

Before writing anything, gather:

1. Load the brand profile from `tools/ig_content_analyzer/brand_profiles/aisystemsbyjon/aisystemsbyjon.yaml`
2. Detect content type from the topic
3. Build brand voice context string
4. If in batch mode: check for topic overlap with existing content plans in Airtable
5. Pull format specs from `generate_content_plan.py:FORMAT_SPECS`

### Step 2: Generate the Plan

For the given topic, generate ALL of the following sections. Each section is a discrete content piece for one format.

---

### Section 1: Topic Overview

| Field | Value |
|-------|-------|
| **Topic** | [the topic] |
| **Content Type** | [educational / smb_automation / community / personal] |
| **CTA Type** | [teaching / freebie] |
| **ManyChat Keyword** | [KEYWORD or N/A] |
| **Target Formats** | 5 (Studio, Cell Phone, Green Screen, Carousel, Tutorial) |

---

### Section 2: Hooks (10 Options)

Generate 10 hooks using these 10 psychological triggers (one each):

| # | Hook Type | Description |
|---|-----------|-------------|
| 1 | Trend Ride | Validate awareness of a current trend |
| 2 | Simplicity Promise | Remove the biggest barrier + time promise |
| 3 | Curiosity Gap | Make them feel like they're missing something |
| 4 | Bold Claim | Lead with the outcome, promise to show how |
| 5 | Direct Question | Call out the exact audience + empathize |
| 6 | Contrarian | Break the assumption holding the audience back |
| 7 | FOMO / Urgency | Social pressure + helpful rescue |
| 8 | Before-After | Relatable pain + clear upgrade path |
| 9 | Demo Tease | Promise a demo, create anticipation |
| 10 | Authority | Credibility-first, establish trust |

For each hook include:
- The hook line (as spoken text, following the contrast pattern from brand profile)
- Type label
- Why it works (1 sentence)
- Best format (which of the 5 formats it suits best)
- Carousel cover version (adapted as a bold headline, max 8 words)

**Hook rules from brand profile:**
- Line 1 must have HIGH TAM (Total Addressable Market) + curiosity
- Preferred pattern: contrast ("Most people think X, but Y")
- Must follow `script_structure.line_1_hook` from the YAML

---

### Section 3: Format 1 — Studio Reel (60s)

**Specs Table:**

| Spec | Value |
|------|-------|
| Aspect Ratio | 9:16 (1080x1920) |
| Duration | 60 seconds |
| Word Target | ~172 words (energetic pace) |
| Tone | Energetic, polished |
| Editing | Remotion (talking head + screen recordings + b-roll) |
| Framework | Hook → Credibility → Value Bridge → Body → CTA |

**Full Voiceover Script:**

Write the complete script with section labels and timing:

```
[0:00-0:03] HOOK
[selected hook from Section 2]

[0:03-0:08] CREDIBILITY
[Line 2 — "Super Hook" — why should I listen?]
[Use or adapt a proof point from brand profile credibility section]

[0:08-0:12] VALUE BRIDGE
[Line 3 — "Speed 2 Value" — what you're about to get]
[Use a template from script_structure.line_3_value_bridge]

[0:12-0:50] BODY
[AD-LIB]
[Main content — numbered points if applicable]
[Use bare numbers: "One," "Two," "Three,"]
[Leave [AD-LIB] markers between major points]

[0:50-0:60] CTA
[Teaching or Freebie CTA based on --freebie flag]
```

**Production Table:**

| Time | Visual | Audio | On-Screen Text |
|------|--------|-------|----------------|
| 0-3s | Talking head, direct to camera | Hook line | [Hook text overlay] |
| 3-8s | [Describe visual] | [Describe audio] | [Text overlay] |
| ... | ... | ... | ... |

**B-Roll / Screen Recording Shot List:**

| # | Shot Description | Type | Duration | Notes |
|---|-----------------|------|----------|-------|
| 1 | [Describe exact shot needed] | Screen recording / B-roll | Xs | [Setup notes] |
| ... | ... | ... | ... | ... |

**Remotion Scene Config:**
Generate JSON matching the Scene interface:
```json
{
  "hook": "...",
  "keyword": "...",
  "scenes": [
    {"type": "talkingHead", "title": "...", "durationInFrames": 90, ...},
    {"type": "split", "title": "...", "brollType": "image", "brollSrc": "...", ...}
  ],
  "fps": 30,
  "durationInFrames": 1800
}
```

**Instagram Caption:**
Write a ready-to-paste caption (300-400 words) with:
- Opening line that hooks (different from video hook)
- Value summary (what they'll learn)
- CTA (teaching or freebie)
- 3 relevant hashtag sets (rotate): AI/Tech, Entrepreneur/Business, Content Creator
- Engagement prompt ("Save this for later" or "Tag someone who needs this")

---

### Section 4: Format 2 — Cell Phone Reel (30-45s)

**Specs Table:**

| Spec | Value |
|------|-------|
| Aspect Ratio | 9:16 (1080x1920) |
| Duration | 30-45 seconds |
| Word Target | ~110 words |
| Tone | Raw, conversational, native |
| Editing | None — captions only, one-take |
| Shot | Handheld, no b-roll, no music |

**Shooting Instructions:**

| Setting | Instruction |
|---------|-------------|
| Camera | Phone, selfie mode, handheld (slight movement OK) |
| Framing | Head and shoulders, slightly off-center |
| Lighting | Natural light or ring light, nothing fancy |
| Audio | Phone mic or lav mic, quiet room |
| Takes | Film 3 takes, pick the most natural one |

**Full One-Take Script (~110 words):**

Write as spoken words — conversational, not copy. Include `[AD-LIB]` markers:

```
[HOOK — 3 seconds]
[Selected hook, adapted for casual delivery]

[AD-LIB — pause, react]

[INSIGHT — 15-20 seconds]
[Core point, said like you're telling a friend]
[Keep it to ONE main idea, not a list]

[AD-LIB — "right?" or "you know what I mean?"]

[QUICK WIN — 10 seconds]
[One actionable thing they can do RIGHT NOW]

[CTA — 5 seconds]
[Teaching or Freebie CTA]
```

**On-Screen Text (max 3 overlays):**
1. Opening: [Hook text, bold, 3s]
2. Key moment: [Core insight, 5s]
3. CTA: [CTA text or keyword, 5s]

**Instagram Caption:**
Shorter than studio reel — 150-200 words. More casual tone. Same hashtag rotation.

---

### Section 5: Format 3 — Green Screen Reel (45-60s)

**Specs Table:**

| Spec | Value |
|------|-------|
| Aspect Ratio | 9:16 (1080x1920) |
| Duration | 45-60 seconds |
| Word Target | ~130 words |
| Tone | Authoritative, walkthrough |
| Editing | CapCut — chroma key + background placement |
| Background | Diagram, flowchart, or tool screenshot |

**Shooting Instructions:**

| Setting | Instruction |
|---------|-------------|
| Green Screen | Wrinkle-free, evenly lit |
| Framing | Waist up, positioned to left or right (leave room for visual) |
| Lighting | Key light on face, separate light on green screen |
| Audio | Lav mic or shotgun mic |
| Gestures | Point to visual elements, use hand gestures for emphasis |

**Background Visual Description:**
[Describe the exact diagram/flowchart/screenshot to prepare BEFORE shoot day. Be specific: what boxes, arrows, labels, tools shown.]

**Full Script (~130 words) with visual cues:**

```
[HOOK — 3 seconds]
[Selected hook]
[VISUAL: Title card or hook text on background]

[SETUP — 10 seconds]
[Context for the visual behind you]
[VISUAL: Full diagram/flowchart visible]

[WALKTHROUGH — 25-35 seconds]
[Walk through each element of the visual]
[VISUAL: Highlight section 1]
[Point to it] One, [explain]
[AD-LIB]
[VISUAL: Highlight section 2]
Two, [explain]
...

[CTA — 5 seconds]
[Teaching or Freebie CTA]
[VISUAL: CTA text overlay on background]
```

**Editing Notes:**
- Chroma key settings: [color range, spill suppression]
- Background placement: [where the visual goes, scale, position]
- Text overlays: [what text appears and when]

**Instagram Caption:**
250-300 words. Reference the visual ("See that flowchart behind me?"). Same hashtag rotation.

---

### Section 6: Format 4 — Carousel (5-10 slides)

**Specs Table:**

| Spec | Value |
|------|-------|
| Resolution | 1080x1350 (4:5) |
| Slides | 5-10 (justify count — every slide earns its spot) |
| Style | Dark background, bold text, checklist format |
| Rendering | Remotion CarouselSlide composition → PNG |

**Slide-by-Slide Content:**

For EVERY slide, provide:

| Slide | Type | Headline | Body | Visual | Purpose |
|-------|------|----------|------|--------|---------|
| 1 | Cover | [Bold hook headline, max 8 words] | [Subheadline] | [Brand colors, bold typography] | Stop the scroll |
| 2 | Context | [The "what" and "why"] | [1-2 sentences] | [Simple icon or illustration] | Set the frame |
| 3-N | Checklist | [Step title] | [3-5 actionable checklist items per slide] | [Checklist layout with checkboxes] | Teach the thing |
| N+1 | Proof | [Outcome/result] | [Stat or testimonial] | [Before/after or metric] | Build belief |
| Last | CTA | [CTA headline] | [Teaching or Freebie CTA] | [Bold keyword if freebie] | Drive action |

**Checklist slide rules:**
- Each item is a DIRECT INSTRUCTION the viewer can follow
- "Go to code.visualstudio.com" — NOT "Install VS Code"
- "Click the Extensions icon (four squares)" — NOT "Find extensions"
- Max 40 words per slide body
- 3-5 checklist items per slide

**Carousel Slide JSON** (for Remotion rendering):
```json
{
  "slides": [
    {
      "slideNumber": 1,
      "slideType": "cover",
      "headline": "...",
      "body": "...",
      "checklistItems": [],
      "visualDescription": "..."
    },
    ...
  ]
}
```

**Instagram Caption:**
350-450 words (carousels get longer captions). Lead with a question or bold statement. Include "Save this for your next [X]" — carousels have the highest save rate. Freebie CTA if applicable.

---

### Section 7: Format 5 — Tutorial Walkthrough (60-90s)

**Specs Table:**

| Spec | Value |
|------|-------|
| Aspect Ratio | 9:16 (1080x1920) |
| Duration | 60-90 seconds |
| Word Target | ~200 words |
| Tone | Patient, demo-driven, show-don't-tell |
| Editing | Screen recording + cuts between steps |

**Full Narration Script (~200 words) with screen markers:**

```
[HOOK — 3 seconds]
[Selected hook]
[SCREEN: Show the end result first — what they'll build]

[VALUE BRIDGE — 5 seconds]
[Line 3 — what they're about to get]
[SCREEN: Still showing result]

[STEP 1 — 15 seconds]
[SCREEN: Open [specific tool/website]]
[Narrate exactly what you're clicking]
"First thing, go to [URL]. Click [button]."

[AD-LIB]

[STEP 2 — 15 seconds]
[SCREEN: Next action]
[Narrate what's happening]

[STEP 3 — 15 seconds]
[SCREEN: Next action]
[Narrate what's happening]

[RESULT — 10 seconds]
[SCREEN: Show the completed thing working]
"And that's it. You now have [outcome]."

[CTA — 5 seconds]
[Teaching or Freebie CTA]
[SCREEN: CTA text overlay]
```

**Screen Recording Shot List:**

| # | Screen/Tool | Action | Duration | Notes |
|---|-------------|--------|----------|-------|
| 1 | [Tool name] | [Exact action to record] | Xs | [Resolution, zoom level] |
| ... | ... | ... | ... | ... |

**Instagram Caption:**
250-300 words. Start with "Full tutorial in 60 seconds." or similar. Include step summary in caption for people who don't watch.

---

### Section 8: ManyChat Automation (if `--freebie=yes`)

**Skip this section if `--freebie=no`.**

**Flow Overview:**
```
User comments KEYWORD on post
    ↓
Auto-reply (rotate 3 options)
    ↓
DM: Opening message + "Send me the link" button
    ↓
Follow gate check (if not following → follow prompt)
    ↓
DM: Delivery message + PDF/link button
    ↓
(24h later) DM: Follow-up if no click
    ↓
Tag subscriber: "{KEYWORD}_lead"
```

**Workflow Name:** `{KEYWORD} DM`

**3 Rotating Comment Auto-Replies:**
1. [Friendly, excited: "Sending it to your DMs right now!"]
2. [Value-add: "Great choice — this one's 🔥. Check your DMs."]
3. [Social proof: "You're going to love this. Just sent it over!"]

**Opening DM:**
> Hey! Saw you commented {KEYWORD} — love it.
>
> I put together a [freebie description] that walks you through [what it covers].
>
> Want me to send it over?
>
> [BUTTON: "Send me the link"]

**Follow Gate Text:**
> Quick thing — I share stuff like this all the time. Follow me so you don't miss the next one, and I'll send it right over.

**Delivery DM:**
> Here's your [freebie name]!
>
> Inside you'll find:
> - [Section 1 summary]
> - [Section 2 summary]
> - [Section 3 summary]
>
> [BUTTON: "Get the guide" → link]
>
> Let me know if you have any questions. I read every DM.

**Follow-up DM (24h, if no click):**
> Hey — just checking in. Did you get a chance to grab the [freebie name]?
>
> [BUTTON: "Get it now" → link]

**Subscriber Tag:** `{KEYWORD}_lead`

---

### Section 9: Freebie PDF Outline (if `--freebie=yes`)

**Skip if `--freebie=no`.**

| Field | Value |
|-------|-------|
| File Name | `{topic-slug}-guide.pdf` |
| Page Count | 8-12 pages |
| Hosting | Google Drive (shareable link) or ManyChat attachment |

**Table of Contents:**

1. **Set Up [Primary Tool]** — Installation, account creation, first-run verification
2. **[Topic Step 1]** — [Description]
3. **[Topic Step 2]** — [Description]
4. **[Topic Step 3]** — [Description]
5. **Quick Reference** — Summary checklist of all steps
6. **What to Build Next** — 3 follow-up projects to try

---

### Section 10: Posting Strategy

**Posting Sequence** (for this topic's 5 pieces):

| Day | Time | Format | Why This Order |
|-----|------|--------|----------------|
| Day 1 | 8am | Cell Phone Reel | Raw content seeds the topic, tests audience interest |
| Day 3 | 12pm | Green Screen Reel | Visual authority builds on the seed |
| Day 5 | 12pm | Tutorial Walkthrough | Deep demo for engaged viewers |
| Day 7 | 6pm | Studio Reel | Polished version for peak evening browsing |
| Day 9 | 8am | Carousel | Save-worthy reference, extends shelf life |

**Hashtags** (10, rotate across posts):
[Generate 10 topic-relevant hashtags, mix of high-volume and niche]

**Best Time to Post:** Based on slot assignment from schedule rotation
**Accounts to Tag:** 1-2 relevant accounts (if applicable, otherwise skip)

---

### Section 11: Content Format Comparison

| Metric | Studio | Cell Phone | Green Screen | Carousel | Tutorial |
|--------|--------|------------|--------------|----------|----------|
| Effort | High | Low | Medium | Medium | Medium |
| Reach | Medium | High | Medium | Medium | Medium |
| Save Rate | Medium | Low | Medium | High | High |
| Authority | High | Low | High | Medium | High |
| Completion Rate | Medium | High | Medium | N/A | Medium |
| Shelf Life | Long | Short | Medium | Long | Long |
| Repurpose | YouTube, TikTok | TikTok, Shorts | TikTok | Pinterest, LinkedIn | YouTube, Blog |

---

### Section 12: Repurposing Matrix

| Platform | Source Format | Adaptation |
|----------|-------------|------------|
| TikTok | Cell Phone Reel | Direct repost, add TikTok captions |
| YouTube Shorts | Studio Reel | Re-export without IG watermark |
| LinkedIn | Carousel | Convert slides to document post |
| Twitter/X | Any Reel | 30s clip + thread with key points |
| Pinterest | Carousel | Pin each slide individually |
| Email | Tutorial | Embed link + step summary |
| Blog | Tutorial + Carousel | Expand into full written tutorial |

---

### Section 13: Production Checklist

**Pre-Production:**
- [ ] All 10 hooks reviewed, best hook selected per format
- [ ] Screen recordings captured for studio reel + tutorial
- [ ] Green screen background diagram/flowchart designed
- [ ] Carousel slides rendered as PNGs via Remotion
- [ ] ManyChat flow built (if freebie)
- [ ] Freebie PDF created and hosted (if freebie)
- [ ] B-roll assets identified and downloaded

**Production:**
- [ ] Studio reel filmed (multiple takes)
- [ ] Cell phone reel filmed (3 takes, pick best)
- [ ] Green screen reel filmed
- [ ] Tutorial screen recording captured
- [ ] Voiceover recorded for tutorial (if separate from screen rec)

**Post-Production:**
- [ ] Studio reel edited in Remotion
- [ ] Green screen reel edited in CapCut
- [ ] Tutorial walkthrough cuts assembled
- [ ] All captions reviewed and finalized
- [ ] Carousel PNGs quality-checked

**Publishing:**
- [ ] Day 1: Cell phone reel posted (8am)
- [ ] Day 3: Green screen reel posted (12pm)
- [ ] Day 5: Tutorial walkthrough posted (12pm)
- [ ] Day 7: Studio reel posted (6pm)
- [ ] Day 9: Carousel posted (8am)
- [ ] Cross-posted to TikTok (reels)
- [ ] Cross-posted to LinkedIn (carousel)

**Post-Launch:**
- [ ] ManyChat delivery tested (if freebie)
- [ ] 24h metrics checked (views, saves, comments)
- [ ] 48h metrics checked
- [ ] 7d metrics checked
- [ ] Performance scored in Airtable

---

### Section 14: Metrics to Track

| Metric | Where to Find | What It Tells You |
|--------|--------------|-------------------|
| Views | IG Insights | Reach / distribution |
| Completion Rate | IG Insights → Reels | Hook strength + content hold |
| Saves | IG Insights | Value perception (especially carousels) |
| Shares | IG Insights | Virality potential |
| Keyword Comments | Post comments | Freebie interest / ManyChat triggers |
| DMs Sent | ManyChat analytics | Funnel conversion |
| PDF Link Clicks | ManyChat / Google Drive | Freebie engagement |
| New Followers | IG Insights | Follow gate effectiveness |

**Success Benchmarks:**

| Metric | Good | Great | Exceptional |
|--------|------|-------|-------------|
| Views | 500+ | 2,000+ | 10,000+ |
| Completion Rate | 30%+ | 50%+ | 70%+ |
| Save Rate | 3%+ | 7%+ | 15%+ |
| Keyword Comments | 10+ | 50+ | 200+ |
| PDF Clicks | 20%+ of DMs | 40%+ | 60%+ |

---

### Step 3: Save to Airtable

After generating all sections, save each content piece to Airtable:

```bash
cd tools/ig_content_analyzer/execution

# The skill calls generate_content_plan.py functions:
# 1. create_content_plan() → creates the plan record
# 2. save_content_piece() → saves each format's script with metadata
# 3. generate_posting_schedule() → assigns dates and time slots
```

For each of the 5 formats, call `save_content_piece()` with:
- `plan_record_id`: The Airtable record ID from create_content_plan()
- `topic`: The topic string
- `format_type`: studio_reel | cell_phone_reel | green_screen_reel | carousel | tutorial_walkthrough
- `script_data`: Dict containing script, hooks, caption, production notes, carousel slides (if applicable), remotion config (if applicable)

### Step 4: Generate Assets (if applicable)

**Carousel PNGs** (always):
```bash
cd tools/ig_content_analyzer/remotion_templates
npx remotion still CarouselSlide "out/carousel/{topic-slug}/slide-1.png" --props='<slide-json>'
```

**Remotion Studio Reel Config** (always for studio reels):
Save the JSON config to `tools/ig_content_analyzer/remotion_templates/src/data/{topic-slug}_reel.json`

## Output

### Save the files
- Content plan markdown: `content-creation/plans/{topic-slug}-content-plan.md`
- Carousel slide JSON: `tools/ig_content_analyzer/remotion_templates/src/data/{topic-slug}_carousel.json`
- Studio reel config: `tools/ig_content_analyzer/remotion_templates/src/data/{topic-slug}_reel.json`
- All scripts: Airtable Generated Scripts table (linked to Content Plan)

### Confirm to user
1. File path of the saved plan
2. Number of hooks generated (should be 10)
3. Formats generated (should be 5)
4. CTA type used (teaching or freebie)
5. ManyChat keyword (or "N/A")
6. Number of carousel slides
7. Number of production checklist items
8. Airtable record IDs for each piece

## Quality Standards

Every plan must meet these standards before saving:

- [ ] All 10 hooks are distinct (no two use the same psychological trigger)
- [ ] All 10 hooks follow the contrast pattern from the brand profile
- [ ] Studio Reel script hits ~60s at energetic pace (~172 words)
- [ ] Cell Phone Reel script reads like speech, not copy (conversational, with [AD-LIB] markers)
- [ ] Green Screen Reel includes [VISUAL:] markers at every background change
- [ ] Tutorial Walkthrough includes [SCREEN:] markers at every action
- [ ] Carousel slide count is justified (every slide earns its spot, checklist items are direct instructions)
- [ ] Production checklist is exhaustive (nothing missing for shoot day)
- [ ] All captions are ready to paste (no placeholders, correct hashtags, correct CTA)
- [ ] CTA matches the --freebie flag (teaching = Venmo $5, freebie = keyword comment)
- [ ] No banned phrases in any script
- [ ] Brand voice anti-patterns avoided (no corporate speak, no passive voice, no filler)
- [ ] ManyChat flow copy complete (if --freebie=yes)
- [ ] Remotion scene JSON matches Scene interface (if studio reel)

## Batch Planning Mode

When given `--batch=topics.txt` or `--generate-topics=N`:

1. **Topic sourcing** (if `--generate-topics`):
   - Load brand profile content pillars (umbrella, problems, credibility)
   - Query Airtable for trending concepts: `generate_content_plan.py --trending --min-virality 8`
   - Optionally run Skool scraper: `clients/borrowedbelief/skool_scraper/execution/analyze_community_sentiment.py`
   - Merge sources into N unique topics, tagged with content_type

2. **Generate one topic at a time** (all 5 formats per topic)

3. **Save progress after each topic** to Airtable

4. **Show progress**: "Topic 3/18 complete. 15 pieces generated so far."

5. **After all topics**: Generate the 30-day posting schedule using `generate_posting_schedule()`

6. **Export calendar view** and first week's shoot-day checklists
