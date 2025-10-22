# Maskinhall
Inventarliste. Hele Kategori "Maskinhall" er et testområde.

Her er en macro test

<ul>
  {# Loop gjennom nav-elementene, ikke page-objektene #}
  {% for nav_item in page.nav.children %}
    <li>
      {# nav_item.title har den riktige tittelen fra mkdocs.yml #}
      {# nav_item.url har den riktige lenken #}
      <a href="{{ nav_item.url }}">{{ nav_item.title }}</a>
    </li>
  {% endfor %}
</ul>
