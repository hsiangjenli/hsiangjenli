{% set author_profile = is_abs_url( author['profile'], static ) %}
{% set author_name_pronunciation = is_abs_url( author['name']['others']['chinese']['pronunciation'], static ) %}

<center>
<div align="center">  
<img width="150px" src="{{ author_profile }}">

# **{{ author['name']['english'] }}** <small> {{ author['name']['nick_name'] }} </small>

<img height="45px" src="{{ author_name_pronunciation }}">

<a href="mailto: {{ author['mail'] }}">
    
**{{ author['mail'] }}**

</a>
</div>
</center>