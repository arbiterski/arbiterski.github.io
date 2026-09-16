"""Build dependency-free, bilingual graphical research abstracts."""
from pathlib import Path
import html
from research_summaries import SUMMARIES
from research_funding import FUNDING
from research_infographics import render

ROOT = Path(__file__).resolve().parents[1]

PROJECTS = [
    {
        "slug": "brain-consciousness", "id": "01", "color": "#166c8c",
        "field": ["NEUROSCIENCE / EEG", "NEUROSCIENCE / EEG"],
        "title": ["從腦波，看見大腦的回應", "Making brain responses visible"],
        "subtitle": ["巨量腦波資料庫・動態腦狀態・意識與預後研究", "An EEG research program for consciousness and recovery"],
        "question": ["無法以動作回應，是否代表大腦沒有反應？", "When a patient cannot move, can the brain still respond?"],
        "summary": ["整合跨院腦波與追蹤資料，探索意識狀態與恢復的客觀線索。", "Connecting multicenter EEG and follow-up data to investigate consciousness and recovery."],
        "stages": [
            ["wave", ["量測腦波", "Record EEG"], ["任務指令 × 休息", "Task × rest"], ["比較接受動作指令與休息時的多通道腦波，保留事件標記並進行訊號品質處理。", "Compare multichannel EEG during movement instructions and rest, with event annotation and signal-quality processing."]],
            ["network", ["分析腦區連結", "Map connectivity"], ["wPLI / wSMI", "wPLI / wSMI"], ["以 wPLI 與 wSMI 分析相位同步與訊息共享，研究不同腦區之間的功能連結。", "Use wPLI and wSMI to study phase synchronization and information sharing between EEG channels."]],
            ["states", ["辨識動態腦狀態", "Identify brain states"], ["分群 × 加權熵", "Clustering × entropy"], ["以分群辨識重複出現的連結模式，再以腦狀態分布及加權熵描述其複雜程度。", "Identify recurring connectivity patterns through clustering; summarize state distributions and weighted entropy."]],
            ["followup", ["驗證臨床關聯", "Validate clinically"], ["意識評估 × 六個月預後", "Assessment × 6-month outcome"], ["比較腦波指標、臨床評估與六個月追蹤結果，檢驗跨病人與跨院的可重現性。", "Compare EEG measures with clinical assessments and six-month follow-up, examining reproducibility across patients and sites."]],
        ],
        "sections": [
            [["臨床問題", "Clinical question"], ["外在行為可能無法完整呈現腦損傷病人的腦部反應。我們希望增加可量化、可追蹤的評估線索。", "Behavior alone may not fully capture brain responses after injury. We investigate quantitative measures that can be followed over time."]],
            [["研究設計", "Study design"], ["建立整合腦波、臨床資料與長期追蹤的跨院資料庫，比較任務與休息條件下的連結及動態腦狀態。", "Build a multicenter database of EEG, clinical information, and longitudinal follow-up; compare connectivity and brain states under task and rest conditions."]],
            [["如何驗證", "Evaluation"], ["檢驗指標與臨床量表的關聯、六個月預後預測能力，以及即時與離線分析的一致性。", "Assess relationships with clinical scales, six-month outcome prediction, and agreement between real-time and offline analysis."]],
        ],
        "goal": ["走向可持續追蹤的床邊意識監測與決策支援。", "Toward longitudinal bedside monitoring and clinical decision support."],
        "boundary": ["研究階段｜方法學驗證與臨床決策支援開發。", "Research stage | Methodological validation and clinical decision-support development."],
        "sources": ["2026-06｜ICU 腦損傷病人意識監測及預後決策支援系統考評簡報", "2026｜動態腦電圖連結分析量化大腦意識之方法學驗證計畫", "Methods: Brain State Entropy Pipeline"],
    },
    {
        "slug": "ai-cancer-registry", "id": "02", "color": "#995238",
        "field": ["CLINICAL AI / ONCOLOGY", "CLINICAL AI / ONCOLOGY"],
        "title": ["讓每一筆癌登，都有據可查", "Cancer registration with traceable evidence"],
        "subtitle": ["個案發現・病歷擷取・人工審核・FHIR 交換", "Case finding, evidence extraction, human review, and FHIR"],
        "question": ["散落各處的病歷，如何成為可核對的癌症資料？", "How can scattered clinical records become verifiable cancer data?"],
        "summary": ["讓 AI 整理候選答案與證據，讓癌登人員保留最終判斷。", "AI organizes candidate answers and evidence; cancer registrars retain the final judgment."],
        "stages": [
            ["documents", ["整合病歷", "Gather records"], ["病理・影像・治療", "Pathology · imaging · treatment"], ["彙整病理、影像、手術與治療紀錄，處理文件格式、時間與來源差異。", "Bring together pathology, imaging, surgery, and treatment records, preserving source and time information."]],
            ["search", ["找個案、取欄位", "Find cases & fields"], ["個案篩選 ≠ 欄位擷取", "Case finding ≠ field extraction"], ["先找可能需要癌登的新發個案，再擷取欄位；特別處理否定、疑似、病史、家族史與原發／轉移關係。", "Identify potentially reportable new cases, then extract fields while handling negation, uncertainty, history, family history, and primary/metastatic relationships."]],
            ["review", ["規則與人工核對", "Review evidence"], ["候選值 + 原文 + 標準碼", "Value + source + code"], ["呈現候選值與來源證據，依癌別、時間及編碼版本檢核，由癌登人員接受、修改或退回。", "Present candidate values and source evidence; apply cancer-specific and version-specific rules before registrar review."]],
            ["exchange", ["標準化交換", "Exchange with FHIR"], ["結構・語意・驗證", "Structure · meaning · validation"], ["發展癌登 FHIR 實作指引及轉換工具，保留個案、原發癌、分期與治療的正確關聯。", "Develop cancer-registry FHIR implementation guidance and conversion tools that preserve links among patients, primary cancers, staging, and treatment."]],
        ],
        "sections": [
            [["臨床問題", "Clinical question"], ["癌登資訊分散於多種文件，且同一欄位可能存在互相衝突的記載。找得到資料，還必須判斷何者適用。", "Information is scattered across documents and may conflict. Finding a value is only the beginning; its context and applicability matter."]],
            [["研究設計", "Study design"], ["將大型語言模型、標準編碼與規則檢核串接，建立「AI 擷取—人工審核—回饋改進」的工作流程。", "Combine language models, standard codes, and rule checks in an extraction–review–feedback workflow."]],
            [["如何驗證", "Evaluation"], ["分別評估個案漏案率、欄位正確性、來源追溯、人工修改率與處理時間，而非只報單一準確率。", "Evaluate case detection, field accuracy, evidence traceability, correction rates, and processing time separately."]],
        ],
        "goal": ["少一點資料搬運，多一點專業判斷。", "Less manual data transfer. More professional judgment."],
        "boundary": ["研究階段｜欄位擷取、跨院介接與人工審核流程持續驗證中。", "Research stage | Ongoing evaluation of field extraction, cross-site integration, and human review."],
        "sources": ["2026-09｜以人工智慧輔助程式導入癌症登記辦理現況", "2026-09-01｜AI 癌登計畫一小時辦理現況報告 v6"],
    },
    {
        "slug": "hai-surveillance", "id": "03", "color": "#226a59",
        "field": ["PATIENT SAFETY / INFECTION", "PATIENT SAFETY / INFECTION"],
        "title": ["從病歷訊號，找到感染線索", "From clinical signals to infection evidence"],
        "subtitle": ["醫療照護相關感染自動化監測與信效度驗證", "Automated healthcare-associated infection surveillance"],
        "question": ["如何讓感染管制人員，更快找到需要確認的個案？", "How can infection-control teams find cases that need review sooner?"],
        "summary": ["結合規則與院內 AI，整理血流感染及泌尿道感染的判讀證據。", "Combine rules and on-premise AI to organize evidence for bloodstream and urinary tract infection surveillance."],
        "stages": [
            ["signals", ["整合院內資料", "Integrate data"], ["培養・用藥・導管・紀錄", "Cultures · drugs · devices · notes"], ["整合微生物培養、檢驗、生命徵象、用藥、導管留置與臨床文字紀錄。", "Integrate microbiology, laboratory results, vital signs, medications, device timing, and clinical notes."]],
            ["filter", ["第一階段：篩選", "Stage 1: screen"], ["規則分流候選個案", "Rule-based case triage"], ["利用規則引擎篩選需進一步判讀的個案，集中後續分析與人工審查的資源。", "Use rules to identify cases requiring further assessment and focus downstream analysis and review."]],
            ["review", ["第二階段：判讀", "Stage 2: assess"], ["院內 LLM + 監測定義", "Local LLM + surveillance rules"], ["院內模型擷取文字中的線索，再依監測定義檢查感染時間窗、污染菌及重複事件等條件。", "Extract evidence from text locally, then apply surveillance criteria including timing, contaminants, and duplicate-event handling."]],
            ["compare", ["人工確認與驗證", "Confirm & validate"], ["專業審閱 × 誤差分析", "Expert review × error analysis"], ["由感染管制人員確認；研究設計另將自動結果與人工監測比對，分析不一致的原因。", "Infection-control professionals confirm cases; validation compares automated and manual surveillance and investigates disagreements."]],
        ],
        "sections": [
            [["臨床問題", "Clinical question"], ["感染判讀仰賴跨系統、跨時間的資料比對。重複查閱負擔與判讀差異，使自動化輔助具有研究價值。", "Surveillance requires information across systems and time. Repetitive review and variation in interpretation motivate automation research."]],
            [["研究設計", "Study design"], ["以血流感染及泌尿道感染為起點，採兩階段架構、院內運算與可追溯證據，並規劃回溯性病歷驗證。", "Start with bloodstream and urinary tract infections, using two-stage processing, on-premise computation, traceable evidence, and planned retrospective validation."]],
            [["如何驗證", "Evaluation"], ["評估敏感度、特異度、陽性預測值、人工判讀一致性與工時；區分資料缺失、規則與文字擷取造成的誤差。", "Measure sensitivity, specificity, predictive value, agreement, and review time; distinguish data, rule, and text-extraction errors."]],
        ],
        "goal": ["讓感染監測更一致，也讓每個判讀可被追溯。", "More consistent surveillance, with evidence behind each assessment."],
        "boundary": ["研究階段｜監測流程開發與回溯性信效度驗證規劃。", "Research stage | Surveillance workflow development and planned retrospective validation."],
        "sources": ["2026｜HAI 自動化監測機制服務建議書 v7.2", "2026-08-13｜HAI 自動化監測信效度驗證研究計畫 v1"],
    },
    {
        "slug": "loinc-mapping", "id": "04", "color": "#68569a",
        "field": ["HEALTH DATA / INTEROPERABILITY", "HEALTH DATA / INTEROPERABILITY"],
        "title": ["讓檢驗資料，說同一種語言", "A shared language for laboratory data"],
        "subtitle": ["LOINC 對應・AI 輔助審閱・跨院語意互通", "LOINC mapping, AI-assisted review, and semantic interoperability"],
        "question": ["名稱看起來相同的檢驗，真的測量同一件事嗎？", "Do similarly named tests actually measure the same thing?"],
        "summary": ["從院內代碼到標準語意，讓資料交換保留正確的臨床意義。", "From local codes to shared semantics: preserving clinical meaning during data exchange."],
        "stages": [
            ["local", ["盤點院內檢驗", "Inventory local tests"], ["名稱・代碼・檢體・單位", "Names · codes · specimens · units"], ["蒐集院內代碼、檢驗名稱、檢體、單位與方法等資訊，先釐清資料實際代表的測量。", "Collect local codes, names, specimens, units, and methods to clarify what each test actually measures."]],
            ["axes", ["拆解測量語意", "Resolve meaning"], ["成分・性質・時間等維度", "Component · property · timing…"], ["核對成分、測量性質、時間、檢體／系統、尺度與方法；相近名稱不必然代表相同概念。", "Check component, property, timing, system/specimen, scale, and method. Similar names do not guarantee equivalent concepts."]],
            ["search", ["AI 推薦、人工審閱", "Suggest & review"], ["候選碼 × 疑義檢查", "Candidate codes × quality checks"], ["以智慧搜尋與 AI 提出候選 LOINC 代碼，配合疑義檢查與專業人員逐項審閱。", "Use search and AI to suggest candidate LOINC codes, supported by quality checks and expert review."]],
            ["exchange", ["版本化對應與交換", "Govern & exchange"], ["LOINC × FHIR", "LOINC × FHIR"], ["維護可追溯、可更新的對應表，支援 FHIR 資料交換與跨院研究，而不只轉換檔案格式。", "Maintain traceable, versioned mappings to support FHIR exchange and cross-site research, beyond file-format conversion."]],
        ],
        "sections": [
            [["資料問題", "Data challenge"], ["院內命名與代碼不一致，容易讓不同測量被混用。語意對應必須理解檢驗情境，不能只比文字。", "Local naming and coding vary. Mapping must capture measurement context rather than matching words alone."]],
            [["研究設計", "Study design"], ["以萬芳與三軍總醫院的常用檢驗對應經驗為基礎，結合候選推薦、疑義檢查、人工審閱與版本管理。", "Build on routine-test mapping experience at Wan Fang and Tri-Service General Hospitals, combining suggestions, discrepancy checks, expert review, and version control."]],
            [["品質重點", "Quality focus"], ["檢查檢體、測量性質與方法的差異，保留審閱依據；並將對應經驗延伸到培養與藥敏資料整合。", "Check specimen, property, and method differences, retain review rationale, and extend mapping experience to culture and susceptibility data."]],
        ],
        "goal": ["資料能交換，更要讓意義不失真。", "Exchange the data. Preserve the meaning."],
        "boundary": ["研究重點｜專業審閱、語意品質與對應版本治理。", "Research focus | Expert review, semantic quality, and mapping version governance."],
        "sources": ["2026｜HAI 服務建議書 v7.2：LOINC 對應治理與資料介接章節", "2026｜英國倫敦演講研究資料：LOINC 標準化研究"],
    },
]

def esc(s):
    return html.escape(s, quote=True)

def bi(pair, tag="span", cls=""):
    return f'<{tag} class="{cls}" data-zh="{esc(pair[0])}" data-en="{esc(pair[1])}">{esc(pair[0])}</{tag}>'

ICONS = {
    "wave": '<rect x="19" y="20" width="125" height="82" rx="12"/><path fill="none" d="M22 69h23l8-20 13 46 12-70 13 57 10-22h36"/><path d="M32 116h98M70 102v14m20-14v14"/>',
    "network": '<path d="m40 42 46-17 39 28-13 51-62 10-26-37 16-35m0 0 72 62M86 25 50 114m-26-37 101-24M40 42l45 37 27 25m-27-25 1-54m-1 54-35 35"/><circle cx="40" cy="42" r="7"/><circle cx="86" cy="25" r="7"/><circle cx="125" cy="53" r="7"/><circle cx="112" cy="104" r="7"/><circle cx="50" cy="114" r="7"/><circle cx="24" cy="77" r="7"/><circle cx="85" cy="79" r="10"/>',
    "states": '<path d="M25 106h112M26 107V28"/><rect x="42" y="63" width="14" height="42" rx="3"/><rect x="65" y="37" width="14" height="68" rx="3"/><rect x="88" y="76" width="14" height="29" rx="3"/><rect x="111" y="51" width="14" height="54" rx="3"/><path d="m38 39 20-12 22 6 24-13 22 9"/>',
    "followup": '<rect x="31" y="23" width="96" height="93" rx="10"/><path d="M31 47h96M53 16v17m53-17v17M47 96l17-23 17 10 29-23"/><circle cx="110" cy="60" r="5"/>',
    "documents": '<rect x="26" y="18" width="75" height="90" rx="8"/><rect x="46" y="37" width="80" height="87" rx="8"/><path d="M61 60h47M61 75h47M61 90h31M61 105h40"/>',
    "search": '<rect x="25" y="19" width="85" height="104" rx="9"/><path d="M41 39h48M41 52h32M41 97h17"/><circle cx="91" cy="78" r="25"/><path d="m109 97 26 25m-56-45 9 9 16-19"/>',
    "review": '<rect x="26" y="25" width="96" height="96" rx="9"/><rect x="55" y="16" width="40" height="18" rx="5"/><path d="m42 56 5 5 9-12M66 57h38m-62 25 5 5 9-12M66 83h38M42 104h62"/>',
    "exchange": '<rect x="17" y="24" width="47" height="38" rx="8"/><rect x="94" y="79" width="47" height="38" rx="8"/><path d="M65 42h52v25m-8-8 8 8 8-8M94 98H41V73m-8 8 8-8 8 8M28 37h25M28 49h17M105 92h25M105 104h17"/>',
    "signals": '<path d="M42 20v23c-25 16-25 49 0 61 26 12 49-5 44-28-2-11-13-20-23-26V20M36 20h32M28 76h54M99 37h32M99 53h32m-32 28h10l7-15 7 31 7-15h11"/><circle cx="47" cy="85" r="4"/>',
    "filter": '<path d="M21 27h119L96 75v37l-32 13V75Z"/><circle cx="48" cy="15" r="4"/><circle cx="80" cy="15" r="4"/><circle cx="111" cy="15" r="4"/><path d="M45 47h70"/>',
    "compare": '<rect x="18" y="31" width="54" height="78" rx="7"/><rect x="91" y="31" width="54" height="78" rx="7"/><path d="M30 49h28M30 63h28m-28 21 7 8 19-20m47-23h28m-28 14h28m-28 21 7 8 19-20M74 20h15m-15 98h15"/>',
    "local": '<rect x="19" y="26" width="121" height="89" rx="8"/><path d="M19 50h121M62 50v65M30 66h20M75 66h51M30 85h20M75 85h30M30 101h20M75 101h44"/>',
    "axes": '<circle cx="80" cy="70" r="22"/><path d="M80 18v30m0 44v31m-49-81 30 17m38 22 30 17M31 98l30-17m38-22 30-17"/><circle cx="80" cy="18" r="7"/><circle cx="80" cy="123" r="7"/><circle cx="31" cy="42" r="7"/><circle cx="31" cy="98" r="7"/><circle cx="129" cy="42" r="7"/><circle cx="129" cy="98" r="7"/>',
}

def icon(name):
    return f'<svg viewBox="0 0 160 140" aria-hidden="true" focusable="false"><g fill="var(--paper)" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g></svg>'

def head(title, depth="../"):
    return f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | Ming-Chin Lin Research</title>
<meta name="description" content="林明錦研究計畫圖解：大腦意識、AI 癌症登記、HAI 感染監測與 LOINC 對應。Bilingual graphical research abstracts.">
<link rel="stylesheet" href="{depth}assets/research.css"><script defer src="{depth}assets/research.js"></script></head><body>
<a class="skip" href="#main">Skip to content / 跳至內容</a>
<header class="site-header"><a class="brand" href="{depth}../../" aria-label="Ming-Chin Lin home">MING-CHIN LIN <span>RESEARCH NOTES</span></a>
<div class="tools"><button id="language" type="button" aria-label="Switch to English">English</button><button class="print" type="button" data-zh="列印 / PDF" data-en="Print / PDF">列印 / PDF</button></div></header>'''

def footer(depth):
    return f'''<footer><a href="{depth}">{bi(["← 所有研究計畫", "← All research projects"])}</a><span>Ming-Chin Lin, MD, PhD · 2026</span></footer></body></html>'''

def build_project(p):
    directory = ROOT/'research'/p['slug']
    directory.mkdir(parents=True, exist_ok=True)
    render(p['slug'], ROOT/'research/assets/infographics')
    paragraphs = ''.join(bi(pair, 'p') for pair in zip(*SUMMARIES[p['slug']]))
    image_path = '../assets/infographics/' + p['slug']
    funding = FUNDING[p['slug']]
    out = head(p['title'][0]) + f'''<main id="main" class="research-content" style="--accent:{p['color']}">
<a class="back" href="../../">{bi(["← 個人首頁", "← Biography"])}</a>
<article>
<header class="content-heading">{bi(p['title'], 'h1')}{bi(["研究摘要 / Abstract", "Abstract"], 'p', 'abstract-label')}</header>
<div class="summary-copy">{paragraphs}</div>
<aside class="funding"><strong>{bi(["經費來源 / Funding source", "Funding source"])}</strong>{bi(funding['label'], 'p', 'funding-name')}{bi(funding['note'], 'p', 'funding-note')}</aside>
<figure class="infographic">
<figcaption>{bi(["研究圖解", "Research infographic (Traditional Chinese)"])}<a href="{image_path}.svg" target="_blank" rel="noopener">{bi(["放大檢視 ↗", "View full size ↗"])}</a></figcaption>
<a href="{image_path}.svg" target="_blank" rel="noopener" aria-label="放大研究資訊圖 / Enlarge infographic"><img src="{image_path}.svg" width="1920" height="1080" alt="{esc(p['title'][0])}：研究方向、方法學、目前進展與成果、預期用途；各項成果標示研究狀態。"></a>
<div class="image-downloads"><a href="{image_path}.svg" download>{bi(["下載向量圖 SVG", "Download SVG"])}</a></div>
</figure>
<p class="source-note">{bi(["內容依據：", "Source documents: "])}{esc('；'.join(p['sources']))}</p>
</article></main>''' + footer('../../')
    out = out.replace('href="../../../"', 'href="../../"').replace('← 所有研究計畫', '← 個人首頁').replace('← All research projects', '← Biography')
    (directory/'index.html').write_text(out)
    # Preserve old preview links while keeping a single canonical content page.
    (directory/'summary.html').write_text('''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><title>研究內容</title><script>location.replace('./' + location.search + location.hash)</script></head><body><a href="./">前往研究內容 / Read the research</a></body></html>''')

def build_index():
    overview_title = ["從臨床問題，\n走向可用的醫療 AI。", "From clinical questions\nto useful medical AI."]
    rows = ''.join(f'''<a class="research-row" href="{p['slug']}/" style="--accent:{p['color']}"><span class="row-number">{p['id']}</span>
<div class="row-icon">{icon(p['stages'][1][0])}</div><div>{bi(p['title'], 'h2')}{bi(p['summary'], 'p')}</div><span class="row-arrow" aria-hidden="true">↗</span></a>''' for p in PROJECTS)
    out = head('研究計畫圖解', '') + f'''<main id="main" class="overview"><div class="eyebrow">MEDICAL INFORMATICS × CLINICAL AI</div>
{bi(overview_title, 'h1')}
{bi(["四個研究方向，一個共同起點：讓資料有意義，讓判斷有依據。", "Four research directions. One shared foundation: meaningful data and evidence-based judgment."], 'p', 'intro')}
<div class="research-list">{rows}</div>
<div class="overview-note">{bi(["每項研究先以文字摘要說明，再呈現研究資訊圖；可切換中英文摘要。", "Read each abstract first, then explore the infographic. Abstracts are available in Chinese and English."], 'p')}</div></main>''' + footer('../')
    out = out.replace('href="../../"', 'href="../"').replace('← 所有研究計畫', '← 個人首頁').replace('← All research projects', '← Personal homepage')
    (ROOT/'research/index.html').write_text(out)

if __name__ == '__main__':
    for project in PROJECTS:
        build_project(project)
    build_index()
