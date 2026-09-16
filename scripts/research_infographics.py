"""Generate editable 1920×1080 research infographics without rasterized text."""
from html import escape
from research_funding import FUNDING

NAVY = '#1B3A5C'
COLORS = ['#2BAA9E', '#3B7DD8', '#7B5EA7', '#4CAF7D']
DATA = {
    'brain-consciousness': {
        'title': '從腦波，看見大腦的回應',
        'subtitle': '大腦意識與巨量腦波研究 ｜ 以客觀訊號補充臨床評估',
        'kpis': [('量測條件', '2 種', '任務指令與休息'), ('連結指標', '2 類', '相位同步與訊息共享'), ('預後追蹤', '6 個月', '與臨床恢復情形比對'), ('資料合作', '跨院整合', '腦波、量表與追蹤'), ('品質重點', '一致性', '即時與離線分析驗證')],
        'stages': [
            ('整合腦波資料', '跨院資料與訊號品質', ['蒐集多通道腦波', '保留任務事件標記', '整合臨床評估量表', '檢查雜訊與品質']),
            ('分析腦區連結', 'wPLI 同步性 × wSMI 訊息共享', ['比較任務與休息', '計算相位同步指標', '估計腦區訊息共享', '建立動態連結矩陣']),
            ('辨識動態腦狀態', '分群分析 × 加權熵', ['辨識重複連結模式', '計算腦狀態分布', '分析加權熵變化', '比較不同反應條件']),
            ('驗證臨床關聯', '量表與預後交叉比對', ['比對意識評估量表', '追蹤六個月預後', '檢驗跨院可重現性', '核對即時離線結果']),
        ],
        'results': [('跨院腦波資料', '已有基礎', '整合腦波與臨床資料', '串聯長期預後追蹤'), ('腦狀態分析流程', '方法產出', '連結分析與分群方法', '以加權熵描述動態變化'), ('意識與預後關聯', '驗證中', '比對意識評估量表', '檢驗六個月預後關聯'), ('床邊監測應用', '研究方向', '比較即時與離線分析', '評估臨床使用可行性')],
        'benefits': [('客觀線索', '補充行為評估'), ('持續追蹤', '掌握腦波變化'), ('資料整合', '串聯跨院研究'), ('方法驗證', '檢查可重現性'), ('決策支援', '提供評估依據')],
        'vision': ['讓腦部反應可量化', '讓恢復歷程可追蹤'],
    },
    'ai-cancer-registry': {
        'title': '讓每一筆癌登，都有據可查',
        'subtitle': 'AI 癌症登記研究 ｜ 讓 AI 整理資料，讓專業人員做判斷',
        'kpis': [('核心任務', '2 類', '個案發現與欄位擷取'), ('病歷來源', '多類文件', '病理、影像與治療'), ('答案依據', '原文追溯', '保留來源與時間'), ('審核機制', '人工確認', '接受、修改或退回'), ('交換標準', 'FHIR', '保留癌登資料關聯')],
        'stages': [
            ('彙整臨床病歷', '整合分散的癌症資訊', ['蒐集病理影像報告', '整合手術治療紀錄', '保留文件日期來源', '核對前後記載差異']),
            ('找個案與取欄位', '語言模型整理候選答案', ['篩選新發癌症個案', '擷取癌登所需欄位', '辨識疑似與既往史', '區分原發癌與轉移']),
            ('規則與人工審核', '每個候選值都有依據', ['顯示原文與來源', '檢查編碼與時間', '由癌登人員確認', '記錄修正與回饋']),
            ('交換與成效驗證', 'FHIR 資料交換 × 成效評估', ['建立標準交換格式', '保留癌症治療關聯', '檢視漏案欄位錯誤', '衡量修改比例工時']),
        ],
        'results': [('AI 癌登原型', '已有基礎', '發展病歷欄位擷取', '串接人工審核流程'), ('標準化資料交換', '開發中', '發展癌登 FHIR 指引', '建置格式轉換工具'), ('跨院病歷介接', '驗證中', '核對不同院所資料', '整理人工修正回饋'), ('成效評估', '待驗證', '分別檢視漏案與錯誤', '衡量人工修改與工時')],
        'benefits': [('減少搬運', '輔助資料整理'), ('證據可查', '連回原始病歷'), ('專業把關', '保留人工判斷'), ('標準交換', '串接不同系統'), ('品質改善', '以錯誤回饋優化')],
        'vision': ['讓癌症資料更可靠', '讓專業判斷更聚焦'],
    },
    'hai-surveillance': {
        'title': '從病歷訊號，找到感染線索',
        'subtitle': '醫療照護相關感染監測 ｜ 以可追溯證據輔助感染管制',
        'kpis': [('起始範圍', '2 類感染', '血流感染與泌尿道感染'), ('系統架構', '2 階段', '規則篩選與模型判讀'), ('運算設計', '院內部署', '整合院內臨床資訊'), ('確認機制', '專業審閱', '由感染管制人員確認'), ('驗證設計', '回溯比對', '自動結果與人工監測')],
        'stages': [
            ('整合感染線索', '串聯資料與發生時間', ['蒐集培養檢驗結果', '整合用藥生命徵象', '核對導管留置時間', '彙整臨床文字紀錄']),
            ('規則篩選個案', '第一階段聚焦審查範圍', ['建立候選篩選規則', '整理跨系統時間軸', '標記需判讀個案', '保留篩選依據']),
            ('模型輔助判讀', '第二階段核對監測定義', ['擷取紀錄中的線索', '檢查感染時間窗', '處理污染菌與重複', '附上來源證據']),
            ('人工確認與驗證', '回溯比對 × 信效度分析', ['由感染管制員審查', '比對人工監測結果', '敏感度與陽性預測值', '分析誤判與審查工時']),
        ],
        'results': [('兩階段監測架構', '設計產出', '規則篩選搭配語言模型', '以血流與泌尿道感染起步'), ('判讀依據整理', '方法設計', '串聯時間窗與臨床線索', '提供人工查核的來源證據'), ('回溯驗證研究', '計畫已擬', '規劃與人工監測比對', '尚待完成信效度驗證'), ('監測效能與工時', '待驗證', '衡量敏感度與特異度', '分析誤判原因與審查時間')],
        'benefits': [('集中線索', '減少反覆查閱'), ('一致判讀', '依循監測定義'), ('證據追溯', '查核每項依據'), ('工時評估', '衡量審查負擔'), ('持續改善', '定位誤判原因')],
        'vision': ['讓感染監測更一致', '讓每次判讀有依據'],
    },
    'loinc-mapping': {
        'title': '讓檢驗資料，說同一種語言',
        'subtitle': 'LOINC 對應與語意治理 ｜ 讓跨院資料交換保留臨床意義',
        'kpis': [('對應基礎', '2 院經驗', '萬芳與三軍總醫院'), ('語意核對', '6 維度', '釐清每項測量意義'), ('推薦方式', 'AI 輔助', '搜尋與候選代碼'), ('品質把關', '專家審閱', '逐項處理對應疑義'), ('維護機制', '版本管理', '記錄更新與審閱依據')],
        'stages': [
            ('盤點院內檢驗', '從地方代碼釐清測量', ['整理檢驗名稱代碼', '蒐集檢體與單位', '確認測量方法', '辨識資料缺漏']),
            ('拆解測量語意', '依六個維度核對概念', ['核對成分與性質', '確認時間與檢體', '辨識尺度與方法', '釐清近似名稱差異']),
            ('推薦與專家審閱', 'AI 提出候選並保留疑義', ['搜尋候選標準碼', '以 AI 輔助推薦', '標記疑義與差異', '由專業人員逐項審閱']),
            ('治理與資料交換', '建立可維護的對應關係', ['保存審閱理由', '維護對應表版本', '支援標準資料交換', '延伸培養藥敏整合']),
        ],
        'results': [('兩院檢驗對應', '已有經驗', '萬芳與三軍總醫院', '常用檢驗的人工對應'), ('語意品質檢查', '經驗整理', '核對檢體與測量差異', '整理需專業審閱的疑義'), ('智慧候選推薦', '發展中', '搜尋與 AI 輔助選碼', '由專家確認對應結果'), ('跨院資料整合', '延伸方向', '維護版本與審閱依據', '延伸培養與藥敏資料')],
        'benefits': [('語意一致', '避免混用測量'), ('輔助對應', '聚焦候選代碼'), ('審閱可查', '保留判斷依據'), ('版本可管', '支援持續更新'), ('跨院研究', '建立資料基礎')],
        'vision': ['資料交換不失真', '研究與 AI 有根據'],
    },
}

ICONS = {
    'data': '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M3 9h18M9 9v12M12 13h6m-6 4h6"/>',
    'network': '<path d="m5 5 14 3-7 11L5 5l-1 12 15-9"/><circle cx="5" cy="5" r="2"/><circle cx="19" cy="8" r="2"/><circle cx="12" cy="19" r="2"/><circle cx="4" cy="17" r="2"/>',
    'check': '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="m7 12 3 3 7-7"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 6v6l4 3"/>',
    'search': '<circle cx="10" cy="10" r="7"/><path d="m15 15 6 6M6 10h8m-4-4v8"/>',
    'calendar': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M7 2v6m10-6v6M7 14h3m4 0h3m-10 4h3"/>',
    'growth': '<path d="M3 3v18h18M6 16l5-6 4 3 6-8m-5 0h5v5"/>',
    'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/><path d="m12 12 9-9"/>',
    'flag': '<path d="m2 22 8-12 5 7 3-4 4 9M10 10V2l10 2-10 3"/>',
}


def render(slug, directory):
    p = DATA[slug]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" role="img" aria-labelledby="title desc"><title id="title">{escape(p["title"])}</title><desc id="desc">研究方向、方法學、目前進展與成果，以及預期用途。成果卡標示已有基礎、開發或驗證狀態。</desc>',
           '<defs><filter id="shadow" x="-5%" y="-5%" width="110%" height="115%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#1B3A5C" flood-opacity=".045"/></filter></defs>',
           '<rect width="1920" height="1080" fill="white"/>',
           '<g fill="none" stroke="#E5F2F2" stroke-width="22"><path d="M-60 160Q90 190 160-50"/><path d="M1780-40Q1740 100 1970 120"/><path d="M-40 960Q130 920 190 1120"/><path d="M1760 1120Q1700 1000 1970 940"/></g>',
           '<g stroke="#DFE8F3" stroke-width="2" fill="#EDF3F9"><path d="m24 20 65 26 40-27m-40 27 31 55M1790 20l53 37 59-28m-59 28 49 59M25 1008l68 35 46-29m1620 18 66-34 67 40"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="6"/>' for x, y in [(24,20),(89,46),(129,19),(120,101),(1790,20),(1843,57),(1902,29),(1892,116),(25,1008),(93,1043),(139,1014),(1759,1032),(1825,998),(1892,1038)]) + '</g>']

    def text(x, y, value, size=24, color=NAVY, weight=400, anchor='start'):
        out.append(f'<text x="{x}" y="{y}" font-family="PingFang TC,Noto Sans TC,Microsoft JhengHei,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>')

    def rect(x, y, w, h, fill='white', stroke='#DFE6EC', shadow=False):
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{stroke}"' + (' filter="url(#shadow)"' if shadow else '') + '/>')

    def icon(x, y, name, color=NAVY, size=30):
        out.append(f'<g transform="translate({x} {y}) scale({size / 24})" fill="none" stroke="{color}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')

    text(960, 74, p['title'], 48, weight=750, anchor='middle')
    text(960, 122, p['subtitle'], 25, '#52687D', anchor='middle')
    text(52, 165, '研究方向導讀｜用什麼資料、採用什麼方法、如何驗證', 19, '#63778B')
    for i, (label, value, note) in enumerate(p['kpis']):
        x = 52 + i * 366
        rect(x, 180, 350, 146, shadow=True)
        icon(x + 20, 198, ['data', 'network', 'clock', 'check', 'search'][i], COLORS[i % 4], 28)
        text(x + 60, 222, label, 22, '#607488')
        text(x + 22, 268, value, 35, weight=750)
        text(x + 22, 303, note, 21, '#607488')

    for i, (title, subtitle, bullets) in enumerate(p['stages']):
        x = 52 + i * 464
        c = COLORS[i]
        rect(x, 350, 422, 346, shadow=True)
        rect(x + 20, 371, 53, 48, c, c)
        text(x + 46, 404, f'0{i + 1}', 26, 'white', 750, 'middle')
        text(x + 87, 404, title, 28, c, 750)
        text(x + 24, 451, subtitle, 22, '#6A7B8A')
        out.append(f'<path d="M{x+24} 470h374" stroke="#E7EDF1"/>')
        for j, bullet in enumerate(bullets):
            assert len(bullet) <= 12, bullet
            icon(x + 25, 492 + 46 * j, ['data', 'search', 'network', 'check'][j], c, 25)
            text(x + 67, 514 + 46 * j, bullet, 25)
        if i < 3:
            text(x + 443, 538, '›', 45, '#91A3B4', 500, 'middle')

    rect(52, 724, 178, 132, NAVY, NAVY)
    icon(72, 739, 'data', 'white', 30)
    text(72, 796, '進展與成果', 25, 'white', 700)
    text(72, 831, '目前做到哪裡', 20, '#DAE9F8')
    for i, (title, status, line1, line2) in enumerate(p['results']):
        x = 244 + i * 410
        rect(x, 724, 394, 132, '#F5F8FB')
        text(x + 376, 761, status, 18, COLORS[i], 650, 'end')
        text(x + 18, 761, title, 25, NAVY, 700)
        text(x + 18, 801, line1, 22, '#52687D')
        text(x + 18, 837, line2, 22, '#52687D')

    rect(52, 884, 178, 139, '#2BAA9E', '#2BAA9E')
    icon(72, 901, 'growth', 'white', 32)
    text(72, 960, '研究用途', 26, 'white', 700)
    text(72, 996, '預期貢獻', 21, 'white')
    for i, (name, note) in enumerate(p['benefits']):
        x = 244 + i * 274
        rect(x, 884, 258, 139)
        icon(x + 18, 903, ['search', 'check', 'network', 'data', 'growth'][i], COLORS[i%4], 27)
        text(x + 59, 927, name, 26, weight=700)
        text(x + 18, 978, note, 22, '#63778B')
    rect(1614, 884, 254, 139, NAVY, NAVY)
    icon(1634, 901, 'flag', 'white', 30)
    text(1679, 927, '願景', 27, 'white', 700)
    for j, line in enumerate(p['vision']):
        text(1634, 964 + j*33, line, 22, 'white')
    text(52, 1056, '林明錦｜臺北醫學大學 · 研究介紹 · 2026.09', 18, '#63778B')
    text(1868, 1056, FUNDING[slug]['short'], 18, '#63778B', anchor='end')
    out.append('</svg>')
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f'{slug}.svg'
    path.write_text('\n'.join(out))
    return path
