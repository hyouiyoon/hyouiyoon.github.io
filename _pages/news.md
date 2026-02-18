---
layout: page
title: News
permalink: /news/
nav: true
nav_order: 4
description: 
---

<div class="publications">
  {% assign sorted_news = site.news | sort: "date" | reverse %}
  {% assign current_year = "" %}
  {% for item in sorted_news %}
    {% assign item_year = item.date | date: "%Y" %}
    {% if item_year != current_year %}
      {% if current_year != "" %}
        </ol>
      {% endif %}
      <h2 class="bibliography">{{ item_year }}</h2>
      <ol class="bibliography">
      {% assign current_year = item_year %}
    {% endif %}
    <li>{% include news_item.liquid %}</li>
  {% endfor %}
  {% if current_year != "" %}
    </ol>
  {% endif %}
</div>
