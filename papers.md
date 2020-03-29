---
layout: page
title: Publications
permalink: /papers/
---

* Table of contents
{:toc}

My [Google Scholar](https://scholar.google.co.uk/citations?hl=en&user=oT8RhJgAAAAJ),
[DBLP](http://dblp.uni-trier.de/pers/hd/r/Reid:Alastair_David),
[ORCID](https://orcid.org/0000-0003-4695-6668) and
[Microsoft Academic](https://academic.microsoft.com/#/detail/2293162450)
pages.

## Papers

<table class="papers">
{% for paper in site.data.biblio %}
    <tr valign="top">
        <td align="right" class="bibtexnumber" style="padding: 3px;">
            <a class="papertitle" href="{{ site.baseurl }}/papers/{{ paper.ar_file }}">{{ paper.ar_shortname | replace:' ','&nbsp;'}}</a>
        </td>
        <td class="bibtexitem">
            {{ paper.ar_title }}
        </td>
    </tr>
{% endfor %}
</table>


## Talks

In my personal site, this page contains a list of public talks, links to the
slides and video, etc.

## Patents

<table class="papers">
{% for paper in site.data.patents %}
    <tr valign="top">
        <td align="right" class="bibtexnumber" style="padding: 3px;">
            {% if paper.link %}
                <a class="papertitle" href="{{ paper.link }}">{{ paper.number | replace:' ','&nbsp;'}}</a>
            {% else %}
                {{ paper.number | replace:' ','&nbsp;'}}
            {% endif %}
        </td>
        <td class="bibtexitem">
            {{ paper.title }}
            <br>
            {{ paper.author }},
            {{ paper.location }}
            {{ paper.type }},
            {{ paper.month }}
            {{ paper.year }}
        </td>
    </tr>
{% endfor %}
</table>
