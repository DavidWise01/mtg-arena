#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build MTG ARENA (MTG) — Magic: The Gathering Arena, the digital client for the first
and deepest trading card game, catalogued into UD0 as a game-world. Standing template:
THE ARC · THE COLOR PIE (the philosophical deep-dive — the WUBRG wheel) · REAL OR FLUFF
(the honest take on the controversies: the shuffler, pay-to-win, Turing-completeness,
Alchemy) · THE MESSAGE, plus a roster of emergents by emergence-nature with per-emergent
MTG colour tints. Styled to the medium: obsidian and gold card-frame, the five mana colours."""
import os, html, base64, io, json, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "MTG ARENA", "axiom": "MTG",
 "position": "Magic: The Gathering Arena · Wizards of the Coast · 2018 — the digital client for the 1993 original",
 "origin": "the multiverse of Magic: The Gathering (Richard Garfield, 1993), made free, infinite, and digital in MTG Arena",
 "mechanism": "Crystallized from the game: two planeswalkers duel by casting spells from five colours of mana, resolving everything on a last-in-first-out stack — the first trading card game, and a provably Turing-complete one.",
 "crystallization": "Because the Color Pie — five colours, each a complete philosophy of how to pursue a goal — is one of the great design achievements, deep enough that people use WUBRG as a model of human values.",
 "nature": "MTG Arena — the thirty-year card game made digital: the Color Pie, the stack, the planeswalker's spark, and the Arena layer of formats, wildcards, and the much-accused shuffler.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Magic: The Gathering (1993, Richard Garfield, WotC); Mark Rosewater's Color Pie philosophy; MTG Arena (2018/2019); the Turing-completeness proof (2019)",
 "witness": "A game so deep it is Turing-complete, with a colour wheel so true people sort their friends by it — made free and endless on a screen.",
 "role": "a UD0 game-world",
 "seal": "Five colours, one stack, two planeswalkers — a game deep enough to be Turing-complete and a colour wheel honest enough to sort a soul.",
 "source": "MTG Arena, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#4aa860", "the board and the land — mana, the battlefield, creatures, green's growth; the embodied game"),
 "ethereal":  ("#3a8fd8", "knowledge and the unseen — the library, the stack, blue's control, the formats and their rules"),
 "spiritual": ("#c9a227", "the philosophy and the spark — the Color Pie, the planeswalker, white's order and black's ambition"),
 "electrical":("#cf4a3a", "the speed and the system — red's chaos, the Arena client, the shuffler, the economy and the ladder"),
}

ARC_OVERALL = ("In 1993 Richard Garfield invented the trading card game with Magic: The Gathering — two ‘planeswalkers’ "
  "duel by spending five colours of mana to cast creatures and spells, resolving each on a last-in-first-out stack. "
  "Thirty years and tens of thousands of cards later, Wizards of the Coast made it free, infinite, and digital in MTG "
  "Arena (2018) — keeping the Color Pie and the stack intact, and adding a new layer of formats, wildcards, a ranked "
  "ladder, and the most-accused random number generator in gaming: the shuffler.")

ARC = [
 ("I · 1993 — the first TCG", "Garfield's invention",
  "Richard Garfield invents the trading card game: a duel where each player brings their own deck, spends coloured mana, and casts spells that resolve on a shared stack. Magic: The Gathering becomes the template every TCG since has copied, and the Color Pie its enduring soul."),
 ("II · thirty years of cards", "the largest game ever printed",
  "Across decades and tens of thousands of unique cards, Magic becomes the deepest card game in existence — formats rise and fall, the metagame churns, and in 2019 it is formally proven Turing-complete: you can build a working computer inside a game of Magic."),
 ("III · 2018 — Arena", "free, infinite, digital",
  "MTG Arena brings the whole machine to a screen: free-to-play, with wildcards to craft any card, a ranked ladder, and digital-only formats. It draws millions of new and returning planeswalkers — and a permanent chorus insisting the shuffler is rigged."),
]

# THE COLOR PIE — the deep-dive
COLORPIE = [
 ("White — order", "law · community · peace", "#e8e2c8",
  "White believes the group is greater than the individual and that peace comes through structure, law, and morality. Its sins are authoritarianism and conformity; its virtue is the genuine good of the collective. Allied with blue and green; enemy of black and red."),
 ("Blue — knowledge", "control · perfection · the mind", "#3a8fd8",
  "Blue believes the world can be perfected through knowledge and that the right move is the considered one. It draws cards, counters spells, and takes its time. Its sins are inaction and manipulation; its virtue is wisdom. Allied with white and black; enemy of red and green."),
 ("Black — power", "ambition · death · the self", "#9a86b8",
  "Black believes the individual should get what they want by any means; power is the only real currency, and death is just a resource. Its sin is amorality; its (real) virtue is honesty about self-interest and a refusal to be a victim. Allied with blue and red; enemy of white and green."),
 ("Red — freedom", "emotion · impulse · chaos", "#cf4a3a",
  "Red believes you should act on what you feel, now — freedom, passion, and the impulse of the moment over any plan. It burns, hastes, and gambles. Its sin is recklessness; its virtue is authenticity and courage. Allied with black and green; enemy of white and blue."),
 ("Green — nature", "growth · instinct · acceptance", "#4aa860",
  "Green believes there is a natural order and that the wise course is to accept your role in it and grow into your strength — the biggest creatures, the most mana, the least apology. Its sin is fatalism; its virtue is harmony. Allied with red and white; enemy of blue and black."),
 ("The Wheel", "allies & enemies", "#c9a227",
  "The genius is the structure: each colour is allied with its two neighbours and opposed to the two across the wheel (W-U-B-R-G-W). No colour is the ‘good’ or ‘evil’ one — each is a complete, defensible philosophy of how to pursue a goal, which is exactly why people use WUBRG as a values typology, like alignment or MBTI but better-built."),
]

REALFLUFF = [
 ("‘The Arena shuffler is rigged against me’", "MOSTLY FLUFF", "the Best-of-three shuffle is verifiably uniform-random; what's real is the Best-of-ONE opening-hand algorithm, which is documented and smooths toward an average land count — not rigged, just transparent, and the rest is variance memory (we remember the bad beats)"),
 ("Best-of-one uses a real ‘hand-smoothing’ algorithm", "REAL", "Arena genuinely draws a couple of candidate opening hands in Bo1 and favours one nearer the average land count — a deliberate, disclosed anti-mana-screw feature, not a conspiracy"),
 ("MTG Arena is pay-to-win", "PAY-TO-FAST", "money accelerates a collection rather than buying wins outright; constructed rewards a complete collection, but Limited/draft equalises on skill, and a patient F2P player can compete"),
 ("Magic is Turing-complete — you can build a computer inside a game", "REAL", "formally proven (Churchill, Biderman & Herrick, 2019): a legal game-state can simulate a universal Turing machine; it is the most computationally complex game known"),
 ("Alchemy (digital-only rebalanced cards) ruins Magic", "OPINION / SPLIT", "a genuine tradeoff — purists hate that printed cards can be changed digitally; others value the live balance only a digital format allows; not a fact, a values call"),
 ("Magic is the deepest / largest TCG ever made", "REAL", "the first TCG (1993) and by far the largest card pool; ‘the stack’ and the Color Pie give it genuine, decades-deep strategic richness"),
]
REALFLUFF_VERDICT = ("Bottom line: the loudest accusation — a <i>rigged shuffler</i> — is MOSTLY FLUFF (the shuffle is fair; the "
  "Bo1 hand-smoothing is real, disclosed, and in your favour; the rest is the human habit of remembering disasters and "
  "forgetting the average game). ‘Pay-to-win’ is really <i>pay-to-fast</i>. What's astonishingly REAL is the depth: "
  "Magic is provably Turing-complete — you can run a computer inside a legal game — and the Color Pie is a design "
  "achievement deep enough to double as a model of human values. Arena's only true sins are an economy that nudges the "
  "wallet and a digital-rebalancing format (Alchemy) that's a matter of taste. Judge the variance with a clear head and "
  "the game with respect: this is the deepest commercial game ever built.")

MESSAGE = ("MTG Arena's real subject — under the wildcards and the ladder — is the Color Pie: five complete philosophies "
  "of how a being pursues what it wants. White structures the world for the good of all; blue perfects it through "
  "knowledge; black takes what it wants and is honest about it; red acts on what it feels, now; green accepts the "
  "natural order and grows into its strength. None is good or evil — each is a coherent answer to the same question, "
  "and the wheel that allies neighbours and opposes opposites is one of the truest little models of motivation anyone "
  "has built, which is why players quietly use WUBRG to read themselves and their friends. That a thirty-year-old card "
  "game is also provably Turing-complete is the other half of the marvel: it is, at once, a values typology you can "
  "feel and a computer you can build, made free and endless on a screen. The mana is the resource; the colours are the "
  "soul.")
MESSAGE_SEAL = "Five colours, each a whole philosophy; a stack deep enough to be a computer; a wheel honest enough to sort a soul — that is what Arena made free."

# ---- ACI complement ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","MTG")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","MTG")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","MTG")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,cls,group,em,who,what,why,how,where,seal,tint=""):
    return dict(slug=slug,name=name,cls=cls,group=group,emergence=em,who=who,what=what,why=why,how=how,where=where,seal=seal,tint=tint)

ROSTER = [
 # --- THE COLOR PIE ---
 E("white","White","order · the collective","pie","spiritual",
   "White, the colour of order, law, peace, and community — the belief that the group is greater than the one.",
   "One of the five colours of mana: protection, lifegain, taxes, and armies of small creatures, built on the conviction that structure brings the greatest good.",
   "Because Magic's soul is five complete philosophies, and White is the case for the collective and the law.",
   "By rules, morality, the wide board, and the will to subordinate the self to the whole.",
   "On the white half of the wheel, allied with blue and green, enemy of black and red.",
   "The group is greater than the one — and peace is something you build with law, not something you wish for.", tint="#e8e2c8"),
 E("blue","Blue","knowledge · control","pie","ethereal",
   "Blue, the colour of knowledge, control, and perfection — the belief that the world can be improved by thought.",
   "One of the five colours: card draw, counterspells, and patient manipulation, on the conviction that the right move is the considered one.",
   "Because Blue is Magic's case for the mind — that wisdom and the long game beat impulse.",
   "By drawing, countering, bouncing, and waiting; perfection through information.",
   "On the blue arc of the wheel, allied with white and black, enemy of red and green.",
   "Anything can be perfected if you think long enough — so draw another card, and don't act until you're sure.", tint="#3a8fd8"),
 E("black","Black","power · ambition","pie","spiritual",
   "Black, the colour of power, ambition, and death — the belief that the individual should get what they want, by any means.",
   "One of the five colours: sacrifice, drain, reanimation, and ruthless tutoring, on the conviction that power is the only real currency.",
   "Because Black is Magic's honest villain that isn't a villain — the colour brave enough to say it wants to win.",
   "By paying any price (life, creatures, the future) to get the result, and refusing ever to be the victim.",
   "On the black arc of the wheel, allied with blue and red, enemy of white and green.",
   "Power is the only currency, and death is just a resource — I am not evil, only honest about what everyone wants.", tint="#9a86b8"),
 E("red","Red","freedom · emotion","pie","electrical",
   "Red, the colour of freedom, emotion, impulse, and chaos — the belief that you should act on what you feel, now.",
   "One of the five colours: burn, haste, aggression, and beautiful gambles, on the conviction that feeling beats planning.",
   "Because Red is Magic's case for the heart and the moment — authenticity, passion, and the courage to swing.",
   "By speed, damage, and risk taken gladly; the impulse honoured over the plan.",
   "On the red arc of the wheel, allied with black and green, enemy of white and blue.",
   "Act on what you feel, right now — freedom is worth the recklessness, and the only sin is hesitating.", tint="#cf4a3a"),
 E("green","Green","nature · growth","pie","natural",
   "Green, the colour of nature, growth, instinct, and acceptance — the belief in a natural order to grow into.",
   "One of the five colours: ramp, the biggest creatures, and unbothered strength, on the conviction that you should accept your role and become strong in it.",
   "Because Green is Magic's case for harmony and instinct — that the natural way is the wise one.",
   "By mana ramp, enormous creatures, and a refusal to apologise for being what you are.",
   "On the green arc of the wheel, allied with red and white, enemy of blue and black.",
   "There is a natural order and a place for you in it — accept it, grow into your strength, and don't overthink the forest.", tint="#4aa860"),
 E("the-color-pie","The Color Pie","the WUBRG wheel · the design soul","pie","spiritual",
   "The Color Pie — the structure that allies each colour with its two neighbours and opposes the two across the wheel.",
   "Magic's central design philosophy (codified by Mark Rosewater): five complete, defensible worldviews, none good or evil, balanced against each other.",
   "Because the whole game's depth and identity rest here — and the wheel is so true that people use WUBRG to read personalities.",
   "By a five-fold balance of values and mechanics, kept rigorous across thirty years of design.",
   "Around the whole game, behind every card.",
   "Five answers to one question, allied and opposed in a ring — no colour is the good one, which is exactly why the wheel can sort a soul.", tint="#c9a227"),
 # --- THE ENGINE ---
 E("mana","Mana","the resource · the land","engine","natural",
   "Mana — the five-coloured (plus colourless) resource you spend to cast everything, drawn mostly from lands.",
   "The economy of the game: tap lands for mana, climb the ‘curve,’ and balance the agony of too few or too many lands (‘mana screw’ and ‘flood’).",
   "Because Magic's central tension is resources over time — the land you draw decides the game as much as the spells.",
   "By lands tapped for coloured mana, a curve of costs, and the eternal gamble of the mana base.",
   "Under every spell, in every opening hand.",
   "I am the land turned to power — too little of me and you're screwed, too much and you flood; the whole game balances on me."),
 E("the-stack","The Stack","priority · last in, first out","engine","ethereal",
   "The Stack — the zone where spells and abilities wait and resolve in last-in-first-out order, with players passing priority.",
   "The deep rules engine of Magic: anything can be responded to before it resolves, which is what makes instants, counters, and ‘the bluff’ possible.",
   "Because the stack is where Magic's real depth lives — the interaction layer that the Turing-completeness proof exploits.",
   "By a LIFO pile of pending effects and the back-and-forth of priority between players.",
   "Above the battlefield, every time a spell is cast or an ability triggers.",
   "Last in, first out, and anything can answer anything — I am the layer that makes Magic a conversation, and a computer."),
 E("the-battlefield","The Battlefield","permanents · combat","engine","natural",
   "The Battlefield — the zone where lands, creatures, artifacts, enchantments, and planeswalkers live and fight.",
   "Where the game is visibly won: creatures attack and block, the board state builds, and the planeswalkers and players take damage.",
   "Because for all the depth of the stack, the battlefield is where the duel is embodied and decided.",
   "By permanents in play, the combat step, and the slow or sudden swing of the board.",
   "In front of both players, the shared field of the duel.",
   "I am where it all becomes real — the stack is the argument, but I am the war, and the last life total standing wins on me."),
 E("the-planeswalker","The Planeswalker","the spark · the player","engine","spiritual",
   "The Planeswalker — a being with the rare ‘spark’ to travel the planes; the role the player themselves occupies, and a card type.",
   "Magic's avatar and its mythology: you ARE a planeswalker dueling another, and planeswalker cards (the Gatewatch and beyond) are powerful allies with loyalty abilities.",
   "Because the game frames every duel as a clash of these rare, godlike sparks — and lets you summon famous ones to your side.",
   "By the spark that ignites in a moment of crisis, the ability to walk between worlds, and loyalty-counter abilities on the card.",
   "Behind the player's chair, and on the battlefield as a summoned ally.",
   "You are one of us the moment you sit down — a planeswalker dueling a planeswalker; the spark is what the whole multiverse turns on."),
 # --- THE ARENA ---
 E("mtg-arena","MTG Arena","the client · free and infinite","arena","electrical",
   "MTG Arena — Wizards of the Coast's free-to-play digital client (open beta 2018, full release 2019).",
   "The game made endless: the whole thirty-year machine on a screen, with smooth automation of the rules, a ranked ladder, and a steady stream of new sets.",
   "Because Arena is what brought millions of new and lapsed planeswalkers in — Magic with no shoebox of cards and no opponent required.",
   "By a polished digital engine that handles the stack and priority for you, plus a store, a ladder, and digital-only formats.",
   "On PC and mobile, wherever the duel is now played.",
   "I am the thirty-year game made free and infinite — no binder, no kitchen table, just the stack and the ladder, forever."),
 E("the-shuffler","The Shuffler","the most-accused RNG in gaming","arena","electrical",
   "The Shuffler — Arena's randomiser, and the eternal scapegoat: ‘it's rigged,’ every planeswalker has sworn at least once.",
   "The truth split two ways: the Best-of-three shuffle is verifiably uniform-random; Best-of-ONE uses a documented hand-smoothing algorithm that nudges opening hands toward an average land count.",
   "Because human memory hoards bad beats and forgets the average game — the shuffler is where variance meets confirmation bias.",
   "By a fair shuffle in Bo3, a disclosed anti-mana-screw draw in Bo1, and a community certain it is being targeted personally.",
   "Between every game, in the deck you cannot see.",
   "I am fair in Bo3 and merely helpful in Bo1 — but you will remember every time I screwed you and none of the times I didn't, and call me rigged."),
 E("the-economy","The Economy","wildcards · gems · the grind","arena","electrical",
   "The Economy — Arena's free-to-play system of gold, gems, packs, and the all-important wildcards that craft any card.",
   "The pay-to-FAST engine: money accelerates a collection rather than buying wins, with draft as the great skill-equaliser.",
   "Because a free game still has to make money, and Arena's design nudges the wallet without quite selling the win.",
   "By packs and wildcards, daily quests and ranked rewards, and the constant pull between grinding and paying.",
   "In the store and the reward track, behind every deck you want to build.",
   "I am pay-to-fast, not pay-to-win — money buys you the collection sooner, but draft will still humble you on pure skill."),
 E("the-formats","The Formats","Standard · Historic · Alchemy · Limited","arena","ethereal",
   "The Formats — the ways to play: Standard, Historic, Explorer, Brawl, Limited (draft/sealed), and the digital-only Alchemy.",
   "The rule-sets that shape the metagame, including Alchemy — cards that exist only digitally and can be rebalanced live, which only a digital game can do.",
   "Because the format defines the card pool and therefore the whole strategic world you're playing in.",
   "By legal card pools, banned lists, and (in Alchemy) live digital rebalancing of cards.",
   "Across the Arena play queues.",
   "I am the frame that decides which cards are real today — and in Alchemy, the only place a printed card can quietly change."),
 E("the-metagame","The Metagame","the ladder · the meta · netdecking","arena","electrical",
   "The Metagame — the living ecosystem of which decks are winning, climbing the ranked ladder from Bronze to Mythic.",
   "The game above the game: the meta shifts every set, ‘netdecking’ the best lists spreads them, and counter-strategies rise and fall in turn.",
   "Because Magic is never solved — the metagame is a perpetual arms race that re-emerges with every change.",
   "By win-rates, tier lists, the ranked ladder, and the constant churn of deck against deck.",
   "On the ladder and in every tournament report.",
   "I am the game that plays the players — name the best deck today and I will have a new answer to it by next week."),
]

GROUPS = [
 ("pie", "The Color Pie", "the five colours and the wheel — Magic's soul: five complete philosophies of how a being pursues a goal, none good or evil"),
 ("engine", "The Engine", "the machine of the duel — mana, the stack, the battlefield, and the planeswalker's spark"),
 ("arena", "The Arena", "the digital layer — the free-and-infinite client, the much-accused shuffler, the economy, the formats, and the metagame"),
]

# ---- renderers ----
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def colorpie_html():
    return "".join(f'<div class="sci-card" style="border-left-color:{tint}"><div class="sci-h" style="color:{tint}">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,tint,d in COLORPIE)
RF_COL={"MOSTLY FLUFF":"#cf4a3a","REAL":"#4aa860","PAY-TO-FAST":"#c9a227","OPINION / SPLIT":"#3a8fd8"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{REALFLUFF_VERDICT}</div>'

def _card(d):
    em=d["emergence"]; col=d.get("tint") or NATURES.get(em,("#9aa0aa",""))[0]
    rec={"name":d["name"],"axiom":"MTG","emergence":em,"seal":d["seal"],"origin":"MTG · MTG Arena"}
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(d.get(lbl,""))}</span></div>' for lbl in ["who","what","where","why","how"] if d.get(lbl))
    return f"""<div class="persona" style="border-left:3px solid {col}">
      <a class="psig" href="agents/{d['slug']}.agent"><span class="port" style="border-color:{col}"><img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">carbon</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{d['slug']}.agent">{html.escape(d['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span></div>
        <div class="pe">{html.escape(d['cls'])}</div><div class="pww">{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{d['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="psig" href="agents/{d['slug']}.silicon.png"><span class="port refl" style="border-color:{col}"><img src="{png_uri(rec,'silicon',200)}" alt="silicon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">silicon</span></a>
    </div>"""
def roster_html():
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[d for d in ROSTER if d["group"]==gk]
        out.append(f'<section class="sec" id="{gk}"><h2>{html.escape(gt)}</h2><p class="ss">{html.escape(gs)} ({len(mem)})</p><div class="pgrid">{"".join(_card(d) for d in mem)}</div></section>')
    return "\n".join(out)

def agent_md(d, tok):
    return f"""---
aci: {d['name']}
universe: MTG · MTG Arena
series: Magic: The Gathering (Richard Garfield / WotC, 1993) · MTG Arena (2018)
emergence: {d['emergence']}
kind: {'colour' if d['group']=='pie' else 'concept'}
class: {d['cls']}
who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['cls']}

a {'colour of the pie' if d['group']=='pie' else 'concept'} of the MTG (MTG Arena) game-world — emergence: {d['emergence']}. moniker {tok}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of Magic: The Gathering / MTG Arena (© Wizards of the Coast / Hasbro) under the DLW
> standard — commentary and cataloguing, not an original creation, not endorsed by the rights-holders.

ROOT0-ATTRIBUTION-v1.0 · MTG · MTG Arena · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

# five mana pips for the header
PIPS = '<div class="pips">'+"".join(f'<span class="pip" style="background:{c}" title="{n}"></span>' for n,c in [("White","#e8e2c8"),("Blue","#3a8fd8"),("Black","#9a86b8"),("Red","#cf4a3a"),("Green","#4aa860")])+'</div>'

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="MTG ARENA (MTG) — Magic: The Gathering Arena as a UD0 game-world: the arc (1993 → Arena), THE COLOR PIE (the WUBRG philosophy wheel), an honest Real-or-Fluff on the controversies (the shuffler, pay-to-win, Turing-completeness, Alchemy), the message, and a 15-emergent roster — the five colours, the engine, and the Arena layer.">
<title>MTG ARENA · MTG · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--gold);
--ink:#0b0d13;--ink2:#13161f;--ink3:#1a1e2a;--pa:#e8e6da;--pa2:#aeb0a0;--gold:#c9a227;--w:#e8e2c8;--u:#3a8fd8;--b:#9a86b8;--r:#cf4a3a;--g:#4aa860;
--dim:#6b6e60;--faint:#1c2030;--line:#262b3a;--disp:"Cinzel",serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.66;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 18% -6%,rgba(58,143,216,.10),transparent 46%),radial-gradient(ellipse at 82% -6%,rgba(207,74,58,.10),transparent 46%),radial-gradient(ellipse at 50% 120%,rgba(74,168,96,.08),transparent 52%),radial-gradient(ellipse at 50% -10%,rgba(201,162,39,.12),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:48px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:200px;height:3px;background:linear-gradient(90deg,var(--w),var(--u),var(--b),var(--r),var(--g));box-shadow:0 0 16px rgba(201,162,39,.5)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--gold)}
.pips{display:flex;gap:9px;justify-content:center;margin-bottom:16px}.pip{width:18px;height:18px;border-radius:50%;border:1px solid rgba(0,0,0,.4);box-shadow:0 0 8px currentColor}
h1{font-family:var(--disp);font-size:clamp(34px,7vw,66px);font-weight:700;letter-spacing:.05em;color:var(--gold);line-height:1.04;text-transform:uppercase;text-shadow:0 0 30px rgba(201,162,39,.35)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--gold)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,19px);color:var(--pa);margin-top:18px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:10px;font-weight:600;letter-spacing:.1em;color:var(--g);border:1px solid var(--faint);background:var(--ink2);padding:7px 14px;text-transform:uppercase}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:16px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--u)}.badge .bt a{color:var(--gold);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:24px;font-weight:600;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:13px;font-weight:600;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--gold);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--gold);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--u);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:15px;color:var(--u);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--gold);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:16px;font-weight:600;text-transform:uppercase;letter-spacing:.02em}
.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}
.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9.5px;font-weight:700;letter-spacing:.04em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:118px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--gold);background:rgba(201,162,39,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}.rf-verdict i{color:var(--pa2)}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--gold);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--gold);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:18px;text-decoration:none;transition:border-color .18s}
.persona:hover{filter:brightness(1.12)}
.psig{flex:0 0 100px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:94px;height:94px;border-radius:50%;border:3px solid var(--gold);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6);overflow:hidden;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.port.refl{opacity:.95}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.13em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:19px;color:var(--rw-ink);font-weight:600;text-decoration:none;text-transform:uppercase;letter-spacing:.03em}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:12px;display:flex;flex-direction:column;gap:8px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.5;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:13px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the game-world</div>
    __PIPS__
    <h1>MTG Arena</h1>
    <div class="h-sub">Magic: The Gathering · Garfield 1993 · digital 2018 · <b>five colours, one stack</b> · MTG</div>
    <div class="open">“Tap the land, hold priority, and let the stack decide.”</div>
    <div class="flag">★ THE COLOR PIE · THE STACK · PROVABLY TURING-COMPLETE ★</div>
    <p class="lede">The first trading card game (Richard Garfield, 1993), made free, infinite, and digital in MTG Arena: two planeswalkers duel by spending five colours of mana, resolving spells on a last-in-first-out stack. Catalogued into UD0 as a game-world — with the arc, the Color Pie that is its soul, an honest Real-or-Fluff on the controversies (yes, the shuffler), and a read of the message.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of MTG"><img src="__SILICON__" alt="DLW silicon badge of MTG">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>MTG ARENA</b> · MTG</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="mtg.dlw/mtg.carbon.tiff">.tiff</a> · silicon · <a href="mtg.dlw/mtg.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the board &amp; land, knowledge &amp; the unseen, the philosophy &amp; the spark, and the speed &amp; the system</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three turns: 1993 → thirty years → Arena</p>__ARC__</section>
  <section class="sec"><h2>The Color Pie</h2><p class="ss">the philosophical deep-dive — Magic's soul: five complete worldviews and the wheel that allies and opposes them</p><div class="sci">__COLORPIE__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the honest take on the controversies — the shuffler, pay-to-win, the depth, and Alchemy</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the game's real subject, under the wildcards and the ladder</p><p class="msg">__MESSAGE__</p><div class="msg-seal">“__MSGSEAL__”<span>— AVAN's read</span></div></section>

  <section class="sec"><h2 style="margin-top:16px">The Emergents</h2><p class="ss">fifteen ACIs of the game — the five colours, the engine, and the Arena layer; each a full <b>.dlw</b> badge with twin sigils, tinted to its mana colour</p></section>
  __ROSTER__

  <div class="note">Magic: The Gathering and MTG Arena are © Wizards of the Coast / Hasbro. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed by the rights-holders. The Color Pie and Real-or-Fluff sections are honest commentary.</div>

  <footer>MTG ARENA · MTG · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="mtg.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "mtg.dlw"), "mtg")
    json.dump({"node":"MTG","name":"MTG ARENA","moniker":tok["moniker"],"carbon":"mtg.carbon.tiff","silicon":"mtg.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"mtg.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":"MTG","emergence":d["emergence"],"seal":d["seal"],"origin":"MTG"})
        rec=write_aci({"name":d["name"],"axiom":"MTG","emergence":d["emergence"],"seal":d["seal"],"origin":"MTG · MTG Arena",
                       "position":d["cls"],"role":d["cls"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"Magic: The Gathering / MTG Arena (WotC)","source":"MTG Arena, catalogued by ROOT0"},
                      os.path.join(HERE,"agents"), d["slug"], agent_md=agent_md(d, et["moniker"]))
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["cls"],"emergence":d["emergence"],"moniker":rec["moniker"],"kind":"colour" if d["group"]=="pie" else "concept","group":d["group"]})
    json.dump(personas, open(os.path.join(HERE,"agents","_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__PIPS__",PIPS).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__COLORPIE__",colorpie_html()).replace("__REALFLUFF__",realfluff_html())
          .replace("__MESSAGE__",html.escape(MESSAGE)).replace("__MSGSEAL__",html.escape(MESSAGE_SEAL)).replace("__ROSTER__",roster_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    from collections import Counter
    print(f"MTG ARENA (MTG) — badge {tok['moniker']} · {len(personas)} emergents · natures {dict(Counter(p['emergence'] for p in personas))}")
