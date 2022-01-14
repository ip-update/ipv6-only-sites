---
---

{% include_relative README.md %}

<h1>IPv6 only sites</h1>
Generated at {{ site.time | date: '%Y-%m-%d %H:%M:%S %Z' }}<br />
<table>
  {% for v6site in site.data.v6onlysites %}
    <tr>
    <td><a href="{{ v6site.url }}">{{ v6site.site }}</a></td>
    <td>{{ v6site.description }}</td>
    </tr>
  {% endfor %}
</table>