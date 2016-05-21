% rebase('layout.tpl')

<html>
<body>
    <h2>Insert Song</h2>
    <form action="/insertsong" method="get"/>
    <table width="50%" height="100%" border='0' align="center">
        <tr>
            <td>Title:</td>
            <td> <input id="titleid" type="text" class="toNavigate" name="title" /> </td>
        </tr>
        <tr>
            <td>Production Year:</td>
            <td> <input id="pyid" type="text" class="toNavigate" name="prodyear" /> </td>
        </tr>
        <tr>
            <td>CD:</td>
            <td>
                <select id="cdid" name="cd" class="toNavigate">
                    %for cd in cds:
                    <option value="{{cd}}" >{{cd}}</option>
                    %end
                </select>  
            </td>
        </tr>
        <tr>
            <td>Singer:</td>
            <td>
                <select id="singerid" name="singer" class="toNavigate">
                    %for cd in cdsingers:
                    <option value="{{cd}}">{{cd}}</option>
                    %end
                </select> 
            </td>
        </tr>
        <tr>
            <td>Composer:</td>
            <td>
                <select id="composerid" name="composer" class="toNavigate">
                    %for cd in cdcomposers:
                    <option value="{{cd}}">{{cd}}</option>
                    %end
                </select>
            </td>
        </tr>
        <tr>
            <td>Song Writer:</td>
            <td>
                <select id="songwriterid" name="songwriter" class="toNavigate">
                    %for cd in cdsongwriters:
                    <option value="{{cd}}">{{cd}}</option>
                    %end
                </select>
            </td>
        </tr>
    </table>
    <br/>
    <br/>
    <div style="text-align:center">
        <input type="submit" name="submitNew" value="Submit"/>
    </div>
</body>
</html>
