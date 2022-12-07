# 主畫面中的「介紹與說明」進去後的畫面
introduction_message = {
    "type": "bubble",
    "size": "giga",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "功能介紹",
                "weight": "bold",
                "size": "lg",
                "margin": "lg",
                "align": "center"
            },
            {
                "type": "text",
                "text": "★　快速查詢日幣匯率的小幫手",
                "wrap": True
            },
            {
                "type": "text",
                "text": "★　數據–臺灣銀行即時爬取",
                "wrap": True
            },
            {
                "type": "text",
                "text": "●　查詢即時匯率（買賣）",
                "wrap": True
            },
            {
                "type": "text",
                "text": "●　查詢近期走勢（近3月／2週）",
                "wrap": True
            },
            {
                "type": "text",
                "text": "●　推薦兌幣程度（低／中／高）",
                "wrap": True
            },
            {
                "type": "text",
                "text": "使用說明",
                "weight": "bold",
                "size": "lg",
                "margin": "lg",
                "align": "center"
            },
            {
                "type": "text",
                "text": "◎　輸入「主選單」來開始所有操作",
                "wrap": True
            },
            {
                "type": "text",
                "text": "　　(也可由下方列選單點選快捷鍵)",
                "wrap": True
            },
            {
                "type": "text",
                "text": "◎　其餘依照按鈕提示進行點選即可",
                "wrap": True
            },
            {
                "type": "text",
                "text": "◎　主選單請拖曳後橫向(左右)滑動",
                "wrap": True
            }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "button",
                "style": "primary",
                "action": {
                    "type": "message",
                    "label": "返回主選單",
                    "text": "主選單"
                }
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}
