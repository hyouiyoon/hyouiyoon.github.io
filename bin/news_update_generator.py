#!/usr/bin/env python3

import argparse
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List


TEMPLATES: Dict[str, Dict[str, Dict[str, List[str]]]] = {
    "en": {
        "publication": {
            "title": [
                "Publication Update: {subject}",
                "New Paper Published: {subject}",
                "Research Publication: {subject}",
            ],
            "description": [
                "Our work was published in {venue}.",
                "This study has been published through {venue}.",
                "The paper is now available in {venue}.",
            ],
        },
        "scholarship": {
            "title": [
                "Scholarship Awarded: {subject}",
                "Scholarship Announcement: {subject}",
                "Funding Update: {subject}",
            ],
            "description": [
                "Received the {subject}{org_phrase}.",
                "I was selected for the {subject}{org_phrase}.",
                "Honored to receive the {subject}{org_phrase}.",
            ],
        },
        "award": {
            "title": [
                "Award Received: {subject}",
                "Research Award: {subject}",
                "Achievement Update: {subject}",
            ],
            "description": [
                "Received the {subject}{venue_phrase}.",
                "I was honored with the {subject}{venue_phrase}.",
                "Awarded the {subject}{venue_phrase}.",
            ],
        },
        "presentation": {
            "title": [
                "Presentation Update: {subject}",
                "Conference Presentation: {subject}",
                "Talk Delivered: {subject}",
            ],
            "description": [
                "Presented this work at {venue}.",
                "Gave a presentation on {subject} at {venue}.",
                "Shared recent research results at {venue}.",
            ],
        },
        "media": {
            "title": [
                "Media Feature: {subject}",
                "Research Highlight: {subject}",
                "Public Outreach Update: {subject}",
            ],
            "description": [
                "This work was featured by {org}.",
                "The project was highlighted on {org}.",
                "A feature article on this work was published by {org}.",
            ],
        },
        "activity": {
            "title": [
                "Lab Update: {subject}",
                "Research Activity: {subject}",
                "Academic Update: {subject}",
            ],
            "description": [
                "Shared an update on {subject}.",
                "Completed an important milestone related to {subject}.",
                "Recorded a recent activity about {subject}.",
            ],
        },
    },
    "ko": {
        "publication": {
            "title": [
                "논문 소식: {subject}",
                "신규 논문 게재: {subject}",
                "연구 성과 게재: {subject}",
            ],
            "description": [
                "{venue}에 본 연구가 게재되었습니다.",
                "해당 연구가 {venue}를 통해 공개되었습니다.",
                "{venue}에서 연구 결과를 확인하실 수 있습니다.",
            ],
        },
        "scholarship": {
            "title": [
                "장학금 수혜: {subject}",
                "장학 소식: {subject}",
                "연구지원 선정: {subject}",
            ],
            "description": [
                "{org_phrase_ko}{subject}에 선정되었습니다.",
                "{subject}{org_suffix_ko}수혜자로 선정되었습니다.",
                "{subject}{org_suffix_ko}받게 되었습니다.",
            ],
        },
        "award": {
            "title": [
                "수상 소식: {subject}",
                "연구 수상: {subject}",
                "성과 소식: {subject}",
            ],
            "description": [
                "{venue_phrase_ko}{subject}을(를) 수상했습니다.",
                "{subject}{venue_suffix_ko}수상했습니다.",
                "{venue_phrase_ko}{subject} 수상자로 선정되었습니다.",
            ],
        },
        "presentation": {
            "title": [
                "발표 소식: {subject}",
                "학술 발표: {subject}",
                "연구 발표 업데이트: {subject}",
            ],
            "description": [
                "{venue}에서 관련 연구를 발표했습니다.",
                "{venue}에서 {subject} 주제로 발표를 진행했습니다.",
                "{venue}에서 최근 연구 결과를 공유했습니다.",
            ],
        },
        "media": {
            "title": [
                "언론/홍보 소식: {subject}",
                "연구 소개: {subject}",
                "대외 소개 업데이트: {subject}",
            ],
            "description": [
                "{org}에서 본 연구를 소개했습니다.",
                "{org}에 연구 내용이 소개되었습니다.",
                "{org}를 통해 연구 소식이 게재되었습니다.",
            ],
        },
        "activity": {
            "title": [
                "연구실 소식: {subject}",
                "학업/연구 활동: {subject}",
                "근황 업데이트: {subject}",
            ],
            "description": [
                "{subject} 관련 활동을 진행했습니다.",
                "{subject}와 관련된 주요 마일스톤을 달성했습니다.",
                "{subject}에 대한 최근 활동 내용을 정리했습니다.",
            ],
        },
    },
}


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([.,!?])", r"\1", text)
    return text


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug or "news-item"


def render_templates(
    language: str,
    event_type: str,
    subject: str,
    venue: str,
    org: str,
    variants: int,
) -> List[Dict[str, str]]:
    selected = TEMPLATES[language][event_type]
    payload = {
        "subject": subject,
        "venue": venue or "the event",
        "org": org or "the organization",
        "venue_phrase": f" at {venue}" if venue else "",
        "venue_suffix_ko": f" ({venue}) " if venue else " ",
        "venue_phrase_ko": f"{venue}에서 " if venue else "",
        "org_phrase": f" from {org}" if org else "",
        "org_suffix_ko": f" ({org}) " if org else " ",
        "org_phrase_ko": f"{org}의 " if org else "",
    }

    outputs = []
    for i in range(variants):
        title_tpl = selected["title"][i % len(selected["title"])]
        desc_tpl = selected["description"][i % len(selected["description"])]
        title = clean_text(title_tpl.format_map(payload))
        description = clean_text(desc_tpl.format_map(payload))
        outputs.append({"title": title, "description": description})
    return outputs


def frontmatter_quote(value: str) -> str:
    return value.replace('"', "'")


def build_markdown(
    title: str,
    date: str,
    description: str,
    img: str,
    link: str,
    link_text: str,
) -> str:
    lines = [
        "---",
        "layout: post",
        f'title: "{frontmatter_quote(title)}"',
        f"date: {date}",
        f'img: {img}',
        f'description: "{frontmatter_quote(description)}"',
    ]
    if link:
        lines.append(f"link: {link}")
        lines.append(f'link_text: "{frontmatter_quote(link_text)}"')
    lines.append("---")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate reusable website news copy and optional Jekyll news markdown."
    )
    parser.add_argument(
        "--event-type",
        required=True,
        choices=["publication", "scholarship", "award", "presentation", "media", "activity"],
    )
    parser.add_argument("--subject", required=True, help="Main subject (paper title, award name, etc.).")
    parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD format.")
    parser.add_argument("--venue", default="", help="Conference, journal, or event name.")
    parser.add_argument("--org", default="", help="Organization or institution name.")
    parser.add_argument("--lang", choices=["en", "ko"], default="en")
    parser.add_argument("--variants", type=int, default=3, help="Number of text variants to generate.")
    parser.add_argument("--pick", type=int, default=1, help="Variant number to use for markdown output.")
    parser.add_argument("--img", default="assets/img/news/1.jpg")
    parser.add_argument("--link", default="")
    parser.add_argument("--link-text", default="Link")
    parser.add_argument("--slug", default="", help="Optional filename slug.")
    parser.add_argument("--write-file", action="store_true", help="Write markdown file into _news/<year>/.")
    parser.add_argument("--output", default="", help="Optional output markdown path.")
    args = parser.parse_args()

    datetime.strptime(args.date, "%Y-%m-%d")
    variants = max(1, min(args.variants, 10))
    picks = render_templates(
        language=args.lang,
        event_type=args.event_type,
        subject=args.subject,
        venue=args.venue,
        org=args.org,
        variants=variants,
    )

    print("Generated text variants:")
    for idx, item in enumerate(picks, start=1):
        print(f"[{idx}] Title: {item['title']}")
        print(f"    Description: {item['description']}")

    pick_idx = min(max(args.pick, 1), len(picks)) - 1
    chosen = picks[pick_idx]
    markdown = build_markdown(
        title=chosen["title"],
        date=args.date,
        description=chosen["description"],
        img=args.img,
        link=args.link,
        link_text=args.link_text,
    )

    print("\nSelected markdown:\n")
    print(markdown)

    if args.write_file:
        year = args.date.split("-")[0]
        slug = args.slug or f"{args.date}-{slugify(args.subject)}"
        output_path = Path(args.output) if args.output else Path(f"_news/{year}/{slug}.md")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
        print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
