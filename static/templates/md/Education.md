<table>
{% for edu in educations %}

<tr>
    <td>
        <img align="center" width='40px' src="static/{{ educations[edu]['University']['Logo'] }}">
    </td>
    <td>
        {{ educations[edu]['Year'] }}
    </td>
    <td>
        <b>{{ educations[edu]['University']['Name'] }}</b>, {{ educations[edu]['University']['Country'] }} <br>
        {{ edu }} in {{ educations[edu]['Major']['Name'] }}
    </td>
    <td>{{ educations[edu]['Major']['Others'] }}</td>
</tr>

{% endfor %}
</table>