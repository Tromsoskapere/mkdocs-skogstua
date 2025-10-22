# Maskinhall
Inventarliste. Hele Kategori "Maskinhall" er et testområde.

Her er en macro test

<ul>
{% for subpage in page.children %}
    <li>
        <strong>TITTEL-DEBUG:</strong>
        <ul>
            <li>subpage.title (fra nav:): [{{ subpage.title }}]</li>
            <li>subpage.meta.title (fra front-matter): [{{ subpage.meta.title }}]</li>
            <li>subpage.file.name (filnavn): [{{ subpage.file.name }}]</li>
        </ul>
        <hr>
        <strong>Endelig lenke:</strong>
        <a href="{{ subpage.url }}">{{ subpage.title or subpage.file.name }}</a>
    </li>
{% endfor %}
</ul>
