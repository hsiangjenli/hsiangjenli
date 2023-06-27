<table>
<tr>
    <td><b>Period</b></td>
    <td><b>Name</b></td>
    <td><b>Tags</b></td>
    <td><b>Documentation</b></td>
</tr>
{% for project in projects %}
<tr>

<td>{{ projects[project]['basic_info']['period_start'] }} ~ {{ projects[project]['basic_info']['period_end'] }}</td>
<td>{{ projects[project][language]['project_name'] }}</td>
<td>

{% for tag in projects[project]['basic_info']['tags'] %}`{{ tag }}` {% endfor %}

</td>
<td>{% if projects[project]['basic_info']['external_link'] %} <a href="{{ projects[project]['basic_info']['external_link'] }}"> 🌐 </a> {% endif %}</td>

</tr>
{% endfor %}
</table>