# Maskinhall
Inventarliste. Hele Kategori "Maskinhall" er et testområde.

Her er en macro test

<ul>
  {% for subpage in page.children %}
    {# subpage.meta.title vil nå fungere! #}
    <li><a href="{{ subpage.url }}">{{ subpage.meta.title or subpage.file.name }}</a></li>
  {% endfor %}
</ul>
