<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
        <title>Odometer — Transition numbers with ease</title>
        <link rel="icon" href="http://static.hubspot.com/favicon.ico">
        <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/modernizr/2.6.2/modernizr.min.js"></script>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        <script src="http://github.hubspot.com/odometer/odometer.js"></script>
        <link rel="stylesheet" href="https://raw.github.com/HubSpot/odometer/master/themes/odometer-theme-train-station.css" />
        <script>
            $(function(){
                var starsOdometer = new Odometer({ el: $('.counter')[0], theme: 'train-station', value: '0' });
                starsOdometer.render();
                starsOdometer.update({{ count }});
                var token = "{{ token }}";
                // TODO update peroid by token
            });
        </script>
    </head>
    <body>
        <h1>#piccollage on Instagram</h1>   
        <div class="counter" style="font-size: 200;" />
    </body>
</html>