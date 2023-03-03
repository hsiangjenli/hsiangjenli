<table>
<tr>
    <td><b>Year</b></td>
    <td><b>Name</b></td>
    <td><b>Tags</b></td>
    <td><b>Documentation</b></td>
</tr>
{% for project in projects %}
<tr>

<td>{{ projects[project]['Year'] }}</td>
<td>{{ projects[project]['Name'] }}</td>
<td>

{% for tag in projects[project]['Tags'] %}`{{ tag }}` {% endfor %}

</td>
<td>{% if projects[project]['Documentation'] %} <a href="{{ projects[project]['Documentation'] }}"> 🌐 </a> {% endif %}</td>

</tr>
{% endfor %}
</table>