import os
import requests
from datetime import datetime

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
PAGE_ID = os.getenv("NOTION_PAGE_ID")

url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data = {
    "children": [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {"type": "text", "text": {"content": f"更新时间：{now}"}}
                ]
            },
        }
    ]
}

r = requests.patch(url, headers=headers, json=data)
r.raise_for_status()
print("已推送到 Notion：", now)
