% rebase('layout.tpl', title=title, year=year)

<html>
<head>
    <title>Update &amp; Search Artists</title>
</head>
<body>
    <table width="100%" height="100%" border='0' align="center">
        <tr>
            <td>
                <h2>Update &amp Search Artists</h2>
                <form>
                    Plane id            : <input type="text" class="toSubmit" name="pid" /><br />
                    Departure Airport id: <input type="text" class="toSubmit" name="did" /><br />
                    Arrival Airport id  : <input type="text" class="toSubmit" name="aid" /><br />
                    Date                : <input type="text" class="toSubmit" name="date" /><br />
                    flight id           : <input type="text" class="toSubmit" name="fid" /><br />

                    <input type="button" name="button" value="Insert" onClick="submitForm(this.form, 'insertData')" />
                </form>
            </td>
        </tr>
    </table>
</body>
</html>
