"""Drafted with Claude Code Fable 5.1 from reviewed research materials; editorially checked."""

SUMMARIES = {'brain-consciousness': [['腦損傷後，有些病人無法以動作或言語回應，但這不一定代表大腦沒有反應。臨床評估多倚賴外在行為，可能漏掉部分訊號。我們想知道，腦波能否提供可量化、可追蹤的線索，補充床邊評估。',
                          '研究團隊整合跨院腦波、臨床評估與長期追蹤資料，建立大型資料庫，同時保留事件標記與訊號品質資訊，供後續分析使用。分析上，比較病人接受動作指令與休息時的多通道腦波，計算腦區之間的功能連結，再辨識重複出現的連結模式，描述腦狀態的動態變化與複雜程度。',
                          '目前重點在方法學驗證：檢視這些指標與意識評估量表的關聯、對六個月預後的預測能力，以及即時與離線分析是否一致，並確認結果能否跨病人、跨院重現。腦波指標不會直接判定意識，長期目標是成為可持續追蹤的床邊監測與臨床決策的輔助依據。'],
                         ['After brain injury, some patients cannot respond through movement or '
                          'speech, yet this does not necessarily mean the brain is unresponsive. '
                          'Clinical assessment relies largely on observable behavior and may '
                          'miss part of the picture. We ask whether EEG can offer quantifiable, '
                          'trackable clues that complement bedside evaluation.',
                          'The team is building a large multicenter database that integrates '
                          'EEG, clinical assessments, and long-term follow-up, while preserving '
                          'event annotations and signal-quality information for later analysis. '
                          'Analytically, we compare multichannel EEG recorded during movement '
                          'instructions and at rest, estimate functional connectivity between '
                          'brain regions, identify recurring connectivity patterns, and describe '
                          'the dynamics and complexity of brain states.',
                          'The current focus is methodological validation: examining how these '
                          'measures relate to consciousness assessment scales, whether they '
                          'predict six-month outcome, whether real-time and offline analyses '
                          'agree, and whether results reproduce across patients and sites. EEG '
                          'measures will not determine consciousness on their own. The long-term '
                          'aim is to support longitudinal bedside monitoring and clinical '
                          'decision-making.']],
 'ai-cancer-registry': [['一位癌症病人的登記資料，往往散落在病理報告、影像報告、手術與治療紀錄之中，同一個欄位還可能出現前後不一致的記載。癌登人員必須逐份翻閱、比對日期與來源，才能決定哪一筆才適用。這項工作耗時，整理可供核對的依據也需要人力。',
                         '我們以院內病歷為資料來源，先找出可能需要登記的新發個案，再擷取各欄位。大型語言模型負責提出候選值，並標示原文出處，同時處理否定、疑似、既往病史、家族史與原發或轉移的關係。系統再依癌別、時間與編碼版本進行規則檢核，最後由癌登人員接受、修改或退回。',
                         '驗證上，我們分別檢視個案漏案、欄位正確性、來源可追溯程度、人工修改比例與處理時間，而不是只看單一準確率。另一方面，團隊也在發展癌登資料的標準化交換格式與轉換工具，讓個案、原發癌、分期與治療之間的關聯在跨院傳遞時仍然正確。目標是減少資料搬運，把時間留給專業判斷。'],
                        ['The registry information for a single cancer patient is often '
                         'scattered across pathology reports, imaging reports, and surgical and '
                         'treatment records, and the same field may carry conflicting entries. '
                         'Registrars must read each document, compare dates and sources, and '
                         'decide which value applies. The work is time-consuming, and organizing '
                         'evidence for later review also requires staff effort.',
                         'Using in-hospital clinical records as the source, we first identify '
                         'newly diagnosed cases that may require registration, then extract '
                         'individual fields. A large language model proposes candidate values '
                         'and marks where each one appears in the original text, while handling '
                         'negation, uncertainty, past medical history, family history, and '
                         'primary versus metastatic relationships. The system then applies rule '
                         'checks by cancer type, timing, and coding version, and registrars '
                         'accept, revise, or reject each result.',
                         'For evaluation, we separately examine missed cases, field accuracy, '
                         'evidence traceability, correction rates, and processing time, rather '
                         'than reporting a single accuracy figure. In parallel, the team is '
                         'developing standardized exchange formats and conversion tools for '
                         'registry data so that the links among patients, primary cancers, '
                         'staging, and treatment remain correct when data move between '
                         'institutions. The goal is less manual data transfer and more time for '
                         'professional judgment.']],
 'hai-surveillance': [['判斷一位住院病人是否發生醫療照護相關感染，需要把培養結果、檢驗數值、生命徵象、用藥與導管留置時間放在一起看，還要對照臨床紀錄。這些資料分散在不同系統與時間點，感染管制人員得反覆查閱，不同人的判讀也可能有差異。',
                       '我們從血流感染與泌尿道感染開始，設計兩階段流程。第一階段以規則引擎整合院內資料，篩出需要進一步判讀的候選個案；第二階段由院內部署的語言模型擷取文字紀錄中的線索，再依監測定義檢查感染時間窗、污染菌與重複事件等條件。流程設計採院內運算，並為每個判讀保留來源證據。',
                       '系統的角色是輔助，最終仍由感染管制人員確認。驗證研究規劃以回溯性病歷比對自動結果與人工監測，評估敏感度、特異度、陽性預測值、判讀一致性與工時，並區分資料缺失、規則設定與文字擷取各自造成的誤差。期望讓監測更一致，也讓每個判讀可以被追溯。'],
                      ['Deciding whether a hospitalized patient has developed a '
                       'healthcare-associated infection means viewing culture results, '
                       'laboratory values, vital signs, medications, and device placement timing '
                       'together, and checking them against clinical notes. These data sit in '
                       'different systems and at different time points, so infection-control '
                       'staff must review them repeatedly, and interpretations can vary between '
                       'reviewers.',
                       'We begin with bloodstream and urinary tract infections and use a '
                       'two-stage workflow. In the first stage, a rule engine integrates '
                       'in-hospital data and screens candidate cases that need further '
                       'assessment. In the second stage, a language model deployed inside the '
                       'hospital extracts clues from free-text notes, after which surveillance '
                       'definitions are applied to check infection time windows, common '
                       'contaminants, and duplicate events. The workflow is designed for '
                       'on-premise computation and retention of source evidence for each '
                       'assessment.',
                       'The system plays a supporting role; infection-control professionals make '
                       'the final confirmation. The planned validation study compares automated '
                       'results against manual surveillance using retrospective records, '
                       'measuring sensitivity, specificity, positive predictive value, '
                       'inter-rater agreement, and review time, and separating errors caused by '
                       'missing data, rule settings, and text extraction. The aim is more '
                       'consistent surveillance in which each assessment can be traced.']],
 'loinc-mapping': [['檢驗項目的名稱看起來相同，不一定測量同一件事。同樣叫血糖的檢驗，在不同醫院可能使用血漿或全血檢體，測量方法與單位也未必相同。院內代碼與命名各自為政，資料一旦跨院交換或用於研究，這些差異若未被辨認，不同的測量就會被混在一起。',
                    '我們以萬芳醫院與三軍總醫院常用檢驗的人工對應經驗為基礎，發展對應到 LOINC '
                    '國際檢驗標準碼的語意治理方式。做法是先盤點院內代碼、名稱、檢體、單位與方法，再逐一核對成分、測量性質、時間、檢體系統、尺度與方法等維度，把每個檢驗實際代表的測量釐清，而不是只比對文字。',
                    '在這個基礎上，團隊正在發展以搜尋與人工智慧提出候選標準代碼的輔助方式，搭配疑義檢查，由專業人員逐項審閱並保留審閱依據。對應表以版本管理維護，可追溯、可更新，用來支援標準化資料交換與跨院研究；後續也規劃將經驗延伸到培養與藥敏資料的整合。'],
                   ['Laboratory tests with similar names do not necessarily measure the same '
                    'thing. A test labeled blood glucose may be run on plasma at one hospital '
                    'and whole blood at another, with different methods and units. Local codes '
                    'and naming conventions vary from site to site, and once data are exchanged '
                    'across hospitals or used for research, unrecognized differences cause '
                    'distinct measurements to be mixed together.',
                    'Building on hands-on experience mapping routine tests at Wan Fang Hospital '
                    'and Tri-Service General Hospital, we are developing a semantic governance '
                    'approach for mapping local tests to LOINC, the international standard for '
                    'laboratory codes. The work starts with an inventory of local codes, names, '
                    'specimens, units, and methods, then checks each test along the dimensions '
                    'of component, property, timing, system or specimen, scale, and method, '
                    'clarifying what each test actually measures rather than matching text '
                    'alone.',
                    'On this foundation, the team is developing search- and AI-based assistance '
                    'that proposes candidate standard codes, paired with discrepancy checks, '
                    'with domain experts reviewing each item and recording the rationale for '
                    'their decisions. Mapping tables are maintained under version control so '
                    'they remain traceable and updatable, supporting standardized data exchange '
                    'and cross-site research. We also plan to extend this experience to the '
                    'integration of culture and antimicrobial susceptibility data.']]}
