---
---

{% include_relative README.md %}

<h1>IPv6 only sites</h1>
Generated at {{ site.time | date: '%Y-%m-%d %H:%M:%s' }}<br />
<table>
  {% for v6site in site.data.v6onlysites %}
    <tr>
    {% for col in v6site %}
      <td>
        {{ col }}
      </td>
    {% endfor %}
    </tr>
  {% endfor %}
</table>