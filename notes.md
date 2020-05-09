---
layout: page
title: Notes
permalink: /notes/
---

<div class="posts">
    <ul>
        {% for note in site.notes %}
            <li><a href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a></li>
        {% endfor %}
    </ul>
</div>
