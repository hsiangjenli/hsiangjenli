<table>

<tr>
    <td><b>Host</b></td>
    <td><b>Year</b></td>
    <td><b>Competition Name</b></td>
    <td><b>Ranking</b></td>
</tr>

{% for award in awards %}
    {% set award_image = is_abs_url( awards[award]['basic_info']['image'], static ) %}

<tr>
    <td> <img width='40px' style='min-width: 40px' src="{{ award_image }}"> </td>
    <td> {{ awards[award]['basic_info']['year'] }} </td>
    <td> <b> {{ awards[award][language]['host'] }} </b><br>{{ awards[award][language]['title'] }} </td>
    <td> {{ awards[award][language]['ranking'] }} </td>

</tr>


{% endfor %}

</table>