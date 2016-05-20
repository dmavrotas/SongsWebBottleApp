% rebase('layout.tpl', title=title, year=year)

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
    <table width="100%" height="100%" border='0' align="center">
        <tr>
            <td>
                <h2>Presentation of Artists</h2>
                <form>
                    Name: <input type="text" class="toNavigate" name="name" /><br />
                    Surname: <input type="text" class="toNavigate" name="surname" /><br />
                    Birth Year - From: <input type="text" class="toNavigate" name="byfrom" /><br />
                    Birth Year - To: <input type="text" class="toNavigate" name="byto" /><br />
                    <select id="artisttypes" class="toNavigate">
                        <option value="1">Singer</option>
                        <option value="2">Song Writer</option>
                        <option value="3">Composer</option>
                    </select> <br />
                    <input type="button" name="button" value="Submit" onClick="submitForm(this.form, 'artistsview')" /> 
                </form>
            </td>
        </tr>
    </table>
</body>
</html>
