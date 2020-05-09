---
layout: page
title: Summaries
permalink: /summaries/
---

## Summaries of papers

<div class="posts">
    <ul>
        {% assign papers = site.summaries | where: "read",true | sort: "readings" | reverse %}
        {% for paper in papers %}
            <li>{{ paper.title }} [<a href="{{ site.baseurl }}{{ paper.url }}">{{ paper.slug }}</a>]</li>
        {% endfor %}
    </ul>
</div>

## Backlog of papers to summarize

<div class="posts">
    <ul>
        {% assign papers = site.summaries | where: "read",false | sort: "added" | reverse %}
        {% for paper in papers %}
            <li>{{ paper.title }} [<a href="{{ site.baseurl }}{{ paper.url }}">{{ paper.slug }}</a>]</li>
        {% endfor %}
    </ul>
</div>
