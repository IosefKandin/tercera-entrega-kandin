{% extends 'base.html' %}

{% block title %}
    Registrar profesor
{% endblock %}

{% block content %}
    <h1>Registrar profesor</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
