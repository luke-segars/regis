<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <link rel="stylesheet" type="text/css" href="/static/css/main.css" />
  <link href='http://fonts.googleapis.com/css?family=Pontano+Sans' rel='stylesheet' type='text/css'>
  <script type="text/javascript" src="/static/js/underscore.js"></script>
  <script type="text/javascript" src="/static/js/jquery.js"></script>
  <script type="text/javascript" src="/static/js/backbone.js"></script>
  <script type="text/javascript" src="/static/js/regis/regis.js"></script>

  <script type="text/javascript">
    $(document).ready(function() {
      // Initialize Regis and get some decks.
      regis_init();
      deck = regis.Deck('Home', 'home');
      
      // Activate a deck after some time has passed.  This should be
      // converted to an event eventually.
      setTimeout(function() { regis.activateDeck(deck); }, 500);
    });
  </script>

  <title>Welcome to codepath!</title>
  {% include 'include/common_header.tpl' %}
</head>
<body>
  <div id='main-display'>
    <h1 id="codepath-title"><span class="cp_first">code</span><span class="cp_second">path</span></h1>
    <div id="navigation">
<!--         <div id="profile_btn"><img src="/static/img/profile.png" />profile</div> -->
    </div>
    <div id='card-stack'>
    </div>
    
  </div>
    <div id='deck-icons' class="ui-layout-south"></div>
<!---
  <div id="" class="ui-layout-south">
    <ul id="deck-bench">
      <li class="deck-icon" style="display:inline; margin-right:10px;">All (37)</li>
      <li class="deck-icon" style="display:inline; margin-right:10px;">Instructor (12)</li>
      <li class="deck-icon" style="display:inline; margin-right:10px;">Unanswered (2)</li>
      <li class="deck-icon" style="display:inline; margin-right:10px;">Midterm Review (8)</li>
      <li class="deck-icon" style="display:inline; margin-right:10px;">Final Review (1)</li>	
      <li class="deck-icon" style="display:inline; margin-right:10px;">My Questions (2)</li>	
    </ul>
  </div>
-->
</body>
</html>
