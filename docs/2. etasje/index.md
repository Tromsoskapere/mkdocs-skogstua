# 2. etasje

<ul>
  {% for subpage in page.children %}
    {# subpage.meta.title vil nå fungere! #}
    <li><a href="{{ subpage.url }}">{{ subpage.meta.title or subpage.file.name }}</a></li>
  {% endfor %}
</ul>

![Plantegning](Skogstua_2etg.png)

Warhammer-klubben Frostlord Wargaming disponerer et eget rom for spilling.



