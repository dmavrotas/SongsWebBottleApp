% rebase('layout.tpl')

<html>
<head>
    <title>Presentation of Artists</title>
    <script>
            function submitForm(form, method) {
                var vals = [];

                for (var n=0; n < form.elements.length; n++) {
                    if(form.elements[n].className === 'toNavigate') {
                        vals.push(form.elements[n].name + "=" + form.elements[n].value);
                    }
                }
                window.parent.document.getElementById('results').contentWindow.location = method + "?" + vals.join("&");
            }
    </script>
</head>
<body>
    <h2>Presentation of Artists</h2>
    <form action="/artists" method="get"/>
    <table width="50%" height="100%" border='0' align="center">
        <tr>
            <td>Name:</td>
            <td> <input id="nameid" type="text" class="toNavigate" name="name" /> </td>
        </tr>
        <tr>
            <td>Surname:</td>
            <td> <input id="surnameid" type="text" class="toNavigate" name="surname" /> </td>
        </tr>
        <tr>
            <td>Birth Year - From:</td>
            <td> <input id="bdfid" type="text" class="toNavigate" name="byfrom" /> </td>
        </tr>
        <tr>
            <td>Birth Year - To:</td>
            <td> <input id="bdtid" type="text" class="toNavigate" name="byto" /> </td>
        </tr>
        <tr>
            <td>Type</td>
            <td>
                <select id="atid" name="artisttype" class="toNavigate">
                    <option value="1">Singer</option>
                    <option value="2">Song Writer</option>
                    <option value="3">Composer</option>
                </select>
            </td>
        </tr>
    </table>
    <br/>
    <br/>
    <div style="text-align:center">
        <!--<a class="btn btn-default" href="\artistsview">Submit &raquo;</a>-->
        <input type="submit" name="submitNew" value="submitNew"/>
    </div>
</body>
</html>
