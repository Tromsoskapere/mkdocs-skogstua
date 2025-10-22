# Maskinhall
Inventarliste. Hele Kategori "Maskinhall" er et testområde.

Her er en macro test

<ul>
  {% for subpage in page.children %}
    <li><a href="{{ subpage.file.name }}/">{{ meta.subpage.title or subpage.file.name }}</a></li>
  {% endfor %}
</ul>
