# Maskinhall
Inventarliste. Hele Kategori "Maskinhall" er et testområde.

Her er en macro test

<ul>
{% for subpage in page.children %}
    <li><a href="{{ subpage.url | url }}">{{ subpage.title }}</a></li>
{% endfor %}
</ul>
