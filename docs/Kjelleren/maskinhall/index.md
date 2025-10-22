# Maskinhall
Inventarliste. Hele Kategori "Maskinhall" er et testområde.

Her er en macro test

<ul>
{% for subpage in page.children %}
    {# Bare bruk subpage.url direkte #}
    <li><a href="{{ subpage.url }}">{{ subpage.title }}</a></li>
{% endfor %}
</ul>
