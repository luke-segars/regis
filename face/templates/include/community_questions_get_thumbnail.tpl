{% comment %} 
question_thumbnail.tpl is intended to be injected into a web page.

Requires:
questionstatus
questionnumber (actually template.id)
questioncontent
questionpublished
hintids

{% endcomment %}
<div id="question{{ questionnumber }}" class="question_container">
  <div class="qbox">
    {% if questionstatus == 'released' %}
      <div class="q_decoration q_unanswered">
        <p class="q_status">unanswered</p>
        <p>answered by 2 of 8</p>
        <p>( 25% )</p>
      </div>
    {% endif %}
    {% if questionstatus == 'answered' %}
      <div class="q_decoration q_answered">
        <p class="q_status">answered</p>
        <p>answered by 2 of 8</p>
        <p>( 25% )</p>
      </div>
    {% endif %} 
    
    <div>
      {% if questionstatus == 'ready' or questionstatus == 'pending' %}
        <h2 class="qbox_head">
          Question #{{ questionnumber }}
        </h2>
        <p class="qbox_preview" style="font-style: italic">This question isn't available yet.</p>
      {% else %}
        <h2 class="qbox_head"><a href="{{questionnumber}}">Question #{{ questionnumber }}</a></h2>
        {% if questioncontent|length > 60 %}
          <p class="qbox_preview">{{ questioncontent|slice:":200" }}...</p>
        {% else %}
          <p class="qbox_preview">{{ questioncontent }}</p>
        {% endif %}
      {% endif %}
      
  
    </div>
  </div>
</div>
